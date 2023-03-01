---
nav_title: "POST : Suppression de l’utilisateur"
article_title: "POST : Suppression de l’utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer des informations utilisateur."

---
{% api %}
# Endpoint Suppression de l’utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/delete
{% endapimethod %}

Utilisez cet endpoint pour supprimer un profil utilisateur en spécifiant un identifiant utilisateur connu. Vous pouvez inclure jusqu’à 50 `external_ids`, `user_aliases`, ou `braze_ids` dans une seule demande. Seul un des `external_ids`, `user_aliases`, ou `braze_ids` peut être inclus dans une seule demande.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

{% alert warning %}
La suppression des profils utilisateur ne peut pas être annulée. Cette action supprimera définitivement les utilisateurs susceptibles de provoquer des écarts dans vos données. En savoir plus sur ce qui se passe lorsque vous [supprimez un profil utilisateur via l’API]({{site.baseurl}}/help/help_articles/api/delete_user/) dans notre documentation d’aide.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (optional, array of string) External ids for the users to delete,
  "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
  "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
}
```
### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Facultatif | Tableau de chaînes de caractères | Identifiants externes pour les utilisateurs à supprimer. |
| `user_aliases` | Facultatif | Tableau de l’objet Alias utilisateur | [Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) pour les utilisateurs à supprimer. |
| `braze_ids` | Facultatif | Tableau de chaînes de caractères | Identifiants utilisateur de Braze pour les utilisateurs à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}



