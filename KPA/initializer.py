import os , glob, hashlib

def initializer():
                                                 
    cwd = os.getcwd()

    db_dir = os.path.join( cwd, 'DB' )    
    key_dir = os.path.join( cwd, 'key' )
    
    os.makedirs( db_dir, exist_ok=True )
    os.makedirs( key_dir, exist_ok=True )

    database_files = glob.glob(os.path.join(db_dir, '*.kdbx'))
    print(database_files)
    key_files = glob.glob(os.path.join(key_dir, '*.txt'))


    return db_dir, database_files, key_dir, key_files

initializer()
