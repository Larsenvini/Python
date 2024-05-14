expression = input("Expression: ")
x, y, z = expression.split(" ")


formatted_expression = "${:.1f}".format(expression)
print(f"Leave{formatted_expression}")


