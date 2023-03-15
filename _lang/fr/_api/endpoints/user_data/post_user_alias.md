---
nav_title: "POST : créer un nouvel alias utilisateur"
article_title: "POST : créer un nouvel alias utilisateur"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer de nouveaux alias utilisateur."

---
{% api %}
# Créer un nouvel alias utilisateur
{% apimethod post %}
/users/alias/new
{% endapimethod %}

Utilisez cet endpoint pour ajouter de nouveaux alias utilisateur pour les utilisateurs identifiés existants, ou pour créer de nouveaux utilisateurs non identifiés.

{% alert note %}
Vous pouvez ajouter jusqu’à 50 alias d’utilisateurs par demande.
{% endalert %}

**Ajouter un alias utilisateur pour un utilisateur existant** nécessite un `external_id` à inclure dans le nouvel objet Alias d’utilisateur. Si un `external_id` indiqué dans l’objet ne correspond pas à un utilisateur `external_id`, l’alias ne sera ajouté à aucun utilisateur. Faute d’un `external_id`, un utilisateur sera créé quand même, mais il devra être identifié ultérieurement. Vous pouvez le faire en utilisant l’« identification des utilisateurs » et l’endpoint `users/identify`.

**Créer un nouvel utilisateur alias uniquement** nécessite que l’`external_id` soit omis du nouvel objet Alias d’utilisateur. Une fois l’utilisateur créé, utilisez l’endpoint `/users/track` pour associer l’utilisateur alias uniquement aux attributs, événements et achats, et l’endpoint `/users/identify` pour identifier l’utilisateur avec un `external_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Requis | Objets Tableau des nouveaux alias utilisateur | Voir [Objet Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Pour plus d’informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Corps de demande d’endpoint avec spécification de l’objet Nouvel alias utilisateur

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

