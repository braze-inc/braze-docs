---
title: Glossaire des codes ou API
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Il s’agit de la description Google Search. Les phrases de plus de 160 caractères seront tronquées… soyez concis !"
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 Créer un modèle d’e-mail
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Publier,E-mail,Créer,Modèle,API,REST
{% endapitags %}

Utilisez les API REST du modèle d’e-mail pour gérer par programme les modèles d’e-mail que vous avez stockés sur les tableaux de bord de Braze de la page Templates & Media (Modèles et médias). Braze fournit deux endpoints pour la création et la mise à jour de vos modèles d’e-mail.

La réponse de cet endpoint comprend un champ `email_template_id` qui peut être utilisé pour mettre à jour le modèle lors des prochains appels d’API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### EXEMPLE DE RÉPONSE
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `modified_after`  | Non | Chaîne de caractères au format ISO 8601 | Récupérer uniquement les modèles mis à jour à l’heure donnée ou après. |
| `modified_before`  |  Non | Chaîne de caractères au format ISO 8601 | Récupérer uniquement les modèles mis à jour à l’heure donnée ou avant. |
| `limit` | Non | Nombre positif | Nombre maximum de modèles à récupérer. Sauf indication contraire, la limite par défaut est de 100 modèles et la valeur maximum est de 1 000. |
| `offset`  |  Non | Nombre positif | Nombre de modèles à ignorer avant de renvoyer le reste des modèles qui correspondent aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 Répertorier les modèles d’e-mail disponibles
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Obtenir,E-mail,Modèle,Liste,REST
{% endapitags %}

Utilisez les endpoints ci-dessous pour obtenir une liste de tous les modèles disponibles.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### EXEMPLE DE RÉPONSE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Oui | Chaîne de caractères | L’identifiant API de votre modèle d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 Envoi de déclencheurs de campagnes
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Publier, Campagnes, Déclencheur, Envoyer{% endapitags %}

La livraison déclenchée par API vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### EXEMPLE DE RÉPONSE
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Oui | Chaîne de caractères | L’identifiant API de votre modèle d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 Envoi de déclencheurs de campagnes
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campagnes, Déclencheur, Envoyer{% endapitags %}

Cet endpoint permet d’enregistrer des événements personnalisés, des attributs utilisateur et des achats concernant les utilisateurs. Vous pouvez inclure jusqu’à 75 attributs, événements et objets d’achat par requête. Les attributs peuvent être publiés pour un maximum de 75 utilisateurs à la fois, mais vous pouvez également fournir jusqu’à 75 événements et 75 achats avec le même appel d’API.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### EXEMPLE DE RÉPONSE
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### INFORMATIONS SUR LES PARAMÈTRES

| Champ profil utilisateur | Spécification des types de données |
| ---| --- |
| pays | (chaîne de caractères) Nous vous demandons de transmettre les indicatifs nationaux à Braze selon la [norme ISO-3166-1 alpha-2][17]. |
| current_location | (objet) du formulaire {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date à laquelle l’utilisateur s’est servi de l’application pour la première fois) Chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| date_of_last_session | (date à laquelle l’utilisateur s’est servi de l’application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| ddn | (date de naissance) Chaîne au format "AAAA-MM-JJ", par exemple, 1980-12-21. |
| e-mail | (string) |
| email_subscribe | (chaîne de caractères) Les valeurs disponibles sont « opted_in » (confirmé : explicitement consenti à recevoir des e-mails), « unsubscribed » (désabonné : a explicitement refusé de recevoir des e-mails), et « subscribed » (abonné : ni accepté, ni refusé).  |
| external_id | (chaîne de caractères) De l’identifiant utilisateur unique. |
| facebook | hachage contenant l’un des `id` (string), `likes` (array of strings), `num_friends` (integer). |
| Prénom | (string) |
| genre | (string) « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). |
| ville | (string) |
| image_url | (chaîne de caractères) URL de l’image à associer au profil utilisateur. |
| langue | (string) la langue doit être transmise à Braze selon la [norme ISO-639-1][24]. <br>[Liste des langues acceptées][1]|
| Nom | (string) |
|email_marqué_comme_spam_à| (chaîne de caractères) Date à laquelle l’e-mail de l’utilisateur a été marqué comme courrier indésirable. La liste est affichée au format ISO 8601 ou au format yyyy-MM-dd'T'HH:mm:ss:SSSZ.|
| téléphone | (string) |
| abonnement aux notifications push | (chaîne de caractères) Les valeurs disponibles sont « confirmé » (a explicitement consenti à recevoir des notifications push), « désabonné » (a explicitement refusé de recevoir des notifications push), et « abonné » (a ni accepté, ni refusé).  |
| push_tokens | Tableau d’objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l’appareil auquel ce jeton est associé, par exemple, `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun `device_id` n’est pas fourni, il sera généré de manière aléatoire. |
| time_zone | (chaîne de caractères) Nom de fuseau horaire de la [base de données de fuseaux horaires IANA][26] (par ex. « Amérique/New_York » ou « Heure de l’Est [États-Unis et Canada] »). Seules les valeurs de fuseau horaire valides seront définies. |
| twitter | Hachage contenant l'un des éléments suivants : `id` (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
