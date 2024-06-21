Pour ajouter le contrôle MFA (Multi-Factor Authentication) avec Google Authenticator dans le PAM (Pluggable Authentication Modules) pour SSH sur un système Linux, vous devez suivre plusieurs étapes. Cela inclut l'installation de Google Authenticator, la configuration de PAM et la modification de la configuration SSH.

Voici les étapes détaillées :

### Étape 1 : Installer Google Authenticator

Sur une distribution Debian/Ubuntu, vous pouvez installer Google Authenticator avec la commande suivante :

```bash
sudo apt-get update
sudo apt install ssh
sudo apt-get install libpam-google-authenticator
```

Sur une distribution Red Hat/CentOS, utilisez :

```bash
sudo yum install epel-release
sudo yum install google-authenticator
```

### Étape 2 : Configurer Google Authenticator pour un Utilisateur

Exécutez la commande suivante pour chaque utilisateur pour lequel vous souhaitez configurer Google Authenticator :

```bash
google-authenticator
```

Vous serez invité à répondre à quelques questions. Typiquement, vous voudrez répondre 'y' (oui) à toutes les questions :

- "Do you want authentication tokens to be time-based?" - Répondez 'y'.
- Ensuite, un code QR sera affiché que vous devrez scanner avec l'application Google Authenticator sur votre téléphone.
- Répondez 'y' aux autres questions pour mettre à jour votre fichier de configuration.

### Étape 3 : Configurer PAM

Modifiez le fichier de configuration PAM pour SSH en ajoutant Google Authenticator. Ouvrez le fichier `/etc/pam.d/sshd` avec un éditeur de texte :

```bash
sudo nano /etc/pam.d/sshd
```

Ajoutez la ligne suivante en dessous de la ligne `@include common-auth` pour activer Google Authenticator :

```plaintext
auth required pam_google_authenticator.so
```

### Étape 4 : Configurer SSH

Modifiez la configuration SSH pour utiliser l'authentification PAM. Ouvrez le fichier `/etc/ssh/sshd_config` avec un éditeur de texte :

```bash
sudo nano /etc/ssh/sshd_config
```

Changez pour yes le paramètre :
```
KbdInteractiveAuthentication yes
```

Vérifies au vous avez une ligne contenant : 
```plaintext
UsePAM yes
```

Et ajoutez en fin de fichier : 

```plaintext
AuthenticationMethods publickey,keyboard-interactive
```

Cela indique que SSH doit utiliser l'authentification par clé publique suivie d'une authentification interactive (comme Google Authenticator).

### Étape 5 : Redémarrer le Service SSH

Pour que les modifications prennent effet, redémarrez le service SSH :

```bash
sudo systemctl restart sshd
```

### Étape 6 : Tester la Configuration

Tentez de vous connecter via SSH pour vérifier que l'authentification à deux facteurs fonctionne correctement :

```bash
ssh your_user@your_server
```

Vous devriez être invité à entrer votre mot de passe suivi d'un code de vérification Google Authenticator.

### Résumé des Modifications

- **/etc/pam.d/sshd** :

  ```plaintext
  auth required pam_google_authenticator.so
  ```

- **/etc/ssh/sshd_config** :

  ```plaintext
  KbdInteractiveAuthentication yes
  AuthenticationMethods publickey,keyboard-interactive
  UsePAM yes
  ```

### Notes Supplémentaires

- Assurez-vous que votre serveur a un horloge correctement synchronisée avec NTP (Network Time Protocol) pour que les codes TOTP fonctionnent correctement.
- Si vous rencontrez des problèmes, vérifiez les journaux du système avec `journalctl -xe` ou les fichiers de journalisation spécifiques à SSH ou PAM.

En suivant ces étapes, vous devriez être en mesure d'ajouter avec succès une authentification MFA avec Google Authenticator pour SSH sur un système Linux.