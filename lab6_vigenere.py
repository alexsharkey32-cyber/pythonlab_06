def vigenere_sq(alphabet):
    print("|   | " + " | ".join(alphabet) + " |")
    print("|---|" + "---|" * len(alphabet))

    for row_index, row_letter in enumerate(alphabet):
        shifted_alphabet = alphabet[row_index:] + alphabet[:row_index]
        print(f"| {row_letter} | " + " | ".join(shifted_alphabet) + " |")


def letter_to_index(letter, alphabet):

    return alphabet.index(letter)


def index_to_letter(index, alphabet):

    return alphabet[index % len(alphabet)]


def vigenere_index(key_letter, plaintext_letter, alphabet):

    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (key_index + plaintext_index) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):

    key = key.upper()
    plaintext = plaintext.upper()

    if not key or any(letter not in alphabet for letter in key):
        raise ValueError("The keyword must contain only letters from the alphabet.")

    encrypted = []

    for position, character in enumerate(plaintext):
        if character in alphabet:
            key_letter = key[position % len(key)]
            encrypted.append(vigenere_index(key_letter, character, alphabet))
        else:
            # The lab's example aligns the key to every character,
            # including spaces and punctuation.
            encrypted.append(character)

    return "".join(encrypted)


def undo_vigenere_index(key_letter, cipher_letter, alphabet):

    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plaintext_index = (cipher_index - key_index) % len(alphabet)
    return index_to_letter(plaintext_index, alphabet)


def decrypt_vigenere(key, cipher_text, alphabet):

    key = key.upper()
    cipher_text = cipher_text.upper()

    if not key or any(letter not in alphabet for letter in key):
        raise ValueError("The keyword must contain only letters from the alphabet.")

    decrypted = []

    for position, character in enumerate(cipher_text):
        if character in alphabet:
            key_letter = key[position % len(key)]
            decrypted.append(undo_vigenere_index(key_letter, character, alphabet))
        else:
            decrypted.append(character)

    return "".join(decrypted)


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        print("\nVigenere Cipher Menu")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Print Vigenere square")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            key = input("Enter the keyword: ").strip()
            plaintext = input("Enter the plaintext: ")
            try:
                print("Encrypted text:", encrypt_vigenere(key, plaintext, alphabet))
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            key = input("Enter the keyword: ").strip()
            cipher_text = input("Enter the ciphertext: ")
            try:
                print("Decrypted text:", decrypt_vigenere(key, cipher_text, alphabet))
            except ValueError as error:
                print("Error:", error)

        elif choice == "3":
            vigenere_sq(alphabet)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
