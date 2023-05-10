import os, glob
import pykeepass
from Toolbox.Hash_Gestion import get_password, check_password, create_hash, save_hash
class KPA:
	def __init__(self):

		database_dir = os.path.join(os.getcwd(), 'kpa', 'DB')
		database_list_files = glob.glob(os.path.join(database_dir, 'KPA.kdbx'))
		# Create the database directory if it does not exist
		os.makedirs(database_dir, exist_ok=True)
		# If there are no KPA database files in the directory, create a new database
		if not database_list_files:
			# Prompt the user to enter a password until a valid one is entered
			prompt = 'Enter the password of the new KPA database --> '
			password = get_password(prompt)
			# Create a new database with the entered password and save it
			keepass = pykeepass.create_database(os.path.join(database_dir, 'KPA.kdbx'), password)
			keepass.save()
			hash_value , salt= create_hash(password)
			save_hash(hash_value, salt)
			print('New KPA database created successfully.')

	def auto_choose_database(self):

		database_list_files = glob.glob(os.path.join('kpa','DB', 'KPA.kdbx'))
		database = database_list_files[0]
			
		return database

	def load_database(self,database):
		password = None
		prompt = 'Enter your KPA database password --> '
		while True:
			password = get_password(prompt)
			if check_password(password):
				break
			else:
				print('Wrong Password!')
		# Create a PyKeePass object for the KPA database with the entered password
		KPA = pykeepass.PyKeePass(database, password)
		# Return the PyKeePass object
		print('Database loaded')
		return KPA

	def Add_Entry(self, kpa: object, group,  Title: str, Username: str, Password: str, Url: str, Notes: str):
		# Check if an entry with the same username and password already exists
		if  kpa.find_entries_by_username(Username) and kpa.find_entries_by_password(Password):
			# If an entry with the same username and password already exists, print a warning message
			print('Warning: an entry with the same Username and Password already exists')
			print('Warning: you are also using this password for another entry')
			print('Warning: the new entry has not been added')
		else:
			# If an entry with the same username and password does not exist, add the new entry
			kpa.add_entry(group, Title, Username, Password, Url, Notes)
		kpa.save()
		# Return True to indicate that the entry was added successfully
		return True