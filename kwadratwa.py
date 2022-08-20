def kwadratowa(a, x, b, c):
    return a * x**2 + b * x + c


print('f(x) = a * x2 + b * x + c')
a = int(input('Podaj a:'))
b = int(input('Podaj b:'))
c = int(input('Podaj c:'))

while 1:
    try:
        x_od, x_do = input('Podaj zakres [od][spacja][do]: ').split(' ')
        x_od, x_do = int(x_od), int(x_do)
        break
    except ValueError:
        print('Dałeś kurwa za dużo liczbuf!!!!!!111')

for x in range(x_od, x_do):
    print(f'f({x}) = {kwadratowa(a, x, b, c)}')
