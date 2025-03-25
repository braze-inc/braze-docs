---
nav_title: Schlüssel-Werte-Paare
article_title: Schlüssel-Werte-Paare
page_order: 4
description: "Dieser Artikel behandelt Schlüssel-Wert-Paare und wie man mit ihnen zusätzliche Nutzdaten an Benutzergeräte sendet."
channel:
  - push
  - in-app messages
  - content cards

---

# Schlüssel-Wert-Paare

> Mit Braze können Sie zusätzliche Nutzdaten mittels Schlüssel-Wert-Paaren an Benutzergeräte senden. Diese Funktion ist bei Push-, In-App-, E-Mail- und Content-Card-Nachrichten verfügbar. 

Mit Schlüssel-Wert-Paaren können Sie Ihren Nachrichten strukturierte Metadaten hinzufügen. Diese zusätzlichen Nutzdaten können Nachrichten um Kontextinformationen ergänzen, die beeinflussen können, wie eine Nachricht dargestellt oder verarbeitet wird.

Da es sich bei den Schlüssel-Wert-Paaren um Metadaten handelt, sind diese Daten für den Empfänger nicht unbedingt sichtbar, können aber von den angeschlossenen Systemen oder Prozessen verwendet werden, um die Bearbeitung von Nachrichten anzupassen. 

Jedes Paar besteht aus:

- **Schlüssel:** Die Kennung (Beispiel: `utm_source`)
- **Wert:** Die zugehörigen Daten (Beispiel: `newsletter`)

## Anwendungsfälle

Hier einige Anwendungsbeispiele für die Ergänzung von Metadaten mit Schlüssel-Wert-Paaren:

1. **Trackingparameter:** Anhängen von UTM-Parametern für Analysezwecke
   - Schlüssel: `utm_campaign`
   - Wert: `spring_sale`
2. **Benutzerdefinierte Tags:** Hinzufügen von Tags für die interne Weiterleitung oder Kategorisierung
   - Schlüssel: `priority`
   - Wert: `high`
3. **Auslöser:** Metadaten, die zum Auslösen oder Anpassen von In-App-Verhaltensweisen verwendet werden
   - Schlüssel: `deep_link`
   - Wert: `app://promo-page`

## Push-Benachrichtigungen

Schlüssel-Wert-Paare können zu Android-, iOS- und Web-Push-Benachrichtigungen hinzugefügt werden. Sie können Schlüssel-Wert-Paare verwenden, um interne Metriken und App-Inhalte zu aktualisieren oder die Eigenschaften von Push-Benachrichtigungen wie Priorisierung, Lokalisierung und Töne anzupassen.

Wählen Sie im Message Composer die Registerkarte **Einstellungen**, klicken Sie auf **Neues Paar hinzufügen** und geben Sie Ihre Schlüssel-Wert-Paare an.

### iOS

Der Apple Push-Benachrichtigungsdienst (APNs) unterstützt die Einstellung von Benachrichtigungspräferenzen und das Senden von benutzerdefinierten Daten unter Verwendung von Schlüssel-Wert-Paaren. APNs verwenden die Apple-Bibliothek ```aps```, die vorgegebene Schlüssel und Werte enthält, die die Meldungseigenschaften bestimmen.

##### APS-Bibliothek

| Schlüssel  | Wertetyp  | Wert Beschreibung |
|-------------------|-----------------------------|----------------------------------|
| Alarm             | String oder Wörterbuchobjekt | Bei String-Eingaben wird eine Warnung mit dem String als Nachricht und den Schaltflächen Schließen und Anzeigen angezeigt; bei Eingaben ohne String wird je nach den Child-Eigenschaften der Eingabe eine Warnung oder ein Banner angezeigt |
| Badge             | Nummer                      | Legt die Zahl fest, die auf dem App-Symbol angezeigt wird                                                                                                                              |
| Sound             | String                      | Der Name der Tondatei, die als Warnung abgespielt werden soll. Sie muss sich im Bundle der App oder im Ordner ```Library/Sounds``` befinden.                                                                                    |
| Inhalt verfügbar | Nummer                      | Eingabewerte von 1 signalisieren der App die Verfügbarkeit neuer Informationen bei Beginn und Wiederaufnahme der Sitzung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Bibliothek der Alert-Eigenschaften

| Schlüssel            | Wertetyp               | Wert Beschreibung                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Titel         | String                   | Eine kurze Zeichenfolge, die die Apple Watch kurz als Teil einer Benachrichtigung anzeigt                                                                    |
| body         | String                   | Der Inhalt der Push-Benachrichtigung                                                                                                                  |
| titel-loc-key  | String oder Null           | Ein Schlüssel, der den Titelstring für die aktuelle Lokalisierung aus der Datei ```Localizable.strings``` abruft.                                          |
| titel-ort-args | Array von Zeichenketten oder null | String-Werte, die anstelle der Formatspezifikationen für die Titellokalisierung in title-loc-key erscheinen können.                                           |
| action-loc-key | array of string oder null  | Falls vorhanden, legt die angegebene Zeichenkette die Lokalisierung der Schaltflächen Schließen und Ansicht fest.                                                         |
| loc-key        | String oder Null           | Ein Schlüssel, der die Hinweismeldung für die aktuelle Lokalisierung aus der Datei ```Localizable.strings``` abruft.                                  |
| loc-args       | Array von Zeichenketten         | String-Werte, die anstelle der Lokalisierungsformatspezifikationen in loc-key erscheinen können.                                                       |
| launch-image   | Zeichenketten                  | Der Name einer Bilddatei im App-Bundle, die als Startbild verwendet werden soll, wenn Benutzer auf die Aktionsschaltfläche tippen oder den Aktionsschieber bewegen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der Braze Nachrichten-Editor erstellt automatisch den Schlüssel **Alarm** und **seine Eigenschaften** **content-available**, **sound** und **category**. 

Diese Werte können auf der Registerkarte **Einstellungen** eingegeben werden, wenn Sie eine Push-Nachricht erstellen. Gehen Sie auf **Hinweisoptionen** und wählen Sie einen Schlüssel aus dem Verzeichnis, der automatisch in einen neuen Schlüssel-Wert-Eintrag eingefügt werden soll.

![][16]
{% raw %}
Wenn Braze eine Push-Benachrichtigung an APNs sendet, wird die Payload als JSON formatiert.

**Einfache Payload**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Komplexe Payload**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Benutzerdefinierte Schlüssel-Wert-Paare

Zusätzlich zu den Werten aus der ```aps```-Bibliothek können Sie auch benutzerdefinierte Schlüssel-Wert-Paare an das Benutzergerät senden. Die Werte in diesen Paaren sind auf primitive Typen beschränkt: dictionary (Objekt), array, string, number und Boolean.

![][17]

Zu den Anwendungsfällen für benutzerdefinierte Schlüssel-Wert-Paare gehören u. a. die Speicherung interner Kennzahlen und die Festlegung des Kontexts für die Benutzeroberfläche. Braze ermöglicht es Ihnen, zusätzliche Schlüssel-Wert-Paare zusammen mit einer Push-Benachrichtigung zu senden, die Sie dann über Ihre Anwendung mit dem [Extras-Schlüssel][1] verwenden können. Wenn Sie einen anderen Schlüssel verwenden möchten, stellen Sie sicher, dass Ihre Anwendung mit diesem Schlüssel umgehen kann.

{% alert warning %}
Sie sollten es vermeiden, in Ihrer Anwendung einen Schlüssel oder ein Wörterbuch der obersten Ebene mit dem Namen "ab" zu verwenden.
{% endalert %}

Apple rät dazu, keine Kundeninformationen oder andere sensible Daten als benutzerdefinierte Payload zu verwenden. Darüber hinaus empfiehlt Apple, dass jede Aktion im Zusammenhang mit einer Warnmeldung keine Daten auf einem Gerät löschen sollte.

{% alert warning %}
Wenn Sie die HTTP/2-Anbieter-API verwenden, dürfen Payloads, die Sie an APNs senden, max. 4096 Bytes groß sein. Die bisherige Binärschnittstelle, die demnächst eingestellt wird, unterstützt nur 2048 Byte Payload.
{% endalert %}

###### Per API ausgelöste Kampagnen

Mit Braze können Sie benutzerdefinierte Paare aus Strings und Schlüsselwerten senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-gestützten und planmäßigen API-gestützten Kampagnen zuzugreifen, legen Sie im Dashboard einen Schlüssel als "example_key" und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies führt zu einer Ausgabe in der Entwicklerkonsole von `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze erlaubt es Ihnen, zusätzliche Daten in Push-Benachrichtigungen unter Verwendung von Schlüssel-Wert-Paaren zu senden.

##### Daten-Nutzlast

Ähnlich wie bei iOS Push können Sie benutzerdefinierte Schlüssel-Wert-Paare an das Gerät eines Benutzers senden.

Zu den Anwendungsfällen für benutzerdefinierte Schlüssel-Wert-Paare gehören das Führen interner Metriken und das Festlegen des Kontexts für die Benutzeroberfläche, aber sie können für jeden beliebigen Zweck verwendet werden.

{% alert important %}
Das Backend Ihrer Anwendung muss in der Lage sein, benutzerdefinierte Schlüssel-Wert-Paare zu verarbeiten, damit die Daten-Nutzlast ordnungsgemäß funktioniert.
{% endalert %}

###### Per API ausgelöste Kampagnen

Mit Braze können Sie benutzerdefinierte Paare aus Strings und Schlüsselwerten senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-gestützten und planmäßigen API-gestützten Kampagnen zuzugreifen, legen Sie im Dashboard einen Schlüssel als "example_key" und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies führt zu einer Ausgabe in der Entwicklerkonsole von `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### FCM-Nachrichtenoptionen

Android-Push-Benachrichtigungen können mit FCM-Nachrichtenoptionen weiter angepasst werden. Dazu gehören [Benachrichtigungspriorität][8], [Ton][10], Verzögerung, Lebensdauer und Ausblendbarkeit. Diese Werte können bei der Erstellung einer Push-Nachricht auf der Registerkarte **Einstellungen** angegeben werden. Unter [Erweiterte Einstellungen für Push-Benachrichtigungen][7] finden Sie weitere Anweisungen, wie Sie diese Optionen im Braze Message Composer einstellen können.

![][18]

### Stille Push-Benachrichtigungen

Eine stille Push-Benachrichtigung ist eine Push-Benachrichtigung, die keine Warnmeldung oder einen Ton enthält und dazu dient, die Oberfläche oder den Inhalt Ihrer App im Hintergrund zu aktualisieren. Diese Benachrichtigungen verwenden Schlüssel-Wert-Paare, um diese Aktionen der App im Hintergrund auszulösen. Stille Push-Benachrichtigungen unterstützen auch unsere [Deinstallationsüberwachung][4].

Vermarkter sollten testen, ob stille Push-Benachrichtigungen das erwartete Verhalten auslösen, bevor sie sie an die Nutzer ihrer App senden. Nachdem Sie Ihre stille Push-Benachrichtigung [für iOS][2] oder [Android][13] verfasst haben, stellen Sie sicher, dass Sie nur einen Testbenutzer ansprechen, indem Sie nach [externer Benutzer-ID][14] oder [E-Mail-Adresse][15] filtern.

Bei der Einführung der Kampagne sollten Sie sich vergewissern, dass Sie keine sichtbare Push-Benachrichtigung auf Ihrem Testgerät erhalten haben.

{% alert note %}
Das iOS-Betriebssystem kann [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) zu einigen Features (Deinstallationsverfolgung, Geofencing und Push-Storys) stummschalten. Beachten Sie, dass dadurch bestimmte Schwierigkeiten mit diesen Features entstehen können.
{% endalert %}

## In-App-Nachrichten

Um einer In-App-Nachricht ein Schlüssel-Wert-Paar hinzuzufügen, wählen Sie die Registerkarte **Einstellungen** im Message Composer, klicken auf **Neues Paar hinzufügen** und geben Ihre Schlüssel-Wert-Paare an.

![][21]

#### Per API ausgelöste Kampagnen

Mit Braze können Sie benutzerdefinierte Paare aus Strings und Schlüsselwerten senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-gestützten und planmäßigen API-gestützten Kampagnen zuzugreifen, legen Sie im Dashboard einen Schlüssel als "example_key" und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies führt zu einer Ausgabe in der Entwicklerkonsole von `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-Mails

Sowohl SparkPost als auch SendGrid unterstützt Schlüssel-Wert-Paare in E-Mails. Wenn Sie SendGrid verwenden, werden die Schlüssel-Wert-Paare als [eindeutige Argumente][11] gesendet. SendGrid erlaubt es Ihnen, eine unbegrenzte Anzahl von Schlüssel-Wert-Paaren mit bis zu 10.000 Byte Daten anzuhängen. Diese Schlüssel-Wert-Paare können Sie in den Posts des SendGrid [Event Webhook][12] einsehen.

{% alert note %}
Abgewiesene E-Mails geben keine Schlüssel-Wert-Paare an SparkPost oder SendGrid weiter.
{% endalert %}

![Tab Sendeinfo des Nachrichten-Editors für E-Mails in Braze.][22]

## Content-Cards

Um ein Schlüssel-Wert-Paar zu einer Inhaltskarte hinzuzufügen, gehen Sie im Braze Message Composer auf die Registerkarte **Einstellungen** und klicken Sie auf **Neues Paar hinzufügen**.

![Schlüssel-Wert-Paar zur Content-Card hinzufügen][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds
[11]: https://docs.sendgrid.com/for-developers/sending-email/unique-arguments
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}
