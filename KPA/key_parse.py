import os,hashlib,re

def check_password(password):
    # Leggi l'hash e il salt della password dal database
    with open(os.path.join('KPA','KEY','KEY_HASH.txt'), 'r') as f:
        saved_hash, salt = f.read().strip().split(',')

    # Aggiungi il salt alla password inserita
    salted_password = password.encode('utf-8') + salt.encode('utf-8')

    # Genera l'hash della password inserita utilizzando SHA-256
    hash_object = hashlib.sha256(salted_password)
    entered_hash = hash_object.hexdigest()

    # Confronta i due hash
    if entered_hash == saved_hash:
        print('Password Correct')
        return True
    else:
        return False
check_password()


# Function to check if a password is valid
def Regex_Clear_password(PSW):
    PASSWORD_REGEX = r'^[a-zA-Z0-9!"#$%&]+$'
    return bool(re.match(PASSWORD_REGEX, PSW))



def get_password():

    PASSWORD_PROMPT = 'Enter the Database password --> '
    while True:
        password = input(PASSWORD_PROMPT)
        if Regex_Clear_password(password):
            break
        else:
           print('Invalid password. Please enter a non-empty password that contains only alphanumeric characters and some special characters.')

    return password
