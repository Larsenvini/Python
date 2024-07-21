students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
    #print(i+1, students[i]):
    #  without +1 would be 0,1,2, with it would be 1,2,3, but we have enumerate function

for i, student in enumerate(students):
    print( i + 1, student)


