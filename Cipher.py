def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            
            start = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            elif mode == "decrypt":
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


print("=== Caesar Cipher Program ===")

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

choice = input("Type 'encrypt' or 'decrypt': ").lower()

if choice == "encrypt":
    encrypted_text = caesar_cipher(message, shift, "encrypt")
    print("Encrypted Message:", encrypted_text)

elif choice == "decrypt":
    decrypted_text = caesar_cipher(message, shift, "decrypt")
    print("Decrypted Message:", decrypted_text)

else:
    print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")