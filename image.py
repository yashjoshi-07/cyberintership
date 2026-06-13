from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Encrypted Successfully!")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Subtract key to restore original image
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Decrypted Successfully!")


choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ").upper()

image_path = input("Enter image path: ")
output_path = input("Enter output image path: ")
key = int(input("Enter encryption key (0-255): "))

if choice == 'E':
    encrypt_image(image_path, output_path, key)
elif choice == 'D':
    decrypt_image(image_path, output_path, key)
else:
    print("Invalid Choice!")