---
nav_title: "POST: Nutzer:innen identifizieren"
article_title: "POST: Nutzer:innen identifizieren"
search_tag: Endpunkt
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Nutzer:innen identifizieren"."

---
{% api %}
# Nutzer:innen identifizieren
{% apimethod post %}
/users/identify
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um nicht identifizierte Nutzer:innen (nur Alias, nur E-Mail oder nur Telefonnummer) anhand der angegebenen externen ID zu identifizieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Funktionsweise

Der Aufruf von `/users/identify` kombiniert ein Nutzerprofil, das durch einen Alias (Nur-Alias-Profil), eine E-Mail-Adresse (Nur-E-Mail-Profil) oder eine Telefonnummer (Nur-Telefonnummer-Profil) identifiziert wird, mit einem Nutzerprofil, das über eine `external_id` (identifiziertes Profil) verfügt, und entfernt dann das Nur-Alias-Profil.

Die Identifizierung von Nutzer:innen erfordert eine `external_id` in den folgenden Objekten:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

Wenn keine Nutzer:in mit dieser `external_id` vorhanden ist, wird die `external_id` zum Datensatz der Alias-Nutzer:in hinzugefügt, und die Nutzer:in gilt als identifiziert. Nutzer:innen können nur einen Alias für ein bestimmtes Label haben. Wenn bereits eine Nutzer:in mit der `external_id` existiert und einen bestehenden Alias mit dem gleichen Label wie das Nur-Alias-Profil hat, werden die Nutzerprofile nicht zusammengeführt.

{% alert tip %}
Um unerwartete Datenverluste bei der Identifizierung von Nutzer:innen zu vermeiden, empfehlen wir Ihnen dringend, zunächst die [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) zu lesen, um zu erfahren, wie Sie Nutzerdaten erfassen können, wenn bereits Nur-Alias-Nutzerinformationen vorhanden sind.
{% endalert %}

### Verhalten bei der Zusammenführung

Standardmäßig führt dieser Endpunkt die folgenden Felder, die **ausschließlich** bei anonymen Nutzer:innen vorhanden sind, mit denen der identifizierten Nutzer:in zusammen.

{% details Liste der Felder, die zusammengeführt werden %}
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
- Anzahl der Sitzungen (die Summe der Sitzungen aus beiden Profilen)
- Datum der ersten Sitzung (Braze wählt das frühere der beiden Daten)
- Datum der letzten Sitzung (Braze wählt das spätere der beiden Daten)
- Angepasste Attribute
- Angepasste Event- und Kauf-Event-Daten
- Angepasste Event- und Kauf-Event-Eigenschaften für die Segmentierung „X-mal in Y Tagen" (wobei X<=50 und Y<=30)
- Segmentierbare Zusammenfassung angepasster Events
  - Anzahl der Events (die Summe aus beiden Profilen)
  - Event erstmals aufgetreten (Braze wählt das frühere der beiden Daten)
  - Event zuletzt aufgetreten (Braze wählt das spätere der beiden Daten)
- In-App-Käufe insgesamt in Cent (die Summe aus beiden Profilen)
- Gesamtzahl der Käufe (die Summe aus beiden Profilen)
- Datum des ersten Kaufs (Braze wählt das frühere der beiden Daten)
- Datum des letzten Kaufs (Braze wählt das spätere der beiden Daten)
- App-Zusammenfassungen
- Last_X_at-Felder (Braze aktualisiert die Felder, wenn die verwaisten Profilfelder aktueller sind)
- Kampagnenzusammenfassungen (Braze wählt die aktuellsten Datumsfelder)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder)
- Nachrichten- und Nachrichten-Engagement-Verlauf
- Angepasste Events und Kauf-Events mit Zählung sowie Zeitstempel für erstes und letztes Datum
  - Diese zusammengeführten Felder aktualisieren die Filter „für X Events in Y Tagen". Bei Kauf-Events umfassen diese Filter „Anzahl der Käufe in Y Tagen" und „Ausgaben in den letzten Y Tagen".
- Sitzungsdaten, wenn die App in beiden Nutzerprofilen vorhanden ist
  - Wenn beispielsweise die Zielnutzer:in keine App-Zusammenfassung für „ABCApp" hat, die ursprüngliche Nutzer:in jedoch schon, erhält die Zielnutzer:in nach der Zusammenführung die App-Zusammenfassung „ABCApp" in ihrem Profil.
{% enddetails %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.identify`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Anfrageparameter

Sie können pro Anfrage bis zu 50 Nutzer-Aliase hinzufügen. Sie können mehrere zusätzliche Nutzer-Aliase mit einer einzigen `external_id` verknüpfen.

{% alert important %}
Eine der folgenden Angaben ist pro Anfrage erforderlich: `aliases_to_identify`, `emails_to_identify` oder `phone_numbers_to_identify`. Sie können diesen Endpunkt zum Beispiel verwenden, um Nutzer:innen per E-Mail zu identifizieren, indem Sie `emails_to_identify` in Ihrer Anfrage verwenden.
{% endalert %}

| Parameter                   | Erforderlich | Datentyp                           | Beschreibung                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Erforderlich | Array von Alias-zu-identifizieren-Objekten | Siehe [Alias-zu-identifizieren-Objekt]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) und [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Erforderlich | Array von Alias-zu-identifizieren-Objekten | Erforderlich, wenn `email` als Bezeichner angegeben ist. E-Mail-Adressen zur Identifizierung von Nutzer:innen. Siehe [Identifizierung von Nutzer:innen per E-Mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Erforderlich | Array von Alias-zu-identifizieren-Objekten | Telefonnummern zur Identifizierung von Nutzer:innen.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Identifizierung von Nutzer:innen anhand von E-Mail-Adressen und Telefonnummern

Wenn eine E-Mail-Adresse oder Telefonnummer als Bezeichner angegeben wird, müssen Sie auch `prioritization` im Bezeichner angeben.

`prioritization` muss ein Array sein, das angibt, welche Nutzer:in zusammengeführt werden soll, wenn mehrere Nutzer:innen gefunden werden. `prioritization` ist ein geordnetes Array – wenn also mehr als eine Nutzer:in aus einer Priorisierung übereinstimmt, findet keine Zusammenführung statt.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (bezieht sich auf die Priorisierung der zuletzt aktualisierten Nutzer:in)
- `least_recently_updated` (bezieht sich auf die Priorisierung der am längsten nicht aktualisierten Nutzer:in)

Es kann jeweils nur eine der folgenden Optionen im Priorisierungs-Array vorhanden sein:

- `identified` bezieht sich auf die Priorisierung einer Nutzer:in mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung einer Nutzer:in ohne eine `external_id`

{% alert note %}
Eine Zusammenführung findet nicht statt, wenn die E-Mail-Adresse oder Telefonnummer mit mehreren Nutzer:innen übereinstimmt. Dies schließt Fälle ein, in denen eine dieser Nutzer:innen die gleiche `external_id` hat wie die in der Anfrage angegebene. In diesen Fällen gibt der Endpunkt `"message": "success"` zurück, aber die Nutzerprofile werden nicht zusammengeführt. Um dies zu vermeiden, stellen Sie sicher, dass die E-Mail-Adresse oder Telefonnummer nur mit nicht identifizierten Nutzer:innen verknüpft ist, bevor Sie diesen Endpunkt aufrufen.
{% endalert %}

## Beispiel für eine Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

### Groß-/Kleinschreibung

Das Feld `alias_name` unterscheidet zwischen Groß- und Kleinschreibung. Eine Anfrage, die einen `201`-Statuscode zurückgibt, bestätigt nur, dass die Anfrage-Syntax gültig war – sie bestätigt nicht, dass der Alias zugeordnet wurde. Wenn die Groß-/Kleinschreibung von `alias_name` in Ihrer Anfrage nicht exakt mit dem im Nutzerprofil gespeicherten Alias übereinstimmt, schlägt der Vorgang stillschweigend fehl und die `external_id` wird nicht zugewiesen. Wenn der gespeicherte Alias beispielsweise `JimJones@example.com` lautet, gibt eine Anfrage mit `jimjones@example.com` zwar Erfolg zurück, erzeugt aber kein Ergebnis.

{% alert tip %}
Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

## Antwort

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}