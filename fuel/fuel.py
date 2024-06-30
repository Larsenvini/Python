def main():
    fuel = get_fraction()
    if fuel == "1/4":
        print("25%")
    elif fuel == "2/4":
        print("50%")
    elif fuel == "3/4":
        print("75%")
    elif fuel == "4/4":
        print("F")
    elif fuel == "0/4":
        print("E")

def get_fraction():
    try:
        return int(input("Fraction:"))
    except:
        pass
