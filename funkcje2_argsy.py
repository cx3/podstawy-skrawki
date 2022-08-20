def super_suma(*args):
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


print(super_suma(['a'], ['b'], ['c']))
print(super_suma('aa', 'bb', 'cc'))
print(super_suma(1, 2, 3))
print(super_suma(True, False))
print(super_suma(True, False, 1, 2))

exit()


def sum_lista(lista: list) -> int:
    result = 0
    for element in lista:
        result += element
    return result


'''print('@@@', sum_lista([2, 3, 5]))
exit()'''

# print(sum(2, 3, 5, 8, 13))
print(sum(*[2, 3, 5]))
exit()



'''print(2)
print(2,3,4)
print(2,3,4, ['abcd', [[['a'], 'aa'], 'aaa', {'x': ['xx']}] ])
exit()'''