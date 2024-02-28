import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")
    password_length = int(input("Enter the length of the password: "))
    random_password = generate_password(password_length)
    print("Your random password is:", random_password)