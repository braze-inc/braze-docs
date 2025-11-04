---
nav_title: "POST: Neuen Nutzer-Alias erstellen"
article_title: "POST: Neuen Nutzer-Alias erstellen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Neue Nutzer:in erstellen Braze."

---
{% api %}
# Neuen Nutzer:in-Alias erstellen
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um neue User-Alias für bestehende identifizierte Nutzer:innen hinzuzufügen oder um neue nicht identifizierte Nutzer:innen zu erstellen.

Pro Anfrage können bis zu 50 Nutzer:innen angegeben werden.

**Um einen Nutzer-Alias für einen bestehenden Nutzer:in hinzuzufügen**, muss ein `external_id` in das neue Nutzer-Alias-Objekt aufgenommen werden. Wenn der `external_id` im Objekt vorhanden ist, es aber keinen Nutzer mit diesem `external_id` gibt, wird der Alias keinem Nutzer:innen hinzugefügt. Wenn `external_id` nicht vorhanden ist, wird ein Nutzer:innen trotzdem angelegt, muss aber später identifiziert werden. Dazu verwenden Sie den Endpunkt "Nutzer:innen identifizieren" und den Endpunkt `users/identify`.

Bei **der Erstellung eines neuen Nutzers:innen, der nur über einen Alias verfügt**, muss die `external_id` im neuen Nutzer-Alias-Objekt weggelassen werden. Nachdem der Nutzer erstellt wurde, verwenden Sie den Endpunkt `/users/track`, um den Nutzer:innen mit Attributen, Ereignissen und Käufen zu verknüpfen, und den Endpunkt `/users/identify`, um den Nutzer mit einem `external_id` zu identifizieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.alias.new`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Erforderlich | Array mit neuen Nutzer:in-Alias-Objekten | Siehe [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu [User-Aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Körper der Anfrage des Endpunkts mit Angabe des neuen Nutzer:in-Objekts für den Nutzer-Alias

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
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

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}

