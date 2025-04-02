---
nav_title: "Benutzerattribute Objekt"
article_title: API Benutzerattribute Objekt
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Objekts Benutzerattribute."

---

# Objekt Benutzerattribute

> Eine API-Anfrage mit einem beliebigen Feld im Attribute-Objekt erstellt oder aktualisiert ein Attribut dieses Namens mit dem angegebenen Wert im angegebenen Benutzerprofil. 

Verwenden Sie die Feldnamen des Braze-Benutzerprofils (wie nachfolgend aufgeführt oder im Abschnitt für [Braze-Benutzerprofilfelder][27]), um diese speziellen Werte im Benutzerprofil im Dashboard zu aktualisieren, oder fügen Sie Ihre eigenen benutzerdefinierten Attributdaten für den Benutzer hinzu.

## Objektkörper

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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

- [Externe Benutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Um ein Profilattribut zu entfernen, setzen Sie es auf `null`. Einige Felder, wie z.B. `external_id` und `user_alias`, können nicht mehr entfernt werden, nachdem sie einem Benutzerprofil hinzugefügt wurden.

#### Nur bestehende Profile aktualisieren

Wenn Sie nur bestehende Benutzerprofile in Braze aktualisieren möchten, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Text Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Benutzerprofil, wenn das `external_id` nicht bereits existiert.

{% alert note %}
Wenn Sie ein reines Alias-Benutzerprofil über den Endpunkt `/users/track` erstellen, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das Profil, das nur einen Alias enthält, nicht erstellt.
{% endalert %}

#### Push-Token-Import

Bevor Sie Push-Token in Braze importieren, überprüfen Sie, ob Sie dies tun müssen. Wenn die Braze SDKs eingesetzt werden, verarbeiten sie Push-Tokens automatisch, ohne dass sie über die API hochgeladen werden müssen.

Wenn Sie sie über die API hochladen müssen, können Sie sie entweder für identifizierte Benutzer oder für anonyme Benutzer hochladen. Das bedeutet, dass entweder ein `external_id` vorhanden sein muss, oder die anonymen Benutzer müssen das `push_token_import` Flag auf `true` gesetzt haben. 

{% alert note %}
Beim Importieren von Push-Tokens aus anderen Systemen ist nicht immer eine `external_id` verfügbar. Um die Kommunikation mit diesen Benutzern während des Übergangs zu Braze aufrechtzuerhalten, können Sie die Legacy-Tokens für anonyme Benutzer importieren, ohne `external_id` anzugeben, indem Sie `push_token_import` als `true` angeben.
{% endalert %}

Wenn Sie `push_token_import` als `true` angeben:

* `external_id` und `braze_id` sollten **nicht** angegeben werden.
* Das Attribut Objekt **muss** ein Push-Token enthalten
* Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert. Andernfalls erstellt Braze ein temporäres, anonymes Benutzerprofil für jedes Token, damit Sie diesen Personen weiterhin Nachrichten schicken können.

Nach dem Import, wenn jeder Benutzer die Braze-aktivierte Version Ihrer App startet, verschiebt Braze automatisch das importierte Push-Token in sein Braze-Benutzerprofil und bereinigt das temporäre Profil.

Braze prüft einmal im Monat, ob ein anonymes Profil mit dem Kennzeichen `push_token_import` kein Push-Token hat. Wenn das anonyme Profil nicht mehr über ein Push-Token verfügt, löschen wir das Profil. Wenn das anonyme Profil jedoch noch ein Push-Token hat, was darauf hindeutet, dass der tatsächliche Benutzer sich noch nicht mit diesem Push-Token am Gerät angemeldet hat, unternehmen wir nichts.

Weitere Informationen finden Sie unter [Migrieren von Push-Tokens][3].

#### Benutzerdefinierte Attribut-Datentypen

Die folgenden Datentypen können als benutzerdefiniertes Attribut gespeichert werden:

| Daten Typ | Anmerkungen |
| --- | --- |
| Arrays | Benutzerdefinierte Attribut-Arrays werden unterstützt. Wenn Sie ein Element zu einem benutzerdefinierten Attribut-Array hinzufügen, wird das Element an das Ende des Arrays angehängt, es sei denn, es ist bereits vorhanden. In diesem Fall wird es von seiner aktuellen Position an das Ende des Arrays verschoben.<br><br>Wenn zum Beispiel ein Array `['hotdog','hotdog','hotdog','pizza']` importiert wurde, wird es im Array-Attribut als `['hotdog', 'pizza']` angezeigt, da nur eindeutige Werte unterstützt werden.<br><br>Sie können nicht nur die Werte eines Arrays setzen, indem Sie etwas wie `"my_array_custom_attribute":[ "Value1", "Value2" ]` sagen, sondern Sie können auch Werte zu bestehenden Arrays hinzufügen, indem Sie etwas wie `"my_array_custom_attribute" : { "add" : ["Value3"] },` tun, oder Werte aus einem Array entfernen, indem Sie etwas wie `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>Die maximale Anzahl von Elementen in benutzerdefinierten Attribut-Arrays beträgt standardmäßig 25, kann aber für ein einzelnes Array auf bis zu 100 erhöht werden. Weitere Informationen finden Sie unter [Arrays][6]. |
| Array von Objekten | Mit Array of Objects können Sie eine Liste von Objekten definieren, wobei jedes Objekt eine Reihe von Attributen enthält. Dies kann nützlich sein, wenn Sie mehrere zusammenhängende Datensätze für einen Benutzer speichern müssen, z. B. Hotelaufenthalte, Kaufhistorie oder Vorlieben. <br><br> Sie können zum Beispiel ein benutzerdefiniertes Attribut für ein Benutzerprofil namens `hotel_stays` definieren. Dieses benutzerdefinierte Attribut kann als Array definiert werden, wobei jedes Objekt einen separaten Aufenthalt darstellt, mit Attributen wie `hotel_name`, `check_in_date`, `nights_stayed`. Weitere Einzelheiten finden Sie in [diesem Beispiel](#array-of-objects-example). |
| Boolesche Wörter | `true` oder `false` |
| Daten | Muss im Format [ISO 8601][19] oder in einem der folgenden Formate gespeichert werden: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Beachten Sie, dass "T" ein Zeitbezeichner ist, kein Platzhalter, und nicht geändert oder entfernt werden sollte. <br><br>Zeitattribute ohne Zeitzone sind standardmäßig auf Mitternacht UTC eingestellt (und werden auf dem Dashboard als das Äquivalent zu Mitternacht UTC in der Zeitzone des Unternehmens formatiert). <br><br> Bei Ereignissen mit Zeitstempeln in der Zukunft wird standardmäßig die aktuelle Zeit verwendet. <br><br> Bei regulären benutzerdefinierten Attributen speichert Braze diese Werte als Zeichenketten für den Benutzer, wenn das Jahr kleiner als 0 oder größer als 3000 ist. |
| Schwimmer | Benutzerdefinierte Float-Attribute sind positive oder negative Zahlen mit einem Dezimalpunkt. Sie können z.B. Floats verwenden, um Kontostände oder Benutzerbewertungen für Produkte oder Dienstleistungen zu speichern. |
| Ganze Zahlen | Ganzzahlige benutzerdefinierte Attribute können um positive oder negative Ganzzahlen erhöht werden, indem Sie ihnen ein Objekt mit dem Feld "inc" und dem Wert, um den sie erhöht werden sollen, zuweisen. <br><br>Beispiel: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Verschachtelte benutzerdefinierte Attribute | Verschachtelte benutzerdefinierte Attribute definieren eine Reihe von Attributen als Eigenschaft eines anderen Attributs. Wenn Sie ein benutzerdefiniertes Attributobjekt definieren, legen Sie eine Reihe von zusätzlichen Attributen für dieses Objekt fest. Weitere Informationen finden Sie unter [Verschachtelte benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support). |
| Streicher | Benutzerdefinierte String-Attribute sind Zeichenfolgen, die zum Speichern von Textdaten verwendet werden. Sie können zum Beispiel Strings verwenden, um Vor- und Nachnamen, E-Mail-Adressen oder Vorlieben zu speichern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Informationen darüber, wann Sie ein benutzerdefiniertes Ereignis und wann Sie ein benutzerdefiniertes Attribut verwenden sollten, finden Sie in unserer jeweiligen Dokumentation zu [benutzerdefinierten Ereignissen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) und [benutzerdefinierten Attributen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).
{% endalert %}

##### Beispiel eines Arrays von Objekten 

Mit dieser Reihe von Objekten können Sie Segmente erstellen, die auf bestimmten Kriterien innerhalb der Aufenthalte basieren, und Ihre Nachrichten anhand der Daten jedes Aufenthalts mit Liquid-Vorlagen personalisieren.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Felder des Benutzerprofils auslöten {#braze-user-profile-fields}

{% alert important %}
Bei den folgenden Feldern des Benutzerprofils wird zwischen Groß- und Kleinschreibung unterschieden. Achten Sie also darauf, dass Sie diese Felder in Kleinbuchstaben referenzieren.
{% endalert %}

| Feld Benutzerprofil | Spezifikation des Datentyps |
| ---| --- |
| alias_name | (Zeichenfolge) |
| alias_label | (Zeichenfolge) |
| braze_id | (string, optional) Wenn ein Benutzerprofil vom SDK erkannt wird, wird ein anonymes Benutzerprofil mit einem zugehörigen `braze_id` erstellt. Die `braze_id` wird von Braze automatisch zugewiesen, kann nicht bearbeitet werden und ist gerätespezifisch. | 
| Land | (string) Wir verlangen, dass die Ländercodes im [ISO-3166-1 alpha-2 Standard][17] an Braze übergeben werden. Unsere API wird sich bemühen, die in verschiedenen Formaten empfangenen Länder abzubilden. Zum Beispiel kann "Australien" auf "AU" abgebildet werden. Wenn die Eingabe jedoch nicht mit einem bestimmten [ISO-3166-1 alpha-2 Standard][17] übereinstimmt, wird der Länderwert auf `NULL` gesetzt. <br><br>Wenn Sie `country` für einen Benutzer durch CSV-Import oder API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden. |
| current_location | (Objekt) der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum, an dem der Benutzer die App zum ersten Mal verwendet hat) String im ISO 8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (Datum, an dem der Benutzer die App zuletzt benutzt hat) String im ISO 8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| Geburtsdatum | (Geburtsdatum) Zeichenfolge im Format "JJJJ-MM-TT", zum Beispiel 1980-12-21. |
| E-Mail | (Zeichenfolge) |
| email_subscribe | (string) Verfügbare Werte sind "opted_in" (explizit für den Erhalt von E-Mail-Nachrichten registriert), "unsubscribed" (explizit für den Erhalt von E-Mail-Nachrichten abgemeldet) und "subscribed" (weder ein- noch abgemeldet).  |
| email_open_tracking_disabled |(boolesch) `true` oder `false` akzeptiert. Setzen Sie diese Option auf `true`, um zu verhindern, dass das Tracking-Pixel für geöffnete E-Mails zu allen zukünftigen E-Mails an diesen Benutzer hinzugefügt wird.|
| email_click_tracking_disabled |(boolesch) `true` oder `false` akzeptiert. Setzen Sie diese Option auf `true`, um das Klick-Tracking für alle Links in einer zukünftigen E-Mail an diesen Benutzer zu deaktivieren.|
| external_id | (string) Ein eindeutiger Bezeichner für ein Benutzerprofil. Nach der Zuweisung eines `external_id` wird das Benutzerprofil auf allen Geräten des Benutzers identifiziert. Wenn Sie einem unbekannten Benutzerprofil zum ersten Mal eine externe_id zuweisen, werden alle bestehenden Benutzerprofildaten in das neue Benutzerprofil migriert. |
| facebook | Hash mit einem der folgenden Werte: `id` (String), `likes` (Array von Strings), `num_friends` (Ganzzahl). |
| first_name | (Zeichenfolge) |
| Geschlecht | (Zeichenfolge) "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen) oder null (unbekannt). |
| home_city | (Zeichenfolge) |
| Sprache | (Zeichenkette) verlangen wir, dass die Sprache im [ISO-639-1-Standard][24] an Braze übergeben wird. Die unterstützten Sprachen finden Sie in unserer [Liste der akzeptierten Sprachen][2].<br><br>Wenn Sie `language` für einen Benutzer durch CSV-Import oder API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden. |
| last_name | (Zeichenfolge) |
| marked_email_as_spam_at | (string) Datum, an dem die E-Mail des Benutzers als Spam markiert wurde. Erscheint im Format ISO 8601 oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| Telefon | (string) Wir empfehlen, die Telefonnummern im [E.164](https://en.wikipedia.org/wiki/E.164) Format anzugeben. Einzelheiten finden Sie unter [Benutzertelefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (string) Verfügbare Werte sind "opted_in" (explizit für den Empfang von Push-Nachrichten registriert), "unsubscribed" (explizit von Push-Nachrichten abgemeldet) und "subscribed" (weder ein- noch abgemeldet).  |
| push_tokens | Array von Objekten mit `app_id` und `token` string. Sie können optional eine `device_id` für das Gerät angeben, mit dem dieses Token verbunden ist, zum Beispiel `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| subscription_groups| Array von Objekten mit `subscription_group_id` und `subscription_state` String, zum Beispiel `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Verfügbare Werte für `subscription_state` sind "abonniert" und "abgemeldet".|
| time_zone | (string) Der Name der Zeitzone aus der [IANA-Zeitzonendatenbank][26] (z. B. "America/New_York" oder "Eastern Time (US & Canada)"). Es werden nur gültige Zeitzonenwerte eingestellt. |
| Twitter | Hash mit einem der folgenden Werte: `id` (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sprachwerte, die explizit über diese API festgelegt werden, haben Vorrang vor den Gebietsschema-Informationen, die Braze automatisch vom Gerät erhält.

####  Benutzerattribut Beispielanfrage

Dieses Beispiel enthält zwei Benutzerattribut-Objekte mit den erlaubten 75 Anfragen pro API-Aufruf.

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1-Codes"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 Zeitcode Wiki"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1-Codes"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
