from Database_Strument.load_database import kpa

def group_parse():

    group = kpa.find_groups_by_name('KPA')
    if not group:
        group = kpa.add_group(kpa.root_group, 'KPA')

    return group

