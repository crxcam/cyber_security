Pour ajouter des certificats SSL/TLS émis par une autorité de certification (CA) à Apache pour un site nommé `poec.lan`, suis cette procédure détaillée :

### Étape 1 : Obtenir les certificats
1. **Certificat du serveur** (`cert.pem` ou `server.crt`)
2. **Clé privée** (`privkey.pem` ou `server.key`)
3. **Chaîne de certificats intermédiaires** (souvent `chain.pem` ou `intermediate.crt`)

### Étape 2 : Copier les certificats sur le serveur
Place les fichiers des certificats dans un répertoire sécurisé sur ton serveur, par exemple `/etc/ssl/poec.lan/`.

### Étape 3 : Configuration d'Apache
1. **Ouvre le fichier de configuration d'Apache pour ton site**. Ce fichier se trouve généralement dans `/etc/apache2/sites-available/` ou `/etc/httpd/conf.d/`. Le nom du fichier peut être `poec.lan.conf` ou similaire.

2. **Ajoute ou modifie les directives suivantes** pour activer SSL et spécifier les chemins vers tes certificats :

```apache
<VirtualHost *:443>
    ServerName poec.lan
    DocumentRoot /var/www/poec.lan

    SSLEngine on
    SSLCertificateFile /etc/ssl/poec.lan/cert.pem
    SSLCertificateKeyFile /etc/ssl/poec.lan/privkey.pem
    SSLCertificateChainFile /etc/ssl/poec.lan/chain.pem

    <Directory /var/www/poec.lan>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/poec.lan-error.log
    CustomLog ${APACHE_LOG_DIR}/poec.lan-access.log combined
</VirtualHost>
```

3. **Active le module SSL et le site** si ce n'est pas déjà fait :

```bash
sudo a2enmod ssl
sudo a2ensite poec.lan.conf
```

### Étape 4 : Tester la configuration
1. **Vérifie la syntaxe de la configuration d'Apache** :

```bash
sudo apachectl configtest
```

2. **Redémarre Apache** pour appliquer les modifications :

```bash
sudo systemctl restart apache2
```
ou 
```bash
sudo service apache2 restart
```

### Étape 5 : Vérifier le fonctionnement du certificat
Ouvre ton navigateur et accède à `https://poec.lan`. Vérifie que le certificat SSL est bien appliqué et que le site est accessible en HTTPS sans erreur de certificat.

### Notes supplémentaires :
- **Sécurité** : Assure-toi que les fichiers de clé privée sont protégés par des permissions adéquates (ex : `chmod 600`).
- **Renouvellement** : Note la date d'expiration de ton certificat et planifie son renouvellement à temps pour éviter des interruptions de service.

En suivant ces étapes, ton site `poec.lan` devrait être configuré pour utiliser les certificats émis par ton autorité de certification. Si tu rencontres des problèmes ou des erreurs, n'hésite pas à me fournir les détails pour que je puisse t'aider à les résoudre.