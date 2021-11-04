"""CLI application for a prefix-notation calculator."""
from functools import reduce
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

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
                print("Please enter a number after the operator")

        elif len(command) > 3:
            numbers = []
            for num in command[1:]:
                try:
                    num = float(num)
                    numbers.append(num)
                except ValueError:
                    print('Please enter numbers after the operator')

            if operator == '+':
                print(reduce(add, numbers))
            elif operator == '-':
                print(reduce(subtract, numbers))
            elif operator == '*':
                print(reduce(multiply, numbers))
            elif operator == '/':
                print(reduce(divide, numbers))
            else:
                print("Not a valid command")

        else:
            print("Not a valid command")






