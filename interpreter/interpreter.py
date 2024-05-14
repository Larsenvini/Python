expression = input("Expression: ")
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print("${:.1f}".format(x + z))






