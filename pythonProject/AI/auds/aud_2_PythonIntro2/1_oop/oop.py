

class Person:
    def __init__(self,name="", lastname=""):
        self.name = name
        self.lastname = lastname

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name

    def get_lastname(self):
        return self.lastname
    def set_lastname(self,lastname):
        self.lastname = lastname

    def to_string(self):
        return (f"Name: {self.name}, LastName: {self.lastname}")



class Student(Person):
    total = 0

    def __init__(self,name="",lastname="",index=101010):
        super(Student, self).__init__(name,lastname)
        self.name = name
        self.lastname = lastname
        self.index = index
        self.__class__.total += 1

    def get_index(self):
        return self.index
    def set_index(self,index):
        self.index = index

    def get_total(self):
        return self.__class__.total

    def to_string(self):
        return (f"Name: {self.name}, LastName: {self.lastname}, Index: {self.index}")




if __name__ == "__main__":

    s = Student("Ace","Gjorgjeivski",201183)
    print(s.to_string())
    # print(getattr(s,"name"))
    # print(getattr(s,"get_index")())
    # print(hasattr(s,"get_index"))
    # print(hasattr(s,"gender"))



