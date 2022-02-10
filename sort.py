import random

kleuren = ["Oranje", "Blauw", "Groen", "Bruin"]
zak = []

aantal = int(input("Hoeveel M&M's wil je?: "))

def zakkenvuller(aantal:int, kleuren:list):
    mnmDictionaryBag = {
        "Oranje": 0,
        "Blauw": 0,
        "Groen": 0,
        "Bruin": 0
    }
    for x in range(aantal):
        zak.append(random.choice(kleuren))
        mnmDictionaryBag[random.choice(list(mnmDictionaryBag))]+=1
    return zak, mnmDictionaryBag

def sortMNM(zak:list):
    zak.sort()
    print(zak)
    return zak

#------------------------------------------------
 
zak, mnmDictionaryBag = zakkenvuller(aantal, kleuren)
sortMNM(zak)
print(mnmDictionaryBag)
