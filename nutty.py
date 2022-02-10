import random

kleuren = ["Oranje", "Blauw", "Groen", "Bruin"]
zak = []

aantal = int(input("Hoeveel M&M's wil je?: "))

def zakkenvuller(aantal):
    for x in range(aantal):
        zak.append(random.choice(kleuren))
    print(zak)
    return zak

#------------------------------------------------
 
zakkenvuller(aantal)