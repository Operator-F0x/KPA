# Loading Database Function

import os
from pykeepass import PyKeePass
from initializer import initializer
from key_parse import get_password, check_password


def db_load():    
    # Get the current working directory, database directory, database file name, key directory, and key file name
    db_dir, database_files, key_dir, key_file = initializer()

    # Create a string containing the full path to the KeePass database file
    Auto_Database = os.path.join( db_dir, database_files[0] )
    
    password = ''

    while not check_password(password):
        password = get_password()

        if not check_password(password):
            print('Wrong password')

    Autokey = password
    print('Database Loaded')

    Keepass = PyKeePass(Auto_Database, password = Autokey)

    # Return the PyKeePass object
    return Keepass

db_load()