---
nav_title: "POST: Nutzer:in aktualisieren"
article_title: "POST: Nutzer:in aktualisieren"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Update Nutzer:innen Braze."
---
{% api %}
# Nutzer:in aktualisieren
{% apimethod post %}
/benutzer/alias/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um bestehende Nutzer:innen-Aliase zu aktualisieren.

Pro Anfrage können bis zu 50 Nutzer:innen angegeben werden.

Um einen Nutzer-Alias zu aktualisieren, müssen `alias_label`, `old_alias_name` und `new_alias_name` in das Objekt Nutzer-Alias aktualisieren aufgenommen werden. Wenn es keinen Nutzer-Alias gibt, der mit `alias_label` und `old_alias_name` verknüpft ist, wird kein Alias aktualisiert. Wenn die angegebenen `alias_label` und `old_alias_name` gefunden werden, dann wird `old_alias_name` auf `new_alias_name` aktualisiert.

{% alert note %}
Dieser Endpunkt garantiert nicht die Reihenfolge, in der die `alias_updates` Objekte aktualisiert werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.alias.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Erforderlich | Array von Update Nutzer:in-Alias-Objekten | Siehe [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Weitere Informationen zu `old_alias_name`, `new_alias_name` und `alias_label` finden Sie unter [Nutzer:innen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Körper der Anfrage des Endpunkts mit der Spezifikation des Objekts Nutzer:in aktualisieren

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Beispiel Anfrage
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

