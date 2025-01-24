import operator
from calculator_logo import calculator_logo

print(calculator_logo)

def calculate_answer(num1,num2, op):
    return ops[op](num1, num2)

continue_calc = 'y'


while True:
    try:
        first_num = int(input(f"What's the first number?: "))
        break
    except ValueError:
        print("You entered a non integer value, try again.")
        continue


print(f"+\n-\n*\n/\n")
while continue_calc == 'y':

    operation = input(f"Pick an operation: ")
    while "+" != operation != "-" and "*" != operation != "/":
        print(f"Please enter +,-,*,or / as your operation. ")
        operation = input(f"Pick an operation: ")

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    # next_num = int(input(f"What's the next number?: "))
    while True:
        try:
            next_num = int(input(f"What's the next number?: "))
            break
        except ValueError:
            print("You entered a non integer value, try again.")
            continue

    answer = calculate_answer(first_num, next_num, operation)

    print(f"{first_num} {operation} {next_num} = {answer}")

    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    while 'n' != continue_calc != 'y':
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_calc == 'n':
        break
    else:
        first_num = answer

