linha = 1
coluna = 1
while linha <= 10:
    print('')
    while coluna <= 10:
        print('{} x {} = {}'.format(linha, coluna, linha * coluna))
        coluna += 1
    linha += 1
    coluna = 1