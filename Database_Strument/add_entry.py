from Database_Strument.load_database import kpa
from Database_Strument.group_parse import group_parse

def AddEntry(Title, Username, Password, Url, Notes):
    
    group = group_parse()

    if  kpa.find_entries_by_username(Username) and kpa.find_entries_by_password(Password):
            
        print('You are entering an entry that has the same Username and Password as another existing key')
        print('Warning, you are also using this password for another entry')
        print('already exists I have not added this new entry')
    else:
        kpa.add_entry(group, Title, Username, Password, Url, Notes)

    kpa.save()

    return True