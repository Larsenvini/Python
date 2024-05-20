amount_due = 50
while amount_due > 0:
    print("Amount due:", amount_due)
    pay = input("Insert coin: ")
    if pay == 25:
        amount_due = amount_due - 25
    elif pay == 10:
        amount_due = amount_due - 10

    elif pay == 5:
        amount_due = amount_due - 5

    else:
        print("Value not accepted")

    if amount_due <= 0:
        break
    print("Change Owed:", pay)



