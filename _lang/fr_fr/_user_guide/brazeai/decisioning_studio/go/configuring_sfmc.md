---
nav_title: Configuration avec Salesforce Marketing Cloud
article_title: Configurer avec Salesforce Marketing Cloud pour BrazeAI Decisioning Studio Go
page_order: 5
description: "Découvrez comment configurer une automatisation des requêtes de données et un parcours dans Salesforce Marketing Cloud pour une utilisation avec BrazeAI Decisioning <sup>StudioTM</sup> Go."
toc_headers: h2
---

# Configurez avec Salesforce Marketing Cloud pour BrazeAI Decisioning Studio™ Go.

> Configurez un parcours dans Salesforce Marketing Cloud (SFMC) pour commencer à déclencher des envois par l'intermédiaire de BrazeAI Decisioning Studio™ Go.

## Mise en place d'une automatisation des requêtes de données

### Étape 1 : Créer une nouvelle automatisation

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

### Étape 2 : Créez vos requêtes SQL

Ensuite, nous allons créer 2 requêtes SQL : une requête sur les abonnés et une requête sur l'engagement. Ces requêtes permettent à BrazeAI Decisioning Studio™ Go de récupérer des données pour alimenter l'audience et ingérer des événements d'engagement.

{% tabs %}
{% tab Subscribers query %}
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
{% endtab %}
{% tab Engagement query %}
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
Le nom de l'extension des données cibles est également fourni dans votre portail BrazeAI Decisioning Studio™ Go pour faire des références croisées.  Assurez-vous que vous regardez l'extension de données cible pour la requête d'engagement. L'**extension de données** pour la demande d'engagement doit se terminer par un suffixe ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Sélectionnez **Écraser**, puis **Suivant.**

![Le nom de l'extension de données qui correspond à la clé externe de l'exemple.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### Étape 3 : Lancer l'automatisation

1. Donnez un nom à l'automatisation et sélectionnez **Enregistrer.**

![Un exemple d'automatisation "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Ensuite, sélectionnez **Exécuter une fois** pour confirmer que tout fonctionne comme prévu.
3\. Sélectionnez les deux requêtes et choisissez **Exécuter**.

![Une automatisation "OFE_Experimenter_Test5_Automation" avec une liste d'activités de requêtes SQL sélectionnées à exécuter.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Sélectionnez **Exécuter maintenant.**

![Une activité de requêtes SQL sélectionnée.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Vous pouvez maintenant vérifier que l'automatisation se déroule correctement. Contactez l'assistance de Braze pour obtenir de l'aide si votre automatisation ne fonctionne pas comme prévu.

## Créer votre parcours SFMC

### Étape 1 : Préparer le voyage

1. Dans Salesforce Marketing Cloud, accédez au **générateur de parcours** > **Journey Builder**.
2. Sélectionnez **Créer un nouveau voyage**.
3. Pour votre type de voyage, sélectionnez **Voyage en plusieurs étapes**, puis **Créer.**

![Une source d'entrée d'événement API connectée à un nœud d'arbre décisionnel et à plusieurs nœuds d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### Étape 2 : Créer le voyage

#### Étape 2.1 : Créer une source d'entrée

1. Pour votre source d'entrée, faites glisser l'**événement API** vers le générateur de parcours.

!["API Event" sélectionné comme source d'entrée.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. Dans l'**événement API**, sélectionnez **Créer un événement**.

![L'option "créer un événement" dans l'API Événement.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Sélectionnez **Sélectionner l'extension de données**. Localisez et sélectionnez l'extension de données sur laquelle BrazeAI Decisioning Studio™ Go écrira des recommandations.
4\. Sélectionnez **Résumé** pour enregistrer vos modifications.
5\. Sélectionnez **Terminé** pour enregistrer l'événement API.

![Résumé de l'événement API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### Étape 2.2 : Ajouter un arbre décisionnel

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

#### Étape 2.3 : Ajouter un e-mail pour chaque arbre décisionnel

1. Faites glisser un nœud **e-mail** dans chaque chemin de l'**arbre décisionnel**.
2. Sélectionnez **E-mail**, puis choisissez le modèle approprié pour chaque chemin d'accès (le modèle avec la valeur ID doit correspondre à la logique de votre arbre décisionnel).

![Un nœud d'e-mail a été ajouté au parcours.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Étape 3 : Activer le voyage

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
