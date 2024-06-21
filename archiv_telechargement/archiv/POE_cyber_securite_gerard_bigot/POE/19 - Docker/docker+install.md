Pour installer Docker sur Ubuntu en utilisant les paquets disponibles dans les dépôts officiels d'Ubuntu, suivez ces étapes simples. Gardez à l'esprit que ces paquets peuvent ne pas être la dernière version de Docker, mais ils sont testés et maintenus par l'équipe d'Ubuntu pour garantir la stabilité et la compatibilité.

### Étape 1: Mise à jour de votre système
Avant de commencer l'installation, assurez-vous que tous les paquets de votre système sont à jour. Ouvrez un terminal et exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt upgrade
```

### Étape 2: Installer Docker et composer
Ubuntu possède un paquet `docker.io` qui est le moteur Docker.
Ubuntu posséde un paquet `docker-composer-v2` pour faciliter la mise en place de service multi-logiciels.

Pour l'installer, utilisez la commande suivante :

```bash
sudo apt install docker.io docker-compose-v2
```

### Étape 3: Démarrer et activer Docker
Après l'installation, assurez-vous que le service Docker est démarré et configuré pour se lancer au démarrage du système :

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Étape 4: Vérifier l'installation
Pour vérifier que Docker a été installé correctement et fonctionne, exécutez la commande suivante pour lancer une image de test (par exemple, hello-world) :

```bash
sudo docker run hello-world
```

Si Docker est correctement installé, cette commande téléchargera une image de test et l'exécutera dans un conteneur. Vous verrez un message indiquant que Docker fonctionne correctement.

### Étape 5: Gérer Docker en tant qu'utilisateur non-root (facultatif)
Par défaut, vous devez utiliser `sudo` pour exécuter les commandes Docker. Pour permettre à votre utilisateur d'exécuter des commandes Docker sans `sudo`, ajoutez votre utilisateur au groupe Docker avec cette commande :

```bash
sudo usermod -aG docker ${USER}
```

Vous devrez vous déconnecter et vous reconnecter ou utiliser la commande :

```bash
newgrp docker
newgrp
```

pour que ces modifications prennent effet.

La commande
 
```bash
id
```
permet de valider l'apparition du group docker dans la liste des groupes de l'utilisateur.

Maintenant, "hello-world' (ainsi que d'autres comandes) fonctionne sans sudo :

```bash
docker run hello-world
docker info
docker ps
docker search ubuntu
```

### Étape 6: Configuration de Docker (facultatif)
Pour des configurations plus avancées, comme la modification du stockage de Docker ou la configuration de Docker pour utiliser un proxy, vous pouvez éditer ou créer de nouveaux fichiers de configuration dans `/etc/docker/`.

Par exemple, pour configurer Docker pour qu'il démarre avec des options spécifiques, vous pouvez éditer le fichier de service systemd :

```bash
sudo systemctl edit docker.service
```

Et ajoutez des modifications personnalisées sous la forme d'override pour les options de démarrage.

### Conclusion
Vous avez maintenant Docker installé en utilisant les paquets standards d'Ubuntu. Cette méthode est idéale pour les utilisateurs et les administrateurs qui préfèrent la facilité d'installation et la stabilité des paquets maintenus par Ubuntu au lieu des toutes dernières fonctionnalités.