---
nav_title: "POST : Supprimer les utilisateurs"
article_title: "POST : Supprimer des utilisateurs"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article décrit les détails de l'endpoint Braze pour supprimer des utilisateurs."

---
{% api %}
# Supprimer les utilisateurs
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> Utilisez cet endpoint pour supprimer un profil utilisateur en spécifiant un identifiant utilisateur connu.

Jusqu'à 50 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, ou `phone_numbers` peuvent être inclus dans une seule demande. Une seule des adresses `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, ou `phone_numbers` peut être incluse dans une seule demande. 

Si vous avez un cas d'utilisation qui ne peut pas être résolu avec la suppression en bloc d'utilisateurs via l'API, contactez l' [équipe d'assistance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) pour obtenir de l'aide.

{% alert warning %}
La suppression des profils utilisateur ne peut pas être annulée. Cette action supprimera définitivement les utilisateurs susceptibles de provoquer des écarts dans vos données. Pour en savoir plus sur ce qui se passe lorsque vous [supprimez un profil utilisateur à l'aide de l'API,]({{site.baseurl}}/help/help_articles/api/delete_user/) consultez notre documentation d'aide.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.delete`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### Paramètres de demande

| Paramètre         | Requis | Type de données                  | Description                                                                                      |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids`    | Facultatif | Tableau de chaînes de caractères           | Identifiants externes à supprimer.                                                    |
| `user_aliases`    | Facultatif | Tableau d’objets Alias utilisateur | [Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) à supprimer. |
| `braze_ids`       | Facultatif | Tableau de chaînes de caractères           | Suppression des identifiants des utilisateurs de Braze.                                                  |
| `email_addresses` | Facultatif | Tableau de chaînes de caractères           | Les e-mails des utilisateurs à supprimer. Pour plus d'informations, reportez-vous à la section [Suppression d'utilisateurs par e-mail](#deleting-users-by-email).                                                             |
| `phone_numbers` | Facultatif | Tableau de chaînes de caractères | Numéros de téléphone de l'utilisateur à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Suppression d'utilisateurs par adresses e-mail et numéros de téléphone

Si une adresse e-mail ou un numéro de téléphone est spécifié comme identifiant, une valeur supplémentaire `prioritization` est requise dans l'identifiant. `prioritization` doit être un tableau ordonné et doit spécifier quel utilisateur doit être supprimé s'il y a plusieurs utilisateurs. Cela signifie que la suppression des utilisateurs ne se produira pas si plus d'un utilisateur correspond à une priorisation.

Les valeurs autorisées pour le tableau sont les suivantes :

- `identified`
- `unidentified`
- `most_recently_updated` (Priorité à l'utilisateur le plus récemment mis à jour)

Une seule des options suivantes peut exister à la fois dans le tableau `prioritization`:

- `identified` Il s'agit de donner la priorité à un utilisateur ayant une `external_id`
- `unidentified` Il s'agit de donner la priorité à un utilisateur qui n'a pas de `external_id`

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
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
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```
{% endapi %}


