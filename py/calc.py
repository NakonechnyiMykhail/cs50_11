from cs50 import get_float, get_string
num1 = get_float("Number1: ")
num2 = get_float("Number2: ")
oper = get_string("Oper: ")
if "+" == oper:
    print(f"{num1} + {num2} =", num1+num2)
elif "-" == oper:
    print(f"{num1} + {num2} =", num1+num2)
elif "/" == oper:
    print(f"{num1} + {num2} =", num1+num2)
elif "*" == oper:
    print(f"{num1} + {num2} =", num1+num2)
else:
    print("smth else")