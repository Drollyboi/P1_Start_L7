import math

prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")

doos = input("Kies een doos: ")

if doos == "1":
    print("je hebt een", prijzenkast[0], "gewonnen!")
elif doos == "2":
    print("je hebt een", prijzenkast[1], "gewonnen!")
elif doos == "3":
    print("je hebt een", prijzenkast[2], "gewonnen!")
else:
    print("invalid number, '1', '2' or '3' expected")