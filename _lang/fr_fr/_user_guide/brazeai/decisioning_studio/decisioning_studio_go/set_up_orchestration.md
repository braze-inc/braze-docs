---
nav_title: "Configurer l'orchestration"
article_title: "Configurer l'orchestration"
page_order: 2
description: "Découvrez comment connecter BrazeAI Decisioning Studio à votre plateforme d'engagement client afin de permettre des communications personnalisées."
toc_headers: h2
---

# Configurer l'orchestration

> BrazeAI Decisioning Studio™ Go doit se connecter à votre plateforme d'engagement client (CEP) afin d'effectuer l'orchestration de communications personnalisées. Cet article explique comment configurer l'intégration pour chaque CEP pris en charge.

## CEP pris en charge

Decisioning Studio Go prend en charge les plateformes d'engagement client suivantes :

| CEP | Type d’intégration | Fonctionnalités clés |
|-----|-----------------|--------------|
| **Braze** | Campagnes déclenchées par API | Intégration native, déclencheur en temps réel |
| **Salesforce Marketing Cloud** | Journey Builder avec événements API | Automatisation des requêtes SQL, extensions de données |
| **Klaviyo** | Flux avec déclencheurs d'indicateurs | Basé sur des modèles, déclencheurs de division |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Veuillez sélectionner votre CEP ci-dessous pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Configuration de l'intégration Braze

Pour réaliser l'intégration de Decisioning Studio Go avec Braze, vous devrez créer une clé API, configurer une campagne déclenchée par API et fournir les identifiants nécessaires au portail Decisioning Studio Go.

### Étape 1 : Créer une clé API REST

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Paramètres** > **API et identifiants** > **Clés API**.
2. Sélectionnez **Créer une clé API**.
3. Veuillez saisir un nom pour votre clé API. Un exemple est « DecisioningStudioGoEmail ».
4. Veuillez sélectionner les autorisations en fonction des catégories suivantes :
    - **Données utilisateur :** veuillez sélectionner `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages :** veuillez sélectionner `messages.send`
    - **Campagnes :** veuillez sélectionner toutes les autorisations répertoriées.
    - **Canvas :** veuillez sélectionner toutes les autorisations répertoriées.
    - **Segments :** veuillez sélectionner toutes les autorisations répertoriées.
    - **Modèles :** veuillez sélectionner toutes les autorisations répertoriées.

{: start="5"}
5\. Sélectionnez **Créer une clé API**.
6\. Veuillez copier la clé API et la coller dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 2 : Veuillez identifier le nom d'affichage de votre adresse e-mail.

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Paramètres** > **Préférences e-mail**.
2. Veuillez identifier l'emplacement du nom d'affichage à utiliser avec BrazeAI Decisioning Studio™ Go.
3. Veuillez copier et coller le **nom d'affichage de l'expéditeur** dans le portail BrazeAI Decisioning Studio™ Go en tant que **nom d'affichage de** **l'e-mail**.
4. Veuillez copier et coller l'adresse e-mail associée dans votre portail BrazeAI Decisioning Studio™ Go en tant qu'**adresse e-mail d'expéditeur**, en combinant la partie locale et le domaine.

### Étape 3 : Veuillez trouver votre URL Braze et votre ID d'application.

**Pour trouver votre URL Braze :**
1. Veuillez vous rendre sur le tableau de bord de Braze.
2. Dans la fenêtre de votre navigateur, l'URL Braze commence par`https://`et se termine par `braze.com`. Un exemple d'URL Braze est `https://dashboard-01.braze.com`.

**Pour trouver votre ID d'application (clé API) :**

{% alert note %}
Braze fournit des identifiants d'application (appelés clés API dans le tableau de bord de Braze) que vous pouvez utiliser à des fins de suivi, par exemple pour associer une activité à une application spécifique dans votre espace de travail. Si vous utilisez des ID d'application, BrazeAI Decisioning Studio™ Go prend en charge l'association d'un ID d'application à chaque expérimentateur.<br><br>Si vous n'utilisez pas d'identifiants d'application, vous pouvez saisir n'importe quelle chaîne de caractères comme marque substitutive.
{% endalert %}

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Paramètres** > **Paramètres de l'application**.
2. Veuillez vous rendre dans l'application que vous souhaitez suivre.
3. Veuillez copier et coller la **clé API** dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 4 : Créer une campagne déclenchée par API

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Envoi de messages** > **Campagnes**.
2. Veuillez sélectionner **Créer une campagne**.
3. Pour le type de campagne, veuillez sélectionner **« Campagne API** ».
4. Veuillez saisir un nom pour votre campagne. Un exemple est « Decisioning Studio Go e-mail ».

![Une campagne API intitulée « Decisioning Studio Go e-mail ».]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Pour votre canal de communication, veuillez sélectionner **e-mail**.

![Option permettant de sélectionner votre canal de communication pour la campagne API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Dans **Options supplémentaires**, veuillez cocher la case **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne**.
7\. Pour redevenir éligible, veuillez saisir **1** et sélectionner **« Heures** » dans le menu déroulant.

![Rééligibilité pour la campagne API sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Veuillez sélectionner **« Enregistrer la campagne** ».

### Étape 5 : Veuillez copier les ID de votre campagne et de votre message.

1. Dans votre campagne API, veuillez copier l'**ID** **de la campagne**. Ensuite, veuillez vous rendre sur le portail BrazeAI Decisioning Studio™ Go et insérer l'**ID** **de la campagne**.

![Exemple d'ID de variante de message à copier-coller.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Veuillez copier **l'ID de la variante du message**. Ensuite, veuillez vous rendre sur le portail BrazeAI Decisioning Studio™ Go et insérer l'**ID de variation de message.**

### Étape 6 : Veuillez identifier un ID d'utilisateur test.

Pour tester votre intégration, vous aurez besoin d'un ID utilisateur :

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Audience** > **Rechercher des utilisateurs**.
2. Recherchez l'utilisateur à l'aide de son ID externe, de son alias d'utilisateur, de son e-mail, de son numéro de téléphone ou de son jeton push.
3. Veuillez copier l'ID utilisateur pour référence dans votre configuration.

![Exemple de profil utilisateur à partir de l'emplacement d'un utilisateur grâce à son ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuration de l'intégration SFMC

Pour intégrer Decisioning Studio Go à Salesforce Marketing Cloud, vous devrez configurer un package d'application, créer une automatisation de requête de données et créer un parcours pour gérer les envois déclenchés.

### Partie 1 : Configurer un package d'application SFMC

1. Veuillez vous rendre sur la page d'accueil de Marketing Cloud.
2. Veuillez ouvrir le menu dans l'en-tête global et sélectionner **Configuration**.
3. Veuillez vous rendre dans **Applications** sous **Outils de la plateforme** dans le panneau de navigation latéral, puis sélectionnez **Paquets installés**.
4. Veuillez sélectionner **Nouveau** pour créer un package d'application.
5. Veuillez attribuer un nom et une description au package de l'application.

![Un package d'application nommé « Experimenter 1 - Test 5 ».]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Veuillez sélectionner **Ajouter un composant**.
7\. Pour le **type de composant**, veuillez sélectionner **l'intégration API**. Ensuite, veuillez sélectionner **Suivant**.
8\. Pour le **type d'intégration**, veuillez sélectionner **Serveur à serveur**. Ensuite, veuillez sélectionner **Suivant**.
9\. Veuillez sélectionner les champs d'application recommandés suivants pour votre package d'application uniquement :
    \- Canaux > E-mail > Lire, rédiger, envoyer
    \- Chaînes > OTT > Lire
    \- Canaux > Push > Lire
    \- Canaux > SMS > Lire
    \- Chaînes > Réseaux sociaux > Lire
    \- Chaînes > Web > Lire
    \- Ressources > Documents et images > Lecture, écriture
    \- Ressources > Contenu enregistré > Lecture, écriture
    \- Automatisation > Automatisations > Lire, écrire, exécuter
    \- Automatisation > Parcours > Lire, Écrire, Exécuter, Activer/Arrêter/Mettre en pause/Envoyer/Planification
    \- Contacts > Audiences > Lire
    \- Contacts > Liste et utilisateurs abonnés > Lecture, écriture
    \- Plateforme Cross Cloud > Audience cible > Afficher
    \- Plateforme Cross Cloud > Membre de l’audience du marché > Afficher
    \- Plateforme Cross Cloud > Marketing Cloud Connect > Lire
    \- Données > Extensions de données > Lecture, écriture
    \- Données > Emplacements des fichiers > Lire
    \- Données > Suivi des événements > Lecture, écriture
    \- Notifications d'événements > Rappels > Lire
    \- Notifications d'événements > Abonnements > Lire

{% details Show image of recommended scopes %}

![Portées recommandées pour le package d'applications Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Sélectionnez **Enregistrer**.
11\. Veuillez copier et coller les champs suivants dans le portail BrazeAI Decisioning Studio™ Go : **ID client**, **clé secrète client**, **URI de base d'authentification**, **URI de base REST**, **URI de base SOAP**.

### Partie 2 : Configurer l'automatisation des requêtes de données

#### Étape 1 : Créer une nouvelle automatisation

1. Depuis votre page d'accueil Salesforce Marketing Cloud, accédez au **générateur de parcours** et sélectionnez **Automation Studio**.

![Option Automation Studio dans la navigation du générateur Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Veuillez sélectionner **Nouvelle automatisation**.
3\. Veuillez glisser-déposer un nœud **de planification** en tant que **source** **de départ**.

![« Planification » comme point de départ d'un parcours.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. Dans le nœud **de planification**, veuillez sélectionner **Configurer**.
5\. Veuillez définir les paramètres suivants pour la planification :
    - **Date de début :** Jour du calendrier de demain
    - **Heure :** **MINUIT**
    - **Fuseau horaire :** **(GMT-05:00) Est (États-Unis et& Canada)**
6\. Pour **Répéter**, veuillez sélectionner **Quotidien**.
7\. Veuillez configurer cette planification pour qu'elle ne se termine jamais.
8\. Veuillez sélectionner **Terminé** pour enregistrer la planification.

![Exemple de planification défini pour le 25 janvier 2024 à minuit (heure de l'Est), à répéter quotidiennement.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Étape 2 : Veuillez créer vos requêtes SQL.

Ensuite, veuillez créer deux requêtes SQL : une requête sur les utilisateurs abonnés et une requête sur l'engagement. Ces requêtes permettent à BrazeAI Decisioning Studio™ Go de récupérer des données afin de constituer l'audience et d'intégrer les événements d'engagement.

**Demande des utilisateurs abonnés :**

1. Veuillez glisser-déposer une **requête SQL** dans le canvas.
2. Veuillez sélectionner **« Choisir** ».
3. Veuillez sélectionner **Créer une nouvelle activité de requête**.
4. Veuillez attribuer un nom et une clé externe à la requête. Nous vous recommandons d'utiliser le nom et la clé externe suggérés pour la requête de l'utilisateur abonné fournie dans votre portail BrazeAI Decisioning Studio™ Go.

![Un exemple"OFE_Subscribers_query_Test5"et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Sélectionnez **Suivant.**
6\. Dans votre portail BrazeAI Decisioning Studio™ Go, veuillez localiser la requête SQL des données système sous **Ressources de requête des utilisateurs abonnés**.
7\. Veuillez copier et coller la requête dans la zone de texte, puis sélectionner **Suivant**.

![Exemple de requête dans la section Requête SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. Dans votre portail BrazeAI Decisioning Studio™ Go, dans la section **Ressources à utiliser**, veuillez localiser la clé externe de l'extension de données cible. Veuillez ensuite le coller dans la barre de recherche pour effectuer la recherche.

![Une clé externe insérée dans la barre de recherche]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Veuillez sélectionner l'extension de données correspondant à la clé externe que vous avez recherchée. Le nom de l'extension de données cible est également fourni dans votre portail BrazeAI Decisioning Studio™ Go à des fins de référence croisée. L'**extension** **de données** pour la requête de l'utilisateur abonné doit se terminer par un`BASE_AUDIENCE_DATA`suffixe.

![Nom de l'extension de données correspondant à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Veuillez sélectionner **« Remplacer** », puis **« Suivant** ».

**Requête d'engagement :**

1. Veuillez glisser-déposer une **requête SQL** dans le canvas.

![« Requêtes SQL » ont été ajoutées en tant qu'activités dans le parcours.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Veuillez sélectionner **« Choisir** ».
3\. Veuillez sélectionner **Créer une nouvelle activité de requête**.
4\. Veuillez attribuer un nom et une clé externe à la requête. Nous vous recommandons d'utiliser le nom et la clé externe suggérés pour la requête d'engagement fournie dans votre portail BrazeAI Decisioning Studio™ Go.

![Un exemple"OFE_Engagement_query"et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Sélectionnez **Suivant.**
6\. Dans votre portail BrazeAI Decisioning Studio™ Go, veuillez déterminer l'emplacement de la requête SQL des données système sous **Ressources de requête d'engagement**.
7\. Veuillez copier et coller la requête dans la zone de texte, puis sélectionner **Suivant**.

![Exemple de requête dans la section Requête SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Veuillez localiser et sélectionner l'extension de données cible pour la requête d'engagement spécifiée dans votre portail BrazeAI Decisioning Studio™ Go.

{% alert tip %}
Le nom de l'extension de données cible est également fourni dans votre portail BrazeAI Decisioning Studio™ Go à des fins de référence croisée. Veuillez vous assurer que vous consultez bien l'extension de données cible pour la requête d'engagement. L'**extension** **de données** pour la requête d'engagement doit se terminer par leENGAGEMENT_DATAsuffixe .
{% endalert %}

{: start="9"}
9\. Veuillez sélectionner **« Remplacer** », puis **« Suivant** ».

![Nom de l'extension de données correspondant à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Étape 3 : Veuillez exécuter l'automatisation.

1. Veuillez attribuer un nom à l'automatisation et sélectionner **Enregistrer**.

![Exemple d'automatisation/assets/img/decisioning_studio_go/query3.pngimage_buster"OFE_Experimenter_Test5_Automation".]({%    %})

{: start="2"}
2\. Ensuite, veuillez sélectionner **« Exécuter une fois** » pour vérifier que tout fonctionne correctement.
3\. Veuillez sélectionner les deux requêtes et cliquer sur **Exécuter**.

![Une automatisation"OFE_Experimenter_Test5_Automation"comprenant une liste d'activités de requêtes SQL sélectionnées à exécuter.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Veuillez sélectionner **« Exécuter maintenant** ».

![Une activité de requête SQL sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Vous pouvez maintenant vérifier que l'automatisation fonctionne correctement. Veuillez contacter le service d'assistance Braze pour obtenir de l'aide si votre automatisation ne fonctionne pas comme prévu.

### Partie 3 : Créez votre parcours SFMC

#### Étape 1 : Configurer le parcours

1. Dans Salesforce Marketing Cloud, veuillez vous rendre dans **Journey Builder** > **Journey Builder**.
2. Veuillez sélectionner **Créer un nouveau parcours**.
3. Pour votre type de parcours, veuillez sélectionner **« Parcours en plusieurs étapes** », puis **« Créer** ».

![Une source d'entrée d'événement API connectée à un arbre décisionnel et à plusieurs nœuds de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Étape 2 : Créez votre parcours

**Veuillez créer une source d'entrée :**

1. Pour votre source d'entrée, veuillez faire glisser **API Event** vers le générateur de parcours.

![« Événement API » sélectionné comme source d'entrée.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. Dans l'**API Événement**, veuillez sélectionner **Créer un événement**.

![L'option « créer un événement » dans l'API Event.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Veuillez sélectionner **l'extension de données**. Veuillez déterminer l'emplacement de l'extension de données dans laquelle BrazeAI Decisioning Studio™ Go enregistrera ses recommandations.
4\. Veuillez sélectionner **Résumé** pour enregistrer vos modifications.
5\. Veuillez sélectionner **Terminé** pour enregistrer l'événement API.

![Résumé de l'événement API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Ajouter un arbre décisionnel :**

1. Veuillez glisser-déposer un **arbre décisionnel** après l'**événement d'entrée API**.
2. Dans les détails **de l’arbre décisionnel**, veuillez sélectionner **Modifier** pour le premier chemin.

![Détails de l’arbre décisionnel avec le bouton « Modifier ».]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Veuillez mettre à jour l'**arbre** **décisionnel** afin d'utiliser l'ID de modèle transmis par l'extension de données de recommandations. Veuillez identifier le champ approprié sous **Données du trajet**.

![La section Données du parcours dans le chemin 1 de l'arbre décisionnel.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Veuillez sélectionner votre événement d'entrée et trouver l'emplacement du champ d'ID du modèle souhaité, puis faites-le glisser dans l'espace de travail.

![L'ID du modèle d'e-mail à inclure.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Veuillez saisir l'ID de votre premier modèle d'e-mail, puis sélectionnez **Terminé**.
6\. Veuillez sélectionner **Résumé** pour enregistrer ce chemin d'accès.
7\. Veuillez ajouter un chemin d'accès pour chacun de vos modèles d'e-mail, puis répétez les étapes 4 à 6 ci-dessus pour définir les critères de filtrage de manière à ce que l'ID du modèle corresponde à la valeur ID de chaque modèle.
8\. Veuillez sélectionner **Terminé** pour enregistrer le nœud **de l'arbre décisionnel**.

![Deux chemins dans un arbre décisionnel pour chaque ID de modèle d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Veuillez ajouter un e-mail pour chaque arbre décisionnel :**

1. Veuillez faire glisser un nœud **e-mail** dans chaque chemin de l'**arbre** **décisionnel**.
2. Veuillez sélectionner **e-mail**, puis choisissez le modèle approprié qui doit être associé à chaque chemin (ce qui signifie que la valeur d'ID du modèle doit correspondre à la logique de votre arbre décisionnel).

![Un nœud e-mail a été ajouté au parcours.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Étape 3 : Veuillez activer le parcours.

Après avoir configuré votre parcours, veuillez l'activer et partager les informations suivantes avec l'équipe BrazeAI Decisioning Studio™ Go :

* Identifiant de voyage
* Nom du voyage
* Clé de définition d'événement API
* Clé externe d'extension des données de recommandations

{% alert note %}
Le portail BrazeAI Decisioning Studio™ Go vous présente l'automatisation SFMC qu'il a mise en place pour exporter les données relatives aux utilisateurs abonnés et à l'engagement une fois par jour. Si vous ouvrez cette automatisation dans SFMC, veuillez vous assurer de la réactiver et de la remettre en ligne/en production/instantanée.
{% endalert %}

1. Dans le portail BrazeAI Decisioning Studio™ Go, veuillez copier le **nom du parcours**.
2. Ensuite, dans Salesforce Marketing Cloud Générateur de parcours, veuillez coller le nom du parcours dans la barre de recherche.
3. Veuillez sélectionner le nom du voyage. Veuillez noter que le parcours est actuellement à l'état de projet.
4. Veuillez sélectionner **Valider**.

![Le parcours terminé est prêt à être activé.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Veuillez ensuite examiner les résultats de la validation et sélectionner **Activer**.

![Veuillez vous référer aux recommandations énumérées dans la section Règles de validation.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. Dans le résumé **Activer le parcours**, veuillez sélectionner à nouveau **Activer**.

![Résumé du parcours.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Vous êtes prêt ! Vous pouvez désormais commencer à utiliser les déclencheurs pour des envois via BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% tab Klaviyo %}

## Configuration de l'intégration Klaviyo

Pour l'intégration de Decisioning Studio Go avec Klaviyo, vous devrez configurer une clé API, créer un modèle de flux marque substitutive et créer un flux pour gérer les envois déclenchés.

### Partie 1 : Configurer les clés API Klaviyo

1. Dans Klaviyo, veuillez vous rendre dans **Paramètres** > **Clés API**.
2. Veuillez sélectionner **Créer une clé API privée**.
3. Saisissez un nom pour la clé API. Un exemple est « Decisioning Studio Experimenters ».
4. Veuillez sélectionner les autorisations suivantes pour la clé API :
    - Campagnes : Accès en lecture
    - Confidentialité des données : Accès complet
    - Événements : Accès complet
    - Flux : Accès complet
    - Images : Accès en lecture
    - Liste : Accès complet
    - Indicateurs : Accès complet
    - Profils : Accès complet
    - Segments : Accès en lecture
    - Modèles : Accès complet
    - Webhooks : Accès en lecture

![Une clé API Klaviyo avec les autorisations sélectionnées.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Sélectionnez **Créer**.
6\. Veuillez copier cette clé API et la coller dans le portail BrazeAI Decisioning Studio™ Go lorsque vous y êtes invité.

### Partie 2 : Veuillez créer un modèle de marque substitutive dans Klaviyo.

BrazeAI Decisioning Studio™ Go importe les modèles associés aux flux existants dans votre compte Klaviyo. Pour utiliser un modèle qui n'est associé à aucun flux, vous pouvez créer un flux marque substitutive contenant les modèles que vous souhaitez utiliser. Le flux peut être laissé à l'état de brouillon ; il n'est pas nécessaire qu'il soit en ligne/en production/instantané.

{% alert note %}
Le but de ce flux marque substitutive est d'importer le contenu souhaité dans BrazeAI Decisioning Studio™ Go. Il est nécessaire de créer un flux distinct à une étape ultérieure, que BrazeAI Decisioning Studio™ Go utilisera en tant que déclencheur pour déclencher les activations une fois que votre expérimentateur sera en ligne/en production/instantané.
{% endalert %}

**Étape 1 : Configurez votre flux**

1. Dans Klaviyo, veuillez sélectionner **Flux**.
2. Veuillez sélectionner **Créer un flux** > **Créer à partir de zéro**.
3. Veuillez attribuer un nom reconnaissable à la marque substitutive Flow, puis sélectionnez **Créer un flux**.

![Un flux nommé « OFE Marque substitutive ».]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Veuillez sélectionner un déclencheur, puis enregistrer le flux.
5\. Veuillez sélectionner **« Confirmer et enregistrer** ».

**Étape 2 : Créer le modèle de marque substitutive**

1. Veuillez glisser-déposer un nœud **e-mail** après le **déclencheur**.

![Un flux avec un nœud Déclencheur suivi d'un nœud e-mail.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. Dans le nœud **e-mail**, veuillez sélectionner **Sélectionner un modèle**.
3\. Ensuite, veuillez sélectionner le modèle à utiliser et choisir **« Utiliser le modèle** ».
4\. Veuillez sélectionner **Enregistrer** > **Terminé**.
5\. (Facultatif) Pour ajouter d'autres modèles à utiliser dans BrazeAI Decisioning Studio™ Go, veuillez ajouter un autre nœud **e-mail** et répéter les étapes 2 à 4.
6\. Veuillez laisser tous les e-mails en mode **Brouillon** et quitter le flux.

Dans le portail BrazeAI Decisioning Studio™ Go, vos modèles devraient être sélectionnables sous votre flux de marque substitutive.

![Exemple de modèle Klaviyo marque substitutive dans le portail Decisioning Studio Go.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### Partie 3 : Créer un flux dans Klaviyo

{% alert important %}
Il est nécessaire de créer un nouveau flux dans Klaviyo pour chaque nouvel expérimentateur que vous configurez. Si vous avez précédemment créé un flux marque substitutive pour importer vos modèles, il est nécessaire de créer un nouveau flux et vous ne pouvez pas réutiliser le flux marque substitutive précédent.
{% endalert %}

Avant de créer un flux dans Klaviyo, il est nécessaire de disposer des informations suivantes provenant de votre portail BrazeAI Decisioning Studio™ Go à titre de référence :

- Nom du flux
- Nom de l'événement déclencheur

#### Étape 1 : Configurer le flux

1. Dans Klaviyo, veuillez sélectionner **Flux** > **Créer un flux**.
2. Veuillez sélectionner **« Créez votre propre** produit ».
3. Dans le champ **Nom**, veuillez saisir le nom du flux provenant de votre portail BrazeAI Decisioning Studio™ Go. Veuillez ensuite sélectionner **Créer manuellement**.

![L'option « Créer manuellement » est sélectionnée pour un exemple de flux.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Veuillez sélectionner le déclencheur.
5\. Veuillez associer le nom de l'indicateur au nom du déclencheur dans votre portail BrazeAI Decisioning Studio™ Go.

![Exemple de nom d'indicateur correspondant au nom de l'événement "OFE_TEST_CASE_API_EVENT_TRIGGER".]({%image_buster/assets/img/decisioning_studio_go/flow2.pngdéclencheur    %})

{: start="6"}
6\. Sélectionnez **Enregistrer**.

{% alert note %}
Si votre expérimentateur dispose d'un modèle de base, veuillez passer à l'étape 2. Si votre expérimentateur dispose de deux modèles de base ou plus, veuillez passer à [l'étape 3 : Veuillez ajouter une division de déclencheur à votre flux](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

#### Étape 2 : Veuillez ajouter un e-mail à votre flux (modèle unique)

1. Veuillez glisser-déposer un nœud **e-mail** après le nœud **déclencheur**.
2. Dans les **détails de l'e-mail**, veuillez sélectionner **« Sélectionner un modèle** ».

![Option « Sélectionner un modèle » dans la section « Détails de l'e-mail ».]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Veuillez rechercher et sélectionner votre modèle de base. Vous pouvez rechercher votre modèle par son nom dans la section **« Ressources à utiliser** » du portail BrazeAI Decisioning Studio™ Go.

![Un exemple de modèle de base dans Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Veuillez sélectionner **« Utiliser le modèle** » puis **« Enregistrer** ».
5\. Dans la **ligne d'objet**, veuillez saisir {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Pour **le nom de l'expéditeur** et **l'adresse e-mail de l'expéditeur**, veuillez saisir les informations que vous souhaitez utiliser.

![Exemple de ligne d'objet, de nom d'expéditeur et d'adresse e-mail d'expéditeur pour « E-mail 1 ».]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Veuillez sélectionner **Terminé**.
8\. Veuillez décocher la case **« Ignorer les profils récemment envoyés par e-mail** », puis sélectionnez **« Enregistrer** ».
9\. Dans le nœud e-mail, veuillez modifier le mode de **Brouillon** à **en ligne/en production/instantané**.

![L'éditeur de flux Klaviyo affichant un nœud déclencheur connecté à un nœud e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Vous êtes prêt ! Vous pouvez désormais utiliser les déclencheurs pour déclencher des activations via BrazeAI Decisioning Studio™ Go.

#### Étape 3 : Ajoutez une division de déclencheur à votre flux (modèles multiples)

1. Veuillez glisser-déposer un nœud **de division de déclencheur** après le **nœud de déclencheur**.
2. Veuillez sélectionner le nœud **de séparation déclencheur** et définir la **dimension** sur **EmailTemplateID**.

![Diagramme de flux Klaviyo illustrant un déclencheur alimentant une division de déclenchement configurée avec la dimension EmailTemplateID.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**Veuillez ajouter votre modèle d'e-mail :**

1. Dans le portail BrazeAI Decisioning Studio™ Go, veuillez rechercher l'**ID du modèle d'e-mail** pour votre premier modèle dans la section **« Ressources à utiliser** ». Veuillez saisir l'**ID du modèle d'e-mail** dans le champ **Dimension**, puis sélectionnez **Enregistrer**.
2. Veuillez glisser-déposer un nœud **e-mail** vers la branche **Oui** de la **bifurcation déclencheur**.

![Un flux Klaviyo avec un nœud de division de déclencheur, dont la branche « Oui » mène à un nœud « e-mail » et la branche « Non » se connecte à une autre division de déclencheur.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Dans les **détails de l'e-mail**, veuillez sélectionner **« Sélectionner un modèle** ».
4\. Veuillez rechercher et sélectionner votre modèle de base. Vous pouvez rechercher votre modèle à partir du nom du modèle de base dans la section **Ressources à utiliser** du portail BrazeAI Decisioning Studio™ Go.
5\. Veuillez sélectionner **« Utiliser le modèle** » puis **« Enregistrer** ».
6\. Dans la **ligne d'objet**, veuillez saisir {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Pour **le nom de l'expéditeur** et **l'adresse e-mail de l'expéditeur**, veuillez saisir les informations que vous souhaitez utiliser.

![Un modèle d'e-mail sélectionné et des champs pour la ligne d'objet, le nom de l'expéditeur et l'adresse e-mail de l'expéditeur.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Veuillez sélectionner **Terminé**.
9\. Veuillez décocher la case **« Ignorer les profils récemment envoyés par e-mail** », puis sélectionnez **« Enregistrer** ».
10\. Dans le nœud e-mail, veuillez modifier le mode de **Brouillon** à **en ligne/en production/instantané**.

**Veuillez ajouter un nouveau déclencheur pour chaque modèle supplémentaire :**

1. Veuillez glisser-déposer un autre nœud **de division de déclencheur** dans la branche **« Non »** du nœud **de division de déclencheur** précédent.
2. Veuillez définir la **dimension** sur **EmailTemplateID** et saisir l'**ID** **du modèle d'e-mail** du modèle de base que vous configurez dans la valeur **de** **la dimension**.
3. Sélectionnez **Enregistrer**.

![Schéma d'un éditeur de flux Klaviyo illustrant un nœud de déclencheur menant à une division de déclencheur. La division du déclencheur comporte une branche « Oui » qui mène à un nœud « e-mail » et une branche « Non » qui se connecte à une autre division du déclencheur menant à des nœuds « e-mail » supplémentaires.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Veuillez glisser-déposer un nœud **e-mail** dans la branche **Oui** de votre nouvelle division de déclencheur.
5\. Veuillez répéter les étapes de configuration du modèle d'e-mail ci-dessus pour sélectionner le modèle correspondant.
6\. Veuillez définir la **ligne d'objet** sur {% raw %}`{{event.SubjectLine}}`{% endraw %}et décocher la case **Ignorer les profils récemment envoyés par e-mail**.
7\. Veuillez répéter ce processus jusqu'à ce que vous disposiez d'un nœud **de déclencheur** et d'un nœud **d'e-mail** pour chaque modèle de base utilisé par votre expérimentateur. Votre dernière division de déclencheur ne devrait rien contenir dans la branche « Non ».

![Un flux Klaviyo comportant plusieurs nœuds de division de déclencheur qui se ramifient vers plusieurs nœuds d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. Dans chacun de vos nœuds **e-mail**, veuillez mettre à jour le mode de **Brouillon** à **en ligne/en production/instantané**.

![L'option permettant de mettre à jour le statut du nœud en « En ligne/en production/instantané ».]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Vous êtes prêt ! Vous pouvez désormais utiliser les déclencheurs pour déclencher des activations via BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Étapes suivantes

Maintenant que vous avez configuré l'orchestration, veuillez procéder à la conception de votre agent :

- [créez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
