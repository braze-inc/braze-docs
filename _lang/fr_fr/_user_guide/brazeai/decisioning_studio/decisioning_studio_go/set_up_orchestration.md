---
nav_title: "Mettre en place l'orchestration"
article_title: "Mettre en place l'orchestration"
page_order: 2
description: "Découvrez comment connecter BrazeAI Decisioning Studio Go à votre plateforme d'engagement client pour permettre des communications personnalisées."
toc_headers: h2
---

# Mettre en place l'orchestration

> BrazeAI Decisioning Studio™ Go doit se connecter à votre plateforme d'engagement client (CEP) pour orchestrer des communications personnalisées. Cet article explique comment configurer l'intégration pour chaque CEP pris en charge.

## PEC soutenus

Decisioning Studio Go prend en charge les plateformes d'engagement client suivantes :

| CEP | Type d’intégration | Fonctionnalités clés |
|-----|-----------------|--------------|
| **Braze** | Campagnes déclenchées par API | Intégration native, déclenchement en temps réel |
| **Salesforce Marketing Cloud** | Générateur de parcours avec événements API | Automatisation des requêtes SQL, extensions de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Sélectionnez votre CEP ci-dessous pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Mise en place de l'intégration de Braze

Pour intégrer Decisioning Studio Go à Braze, vous devez créer une clé API, configurer une campagne déclenchée par l'API et fournir les identifiants nécessaires au portail Decisioning Studio Go.

### Étape 1 : Créer une clé API REST

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **API et identifiants** > **Clés API.**
2. Sélectionnez **Créer une clé API**.
3. Saisissez un nom pour votre clé API. Un exemple est "DecisioningStudioGoEmail".
4. Sélectionnez les autorisations en fonction des catégories suivantes :
    - **Données utilisateur :** sélectionnez `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages :** sélectionnez `messages.send`
    - **Campagnes :** sélectionnez toutes les autorisations énumérées
    - **Canvas :** sélectionner toutes les autorisations énumérées
    - **Segments :** sélectionnez toutes les autorisations répertoriées
    - **Modèles :** sélectionnez toutes les autorisations énumérées

{: start="5"}
5\. Sélectionnez **Créer une clé API**.
6\. Copiez la clé API et collez-la dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 2 : Emplacement/localisation du nom d'affichage de votre e-mail

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **Préférences d'e-mail.**
2. Localisez le nom d'affichage à utiliser avec BrazeAI Decisioning Studio™ Go.
3. Copiez et collez le **nom d'affichage de dans** le portail BrazeAI Decisioning Studio™ Go en tant que **nom d'affichage de l'e-mail**.
4. Copiez et collez l'adresse e-mail associée dans votre portail BrazeAI Decisioning Studio™ Go en tant qu'**adresse e-mail From**, qui combine la partie locale et le domaine.

### Étape 3 : Trouvez l'URL et l'ID de votre application Braze

**Pour trouver l'URL de votre Braze :**
1. Accédez au tableau de bord de Braze.
2. Dans la fenêtre de votre navigateur, votre URL Braze commence par `https://` et se termine par `braze.com`. Un exemple d'URL de Braze est `https://dashboard-01.braze.com`.

**Pour trouver votre ID d'application (clé API) :**

{% alert note %}
Braze propose des ID d'apps (appelés clés API dans le tableau de bord de Braze) que vous pouvez utiliser à des fins de suivi, par exemple pour associer une activité à une app spécifique dans votre espace de travail. Si vous utilisez des ID d'apps, BrazeAI Decisioning Studio™ Go prend en charge l'association d'un ID d'app à chaque expérimentateur.<br><br>Si vous n'utilisez pas d'ID d'application, vous pouvez saisir n'importe quelle chaîne de caractères comme marque substitutive.
{% endalert %}

1. Dans le tableau de bord de Braze, allez dans **Paramètres** > **Paramètres de l'application**.
2. Accédez à l'application que vous souhaitez suivre.
3. Copiez et collez la **clé API** dans votre portail BrazeAI Decisioning Studio™ Go.

### Étape 4 : Créez une campagne déclenchée par l'API

1. Dans le tableau de bord de Braze, allez dans **Envoi de messages** > Campagnes.
2. Sélectionnez **Créer une campagne**.
3. Pour votre type de campagne, sélectionnez **Campagne API**.
4. Saisissez un nom pour votre campagne. Un exemple est "Decisioning Studio Go Email".

![Une campagne API intitulée "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Pour votre canal de communication, sélectionnez **E-mail.**

![Option permettant de sélectionner votre canal de communication pour la campagne API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Dans **Options supplémentaires**, cochez la case **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne.** 
7\. Pour le délai de réadmissibilité, entrez **1** et sélectionnez **Heures** dans la liste déroulante.

![Rééligibilité pour la campagne API sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Sélectionnez **Enregistrer la campagne**.

### Étape 5 : Copiez les ID de vos campagnes et de vos messages.

1. Dans votre campagne API, copiez l'**ID de** la campagne. Ensuite, rendez-vous sur le portail BrazeAI Decisioning Studio™ Go et collez l'**ID de la campagne**.

![Un exemple d'envoi de messages ID à copier-coller.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Copiez l'**ID de la variation du message**. Ensuite, accédez au portail BrazeAI Decisioning Studio™ Go et collez l'**ID de la variation du message**.

### Étape 6 : Emplacement/localisation d'un utilisateur test ID

Pour tester votre intégration, vous aurez besoin d'un ID utilisateur :

1. Dans le tableau de bord de Braze, allez dans **Audience** > Recherche d'utilisateurs.
2. Recherchez l'utilisateur par son ID externe, son alias d'utilisateur, son e-mail, son numéro de téléphone ou son jeton push.
3. Copiez l'ID de l'utilisateur pour vous y référer dans votre configuration.

![Exemple de profil utilisateur à partir de l'emplacement/localisation d'un utilisateur avec son ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Mise en place de l'intégration du SFMC

Pour intégrer Decisioning Studio Go à Salesforce Marketing Cloud, vous allez configurer un package d'apps, créer une automatisation des requêtes de données et créer un Journey pour gérer les envois déclenchés.

### Partie 1 : Créer un paquet d'applications SFMC

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
9\. Sélectionnez les champs d'application recommandés suivants pour votre paquet d'applications uniquement :
    \- Canaux > E-mail > Lire, écrire, envoyer
    \- Chaînes > OTT > Lire
    \- Canaux > Pousser > Lire
    \- Canaux > SMS > Lire
    \- Canaux > Social > Lire
    \- Canaux > Web > Lire
    \- Ressources > Documents et images > Lire, écrire
    \- Ressources > Contenu enregistré > Lire, écrire
    \- Automatisation > Automatisations > Lecture, écriture, exécution
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

### Partie 2 : Mise en place d'une automatisation des requêtes de données

#### Étape 1 : Créer une nouvelle automatisation

1. Depuis la page d'accueil de Salesforce Marketing Cloud, accédez à **Journey Builder** et sélectionnez **Automation Studio**.

![Option Automation Studio dans la navigation de Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Sélectionnez **Nouvelle automatisation**.
3\. Glissez-déposez un nœud de **planification** comme **source de départ**.

!["Planification" comme source de départ d'un voyage.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. Dans le nœud **Planification**, sélectionnez **Configurer**.
5\. Définissez les éléments suivants pour la planification :
    - **Date de début :** Le jour du calendrier de demain
    - **Le temps :** **12:00 AM**
    - **Fuseau horaire :** **(GMT-05:00) Est (US & Canada)**
6\. Pour **Répéter**, sélectionnez **Quotidien**.
7\. Fixez cette planification pour qu'elle ne s'arrête jamais.
8\. Sélectionnez **Terminé** pour enregistrer la planification.

![Un exemple de planification définie pour le 25 janvier 2024 à 12 h ET, à répéter tous les jours.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Étape 2 : Créez vos requêtes SQL

Ensuite, créez 2 requêtes SQL : une requête sur les abonnés et une requête sur l'engagement. Ces requêtes permettent à BrazeAI Decisioning Studio™ Go de récupérer des données pour alimenter l'audience et ingérer des événements d'engagement.

**Requête des utilisateurs :**

1. Glissez-déposez une **requête SQL** dans le canvas.
2. Sélectionnez **Choisir**.
3. Sélectionnez **Créer une nouvelle activité de requête**.
4. Donnez un nom et une clé externe à la requête. Nous vous recommandons d'utiliser le nom et la clé externe suggérés pour la requête de l'utilisateur, fournis dans votre portail BrazeAI Decisioning Studio™ Go.

![Un exemple "OFE_Subscribers_query_Test5" et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Sélectionnez **Suivant.**
6\. Dans votre portail BrazeAI Decisioning Studio™ Go, localisez la requête SQL sur les données du système sous **Ressources de requêtes abonnés**.
7\. Copiez et collez la requête dans la zone de texte et sélectionnez **Suivant.**

![Un exemple de requête dans la section Requête SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. Dans votre portail BrazeAI Decisioning Studio™ Go, dans la section **Ressources à utiliser**, localisez la clé externe de l'extension de données cible. Ensuite, collez-la dans la barre de recherche pour effectuer une recherche.

![Une clé externe collée dans la barre de recherche]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Sélectionnez l'extension de données qui correspond à la clé externe recherchée. Le nom de l'extension des données cibles est également fourni dans votre portail BrazeAI Decisioning Studio™ Go pour faire des références croisées. L'**extension de données** pour la requête de l'utilisateur doit se terminer par un suffixe `BASE_AUDIENCE_DATA`.

![Le nom de l'extension de données qui correspond à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Sélectionnez **Écraser**, puis **Suivant.**

**Demande d'engagement :**

1. Glissez-déposez une **requête SQL** dans le canvas.

!["Requêtes SQL" ajoutées en tant qu'activité dans le parcours.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Sélectionnez **Choisir**.
3\. Sélectionnez **Créer une nouvelle activité de requête**.
4\. Donnez un nom et une clé externe à la requête. Nous vous recommandons d'utiliser le nom et la clé externe suggérés pour la requête d'engagement fournis dans votre portail BrazeAI Decisioning Studio™ Go.

![Un exemple "OFE_Engagement_query" et la clé externe.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Sélectionnez **Suivant.**
6\. Dans votre portail BrazeAI Decisioning Studio™ Go, localisez la requête SQL sur les données du système sous **Ressources de requêtes d'engagement.**
7\. Copiez et collez la requête dans la zone de texte et sélectionnez **Suivant.**

![Un exemple de requête dans la section Requête SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Localisez et sélectionnez l'extension de données cible pour la requête d'engagement spécifiée dans votre portail BrazeAI Decisioning Studio™ Go.

{% alert tip %}
Le nom de l'extension des données cibles est également fourni dans votre portail BrazeAI Decisioning Studio™ Go pour faire des références croisées. Assurez-vous que vous regardez l'extension de données cible pour la requête d'engagement. L'**extension de données** pour la demande d'engagement doit se terminer par un suffixe ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Sélectionnez **Écraser**, puis **Suivant.**

![Le nom de l'extension de données qui correspond à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Étape 3 : Lancer l'automatisation

1. Donnez un nom à l'automatisation et sélectionnez **Enregistrer.**

![Un exemple d'automatisation "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Ensuite, sélectionnez **Exécuter une fois** pour confirmer que tout fonctionne comme prévu.
3\. Sélectionnez les deux requêtes et choisissez **Exécuter**.

![Une automatisation "OFE_Experimenter_Test5_Automation" avec une liste de requêtes SQL sélectionnées à exécuter.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Sélectionnez **Exécuter maintenant.**

![Une activité de requêtes SQL sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Vous pouvez maintenant vérifier que l'automatisation se déroule correctement. Contactez l'assistance de Braze pour obtenir de l'aide si votre automatisation ne fonctionne pas comme prévu.

### Partie 3 : Créez votre parcours SFMC

#### Étape 1 : Préparer le voyage

1. Dans Salesforce Marketing Cloud, accédez au **générateur de parcours** > **Journey Builder**.
2. Sélectionnez **Créer un nouveau voyage**.
3. Pour votre type de voyage, sélectionnez **Voyage en plusieurs étapes**, puis **Créer.**

![Une source d'entrée d'événement API connectée à un nœud d'arbre décisionnel et à plusieurs nœuds d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Étape 2 : Créer le voyage

**Créez une source d'entrée :**

1. Pour votre source d'entrée, faites glisser l'**événement API** vers le générateur de parcours.

!["API Event" sélectionné comme source d'entrée.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. Dans l'**événement API**, sélectionnez **Créer un événement**.

![L'option "créer un événement" dans l'API Événement.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Sélectionnez **Sélectionner l'extension de données**. Localisez et sélectionnez l'extension de données sur laquelle BrazeAI Decisioning Studio™ Go écrira des recommandations.
4\. Sélectionnez **Résumé** pour enregistrer vos modifications.
5\. Sélectionnez **Terminé** pour enregistrer l'événement API.

![Résumé de l'événement API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Ajouter un arbre décisionnel :**

1. Glissez-déposez un **arbre décisionnel** après l'**événement d'entrée dans l'API**.
2. Dans les détails de l'arbre **décisionnel**, sélectionnez **Modifier** pour le premier chemin.

![Décision Détails du fractionnement avec le bouton "Modifier".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Mettez à jour l'**arbre décisionnel** afin d'utiliser l'ID du modèle transmis par l'extension des données de recommandation. Emplacement/localisation du champ approprié sous **Données d'itinéraire**.

![La section Données d'itinéraire dans le chemin 1 de l'arbre décisionnel.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Sélectionnez votre événement d'entrée et localisez le champ ID du modèle souhaité, puis faites-le glisser dans l'espace de travail.

![L'ID du modèle d'e-mail à inclure.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Saisissez l'ID de votre premier modèle d'e-mail, puis sélectionnez **Terminé**.
6\. Sélectionnez **Résumé** pour enregistrer ce chemin.
7\. Ajoutez un chemin pour chacun de vos modèles d'e-mail, puis répétez les étapes 4 à 6 ci-dessus pour définir les critères de filtrage de sorte que l'ID du modèle corresponde à la valeur de l'ID de chaque modèle.
8\. Sélectionnez **Terminé** pour enregistrer le nœud de **fractionnement de la décision**.

![Deux chemins dans un arbre décisionnel pour chaque ID de modèle d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Ajoutez un e-mail pour chaque arbre décisionnel :**

1. Faites glisser un nœud **e-mail** dans chaque chemin de l'**arbre décisionnel**.
2. Sélectionnez **E-mail**, puis choisissez le modèle approprié pour chaque chemin d'accès (le modèle avec la valeur ID doit correspondre à la logique de votre arbre décisionnel).

![Un nœud d'e-mail a été ajouté au parcours.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Étape 3 : Activer le voyage

Après avoir configuré votre Teams, activez-le et partagez les détails suivants avec l'équipe BrazeAI Decisioning Studio™ Go :

* Journey ID
* Nom du voyage
* Clé de définition de l'événement API
* Recommandations extension des données clé externe

{% alert note %}
Le portail BrazeAI Decisioning Studio™ Go vous montre l'automatisation SFMC qu'il a provisionnée pour exporter les données relatives aux abonnés et à l'engagement une fois par jour. Si vous ouvrez cette automatisation dans SFMC, veillez à la mettre en ligne/en production/instantanée.
{% endalert %}

1. Dans le portail BrazeAI Decisioning Studio™ Go, copiez le **nom du parcours**.
2. Ensuite, dans Salesforce Marketing Cloud Journey Builder, collez le nom du parcours dans la barre de recherche.
3. Sélectionnez le nom du voyage. Notez que le voyage est actuellement à l'état de projet.
4. Sélectionnez **Valider**.

![Le voyage achevé pour activer.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Examinez ensuite les résultats de la validation et sélectionnez **Activer**.

![Recommandations énumérées dans la section Règles de validation.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. Dans le résumé du **parcours d'activation**, sélectionnez **Activer** à nouveau.

![Résumé pour le voyage.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Vous êtes prêt ! Vous pouvez désormais commencer à déclencher des envois par l'intermédiaire de BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Étapes suivantes

Maintenant que vous avez mis en place l'orchestration, passez à la conception de votre agent :

- [créez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
