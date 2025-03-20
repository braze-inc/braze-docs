---
nav_title: "POST: Externe ID entfernen"
article_title: "POST: Externe ID entfernen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Externe IDs entfernen."

---
{% api %}
# Externe ID entfernen
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die alten, veralteten externen IDs Ihrer Benutzer zu entfernen. 

Sie können bis zu 50 externe IDs pro Anfrage senden. 

{% alert warning %}
Dieser Endpunkt entfernt die veraltete ID vollständig und kann nicht rückgängig gemacht werden. Wenn Sie diesen Endpunkt verwenden, um veraltete `external_ids` zu entfernen, die noch mit Benutzern in Ihrem System verknüpft sind, können Sie dauerhaft verhindern, dass Sie die Daten dieser Benutzer finden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.external_ids.remove`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Erforderlich | Array von Zeichenketten | Externe Identifikatoren für die Benutzer zum Entfernen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel anfordern

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
Nur veraltete IDs können entfernt werden. Der Versuch, eine primäre externe ID zu entfernen, führt zu einem Fehler.
{% endalert %}

## Antwort

Die Antwort bestätigt alle erfolgreichen Umzüge sowie die nicht erfolgreichen Umzüge mit den dazugehörigen Fehlern. Fehlermeldungen im Feld `removal_errors` verweisen auf den Index im Array der ursprünglichen Anfrage.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

Das Feld `message` gibt `success` für jede gültige Anfrage zurück. Spezifischere Fehler werden im Array `removal_errors` festgehalten. Das Feld `message` gibt einen Fehler zurück, wenn der Fall eintritt:
- Ungültiger API-Schlüssel
- Leeres `external_ids` Array
- `external_ids` Array mit mehr als 50 Elementen
- Ratenlimit erreicht (mehr als 1.000 Anfragen/Minute)

{% endapi %}
