# Versenden von Test Nachrichten

> Bevor Sie eine Benachrichtigungskampagne an Ihre Benutzer senden, sollten Sie sie testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Über das Dashboard können Sie Testnachrichten mit Push-Benachrichtigungen, In-App-Nachrichten (IAM) oder E-Mails erstellen und versenden.

## Versenden einer Testnachricht

### Schritt 1: Erstellen Sie ein bestimmtes Testsegment <a class="margin-fix" name="test-segment"></a>

Nachdem Sie ein Testsegment eingerichtet haben, können Sie es verwenden, um jeden Ihrer Messaging-Kanäle von Braze zu testen. Bei richtiger Einrichtung muss dies nur ein einziges Mal geschehen.

Um ein Testsegment einzurichten, gehen Sie zu **Segmente** und erstellen Sie ein neues Segment. Wählen Sie **Filter hinzufügen** und wählen Sie dann einen der Testfilter aus.

![Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Filter anzeigt.]({% image_buster /assets/img_archive/testmessages1.png %})

Mit Testfiltern können Sie sicherstellen, dass nur Nutzer:innen mit einer bestimmten E-Mail Adresse oder [externen ID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) die Nachricht erhalten.

![Dropdown-Menü mit mehreren Filtern, die unter der Überschrift "Testen" aufgeführt sind]({% image_buster /assets/img_archive/testmessages2.png %})

Sowohl die Filter für E-Mail-Adressen als auch für externe IDs bieten die folgenden Optionen:

| Operator          | Beschreibung |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Es wird nach einer genauen Übereinstimmung mit der von Ihnen angegebenen E-Mail oder Nutzer:in gesucht. Verwenden Sie diese Option, wenn Sie die Testkampagnen nur an Geräte senden möchten, die mit einer einzigen E-Mail oder Benutzer-ID verbunden sind. |
| `does not equal` | Verwenden Sie diese Option, wenn Sie eine bestimmte E-Mail oder Nutzer:innen-ID von Kampagnen ausschließen möchten. |
| `matches`     | So finden Sie Nutzer:innen, deren E-Mail-Adressen oder IDs mit einem Teil des von Ihnen angegebenen Suchbegriffs übereinstimmen. Damit können Sie nur die Nutzer:innen finden, die eine `@yourcompany.com` Adresse haben, was es Ihnen erlaubt, Nachrichten an alle Mitglieder Ihres Teams zu senden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Sie können mehrere bestimmte E-Mails auswählen, indem Sie die Option "`matches`" verwenden und die E-Mail-Adressen mit einem | Zeichen trennen. Zum Beispiel: "`matches`" "`email1@braze.com` | `email2@braze.com`". Sie können auch mehrere Operatoren miteinander kombinieren. Das Testsegment könnte zum Beispiel einen Filter für E-Mail-Adressen enthalten, der "`matches`" "`@braze.com`" und einen anderen Filter, der "`does not equal`" "`sales@braze.com`". 

Nachdem Sie die Testfilter zu Ihrem Testsegment hinzugefügt haben, können Sie überprüfen, ob sie funktionieren, indem Sie **Vorschau** auswählen oder indem Sie **Einstellungen** > **CSV-Export aller Nutzer:innen** wählen, um die Nutzerdaten dieses Segments in eine CSV-Datei zu exportieren.

![Abschnitt einer Braze Kampagne mit dem Titel "Segment-Details"]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
Der Export der Nutzerdaten des Segments in eine CSV-Datei ist die genaueste Überprüfungsmethode, da die Vorschau nur eine Stichprobe Ihrer Nutzer:innen zeigt und möglicherweise nicht alle Nutzer:innen umfasst.
{% endalert %}

### Schritt 2: Senden Sie die Nachricht

Sie können eine Nachricht über das Braze-Dashboard oder die Befehlszeile senden.

{% tabs local %}
{% tab Verwendung des Dashboards %}
{% subtabs %}
{% subtab push or in-app message %}
Um Push-Benachrichtigungen oder In-App-Nachrichten zum Test zu versenden, müssen Sie Ihr zuvor erstelltes Testsegment adressieren. Beginnen Sie mit der Erstellung Ihrer Kampagne und folgen Sie den üblichen Schritten. Wenn Sie den Schritt **Zielgruppen** erreichen, wählen Sie Ihr Testsegment aus dem Dropdown-Menü aus.

![Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Segmente anzeigt.]({% image_buster /assets/img_archive/test_segment.png %})

Bestätigen Sie Ihre Kampagne und starten Sie sie, um Ihre Push-Benachrichtigungen und In-App-Nachrichten zu testen.

{% alert note %}
Stellen Sie sicher, dass Sie im Abschnitt **Zeitplan** des Kampagnenkomponisten die Option **Erlauben, dass sich Benutzer erneut für den Erhalt der Kampagne qualifizieren können** auswählen, wenn Sie eine einzelne Kampagne verwenden möchten, um sich selbst mehr als einmal eine Testnachricht zu senden.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Wenn Sie ausschließlich E-Mail-Nachrichten testen, müssen Sie nicht unbedingt ein Testsegment einrichten. Im ersten Schritt des Kampagnen-Composers, in dem Sie die E-Mail-Nachricht Ihrer Kampagne verfassen, klicken Sie auf **Test senden** und geben die E-Mail-Adresse ein, an die Sie eine Test-E-Mail senden möchten. 

![Braze Kampagne mit ausgewähltem Tab "Test senden"]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Sie können auch aktivieren oder deaktivieren, dass [TEST (oder SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) an Ihre Nachrichten angehängt wird.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Verwenden der Befehlszeile %}
Alternativ können Sie eine einzelne Nachricht mit cURL und der [Braze Messaging API]({{site.baseurl}}/api/endpoints/messaging/) senden. Beachten Sie, dass diese Beispiele eine Anfrage über die Instanz `US-01` stellen. Um Ihre herauszufinden, referenzieren Sie die [API Endpunkte]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Ersetzen Sie Folgendes:

| Platzhalter         | Beschreibung                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Ihr Braze API-Schlüssel, der für die Authentifizierung verwendet wird. Gehen Sie in Braze zu **Einstellungen** > **API-Schlüssel**, um Ihren Schlüssel zu finden. |
| `EXTERNAL_USER_ID` | Die externe ID des Nutzers, mit der Sie Ihre Nachricht an einen bestimmten Nutzer:innen senden. Gehen Sie in Braze zu **Zielgruppe** > **Nutzer:innen suchen**, und suchen Sie dann nach einem Nutzer:in. |
| `CUSTOM_KEY`         | (Optional) Ein angepasster Schlüssel für zusätzliche Daten.              |
| `CUSTOM_VALUE`       | (Optional) Ein angepasster Wert, der Ihrem angepassten Schlüssel zugewiesen ist.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Test Einschränkungen

Es gibt einige Situationen, in denen Testnachrichten nicht die gleichen Funktionen aufweisen wie der Start einer Kampagne oder eines Canvas für eine echte Gruppe von Benutzern. In diesen Fällen sollten Sie die Kampagne oder das Canvas für eine begrenzte Anzahl von Testbenutzern starten, um dieses Verhalten zu überprüfen.

- Wenn Sie das [Braze-Einstellungscenter]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) über **Testnachrichten** aufrufen, ist der Button Senden ausgegraut.
- Die Kopfzeile list-unsubscribe ist in den von der Testnachrichten-Funktionalität gesendeten Nachrichten nicht enthalten.
- Für In-App-Nachrichten und Content-Cards muss die Zielgruppe Nutzer:innen über ein Push-Token für das Targeting-Gerät verfügen.
