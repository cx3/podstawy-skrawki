def sortowanie_babelkowe(lista):
    n = len(lista)

    while n > 1:
        zamien = False
        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                zamien = True

        n -= 1
        print(lista)
        if not zamien:
            break

    return lista


posortwane = sortowanie_babelkowe([8, 0, 3, 5, 1, 4])
print('\n\nPosortowane', posortwane)
