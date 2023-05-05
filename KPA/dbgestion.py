from initializer import initializer
from pykeepass import PyKeePass
import os

def dbLoad():
    
    # Get the current working directory, database directory, database file name, key directory, and key file name
    db_dir, database_files, key_dir, key_file = initializer()
    
    # Get the path separator for the current operating system
    
    # Create a string containing the full path to the KeePass database file
    Autodatabase = os.path.join( db_dir, database_files[0] )
    
    # Open the key file, read its contents, and assign the password to the Autokey variable
    keyOpen = open( os.path.join(key_dir, key_file[0]) ) 
    keyRead = keyOpen.read()
    Autokey = keyRead
    
    # Create a PyKeePass object using the Autodatabase and Autokey variables
    Keepass = PyKeePass(Autodatabase, password = Autokey)

    # Return the PyKeePass object
    return Keepass



Keepass = dbLoad()


def AddEntry(Prompt, Title, Username, Password, Url, Notes):
    if Prompt == 'Save':
        Keepass.save()
 
    group = Keepass.find_groups_by_name('KPAutomated') #hard Coded Default group change if u want choose other group

    if Prompt == 'Newentry' and Keepass.find_entries_by_title(Title) and Keepass.find_entries_by_username(Username) and Keepass.find_entries_by_password(Password):
            
            print('You are entering an entry that has the same Title or Password as another existing key')
            print('Warning, you are also using this password for another entry')
            print('already exists I have not added this new entry')
    else:
            Keepass.add_entry(group, Title, Username, Password, Url, Notes)

        


