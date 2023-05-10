def group_root(kpa: object):
    
    group = kpa.find_groups_by_name('KPA')
    if not group:
        group = kpa.add_group(kpa.root_group, 'KPA')

    return group

