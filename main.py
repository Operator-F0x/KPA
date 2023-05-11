from Database_Strument.Database_Manager import KPA
#
kpa_istance = KPA()
database = kpa_istance.auto_choose_database()
kpa = kpa_istance.load_database(database) 
