def main():
    fuel = get_fraction()
    print(fuel)

def get_fraction():
    try:
        return int(input("Fraction:"))
    except:
        pass
