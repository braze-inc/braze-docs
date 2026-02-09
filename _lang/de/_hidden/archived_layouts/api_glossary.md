---
title: API oder Code Glossar
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Dies ist die Beschreibung der Google-Suche. Zeichen, die über 160 hinausgehen, werden abgeschnitten, fassen Sie sich kurz."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 E-Mail Template erstellen
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
Posten,E-Mail,Erstellen,Template,REST,API
{% endapitags %}

Verwenden Sie die E-Mail Template REST APIs, um die E-Mail Templates, die Sie auf den Braze Dashboards gespeichert haben, auf der Seite Templates & Medien programmatisch zu verwalten. Braze bietet zwei Endpunkte zum Erstellen und Aktualisieren Ihrer E-Mail Templates.

Die Antwort von diesem Endpunkt enthält ein Feld für `email_template_id`, das zum Update des Templates in nachfolgenden API-Aufrufen verwendet werden kann.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGE KÖRPER
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### BEISPIELANTWORT
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `modified_after`  | Kein:e | String in ISO 8601 | Ruft nur Templates ab, die zum oder nach dem angegebenen Zeitpunkt aktualisiert wurden. |
| `modified_before`  |  Kein:e | String in ISO 8601 | Ruft nur Templates ab, die zum oder vor dem angegebenen Zeitpunkt aktualisiert wurden. |
| `limit` | Kein:e | Positive Zahl | Maximale Anzahl der abzurufenden Templates, Standard ist 100, wenn nicht angegeben, der maximal zulässige Wert ist 1000. |
| `offset`  |  Kein:e | Positive Zahl | Anzahl der Templates, die übersprungen werden sollen, bevor der Rest der Templates, die den Suchkriterien entsprechen, zurückgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 Liste verfügbarer E-Mails Template
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
Holen,E-Mail,Template,Liste,REST
{% endapitags %}

Verwenden Sie die folgenden Endpunkte, um eine Liste der verfügbaren Templates zu erhalten.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGE KÖRPER
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### BEISPIELANTWORT
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `email_template_id`  | Ja | String | Der API Bezeichner Ihrer E-Mail Vorlage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 Kampagnen triggern das Senden
{% apimethod post %}Kampagnen/triggern/senden{% endapimethod %}
{% apitags %}Posten, Kampagnen, Triggern, Senden{% endapitags %}

Mit der API-getriggerten Zustellung können Sie den Inhalt von Nachrichten innerhalb des Braze-Dashboards unterbringen und gleichzeitig über Ihre API festlegen, wann und an wen eine Nachricht gesendet wird. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGE KÖRPER
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### BEISPIELANTWORT
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### PARAMETER-DETAILS

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `email_template_id`  | Ja | String | Der API Bezeichner Ihrer E-Mail Vorlage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 Kampagnen triggern das Senden
{% apimethod put %}Nutzer:innen/Tracking{% endapimethod %}
{% apitags %}PUT, Kampagnen, Triggern, Senden{% endapitags %}

Mit diesem Endpunkt können Sie angepasste Events, Benutzer-Attribute und Käufe für Nutzer:innen aufzeichnen. Sie können bis zu 75 Attribute, Ereignisse und Kauf-Objekte pro Anfrage hinzufügen. Das heißt, Sie können nur Attribute für bis zu 75 Nutzer:innen gleichzeitig veröffentlichen, aber im selben API-Aufruf können Sie auch bis zu 75 Ereignisse und bis zu 75 Käufe bereitstellen.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### ANFRAGE KÖRPER
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### BEISPIELANTWORT
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### PARAMETER-DETAILS

| Feld Nutzer:in | Spezifikation des Datentyps |
| ---| --- |
| Land | (String) Wir verlangen, dass die Ländercodes im [ISO-3166-1 alpha-2 Standard][17] an Braze übergeben werden. |
| current_location | (object) Der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum, an dem der Nutzer:innen die App zum ersten Mal benutzt hat) String im Format ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| date_of_last_session | (Datum, an dem der Nutzer:innen die App zuletzt benutzt hat) String im Format ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. |
| Geburtsdatum | (Geburtsdatum) String im Format "JJJJ-MM-TT", zum Beispiel 1980-12-21. |
| E-Mail | (String) |
| email_subscribe | (String) Verfügbare Werte sind "opted_in" (explizit für den Erhalt von E-Mail-Nachrichten registriert), "abgemeldet" (explizit gegen E-Mail-Nachrichten) und "abonniert" (weder Opt-in noch Opt-out).  |
| external_id | (String) des eindeutigen Bezeichners des Nutzers:in. |
| Facebook | Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| first_name | (String) |
| Geschlecht | (String) "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen) oder nil (unbekannt). |
| home_city | (String) |
| image_url | (String) URL des Bildes, das mit dem Nutzerprofil verknüpft werden soll. |
| Sprache | (String) verlangen wir, dass die Sprache an Braze im [ISO-639-1-Standard][24] übergeben wird. <br>[Liste der akzeptierten Sprachen](/docs/user_guide/data_and_analytics/user_data_collection/language_codes/)|
| last_name | (String) |
|marked_email_as_spam_at| (String) Datum, an dem die E-Mail des Nutzers:in als Spam markiert wurde. Erscheint im Format ISO 8601 oder im Format jjjj-MM-tt'T'HH:mm:ss:SSSZ.|
| Telefon | (String) |
| push_subscribe | (String) Verfügbare Werte sind "opted_in" (explizit für den Empfang von Push-Nachrichten registriert), "abgemeldet" (explizit von Push-Nachrichten abgemeldet) und "abonniert" (weder Opt-in noch abgemeldet).  |
| push_tokens | Array von Objekten mit `app_id` und `token` String. Sie können optional eine `device_id` für das Gerät angeben, mit dem dieses Token verbunden ist, z.B. `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| time_zone | (String) Der Name der Zeitzone aus der [IANA-Zeitzonendatenbank][26] (zum Beispiel "America/New_York" oder "Eastern Time (US & Canada)"). Es werden nur gültige Zeitzonenwerte eingestellt. |
| Twitter | Hash mit einem der folgenden Werte: `id` (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
