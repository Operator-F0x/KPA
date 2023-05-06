from DB_Load import db_load

kpa = db_load()

def group_parse():

    group = kpa.find_groups_by_name('KPA')
    if not group:
        group = kpa.add_group(kpa.root_group, 'KPA')

    return group

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

        