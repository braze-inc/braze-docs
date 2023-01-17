---
title: API or Code Glossary
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Il s’agit de la description Google Search. Les phrases de plus de 160 caractères seront tronquées… soyez concis !"
page_type: glossary
#À utiliser, si applicable

tool:
  - Tableau de bord
  - Docs
  - Canvas
  - Campagnes
  - Segments
  - Modèles
  - Médias
  - Localisation
  - Currents
  - Rapports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - cartes de contenu
  - E-mail
  - Fil d’actualité
  - Messages in-app
  - Notification push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: supprimer le noindex et l’alerte de ce modèle

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

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
{
  "template_name": "email_template_name",
  "subject": "Bienvenue dans mon nouveau modèle d’e-mail !",
  "body": "Il s’agit du texte du corps de mon e-mail. https://www.braze.com/ est un lien vers Braze.com.",
  "plaintext_body": "Il s’agit du texte du corps de mon e-mail avec un lien vers Braze.com.",
  "preheader": "Mon accroche est impeccable."
}

```

#### EXEMPLE DE RÉPONSE
```
{
  "template_name": "email_template_name",
  "subject": "Bienvenue dans mon nouveau modèle d’e-mail !",
  "body": "Il s’agit du texte du corps de mon e-mail. https://www.braze.com/ est un lien vers Braze.com.",
  "plaintext_body": "Il s’agit du texte du corps de mon e-mail avec un lien vers Braze.com.",
  "preheader": "Mon accroche est impeccable."
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `modified_after`  | Non | Chaîne de caractères au format ISO 8601 | Récupérer uniquement les modèles mis à jour à l’heure donnée ou après. |
| `modified_before`  |  Non | Chaîne de caractères au format ISO 8601 | Récupérer uniquement les modèles mis à jour à l’heure donnée ou avant. |
| `limit` | Non | Nombre positif | Nombre maximum de modèles à récupérer. Sauf indication contraire, la limite par défaut est de 100 modèles et la valeur maximum est de 1 000. |
| `offset`  |  Non | Nombre positif | Nombre de modèles à ignorer avant de renvoyer le reste des modèles qui correspondent aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


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

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: nombre de modèles renvoyés
  “templates”: [modèle comportant les propriétés suivantes] :
    “email_template_id”: (chaîne de caractères) l’identifiant API de votre modèle d’e-mail,
    “template_name”: (chaîne de caractères) le nom de votre modèle d’e-mail,
    “created_at”: (chaîne de caractères au format ISO 8601),
    “updated_at”: (chaîne de caractères au format ISO 8601)
}

```

#### EXEMPLE DE RÉPONSE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: nombre de modèles renvoyés
  “templates”: [modèle comportant les propriétés suivantes] :
    “email_template_id”: (chaîne de caractères) l’identifiant API de votre modèle d’e-mail,
    “template_name”: (chaîne de caractères) le nom de votre modèle d’e-mail,
    “created_at”: (chaîne de caractères au format ISO 8601),
    “updated_at”: (chaîne de caractères au format ISO 8601)
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Oui | Chaîne de caractères | L’identifiant API de votre modèle d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 3 Envoi de déclencheurs de campagnes
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}Publier, Campagnes, Déclencheur, Envoyer{% endapitags %}

La livraison déclenchée par API vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API. 

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (obligatoire, chaîne de caractères) voir l’identifiant de campagne,
  "send_id": (optionnel, chaîne de caractères) voir l’identifiant d’envoi,
  "trigger_properties": (optionnel, objet) les paires clé-valeur de personnalisation qui s’appliquent à tous les utilisateurs de cette demande,
  "broadcast": (optionnel, booléen) voir Diffusion ; défini par défaut sur « faux » le 31/8/17, doit être défini sur « vrai » si "recipients" est absent,
  "audience": (optionnel, objet d’audience connectée) voir Audience connectée,
  // En incluant 'audience', les messages seront uniquement envoyés aux utilisateurs de l’audience en question
  "recipients": (optionnel, tableau ; si non renseigné et que la diffusion n’est pas définie sur « faux », le message sera envoyé au segment entier ciblé par la campagne) [
    {
      // "external_user_id" ou "user_alias" est requis. Les demandes ne doivent en spécifier qu’un seul des deux.
      "user_alias": (optionnel, objet alias utilisateur) l’alias utilisateur de l’utilisateur devant recevoir le message,
      "external_user_id": (optionnel, chaîne de caractères) l’ID externe de l’utilisateur devant recevoir des messages,
      "trigger_properties": (optionnel, objet) les paires clé-valeur de personnalisation qui s’appliquent à cet utilisateur (ces paires clé-valeur remplaceront toute clé qui entre en conflit avec les trigger_properties du parent)
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
  "canvas_id": (obligatoire, chaîne de caractères) voir l’identifiant Canvas,
  "canvas_entry_properties": (optionnel, objet) les paires clé-valeur de personnalisation qui s’appliquent à tous les utilisateurs de cette demande,
  "broadcast": (optionnel, booléen) voir Diffusion ; défini par défaut sur « faux » le 31/8/17, doit être défini sur « vrai » si "recipients" est absent,
  "audience": (optionnel, objet d’audience connectée) voir Audience connectée,
  // En incluant 'audience', les messages seront uniquement envoyés aux utilisateurs de l’audience en question
  "recipients": (optionnel, tableau ; si non renseigné et que la diffusion n’est pas définie sur « faux », le message sera envoyé au segment entier ciblé par le Canvas) [
    {
      // "external_user_id" ou "user_alias" est requis. Les demandes ne doivent en spécifier qu’un seul des deux.
      "user_alias": (optionnel, objet alias utilisateur) l’alias utilisateur de l’utilisateur devant recevoir le message,
      "external_user_id": (optionnel, chaîne de caractères) l’ID externe de l’utilisateur devant recevoir des messages,
      "canvas_entry_properties": (optionnel, objet) les paires clé-valeur de personnalisation qui s’appliquent à l’utilisateur (ces paires clé-valeur vont écraser toute clé qui entre en conflit avec les canvas_entry_properties du parent)
    },
    ...
  ]
}
```


#### INFORMATIONS SUR LES PARAMÈTRES

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Oui | Chaîne de caractères | L’identifiant API de votre modèle d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 4 Envoi de déclencheurs de campagnes
{% apimethod put %}users/track{% endapimethod %}
{% apitags %}PUT, Campagnes, Déclencheur, Envoyer{% endapitags %}

Cet endpoint permet d’enregistrer des événements personnalisés, des attributs utilisateur et des achats concernant les utilisateurs. Vous pouvez inclure jusqu’à 75 attributs, événements et objets d’achat par requête. Les attributs peuvent être publiés pour un maximum de 75 utilisateurs à la fois, mais vous pouvez également fournir jusqu’à 75 événements et 75 achats avec le même appel d’API.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### CORPS DE LA DEMANDE
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optionnel, tableau d’objets d’attribut),
   "events" : (optionnel, tableau d’objets d’événement),
   "purchases" : (optionnel, tableau d’objets d’achat)
}

```

#### EXEMPLE DE RÉPONSE
```
{
  // Un parmi "external_id", "user_alias" ou "braze_id" est obligatoire
  "external_id" : (optionnel, chaîne de caractères), voir l’ID d’utilisateur externe,
  "user_alias" : (optionnel, objet d’alias utilisateur),
  "braze_id" : (optionnel, chaîne de caractères) identifiant de l’utilisateur Braze,
  // Définir cet indicateur sur « vrai » placera l’API en mode « Update Only ».
  // Lorsqu’un "user_alias" est utilisé, le mode « Update Only » est toujours « vrai ».
  "_update_existing_only" : (optionnel, booléen),
  // Consultez les notes concernant l’importation de jetons de notification push anonymes
  "push_token_import" : (optionnel, booléen).
  // Champs Braze User Profile (Profil d’utilisateur Braze)
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Attributs personnalisés
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Ajouter une nouvelle valeur dans un tableau d’attributs personnalisés
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Supprimer une valeur d’un tableau d’attributs personnalisés
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### INFORMATIONS SUR LES PARAMÈTRES

| Champ profil utilisateur | Spécification des types de données |
| ---| --- |
| country | (chaîne de caractères) Nous vous demandons de transmettre les indicatifs nationaux à Braze selon la [norme ISO-3166-1 alpha-2][17]. |
| current_location | (objet) De la forme {"longitude" : -73.991443, "latitude" : 40.753824} |
| date_of_first_session | (date à laquelle l’utilisateur s’est servi de l’application pour la première fois) Chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| date_of_last_session | (date à laquelle l’utilisateur s’est servi de l’application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| dob | (date de naissance) Chaîne de caractères au format « AAAA-MM-DD », p. ex. 1980-12-21. |
| email | (chaîne de caractères) |
| email_subscribe | (chaîne de caractères) Les valeurs disponibles sont « confirmé » (explicitement consenti à recevoir des e-mails), « désabonné » (explicitement refusé de recevoir des e-mails), et « abonné » (ni accepté, ni refusé).  |
| external_id | (chaîne de caractères) De l’identifiant utilisateur unique. |
| facebook | hachage contenant l’un des `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères), `num_friends` (entier). |
| first_name | (chaîne de caractères) |
| gender | (chaîne de caractères) « H », « F », « A » (autre), « S/O » (sans objet), « P » (préfère ne pas dire) ou nul (inconnu). |
| home_city | (chaîne de caractères) |
| image_url | (chaîne de caractères) URL de l’image à associer au profil utilisateur. |
| language | (chaîne de caractères) la langue doit être transmise à Braze selon la [norme ISO-639-1][24]. <br>[Liste des langages acceptés][1]|
| last_name | (chaîne de caractères) |
|marked_email_as_spam_at| (chaîne de caractères) Date à laquelle l’e-mail de l’utilisateur a été marqué comme courrier indésirable. La liste est affichée au format ISO 8601 ou au format aaaa-MM-jj'T'HH:mm:ss:SSSZ.|
| phone | (chaîne de caractères) |
| push_subscribe | (chaîne de caractères) Les valeurs disponibles sont « confirmé » (explicitement consenti à recevoir des notifications push), « désabonné » (explicitement refusé de recevoir des notifications push), et « abonné » (ni accepté, ni refusé).  |
| push_tokens | Tableau d’objets avec `app_id` et la chaîne de caractères `token`. Vous pouvez éventuellement fournir un `device_id` pour l’appareil auquel ce jeton est associé, par exemple, `[{"app_id": Identifiant d’application, "token": "abcd", "device_id": "optional_field_value"}]`. If a `device_id` n’a pas été fourni et sera donc généré de manière aléatoire. |
| time_zone | (chaîne de caractères) Nom de fuseau horaire de la [base de données de fuseaux horaires IANA][26] (par ex. « Amérique/New_York » ou « Heure de l’Est (États-Unis et Canada) »). Seules les valeurs de fuseau horaire valides seront définies. |
| twitter | Hachage contenant l’un des `id` (entier), `screen_name` (chaîne de caractères, nom d’utilisateur Twitter), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier). |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
