
from datetime import date
nameYear = []

curr_year = 2020
def calculate(age):
    return (curr_year - age) + 100

if __name__ == "__main__":
    print("Vnesete ime i godini:")
    data = input().split(" ")
    name = data[0]
    age = int(data[1])

    print(f"{name} kje ima 100 godini vo {calculate(age)}")

