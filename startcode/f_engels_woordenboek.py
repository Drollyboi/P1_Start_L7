dictionarie = {
    "Hallo" : "Hello",
    "Hoe" : "how",
    "Kweetnie" : "Idunno"
}

te_vertalen_woord = input("Geef een nl woord (Hallo, Hoe of Kweetnie) ")

if te_vertalen_woord in dictionarie:
    print(f"De engelse vertaling van {te_vertalen_woord} is {dictionarie[te_vertalen_woord]}")
else:
    print(f"{te_vertalen_woord} is niet in het woordenboek")