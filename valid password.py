# Define a function to check the validity of a password
def check_password(password):
    # Define the minimum length of the password
    min_length = 6
    maxlength=16

    # Check if the password is long enough
    if len(password) < min_length:
        if len(password)>maxlength:
            return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one special character
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    if not any(char in special_chars for char in password):
        return False

    # If all checks pass, the password is valid
    return True

# Get the password from the user
password = input("Enter a password: ")

# Check if the password is valid
if check_password(password):
    print("The password is valid.")
else:
    print("The password is not valid. Please make sure it is at least 6 characters long and less then 16 character, contains at least one digit, one lowercase letter, one uppercase letter, and one special character.")