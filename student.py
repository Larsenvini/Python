class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student:
    def __init__(self, name, house):
     #self gets the just created object (Student()


        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

class Professor:
    def __init__(self, name, subject):
       
        self.subject = subject

        ...

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property #getter
    def house(self):
        return self._house

    @house.setter
#setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():

    name = input("Name: ")
    house = input("House: ")

    return Student(name, house)




if __name__ == "__main__":
    main()

'''
before = better for longer code:
def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


but now we know abt classes and objects
'''
