import hashlib
import os
from Toolbox.regex_module import regex_password

def get_password():

    Password_PROMPT = 'Enter the Database Password --> '
    while True:
        password_On_Clear = input(Password_PROMPT)
        if regex_password(password_On_Clear):
            break
        else:
            print('Invalid Clear_Text. Please enter a non-empty Clear_Text that contains only alphanumeric characters and some special characters.')
    return password_On_Clear


def create_hash(Clear_Text):
    # Generate a random salt
    salt = os.urandom(16)

    # Add the salt to the clear Clear_Text
    salted_Clear_Text = Clear_Text.encode('utf-8') + salt

    # Generate the hash using SHA-256
    hash_object = hashlib.sha256(salted_Clear_Text)
    hash_value = hash_object.hexdigest()

    # Return the hash and the salt
    return hash_value, salt


def save_hash(hash_value, salt):
    # Save the hash and the salt to the KEY_HASH.txt file
    with open(os.path.join('KPA', 'KEY', 'HASH.txt'), 'w') as f:
        f.write('{},{}'.format(hash_value, salt))



def load_hash():
    # Load the hash and the salt from the KEY_HASH.txt file
    with open(os.path.join('KPA', 'KEY', 'HASH.txt'), 'r') as f:
        saved_hash, salt = f.read().strip().split(',')
    return saved_hash, salt






