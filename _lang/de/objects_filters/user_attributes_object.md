---
nav_title: "Nutzer:innen Attribute Objekt"
article_title: "API Nutzer:innen Attribute Objekt"
page_order: 11
page_type: reference
description: "Dieser referenzierte Artikel erläutert die verschiedenen Komponenten des Objekts Nutzer:in."

---

# Nutzer:innen Attribute Objekt

> Eine API-Anfrage mit einem beliebigen Feld im Attribute-Objekt erstellt oder aktualisiert ein Attribut dieses Namens mit dem angegebenen Wert im angegebenen Nutzerprofil. 

Verwenden Sie die Feldnamen des Braze-Benutzerprofils (wie nachfolgend aufgelistet oder alle im Abschnitt für [Braze-Benutzerprofilfelder](#braze-user-profile-fields) aufgelisteten), um diese speziellen Werte im Benutzerprofil im Dashboard zu aktualisieren, oder fügen Sie Ihre eigenen angepassten Attributdaten für den Benutzer hinzu.

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
- [Nutzer-Aliasse]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

Um ein Attribut des Profils zu entfernen, setzen Sie es auf `null`. Einige Felder, wie `external_id` und `user_alias` können nicht mehr entfernt werden, nachdem sie einem Nutzerprofil hinzugefügt wurden.

#### Nur bestehende Profile aktualisieren

Wenn Sie nur bestehende Nutzerprofile in Braze aktualisieren möchten, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Hauptteil Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Nutzerprofil, wenn das `external_id` nicht bereits existiert.

{% alert note %}
Wenn Sie über den Endpunkt `/users/track` ein Nutzerprofil erstellen, das nur aus Aliasen besteht, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das Profil, das nur einen Alias enthält, nicht erstellt.
{% endalert %}

#### Push-Token importieren

Bevor Sie Push-Tokens nach Braze importieren, überprüfen Sie, ob Sie das müssen. Wenn die SDKs von Braze eingerichtet sind, verarbeiten sie Push-Tokens automatisch, ohne dass sie über die API hochgeladen werden müssen.

Wenn Sie sie über die API hochladen müssen, können sie entweder für identifizierte Nutzer:innen oder anonyme Nutzer:innen hochgeladen werden. Das bedeutet, dass entweder ein `external_id` vorhanden sein muss, oder die anonymen Nutzer:innen müssen das `push_token_import` Flag auf `true` gesetzt haben. 

{% alert note %}
Beim Importieren von Push-Tokens aus anderen Systemen ist nicht immer eine `external_id` verfügbar. Um die Kommunikation mit diesen Nutzern während der Umstellung auf Braze aufrechtzuerhalten, können Sie die Legacy-Token für anonyme Nutzer:innen importieren, ohne `external_id` anzugeben, indem Sie `push_token_import` als `true` angeben.
{% endalert %}

Wenn Sie `push_token_import` als `true` angeben:

* `external_id` und `braze_id` sollten **nicht** angegeben werden.
* Das Attribut-Objekt **muss** ein Push-Token enthalten
* Wenn das Token bereits in Braze vorhanden ist, wird die Anfrage ignoriert. Andernfalls erstellt Braze ein temporäres, anonymes Nutzerprofil für jedes Token, damit Sie diesen Personen weiterhin Nachrichten schicken können.

Nach dem Import, wenn jeder Nutzer die Braze-fähige Version Ihrer App startet, verschiebt Braze das importierte Push-Token automatisch in sein Nutzerprofil und bereinigt das temporäre Profil.

Braze sucht einmal im Monat nach anonymen Profilen mit dem Kennzeichen `push_token_import`, die kein Push-Token haben. Wenn das anonyme Profil nicht mehr über einen Push-Token verfügt, löschen wir das Profil. Wenn das anonyme Profil jedoch noch einen Push-Token hat, was darauf hindeutet, dass der tatsächliche Nutzer sich noch nicht mit diesem Push-Token am Gerät angemeldet hat, unternehmen wir nichts.

Weitere Informationen finden Sie unter [Migration von Push-Tokens](#migrating-push-tokens).

#### Angepasste Attribut-Datenarten

Die folgenden Datenarten können als angepasstes Attribut gespeichert werden:

| Datentyp | Anmerkungen |
| --- | --- |
| Arrays | Angepasste Attribut-Arrays werden unterstützt. Wenn Sie ein Element zu einem angepassten Attribut-Array hinzufügen, wird das Element an das Ende des Arrays angehängt, es sei denn, es ist bereits vorhanden. In diesem Fall wird es von seiner aktuellen Position an das Ende des Arrays verschoben.<br><br>Wenn zum Beispiel das Array `['hotdog','hotdog','hotdog','pizza']` importiert wurde, wird es im Array-Attribut als `['hotdog', 'pizza']` angezeigt, da nur eindeutige Werte unterstützt werden.<br><br>Sie können nicht nur die Werte eines Arrays setzen, indem Sie etwas wie `"my_array_custom_attribute":[ "Value1", "Value2" ]` sagen, sondern auch Werte zu bestehenden Arrays hinzufügen, indem Sie etwas wie `"my_array_custom_attribute" : { "add" : ["Value3"] },` tun, oder Werte aus einem Array entfernen, indem Sie etwas wie `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>Die Höchstzahl an Elementen in angepassten Attribut-Arrays ist standardmäßig auf 25 festgelegt, kann aber für ein einzelnes Array auf bis zu 100 erhöht werden. Weitere Informationen finden Sie unter [Arrays]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays). |
| Array von Objekten | Array of Objects ermöglicht es Ihnen, eine Liste von Objekten zu definieren, wobei jedes Objekt eine Reihe von Attributen enthält. Dies kann nützlich sein, wenn Sie mehrere Datensätze mit verwandten Daten für einen Nutzer:innen speichern müssen, z.B. Hotelaufenthalte, Kaufverläufe oder Vorlieben. <br><br> Sie können zum Beispiel ein angepasstes Attribut für ein Nutzerprofil mit dem Namen `hotel_stays` definieren. Dieses angepasste Attribut kann als Array definiert werden, in dem jedes Objekt einen separaten Aufenthalt darstellt, mit Attributen wie `hotel_name`, `check_in_date`, `nights_stayed`. Weitere Einzelheiten finden Sie in [diesem Beispiel](#array-of-objects-example). |
| Boolesche Werte | `true` oder `false` |
| Daten | Muss im Format [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) oder in einem der folgenden Formate gespeichert werden: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Beachten Sie, dass "T" ein Zeitbezeichner und kein Platzhalter ist und nicht geändert oder entfernt werden sollte. <br><br>Zeitattribute ohne Zeitzone sind standardmäßig auf Mitternacht UTC eingestellt (und werden auf dem Dashboard als das Äquivalent zu Mitternacht UTC in der Zeitzone des Unternehmens formatiert). <br><br> Ereignisse mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt. <br><br> Bei regulären angepassten Attributen speichert Braze, wenn das Jahr kleiner als 0 oder größer als 3000 ist, diese Werte als Strings auf den Nutzer:innen. |
| Gleitkommazahlen | Gleitkommazahlen für angepasste Attribute sind positive oder negative Zahlen mit einem Dezimalpunkt. Sie können beispielsweise Gleitkommazahlen verwenden, um Kontostände oder Nutzer:innen-Bewertungen für Produkte oder Dienste zu speichern. |
| Ganze Zahlen | Ganzzahlige angepasste Attribute können um positive oder negative ganze Zahlen erhöht werden, indem Sie ihnen ein Objekt mit dem Feld "inc" und dem Wert, um den sie erhöht werden sollen, zuweisen. <br><br>Beispiel: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Verschachtelte angepasste Attribute | Verschachtelte angepasste Attribute definieren eine Gruppe von Attributen als Eigenschaft eines anderen Attributs. Wenn Sie ein angepasstes Attribut-Objekt definieren, legen Sie eine Reihe von zusätzlichen Attributen für dieses Objekt fest. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/). |
| Strings | Angepasste String Attribute sind Zeichenfolgen, die zum Speichern von Textdaten verwendet werden. Sie können zum Beispiel Strings verwenden, um Vor- und Nachnamen, E-Mail-Adressen oder Präferenzen zu speichern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Informationen darüber, wann Sie ein angepasstes Event und wann Sie ein angepasstes Attribut verwenden sollten, finden Sie in unserer Dokumentation zu [angepassten Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) und [angepassten Attributen]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).
{% endalert %}

##### Beispiel für ein Objekt-Array 

Mit diesem Array von Objekten können Sie Segmente auf der Grundlage bestimmter Kriterien innerhalb der Aufenthalte erstellen und Ihre Nachrichten anhand der Daten der einzelnen Aufenthalte mit Liquid-Templates personalisieren.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### Felder des Nutzerprofils von Braze {#braze-user-profile-fields}

{% alert important %}
Bei den folgenden Feldern des Nutzerprofils wird zwischen Groß- und Kleinschreibung unterschieden. Achten Sie also darauf, dass Sie diese Felder in Kleinbuchstaben referenzieren.
{% endalert %}

| Feld Nutzer:in | Spezifikation des Datentyps |
| ---| --- |
| alias_name | (String) |
| alias_label | (String) |
| braze_id | (String, optional) Wenn ein Nutzerprofil vom SDK erkannt wird, wird ein anonyme Nutzer:in-Profil mit einem zugehörigen `braze_id` erstellt. Die `braze_id` wird von Braze automatisch zugewiesen, kann nicht bearbeitet werden und ist gerätespezifisch. | 
| Land | (String) Wir verlangen, dass die Ländercodes im [ISO-3166-1 alpha-2 Standard](http://en.wikipedia.org/wiki/ISO_3166-1) an Braze übergeben werden. Unsere API wird sich bemühen, die in verschiedenen Formaten empfangenen Länder abzubilden. Zum Beispiel kann "Australien" auf "AU" abgebildet werden. Wenn die Eingabe jedoch nicht mit einem bestimmten [ISO-3166-1 alpha-2 Standard](http://en.wikipedia.org/wiki/ISO_3166-1) übereinstimmt, wird der Länderwert auf `NULL` gesetzt. <br><br>Wenn Sie `country` für einen Nutzer:innen per CSV-Import oder API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden. |
| current_location | (object) Der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum, an dem der Nutzer:innen die App zum ersten Mal benutzt hat) String im Format ISO 8601 oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (Datum, an dem der Nutzer:innen die App zuletzt benutzt hat) String im Format ISO 8601 oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| Geburtsdatum | (Geburtsdatum) String im Format "JJJJ-MM-TT", zum Beispiel 1980-12-21. |
| E-Mail | (String) |
| email_subscribe | (String) Verfügbare Werte sind "opted_in" (explizit für den Erhalt von E-Mail-Nachrichten registriert), "abgemeldet" (explizit gegen E-Mail-Nachrichten) und "abonniert" (weder Opt-in noch Opt-out).  |
| email_open_tracking_disabled |(boolesch) `true` oder `false` akzeptiert. Setzen Sie diese Option auf `true`, um zu verhindern, dass das Tracking-Pixel für die Öffnung zu allen zukünftigen E-Mails hinzugefügt wird, die an diese Nutzer:innen gesendet werden. Nur für SparkPost und SendGrid verfügbar.|
| email_click_tracking_disabled |(boolesch) `true` oder `false` akzeptiert. Setzen Sie diese Option auf `true`, um das Tracking von Klicks für alle Links in einer zukünftigen E-Mail an diesen Nutzer:innen zu deaktivieren. Nur für SparkPost und SendGrid verfügbar.|
| external_id | (String) Ein eindeutiger Bezeichner für ein Nutzerprofil. Nach Zuweisung eines `external_id` wird das Nutzerprofil auf allen Geräten eines Nutzers:innen identifiziert. Bei der ersten Instanz, in der Sie einem unbekannten Nutzerprofil eine external_id zuweisen, werden alle vorhandenen Nutzerdaten in das neue Nutzerprofil migriert. |
| Facebook | Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| first_name | (String) |
| Geschlecht | (String) "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen) oder nil (unbekannt). |
| home_city | (String) |
| Sprache | (String) verlangen wir, dass die Sprache im [ISO-639-1-Standard](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) an Braze übergeben wird. Die unterstützten Sprachen finden Sie in unserer [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/).<br><br>Wenn Sie `language` für einen Nutzer:innen per CSV-Import oder API einstellen, verhindert Braze, dass diese Informationen automatisch über das SDK erfasst werden. |
| last_name | (String) |
| marked_email_as_spam_at | (String) Datum, an dem die E-Mail des Nutzers:in als Spam markiert wurde. Erscheint im Format ISO 8601 oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| Telefon | (String) Wir empfehlen die Angabe von Telefonnummern im [E.164](https://en.wikipedia.org/wiki/E.164) Format anzugeben. Weitere Informationen finden Sie unter [Nutzer:innen Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting).|
| push_subscribe | (String) Verfügbare Werte sind "opted_in" (explizit für den Empfang von Push-Nachrichten registriert), "abgemeldet" (explizit von Push-Nachrichten abgemeldet) und "abonniert" (weder Opt-in noch abgemeldet).  |
| push_tokens | Array von Objekten mit `app_id` und `token` String. Sie können optional eine `device_id` für das Gerät angeben, mit dem dieses Token verbunden ist, z.B. `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| subscription_groups| Array von Objekten mit `subscription_group_id` und `subscription_state` String, zum Beispiel `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Verfügbare Werte für `subscription_state` sind "Abonnent:in" und "abgemeldet".|
| time_zone | (String) Der Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (zum Beispiel "America/New_York" oder "Eastern Time (US & Canada)"). Es werden nur gültige Zeitzonenwerte eingestellt. |
| Twitter | Hash mit einem der folgenden Werte: `id` (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sprachwerte, die explizit über diese API festgelegt werden, haben Vorrang vor den Gebietsschema-Informationen, die Braze automatisch vom Gerät erhält.

####  Beispiel für eine Anfrage zum Attribut Nutzer:in

Dieses Beispiel enthält vier Attribut-Objekte für Nutzer:innen, von insgesamt 75 zulässigen Attribut-Objekten pro API-Aufruf.

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

## Migration von Push-Tokens

Wenn Sie vor der Integration von Braze bereits Push-Benachrichtigungen versendet haben, entweder selbst oder über einen anderen Anbieter, ist es mit der Push-Token Migration zulässig, weiterhin Push-Benachrichtigungen an Ihre Nutzer:innen mit registrierten Push-Token zu senden.

### Automatische Migration über SDK

Nachdem Sie [das Braze SDK integriert haben]({{site.baseurl}}/developer_guide/sdk_integration/), werden die Push-Token für Ihre Opt-in Nutzer:innen automatisch migriert, wenn sie Ihre App das nächste Mal öffnen. Bis dahin können Sie diesen Nutzer:innen keine Push-Benachrichtigungen über Braze senden.

Alternativ können Sie [Ihre Push-Token auch manuell migrieren](#manual-migration-via-api), was eine schnellere erneute Interaktion mit Ihren Nutzer:innen zulässt.

#### Überlegungen zum Internet Token

Aufgrund der Natur von Web-Push-Tokens sollten Sie bei der Implementierung von Push für das Internet Folgendes beachten:

|Betrachtung|Details|
|----------------------|------------|
| **Service-Teammitglieder**  | Standardmäßig sucht das Internet SDK unter `./service-worker` nach einem Service-Teammitglied, es sei denn, es ist eine andere Option angegeben, wie `manageServiceWorkerExternally` oder `serviceWorkerLocation`. Wenn Ihr Service-Teammitglied nicht richtig eingerichtet ist, kann dies dazu führen, dass Push-Token für Ihre Nutzer:innen ablaufen. |
| **Abgelaufene Token**   | Wenn ein Nutzer:innen innerhalb von 60 Tagen keine Internetsitzung gestartet hat, verfällt sein Push-Token. Da Braze abgelaufene Push-Token nicht migrieren kann, müssen Sie einen [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) senden, um sie erneut zu engagieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Manuelle Migration über APIs

Bei der manuellen Push-Token Migration werden diese zuvor erstellten Schlüssel über die API in Ihre Braze Plattform importiert.

Programmatische Migration von iOS- (APNs) und Android- (FCM) Token auf Ihre Plattform mit Hilfe des [Endpunkts`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Sie können sowohl identifizierte Nutzer:in (Nutzer mit einer zugehörigen externen ID) als auch anonyme Nutzer:innen (Nutzer ohne externe ID) migrieren.

Geben Sie während der Push-Token Migration die `app_id` Ihrer App an, um das entsprechende Push-Token mit der entsprechenden App zu verknüpfen. Jede App (iOS, Android, etc.) hat ihre eigene `app_id`, die Sie im Abschnitt **Identifikation** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) finden. Achten Sie darauf, dass Sie die richtige Plattform `app_id` verwenden.

{% alert important %}
Es ist nicht möglich, Web-Push-Tokens über die API zu migrieren. Das liegt daran, dass Web-Push-Tokens nicht demselben Schema entsprechen wie andere Plattformen. 

<br>Wenn Sie versuchen, Web-Push-Tokens programmatisch zu migrieren, wird möglicherweise eine Fehlermeldung wie die folgende angezeigt: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Als Alternative zur API-Migration empfehlen wir Ihnen, das SDK zu integrieren und zuzulassen, dass sich Ihre Token-Basis auf natürliche Weise neu füllt.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
Für identifizierte Nutzer:innen setzen Sie das Kennzeichen `push_token_import` auf `false` (oder lassen den Parameter weg) und geben die Werte `external_id`, `app_id` und `token` im Objekt `attributes` des Nutzers an. 

Zum Beispiel:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
Beim Importieren von Push-Tokens aus anderen Systemen ist nicht immer eine `external_id` verfügbar. In diesem Fall setzen Sie das Kennzeichen `push_token_import` auf `true` und geben die Werte `app_id` und `token` an. Braze erstellt für jeden Token ein temporäres, anonymes Nutzerprofil, damit Sie diesen Personen weiterhin Nachrichten schicken können. Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert.

Zum Beispiel:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

Wenn der anonyme Nutzer:in nach dem Import die Braze-fähige Version Ihrer App startet, verschiebt Braze das importierte Push-Token automatisch in sein Nutzerprofil und bereinigt das temporäre Profil.

Braze sucht einmal im Monat nach anonymen Profilen mit dem Kennzeichen `push_token_import`, die kein Push-Token haben. Wenn das anonyme Profil nicht mehr über einen Push-Token verfügt, löschen wir das Profil. Wenn das anonyme Profil jedoch immer noch ein Push-Token hat, was darauf hindeutet, dass der tatsächliche Nutzer sich noch nicht mit dem besagten Push-Token bei dem Gerät angemeldet hat, unternehmen wir nichts.
{% endtab %}
{% endtabs %}

### Importieren von Android Push-Tokens

{% alert important %}
Die folgenden Überlegungen gelten nur für Android Apps. iOS Apps benötigen diese Schritte nicht, da diese Plattform nur ein Framework für die Anzeige von Push hat und Push-Benachrichtigungen sofort gerendert werden, solange Braze über die notwendigen Push-Token und Zertifikate verfügt.
{% endalert %}

Wenn Sie Android Push-Benachrichtigungen an Ihre Nutzer:innen senden müssen, bevor die Braze SDK-Integration abgeschlossen ist, verwenden Sie Schlüssel-Wert-Paare, um Push-Benachrichtigungen zu validieren. 

Sie müssen über einen Empfänger verfügen, der Push-Nutzdaten verarbeiten und anzeigen kann. Um den Empfänger der Push-Nutzdaten zu benachrichtigen, fügen Sie der Kampagne die erforderlichen Schlüssel-Wert-Paare hinzu. Die Werte dieser Paare hängen von dem Push-Partner ab, den Sie vor Braze verwendet haben.

{% alert note %}
Bei einigen Anbietern von Push-Benachrichtigungen muss Braze die Schlüssel-Wert-Paare glätten, damit sie richtig interpretiert werden können. Um Schlüssel-Wert-Paare für eine bestimmte Android App zu reduzieren, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}