import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction_selected, original_text, shift_amount):
    shifted_text = ""
    for char in original_text:
        if char not in alphabet:
            shifted_text += char
        else:
            new_index = alphabet.index(char)
            if direction_selected == "encode":
                new_index += shift_amount
            elif  direction_selected == "decode":
                new_index -= shift_amount
            new_index %= len(alphabet)
            shifted_text += alphabet[new_index]
    print(shifted_text)

play = True

while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    play_input = input("Do you want to play again?")
    if play_input == "no":
        play = False




