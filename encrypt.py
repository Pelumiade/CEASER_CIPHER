message = input("enter the message you want to decode: ")
shift = int(input("enter the shift value: "))
shift_direction = input("Please enter the shift direction (Enter 'F' for forward, 'B' for backward): ")

def decrypt_message(message, shift, shift_direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    figure = '0123456789'
    result = ""
    result_figure = ""

    # Determine the direction of the shift
    if shift_direction.lower() == 'b':
        shift = - shift   
    #run on each letter in the message
    for letter in message:
        if letter.isdigit() and letter in figure:
            index = figure.find(letter)
            index = (index + shift) % ((len(figure)))
            letter = (figure[index])
            result_figure += letter
        elif letter in alphabet:
            index = alphabet.find(letter.lower())
            index = (index + shift) % (len(alphabet))
            #deals with wrap around if index is greater than 26 or less than 0
            if index < 0:
                index = index + len(alphabet)

            if letter.isupper():
                result += alphabet[index].lower()
            elif letter.islower():
                result += alphabet[index].upper()
        else:
            result += letter
            
    return result + result_figure

print(decrypt_message(message, shift, shift_direction))
