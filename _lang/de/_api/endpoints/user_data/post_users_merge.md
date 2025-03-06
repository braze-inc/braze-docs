---
nav_title: "POST: Benutzer zusammenführen"
article_title: "POST: Benutzer zusammenführen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt für Merge-Benutzer."

---
{% api %}
# Benutzer zusammenführen
{% apimethod post %}
/users/merge
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Benutzer mit einem anderen Benutzer zusammenzuführen. 

Pro Anfrage können bis zu 50 Zusammenführungen angegeben werden. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.merge`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `merge_updates` | Erforderlich | Array | Ein Objekt-Array. Jedes Objekt sollte ein `identifier_to_merge` Objekt und ein `identifier_to_keep` Objekt enthalten, die jeweils einen Benutzer entweder durch `external_id`, `user_alias`, `phone` oder `email` referenzieren sollten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Verhalten beim Zusammenführen

Das unten beschriebene Verhalten gilt für alle Braze-Funktionen, die *nicht* von Snowflake unterstützt werden. Benutzerzusammenführungen werden für die Registerkarte **Nachrichtenverlauf**, Segmenterweiterungen, Query Builder und Aktuelles nicht berücksichtigt.

{% alert important %}
Der Endpunkt garantiert nicht die Reihenfolge der `merge_updates` Objekte, die aktualisiert werden.
{% endalert %}

Dieser Endpunkt fügt die folgenden Felder zusammen, wenn sie beim Zielbenutzer nicht gefunden werden.

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Rufnummer
- Zeitzone
- Heimatstadt
- Land
- Sprache
- Informationen zum Gerät
- Anzahl der Sitzungen (die Summe der Sitzungen aus beiden Profilen)
- Datum der ersten Sitzung (Braze wählt das frühere Datum der beiden Termine)
- Datum der letzten Sitzung (Braze wählt das spätere Datum der beiden Termine)
- Benutzerdefinierte Attribute (bestehende benutzerdefinierte Attribute im Zielprofil werden beibehalten und umfassen auch benutzerdefinierte Attribute, die im Zielprofil nicht vorhanden waren)
- Benutzerdefinierte Ereignis- und Kaufereignisdaten
- Benutzerdefinierte Ereignis- und Kaufereigniseigenschaften für die Segmentierung "X Mal in Y Tagen" (wobei X<=50 und Y<=30)
- Segmentierbare Zusammenfassung benutzerdefinierter Ereignisse
  - Ereignisanzahl (die Summe aus beiden Profilen)
  - Das Ereignis trat zuerst ein (Braze wählt das frühere der beiden Daten)
  - Letztes Ereignis (Braze wählt das spätere Datum der beiden Daten)
- In-App-Käufe insgesamt in Cent (die Summe aus beiden Profilen)
- Gesamtzahl der Käufe (die Summe aus beiden Profilen)
- Datum des ersten Kaufs (Braze wählt das frühere Datum der beiden Daten)
- Datum des letzten Kaufs (Braze wählt das spätere Datum der beiden Daten)
- App-Zusammenfassungen
- Last_X_at Felder (Braze aktualisiert die Felder, wenn die verwaisten Profilfelder neueren Datums sind)
- Daten zur Kampagneninteraktion (Braze wählt die aktuellsten Datumsfelder aus)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Verlauf der Nachrichten und des Nachrichteninteresses
- Sitzungsdaten werden nur zusammengeführt, wenn die App in beiden Benutzerprofilen vorhanden ist.

{% alert note %}
Beim Zusammenführen von Benutzern funktioniert die Verwendung des Endpunkts `/users/merge` genauso wie die [Methode`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Benutzerdefiniertes Verhalten bei Ereignisdatum und Kaufereignisdatum

Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Für Kaufereignisse umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".

### Zusammenführen von Benutzern nach E-Mail oder Telefonnummer

Wenn ein `email` oder `phone` als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization` Wert im Bezeichner erforderlich. `prioritization` sollte ein Array sein, das angibt, welcher Benutzer zusammengeführt werden soll, wenn mehrere Benutzer gefunden werden. `prioritization` ist ein geordnetes Array, d.h. wenn mehr als ein Benutzer aus einer Priorisierung übereinstimmt, wird die Zusammenführung nicht durchgeführt.

Die zulässigen Werte für das Array sind: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` bezieht sich auf die Priorisierung des zuletzt aktualisierten Benutzers.

Es kann jeweils nur eine der folgenden Optionen im Prioritätsfeld vorhanden sein:
- `identified` bezieht sich auf die Priorisierung eines Benutzers mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Benutzers ohne `external_id`

## Beispiel Anfragen

### Grundlegende Anfrage

Dies ist ein einfacher Anfragekörper, der das Muster der Anfrage zeigt.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Nicht identifizierten Benutzer zusammenführen

Die folgende Anfrage würde den zuletzt aktualisierten nicht identifizierten Benutzer mit der E-Mail-Adresse "john.smith@braze.com" mit dem Benutzer mit `external_id` "john" zusammenführen. Die Verwendung von `most_recently_updated` filtert die Abfrage auf nur einen nicht identifizierten Benutzer. Wenn es also zwei nicht identifizierte Benutzer mit dieser E-Mail-Adresse gäbe, würde nur einer von ihnen mit dem Benutzer mit `external_id` "john" zusammengeführt werden.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Nicht identifizierter Benutzer in identifizierten Benutzer umwandeln

In diesem nächsten Beispiel wird der zuletzt aktualisierte nicht identifizierte Benutzer mit der E-Mail-Adresse "john.smith@braze.com" mit dem zuletzt aktualisierten identifizierten Benutzer mit der E-Mail-Adresse "john.smith@braze.com" zusammengeführt. Die Verwendung von `most_recently_updated` filtert die Abfragen auf nur einen Benutzer (einen nicht identifizierten Benutzer für `identifier_to_merge` und einen identifizierten Benutzer für `identifier_to_keep`).

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Zusammenführen eines nicht identifizierten Benutzers ohne Einbeziehung der zuletzt aktualisierten Priorisierung

Wenn es zwei nicht identifizierte Benutzer mit der E-Mail-Adresse "john.smith@braze.com" gibt, führt diese Beispielanfrage keine Benutzer zusammen, da es zwei nicht identifizierte Benutzer mit dieser E-Mail-Adresse gibt. Diese Anfrage funktioniert nur, wenn es nur einen nicht identifizierten Benutzer mit der E-Mail-Adresse "john.smith@braze.com" gibt.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Antwort

Es gibt zwei Statuscode-Antworten für diesen Endpunkt: `202` und `400`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlersuche](#troubleshooting).

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Fehlersuche

Die folgende Tabelle enthält mögliche Fehlermeldungen, die auftreten können.

| Fehler | Fehlersuche |
| --- |
| `'merge_updates' must be an array of objects` | Prüfen Sie, ob `merge_updates` ein Array von Objekten ist. |
| `a single request may not contain more than 50 merge updates` | Sie können nur bis zu 50 Zusammenführungs-Updates in einer Anfrage angeben. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, or 'email' property that is a string` | Überprüfen Sie die Identifikatoren in Ihrer Anfrage. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Stellen Sie sicher, dass `merge_updates` nur die beiden Objekte `identifier_to_merge` und `identifier_to_keep` enthält. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
