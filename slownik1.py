import os
import json
from typing import List, Dict


def wczytaj_slowniki() -> List[Dict]:
    slowniki = []
    for linia in open('KODY-POCZTOWE.json'):
        if linia != '\n':
            d = json.loads(linia)
            slowniki.append(d)
    return slowniki


def pokaz_klucze():
    slowniki = wczytaj_slowniki()
    for slownik in slowniki:
        print(sorted(slownik.keys()))


def pokaz_klucze2(slowniki: List[Dict], kolejnosc: int = 0) -> List[str]:
    lista_kluczy = []

    if not isinstance(kolejnosc, int):  #
        kolejnosc = 0

    for slownik in slowniki:
        lista_kluczy.append(sorted(list(slownik.keys())))

    for e in range(len(lista_kluczy) - 1):
        for element in range(len(lista_kluczy)-1):
            if len(lista_kluczy[element]) > len(lista_kluczy[element + 1]):
                lista_kluczy[element], lista_kluczy[element + 1] = lista_kluczy[element + 1], lista_kluczy[element]

    if kolejnosc == 0:
        return lista_kluczy
    return lista_kluczy[::-1]


def pokaz_klucze3(slowniki: List[Dict], kolejnosc: int = 0) -> List[List[str]]:
    lista_kluczy = []
    print('def pokaz_klucze3()...')

    if not isinstance(kolejnosc, int):  #
        kolejnosc = 0

    for slownik in slowniki:
        lista_kluczy.append(list(sorted(slownik.keys())))

    lista_kluczy.sort(key=lambda x: len(x), reverse=bool(kolejnosc))
    return lista_kluczy


def wyszukaj(
        slowniki: List[Dict],
        nazwa_klucza: str,
        szukana_wartosc: str) -> List[Dict]:

    wyniki = []
    for slownik in slowniki:
        if nazwa_klucza in slownik:
            if slownik[nazwa_klucza] == szukana_wartosc:
                wyniki.append(slownik)

    return wyniki


def szukaj_test():
    slowniki = wczytaj_slowniki()
    wyniki_szukania = wyszukaj(slowniki, "ulica", "Zgoda")

    for wynik in wyniki_szukania:
        print('WYNIK:', wynik)


def test_pokaz_klucze2():
    slowniki = wczytaj_slowniki()
    posortowane = pokaz_klucze2(slowniki, kolejnosc=1)
    for p in posortowane:
        print(p)


def test_pokaz_klucze3():
    slowniki = wczytaj_slowniki()
    posortowane = pokaz_klucze3(slowniki, kolejnosc=0)
    print('Metoda 3 test')
    for p in posortowane:
        print(p)


if __name__ == '__main__':
    #szukaj_test()
    test_pokaz_klucze3()
    exit()















exit()
postals = []







for file in os.listdir('.'):
    try:
        '''if 'KODY' in file:
            continue'''
        if file.endswith('.json'):
            data = open(file).read()
            print('data jest typu:', type(data))
            postals += json.loads(data)
            print('ostatni element pstals jest typu', type(postals[-1]))
            print('a wyglada tak:', postals[-1])

            print(f'{file}: len(postals)', len(postals))

    except json.decoder.JSONDecodeError:
        print('error>>>', file)
        input('czekam na enter')


'''for some in postals:
    print(sorted(some.keys()))'''

f = open('KODY-POCZTOWE.json', 'w')
for postal in postals:
    try:
        d = json.dumps(postal)
        f.write(d+'\n')
    except json.decoder.JSONDecodeError:
        print(postal)
f.close()


