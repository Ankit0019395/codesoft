import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))

            password = generate_password(length)

            print(f"Generated Password: {password}")

            try_again = input("Do you want to generate another password? (yes/no): ").lower()
            if try_again != 'yes':
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
