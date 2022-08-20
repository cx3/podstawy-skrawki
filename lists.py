miasta = ['Wrocław', 'Gdańsk', 'Poznań', 'Katowice']

print('Czy wrocław jest w liście: ', 'wrocław' in miasta)
print('Ile razy w liście:', miasta.count('wrocław'))
print('Ile razy w liście:', miasta.count('Wrocław'))
print('Indeks w liście:', miasta.index('Gdańsk'))
try:
    print('Indeks w liście:', miasta.index('gdańsk'))
except ValueError:
    print('gdańsk z małej nie występuje w liście')

miasta += ['Bydgoszcz']

print('Dlugosc listy po += wynosi:', len(miasta))
print('Lista miast:', miasta)

# miasta.reverse()

print('Miasta od tyłu:', miasta[::-1])

separator = ['='] * 30
separator = ''.join(separator)
print('jakiego typu jest zmienna separator:', type(separator))

print(separator)

print(miasta[2:])

skomplikowane = miasta[2:][::-1][::-1][::-1] * 3
print(skomplikowane)
print('Poznań jest razy ', skomplikowane.count('Poznań'))
print('Poznań jest pod indeksem ', skomplikowane.index('Poznań'))

while 1:
    try:
        miasto_do_szukania = input('Podaj miasto: ')

        if miasto_do_szukania not in skomplikowane:
            raise ValueError
        break
    except ValueError:
        print('Takiego miasta nie ma w liscie')

indeksy = []
for indeks_teraz, miasto in enumerate(skomplikowane):
    #indeks_teraz += 1
    if miasto == miasto_do_szukania:
        indeksy.append(indeks_teraz)

print('Poznań występuje pod indeksami:', indeksy)
