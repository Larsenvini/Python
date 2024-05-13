def main():
    dollars = dollars_to_float(float("How much was the meal? "))
    percent = percent_to_float(float("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip('$')
    return(float)



def percent_to_float(p):
    p = p.strip('%')
    return(float)

main()
