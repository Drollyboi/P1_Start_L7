telefoonboek = {
    "Bob" : "0473 81 99 37",
    "John" : "0478 91 34 88",
    "GOD" : "7777 77 77 77"
}


def nummer():
    while True:
        naam = input("Geef een naam, dan geef ik het nummer (stop om te stoppen): ")

        if naam in telefoonboek:
        print(f"Het nummer van {naam} is {telefoonboek[naam]}")
        else:
        print("Dit nummer staat niet in het telefoonboek!")
