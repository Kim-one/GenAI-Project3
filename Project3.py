# Project: Password Strength Checker

score=0 # score 
string="" # string to print 

# Gets user input
password_input = input("Enter a password: ")

# Checks if the password meets the requirements 

# Checks the length of the password is greater than or equal to 8
if len(password_input) >= 8:
    score+=2
else:
    string += " more characters"

# Checks if the password contains at least one uppercase letter
if any(char.isupper() for char in password_input):
    score+=2
else:
    string += " at least one uppercase letter"

# Checks if the password contains at least one lowercase letter 
if any(char.islower() for char in password_input):
    score+=2
else:
    string+=" at least one lowercase letter"

# Checks if the password contains at least one digit 
if any(char.isdigit() for char in password_input):
    score+=2
else:
    string+=" needs a digit"

# Checks if the password contains at least one special character
if any(char in "!@#$%^&*()_+=[];:<>?" for char in password_input ):
    score+=2    
else:
    string+=" and a special character such as (@,#,!)"

# Checks if the password has a perfect score
if score==10:
    print("Your password is strong! 💪")
else:
    print(f"Your password needs{string}.")      
print(score)