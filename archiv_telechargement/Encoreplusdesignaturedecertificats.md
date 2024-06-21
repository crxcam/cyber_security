# Configurer une Autorité de Certification (CA) locale pour générer un premier certificat. 

### Création de l'Autorité de Certification Racine

```bash
# Générer une clé privée pour l'Autorité de Certification Racine
openssl genrsa -out CA-ROOT.key

# Créer une demande de signature de certificat (CSR) pour la CA Racine
openssl req -new -key CA-ROOT.key -out CA-ROOT.csr -sha256

# Signer le CSR pour obtenir le certificat de la CA Racine (valide pour 365 jours)
openssl x509 -req -days 365 -in CA-ROOT.csr -out CA-ROOT.crt -signkey CA-ROOT.key

# Informations du sujet du certificat
* subject=C=FR, ST=idf, L=Paris, O=M2I, OU=IAM, CN=gerard
```

### Configuration de l'Autorité de Certification

```bash
# Édition du fichier de configuration pour la CA
vi ca-ssl.conf
```
Contenu du fichier `ca-ssl.conf`:
```ini
[ ca ]
default_ca = M2I_ca

[ M2I_ca ]
# Informations de la CA Racine
certificate = CA-ROOT.crt
private_key = CA-ROOT.key
new_certs_dir = .
database = ./index.txt
serial = ./serial

default_md = sha512
default_days = 365
policy = M2I_policy

[ M2I_policy ]
countryName = match
stateOrProvinceName = match
organizationName = match
organizationalUnitName = optional
commonName = supplied
emailAddress = optional

[ req ]
default_bits = 2048
distinguished_name = req_distinguished_name
string_mask = utf8only
default_md = sha512
```

### Préparation des fichiers nécessaires pour la CA

```bash
# Créer un fichier index pour le suivi des certificats signés
touch index.txt

# Initialiser le fichier de sérialisation pour le premier certificat
echo '01' > serial
```

### Signature du Premier Certificat

```bash
# Générer une clé privée pour le premier certificat
openssl genrsa -out monpremiercert.key

# Créer une CSR pour le premier certificat
openssl req -new -key monpremiercert.key -out monpremiercert.csr

# Vérifier le contenu de la CSR
openssl req -text -noout -verify -in monpremiercert.csr | grep Subject:

# Utiliser la configuration de la CA pour signer le certificat
openssl ca -config ca-ssl.conf -out monpremiercert.crt -in monpremiercert.csr
```

Ces commandes détaillent le processus de création et de gestion d'une Autorité de Certification locale, ainsi que la génération et la signature d'un certificat client. Chaque étape est essentielle pour maintenir la sécurité et l'intégrité des communications sécurisées au sein de votre réseau ou de votre application.