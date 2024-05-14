expression = input("Expression: ")
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(x + z)

    formatted_expression = "${:.1f}".format(expression)
print(f"Leave{formatted_expression}")


