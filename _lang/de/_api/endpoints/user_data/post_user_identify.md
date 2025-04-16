---
nav_title: "POST: Nutzer:innen identifizieren"
article_title: "POST: Nutzer:innen identifizieren"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Dieser Artikel beschreibt die Details des Endpunkts Nutzer:innen identifizieren in Braze."

---
{% api %}
# Nutzer:innen identifizieren
{% apimethod post %}
/benutzer:innen/identify
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen nicht identifizierten Nutzer:innen (nur Alias, nur E-Mail oder nur Telefonnummer) anhand der angegebenen externen ID zu identifizieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Funktionsweise

Der Aufruf von `/users/identify` kombiniert ein Nutzerprofil, das durch einen Alias (Nur-Alias-Profil), eine E-Mail Adresse (Nur-E-Mail-Profil) oder eine Telefonnummer (Nur-Telefonnummer-Profil) identifiziert wird, mit einem Nutzerprofil, das über eine `external_id` (identifiziertes Profil) verfügt, und entfernt dann das Nur-Alias-Profil. 

Um einen Nutzer:in zu identifizieren, muss ein `external_id` in das Objekt `aliases_to_identify` oder `emails_to_identify` oder `phone_numbers_to_identify` aufgenommen werden. Wenn es keinen Nutzer:in mit diesem `external_id` gibt, wird `external_id` zum Datensatz des Nutzer:innen hinzugefügt, und der Nutzer gilt als identifiziert.

Beachten Sie das Folgende:

- Wenn diese nachträglichen Verknüpfungen mit dem Feld `merge_behavior` auf `none` gesetzt werden, werden nur die Push-Tokens und der Verlauf der Nachrichten, die mit dem Nutzer-Alias verbunden sind, beibehalten. Alle Attribute, Ereignisse oder Käufe werden "verwaist" und sind für den identifizierten Nutzer:innen nicht verfügbar. Eine Abhilfe besteht darin, die Daten des Nutzer:innen vor der Identifizierung über den [Endpunkt`/users/export/ids` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) zu exportieren und dann die Attribute, Ereignisse und Käufe erneut mit dem Nutzer:innen zu verknüpfen.
- Wenn das Feld `merge_behavior` auf `merge` eingestellt ist, führt dieser Endpunkt [bestimmte Felder](#merge) des anonymen Nutzer:in mit dem identifizierten Nutzer zusammen.
- Nutzer:innen können nur einen Alias für ein bestimmtes Label haben. Wenn es bereits einen Nutzer:innen mit der Adresse `external_id` gibt, der einen Alias mit demselben Label wie das Profil "Nur Alias" hat, werden die Nutzerprofile nicht kombiniert.

{% alert tip %}
Um unerwartete Datenverluste bei der Identifizierung von Nutzer:innen zu vermeiden, empfehlen wir Ihnen dringend, zunächst die [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) zu referenzieren, um zu erfahren, wie Sie Nutzerdaten erfassen können, wenn bereits Bezeichner-Alias-Informationen vorhanden sind.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.identify`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpunkt='Nutzer:innen identifizieren' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of string) User emails to identify,
   "phone_numbers_to_identify": (optional, array of string) User phone numbers to identify,
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Parameter der Anfrage

Sie können pro Anfrage bis zu 50 Nutzer:innen-Aliase hinzufügen. Sie können mehrere zusätzliche Nutzer:innen-Alias mit einem einzigen `external_id` verknüpfen.

| Parameter                   | Erforderlich | Datentyp                           | Beschreibung                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | Erforderlich | Bezeichner-Array zur Identifizierung des Objekts | Siehe [Bezeichner zur Identifizierung des Objekts]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) und [Nutzer:in-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`        | Erforderlich | Bezeichner-Array zur Identifizierung des Objekts | E-Mail-Adressen zur Identifizierung von Nutzer:innen. Siehe [Identifizierung von Nutzer:innen per E-Mail](#identifying-users-by-email).                                                                                                              |
| `phone_numbers_to_identify` | Erforderlich | Bezeichner-Array zur Identifizierung des Objekts | Telefonnummern zur Identifizierung von Nutzer:innen.                                                                                                                                            |
| `merge_behavior`            | Optional | String                              | Erwartet wird eines von `none` oder `merge`.                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Feld Merge_behavior {#merge}

Wenn Sie das Feld `merge_behavior` auf `merge` setzen, wird der Endpunkt so eingestellt, dass er die folgende Liste von Feldern, die **ausschließlich** bei anonymen Nutzer:in gefunden wurden, mit dem identifizierten Nutzer zusammenführt. Wenn Sie das Feld auf `none` setzen, werden keine Nutzerdaten mit dem identifizierten Nutzerprofil zusammengeführt. Standardmäßig wird dieses Feld auf `merge` gesetzt.

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
- Datum der ersten Sitzung (Braze wählt das frühere Datum der beiden Termine)
- Datum der letzten Sitzung (Braze wählt das spätere Datum der beiden Termine)
- Angepasste Attribute
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
- Kampagnen-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Verlauf des Messaging und des Engagements für Nachrichten
- Angepasste Events und Kauf-Events mit Zählung und Zeitstempel für das erste und letzte Datum 
  - Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Bei Kauf-Events umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".
- Sitzungsdaten, wenn die App in beiden Nutzerprofilen vorhanden ist
  - Wenn unsere Zielgruppe zum Beispiel keine App-Zusammenfassung für "ABCApp" hat, unser ursprünglicher Nutzer aber schon, dann hat der Nutzer:innen nach der Zusammenführung die App-Zusammenfassung "ABCApp" in seinem Profil.
{% enddetails %}

### Identifizierung von Nutzer:innen per E-Mail

Wenn ein `email` als Bezeichner angegeben wird, müssen Sie auch `prioritization` in den Bezeichner aufnehmen. `prioritization` muss ein Array sein, das angibt, welcher Nutzer:innen zusammengeführt werden soll, wenn mehrere Nutzer:innen gefunden werden. `prioritization` ist ein geordnetes Array, d.h. wenn mehr als ein Nutzer:innen aus einer Priorisierung übereinstimmt, wird die Zusammenführung nicht durchgeführt.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (referenziert auf den zuletzt aktualisierten Nutzer:in)
- `least_recently_updated` (referenziert auf die Priorisierung des Nutzers:in, der zuletzt aktualisiert wurde)

Es kann jeweils nur eine der folgenden Optionen im Prioritätsfeld vorhanden sein:

- `identified` bezieht sich auf die Priorisierung eines Nutzer:innen mit einem `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Nutzer:in ohne ein `external_id`

Wenn Sie in dem Array `identified` angeben, würde das bedeuten, dass der Nutzer:in über eine `external_id` verfügen **muss**, um in den Canvas eingegeben zu werden. Wenn Sie möchten, dass Nutzer:innen mit E-Mail-Adressen die Nachricht eingeben können, unabhängig davon, ob sie identifiziert sind oder nicht, verwenden Sie stattdessen nur den Parameter `most_recently_updated` oder `least_recently_updated`.

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
  "merge_behavior": "merge"
}'
```

{% alert tip %}
Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu [User-Aliases]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
{% endalert %}

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
