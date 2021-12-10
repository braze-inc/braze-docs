---
title: Glossaire API ou Code
navlink: apitest
layout: api_page
page_order: 2
#Required
description: "Ceci est la description de la recherche Google. Les personnages de plus de 160 sont tronqués, concis-le brièvement."
page_type: glossary
#Use if applicable
tool:
  - Tableau de bord
  - Documents
  - Toile
  - Campagnes
  - Segments
  - Modèles
  - Médias
  - Localisation
  - Courants
  - Rapports
platform:
  - iOS
  - Android
  - Web
  - API
channel:
  - Cartes de contenu
  - Courriel
  - Flux d'actualité
  - Messages In-App
  - Pousser
  - SMS
  - Webhooks
noindex: vrai
#ATTENTION: remove noindex and this alert from template
excerpt_separator: ""
---

{% api %}
## 1 Créer un modèle d'e-mail
{% apimethod post %}
/fr/templates/email/create
{% endapimethod %}
{% apitags %}
Post,E-mail,Créer,Template,REST,API
{% endapitags %}

Utilisez les API REST de modèle d'e-mail pour gérer programmatiquement les modèles d'e-mail que vous avez stockés sur les tableaux de bord Braze, sur la page Modèles & Médias. Braze fournit deux terminaux pour la création et la mise à jour de vos modèles de courriel.

La réponse de ce point de terminaison inclut un champ pour `email_template_id`, qui peut être utilisé pour mettre à jour le modèle dans les appels API suivants.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### DEMANDER LE CODE
```
{
  "template_name": "email_template_name",
  "subject": "Bienvenue dans mon modèle d'e-mail! ,
  "body": "This is the text within my email body and https://www. raser. om/ voici un lien vers Braze.com. ,
  "plaintext_body": "Ceci est le texte dans le corps de mon e-mail et ici est un lien vers https://www. raze.com/.",
  "preheader": "Mon préen-tête est assez cool."
}

```

#### RÉPONSE DU SAMPLE
```
{
  "template_name": "email_template_name",
  "subject": "Bienvenue dans mon modèle d'e-mail! ,
  "body": "This is the text within my email body and https://www. raser. om/ voici un lien vers Braze.com. ,
  "plaintext_body": "Ceci est le texte dans le corps de mon e-mail et ici est un lien vers https://www. raze.com/.",
  "preheader": "Mon préen-tête est assez cool."
}
```


#### DÉTAILS DE PARAMETRES

| Paramètre       | Requis | Type de données    | Libellé                                                                                                                     |
| --------------- | ------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `Modifié_après` | Non    | Chaîne en ISO 8601 | Récupérer uniquement les modèles mis à jour à ou après l'heure donnée.                                                      |
| `modifié_avant` | Non    | Chaîne en ISO 8601 | Récupérer uniquement les modèles mis à jour à ou avant l'heure donnée.                                                      |
| `limite`        | Non    | Nombre positif     | Nombre maximum de gabarits à récupérer, par défaut à 100 s'ils ne sont pas fournis, la valeur maximale acceptable est 1000. |
| `décalage`      | Non    | Nombre positif     | Nombre de modèles à ignorer avant de retourner le reste des modèles qui correspondent aux critères de recherche.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


{% endapi %}
{% api %}
## 2 Liste de modèles d'e-mail disponibles
{% apimethod get %}
/fr/templates/email/list
{% endapimethod %}
{% apitags %}
Obtenez,E-mail,Modèle,Liste,REST
{% endapitags %}

Utilisez les points de terminaison ci-dessous pour obtenir une liste de modèles disponibles.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### DEMANDER LE CODE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: nombre de modèles retournés
  “templates”: [template with the following properties]:
    “email_template_id”: (string) your email template API Identifier,
    « template_name » : (chaîne) le nom de votre modèle de courriel,
    « created_at » : (chaîne, dans ISO 8601),
    « updated_at » : (chaîne de caractères dans ISO 8601)
}

```

#### RÉPONSE DU SAMPLE
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  “count”: nombre de modèles retournés
  “templates”: [template with the following properties]:
    “email_template_id”: (string) your email template API Identifier,
    « template_name » : (chaîne) le nom de votre modèle de courriel,
    « created_at » : (chaîne, dans ISO 8601),
    « updated_at » : (chaîne de caractères dans ISO 8601)
}
```


#### DÉTAILS DE PARAMETRES

| Paramètre                | Requis | Type de données      | Libellé                                      |
| ------------------------ | ------ | -------------------- | -------------------------------------------- |
| `Identifiant de l'email` | Oui    | Chaîne de caractères | Identifiant API de votre modèle de courriel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 3 Campagnes Déclencher Envoi
{% apimethod post %}campagnes/déclencheur/envoyer{% endapimethod %}
{% apitags %}Post, Campagnes, Déclenchement,Envoyer{% endapitags %}

La distribution déclenchée par l'API vous permet d'héberger le contenu des messages dans le tableau de bord de Braze, en dictant quand un message est envoyé, et à qui via votre API.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### DEMANDER LE CODE
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (requis, chaîne) voir Identifiant de campagne,
  "send_id": (optionnel, chaîne) voir Send Identifier,
  "trigger_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à tous les utilisateurs de cette requête,
  "broadcast": (optionnel, booléen) voir Broadcast -- false par défaut le 8/31/17, doit être défini à true si "destinataires" est omis,
  "audience": (optionnel, Objet public connecté) voir Audience connectée,
  // Inclure 'audience' enverra uniquement aux utilisateurs dans l'auditoire
  "destinataires": (optionnel, tableau; si non fourni et diffusé n'est pas défini à 'false', sera envoyé à tout le segment ciblé par la campagne) [
    {
      // "external_user_id" ou "user_alias" est requis. Les requêtes ne doivent spécifier qu'une seule fois.
      "user_alias": (optionnel, objet d'alias utilisateur) Alias de l'utilisateur pour recevoir le message,
      "external_user_id": (optionnel, string) Id externe de l'utilisateur à recevoir le message,
      "trigger_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à cet utilisateur (ces paires clé-valeur remplaceront toutes les clés qui entrent en conflit avec trigger_properties ci-dessus)
    },
...
  ]
}

```

#### RÉPONSE DU SAMPLE
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (requis, string) voir Canvas Identifier,
  "canvas_entry_properties": (optionnel, objet) paires clé-valeur de personnalisation qui s'appliqueront à tous les utilisateurs dans cette requête,
  "broadcast": (optionnel, booléen) voir Broadcast -- false par défaut le 8/31/17, doit être défini à true si "destinataires" est omis,
  "audience": (optionnel, Objet public connecté) voir Audience connectée,
  // Inclure 'audience' enverra uniquement aux utilisateurs dans l'auditoire
  "destinataires": (optionnel, tableau; si non fourni et diffusé n'est pas défini à 'false', sera envoyé à tout le segment ciblé par le Canvas) [
    {
      // "external_user_id" ou "user_alias" est requis. Les requêtes ne doivent spécifier qu'une seule fois.
      "user_alias": (optionnel, objet d'alias utilisateur) Alias de l'utilisateur pour recevoir le message,
      "external_user_id": (optionnel, string) Id externe de l'utilisateur à recevoir le message,
      "canvas_entry_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à cet utilisateur (ces paires clé-valeur remplaceront toutes les clés qui entrent en conflit avec canvas_entry_properties ci-dessus)
    },
...
  ]
}
```


#### DÉTAILS DE PARAMETRES

| Paramètre                | Requis | Type de données      | Libellé                                      |
| ------------------------ | ------ | -------------------- | -------------------------------------------- |
| `Identifiant de l'email` | Oui    | Chaîne de caractères | Identifiant API de votre modèle de courriel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% endapi %}


{% api %}
## 4 Campagnes Déclencher Envoi
{% apimethod put %}utilisateurs/piste{% endapimethod %}
{% apitags %}PUT, Campagnes, Déclenchement, Envoyer{% endapitags %}

Ce point de terminaison peut être utilisé pour enregistrer des événements personnalisés, des attributs utilisateur et des achats pour les utilisateurs. Vous pouvez inclure jusqu'à 75 Attributs, Événement, et Achat d'objets par demande. C'est-à-dire que vous pouvez publier des attributs pour jusqu'à 75 utilisateurs à la fois, mais dans le même appel API, vous pouvez également fournir jusqu'à 75 événements et jusqu'à 75 achats.

{% apiref swagger %}https://www.braze.com/docs/api/interactive/ {% endapiref %}
{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### DEMANDER LE CODE
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (facultatif, tableau de l'objet Attributes),
   "événements" : (optionnel, tableau d'objet événement),
   "achats" : (optionnel, tableau d'objet d'achat)
}

```

#### RÉPONSE DU SAMPLE
```
{
  // Un de "external_id" ou "user_alias" ou "braze_id" est requis
  "external_id" : (optionnel, string) voir ID utilisateur externe ci-dessous,
  "user_alias" : (optionnel, Objet User Alias),
  "braze_id" : (optionnel, chaîne) Braze User Identifier,
  // Mettre ce drapeau à true mettra l'API en mode "Mise à jour uniquement".
  // Lorsque vous utilisez un "user_alias", le mode "Update only" est toujours vrai.
  "_update_existing_only" : (optionnel, booléen),
  // Voir la note ci-dessous concernant les importations de jetons de poussage anonymes
  "push_token_import" : (optionnel, booléen).
  // Braze champs de profil utilisateur
  "prénom" : "Jon",
  "email" : "bob@example. om",
  // Attributs personnalisés
  "mon_custom_attribute" : valeur,
  "mon_custom_attribute_2" : {"inc" : int_value},
  "mon_array_custom_attribute":[ "Valeur1", "Valeur2" ],
  // Ajout d'une nouvelle valeur à un attribut personnalisé tableau
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Suppression d'une valeur d'un attribut personnalisé tableau
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### DÉTAILS DE PARAMETRES

| Champ de profil utilisateur | Spécification du type de données                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pays                        | (string) Nous exigeons que les codes pays soient passés à Braze dans le \[norme ISO-3166-1 alpha-2\]\[17\].                                                                                                                                                                                                               |
| emplacement actuel          | (objet) De la forme {"longitude": -73.991443, "latitude": 40.753824}                                                                                                                                                                                                                                                      |
| Date de la première session | (date à laquelle l'utilisateur a utilisé l'application pour la première fois) Chaîne au format ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`.                                                                                                                                                                        |
| Date de la dernière session | (date à laquelle l'utilisateur a utilisé la dernière fois l'application) Chaîne au format ISO 8601 ou au format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`.                                                                                                                                                                             |
| chien                       | (date de naissance) Chaîne au format "AAAA-MM-JJ", par exemple 1980-12-21.                                                                                                                                                                                                                                                |
| Email                       | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Inscription par e-mail      | (string) Les valeurs disponibles sont "opted_in" (explicitement enregistrées pour recevoir des messages électroniques), "unsubscribed" (explicitement opted out of email messages) et "subscribed" (ni opted in ni out).                                                                                                  |
| id externe                  | (chaîne) De l'identifiant unique de l'utilisateur.                                                                                                                                                                                                                                                                        |
| facebook                    | hash contenant un de `id` (chaîne), `likes` (tableau de chaînes), `num_friends` (entier).                                                                                                                                                                                                                                 |
| prénom                      | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Sexe                        | (chaîne) "M", "F", "O" (autre), "N" (non applicable), "P" (préfère ne pas dire) ou "nil (inconnu).                                                                                                                                                                                                                        |
| ville_domicile              | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| url de l'image              | (chaîne) URL de l'image à associer au profil de l'utilisateur.                                                                                                                                                                                                                                                            |
| Langue                      | (chaîne) nous avons besoin que le langage soit passé à Braze dans le [norme ISO-639-1[24]. <br>[Liste des langues acceptées][1]                                                                                                                                                                                     |
| nom_de famille              | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Marqué comme spam à         | (chaîne) Date à laquelle l'email de l'utilisateur a été marqué comme spam. Apparaît au format ISO 8601 ou au format yyyy-MM-dd'T'H:mm:ss:SSSZ.                                                                                                                                                                            |
| Téléphone                   | (chaîne)                                                                                                                                                                                                                                                                                                                  |
| Poussez vous abonner        | (string) Les valeurs disponibles sont "opted_in" (explicitement enregistrées pour recevoir des messages push), "unsubscribed" (explicitement opted out of push messages), et "subscribed" (ni opted in ni out).                                                                                                           |
| Pousse_tokens               | Tableau d'objets avec la chaîne `app_id` et `token`. Vous pouvez éventuellement fournir un `device_id` pour l'appareil auquel ce jeton est associé. ., `[{"app_id": Identifiant d'application, "token": "abcd", "device_id": "optional_field_value"}]`. Si un `device_id` n'est pas fourni, on sera généré aléatoirement. |
| fuseau horaire              | (string) Of time zone name from \[IANA Time Zone Database][26\] (e.g., "America/New_York" or "Eastern Time (US & Canada)"). Seules les valeurs de fuseau horaire valides seront définies.                                                                                                                                 |
| twitter                     | Hash contenant l'un des `id` (entier), `nom_écran` (chaîne, gestionnaire Twitter), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier).                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
