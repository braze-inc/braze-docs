---
nav_title: Calendrier de Rokt
article_title: Calendrier de Rokt
alias: /fr/partners/rokt_calendar/
description: "Cet article décrit le partenariat entre Braze et Rokt Calendar, une technologie dynamique de marketing de calendrier qui permet aux marques de pousser des événements 1:1 et des communications promotionnelles."
page_type: partenaire
search_tag: Partenaire
---

# Calendrier de Rokt

> Rokt Calendar est une technologie dynamique de marketing de calendrier qui permet aux marques de pousser des événements 1:1 et des communications promotionnelles. sous forme d'événements de calendrier et de notifications, à travers un réseau propriétaire de calendriers d'abonnés.

L'intégration du calendrier Rokt et de Braze permet aux abonnés du calendrier Rokt et aux données d'abonnement associées d'être envoyés au Brésil.

Les clients peuvent utiliser la toile de Braze pour définir le ciblage de voyages, un segment de votre public, en utilisant l'événement du calendrier comme méthode de communication, de la même manière que les notifications SMS, e-mail et push sont utilisées. La segmentation du public peut être effectuée sur n'importe lequel des attributs standard de l'utilisateur Braze ainsi que sur les attributs personnalisés générés par l'abonnement au calendrier.

Rokt Calendar offre aux clients Braze la possibilité d’aligner leurs initiatives marketing personnalisées et d’étendre le contenu personnalisé au calendrier de l’utilisateur final. Ainsi, en faisant une expérience plus homogène pour l'utilisateur final et en développant davantage la coloration avec les services de nos clients.

## Pré-requis

| Exigences                               | Origine            | Qui                                        | Libellé                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------- | ------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte calendrier Rokt                  | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Un compte de calendrier Rokt spécifique au client sera configuré.                                                                                                                                                                                                                                                                        |
| Configuration du calendrier             | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Un calendrier sera mis en place pour refléter les besoins du contexte et des paramètres du client : <br>- Drapeau de fusion<br>- Drapeau de secours de l'abonné ID<br>- Capture d'email si nécessaire                                                                                                                  |
| Calendrier de Rokt - Identifiants OAuth | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Cette clé vous permettra de connecter vos comptes de calendrier Braze et Rokt. Il est mis en place pour chaque nouveau client Braze et ajouté à ‘Contenu connecté’ en Brésil. <br><br> `Gérer les paramètres` > `Contenu connecté` > `+Ajouter des identifiants`                                                             |
| Braze API Key and Permissions           | Brasero            | Client                                     | Chaque application a son propre jeu de clés API REST. Vous devrez créer une nouvelle clé API pouvant être créée dans la `Console développeur` > `Paramètres de l'API` > `+Créer une nouvelle clé API` avec `utilisateurs. les autorisations de rack`. <br>La clé API Braze devra être fournie à votre gestionnaire de compte Rokt. |
| ID de l'abonné externe                  | Client             | Client                                     | C'est l'identifiant qui sera utilisé par le processus d'abonnement au calendrier Rokt pour faire correspondre l'abonné au calendrier avec l'utilisateur Braze. C'est quelque chose qui est passé par le client à Rokt Calendar ou e-mail est utilisé.                                                                                    |
| Configuration du Webhook                | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Ajoutez le type de webhook Braze au centre de gestion en utilisant votre [point d'extrémité de Braze]({{site.baseurl}}/api/basics?redirected=true#endpoints) et votre clé d'API REST                                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration de l'API

### Établir une audience pour les abonnés au calendrier

Afin d'envoyer des événements de calendrier depuis Canvas en utilisant l'intégration du calendrier Rokt, il est nécessaire que vous ayez une configuration de calendrier Rokt et que les utilisateurs se soient inscrits au calendrier. Pour ce faire, vous devrez informer vos utilisateurs où et comment vous abonner au calendrier.

| Exigences                                     | Origine            | Qui                                        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration du compte calendrier de Rokt    | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Un compte de calendrier Rokt spécifique au client sera configuré, veuillez contacter [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) pour parler avec un gestionnaire de compte                                                                                                                                                                                                                                                                                               |
| Rokt Calendar Calendar Setup                  | Calendrier de Rokt | Gestionnaire de comptes calendrier de Rokt | Un calendrier sera mis en place pour refléter les besoins du client. Le gestionnaire de compte travaillera avec vous pour mettre en place le calendrier le mieux adapté à vos besoins.                                                                                                                                                                                                                                                                                                  |
| Fournir des points d’intégration d’abonnement | Client             | Client                                     | Afin de créer un public d'abonnés au calendrier, vous devrez offrir une destination à laquelle l'utilisateur peut naviguer et s'abonner au calendrier.<br><br>Exemples de point d'intégration de l'abonnement :<br>- Ajouter au bouton calendrier à votre site web<br>- Ajouter au bouton calendrier à votre application<br>- Ajouter au lien calendrier dans un e-mail ou un SMS<br>- Ajouter au lien calendrier sur les réseaux sociaux<br> |
| Promouvoir le calendrier                      | Client             | Client                                     | Afin de créer un public d’abonnés au calendrier, vous devrez promouvoir le calendrier auprès de votre public afin qu’il sache où/comment s’abonner. <br><br>Exemples de promotion du calendrier :<br>- Posts sur les médias sociaux<br>- Courriels de newsletters et mises à jour<br>- Articles de blog<br>- Notifications dans l'application                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Segmentation de l'auditoire dans Braze

Quand Rokt crée un nouvel utilisateur ou correspond à un abonné existant avec un utilisateur Braze, Rokt enverra les attributs d'abonnement suivants que vous pouvez filtrer au Brésil :

| Attribut personnalisé     | Définition                                                                     | Exemple                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `rokt:account_code`       | Code du compte calendrier Rokt                                                 | `brazetest/f5733866ade2` et `brazetest/ff10919f1078`                                               |
| `rokt:account_id`         | ID du compte de calendrier Rokt                                                | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2`                                                |
| `rokt:nom_compte`         | Nom du compte calendrier Rokt                                                  | `Braze Test/f5733866ade2`                                                                          |
| `rokt:calendar_code`      | Code du calendrier Rokt                                                        | `test-calendar-1/f5733866ade2`                                                                     |
| `rokt:calendar_id`        | ID du calendrier Rokt                                                          | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2`                                                |
| `rokt:calendar_title`     | Titre du calendrier Rokt                                                       | `Test Calendar 1/f5733866ade2`                                                                     |
| `rokt:country_code`       | Code pays lié à l'abonnement créé                                              | `AU/f5733866ade2`                                                                                  |
| `rokt:device_name`        | Type d'appareil lié à l'abonnement créé                                        | `Desktop/f5733866ade2`                                                                             |
| `rokt:geo_country`        | Pays d'origine lié à l'abonnement créé                                         | `Australia/f5733866ade2`                                                                           |
| `rokt:optIn1`             | Si l'utilisateur a opté pour le premier des 2 opt-ins liés à l'abonnement créé | `True/f5733866ade2`                                                                                |
| `rokt:optIn2`             | Si l'utilisateur a opté à la seconde de 2 opt-ins liés à l'abonnement créé     | `True/f5733866ade2`                                                                                |
| `rokt:source`             | La source de l'abonnement créé                                                 | `Calendrier Rokt`                                                                                  |
| `rokt:subscriber_email`   | L'adresse e-mail saisie par l'utilisateur lors du processus d'abonnement       | `test@email.com/f5733866ade2`                                                                      |
| `rokt:subscription_id`    | L'ID d'abonnement, servant d'identifiant unique, lié à l'abonnement créé       | `06423672-b6ba-4536-aa36-70788a7a0a36`                                                             |
| `rokt:abonnement_méthode` | Méthode d'abonnement (webcal/Google) liée à l'abonnement créé.                 | `WebCal/f5733866ade2`                                                                              |
| `rokt:tags`               | Étiquettes de calendrier utilisées en relation avec l'abonnement créé.         | `Calendrier de test 1/Toutes les équipes/f5733866ade2 et Calendrier de test 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

De plus, Rokt déclenchera également un événement personnalisé `subscribe` dès que l'utilisateur est abonné à votre calendrier Rokt qui peut être utilisé soit dans la segmentation de Braze soit comme déclencheur pour une étape de campagne ou de Canvan.

## Utiliser le calendrier Rokt dans vos campagnes de Braze et vos toiles

Au sein de Braze, vous pouvez mettre en place une campagne de webhook ou un webhook dans un Canvas à soit :

- __Envoyer un nouvel événement personnalisé__: cela permettra d'ajouter de nouveaux événements à un segment des calendriers des abonnés.
- __Mise à jour événement personnalisé__: Ceci permettra de mettre à jour un événement qui a déjà été ajouté aux calendriers des abonnés.

Avant de commencer, les champs ci-dessous détaillent les informations qui peuvent être personnalisées au niveau de l'événement.

| Champ                                        | Définition                                                                                                                                                                                                | Exemple                                                                                    |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `eventId` <br>*__Requis__              | Un identifiant unique pour l'événement à ajouter ou à mettre à jour                                                                                                                                       | `Événement_00001`                                                                          |
| `titre de l'événement` <br>*__Requis__ | Le titre de l'événement tel qu'il apparaîtra dans le calendrier                                                                                                                                           | Soldes d'été 2019                                                                          |
| `Description de l'événement`                 | La description de l'événement tel qu'il apparaîtra dans le calendrier                                                                                                                                     | La vente dure 3 jours, cliquez sur ce lien `www.mybusiness.com/sale` pour voir les offres. |
| `Localisation de l'événement`                | L'emplacement de l'événement tel qu'il apparaîtra dans le calendrier, notez que cela est souvent utilisé comme un deuxième appel à l'action qui est complémentaire au titre de l'événement.               | Ouvrez l'événement pour obtenir 50 % de réduction                                          |
| `eventStart` <br>*__Requis__           | La date et l'heure de début de l'événement telle qu'elle apparaît dans le calendrier                                                                                                                      | `2019-02-21T15:00:00`                                                                      |
| `event End` <br>*__Requis__            | La date et l'heure de début de l'événement telle qu'elle apparaît dans le calendrier                                                                                                                      | `2019-02-21T16:00:00`                                                                      |
| `eventTz` <br>*__Requis__              | Le fuseau horaire de l'événement tel qu'il apparaîtra dans le calendrier, Notez que la liste des fuseaux horaires applicables peut être trouvée [ici](https://roktcalendar-api.readme.io/docs/timezones). | `Heure normale de l'Est`                                                                   |
| `notifyAvant` <br>*__Requis__          | L'heure de rappel de l'événement tel qu'il apparaîtra dans le calendrier, notez que ceci est exprimé en minutes                                                                                           | `15`                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% tabs %}
{% tab Send a New Event %}
## Envoyer un nouvel événement

### Étape 1 : Créer un modèle de webhook dans Braze

Pour créer un nouveau modèle de Webhook de calendrier Rokt, vous pouvez soit naviguer vers **Modèles & Médias** ou créer une nouvelle campagne de webhook via le tableau de bord.

Dans la liste des modèles, sélectionnez **Modèle vierge**.

### Étape 2 : Remplissez votre modèle

Le modèle de Webhook vide se compose de deux composants principaux, l’onglet composition et paramètres. Ci-dessous nous allons décomposer les composants de chaque onglet et les paramètres que vous devez définir.

#### Étape 2: Webhook - paramètres

Naviguez dans l'onglet paramètres et éditez les champs __En-tête de requête__ et __Méthode HTTP__ avec les segments de texte correspondants.

| En-têtes de la requête                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Autorisation | {% raw %}Porteur {% connected_content https://api.roktcalendar. om/oauth2/token :method post :basic_auth Rokt-Calendar-API :body grant_type=client_credentials :save token :retry %}{{token.access_token}}{% endraw %} <br><br> Note: __Rokt-Calendar-API__ doit être remplacé par le nom d'identification trouvé dans `Gérer les paramètres` > `Contenu connecté` > `Identifiants` |
| Content-Type | application/json                                                                                                                                                                                                                                                                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2}

| Méthode HTTP |
| ------------ |
| POSTER       |
{: .reset-td-br-1 .reset-td-br-2}

#### Étape 2b: Webhook - composer

Complétez la configuration en naviguant dans l'onglet Composer et définissez l'URL __Webhook__ et modifiez le contenu du __Corps de Requête__ en fonction des attributs et des tableaux de champs indiqués ci-dessus.

| URL du Webhook                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {% raw %}{% assigner accountCode = {{custom_attribute.${rokt:account_code}}}[0] &#124; divisé : '/' &#124; premier %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}} {% endraw %} |
{: .reset-td-br-1}

##### Corps de la requête

{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Lieu de l'événement{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "titre": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "emplacement": "{{eventLocation}}",
    "départ": "{{eventStart}}",
    "fin": "{{eventEnd}}",
    "fuseau horaire": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.{rokt:subscription_id}| rejoindre: '","' }}"]
}
```
{% endraw %}

{% alert tip %}

Pour une liste de fuseaux horaires valides, voir [https://roktcalendar-api.readme.io/docs/timefuseaux](https://roktcalendar.readme.io/docs/timezones).

{% endalert %}

### Étape 3 : Aperçu de votre demande

Vous verrez que votre texte brut met automatiquement en évidence s'il s'agit d'une balise Braze applicable.

Vous devriez être en mesure de prévisualiser votre demande dans le panneau de gauche ou de naviguer vers l’onglet `Tester` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook.

N'oubliez pas d'enregistrer votre modèle avant de quitter la page!

{% endtab %}
{% tab Update to Existing Event %}

## Mettre à jour un événement existant

### Étape 1 : Créer un modèle de webhook dans Braze

Pour créer un nouveau modèle de Webhook de calendrier Rokt, vous pouvez soit naviguer vers **Modèles & Médias** ou créer une nouvelle campagne de webhook via le tableau de bord.

Dans la liste des modèles, sélectionnez **Modèle vierge**.

### Étape 2 : Remplissez votre modèle

Le modèle de Webhook vide se compose de deux composants principaux, l’onglet composition et paramètres. Ci-dessous nous allons décomposer les composants de chaque onglet et les paramètres que vous devez définir.

#### Étape 2: Webhook - paramètres

Naviguez dans l'onglet paramètres et éditez les champs __En-tête de requête__ et __Méthode HTTP__ avec les segments de texte correspondants.

| En-têtes de la requête |                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Autorisation           | {% raw %}Porteur {% connected_content https://api.roktcalendar. om/oauth2/token :method post :basic_auth Rokt-Calendar-API :body grant_type=client_credentials :save token :retry %}{{token.access_token}}{% endraw %} <br><br> Note: __Rokt-Calendar-API__ doit être remplacé par le nom d'identification trouvé dans `Gérer les paramètres` > `Contenu connecté` > `Identifiants` |
| Type de contenu        | application/json                                                                                                                                                                                                                                                                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2}

| Méthode HTTP |
| ------------ |
| POSTER       |
{: .reset-td-br-1}

#### Étape 2b: Webhook - composer

Complétez la configuration en naviguant dans l'onglet Composer et définissez l'URL __Webhook__ et modifiez le contenu du __Corps de Requête__ en fonction des attributs et des tableaux de champs indiqués ci-dessus.

| URL du Webhook                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| {% raw %}{% assigner accountCode = {{custom_attribute.${rokt:account_code}}}[0] &#124; split: '/' &#124; first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update {% endraw %} |
{: .reset-td-br-1}

##### Corps de la requête
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Lieu de l'événement{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "titre": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "emplacement": "{{eventLocation}}",
    "départ": "{{eventStart}}",
    "fin": "{{eventEnd}}",
    "fuseau horaire": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
}

```
{% endraw %}

{% alert tip %}

Pour une liste de fuseaux horaires valides, voir [https://roktcalendar-api.readme.io/docs/timefuseaux](https://roktcalendar-api.readme.io/docs/timezones).

{% endalert %}

### Étape 3 : Aperçu de votre demande

Vous verrez que votre texte brut met automatiquement en évidence s'il s'agit d'une balise Braze applicable.

Vous devriez être en mesure de prévisualiser votre demande dans le panneau de gauche ou de naviguer vers l’onglet `Tester` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook.

N'oubliez pas d'enregistrer votre modèle avant de quitter la page!

{% endtab %}
{% endtabs %}
