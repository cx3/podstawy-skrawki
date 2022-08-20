def some_func(a=1, b=1, c=1):
    print('parametry:')
    print(f'a={a}, b={b}, c={c}')


print(some_func(a=5.3, c=.3))
exit()


def func(**kwargs):
    print('kwargs jest typu', type(kwargs))
    for k in kwargs:
        print(k, '->', kwargs[k])


slownik = {'a': 1, 'b': 2, 'c': 3}

print(slownik)
print(type(slownik))
func(**slownik)