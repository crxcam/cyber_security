Les termes "IOC" (Indicator of Compromise) et "IOA" (Indicator of Attack) sont fondamentaux dans le domaine de la cybersécurité, surtout en ce qui concerne la détection et la réponse aux incidents de sécurité. Bien qu'ils partagent des objectifs similaires, ils représentent des approches et des perspectives différentes sur la sécurité.

### IOC (Indicator of Compromise)

Les IOC sont des éléments de preuve utilisés pour identifier une activité malveillante déjà réalisée ou en cours dans un système informatique ou un réseau. Ces indicateurs sont souvent utilisés pour détecter des compromissions après qu'elles se soient produites ou pendant qu'elles se déroulent. Voici des exemples courants d'IOC :

- **Adresses IP malveillantes** : Adresses IP utilisées par des acteurs malveillants pour mener des attaques ou communiquer avec des malwares.
- **Domaines et URLs suspects** : Liens utilisés dans des activités de phishing ou pour distribuer des malwares.
- **Hash de fichiers** : Empreintes numériques de fichiers malveillants permettant de les identifier rapidement.
- **Signatures de Malware** : Séquences de code spécifiques à un malware particulier.
- **Chaînes et motifs dans les fichiers** : Textes ou codes binaires qui suggèrent une compromission, tels que des clés de chiffrement ou des mots de passe en dur.

### IOA (Indicator of Attack)

Les IOA, en revanche, sont utilisés pour détecter les tentatives d'attaque avant qu'une compromission ne soit effective. Ils se concentrent sur les tactiques, techniques et procédures (TTP) utilisées par les attaquants, plutôt que sur les artefacts laissés derrière eux. Voici des exemples d'IOA :

- **Séquences de comportement suspect** : Comme les tentatives répétées de connexion échouée ou les mouvements latéraux inhabituels dans un réseau.
- **Anomalies de trafic réseau** : Augmentations soudaines du trafic ou communications vers des destinations inhabituelles qui peuvent indiquer une exfiltration de données.
- **Utilisation anormale des ressources système** : Utilisation excessive du CPU ou de la mémoire qui pourrait indiquer un cryptominage ou une exploitation de failles.
- **Modifications suspectes de la configuration** : Changements inattendus dans les paramètres de sécurité ou les fichiers système qui pourraient indiquer une tentative d'établissement de persistance.

La distinction entre IOC et IOA est essentielle pour une stratégie de cybersécurité complète : les IOC aident à identifier et à comprendre les attaques qui ont déjà eu lieu ou sont en cours, tandis que les IOA sont cruciaux pour prévenir les attaques avant qu'elles ne réussissent. Une combinaison de ces deux types d'indicateurs permet une défense en profondeur plus robuste et proactive.