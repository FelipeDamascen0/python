import random
jogadorDeposito = int(input('Digite o valor de deposito :'))
iniciarJogo = input('Deseja iniciar o jogo:')
while True:
    if iniciarJogo == 's':
        dadoAleatorio = random.randint(1, 7)
        print(dadoAleatorio)
        valorAposta = int(input('Digite o valor da aposta :'))
        if valorAposta > jogadorDeposito:
            print('Saldo insufisciente!!!')
            break
        jogadorDeposito -= valorAposta
        jogador = int(input('Chute um numero :'))

        if jogador == dadoAleatorio:
            valorAposta = valorAposta + valorAposta
            jogadorDeposito = valorAposta + jogadorDeposito
            print('Parabens voce ganhou R$',valorAposta,'E ficou com R$',jogadorDeposito)
        else:
            print('Nao foi dessa vez você perdeu R$',valorAposta ,'o numero era',dadoAleatorio,'e ficou com R$',jogadorDeposito)
        jogarNovamente = input('Deseja jogar novamente :')
        if jogarNovamente == 'n':
            print('Voce saiu com um saldo de R$',jogadorDeposito)
            break
        if jogadorDeposito == 0:
            print('Voce perdeu tudo deposite mais para jogar')
            break
