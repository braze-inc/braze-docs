---
nav_title: "POST : Mettre à jour l’alias d’utilisateur"
article_title: "POST : Mise à jour de l'alias d'utilisateur"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour les alias utilisateur."
---
{% api %}
# Mettre à jour l’alias d’utilisateur
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour les alias utilisateur existants.

Vous pouvez spécifier jusqu’à 50 alias de l’utilisateur par requête.

Mettre à jour d’un alias d’utilisateur nécessite que `alias_label`, `old_alias_name` et `new_alias_name` soient compris dans l’objet de mise à jour d’alias d’utilisateur. Si aucun alias d’utilisateur n’est associé au `alias_label` ni au `old_alias_name`, aucun alias ne sera mis à jour. Si le `alias_label` et le `old_alias_name` sont trouvés, le `old_alias_name` sera mis à jour vers le `new_alias_name`.

{% alert note %}
Cet endpoint ne garantit pas que la séquence des objets `alias_updates` soit mise à jour.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.alias.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Requis | Tableau des objets alias utilisateur mis à jour | Voir l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Pour plus d'informations sur `old_alias_name`, `new_alias_name`, et `alias_label`, reportez-vous à la section [Alias de l'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Corps de demande d’endpoint avec spécification de l’objet de mise à jour d’alias utilisateur

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}

