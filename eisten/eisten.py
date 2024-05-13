from operator import mul
def calculator():
    m = int(input("Welcome to Vini's EnergyCalculator! Type a mass: "))
    c = 300000000
    e = mul(m, pow(c, 2))

    print(e)

calculator()




