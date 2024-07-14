class Student():
    def __init__(self, name, house): #self gets the just created object (Student())
       self.name = name
       self.house = house
    ...

    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")

        def get_student():

            name = input("Name: ")
            house = input("House: ")
            student = Student(name, house)

            return student
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
