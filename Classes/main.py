import random
import string
from __init__ import CURSOR, CONN
from user import User
from username import Username
from password import Password

# ANSI color escape codes for colorful printing
COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m"  # Reset to default color
}

password_objs = Password.get_all() # using Password class instance method to get all rows in the passwords table as objects
username_objs = Username.get_all() # using Username class instance method to get all rows in the usernames table as objects
username_list = [obj.username for obj in username_objs] # using list comprehension on the username objects to create a list of all usernames
password_list = [obj.password for obj in password_objs] # using list comprehension on the passsword objects to create a list of all passwords
list_of_ids = list(range(1, len(username_list) + 1)) # made a list of ids that are the same as the id number in the db.
passwords_table = {key: value for key, value in zip(list_of_ids, password_list)} # zipping the list_of_ids with the passwords list to create ditionary e.g {1: "password"}

def crack(password):
    if password in passwords_table.values(): # to check if the password parameter is inside of the passwords_table dictionary 
        attempts = 0  # Counter for attempts
        while True:  # Keep trying until the password is cracked
            guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))  # Generate a random guess at the length of the passed password parameter
            attempts += 1  # Increment attempts counter
            color = random.choice(list(COLORS.values())[:-1])  # Select a random color
            print(f"attempt # {attempts} - {color}{guess}{COLORS['RESET']}")  # Print the attempt in color
            if guess == password:  # Check if the guess matches the password
                return guess, attempts  # If so, return the cracked password and the number of attempts

def crack_password_for_username(username):
    for user_id, user_name in enumerate(username_list, start=1):
        if user_name == username:  # Check if the provided username matches the current username in the loop
            password = passwords_table[user_id]  # Get the password associated with the current user_id
            print(f"Cracking password for {username}...")  # Print message indicating cracking has started
            cracked_password, attempts = crack(password)  # Crack the password cracked password and attempts are varibales being assighned the value of the crack function, becuase crack returns 2 variables it sets the values respectively, cracked_password == guess and atempts == attempts
            if cracked_password:  # Check if the password is cracked successfully
                print(f"The password for {username} is: {cracked_password} (cracked in {attempts} attempts).") # print message if successfull
            else:
                print(f"Failed to crack the password for {username}.")  # Print message if failed to crack the password
            break # to stop loop once cracked_password is returned
    else:
        print("Username not found.")  # Print message if the username is not found


def main():
    username = input("Enter the username: ")
    crack_password_for_username(username)  # Call the method to crack the password for the provided username

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly

# def crack_password_for_username(username):
#     if username in usernames_table.values():  # Check if the username exists
        # user_id = list(usernames_table.keys())[list(usernames_table.values()).index(username)]
#         password = passwords_table[user_id]  # Get the password associated with the username
#         print(f"Cracking password for {username}...")  # Print message indicating cracking has started
#         cracked_password, attempts = crack(password)  # Crack the password
#         print(f"The password for {username} is: {cracked_password} (cracked in {attempts} attempts).")  # Print the cracked password and number of attempts
#     else:
#         print("Username not found.")  # Print message if the username is not found