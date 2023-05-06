import hashlib, os

def Hashing_Password(password_On_Clear):
    # Genera un salt casuale
    salt = os.urandom(16)

    # Aggiungi il salt alla password in chiaro
    salted_password = password_On_Clear.encode('utf-8') + salt

    # Genera l'hash utilizzando SHA-256
    hash_object = hashlib.sha256(salted_password)
    hash_value = hash_object.hexdigest()
    

    # Restituisci l'hash e il salt
    return hash_value, salt
