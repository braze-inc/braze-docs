---
nav_title: Décisions Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 0
description: "Découvrez comment configurer et intégrer BrazeAI Decisioning <sup>StudioTM</sup> Go dans Braze."
---

# BrazeAI Decisioning Studio™ Go

> Emplacement/localisation des informations clés dans Braze pour commencer l'intégration avec BrazeAI Decisioning Studio™ Go.

## L'essentiel

### Création d'une clé API REST dans Braze

Pour créer une nouvelle clé d’API REST :

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **API et identifiants** > **Clés API.**
2. Sélectionnez **Créer une clé API**.
3. Saisissez un nom pour votre clé API. Un exemple est "DecisioningStudioGoEmail".
4. Sélectionnez les autorisations en fonction des catégories suivantes :
    - **Données utilisateur :** sélectionnez `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages :** sélectionnez `messages.send`
    - **Campagnes :** sélectionnez toutes les autorisations répertoriées
    - **Canvas :** sélectionner toutes les autorisations énumérées
    - **Segments :** sélectionnez toutes les autorisations répertoriées
    - **Modèles :** sélectionnez toutes les autorisations énumérées

{: start="5"}
5\. Sélectionnez **Créer une clé API**.
6\. Ensuite, copiez la clé API et collez-la dans votre portail BrazeAI Decisioning Studio™ Go.

### Emplacement/localisation du nom d'affichage de votre e-mail Braze

Pour trouver le nom d'affichage de votre e-mail Braze :

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **Préférences d'e-mail.**
2. Localisez le nom d'affichage à utiliser avec BrazeAI Decisioning Studio™ Go.
3. Copiez et collez le **nom d'affichage de dans** le portail BrazeAI Decisioning Studio™ Go en tant que **nom d'affichage de l'e-mail**.
4. Copiez et collez l'adresse e-mail associée dans votre portail BrazeAI Decisioning Studio™ Go en tant qu'**adresse e-mail From**, qui combine la partie locale et le domaine.

### Emplacement/localisation de votre ID utilisateur

Pour trouver votre ID utilisateur :

1. Dans le tableau de bord de Braze, allez dans **Audience** > Recherche d'utilisateurs.
2. Recherchez l'utilisateur par son ID externe, son alias d'utilisateur, son e-mail, son numéro de téléphone ou son jeton push.
3. Copiez l'ID de l'utilisateur pour vous y référer dans votre configuration.

![Exemple de profil utilisateur à partir de l'emplacement/localisation d'un utilisateur avec son ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Trouver votre URL Braze

Pour identifier l'URL de votre Braze :

1. Accédez au tableau de bord de Braze.
2. Dans la fenêtre de votre navigateur, votre URL Braze commence par `https://` et se termine par `braze.com`. Un exemple d'URL de Braze est `https://dashboard-01.braze.com`.

### Trouver votre clé API Braze

{% alert note %}
Braze propose des ID d'apps (appelés clés API dans le tableau de bord de Braze) que vous pouvez utiliser à des fins de suivi, par exemple pour associer une activité à une app spécifique dans votre espace de travail. Si vous utilisez des ID d'apps, BrazeAI Decisioning Studio™ Go prend en charge l'association d'un ID d'app à chaque expérimentateur.<br><br>Si vous n'utilisez pas d'ID d'application, vous pouvez saisir n'importe quelle chaîne de caractères comme marque substitutive.
{% endalert %}

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **Paramètres de l'application**.
2. Accédez à l'application que vous souhaitez suivre.
3. Copiez et collez la **clé API** dans votre portail BrazeAI Decisioning Studio™ Go.

### Configurer les clés API de Klaviyo

Vous devez configurer une clé API pour utiliser Klaviyo pour BrazeAI Decisioning Studio™ Go.

1. Dans Klaviyo, allez dans **Paramètres** > **Clés API**.
2. Sélectionnez **Créer une clé API privée.** 
3. Saisissez un nom pour la clé API. Un exemple est "Decisioning Studio Experimenters".
4. Sélectionnez les autorisations suivantes pour la clé API :
    - Campagnes : Lire l'accès
    - Confidentialité des données : Accès complet
    - Événements : Accès complet
    - Flux : Accès complet
    - Images : Lire l'accès
    - Liste : Accès complet
    - Indicateurs : Accès complet
    - Profils : Accès complet
    - Segments : Lire l'accès
    - Modèles : Accès complet
    - Webhooks : Lire l'accès

![Une clé API Klaviyo avec les autorisations sélectionnées.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Sélectionnez **Créer**.
6\. Copiez cette clé API et collez-la dans le portail BrazeAI Decisioning Studio™ Go lorsque vous y êtes invité.

### Mise en place d'un paquet d'applications SFMC

Pour utiliser Salesforce Marketing Cloud pour BrazeAI Decisioning Studio™ Go, vous devez configurer un package d'apps dans Salesforce Marketing Cloud. 

1. Rendez-vous sur la page d'accueil de votre Marketing Cloud. 
2. Ouvrez le menu dans l'en-tête global et sélectionnez **Configuration**.
3. Allez dans **Apps** sous **Platform Tools** dans le panneau latéral de navigation, puis sélectionnez **Installed Packages**.
4. Sélectionnez **Nouveau** pour créer un paquet d'applications.
5. Donnez un nom et une description au paquet d'applications.

![Un paquet d'applications avec le nom "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Sélectionnez **Ajouter un composant**.
7\. Pour le **type de composant**, sélectionnez **Intégration API.** Sélectionnez ensuite **Suivant.**
8\. Pour le **type d'intégration**, sélectionnez **Serveur à serveur.** Sélectionnez ensuite **Suivant.**
9\. Ensuite, sélectionnez les champs d'application recommandés suivants pour votre paquet d'applications uniquement :
    \- Canaux > E-mail > Lire, écrire, envoyer
    \- Chaînes > OTT > Lire
    \- Canaux > Pousser > Lire
    \- Canaux > SMS > Lire
    \- Canaux > Social > Lire
    \- Canaux > Web > Lire
    \- Ressources > Documents et images > Lire, écrire
    \- Ressources > Contenu enregistré > Lire, écrire
    \- Automatisation > Automatisations > Lire, écrire, exécuter
    \- Automatisation > Trajets > Lire, écrire, exécuter, activer/arrêter/pause/envoyer/planifier
    \- Contacts > Audiences > Lire
    \- Contacts > Liste et abonnés > Lire, écrire
    \- Cross Cloud Platform > Audience du marché > Vue
    \- Cross Cloud Platform > Membre de l'audience du marché > Vue
    \- Cross Cloud Platform > Marketing Cloud Connect > Lire
    \- Données > Extensions de données > Lecture, écriture
    \- Données > Emplacements des fichiers > Lecture
    \- Données > Suivi des événements > Lecture, écriture
    \- Notifications d'événements > Rappels > Lecture
    \- Notifications d'événements > Abonnements > Lire

{% details Show image of recommended scopes %}

![Les champs d'application recommandés pour le package d'applications Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Sélectionnez **Enregistrer**.
11\. Copiez et collez les champs suivants dans le portail BrazeAI Decisioning Studio™ Go : **ID du client**, **secret du client**, **URI de base d'authentification**, **URI de base REST**, **URI de base SOAP**.