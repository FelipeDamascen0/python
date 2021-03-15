import random
meu = [8, 14, 23, 33, 47, 58]
megasena = list(range(1, 61))
n = int(input('Numero de testes :'))
soma = 0
for i in range(n):
    sorteado = []
    cont = 0
    while meu != sorteado:
        megaSort = megasena.copy()
        sorteado = []
        for j in range(6):
            numSorteado = random.choice(megaSort)
            sorteado.append(numSorteado)
            megaSort.remove(numSorteado)
        sorteado.sort()
        cont += 1
    soma += cont
    print(f'Resultado do teste {i+1}: {cont} tentativas')
soma /= n
print(f'Media dos resultados {soma}')