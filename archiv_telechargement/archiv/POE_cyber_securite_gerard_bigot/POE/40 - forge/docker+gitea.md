
```bash
sudo adduser --system --shell /bin/bash --gecos 'Git Version Control' --group --disabled-password --home /home/gitea gitea

info: Adding system user 'gitea' **(UID 118)** ...  
info: Adding new group 'gitea' **(GID 131)** ...  
info: Adding new user 'gitea' (UID 118) with group `gitea' ...   
```

mkdir ~/gitea
cd ~/gitea

Vi docker-compose.yml

```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=<giteaUID>	
      - USER_GID=<giteaGUID>
    restart: always
    networks:
      - gitea
    volumes:
      - ./gitea:/data
      - /home/gitea/.ssh/:/data/git/.ssh
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
#     - "127.0.0.1:3000:3000"
#     - "127.0.0.1:2222:22"
      - "3000:3000"
      - "2222:22"
```

Validez

Cliquez sur le lien " Pas de compte ? Inscrivez-vous maintenant." Pour démarrer.

Créez un repo en cliquant sur le +
Clonez un repo distant en cliquant sur "Migrez-le ici."