def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"

    print(f"{student[1]} from {student[1]}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
