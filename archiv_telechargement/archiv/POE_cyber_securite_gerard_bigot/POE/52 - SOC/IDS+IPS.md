Les termes IDS (Intrusion Detection System) et IPS (Intrusion Prevention System) désignent deux systèmes cruciaux dans la protection des réseaux informatiques contre les cyberattaques. Ces technologies jouent un rôle essentiel dans la surveillance et la défense des infrastructures de réseau. Voici un aperçu détaillé de chacun :

### IDS (Intrusion Detection System)

- **Fonction** : Un IDS est conçu pour détecter les activités malveillantes ou suspectes dans un réseau ou un système. Il surveille le trafic et les activités pour identifier les comportements anormaux ou les signatures de menaces connues.
  
- **Types d'IDS** :
  - **NIDS (Network IDS)** : Surveille le trafic de réseau à la recherche de signes d'attaques ou d'activités suspectes.
  - **HIDS (Host-based IDS)** : Installé sur des machines individuelles (serveurs, ordinateurs), il surveille les activités internes et les fichiers systèmes pour détecter des intrusions.

- **Méthodes de Détection** :
  - **Détection basée sur les signatures** : Utilise des bases de données de signatures connues pour identifier des menaces spécifiques.
  - **Détection basée sur l'anomalie** : Analyse le comportement habituel du réseau ou du système pour détecter des écarts qui pourraient indiquer une intrusion.

- **Avantages** : Fournit des alertes précoces sur les tentatives d'intrusion, permettant aux équipes de sécurité de réagir rapidement.

### IPS (Intrusion Prevention System)

- **Fonction** : Un IPS, tout en ayant les capacités de détection d'un IDS, est aussi capable de prendre des mesures préventives pour arrêter ou atténuer les attaques détectées. Il s'interpose directement dans le flux de trafic pour bloquer les activités malveillantes.

- **Types d'IPS** :
  - **NIPS (Network IPS)** : Agit au niveau du réseau pour inspecter et bloquer les paquets malveillants.
  - **HIPS (Host-based IPS)** : Fonctionne sur des hôtes individuels pour contrôler les processus et les connexions, empêchant les activités malveillantes.

- **Méthodes d'Action** :
  - **Blocage automatique** : L'IPS peut automatiquement bloquer le trafic suspect ou les connexions basées sur les règles prédéfinies.
  - **Réinitialisation de la connexion** : Peut réinitialiser les connexions réseau pour arrêter les communications suspectes.
  - **Quarantaine** : Isoler les systèmes ou les processus infectés pour prévenir la propagation de l'attaque.

- **Avantages** : Non seulement détecte les intrusions, mais intervient également pour empêcher les dommages, offrant ainsi une couche de protection proactive.

### Comparaison et Complémentarité

- **Complémentarité** : Souvent, les IDS et IPS sont utilisés en tandem pour une protection complète. L'IDS sert de système d'alerte précoce, tandis que l'IPS agit pour bloquer activement les menaces détectées.
- **Déploiement** : Pour une sécurité optimale, les entreprises déploient ces systèmes à différents points stratégiques de leur réseau pour assurer à la fois la détection et la prévention des intrusions.

En conclusion, l'utilisation combinée des IDS et des IPS forme une approche robuste pour la surveillance, la détection et la prévention des intrusions, renforçant ainsi la sécurité des réseaux et des systèmes informatiques contre les cyberattaques.