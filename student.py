class Student():
    def __init__(self, name, house):
     #self gets the just created object (Student())
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

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
