Dans le répertoire de lancement des dockerfiles : 

```
mkdir -p docker/GLPI   
cd docker/GLPI
```

Créer un fichier nommé compose.yml avec ce contenu : 

```
version: "3.8"

services:
#MariaDB Container
  mariadb:
    image: mariadb:10.7
    container_name: mariadb
    hostname: mariadb
    environment:
      - MARIADB_ROOT_PASSWORD=password
      - MARIADB_DATABASE=glpidb
      - MARIADB_USER=glpi_user
      - MARIADB_PASSWORD=glpi

#GLPI Container
  glpi:
    image: diouxx/glpi
    container_name : glpi
    hostname: glpi
    ports:
      - "8080:80"

```

Lancer le composer : 

```
docker compose up -d
docker ps
sudo ss -ntlupd
```

Se connecter sur le serveur port 8080, accepter les mises à jour et fournir les informations suivantes :

``` 
Databse : Mariadb
user : glpi_user
password : glpi
```

Puis, se connecter avec l'un des comptes : 

| Login/Password   | Role  |
|:----------|:----------|
| glpi/glpi          | admin account    |
| tech/tech          | technical account    |
| normal/normal      | "normal" account   |
| post-only/postonly | post-only account   |

