import pykeepass
import os
from Toolbox.initializer import initializer
from Toolbox.Hash_Gestion import create_hash, save_hash, get_password




def create_new_database():

    db_dir,  _  , key_dir,  _  = initializer()

    # Prompt the user to enter a password until a valid one is entered
    password = get_password()
    
    # Create a new database with the entered password and save it
    keepass = pykeepass.create_database(os.path.join(db_dir, 'KPA.kdbx'), password)
    keepass.save()

    hash_value , salt= create_hash(password)
    with open(os.path.join(key_dir, 'HASH.txt'), 'w') as f:
        f.write(str(hash_value))
    

    save_hash(hash_value, salt)
    

if __name__ == '__main__':
    None