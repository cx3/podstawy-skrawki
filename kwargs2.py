def func(*krotka, **slownik) -> dict:

    if krotka:
        slownik['args'] = krotka

    print('Jestem w funkcji, buduje slownik')
    for k in slownik.keys():
        print(k, '->', slownik[k])
    print('koniec funkcji')

    return slownik


jakis_moj_slownik = {'a': 1, 'b': 2, 'c': 3}

nowy = func(*(1,), **jakis_moj_slownik)

print('')

print('nowy jest typu:', type(nowy))
print('wartosc obiektu nowy:', nowy)