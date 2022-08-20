slownik = {
    "kod": "00-036", "miejscowosc": "Warszawa", "ulica": "Krzysztofa Kamila Baczy\u0144skiego",
    "gmina": "Warszawa-\u015ar\u00f3dmie\u015bcie", "powiat": "Warszawa", "wojewodztwo": "mazowieckie",
    "dzielnica": "\u015ar\u00f3dmie\u015bcie", "numeracja": []
}


for klucz in slownik:
    print(f'{klucz}: {slownik[klucz]}')

print('-' * 44)

for klucz, wartosc in slownik.items():
    print(f'{klucz}: {wartosc}')

print('=' * 55)

try:
    slownik['dskfjdkjfdkgjdfkfjd']
except KeyError as e:
    #print('przechwycilem blad typu', type(e))
    print('Nie ma takiego klucza. Klucze:', slownik.keys())


print('Wartosci w sklowniku:', slownik.values())
print('@' * 44)

slownik['moj nowy klucz'] = 'moja nowa wartosc'

if 'moj nowy klucz' in slownik:
    print('moj nowy klucz  ZNAJDUJE SIE W slowniku' )

if 'czy taki klucz' not in slownik:
    print('czy taki klucz  NIE ZNAJDUJE SIE w slowniku')

if 'czy taki klucz' not in slownik.keys():
    print('czy taki klucz  NIE ZNAJDUJE SIE w slowniku')

print('A teraz usuwam "moj nowy klucz"')
del slownik['moj nowy klucz']

if 'moj nowy klucz' in slownik:
    print('moj nowy klucz  ZNAJDUJE SIE W slowniku' )
else:
    print('moj nowy klucz  >>NIE<< ZNAJDUJE SIE JUZ W slowniku' )

print('#' * 55 + '\n\n')

slownik['kod'] = 'QQ-QQQ'
del slownik['kod']
print(slownik.get('kod', 'Nie ma takiego klucza'))
slownik['kod'] = '00-036'
print(slownik.get('kod', 'Nie ma takiego klucza'))


print('%' * 33)

slownik.update({
    'AAA': 'AAA',
    'BBB': 'BBB',
    'PODSLOWNIK': {
        'AAAAAAAAAA': 'AAAAAAAAA',
        'BBBBBBBBBB': 'BBBBBBBBB',
    }
})

print('\n\nBawimy sie w update:')
for key, val in sorted(slownik.items(), reverse=True):
    print(f'{key} -> {val}')
