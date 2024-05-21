amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    pay = input("Insert coin (25c, 10c or 5c): ")
    if pay == '25':
        amount_due = amount_due - 25
    elif pay == '10':
        amount_due = amount_due - 10
    elif pay == '5':
        amount_due = amount_due - 5
        owed = pay
    else:
        amount_due = amount_due

if amount_due == 0:
    print("Change Owed: 0")



if amount_due < 0:
   float(amount_due)
   print("Change Owed:", abs(amount_due))










