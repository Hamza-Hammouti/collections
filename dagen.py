from re import I


dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]

print(f"Alle dagen van de week zijn:")
for x in range(7):
    print(dagen[x])
print(f"De werkdagen zijn:")
for x in range(5):
    print(dagen[x])
print(f"De weekenddagen zijn:")
for x in range(7):
    print(dagen[x])
print(f"Alle dagen van de week in omgekeerde volgorde zijn:")
for x in range(6, -1, -1):
    print(dagen[x])
print(f"De weekenddagen in omgekeerde volgorde zijn:")
for x in range(6, 4, -1):
    print(dagen[x])