Les services "*beat" sont des agents légers utilisés dans l'écosystème Elastic, notamment avec Kibana, Elasticsearch et Logstash, pour collecter différents types de données depuis des machines et les envoyer vers Elasticsearch pour analyse et visualisation dans Kibana. Chaque "beat" est spécialisé dans la collecte d'un type spécifique de données. Voici les principaux *beats utilisés dans ce contexte :

### 1. **Filebeat**
- **Fonction** : Filebeat est conçu pour la collecte, le suivi et l'envoi de fichiers journaux (log files) vers Elasticsearch ou Logstash. 
- **Utilisation typique** : Idéal pour centraliser les logs de serveurs, d'applications et de services. Filebeat prend en charge de nombreux formats de logs et peut suivre les modifications en temps réel, facilitant ainsi l'analyse des logs sans interrompre les services.

### 2. **Metricbeat**
- **Fonction** : Metricbeat est utilisé pour collecter et expédier des métriques et des statistiques systèmes et de services. 
- **Utilisation typique** : Il peut collecter des métriques de CPU, mémoire, disque, réseau, et bien d'autres encore, ainsi que des statistiques spécifiques à des services comme Nginx, Apache, MongoDB, et d'autres.

### 3. **Packetbeat**
- **Fonction** : Packetbeat est un agent de surveillance du trafic réseau qui analyse et transmet des informations sur les transactions et les flux de trafic.
- **Utilisation typique** : Analyse des performances réseau, détection des anomalies de trafic, et diagnostic des problèmes de connectivité ou de latence entre services.

### 4. **Auditbeat**
- **Fonction** : Auditbeat est axé sur la sécurité et l'audit. Il collecte des données sur les accès aux fichiers, les modifications de configurations, et les activités suspectes sur les hôtes.
- **Utilisation typique** : Surveillance des accès et modifications de fichiers sensibles, suivi des commandes exécutées sur des serveurs, et collecte de données pour l'analyse de comportements malveillants.

### 5. **Heartbeat**
- **Fonction** : Heartbeat surveille la disponibilité des services en envoyant des requêtes périodiques pour vérifier leur état et leur performance.
- **Utilisation typique** : Monitoring de la disponibilité de sites web, d'applications web, et de services réseau à travers des tests ICMP, TCP, ou HTTP.

### 6. **Winlogbeat**
- **Fonction** : Winlogbeat est conçu pour les systèmes Windows pour collecter et envoyer les logs d'événements Windows (Windows Event Logs).
- **Utilisation typique** : Surveillance des événements de sécurité Windows, des logs d'applications et des logs systèmes pour l'analyse et la détection d'incidents de sécurité.

### Intégration et Utilisation dans Kibana

Ces *beats sont des composants clés pour fournir des données en temps réel à Kibana. Une fois que les données sont collectées par les *beats et stockées dans Elasticsearch, elles peuvent être visualisées et analysées dans Kibana à travers des tableaux de bord, des graphiques et d'autres visualisations. Cette intégration permet aux équipes de mieux comprendre les performances, la sécurité et l'état général de leur infrastructure et applications.