def liniowa(a, x, b):
    return a * x + b

print('f(x) = a * x + b')
a = int(input('Podaj a:'))
b = int(input('Podaj b:'))

while 1:
    try:
        x_od, x_do = input('Podaj zakres [od][spacja][do]: ').split(' ')
        x_od, x_do = int(x_od), int(x_do)
        break
    except ValueError:
        print('Dałeś kurwa za dużo liczbuf!!!!!!111')

for x in range(x_od, x_do):
    print(f'f({x}) = {liniowa(a=a, x=x, b=b)}')
