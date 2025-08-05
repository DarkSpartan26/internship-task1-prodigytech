from PIL import Image
import os

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    # Encrypt by reversing RGB values of each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

    img.save(output_path)
    print(f"🔐 Encrypted image saved as: {output_path}")

def decrypt_image(input_path, output_path):
    # Same logic as encryption because it's reversible
    encrypt_image(input_path, output_path)
    print(f"🔓 Decrypted image saved as: {output_path}")

def main():
    print("=== Image Encryptor / Decryptor ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ")

    input_file = input("Enter the path of the image file: ")
    if not os.path.exists(input_file):
        print("❌ File not found.")
        return

    output_file = input("Enter the output file name (e.g., encrypted.png): ")

    if choice == "1":1
        encrypt_image(input_file, output_file)
    elif choice == "2":
        decrypt_image(input_file, output_file)
    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
