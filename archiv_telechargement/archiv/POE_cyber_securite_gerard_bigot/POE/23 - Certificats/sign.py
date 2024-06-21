from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Génération d'une nouvelle paire de clés RSA pour la démonstration de signature numérique
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Message à signer
message = b"Message tres important pour la signature numerique."

# Signature du message avec la clé privée
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Tentative de vérification de la signature avec la clé publique
verification_result = False
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    verification_result = True
except Exception as e:
    verification_result = False

(signature, verification_result)
print("message : ", message )
print("signature : ",  signature)
print("verification_result : ",  verification_result)
