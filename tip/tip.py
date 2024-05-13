def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    rounded_tip = tip(round, 2)
    print(f"Leave ${rounded_tip:.2f}")


def dollars_to_float(d):
    d = d.strip('$')
    return(float)



def percent_to_float(p):
    p = p.strip('%')
    return(float)

main()
