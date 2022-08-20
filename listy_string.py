moj_jakis_str = 'Ala ma kota, kot ma AIDS'

moja_tupla = [_.upper() for _ in moj_jakis_str]
print('moja tupla jest typu:', type(moja_tupla))

duze_litery = ''.join(moja_tupla)
print('teraz duze litery są typu ', type(duze_litery))
dlugosc_przed = len(duze_litery)

print('Zobaczmy teraz:', duze_litery)

for literka in moj_jakis_str:
    duze_litery += literka.upper()

print(duze_litery)
print('=' * dlugosc_przed * 2)

print('ala'.upper() in duze_litery)

if 'ala'.upper() in duze_litery and len(duze_litery) > 1:
    print('spelniony warunek')
else:
    print('niespelniony warunek')


print('=' * len(duze_litery))

komentarz = '''for literka in duze_litery[3:-3][::-1]:
    print('literka:', literka, 'jej kod ASCII', ord(literka))'''

# print(komentarz)

duze_litery += 'QWERTY'
duze_litery += str(1)

for indeks, literka in enumerate(duze_litery):
    print(' ' * indeks + duze_litery[indeks:len(duze_litery)], '\t\t', indeks)
