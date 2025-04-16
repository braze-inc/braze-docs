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

> Verwenden Sie diesen Endpunkt, um die alten, veralteten externen IDs Ihrer Nutzer:innen zu entfernen. 

Sie können bis zu 50 externe IDs pro Anfrage senden. 

{% alert warning %}
Dieser Endpunkt löscht die veraltete ID vollständig und kann nicht rückgängig gemacht werden. Wenn Sie diesen Endpunkt verwenden, um veraltete `external_ids` zu entfernen, die noch mit Nutzern:innen in Ihrem System verbunden sind, können Sie die Daten dieser Nutzer:innen nicht mehr finden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.external_ids.remove`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Erforderlich | String-Array | Externe Bezeichner für die Nutzer:innen zum Entfernen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel für eine Anfrage

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

Die Antwort bestätigt alle erfolgreichen Entfernungen sowie erfolglose Entfernungen mit den dazugehörigen Fehlern. Fehlermeldungen im Feld `removal_errors` referenzieren den Index im Array der ursprünglichen Anfrage.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

Das Feld `message` gibt für jede gültige Anfrage `success` zurück. Spezifischere Fehler werden im Array `removal_errors` festgehalten. Das Feld `message` gibt einen Fehler zurück, wenn der Fall eintritt:
- Ungültiger API-Schlüssel
- Leeres `external_ids` Array
- `external_ids` Array mit mehr als 50 Artikeln
- Erreichen des Rate-Limits (mehr als 1.000 Anfragen/Minute)

{% endapi %}
