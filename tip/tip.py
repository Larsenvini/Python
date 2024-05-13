def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    print("Leave ${0}".format(tip))


def dollars_to_float(d):
    d = d.strip('$')
    return round(float(d),3)



def percent_to_float(p):
    p = p.strip('%')
    return round(float(p)/100,3)

main()
