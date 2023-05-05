import os , glob, hashlib, pykeepass,re

def initializer():
                                                 
    cwd = os.getcwd()

    db_dir = os.path.join( cwd, 'DB' )    
    key_dir = os.path.join( cwd, 'key' )
    
    os.makedirs( db_dir, exist_ok=True )
    os.makedirs( key_dir, exist_ok=True )

    
    database_files = glob.glob(os.path.join(db_dir, '*.kdbx'))

    PASSWORD_REGEX =  r'^[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+$'
    def validate_password(password):
        return bool(re.match(PASSWORD_REGEX, password))
    
    if not database_files:
        print('No database found. Please create a password for the new database.')
        while True:
            password = input('Enter a password for the new database: ')
            if validate_password(password):
                break      
        pykeepass.pykeepass.create_database('KPA', password)
    key_files = glob.glob(os.path.join(key_dir, '*.txt'))


    return db_dir, database_files, key_dir, key_files

initializer()
