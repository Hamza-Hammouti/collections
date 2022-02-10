import random

mnmDictionaryBag = {}

aantal = int(input("Hoeveel M&M's wil je?: "))

def zakkenvuller(aantal):

    mnmDictionaryBag = {
        "Oranje": 0,
        "Blauw": 0,
        "Groen": 0,
        "Bruin": 0
    }

    for x in range(aantal):
        mnmDictionaryBag[random.choice(list(mnmDictionaryBag))]+=1
    print(mnmDictionaryBag)
    return mnmDictionaryBag

#------------------------------------------------
 
mnmDictionaryBag = zakkenvuller(aantal)
