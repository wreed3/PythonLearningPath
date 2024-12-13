import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

def password_generator():
    def random_values(array, num):
        value_array = []
        for value in range(1,num+1):
            item = random.choice(array)
            value_array.append(item)
        return value_array

    password_array = []

    random_letter_values_array = random_values(letters, nr_letters)

    random_number_values_array = random_values(numbers, nr_numbers)

    random_symbol_values_array = random_values(symbols, nr_symbols)

    password_array = random_letter_values_array + random_number_values_array + random_symbol_values_array

    random.shuffle(password_array)

    # 3 different ways to turn the array into a string

    # 1. ________________________________
    password = ''.join(password_array)
    #____________________________________


    # 2._________________________________
    # password = ""
    # for char in password_array:
    #     password += char
    # ____________________________________


    # 3.__________________________________
    # password = ''.join(random.sample(password_array, len(password_array)))
    #______________________________________
    print(password)

password_generator()