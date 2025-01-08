from cipher_logo import cipher_logo
print(f"{cipher_logo}")
response = "yes"
while response == "yes":
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ''
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount if encode_or_decode == 'encode' else alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        print(f" Here is the {encode_or_decode}d result: {output_text}")

    while 'encode' != direction != 'decode':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message: \n").lower()
    # text_list = list(text)


    shift = int(input("Type the shift number:\n"))

    while not shift.is_integer():
        shift = int(input("Please enter a number:\n"))

    caesar(text, shift, direction)

    response = input(f"Do you want to cipher another word? Yes or No: ").lower()
print("GoodBye!")


    # if direction == 'encode':
    #     encrypt(text, shift)
    # elif direction == 'decode':
    #     decrypt(text, shift)

