import os , glob, hashlib 
from pykeepass import pykeepass
from key_parse import Regex_Clear_password
from key_maker import Hashing_Password

# Function to initialize the program and create necessary directories and files
def initializer():
                                                 
    # Get the current working directory
    cwd = os.getcwd()

    # Define the paths for the database and key directories
    db_dir = os.path.join( cwd,'KPA', 'DB' )    
    key_dir = os.path.join( cwd,'KPA', 'KEY' )
    
    # Create the database and key directories if they don't exist
    os.makedirs( db_dir, exist_ok=True )
    os.makedirs( key_dir, exist_ok=True )

    # Get a list of all database files in the database directory
    database_files = glob.glob(os.path.join(db_dir, 'KPA.kdbx'))

    # If no database exists, create a new one and prompt the user to create a key for it
    if not database_files:
        print('No database found. Please create a password for the new database.')    
        
        password = ''

        # Prompt the user to enter a password until a valid one is entered
        while True:

            password = input('Enter a password for the new database: ')
            if Regex_Clear_password(password):
                break
            else:
                print('Invalid password. Please enter a non-empty password that contains only alphanumeric characters and some special characters.')                         

        # Create a new database with the entered password and save it
        keepass = pykeepass.create_database(os.path.join(db_dir,'KPA.kdbx'),password)
        keepass.save()

        hash_value = Hashing_Password(password)
        Hash_Key = open(os.path.join(key_dir,'KEY_HASH.txt'),'w')
        Hash_Key.write(str(hash_value))
        Hash_Key.close()
        
    # Get a list of all key files in the key directory
    key_files = glob.glob(os.path.join(key_dir, 'KEY_HASH.txt'))

    # Return the paths for the database and key directories, and the list of database and key files
    return db_dir, database_files, key_dir, key_files

# Call the initializer function
initializer()