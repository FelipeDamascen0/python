import random

timeUm = input('Digite o nome do time um :')
timeDois = input('Digite o nome do outro time :')
tempo = 0

timesOne = 0
timesTwo = 0
while tempo <= 80:
    tempo += 1
    pontos = random.randint(2,3)
    timePonto = random.randint(1, 2)
    if timePonto == 1:
        timesOne += pontos
        print(f'{timeUm} marcou {pontos}')
    else:
        timesTwo += pontos
        print(f'{timeDois} marcou {pontos}')


print(f'{timeUm} {timesOne} x {timeDois} {timesTwo}')
