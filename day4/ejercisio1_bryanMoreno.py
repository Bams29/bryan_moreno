def encontrar_pares_divisibles(lista, k):
    pares_divisibles = set()

    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if (lista[i] + lista[j]) % k == 0:
                pares_divisibles.add((lista[i], lista[j]))

    return pares_divisibles


T = int(input(" "))
pares_encontrados2 = []
for y in range(1, T + 1):

    n, k = map(int, input(" ").split())
    lista = list(map(int, input(" ").split()))

    pares_encontrados = encontrar_pares_divisibles(lista, k)


    if pares_encontrados:
        pares_encontrados2.append(len(pares_encontrados))
    else:
        print("No se encontraron pares que cumplan con las restricciones.")
for z in range(0, T, 1):
    print(f"Caso #{z+1}: {pares_encontrados2[z]}")