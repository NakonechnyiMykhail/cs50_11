from cs50 import get_int, get_char
num1 = get_int("Number1: ")
num2 = get_int("Number2: ")
oper = get_char("Oper: ")
if "+" == oper:
    print(f"{num1} + {num2} =", num1+num2)
elif "-" == oper:
    # ...
elif "/" == oper:
    #...
elif "*" == oper:
    # ...
else:
    print("smth else")