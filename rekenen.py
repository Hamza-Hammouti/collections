listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def addAndDisplayLists():
    for x in range(10):
        listThree = listOne[x] + listTwo[x]
        print(f'{listOne[x]} + {listTwo[x]} = {listThree}')

def substractAndDisplayLists():
    for x in range(10):
        listThree = listOne[x] - listTwo[x]
        print(f'{listOne[x]} - {listTwo[x]} = {listThree}')

def multiplyAndDisplayLists():
    for x in range(10):
        listThree = listOne[x] * listTwo[x]
        print(f'{listOne[x]} * {listTwo[x]} = {listThree}')

def divideAndDisplayLists():
    for x in range(10):
        listThree = listOne[x] / listTwo[x]
        print(f'{listOne[x]} / {listTwo[x]} = {listThree}')

print("Add lists")
addAndDisplayLists()

print("-----------------")

print("Substract lists")
substractAndDisplayLists()

print("-----------------")

print("Multiply lists")
multiplyAndDisplayLists()

print("-----------------")

print("Divide lists")
divideAndDisplayLists()

