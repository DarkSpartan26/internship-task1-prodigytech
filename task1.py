def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap using modulo
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Leave non-alphabet characters unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Select an option (1/2): ")

    if choice not in ["1", "2"]:
        print("❌ Invalid option. Exiting.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("❌ Please enter a valid number for shift.")
        return

    if choice == "1":
        encrypted = caesar_encrypt(message, shift)
        print(f"\n🔐 Encrypted Message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()