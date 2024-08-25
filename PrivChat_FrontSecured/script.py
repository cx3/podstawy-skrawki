from os import urandom

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send, join_room

from ChatUtils import RoomUser, ChatRooms

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(64).hex()
socketio = SocketIO(app)
created_rooms = ChatRooms()


@app.route('/', methods=['GET'])
def index_route():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login_route():

    # client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        room_name = request.form.get('roomname', False)
        user_name = request.form.get('username', False)
        passwd = request.form.get('password', False)

        if room_name and user_name and passwd:
            print('all fileds ok')
            user = RoomUser(user_name, request.remote_addr)
            if created_rooms.join_user_to_room(user, room_name, passwd):

                print('user joined, redirect to chat')
                return f"""
                <script>
                   window.location.href="/chat/{room_name}";
                </script>
                """
            else:
                return render_template('login.html', error="Username busy or incorrect password")
        else:
            return render_template('login.html', error="Fill all fields")


@app.route('/chat/<room_name>', methods=['POST', 'GET'])
def chat_room_route(room_name: str):
    print('in chat/<room_name>  route')
    if created_rooms.is_ip_in_room(request.remote_addr, room_name):
        print('if ip in room - show chat')
        user_name = created_rooms.name_by_ip_in_room(room_name, request.remote_addr)
        return render_template('chat.html', room_name=room_name, user_name=user_name)

    print('ip not in room, redirect to login')
    return redirect(url_for('login_route'))


@socketio.on('join')
def handle_join(data: dict):
    print(f'socketio join route. data={data}')
    print(f'request addr: {request.remote_addr}')
    room = data['room']
    join_room(room)
    send(f'{data["username"]} has joined the room {room}.', room=room)


@socketio.on('message')
def handle_message(data: dict):

    print('socketio GOT message:', data)
    if isinstance(data, dict):
        user = data.get('user_name', False)
        room = data.get('room_name', False)
        msg = data.get('message', False)

        if user and msg and room:
            print('flask backend >send< msg to chat')
            send(f'{user}: {msg}', room=room)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True, use_reloader=True, ssl_context='adhoc')
