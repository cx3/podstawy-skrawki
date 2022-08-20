from typing import List, Dict


some_list = [
    {'x': 'x'},
    {'x': 'x'},
    {'x': 'x'},
    {'a': 'a', 'b': 'b'},
    {'a': 'a', 'b': 'b'},
    {'a': 'a', 'b': 'b', 'c': 'c'},
    {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'},
]

for indeks, element in enumerate(some_list):
    print(indeks, '->', element)

print('\n\nsome_list2')
some_list2 = []
for next_dict in some_list:
    tmp = []
    for key in next_dict:
        tmp.append((key, next_dict[key]))

    some_list2.append(tuple(tmp))

for indeks, items in enumerate(some_list2):
    print(items)

print('removed_repetitions:')
tuples_list = list(set(some_list2))

removed_repetitions: List[Dict] = []

for next_tuple in tuples_list:
    new_dict = dict()
    for pair in next_tuple:
        key, value = pair
        new_dict[key] = value
    removed_repetitions.append(new_dict)

for indeks, rp in enumerate(removed_repetitions):
    print(indeks, rp)
