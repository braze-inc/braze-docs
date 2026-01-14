---
nav_title: "POST: Nutzer:innen zusammenführen"
article_title: "POST: Nutzer:innen zusammenführen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Nutzer:innen zusammenführen Braze."

---
{% api %}
# Nutzer:innen zusammenführen
{% apimethod post %}
/nutzer:innen/merge
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Nutzer:innen mit einem anderen Nutzer zusammenzuführen. 

Pro Anfrage können bis zu 50 Zusammenführungen angegeben werden. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.merge`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `merge_updates` | Erforderlich | Array | Ein Objekt-Array. Jedes Objekt sollte ein `identifier_to_merge` Objekt und ein `identifier_to_keep` Objekt enthalten, die jeweils einen Nutzer:innen entweder durch `external_id`, `user_alias`, `phone` oder `email` referenzieren sollten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Zusammenführungsverhalten

Das unten dokumentierte Verhalten gilt für alle Braze Features, die *nicht* von Snowflake unterstützt werden. Nutzer:innen werden auf dem Tab **Verlauf von Messaging**, Segment-Erweiterungen, Query Builder und Currents nicht mehr zusammengeführt.

{% alert important %}
Der Endpunkt garantiert nicht die Reihenfolge der `merge_updates` Objekte, die aktualisiert werden.
{% endalert %}

Dieser Endpunkt fügt die folgenden Felder zusammen, wenn sie bei dem Targeting Nutzer:innen nicht gefunden werden.

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Telefonnummer
- Zeitzone
- Wohnort
- Land
- Sprache
- Informationen zum Gerät
- Anzahl der Sitzungen (die Summe der Sitzungen aus beiden Profilen)
- Datum der ersten Sitzung (Braze wählt das frühere Datum der beiden Termine)
- Datum der letzten Sitzung (Braze wählt das spätere Datum der beiden Termine)
- Angepasste Attribute (bestehende angepasste Attribute auf dem Zielprofil werden beibehalten und umfassen auch angepasste Attribute, die auf dem Zielprofil nicht vorhanden waren)
- Angepasste Event- und Kauf-Event-Daten
- Angepasste Event- und Kauf-Event-Eigenschaften für die Segmentierung "X mal in Y Tagen" (wobei X<=50 und Y<=30)
- Segmentierbare Zusammenfassung angepasster Events
  - Anzahl der Ereignisse (die Summe aus beiden Profilen)
  - Das Ereignis ist zuerst eingetreten (Braze wählt das frühere Datum der beiden Daten)
  - Letztes Ereignis (Braze wählt das spätere Datum der beiden Daten)
- In-App-Käufe insgesamt in Cent (die Summe aus beiden Profilen)
- Gesamtzahl der Käufe (die Summe aus beiden Profilen)
- Datum des ersten Kaufs (Braze wählt das frühere der beiden Daten)
- Datum des letzten Kaufs (Braze wählt das spätere Datum der beiden Daten)
- App Zusammenfassungen
- Last_X_at Felder (Braze aktualisiert die Felder, wenn die verwaisten Profilfelder neueren Datums sind)
- Daten zur Interaktion mit Kampagnen (Braze wählt die aktuellsten Datumsfelder aus)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Verlauf des Messaging und des Engagements für Nachrichten
- Sitzungsdaten werden nur zusammengeführt, wenn die App in beiden Nutzerprofilen vorhanden ist.

{% alert note %}
Bei der Zusammenführung von Nutzer:innen funktioniert die Verwendung des Endpunkts `/users/merge` genauso wie bei der [Methode`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

#### Angepasstes Event-Datum und Kauf-Event-Datum Verhalten

Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Bei Kauf-Events umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".

### Zusammenführung von Nutzer:innen per E-Mail oder Telefonnummer

Wenn ein `email` oder `phone` als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization` Wert im Bezeichner erforderlich. `prioritization` sollte ein Array sein, das angibt, welcher Nutzer:innen zusammengeführt werden soll, wenn mehrere Nutzer:innen gefunden werden. `prioritization` ist ein geordnetes Array, d.h. wenn mehr als ein Nutzer:innen aus einer Priorisierung übereinstimmt, wird die Zusammenführung nicht durchgeführt.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (referenziert auf den zuletzt aktualisierten Nutzer:in)
- `least_recently_updated` (referenziert auf die Priorisierung des Nutzers:in, der zuletzt aktualisiert wurde)

Es kann jeweils nur eine der folgenden Optionen im Prioritätsfeld vorhanden sein:

- `identified` bezieht sich auf die Priorisierung eines Nutzer:innen mit einem `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Nutzer:in ohne ein `external_id`

## Beispiel-Anfragen

### Einfache Anfrage

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

### Zusammenführung nicht identifizierter Nutzer:in

Die folgende Anfrage würde den zuletzt aktualisierten nicht identifizierten Nutzer:innen mit der E-Mail Adresse "john.smith@braze.com" mit dem Nutzer:innen mit `external_id` "john" zusammenführen. Die Verwendung von `most_recently_updated` oder `least_recently_updated` filtert die Abfrage auf nur einen nicht identifizierten Nutzer:innen. Wenn es also zwei nicht identifizierte Nutzer:innen mit dieser E-Mail Adresse gäbe, würde nur eine davon mit dem Nutzer:innen mit `external_id` "john" zusammengeführt werden.

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

### Zusammenführung nicht identifizierter Nutzer:innen in identifizierte Nutzer:innen

In diesem nächsten Beispiel wird der zuletzt aktualisierte nicht identifizierte Nutzer:innen mit der E-Mail Adresse "john.smith@braze.com" mit dem zuletzt aktualisierten identifizierten Nutzer:innen mit der E-Mail Adresse "john.smith@braze.com" zusammengeführt. Die Verwendung von `most_recently_updated` oder `least_recently_updated` filtert die Abfragen auf nur einen Nutzer:innen (einen nicht identifizierten Nutzer für `identifier_to_merge` und einen identifizierten Nutzer für `identifier_to_keep`).

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
        "prioritization": ["unidentified", "most_recently_updated", "least_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated", "least_recently_updated"]
      }
    }
  ]
}'
```

### Zusammenführen eines nicht identifizierten Nutzer:in ohne Einbeziehung der zuletzt aktualisierten Priorisierung

Wenn es zwei nicht identifizierte Nutzer:innen mit der E-Mail Adresse "john.smith@braze.com" gibt, werden in dieser Beispielanfrage keine Nutzer:innen zusammengeführt, da es zwei nicht identifizierte Nutzer:innen mit dieser E-Mail Adresse gibt. Diese Anfrage funktioniert nur, wenn es nur einen nicht identifizierten Nutzer:in mit der E-Mail Adresse "john.smith@braze.com" gibt.

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

Für diesen Endpunkt gibt es zwei Status Code Antworten: `202` und `400`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `202` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Fehlersuche

In der folgenden Tabelle sind mögliche Fehlermeldungen aufgeführt.

| Fehler | Fehlersuche |
| --- |
| `'merge_updates' must be an array of objects` | Prüfen Sie, ob `merge_updates` ein Array von Objekten ist. |
| `a single request may not contain more than 50 merge updates` | Sie können in einer einzigen Anfrage nur bis zu 50 zusammenführende Updates angeben. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Überprüfen Sie die Bezeichner in Ihrer Anfrage. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Stellen Sie sicher, dass `merge_updates` nur die beiden Objekte `identifier_to_merge` und `identifier_to_keep` enthält. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
