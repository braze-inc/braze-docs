---
nav_title: "POST: Benutzer-Alias aktualisieren"
article_title: "POST: Benutzer-Alias aktualisieren"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt Benutzer-Aliase aktualisieren."
---
{% api %}
# Benutzer-Alias aktualisieren
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um bestehende Benutzer-Aliase zu aktualisieren.

Pro Anfrage können bis zu 50 Benutzer-Aliase angegeben werden.

Für die Aktualisierung eines Benutzer-Alias müssen `alias_label`, `old_alias_name` und `new_alias_name` in das Objekt update user alias aufgenommen werden. Wenn kein Benutzer-Alias mit `alias_label` und `old_alias_name` verknüpft ist, wird kein Alias aktualisiert. Wenn die angegebenen `alias_label` und `old_alias_name` gefunden werden, dann wird `old_alias_name` auf `new_alias_name` aktualisiert.

{% alert note %}
Dieser Endpunkt garantiert nicht die Reihenfolge, in der die `alias_updates` Objekte aktualisiert werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.alias.update`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Erforderlich | Array von Update-Benutzer-Alias-Objekten | Siehe [Benutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Weitere Informationen zu `old_alias_name`, `new_alias_name` und `alias_label` finden Sie unter [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Endpunkt-Anfragekörper mit Angabe des Objekts Benutzer-Alias aktualisieren

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

