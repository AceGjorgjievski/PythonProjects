

def execute(num1, num2):
    if num1 % num2 == 0:
        return "Deliv"
    else:
        return "Ne e deliv"


if __name__ == "__main__":
    print("Vnesete dva broja:")
    num1 = int(input())
    num2 = int(input())

    print(execute(num1,num2))

