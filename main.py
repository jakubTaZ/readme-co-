# Autor: Jakub Tazbir



def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            new_code = ord(char) + shift
            if new_code > ord('Z'):
                new_code = ord('A') + (new_code - ord('Z') - 1)
            result += chr(new_code)
        else:
            result += char
    return result


if __name__ == "__main__":
    text = input("Podaj tekst (duże litery A-Z): ")
    shift = int(input("Podaj przesunięcie: "))
    encrypted = caesar_cipher(text, shift)
    print("Zaszyfrowany tekst:", encrypted)