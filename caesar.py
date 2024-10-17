def encrypt(text, shift):
    encryptedText = ""

    for index in range(len(text)):
        character = text[index]
        if (character.isalpha()):
            encryptedText += (chr(ord(character) + (shift % 26)))
        else:
            encryptedText += character

    return encryptedText