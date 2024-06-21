### Création de la clé et de la demande de signature de certificat (CSR) pour la CA Root

Génèrer une clé RSA privée pour votre autorité de certification racine (CA Root). 
Le fichier CA-ROOT.key contiendra cette clé privée.
```bash
    openssl genrsa -out CA-ROOT.key
```

Créer une nouvelle demande de signature de certificat (CSR) en utilisant la clé privée CA-ROOT.key. 
Le CSR est enregistré dans le fichier CA-ROOT.csr et est signé en utilisant l'algorithme SHA-256.
```bash
    openssl req -new -key CA-ROOT.key -out CA-ROOT.csr -sha256
```

Signer le CSR et génère un certificat X.509 (CA-ROOT.crt) qui est valide pour 365 jours. 
Ce certificat est auto-signé en utilisant la clé privée CA-ROOT.key.
```bash
    openssl x509 -req -days 365 -in CA-ROOT.csr -out CA-ROOT.crt -signkey CA-ROOT.key
```

Description du type de données à rentrer dans le questionnaire :
```
    * subject=C=FR  
    * ST=idf  
    * L=Paris  
    * O=M2I  
    * OU=IAM  
    * CN=gerard  
```
Ces commandes détaillent le processus de création et de gestion d'une Autorité de Certification locale, ainsi que la génération et la signature d'un certificat client. Chaque étape est essentielle pour maintenir la sécurité et l'intégrité des communications sécurisées au sein de votre réseau ou de votre application. 
### Configuration de l'Autorité de Certification

vi ca-ssl.conf

--------------------------

[ ca ]  
default_ca = POE_ca  

[ POE_ca ]  
certificate = CA-ROOT.crt  
private_key = CA-ROOT.key

new_certs_dir     = .  
database          = ./index.txt  
serial            = ./serial  

default_md = sha512 
default_days = 365  
policy = POE_policy  

[ POE_policy ]   
countryName             = match   
stateOrProvinceName     = match   
organizationName        = match   
organizationalUnitName  = optional   
commonName              = supplied   
emailAddress            = optional

[ req ]  
default_bits        = 2048   
distinguished_name  = req_distinguished_name   
string_mask         = utf8only   
default_md          = sha512   

----------------------------


### Description du fichier 
 * **[ ca ]** :
Définit le nom par défaut de la CA.  
 * **[ POE_ca ]** :  
Contient les paramètres de la CA, incluant :  
	+ le certificat de la CA    
	+ le répertoire pour les nouveaux certificats    
	+ la base de données des certificats signés (index.txt)    
	+ le fichier de séquence (serial)    
	+ le hachage par défaut (sha512)    
	+ la durée par défaut des certificats (365 jours)
 * **[ POE_policy ]** :   
Définit les politiques de vérification des champs du certificat lors de la signature.
 * **[ req ]** :  
Configure les paramètres par défaut pour les nouvelles demandes de certificats :  
	+ la taille des clés  
	+ le nom distingué requis   
	+ le hachage par défaut  

### Préparation des fichiers de la CA

Crée un fichier vide **index.txt** qui servira de base de données pour enregistrer tous les certificats émis par cette CA.
```bash
    touch index.txt
```

Initialise le fichier **serial** avec la valeur '01'. Ce fichier est utilisé pour attribuer un numéro unique à chaque certificat signé par la CA.
```bash
    echo '01' > serial
```

### Signature du premier certificat

Génèrer une clé privée pour votre premier certificat utilisateur. Le fichier monpremiercert.key contiendra cette clé.
```bash
    openssl genrsa -out monpremiercert.key
```

Créer un CSR pour le premier certificat en utilisant la clé monpremiercert.key. Le CSR est enregistré dans monpremiercert.csr.
```bash
    openssl req -new -key monpremiercert.key -out monpremiercert.csr
```

Vérifier le contenu du CSR monpremiercert.csr et afficher la ligne "Subject:" pour vérifier les informations du demandeur.
```bash
    openssl req -text -noout -verify -in monpremiercert.csr | grep Subject:
```

Utiliser la configuration de la CA (ca-ssl.conf) pour signer le CSR monpremiercert.csr et créer le certificat monpremiercert.crt.
```bash
    openssl ca -config ca-ssl.conf -out monpremiercert.crt -in monpremiercert.csr
```

Ces commandes détaillent le processus de création et de gestion d'une Autorité de Certification locale, ainsi que la génération et la signature d'un certificat client. Chaque étape est essentielle pour maintenir la sécurité et l'intégrité des communications sécurisées au sein de votre réseau ou de votre application. 
