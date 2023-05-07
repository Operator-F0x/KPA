import os
from pykeepass import PyKeePass
from Toolbox.initializer import initializer
from Toolbox.regex_module import regex_password
from Database_Strument.create_db import create_new_database
from Toolbox.Hash_Gestion import get_password



def check_password(Clear_Text):
    # Check if the Clear_Text is valid
    if not regex_password(Clear_Text):
        print('Invalid Clear_Text. Please enter a non-empty Clear_Text that contains only alphanumeric characters and some special characters.')
        return False
    else:
        return True




def load_database():
    # Get the current working directory, database directory, database file name, key directory, and key file name
    db_dir, database_files, _, _ = initializer()

    # If no database exists, create a new one and prompt the user to create a key for it
    if not database_files:
        print('No database found. Please create a password for the new database.')
        create_new_database()

    # Create a string containing the full path to the KeePass database file
    auto_database = os.path.join(db_dir, database_files[0])

    # Prompt the user to enter the password until a valid one is entered
    while True:
        password = get_password()
        if check_password(password):
            break
        else:
            print('Wrong password')

    print('Database Loaded')

    kpa = PyKeePass(auto_database, password=password)

    return kpa 
