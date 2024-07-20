"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
#unpacking = * for lists, ** for dicts
coins = {"galleons":100, "sickles": 50 ,"knuts": 25}

print(total(**coins), "Knuts")
"""
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons = 100, sickles = 50, knuts = 25, pennies = 5)
