import re

# Function to check if the password matches the pattern
def regex_password(psw):
    
    password_REGEX = r'^[a-zA-Z0-9!"#$&]+$'
    
    return bool(re.match(password_REGEX, psw))
  


#Function to prompt the user to enter a password and check if it complies with the pattern
def get_password(PROMPT_REQUEST: str):

    while True:
        password_On_Clear = input(PROMPT_REQUEST)
        if regex_password(password_On_Clear):
            break
        else:
            print('Please enter a non-empty Clear_Text that contains only alphanumeric characters and some special characters.')
  
    return password_On_Clear
