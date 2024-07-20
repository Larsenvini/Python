def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
#unpacking
coins = [100, 50 ,25]

print(total(*coins), "Knuts")

