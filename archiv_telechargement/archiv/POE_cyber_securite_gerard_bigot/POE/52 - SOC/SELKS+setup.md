Voici une traduction en français de l'instruction d'installation basique que vous avez mentionnée :

### Installation Basique

1. Clonez le dépôt SELKS depuis GitHub :
   ```bash
   git clone https://github.com/StamusNetworks/SELKS.git
   ```
2. Accédez au répertoire Docker de SELKS :
   ```bash
   cd SELKS/docker/
   ```
3. Exécutez le script de configuration facile :
   ```bash
   ./easy-setup.sh
   ```
4. Utilisez Docker Compose pour lancer les conteneurs en arrière-plan :
   ```bash
   sudo -E docker compose up -d
   ```

Une fois les conteneurs actifs et en fonction, vous devriez simplement diriger votre navigateur vers `https://votre.ip.selks.ici/`. Si vous avez choisi d'installer Portainer durant l'installation, vous devez visiter `https://votre.ip.selks.ici:9443` pour définir le mot de passe administrateur de Portainer.

Si le script de configuration échoue, veuillez consulter la section d'installation manuelle de Docker et signaler un problème.

### Identifiants et Connexion

Pour accéder à Scirius, vous aurez besoin des identifiants suivants :

- **Utilisateur** : selks-user
- **Mot de passe** : selks-user

Cela devrait vous permettre de démarrer et d'utiliser SELKS pour surveiller et analyser la sécurité de votre réseau.