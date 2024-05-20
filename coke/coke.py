amount_due = 50
while amount_due > 0:
    print("Amount due:", amount_due)
    pay = input("Insert coin: ")
    amount_due = amount_due - pay

    if amount_due <= 0:
        break
    print("Change Owed:", pay)



