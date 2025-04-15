---
nav_title: "POST: Benutzer identifizieren"
article_title: "POST: Benutzer identifizieren"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "Dieser Artikel enthält Einzelheiten zum Braze-Endpunkt Identifizieren von Benutzern."

---
{% api %}
# Identifizieren Sie Benutzer
{% apimethod post %}
/users/identify
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen nicht identifizierten Benutzer (nur Alias oder nur E-Mail) anhand der angegebenen externen ID zu identifizieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Wie es funktioniert

Der Aufruf von `/users/identify` kombiniert ein Benutzerprofil, das durch einen Alias (Nur-Alias-Profil) oder eine E-Mail-Adresse (Nur-E-Mail-Profil) identifiziert wird, mit einem Benutzerprofil, das eine `external_id` (identifiziertes Profil) hat, und entfernt dann das Nur-Alias-Profil. 

Zur Identifizierung eines Benutzers muss ein `external_id` in das Objekt `aliases_to_identify` oder `emails_to_identify` aufgenommen werden. Wenn es keinen Benutzer mit diesem `external_id` gibt, wird `external_id` zum Datensatz des Alias-Benutzers hinzugefügt und der Benutzer gilt als identifiziert.

Beachten Sie das Folgende:

- Wenn diese nachträglichen Verknüpfungen mit dem Feld `merge_behavior` auf `none` gesetzt werden, werden nur die Push-Token und die Nachrichtenhistorie, die mit dem Benutzer-Alias verbunden sind, beibehalten; alle Attribute, Ereignisse oder Käufe werden "verwaist" und sind für den identifizierten Benutzer nicht verfügbar. Eine Abhilfe besteht darin, die Daten des Alias-Benutzers vor der Identifizierung über den [Endpunkt`/users/export/ids` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) zu exportieren und dann die Attribute, Ereignisse und Einkäufe erneut mit dem identifizierten Benutzer zu verknüpfen.
- Wenn Assoziationen hergestellt werden und das Feld `merge_behavior` auf `merge` gesetzt ist, wird dieser Endpunkt [bestimmte Felder](#merge) des anonymen Benutzers mit dem identifizierten Benutzer zusammenführen.

{% alert tip %}
Um unerwartete Datenverluste bei der Identifizierung von Benutzern zu vermeiden, empfehlen wir Ihnen dringend, sich zunächst in den [bewährten Verfahren zur Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) über die Erfassung von Benutzerdaten zu informieren, wenn bereits Alias-Benutzerinformationen vorhanden sind.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.identify`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "email_addresses": (optional, array of string) User emails for the users to identify,
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### Parameter anfordern

Sie können bis zu 50 Benutzer-Aliase pro Anfrage hinzufügen. Sie können mehrere zusätzliche Benutzer-Aliase mit einem einzigen `external_id` verknüpfen.

| Parameter             | Erforderlich | Daten Typ                           | Beschreibung                                                                                                                                                                 |
|-----------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify` | Erforderlich | Array von Aliasen zur Identifizierung des Objekts | Siehe [Alias zur Identifizierung des Objekts]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) und [Benutzer-Aliasobjekt]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `emails_to_identify`  | Erforderlich | Array von Aliasen zur Identifizierung des Objekts | Siehe [Identifizierung von Benutzern per E-Mail](#identifying-users-by-email).                                                                                                              |
| `merge_behavior`      | Optional | String                              | Erwartet wird eines von `none` oder `merge`.                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Feld Merge_behavior {#merge}

Wenn Sie das Feld `merge_behavior` auf `merge` setzen, wird der Endpunkt so eingestellt, dass er die folgende Liste von Feldern, die **ausschließlich** bei dem anonymen Benutzer gefunden wurden, mit dem identifizierten Benutzer zusammenführt. Wenn Sie das Feld auf `none` setzen, werden keine Benutzerdaten mit dem identifizierten Benutzerprofil zusammengeführt.

{% details Liste der Felder, die zusammengeführt werden %}
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
- Anzahl der Sitzungen (die Summe der Sitzungen aus beiden Profilen)
- Datum der ersten Sitzung (Braze wählt das frühere Datum der beiden Termine)
- Datum der letzten Sitzung (Braze wählt das spätere Datum der beiden Termine)
- Benutzerdefinierte Attribute
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
- Kampagnenzusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder aus)
- Verlauf der Nachrichten und des Nachrichteninteresses
- Benutzerdefinierte Ereignis- und Kaufereigniszählung sowie Zeitstempel für das erste und letzte Datum 
  - Diese zusammengeführten Felder aktualisieren die Filter "für X Ereignisse in Y Tagen". Für Kaufereignisse umfassen diese Filter "Anzahl der Käufe in Y Tagen" und "Geldausgabe in den letzten Y Tagen".
- Sitzungsdaten, wenn die App auf beiden Benutzerprofilen existiert
  - Wenn unser Zielbenutzer beispielsweise keine App-Zusammenfassung für "ABCApp" hat, unser ursprünglicher Benutzer aber schon, wird der Zielbenutzer nach der Zusammenführung die App-Zusammenfassung "ABCApp" in seinem Profil haben.
{% enddetails %}

### Identifizierung von Benutzern per E-Mail

Wenn ein `email` als Bezeichner angegeben wird, ist ein zusätzlicher `prioritization` Wert im Bezeichner erforderlich. `prioritization` sollte ein Array sein, das angibt, welcher Benutzer zusammengeführt werden soll, wenn mehrere Benutzer gefunden werden. `prioritization` ist ein geordnetes Array, d.h. wenn mehr als ein Benutzer aus einer Priorisierung übereinstimmt, wird die Zusammenführung nicht durchgeführt.

Die zulässigen Werte für das Array sind: `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated` bezieht sich auf die Priorisierung des zuletzt aktualisierten Benutzers.

Es kann jeweils nur eine der folgenden Optionen im Prioritätsfeld vorhanden sein:
- `identified` bezieht sich auf die Priorisierung eines Benutzers mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung eines Benutzers ohne `external_id`

## Beispiel anfordern
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
Weitere Informationen zu `alias_name` und `alias_label` finden Sie in unserer Dokumentation zu den [Benutzer-Aliasnamen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
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
