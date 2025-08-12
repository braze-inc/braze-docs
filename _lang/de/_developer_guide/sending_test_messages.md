---
nav_title: Versenden von Testnachrichten
article_title: Versenden von Testnachrichten
page_order: 4.1
description: "Dieser Referenzartikel behandelt das Senden von Testnachrichten für verschiedene Kanäle."

---

# Versenden von Test Nachrichten

> Bevor Sie eine Benachrichtigungskampagne an Ihre Benutzer senden, sollten Sie sie testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Das Erstellen und Versenden von Testnachrichten an ausgewählte Geräte oder Mitglieder Ihres Teams ist mit den Tools im Dashboard sehr einfach.

## Erstellen eines bestimmten Testsegments <a class="margin-fix" name="test-segment"></a>

Sobald Sie ein Testsegment eingerichtet haben, können Sie es verwenden, um **jeden** unserer Nachrichtenkanäle zu testen. Wenn der Vorgang richtig konfiguriert ist, muss er nur einmal durchgeführt werden.

Um ein Testsegment einzurichten, navigieren Sie zur Seite **Segmente** im Dashboard und erstellen ein neues Segment. Klicken Sie auf **Filter hinzufügen**, um einen der Testfilter auszuwählen, die Sie unten im Dropdown-Menü finden.

![Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Filter anzeigt.]({% image_buster /assets/img_archive/testmessages1.png %})

Zwei solcher Testfilter ermöglichen es Ihnen, Benutzer mit bestimmten E-Mail-Adressen oder externen [Benutzer-IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) auszuwählen.

![Dropdown-Menü mit mehreren Filtern, die unter der Überschrift "Testen" aufgeführt sind]({% image_buster /assets/img_archive/testmessages2.png %})

Die Filter für E-Mail-Adressen und externe Benutzer-IDs bieten jeweils drei Optionen:

  1) **"Gleich"** \- Diese Option sucht nach einer exakten Übereinstimmung mit der von Ihnen angegebenen E-Mail oder Benutzer-ID. Verwenden Sie diese Option, wenn Sie die Testkampagnen nur an Geräte senden möchten, die mit einer einzigen E-Mail oder Benutzer-ID verbunden sind.

  2) **"Ist nicht gleich"** \- Verwenden Sie diese Option, wenn Sie eine bestimmte E-Mail oder Benutzer-ID von Testkampagnen ausschließen möchten.

  3) **"Übereinstimmungen"** \- Damit werden Benutzer gefunden, deren E-Mail-Adressen oder Benutzer-IDs mit einem Teil des von Ihnen angegebenen Suchbegriffs übereinstimmen. Auf diese Weise können Sie nach Nutzern suchen, die eine "@yourcompany.com" Adresse haben, was es Ihnen erlaubt, Nachrichten an alle Mitglieder Ihres Teams zu senden.

Sie können mehrere bestimmte E-Mails auswählen, indem Sie die Option "Übereinstimmungen" verwenden und die E-Mail-Adressen mit einem dem Zeichen | voneinander trennen (z. B. "Übereinstimmungen" "email1@braze.com | email2@braze.com").

Diese Filter können auch in Kombination miteinander verwendet werden, um die Liste Ihrer Testnutzer einzugrenzen. Das Testsegment könnte zum Beispiel einen Filter für E-Mail-Adressen, der mit "@braze.com" übereinstimmt, und einen weiteren Filter, der nicht mit "sales@braze.com" übereinstimmt, enthalten. 

Nachdem Sie die Testfilter zu Ihrem Testsegment hinzugefügt haben, können Sie überprüfen, ob Sie nur die gewünschten Benutzer ausgewählt haben, indem Sie oben im Segmenteditor auf **Vorschau** klicken oder indem Sie die Benutzerdaten dieses Segments in eine CSV-Datei exportieren, indem Sie auf das Zahnradsymbol in der rechten Ecke des Editors klicken und aus dem Dropdown-Menü **CSV-Export aller Benutzerdaten** wählen.

![Abschnitt einer Braze Kampagne mit dem Titel "Segment-Details"]({% image_buster /assets/img_archive/testmessages3.png %})

>  Wenn Sie die Benutzerdaten des Segments in eine CSV-Datei exportieren, erhalten Sie ein möglichst genaues Bild davon, wer unter dieses Segment fällt. Die Registerkarte **Vorschau** stellt nur eine Auswahl der Benutzer im Segment dar und kann daher den Eindruck erwecken, dass nicht alle vorgesehenen Mitglieder ausgewählt wurden.

## Versenden von Push-Benachrichtigungen oder In-App-Nachrichten zum Testen <a class="margin-fix" name="push-inapp-test"></a>

Um Push-Benachrichtigungen oder In-App-Nachrichten zum Test zu versenden, müssen Sie Ihr zuvor erstelltes Testsegment adressieren. Beginnen Sie mit der Erstellung Ihrer Kampagne und folgen Sie den üblichen Schritten. Wenn Sie den Schritt **Zielbenutzer** erreichen, wählen Sie Ihr Testsegment aus dem Dropdown-Menü aus.

![Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Segmente anzeigt.]({% image_buster /assets/img_archive/test_segment.png %})

Bestätigen Sie Ihre Kampagne und starten Sie sie, um Ihre Push-Benachrichtigungen und In-App-Nachrichten zu testen.

>  Stellen Sie sicher, dass Sie im Abschnitt **Zeitplan** des Kampagnenkomponisten die Option **Erlauben, dass sich Benutzer erneut für den Erhalt der Kampagne qualifizieren können** auswählen, wenn Sie eine einzelne Kampagne verwenden möchten, um sich selbst mehr als einmal eine Testnachricht zu senden.

## Versenden einer E-Mail Nachricht zum Testen

Wenn Sie ausschließlich E-Mail-Nachrichten testen, müssen Sie nicht unbedingt ein Testsegment einrichten. Im ersten Schritt des Kampagnen-Composers, in dem Sie die E-Mail-Nachricht Ihrer Kampagne verfassen, klicken Sie auf **Test senden** und geben die E-Mail-Adresse ein, an die Sie eine Test-E-Mail senden möchten. 

![Braze Kampagne mit ausgewähltem Tab "Test senden"]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Sie können auch aktivieren oder deaktivieren, dass [TEST (oder SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) an Ihre Nachrichten angehängt wird.
{% endalert %}

## Testen über die Befehlszeile

Wenn Sie Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie alternativ die folgenden Beispiele für einzelnen Plattformen verwenden.

### Push-Tests mit iOS-Apps über cURL

Sie können eine einzelne Benachrichtigung über CURL und die [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) über das Terminal versenden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` - verfügbar unter **Einstellungen** > **API-Schlüssel**
- `YOUR_EXTERNAL_USER_ID` - verfügbar auf der Seite **Benutzer suchen** 
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befinden sich diese Seiten an einer anderen Stelle: <br>- **API-Schlüssel** finden Sie unter **Entwicklerkonsole** > **API-Einstellungen** <br>- **Benutzer suchen** finden Sie unter **Benutzer** > **Benutzersuche**
{% endalert %}

>  Die folgenden Beispiele zeigen die entsprechenden API-Endpunkte für Kunden in der Instanz `US-01`. Wenn Sie nicht auf dieser Instanz sind, sehen Sie in unserer [API-Dokumentation]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) nach, an welchen Endpunkt Sie Anfragen stellen müssen.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Push-Tests mit Android-Apps über cURL

Über cURL und die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) können Sie eine einzelne Benachrichtigung über das Terminal versenden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` (Gehen Sie zu **Einstellungen** > **API-Schlüssel**.)
- `YOUR_EXTERNAL_USER_ID` (Suchen Sie auf der Seite **Benutzer suchen** nach einem Profil).
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

>  Die folgenden Beispiele zeigen die entsprechenden API-Endpunkte für Kunden in der Instanz `US-01`. Wenn Sie nicht auf dieser Instanz sind, sehen Sie in unserer [API-Dokumentation]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) nach, an welchen Endpunkt Sie Anfragen stellen müssen.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Testen von Push mit Kindle-Anwendungen über cURL

Über cURL und die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) können Sie eine einzelne Benachrichtigung über das Terminal versenden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` - verfügbar auf der Seite **Entwicklungskonsole**
- `YOUR_EXTERNAL_USER_ID` - verfügbar auf der Seite **Benutzersuche** 
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Beschränkungen der Testnachrichten

Es gibt einige Situationen, in denen Testnachrichten nicht die gleichen Funktionen aufweisen wie der Start einer Kampagne oder eines Canvas für eine echte Gruppe von Benutzern. In diesen Fällen sollten Sie die Kampagne oder das Canvas für eine begrenzte Anzahl von Testbenutzern starten, um dieses Verhalten zu überprüfen.

- Wenn Sie das [Braze-Einstellungscenter]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) über **Testnachrichten** aufrufen, ist die Schaltfläche Senden ausgegraut.
- Der List-Unsubscribe-Header ist in den über die Testfunktion gesendeten E-Mails nicht enthalten.
- Für In-App-Nachrichten und Content-Cards muss der Zielnutzer über ein Push-Token für das Targeting-Gerät verfügen.

