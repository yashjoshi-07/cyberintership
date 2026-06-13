

def save_text():
    text = input("Type something: ")

    with open("log.txt", "a") as file:
        file.write(text + "\n")

    print("Text saved to log.txt")

while True:
    save_text()

    choice = input("Continue? (y/n): ")
    if choice.lower() != 'y':
        break