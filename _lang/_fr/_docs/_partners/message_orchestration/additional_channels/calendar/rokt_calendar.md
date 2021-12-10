---
nav_title: Calendrier de Rokt
article_title: Calendrier de Rokt
alias: /fr/partners/rokt_calendar/
description: "Cet article décrit le partenariat entre Braze et Rokt Calendar, une technologie dynamique de marketing de calendrier qui permet aux marques de pousser des événements 1:1 et des communications promotionnelles, sous la forme d'événements de calendrier et de notifications."
page_type: partenaire
search_tag: Partenaire
---

# Calendrier de Rokt

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) est une technologie de marketing de calendrier dynamique qui permet aux marques de pousser des événements 1:1 et des communications promotionnelles sous la forme d'événements de calendrier et de notifications.

L'intégration du calendrier Braze et Rokt permet à vos abonnés du calendrier Rokt et à leurs données d'être poussées à Braze via le webhook de Braze. Vous pouvez ensuite utiliser ces données dans Braze Canvases pour cibler votre voyage et segmenter votre audience en utilisant n'importe lequel des attributs personnalisés du calendrier Rokt listés [ci-dessous](#audience-segmentation).

## Pré-requis

| Exigences                                                                 | Libellé                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte calendrier Rokt                                                    | Un compte client spécifique à Rokt Calendar est nécessaire pour profiter de ce partenariat. Veuillez contacter [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) pour parler à un responsable de compte                                                                    |
| Rokt Calendar setup                                                       | Votre gestionnaire de compte Rokt Calendar travaillera avec vous pour configurer le calendrier selon vos besoins, y compris les paramètres comme:<br>- Drapeau de fusion<br>- Drapeau de secours de l'abonné ID<br>- Capture d'e-mail, si nécessaire             |
| Identifiants OAuth du calendrier de Rokt                                  | Cette clé fournie par votre gestionnaire de comptes Rokt vous permettra de connecter vos comptes de calendrier Braze et Rokt.<br><br>Ceci peut être créé dans le tableau de bord Braze sous **Gérer les paramètres > Contenu connecté > +Ajouter des identifiants**.   |
| Braze clé API REST                                                        | Une clé API Braze REST avec les permissions `users.track`. Vous devrez fournir cette clé à votre gestionnaire de compte de Rokt.<br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__. |
| [Point de terminaison REST Braze]({{site.baseurl}}/api/basics/#endpoints) | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                                                                                          |
| ID de l'abonné externe                                                    | Il s'agit de l'identifiant utilisé par le processus d'abonnement à Rokt Calendar pour faire correspondre l'abonné au calendrier avec l'utilisateur Braze. C'est quelque chose que vous passez au calendrier Rokt.                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

## Segmentation de l'audience {#audience-segmentation}

Quand Rokt Calendar crée un nouvel utilisateur ou correspond à un abonné existant avec un utilisateur de Braze, Le calendrier Rokt enverra les attributs d'abonnement personnalisés suivants que vous pouvez filtrer au Brésil :

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

Le calendrier Rokt déclenchera également un événement personnalisé `subscribe` dès que l'utilisateur s'est abonné à votre calendrier Rokt qui peut être utilisé soit dans la segmentation de Braze soit comme déclencheur pour une étape de campagne ou de Canvan.

## Intégration

### Étape 1 : Créer une audience pour les abonnés du calendrier

Pour envoyer des événements de calendrier depuis Canvas, vous devez d'abord avoir une configuration de calendrier Rokt avec les utilisateurs déjà abonnés. Pour ce faire, vous devrez informer vos utilisateurs où et comment vous abonner au calendrier. Le calendrier Rokt vous recommande :

#### Fournir des points d’intégration d’abonnement
Pour créer un public d'abonnés au calendrier, vous devez offrir une destination à laquelle un utilisateur peut naviguer et s'abonner. Quelques exemples de points d'intégration de l'abonnement incluent :
  - Ajouter un bouton calendrier à votre site web
  - Ajout d'un lien de calendrier dans un e-mail ou un SMS
  - Ajouter un bouton calendrier à votre application
  - Ajouter un lien de calendrier sur les réseaux sociaux

#### Promouvoir le calendrier
Pour créer un public d'abonnés, vous devrez promouvoir le calendrier auprès de votre public afin qu'il sache comment vous abonner. Certains exemples de promotion du calendrier incluent :
  - Publications sur les réseaux sociaux
  - Newsletters et mises à jour par e-mail
  - Articles du blog
  - Notifications In-App

### Étape 2 : Créez un webhook de Rokt Calendar dans Braze

Au sein de Braze, vous pouvez mettre en place une campagne de webhook ou un webhook dans un Canvas à soit :

- Envoyer un nouvel événement personnalisé : Permettre l'ajout de nouveaux événements à un segment des calendriers des abonnés.
- Mettre à jour un événement personnalisé : Permet de mettre à jour un événement existant dans les calendriers des abonnés.

Créer un modèle de webhook de Rokt Calendar à utiliser dans de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne de webhook unique de Rokt ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

{% tabs %}
{% tab Send a new event %}
Une fois que vous avez sélectionné le modèle de webhook de Rokt Calendar, vous devriez voir ce qui suit :
- **URL du Webhook**: {% raw %}`{% assigner accountCode = {{custom_attribute.${rokt:account_code}}}[0] | division : '/' | premier %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Corps de la requête**: Texte brut
{% endtab %}
{% tab Update an existing event %}
Une fois que vous avez sélectionné le modèle de webhook de Rokt Calendar, vous devriez voir ce qui suit :
- **URL du Webhook**: {% raw %}`{% assigner accountCode = {{custom_attribute.${rokt:account_code}}}[0] | division : '/' | premier %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Corps de la requête**: Texte brut
{% endtab %}
{% endtabs %}

#### En-têtes de requête et méthode

Le calendrier Rokt nécessite un `en-tête HTTP` pour être autorisé qui inclut votre nom d’identification de contenu connecté au calendrier Rokt. Les éléments suivants seront déjà inclus dans le modèle en tant que paires clé-valeur, mais dans l'onglet **Paramètres** , vous devez remplacer `<Rokt-Calendar-API>` par le nom d'identification trouvé dans `Gérer les paramètres > Contenu connecté > Identifiant`.

{% raw %}
- **Méthode HTTP**: POST
- **En-tête de la requête**:
  - **Autorisation**: Porteur `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Corps de la requête**: application/json
{% endraw %}

#### Corps de la requête

{% tabs local %}
{% tab Send a new event %}
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
{% endtab %}
{% tab Update an existing event %}
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
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
La liste ci-dessous contient des informations qui peuvent être personnalisées au niveau de l'événement.

| Champ                                        | Définition                                                                                                                                                                                                | Exemple                                                                                         |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `eventId` <br>*__Requis__              | Un identifiant unique pour l'événement à ajouter ou à mettre à jour                                                                                                                                       | `Événement_00001`                                                                               |
| `titre de l'événement` <br>*__Requis__ | Le titre de l'événement tel qu'il apparaîtra dans le calendrier                                                                                                                                           | Soldes d'été 2019                                                                               |
| `Description de l'événement`                 | La description de l'événement tel qu'il apparaîtra dans le calendrier                                                                                                                                     | La vente dure trois jours ; cliquez sur ce lien `www.mybusiness.com/sale` pour voir les offres. |
| `Localisation de l'événement`                | L'emplacement de l'événement tel qu'il apparaîtra dans le calendrier, notez que cela est souvent utilisé comme un deuxième appel à l'action, qui est complémentaire au titre de l'événement.              | Ouvrez l'événement pour obtenir 50 % de réduction                                               |
| `eventStart` <br>*__Requis__           | La date et l'heure de début de l'événement telle qu'elle apparaît dans le calendrier                                                                                                                      | `2019-02-21T15:00:00`                                                                           |
| `event End` <br>*__Requis__            | La date et l'heure de début de l'événement telle qu'elle apparaît dans le calendrier                                                                                                                      | `2019-02-21T16:00:00`                                                                           |
| `eventTz` <br>*__Requis__              | Le fuseau horaire de l'événement tel qu'il apparaîtra dans le calendrier, Notez que la liste des fuseaux horaires applicables peut être trouvée [ici](https://roktcalendar-api.readme.io/docs/timezones). | `Heure normale de l'Est`                                                                        |
| `notifyAvant` <br>*__Requis__          | L'heure de rappel de l'événement tel qu'il apparaîtra dans le calendrier, notez que ceci est exprimé en minutes                                                                                           | `15`                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour une liste de fuseaux horaires valides, voir [https://roktcalendar-api.readme.io/docs/fuseaux horaires](https://roktcalendar.readme.io/docs/timezones).
{% endalert %}

### Étape 3 : Aperçu de votre demande

Prévisualisez votre demande dans le panneau de gauche ou accédez à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
