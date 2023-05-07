import os
import glob

def initializer():
    # Get the current working directory
    cwd = os.getcwd()

    # Define the paths for the database and key directories
    database_dir = os.path.join(cwd, 'kpa', 'DB')
    key_dir = os.path.join(cwd, 'kpa', 'KEY')

    # Create the database and key directories if they don't exist
    os.makedirs(database_dir, exist_ok=True)
    os.makedirs(key_dir, exist_ok=True)

    # Get a list of all database files in the database directory
    database_files = glob.glob(os.path.join(database_dir, 'KPA.kdbx'))

    # Get a list of all key files in the key directory
    key_files = glob.glob(os.path.join(key_dir, 'HASH.txt'))

    # Return the paths for the database and key directories, and the list of database and key files
    return database_dir, database_files, key_dir, key_files or []


