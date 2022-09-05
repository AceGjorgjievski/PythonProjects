


birthdays = {}

if __name__ == "__main__":
    print("Dobredojdovte do rechnikot za rodendeni.")

    while True:
        print("Kolku lichnosti sakate da ima rechnikot? ...")
        broj = int(input())
        print("Vnesete ime i soodvedno rodendenot na taa lichnost")
        for i in range(broj):
            print(f"Lichnost broj: {i+1}")
            print("Ime:")
            name = input()
            print("Rodenden: (dd/mm/yy)")
            birthday = input()
            birthdays[name] = birthday
        print("Uspeshno go popolnivte rechnikot")
        print(f"Kolku rodendeni sakate da prikazhete? Validni iminja: {', '.join(birthdays.keys())}")
        num = int(input())
        for i in range(num):
            print(f"Imeto na lichnosta broj {i+1}")
            name = input()
            print(f"Rodendenot na {name} e {birthdays.get(name)}")
        print("Dali sakate povtorno? (Y/N)")
        answer = str(input()).lower()
        if answer[0] == "n":
            break



    print("Blagodaram ! prijatno")










