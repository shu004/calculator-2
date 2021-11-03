"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#get user input save that to a variable
#split by spaces to a list

while True:
    command = input("> ").split(" ")
    operator = command[0]
    if operator == "q":
        break
    else:
        if len(command) == 3:
            try:
                num1 = float(command[1])
                num2 = float(command[2])

                if operator == '+':
                    print(add(num1, num2))
                elif operator == '-':
                    print(subtract(num1, num2))
                elif operator == '*':
                    print(multiply(num1, num2))
                elif operator == '/':
                    print(divide(num1, num2))
                elif operator == 'pow':
                    print(power(num1, num2))
                elif operator == 'mod':
                    print(mod(num1, num2))
                else:
                    print("Not a valid command")
            except ValueError:
                print("Please enter a number after the operator")

        elif len(command) == 2:
            try:
                num1 = float(command[1])

                if operator == 'square':
                    print(square(num1))
                elif operator == 'cube':
                    print(cube(num1))
                else:
                    print("Not a valid command")
            except ValueError:
                print("Please a number after the operator")

        else:
            print("Not a valid command")






