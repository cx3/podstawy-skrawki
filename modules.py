import inspect
import importlib
from typing import List, Dict
from pip._internal.operations.freeze import freeze


'''
https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
https://www.geeksforgeeks.org/inspect-module-in-python/
https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
https://www.pythonpool.com/python-inspect/
'''


def list_installed_modules(version_info=True) -> List[str]:
    return [_ if version_info else _.split('==')[0] for _ in freeze(local_only=True)]


def inspect_module(name_or_module) -> Dict:

    classes = []
    methods = []
    functions = []
    generators = []

    if isinstance(name_or_module, str):
        my_module = importlib.import_module(name_or_module)

        for item in dir(my_module):
            attr = getattr(my_module, item)

            if inspect.isclass(attr):
                classes.append(attr)
            if inspect.ismethod(attr):
                methods.append(attr)
            elif inspect.isfunction(attr):
                functions.append(attr)
            if inspect.isgenerator(attr):
                generators.append(attr)

        return {
            'classes': classes,
            'methods': methods,
            'functions': functions,
            'generators': generators
        }


for k, v in inspect_module('os').items():
    print(k, '->', v)


# inspect_module('os')




