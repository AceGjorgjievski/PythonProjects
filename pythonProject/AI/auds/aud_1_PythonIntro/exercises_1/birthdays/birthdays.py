



birthdays = {
    "Ana": "13/03/1999",
    "Marija": "17/01/1991",
    "Stefan": "11/08/1896",
    "Aleksandar": "25/10/1992"
}

if __name__ == "__main__":
    print("Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:")
    names = birthdays.keys()
    print('\n'.join(names))
    print("Koj rodenden e potrebno da se prebara?")
    name = input()
    birthday = birthdays[name]
    print(f"Rodendenot na {name} e na {birthday}")
    

