import random

def play():
    computer = random.choice(['p', 'h', 'f'])
    while 1 == 1:
        ok = 1
        player = input("Ce alegi?: 'p' pentru piatra, 'h' pentru hartie, 'f' pentru foarfeca\n")

        if player == computer:
            print('Egalitate')

        if castig(player, computer):
            print('Ai castigat!')

        if castig(computer, player):
            print('Ai pierdut!')

        if player not in ['p', 'h', 'f']:
            print('Ai gresit!')

        if ok == 1:
            print('Vrei sa continui?')
            alegere = input("Ce alegi?: 'd' pentru Da, 'n' pentru Nu\n")
            while 2 == 2:
                if alegere not in ['d', 'n']:
                   print('Raspuns gresit. Repetati: ')
                   alegere = input('Iara: ')
                elif alegere == 'n':
                    return 0
                elif alegere == 'd':
                    break
                else:
                    continue

def castig(jucator, oponent):
    if (jucator == 'p' and oponent == 'f') or (jucator == 'f' and oponent == 'h') \
            or (jucator == 'h' and oponent == 'p'):
        return True

print(play())
