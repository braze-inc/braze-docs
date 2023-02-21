---
nav_title: "POST : Mettre à jour l’alias d’utilisateur"
article_title: "POST : Mettre à jour l’alias d’utilisateur"
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

Utilisez cet endpoint pour mettre à jour les alias utilisateur existants.

{% alert note %}
Vous pouvez mettre à jour jusqu’à 50 alias d’utilisateurs par demande.
{% endalert %}

Mettre à jour d’un alias d’utilisateur nécessite que `alias_label`, `old_alias_name` et `new_alias_name` soient compris dans l’objet de mise à jour d’alias d’utilisateur. Si aucun alias d’utilisateur n’est associé au `alias_label` ni au `old_alias_name`, aucun alias ne sera mis à jour. Si le `alias_label` et le `old_alias_name` sont trouvés, le `old_alias_name` sera mis à jour vers le `new_alias_name`.

{% alert note %}
Cet endpoint ne garantit pas que la séquence des objets `alias_updates` soit mise à jour.
{% endalert %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "alias_updates" : (obligatoire, tableau d’objets de mise à jour d’alias d'utilisateur)
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Requis | Tableau des objets alias utilisateur mis à jour | Voir [Objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Pour plus d’informations sur `old_alias_name`, `new_alias_name` et `alias_label`, reportez-vous aux [alias d’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
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

