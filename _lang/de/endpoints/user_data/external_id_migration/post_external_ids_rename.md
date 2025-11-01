---
nav_title: "POST: Externe ID umbenennen"
article_title: "POST: Externe ID umbenennen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt Externe IDs umbenennen."

---
{% api %}
# Externe ID umbenennen
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die externen IDs Ihrer Nutzer:innen umzubenennen. 

Sie können bis zu 50 Umbenennungsobjekte pro Anfrage senden. 

Dieser Endpunkt legt eine neue (primäre) `external_id` für den Nutzer:innen fest und veraltet seine bestehende `external_id`. Das bedeutet, dass der Nutzer:innen durch einen der beiden `external_id` identifiziert werden kann, bis der veraltete Bezeichner entfernt wird. Mehrere externe IDs sind für eine Migration zulässig, so dass ältere Versionen Ihrer Apps, die das vorherige Namensschema für externe IDs verwenden, nicht beschädigt werden. 

Nachdem Ihr altes Namensschema nicht mehr verwendet wird, empfehlen wir dringend, veraltete externe IDs über den [Endpunkt `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) zu entfernen.

{% alert warning %}
Stellen Sie sicher, dass Sie veraltete externe IDs mit dem Endpunkt `/users/external_ids/remove` anstelle von `/users/delete` entfernen. Wenn Sie eine Anfrage an `/users/delete` mit der veralteten externen ID senden, wird das Nutzerprofil vollständig gelöscht und kann nicht rückgängig gemacht werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.external_ids.rename`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Erforderlich | Array mit externen Bezeichnern Objekte umbenennen | Sehen Sie sich das Beispiel der Anfrage und die folgenden Einschränkungen für die Struktur des Objekts "Externer Bezeichner umbenennen" an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie das Folgende:

- Die `current_external_id` muss die primäre ID des Nutzers:innen sein und darf keine veraltete ID sein.
- Die `new_external_id` darf nicht bereits als primäre ID oder als veraltete ID verwendet werden.
- Die `current_external_id` und `new_external_id` können nicht dasselbe sein.

## Beispiel für eine Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Antwort

Die Antwort bestätigt alle erfolgreichen Umbenennungen sowie erfolglose Umbenennungen mit den entsprechenden Fehlern. Fehlermeldungen im Feld `rename_errors` referenzieren den Index des Objekts im Array der ursprünglichen Anfrage.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

Das Feld `message` gibt `success` für jede gültige Anfrage zurück. Spezifischere Fehler werden im Array `rename_errors` festgehalten. Das Feld `message` gibt einen Fehler zurück, wenn der Fall eintritt:

- Ungültiger API-Schlüssel
- Leeres `external_id_renames` Array
- `external_id_renames` Array mit mehr als 50 Objekten
- Erreichen des Rate-Limits (mehr als 1.000 Anfragen pro Minute)

## Häufig gestellte Fragen

### Hat dies Auswirkungen auf MAU?
Nein, da die Anzahl der Nutzer:innen gleich bleibt, werden sie einfach eine neue `external_id` haben.

### Hat sich das Verhalten der Nutzer:innen im Laufe der Zeit verändert?
Nein, denn die Nutzer:innen sind immer noch dieselben, und ihr gesamtes historisches Verhalten ist immer noch mit ihnen verbunden.

### Kann es in Entwickler:in oder Staging Workspaces ausgeführt werden?
Ja Wir empfehlen dringend, die Migration in einem Staging- oder Entwicklungs-Workspace zu testen und sicherzustellen, dass alles reibungslos funktioniert, bevor Sie die Migration mit den Produktionsdaten durchführen.

### Werden damit Datenpunkte aufgezeichnet?
Mit diesem Feature werden keine Datenpunkte protokolliert.

### Welcher Zeitraum wird für die Abschreibung empfohlen?
Es gibt keine feste Grenze, wie lange Sie veraltete externe IDs beibehalten können, aber wir empfehlen dringend, sie zu entfernen, wenn es nicht mehr notwendig ist, Nutzer:innen mit der veralteten ID zu referenzieren.

{% endapi %}
