students = [
    {"name": "Hermione", "house": "Gryffindor"},
     {"name": "Harry", "house": "Gryffindor"},
      {"name": "Ron", "house": "Gryffindor"},
       {"name": "Draco", "house": "Gryffindor"},
        {"name": "Padma", "house": "Gryffindor"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
