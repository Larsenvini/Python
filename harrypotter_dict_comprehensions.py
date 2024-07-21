students = ["Hermione", "Harry", "Ron"]
"""
before:
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
"""
# this would be a list comprehension gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#dict comprehension:
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
