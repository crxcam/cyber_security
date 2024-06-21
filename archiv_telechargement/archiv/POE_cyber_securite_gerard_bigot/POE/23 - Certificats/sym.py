from cryptography.fernet import Fernet

# Génération d'une clé de chiffrement
cle = Fernet.generate_key()

# Création d'une instance de Fernet avec la clé générée
fernet = Fernet(cle)

# Message à chiffrer
message = "Ceci est un message secret."

# Chiffrement du message
message_chiffre = fernet.encrypt(message.encode())

# Déchiffrement du message
message_dechiffre = fernet.decrypt(message_chiffre).decode()

print ("cle : ", cle) 
print("Message : ",  message)
print("Message chiffré : ",  message_chiffre)
print("Message déchiffré : ",  message_dechiffre)
