from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Génération d'une paire de clés RSA (privée et publique)
cle_privee = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

cle_publique = cle_privee.public_key()

# Message à chiffrer
message = b"Ceci est un message secret asymetrique."

# Chiffrement du message avec la clé publique
message_chiffre = cle_publique.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Déchiffrement du message avec la clé privée
message_dechiffre = cle_privee.decrypt(
    message_chiffre,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

(message_chiffre, message_dechiffre)

print ("cle_privee : ", cle_privee)
print ("cle_publique : ", cle_publique)
print("Message : ",  message)
print("Message chiffré : ",  message_chiffre)
print("Message déchiffré : ",  message_dechiffre)
