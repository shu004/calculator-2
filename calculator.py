"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#get user input save that to a variable
#split by spaces to a list

while True:
    command = input("> ").split(" ")

    if command[0] == "q":
        break
    else:
        num1 = float(command[1])
        num2 = float(command[2])
        if command[0] == '+':
            print(add(num1, num2))

