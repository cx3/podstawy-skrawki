import os
import threading
import time
from datetime import datetime
from dateutil import parser


def get_file_data(filepath):
    file_info = {}
    try:
        filepath = filepath.replace('\\', '/')
        stat_info = os.stat(filepath)
        file_info['path'] = filepath
        file_info['name'] = filepath.split('/')[-1]
        file_info['size'] = stat_info.st_size
        file_info['created_at'] = datetime.fromtimestamp(stat_info.st_ctime).isoformat()
        file_info['permissions'] = stat_info.st_mode
        file_info['extension'] = os.path.splitext(filepath)[1]  # path, name, size, created_at, permissions, extensions, actions
        return file_info
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
        return None


def match_query(file_info, **use_filters):
    matches = 0
    for key, value in use_filters.items():
        if key == 'starts_with':
            if file_info['name'].startswith(value):
                matches += 1
        if key == 'ends_with':
            if file_info['name'].endswith(value):
                matches += 1
        if key == 'partial_name':
            if value in file_info['name']:
                matches += 1
        if key == 'min_size':
            if int(file_info['size']) >= int(value):
                matches += 1
        if key == 'max_size':
            if int(file_info['size']) <= int(value):
                matches += 1
        '''if key == 'created_after':
            
        if key == 'created_before':
        if key == 'extension':'''

    return True if matches >= len(use_filters) else False


class FileSearcher:
    def __init__(self, root_dir, **query):
        self.root_dir = root_dir
        self.query = query
        self.result = []
        self.current_index = 0
        self.search_thread = threading.Thread(target=self._search_files)
        self.search_thread.start()
        time.sleep(0.25)

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if start is None:
                start = 0
            if stop is None:
                stop = len(self.result)
            return self.result[start:stop:step]
        else:
            return self.result[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.result):
            result = self.result[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration()

    def __len__(self):
        return len(self.result)

    def _search_files(self):

        filters = [
            'starts_with', 'ends_with', 'partial_name', 'min_size', 'max_size', 'created_after', 'created_before',
            'extension'
        ]

        use_filters = {}

        for key, value in self.query.items():
            if key in filters and value != '':
                use_filters[key] = value

        iters = 0
        for dirs, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                filepath = os.path.join(dirs, filename)
                file_data = get_file_data(filepath)
                iters += 1
                if match_query(file_data, **use_filters):
                    self.result.append(file_data)
                    if len(self.result) % 100 == 0:
                        socketio.emit('next_hundred_found', {
                            'found': len(self.result) // 100, 'iters': iters}
                        )
        socketio.emit('search_finished', {'len': len(self.result)})

    def wait_until_finished(self):
        self.search_thread.join()

    def is_finished(self):
        return not self.search_thread.is_alive()


def filter_results(results, **kwargs):
    return [file for file in results if match_query(file, **kwargs)]


def sort_results(results, **kwargs):
    def _get_sort_key(file_info, **sort_params):
        # Możesz dostosować logikę sortowania do swoich potrzeb
        sort_key = []
        for key, reverse in sort_params.items():
            if key == 'size':
                sort_key.append((file_info.get(key, 0), reverse))
            elif key == 'created_at':
                sort_key.append((file_info.get(key, datetime.min), reverse))
            # Dodaj inne kryteria sortowania według potrzeb
        return tuple(sort_key)

    if kwargs:
        results.sort(key=lambda file_info: _get_sort_key(file_info, **kwargs))
    return results


def test():
    # Przykład użycia
    searcher = FileSearcher(root_dir="c:/STABLED/")
    searcher.wait_until_finished()

    # Sortowanie i filtrowanie wyników
    sorted_searcher = searcher.sort_results(size=True, created_at=False)
    filtered_sorted_searcher = sorted_searcher.filter_results(created_after="2023-01-01", extension=".txt")

    print(f"Liczba znalezionych plików po sortowaniu i filtrowaniu: {len(filtered_sorted_searcher)}")
    print("Wyniki:")
    print(filtered_sorted_searcher[:10])  # Wyświetlenie pierwszych 10 wyników


    # Grouping results
    grouped_result = filtered_sorted_searcher.group_results('extension', 'size')
    for group_key, group_files in grouped_result.items():
        print(f"Group: {group_key}")
        for file_info in group_files:
            print(file_info)


####################################################################################3333333

import os
import platform
import mimetypes
from datetime import datetime

from flask import Flask, jsonify, request, render_template, send_file, url_for, redirect, session
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
socketio = SocketIO(app)


@app.route('/search', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        if len(request.args) == 0:
            return render_template('advanced_search_form.html')
        return redirect(url_for('results_route', **request.args.to_dict()))


@app.route('/search/results')
def results_route():
    print("RESULTS!", request.path)

    if not request.args:
        return redirect(url_for('index'))
    return render_template('advanced_search_form_results.html')


@socketio.on('search_files')
def handle_search_files(data):
    root_dir = data.get('root_dir', os.getcwd())
    search_params = data.get('search_params', {})
    print("@socketio.on   search_params: ", search_params)

    file_searcher = FileSearcher(**search_params)
    session['file_searcher'] = file_searcher

    page = 1  # data.get('page', 1)
    items_per_page = 100
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    if end_index > len(file_searcher):
        end_index = len(file_searcher)
    paginated_results = file_searcher[start_index:end_index]

    emit('search_results', {'results': paginated_results})


@socketio.on('get_page')
def handle_get_page(data):
    page = int(data.get('page', 1))
    items_per_page = 100
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    x = session['file_searcher']

    if end_index > len(x):
        end_index = len(x)
    paginated_results = x[start_index:end_index]

    emit('render_new_page', {'results': paginated_results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)