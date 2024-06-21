**Kubernetes**, souvent appelé **K8s**, est un système open source pour l'automatisation du déploiement, la mise à l'échelle et la gestion des applications conteneurisées. Développé initialement par Google et maintenant maintenu par la Cloud Native Computing Foundation, Kubernetes est devenu le standard de facto pour l'orchestration de conteneurs, permettant aux organisations de déployer, maintenir et mettre à l'échelle des applications de manière efficace et fiable dans des environnements de cloud ou sur site.

### Fonctionnalités clés de Kubernetes

1. **Orchestration de conteneurs** :
   - Kubernetes gère le cycle de vie des conteneurs dans des environnements distribués, assurant que l'état des applications corresponde toujours à celui spécifié par l'utilisateur.

2. **Automatisation du déploiement et de la mise à l'échelle** :
   - Il automatise le déploiement des applications, leur mise à l'échelle en ajoutant ou supprimant des instances de conteneurs pour s'adapter à la charge, et leur mise à jour avec des stratégies de déploiement définies pour minimiser les interruptions.

3. **Gestion des ressources** :
   - Kubernetes gère les ressources informatiques, de stockage et de réseau pour les conteneurs. Il permet de définir des requêtes et des limites de ressources pour garantir une utilisation optimale.

4. **Service Discovery et Load Balancing** :
   - Kubernetes expose automatiquement les conteneurs à l'aide de DNS ou d'adresses IP et équilibre la charge entre eux pour répartir le trafic.

5. **Auto-réparation** :
   - Il surveille l'état des conteneurs et redémarre automatiquement les conteneurs qui échouent, remplacent ceux qui ne répondent pas, et tue ceux qui ne répondent pas aux vérifications de santé définies par l'utilisateur.

### Architecture de Kubernetes

Kubernetes suit une architecture maître-nœud :

- **Maître (Master)** : Le maître coordonne le cluster, gérant la planification des déploiements et la communication entre les différents composants. Les composants du maître incluent l'API Server, le Scheduler, le Controller Manager et etcd.
  
- **Nœuds (Nodes)** : Les nœuds sont les machines (physiques ou virtuelles) sur lesquelles les conteneurs sont exécutés. Chaque nœud exécute les services nécessaires pour communiquer avec le maître et gérer les conteneurs, y compris Kubelet, le Kube Proxy et le conteneur runtime (comme Docker ou rkt).

~~### Installation de Kubernetes~~
**On va plutôt utiliser KIND**

L'installation de Kubernetes peut varier en fonction de l'environnement (développement, test ou production) et de la plateforme (local, cloud). Pour un essai local simple, **Minikube** est une option populaire :

1. **Installer Minikube** :
   - Minikube permet de créer un cluster Kubernetes local sur une machine virtuelle. Pour l'installer :
     ```bash
     curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube /usr/local/bin
     ```

2. **Démarrer Minikube** :
   - Exécutez Minikube pour démarrer le cluster :
     ```bash
     minikube start
     ```

### Utilisation de Kubernetes

L'utilisation de Kubernetes se fait principalement à travers `kubectl`, la ligne de commande pour interagir avec le cluster Kubernetes.

1. **Créer des déploiements** :
   - Pour déployer une application, vous utilisez des fichiers YAML décrivant les ressources, par exemple :
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: nginx-deployment
     spec:
       replicas: 3
       selector:
         matchLabels:
           app: nginx
       template:
         metadata:
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: nginx:1.14.2
             ports:
             - containerPort: 80
     ```
   - Appliquez ce fichier avec :
     ```bash
     kubectl apply -f deployment.yaml
     ```

2. **Mise à l'échelle des applications** :
   - Pour changer le nombre de répliques :
     ```bash
     kubectl scale deployment/nginx-deployment --replicas=5
     ```

3. **Mise à jour et déploiement continu** :
   - Kubernetes facilite les mises à jour sans interruption en utilisant des stratégies de déploiement comme RollingUpdate.

### Avantages de Kubernetes

- **Flexibilité et Portabilité** : Fonctionne avec n'importe quel environnement de conteneurs (Docker, rkt) et sur n'importe quel type de plateforme (cloud, VMs, bare metal).
- **Écosystème riche et dynamique** : De nombreux outils et extensions sont disponibles pour étendre les fonctionnalités de Kubernetes.
- **Scalabilité et Fiabilité** : Conçu pour des environnements à grande échelle, il peut gérer des milliers de conteneurs sans sacrifier la performance.

En résumé, Kubernetes est l'outil de choix pour l'orchestration de conteneurs à grande échelle, offrant une robustesse, une scalabilité et une flexibilité qui répondent aux besoins des entreprises modernes pour déployer et gérer des applications complexes dans des environnements de cloud hybrides ou multi-clouds.