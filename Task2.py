#Password Generator: 
import random
import string


def generate_password(Length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
#remove whitespace characters from the set of punctuation characters
    special_characters = string.punctuation.replace(" ", "")

    password = [random.choice(uppercase_letters),random.choice(lowercase_letters),random.choice(special_characters)]

#remaining Characters Length of a Password: 

    for gen in range(Length - 3):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    #We are using shuffle to show randomness in password:

    random.shuffle(password)

    password = ''.join(password)
    return password

def main():
    try:
        Length = int(input("Enter the desired length of the password: "))
        if Length <= 5:
            print("Password length must be greater then 5.")
        else:
            password = generate_password(Length)
            print("Generated Password:",password)
    except ValueError:
        print("Please Enter a Valid Integer. ")

if __name__ == "__main__":
    main()