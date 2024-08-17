import json
import os

# File to store user data
USER_DATA_FILE = "users.json"

# Load existing users from the file if it exists, otherwise start with an empty dictionary
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to the file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Sign up function
def sign_up(users):
    username = input("Enter Username: ")
    if username in users:
        print("Username already exists. Try signing in.")
        return
    
    password = input("Enter Password: ")
    mobile_number = input("Enter Mobile Number: ")
    
    # Add new user to the users dictionary
    users[username] = {
        "password": password,
        "mobile_number": mobile_number
    }
    
    # Save updated users data
    save_users(users)
    print("User registered successfully!")

# Sign in function
def sign_in(users):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # Check if the username exists and the password matches
    if username in users and users[username]["password"] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your mobile number is: {users[username]['mobile_number']}")
    else:
        print("Incorrect credentials. Program terminated.")

def main():
    users = load_users()
    
    print("1. Sign Up")
    print("2. Sign In")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        sign_up(users)
    elif choice == "2":
        sign_in(users)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
