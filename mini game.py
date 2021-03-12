import random
playerVida = 500
playerSp = 100

vidaInimigo  = 50
numeroInimigos = int(input('Escolha o numero de inimigos :'))
inimigos = []

for i in range(numeroInimigos):
    inimigos.append([i+1, vidaInimigo])

jogando = True
while jogando:
    print('Vida :',playerVida)
    print('SP :',playerSp)

    ataqueCura = int(input('Atacar (1) ou curar (2) :'))

    if ataqueCura == 1:
        selecionado = random.choice(inimigos)
        dano = random.randint(10, 15)
        print(f'Voce causou {dano} de dano ao inimigo {selecionado[0]}')
        selecionado[1] -= dano
        if selecionado[1] <= 0:
            print(f'O inimigo {selecionado[0]} morreu!')
            inimigos.remove(selecionado)
    else:
        if playerSp >= 10:
            cura = random.randint(10, 15)
            print(f'Voce recebeu {cura} de vida')
            playerVida += cura
            playerSp -= 10
        else:
            print('SP insuficiente')

    for inimigo in inimigos:
        acertou = bool(random.choice([1,1,1,0]))
        if acertou:
            dano = random.randint(1, 3)
            print(f'o inimigo {inimigo[0]} causou {dano} de dano')
            playerVida -= dano
        else:
            print(f'inimigo {inimigo[0]} errou o ataque')

    if playerSp < 100:
         playerSp += 3

    if playerSp > 100:
        playerSp = 100

    if playerVida <= 0:
        print('PERDEU O JOGO !!!')
        jogando = False

    if len(inimigos) == 0:
        print('Voce venceu')
        jogando =  False
