def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    rounded_tip = tip(round, 2)
    print("Leave ${0}".format(rounded_tip))


def dollars_to_float(d):
    d = d.strip('$')
    return float(d)



def percent_to_float(p):
    p = p.strip('%')
    return float(p)/100

main()
