import os , glob, hashlib,re 
from pykeepass import pykeepass


def initializer():
                                                 
    cwd = os.getcwd()


    db_dir = os.path.join( cwd,'KPA', 'DB' )    
    key_dir = os.path.join( cwd,'KPA', 'KEY' )
    
    os.makedirs( db_dir, exist_ok=True )
    os.makedirs( key_dir, exist_ok=True )

    
    
    database_files = glob.glob(os.path.join(db_dir, '*.kdbx'))

#  If no database exists, a default one is created and I request to create a key for this database
    if not database_files:
        print('No database found. Please create a password for the new database.')    

        password = ''

        def checkpass(PSW):
            PASSWORD_REGEX = r'^[a-zA-Z0-9!"#$%&]+$'
            return bool(re.match(PASSWORD_REGEX, PSW))
        
        while True:
            password = input('Enter a password for the new database: ')
            if checkpass(password):
                break
            else:
                print('Invalid password. Please enter a non-empty password that contains only alphanumeric characters and some special characters.')                         
        keepass = pykeepass.create_database(os.path.join(db_dir,'KPA.kdbx'),password)
        keepass.save()


        def Hashing_Password(password_On_Clear):

            password_bytes = password_On_Clear.encode('utf-8')
            hash_object = hashlib.new('sha256')
            hash_object.update(password_bytes)
            hash_value = hash_object.hexdigest()

            return hash_value
        
    hash_value = Hashing_Password(password)
    Hash_Key = open(os.path.join(key_dir,'KEY.txt'),'w')
    Hash_Key.write(hash_value)
    Hash_Key.close()



    key_files = glob.glob(os.path.join(key_dir, '*.txt'))


    return db_dir, database_files, key_dir, key_files

initializer()


