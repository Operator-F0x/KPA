import os , glob, hashlib,re 
from pykeepass import pykeepass

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
    database_files = glob.glob(os.path.join(db_dir, '*.kdbx'))

    # If no database exists, create a new one and prompt the user to create a key for it
    if not database_files:
        print('No database found. Please create a password for the new database.')    

        password = ''

        # Function to check if a password is valid
        def checkpass(PSW):
            PASSWORD_REGEX = r'^[a-zA-Z0-9!"#$%&]+$'
            return bool(re.match(PASSWORD_REGEX, PSW))
        
        # Prompt the user to enter a password until a valid one is entered
        while True:
            password = input('Enter a password for the new database: ')
            if checkpass(password):
                break
            else:
                print('Invalid password. Please enter a non-empty password that contains only alphanumeric characters and some special characters.')                         

        # Create a new database with the entered password and save it
        keepass = pykeepass.create_database(os.path.join(db_dir,'KPA.kdbx'),password)
        keepass.save()

        # Function to hash the password and return the hash value
        def Hashing_Password(password_On_Clear):
            password_bytes = password_On_Clear.encode('utf-8')
            hash_object = hashlib.new('sha256')
            hash_object.update(password_bytes)
            hash_value = hash_object.hexdigest()
            return hash_value
        
        # Hash the password and save the hash value to a file in the key directory
        hash_value = Hashing_Password(password)
        Hash_Key = open(os.path.join(key_dir,'KEY.txt'),'w')
        Hash_Key.write(hash_value)
        Hash_Key.close()

    # Get a list of all key files in the key directory
    key_files = glob.glob(os.path.join(key_dir, '*.txt'))

    # Return the paths for the database and key directories, and the list of database and key files
    return db_dir, database_files, key_dir, key_files

# Call the initializer function
initializer()
