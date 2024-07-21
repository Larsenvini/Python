students = ["Hermione", "Harry", "Ron"]
"""
before:
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
"""
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
