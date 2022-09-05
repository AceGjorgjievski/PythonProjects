


def execute(number):
    if number % 2 == 0:
        print("Paren")
        if number % 4 == 0:
            print("Deliv so 4")
    else:
        print("Neparen")


if __name__ == "__main__":
    print("Vnesete broj:")
    number = int(input())
    execute(number)




