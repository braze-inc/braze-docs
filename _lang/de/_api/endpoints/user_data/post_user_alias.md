---
nav_title: "POST: Neuen Benutzer-Alias erstellen"
article_title: "POST: Neuen Benutzer-Alias erstellen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt Neuen Benutzer-Alias erstellen."

---
{% api %}
# Neuen Benutzer-Alias erstellen
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um neue Benutzer-Aliase für bestehende identifizierte Benutzer hinzuzufügen oder um neue nicht identifizierte Benutzer zu erstellen.

Pro Anfrage können bis zu 50 Benutzer-Aliase angegeben werden.

**Um einen Benutzer-Alias für einen bestehenden Benutzer hinzuzufügen**, muss ein `external_id` in das neue Benutzer-Alias-Objekt aufgenommen werden. Wenn der `external_id` im Objekt vorhanden ist, es aber keinen Benutzer mit diesem `external_id` gibt, wird der Alias keinem Benutzer hinzugefügt. Wenn ein `external_id` nicht vorhanden ist, wird ein Benutzer trotzdem erstellt, muss aber später identifiziert werden. Sie können dies über den Endpunkt "Benutzer identifizieren" und den `users/identify` tun.

**Wenn Sie einen neuen, reinen Alias-Benutzer anlegen**, müssen Sie die `external_id` im neuen Alias-Objekt des Benutzers weglassen. Nachdem der Benutzer erstellt wurde, verwenden Sie den Endpunkt `/users/track`, um den Nur-Alias-Benutzer mit Attributen, Ereignissen und Käufen zu verknüpfen, und den Endpunkt `/users/identify`, um den Benutzer mit einem `external_id` zu identifizieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.alias.new`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Erforderlich | Array mit neuen Benutzer-Alias-Objekten | Siehe [Benutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Weitere Informationen über `alias_name` und `alias_label` finden Sie in unserer Dokumentation über [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Endpunkt-Anfragekörper mit Angabe des neuen Benutzer-Aliasobjekts

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

