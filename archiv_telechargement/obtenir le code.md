Pour obtenir le code temporaire d'une configuration avec TOTP (Time-based One-Time Password) comme MFA (Multi-Factor Authentication) en utilisant une extension de navigateur et une application mobile, suivez ces étapes :

### Utilisation d'une Application Mobile (Google Authenticator)

1. **Installer Google Authenticator sur votre téléphone :**
   - Sur iOS : Ouvrez l'App Store, recherchez "Google Authenticator", téléchargez et installez l'application.
   - Sur Android : Ouvrez le Google Play Store, recherchez "Google Authenticator", téléchargez et installez l'application.

2. **Ajouter un compte à Google Authenticator :**
   - Ouvrez l'application Google Authenticator.
   - Cliquez sur le bouton "+" pour ajouter un nouveau compte.
   - Vous avez deux options :
     - **Scanner un code QR** : Utilisez l'appareil photo de votre téléphone pour scanner le code QR fourni par le service que vous configurez.
     - **Entrer une clé manuellement** : Si vous avez une clé secrète fournie par le service, sélectionnez "Entrer une clé manuellement" et saisissez la clé.

3. **Obtenir le code temporaire :**
   - Après avoir ajouté le compte, Google Authenticator générera un code temporaire (valide pendant 30 secondes) que vous pourrez utiliser pour vous authentifier.

### Utilisation d'une Extension de Navigateur (Authenticator Extension)

1. **Installer une extension TOTP pour votre navigateur :**
   - Pour Chrome : Ouvrez le Chrome Web Store, recherchez "Authenticator", téléchargez et installez l'extension "Authenticator" développée par "Authenticator".
   - Pour Firefox : Ouvrez les modules complémentaires Firefox, recherchez "Authenticator", téléchargez et installez l'extension.

2. **Ajouter un compte à l'extension :**
   - Cliquez sur l'icône de l'extension dans la barre d'outils de votre navigateur.
   - Cliquez sur le bouton "+" pour ajouter un nouveau compte.
   - Vous avez deux options :
     - **Scanner un code QR** : Utilisez la fonctionnalité de scan QR de l'extension pour scanner le code QR fourni par le service que vous configurez.
     - **Entrer une clé manuellement** : Si vous avez une clé secrète fournie par le service, sélectionnez "Entrer une clé manuellement" et saisissez la clé.

3. **Obtenir le code temporaire :**
   - Après avoir ajouté le compte, l'extension générera un code temporaire (valide pendant 30 secondes) que vous pourrez utiliser pour vous authentifier.

### Exemple de Clé Secrète TOTP

Si vous avez une clé secrète TOTP, voici comment vous pouvez la configurer dans les deux options ci-dessus :

#### Exemple avec Google Authenticator (Mobile)

- Ouvrez Google Authenticator.
- Appuyez sur le "+".
- Sélectionnez "Entrer une clé manuellement".
- Entrez un nom de compte (par exemple, "Mon Service").
- Entrez la clé secrète TOTP fournie (par exemple, "JBSWY3DPEHPK3PXP").
- Appuyez sur "Ajouter".

#### Exemple avec Authenticator Extension (Navigateur)

- Ouvrez l'extension Authenticator.
- Cliquez sur le "+".
- Sélectionnez "Entrer une clé manuellement".
- Entrez un nom de compte (par exemple, "Mon Service").
- Entrez la clé secrète TOTP fournie (par exemple, "JBSWY3DPEHPK3PXP").
- Cliquez sur "Ajouter".

### Conclusion

Une fois que le compte est ajouté à votre application mobile ou extension de navigateur, le code temporaire apparaîtra et changera toutes les 30 secondes. Utilisez ce code pour vous authentifier avec le service configuré.