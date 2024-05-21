amount_due = 50
while amount_due > 0:
    print("Amount due:", amount_due)
    pay = input("Insert coin (25c, 10c or 5c): ")
    if pay == '25':
        amount_due = amount_due - 25
    elif pay == '10':
        amount_due = amount_due - 10
    elif pay == '5':
        amount_due = amount_due - 5
        owed = pay
    else:
        print("Invalid coin, please insert 25c, 10c or 5c only.")

if amount_due < 0:
    print("Change Owed:", amount_due)

def owed():
    








