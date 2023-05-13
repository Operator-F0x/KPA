from Database_Strument.Database_Manager import KPA

KPA_ISTANCE = KPA()
DATABASE = KPA_ISTANCE.auto_choose_database()
KPA_PYKEEPASS = KPA_ISTANCE.load_database(DATABASE)

