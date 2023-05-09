import os
from pykeepass import PyKeePass
from Toolbox.initializer import initializer
from Database_Strument.create_db import create_KPA_database
from Toolbox.Hash_Gestion import get_password, check_password

def load_database():
    # Get the database directory and database list
    db_dir, database_files, _, _ = initializer()

    # If no database exists, create a new one and prompt the user to create a key for it
    if not database_files:
        print('No database found. Please create a password for the new database.')
        print('Enter new Password for KPA Database --> ', end= '')
        create_KPA_database()
        _, database_files, _, _ = initializer() # I reinitialize the database list
    # END IF

    print('KPA Database Loading'.center(30,'-'))
    # Create a string containing the full path to the KPA.kdbx Database
    auto_database = os.path.join(db_dir, database_files[0])
      
    # Prompt the user to enter the password until a valid one is entered
    while True:
        print('Enter the Database Password --> ', end= '')
        password = get_password()
        if check_password(password):
            break
        else:
            print('Invalid Clear_Text. Please enter a non-empty Clear_Text that contains only alphanumeric characters and some special characters.')

    print(' KPA - Database Loaded')
    kpa = PyKeePass(auto_database, password=password)

    return kpa

if __name__ == '__main__':
    None
