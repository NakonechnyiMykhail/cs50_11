from cs50 import get_string, get_int, get_float
# import random
'''
multi-line
comment
'''
# name = get_string("Enter your name: ")
# print("hello", name, "!")
# print("hello " + name)
# print(f"hello, {name}")

# name = input("Enter your name: ")
# name_str = str(input("Enter your name: ")) # == get_string
# number_str = input('Enter your age: ') # -> string
# number = int(input('Enter your age: ')) # integer == get_int
# number_fl = float(input('Enter your age: ')) # float == get_float

# loops
# for index in range(10):
#     print(index)
#     print("\t", index * index)

num = 1
while True: # False
    print("index = " + str(num))
    num += 2 # num = num + 1
    if num == 10 or num == 12:
        break
    elif num < 20 and num > 1: # .. and ... or
        continue
    else: # if num >= 20
        break

print("end program")
