Pour lancer et prévisualiser une instance de Mattermost à l'aide de Docker, suis ces étapes :

1. **Lance la commande Docker** :

   - Ouvre une fenêtre de terminal sur ton ordinateur.
   - Tape et exécute la commande suivante :
     ```
     docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview
     ```
     Cette commande va télécharger l'image Docker de Mattermost, créer un conteneur nommé `mattermost-preview`, et publier le port 8065 du conteneur sur le port 8065 de ton hôte local.

2. **Accède à Mattermost** :

   - Une fois que Docker a terminé de télécharger et de lancer l'image, ouvre un navigateur web.
   - Navigue vers `http://localhost:8065/` pour accéder à l'interface de Mattermost.

3. **Crée un compte** :

   - Sur la page d'accueil de Mattermost, clique sur « Don’t have an account » (Je n'ai pas de compte) situé dans le coin supérieur droit de l'écran pour créer un compte sur ton instance de prévisualisation.
   - Si tu ne vois pas cette option, assure-toi que la configuration « Enable open server » (Activer le serveur ouvert) est activée. Par défaut, ce réglage est désactivé pour les déploiements auto-hébergés de Mattermost.

4. **Connecte-toi à ton instance** :
   - Une fois ton compte créé, utilise tes identifiants pour te connecter à l'instance de prévisualisation de Mattermost.

Ces étapes te permettront de lancer une instance de prévisualisation de Mattermost localement pour évaluer ses fonctionnalités et son interface utilisateur.
