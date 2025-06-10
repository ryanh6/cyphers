def caesarEncrypt(text, shift):
    encryptedText = ""

    for index in range(len(text)):
        character = text[index]
        if (character.isupper()):
            encryptedText += chr(((ord(character) - 65 + shift) % 26) + 65)
        elif (character.islower()):
            encryptedText += chr(((ord(character) - 97 + shift) % 26) + 97)
        else:
            encryptedText += character

    return encryptedText

def caesarDecrypt(text, shift):
    encryptedText = ""

    for index in range(len(text)):
        character = text[index]
        if (character.isupper()):
            encryptedText += chr(((ord(character) - 65 - shift) % 26) + 65)
        elif (character.islower()):
            encryptedText += chr(((ord(character) - 97 - shift) % 26) + 97)
        else:
            encryptedText += character

    return encryptedText