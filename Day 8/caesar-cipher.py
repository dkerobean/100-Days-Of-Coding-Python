from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for i in plain_text:
#         position = alphabet.index(i) + shift_amount
#         cipher_text += alphabet[position]
#     print(f"the encoded text is {cipher_text}")
#
#
# def decrypt(plain_text, shift_amount):
#     decipher_text = ""
#     for i in plain_text:
#         position = alphabet.index(i) - shift_amount
#         decipher_text += alphabet[position]
#     print(f"the decoded text is {decipher_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)


def caesar(plain_text, shift_amount, cipher_direction):
    final_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in plain_text:

        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += letter

    print(f"the {cipher_direction}d text is {final_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # when user enters number beyond 26
    shift %= 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Else type 'no'\n")
    if result == "no":
        should_continue = False
        print("Good Bye")










