import random
import string
adjectives = ["Happy", "Cool", "Fast", "Brave", "Clever", "Lucky", "Fierce", "Mighty"]
nouns = ["Tiger", "Dragon", "Panda", "Wizard", "Knight", "Phoenix", "Ninja", "Robot"]
def generate_username(include_numbers=True, include_special_chars=True):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adj + noun

    if include_numbers:
        username += str(random.randint(10, 99))  # Adds a random two-digit number

    if include_special_chars:
        username += random.choice(string.punctuation)  # Adds a random special character
    
    return username
def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"Username '{username}' saved to {filename}.")
def main():
    print("Welcome to the Random Username Generator!")

    while True:
        num_usernames = int(input("How many usernames do you want to generate? "))
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        print("\nGenerated Usernames:")
        for _ in range(num_usernames):
            username = generate_username(include_numbers, include_special_chars)
            print(username)
            save_to_file(username)

        another = input("\nGenerate more usernames? (yes/no): ").strip().lower()
        if another != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
