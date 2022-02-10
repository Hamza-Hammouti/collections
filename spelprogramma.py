import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
minimum = 3
maximum = 10

def spelProgramma(spelList, minimum, maximum):
    rndm = random.choice(range(minimum, maximum))
    for x in range(rndm):
        print(random.choice(spelList))
        
spelProgramma(spelList, minimum, maximum)

