miasta = ['Wrocław', 'Gdańsk', 'Poznań', 'Katowice']
MIASTA = [_.upper()[::-1] for _ in miasta][::-1]

naprawione = []

for miasto in MIASTA:
    miasto_od_tylu = miasto[::-1]
    element = miasto_od_tylu[0] + miasto_od_tylu[1:].lower()
    naprawione.append(element)
    print('@@@', miasto, naprawione)

print(MIASTA)
print('!!' * 33)

print('NAPRAWIONE:', naprawione)
