Trivy d'Aqua Security est un scanner de vulnérabilités simple et complet pour les conteneurs et d'autres artefacts, adapté à l'intégration continue (CI). Voici un tour d'horizon des fonctionnalités principales de Trivy en mode autonome (standalone) :

1. **Détection des Vulnérabilités** : Trivy est capable de détecter les vulnérabilités à la fois dans les paquets OS (comme Alpine, Red Hat, Debian, Ubuntu) et les dépendances d'applications (comme Bundler, Composer, npm, yarn). Cela le rend très utile pour les audits de sécurité approfondis.

2. **Facilité d'Utilisation** : Trivy est conçu pour être simple à utiliser. Une fois installé, il suffit de spécifier le nom d'une image ou d'un artefact pour démarrer l'analyse. Ce processus rapide permet une intégration aisée dans les flux de travail de développement.

3. **Vitesse** : Les premières analyses se terminent généralement en moins de 10 secondes, dépendant de votre réseau. Les analyses suivantes sont encore plus rapides, ce qui distingue Trivy d'autres scanners qui peuvent être plus lents lors de la première exécution.

4. **Installation Facile** : Trivy peut être installé via des commandes courantes comme `apt-get install`, `yum install` et `brew install`, sans nécessité de préparer une base de données ou d'autres librairies préalables.

5. **Précision Élevée** : Trivy montre une précision particulièrement élevée dans l'identification des vulnérabilités, surtout pour Alpine Linux et RHEL/CentOS, mais aussi pour d'autres systèmes d'exploitation.

6. **Support de Formats Multiples** : Trivy peut scanner des images de conteneur locales ou distantes, des systèmes de fichiers locaux, et des dépôts Git distants. Il prend en charge les formats d'image OCI et les archives tar.

7. **Détection de Mauvaises Configurations (IaC)** : Trivy intègre également des politiques de détection de mauvaises configurations pour Kubernetes, Docker, Terraform, entre autres, et permet l'utilisation de politiques personnalisées.

Trivy est directement disponible dans ubuntu grâce à snap : 

```bash
sudo snap install trivy
```

Pour plus de détails sur les fonctionnalités et les capacités de Trivy, vous pouvez consulter la [documentation officielle de Trivy](https://aquasecurity.github.io/trivy/v0.29.2/docs/).