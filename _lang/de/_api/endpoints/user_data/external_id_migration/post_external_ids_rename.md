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

> Verwenden Sie diesen Endpunkt, um die externen IDs Ihrer Benutzer umzubenennen. 

Sie können bis zu 50 Umbenennungsobjekte pro Anfrage senden. 

Dieser Endpunkt legt eine neue (primäre) `external_id` für den Benutzer fest und verwirft seine bestehende `external_id`. Das bedeutet, dass der Benutzer über einen der beiden `external_id` identifiziert werden kann, bis die veraltete Version entfernt wird. Mehrere externe IDs ermöglichen eine Migrationsphase, so dass ältere Versionen Ihrer Anwendungen, die das vorherige Namensschema für externe IDs verwenden, nicht beschädigt werden. 

Nachdem Ihr altes Benennungsschema nicht mehr verwendet wird, empfehlen wir Ihnen dringend, veraltete externe IDs mit dem [Endpunkt`/users/external_ids/remove` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) zu entfernen.

{% alert warning %}
Stellen Sie sicher, dass Sie veraltete externe IDs mit dem Endpunkt `/users/external_ids/remove` anstelle von `/users/delete` entfernen. Wenn Sie eine Anfrage an `/users/delete` mit der veralteten externen ID senden, wird das Benutzerprofil vollständig gelöscht und kann nicht rückgängig gemacht werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.external_ids.rename`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Erforderlich | Array mit Objekten zur Umbenennung externer Bezeichner | Sehen Sie sich das Anfragebeispiel und die folgenden Einschränkungen für die Struktur des Objekts Externer Bezeichner umbenennen an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie das Folgende:

- Die `current_external_id` muss die primäre ID des Benutzers sein und darf keine veraltete ID sein.
- Die `new_external_id` darf nicht bereits als primäre ID oder veraltete ID verwendet werden.
- Die `current_external_id` und `new_external_id` können nicht dasselbe sein.

## Beispiel anfordern
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

In der Antwort werden alle erfolgreichen Umbenennungen sowie die nicht erfolgreichen Umbenennungen mit den dazugehörigen Fehlern bestätigt. Fehlermeldungen im Feld `rename_errors` verweisen auf den Index des Objekts im Array der ursprünglichen Anfrage.

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
- Ratenlimit erreicht (mehr als 1.000 Anfragen pro Minute)

## Häufig gestellte Fragen

### Hat dies Auswirkungen auf die MAU?
Nein, da die Anzahl der Nutzer gleich bleibt, wird es nur eine neue `external_id` geben.

### Hat sich das Benutzerverhalten im Laufe der Zeit verändert?
Nein, denn der Benutzer ist immer noch derselbe, und sein gesamtes historisches Verhalten ist immer noch mit ihm verbunden.

### Kann es auf Entwicklungs- oder Staging-Workspaces ausgeführt werden?
Ja. Wir empfehlen Ihnen, die Migration in einem Staging- oder Entwicklungsarbeitsbereich zu testen und sicherzustellen, dass alles reibungslos funktioniert, bevor Sie die Migration mit Produktionsdaten durchführen.

### Werden dadurch Datenpunkte verbraucht?
Diese Funktion kostet keine Datenpunkte.

### Welcher Zeitraum wird für die Abschreibung empfohlen?
Es gibt keine feste Grenze dafür, wie lange Sie veraltete externe IDs beibehalten können, aber wir empfehlen dringend, sie zu entfernen, wenn keine Notwendigkeit mehr besteht, Benutzer über die veraltete ID zu referenzieren.

{% endapi %}
