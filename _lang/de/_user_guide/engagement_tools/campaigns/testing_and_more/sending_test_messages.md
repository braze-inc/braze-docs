---
nav_title: Test Nachrichten senden
article_title: Test Nachrichten senden
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Testnachrichten über die verschiedenen Braze-Kanäle senden und wie Sie benutzerdefinierte Ereigniseigenschaften oder Benutzerattribute einbinden."

---

# Test Nachrichten senden

> Bevor Sie eine Messaging-Kampagne an Ihre Nutzer:innen verschicken, empfehlen wir Ihnen, die Kampagne zu testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Sie können mit den Tools im Braze-Dashboard Testnachrichten erstellen und an ausgewählte Geräte oder Teammitglieder senden.

{% alert important %}
Stellen Sie sicher, dass Sie Ihren Kampagnenentwurf nach dem Testen speichern, damit Ihre Kampagne nicht gelöscht wird. Sie können Testnachrichten senden, ohne die Nachricht als Entwurf zu speichern.
{% endalert %}

## Schritt 1: Testnutzer:innen identifizieren

Bevor Sie Ihre Messaging-Kampagne testen, ist es wichtig, Ihre Testnutzer:innen zu identifizieren. Bei diesen Nutzern kann es sich entweder um bestehende IDs oder E-Mail-Adressen handeln oder um neue Nutzer:innen, die ausschließlich zum Testen von Messaging-Kampagnen verwendet werden. 

### Optional: Erstellen Sie eine Inhaltstestgruppe

Eine bequeme Möglichkeit, Ihre Testnutzer zu organisieren, ist die Erstellung einer [Content-Test-Gruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), die eine Gruppe von Nutzern umfasst, die Testnachrichten von Kampagnen erhalten werden. Sie können diese Testgruppe im Feld **Inhaltstestgruppen hinzufügen** unter **Test Empfänger:innen** in Ihrer Kampagne hinzufügen und Ihre Tests einführen, ohne einzelne Nutzer:innen zu erstellen oder hinzuzufügen.

## Schritt 2: Kanalspezifische Testnachrichten senden

Die Schritte zum Senden von Testnachrichten finden Sie im folgenden Abschnitt für Ihren jeweiligen Kanal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Bevor Sie Banner-Nachrichten in Braze testen können, müssen Sie eine Banner-Kampagne in Braze erstellen. Überprüfen Sie außerdem, ob die Platzierung, die Sie testen möchten, bereits [in Ihrer App oder Website vorhanden]({{site.baseurl}}/developer_guide/banners/placements) ist.
{% endalert %}

Nachdem Sie Ihre Banner Nachricht erstellt haben, können Sie eine Vorschau Ihres Banners anzeigen oder eine Testnachricht senden.

1. Entwerfen Sie Ihre Banner Nachricht.
2. Wählen Sie **Vorschau**, um eine Vorschau Ihres Banners anzuzeigen oder eine Testnachricht zu senden.
3. Um eine Nachricht zu testen, fügen Sie entweder eine Testgruppe oder einen oder mehrere einzelne Nutzer:innen als **Empfänger:innen** hinzu und wählen dann **Test senden**. 

Sie können Ihre Nachricht bis zu 5 Minuten lang auf dem Gerät sehen.

![Tab Vorschau des Banner Composers.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Denken Sie daran, dass Ihre Vorschau aufgrund von Unterschieden in der Hardware möglicherweise nicht mit der endgültigen Darstellung auf dem Gerät eines Nutzers:innen identisch ist.
{% endalert %}

### Test-Checkliste

- Ist Ihre Banner Kampagne einer Platzierung zugewiesen?
- Werden die Bilder und Medien auf den von Ihnen anvisierten Gerätetypen und Bildschirmgrößen wie erwartet angezeigt und funktionieren sie?
- Führen Ihre Links und Buttons die Nutzer:innen dorthin, wohin sie gehen sollen?
- Funktioniert das Liquid wie erwartet? Haben Sie einen Standard-Attributwert für den Fall vorgesehen, dass das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
Um einen Test entweder an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder an einzelne Benutzer zu senden, muss Push auf Ihren Testgeräten aktiviert sein und es müssen gültige Push-Token für den Testbenutzer registriert sein, bevor Sie den Test senden. Für iOS Nutzer:innen müssen Sie auf die Push-Benachrichtigung tippen, die von Braze gesendet wird, um die Content-Card für den Test anzuzeigen. Dieses Verhalten gilt nur für Test-Inhaltskarten.
{% endalert %}

Nachdem Sie Ihre Content-Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht.

1. Entwerfen Sie Ihre Content-Card.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Content-Card an Ihre App zu senden.

![Content-Card testen]({% image_buster /assets/img/contentcard_test.png %})

### Vorschau

Auf dem Tab **Vorschau** können Sie eine Vorschau Ihrer Karte sehen, während Sie sie zusammenstellen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Sicht des Benutzers aussehen wird.

{% alert note %}
Auf der Registerkarte **Vorschau** Ihres Composers ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät des Benutzers identisch. Wir empfehlen, immer eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und benutzerdefinierten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert das Liquid wie erwartet? Haben Sie einen [Standardattribut-Wert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) vorgesehen, wenn das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Führen Ihre Links den Benutzer dorthin, wohin er gehen soll?

### Debuggen

Nachdem Ihre Content Cards versendet wurden, können Sie im [Ereignisbenutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) in der Entwicklerkonsole eventuelle Probleme aufschlüsseln oder beheben. 

Ein häufiger Anwendungsfall ist die Fehlersuche, wenn ein:e Nutzer:in eine bestimmte Content-Card nicht sehen kann. Dazu können Sie in den **Event-Nutzerprotokollen** nach den Content-Cards suchen, die dem SDK beim Sitzungsstart, aber vor einer Impression zugestellt wurden, und diese zu einer bestimmten Kampagne zurückverfolgen:

1. Gehen Sie zu **Einstellungen** > **Ereignisbenutzerprotokoll**.
2. Suchen Sie die SDK-Anfrage für Ihren Testbenutzer und erweitern Sie sie.
3. Klicken Sie auf **Rohdaten**.
4. Finden Sie die `id` für Ihre Sitzung. Im Folgenden sehen Sie einen Beispielauszug:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```
    
{: start="5"}
5\. Verwenden Sie ein Dekodierungstool wie [Base64 Decode and Encode](https://www.base64decode.org/), um die `id` aus dem Base64-Format zu dekodieren und die zugehörige `campaign_id` zu finden. In unserem Beispiel ergibt sich daraus folgendes:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Where `4861692e-6fce-4215-bd05-3254fb9e9057` is the `campaign_id`.<br><br>

6. Gehen Sie auf die Seite **Kampagnen** und suchen Sie nach der `campaign_id`.

![Suchen Sie auf der Seite Kampagnen nach campaign_id ]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Von dort aus können Sie Ihre Nachrichteneinstellungen und Inhalte überprüfen, um herauszufinden, warum ein Benutzer eine bestimmte Inhaltskarte nicht sehen kann.

{% endtab %}
{% tab Email %}

1. Verfassen Sie Ihre E-Mail Nachricht.
2. Wählen Sie **Vorschau und Test**.
3. Wählen Sie den Tab **Test senden** und fügen Sie Ihre E-Mail Adresse oder Nutzer:innen in das Feld **Einzelne Nutzer:innen hinzufügen** ein. 
4. Wählen Sie **Test senden**, um Ihre entworfene E-Mail an Ihren Posteingang zu senden.

![E-Mail testen]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Um einen Test entweder an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert werden. Sie müssen zum Beispiel Push auf Ihrem iOS Gerät aktiviert haben, um auf die Benachrichtigung zu tippen, bevor die Testnachricht angezeigt wird. {% endalert %}

Wenn Sie in Ihrer App und auf Ihrem Testgerät Push-Benachrichtigungen eingerichtet haben, können Sie In-App-Nachrichten an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht. 

1. Verfassen Sie Ihre In-App-Nachricht.
2. Wählen Sie die Registerkarte **Test** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein. 
3. Wählen Sie **Test senden**, um Ihre Push Nachricht an Ihr Gerät zu senden.

Am oberen Rand des Bildschirms Ihres Geräts erscheint eine Push-Nachricht zum Test.

![Test in der App]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Bei Testsendungen kann es vorkommen, dass mehr als eine In-App-Nachricht an jeden Empfänger:in gesendet wird.
{% endalert %}

Wenn Sie direkt auf die Push-Nachricht klicken und sie öffnen, werden Sie zu Ihrer App weitergeleitet, wo Sie Ihren In-App-Nachrichtentest sehen können. Beachten Sie, dass dieses Feature zum Testen von In-App-Nachricht darauf beruht, dass der oder die Nutzer:in auf eine Push-Benachrichtigung zum Testen klickt, um die In-App Nachricht zu triggern. Für die erfolgreiche Zustellung der Push-Benachrichtigung muss der oder die Nutzer:in in der entsprechenden App zum Empfang von Push-Benachrichtigungen berechtigt sein.

### Vorschau

Auf dem Tab **Vorschau** können Sie eine Vorschau Ihrer In-App-Nachricht sehen, während Sie sie verfassen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Sicht des Benutzers aussehen wird. Sie können eine Vorschau darauf geben, wie Ihre Nachricht bei einem zufälligen Nutzer, einem bestimmten Nutzer:innen oder einem angepassten Nutzer aussehen wird. Sie können auch eine Vorschau der Nachrichten für mobile Geräte oder Tablets anzeigen.

![Tab "Verfassen" beim Erstellen einer In-App-Nachricht mit einer Vorschau, wie die Nachricht aussehen wird. Ein:e Nutzer:in ist nicht ausgewählt, so dass das im Body-Bereich hinzugefügte Liquid so angezeigt wird, wie es ist.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze verfügt über drei Generationen von In-App-Nachrichten. Sie können genau festlegen, an welche Geräte Ihre Nachrichten gesendet werden sollen, je nachdem, welche Generation sie unterstützen.

![Umschalten zwischen den Generationen bei der Vorschau einer In-App-Nachricht.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
In der **Vorschau** ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät des Benutzers identisch. Wir empfehlen immer, eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und benutzerdefinierten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert das Liquid wie erwartet? Haben Sie einen [Standardattribut-Wert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) vorgesehen, wenn das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Zeigen Ihre Schaltflächen dem Benutzer, wohin er gehen soll?

### Accessibility scanner

To support accessibility best practices, Braze automatically scans the content of in-app messages created using the traditional HTML editor against accessibility standards. This scanner helps identify content that may not meet Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) standards. WCAG ist eine Reihe von international anerkannten technischen Standards, die vom World Wide Web Consortium (W3C) entwickelt wurden, um Webinhalte für Menschen mit Behinderungen zugänglicher zu machen.

![Ergebnisse des Accessibility-Scans]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
The in-app message accessibility scanner only runs on messages built with custom HTML.
{% endalert %}

#### How it works

The scanner runs automatically on custom HTML messages and evaluates your entire HTML message against the full [WCAG 2.1 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). For each flagged issue, it shows:

- The specific HTML element involved
- A description of the accessibility issue
- A link to additional context or remediation guidance

#### Verständnis der automatisierten Zugänglichkeitstests

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Erstellen Sie Ihre LINE Nachricht.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll.
3. Wählen Sie **Test senden**, um Ihre Nachricht zu versenden.

![LINE Nachricht testen.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Mobiler Push

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail Adresse oder Nutzer:innen in das Feld **Einzelne Nutzer:innen hinzufügen** ein.
3. Wählen Sie **Test senden**, um Ihre entworfene Nachricht an Ihr Gerät zu senden.

![Push testen]({% image_buster /assets/img_archive/testpush.png %})

#### Web-Push

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie die Registerkarte **Test**. 
3. Wählen Sie **Test an mich selbst senden**.
4. Wählen Sie **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Web-Push testen]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie bereits Push-Nachrichten aus dem Braze Dashboard akzeptiert haben, wird der Push in der Ecke Ihres Bildschirms angezeigt. Andernfalls klicken Sie auf **Zulassen**, wenn Sie dazu aufgefordert werden, und die Meldung wird angezeigt.

{% endtab %}
{% tab SMS/MMS and RCS %}

Nachdem Sie Ihre SMS-, MMS- oder RCS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um zu sehen, wie sie in Realtime aussehen wird. 

1. Entwerfen Sie Ihre SMS-, MMS- oder RCS-Nachricht.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Testnachricht zu versenden.

![Content-Card testen]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Antwort des Webhooks zu überprüfen. Wählen Sie die Registerkarte **Test** und wählen Sie **Test senden**, um eine Testübertragung an die angegebene Webhook-URL zu senden. Sie können auch eine:n einzelne:n Nutzer:in auswählen, um eine Vorschau der Antwort zu erhalten. 

![Content-Card testen]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. Erstellen Sie Ihre WhatsApp Nachricht.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll.
3. Initiieren Sie ein Konversationsfenster, indem Sie eine WhatsApp-Nachricht an die Telefonnummer senden, die mit der Abo-Gruppe verbunden ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer wird in der Benachrichtigung auf der Registerkarte **Test** aufgeführt.
4. Wählen Sie **Test senden**, um Ihre Nachricht zu versenden.

![WhatsApp Nachricht testen.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Kampagnen testen 

Wenn Sie Kampagnen testen, die Nutzerdaten enthalten oder angepasste Event-Eigenschaften verwenden, müssen Sie zusätzliche oder andere Schritte unternehmen.

### Testen von mit Benutzerattributen personalisierten Kampagnen

Wenn Sie die [Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) in Ihrer Nachricht verwenden, müssen Sie zusätzliche Schritte unternehmen, um eine Vorschau Ihrer Kampagne zu erstellen und zu überprüfen, ob die Nutzerdaten den Inhalt richtig füllen.

Wenn Sie eine Testnachricht senden, wählen Sie entweder die Option **Vorhandene:n Nutzer:in auswählen** oder die Vorschau-Option **Angepassten Nutzer:innen** aus.

![Testen einer personalisierten Nachricht]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Einen bestehenden Benutzer auswählen

Wenn Sie eine:n bestehende:n Nutzer:in auswählen, geben Sie die ID oder E-Mail des Nutzers oder der Nutzerin in das Suchfeld ein. Verwenden Sie dann die Dashboard-Vorschau, um zu sehen, wie Ihre Nachricht für diesen Benutzer aussehen würde, und senden Sie eine Testnachricht an Ihr Gerät, die widerspiegelt, was dieser Benutzer sehen würde.

![Nutzer:in auswählen]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Einen angepassten Nutzer:innen auswählen

Wenn Sie eine Vorschau als angepasste:r Nutzer:in anzeigen, geben Sie den Text für die verschiedenen Felder ein, die für die Personalisierung zur Verfügung stehen, z. B. den Vornamen des Nutzers oder der Nutzerin und alle angepassten Attribute. Auch hier können Sie Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste:r Nutzer:in]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Anpassen eines bestehenden Nutzers:in

Sie können einzelne Felder eines zufälligen oder bestehenden Nutzers bearbeiten, um dynamische Inhalte in Ihrer Nachricht zu testen. Wählen Sie **Bearbeiten**, um den ausgewählten Nutzer:innen in einen angepassten Nutzer umzuwandeln, den Sie ändern können.

![Der Tab "Vorschau als Nutzer:in" mit einem Button "Bearbeiten".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Personalisierte Kampagnen mit benutzerdefinierten Ereigniseigenschaften testen

Das Testen von Kampagnen, die mit [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) personalisiert sind, unterscheidet sich geringfügig vom Testen anderer Arten von Kampagnen, die hier beschrieben werden. 

{% tabs local %}
{% tab Trigger manually %}

#### Methode 1: Kampagne manuell auslösen

Sie können die Kampagne selbst triggern, um Kampagnen zu testen, die mit angepassten Event-Eigenschaften personalisiert sind:

1. Schreiben Sie die Kopie mit den Eigenschaften des Events auf. 

![Testnachricht mit Eigenschaften zusammenstellen]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Verwenden Sie die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), um die Kampagne zuzustellen, wenn das Ereignis eintritt.

{% alert note %}
Wenn Sie eine Kampagne für iOS testen, müssen Sie die Verzögerung auf eine Minute einstellen, damit Sie Zeit haben, die App zu verlassen, denn iOS stellt keine Push-Benachrichtigungen für die aktuell geöffnete App zu. Andere Arten von Kampagnen können so eingestellt werden, dass sie sofort geliefert werden.
{% endalert %}

![Zustellung von Testnachrichten]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Stellen Sie die Nutzer:innen wie zu Testzwecken zusammen, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail Adresse als Targeting verwenden, und schließen Sie die Erstellung der Kampagne ab. 

![Targeting von Testnachrichten]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Gehen Sie in Ihre App und schließen Sie das angepasste Event ab.

Die Kampagne wird getriggert und zeigt die mit der Eigenschaft Event angepasste Nachricht an.

![Beispiel für eine Testnachricht]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Methode 2: Senden Sie sich eine Testnachricht

Wenn Sie angepasste Nutzer:innen-IDs speichern, können Sie die Kampagne auch testen, indem Sie eine angepasste Nachricht an sich selbst senden.

1. Schreiben Sie den Text für Ihre Kampagne.
2. Wählen Sie die Registerkarte **Test** und wählen Sie **Benutzerdefiniert**. 
3. Fügen Sie die angepasste Event-Eigenschaft unten auf der Seite hinzu, und fügen Sie Ihre Nutzer:in oder Ihre E-Mail Adresse in das obere Feld ein.
4. Wählen Sie **Test senden**, um eine mit der Eigenschaft personalisierte Nachricht zu erhalten.

![Testen mit angepassten Benutzern]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Methode 3: Liquid verwenden

Sie können angepasste Event-Eigenschaften testen, indem Sie die Werte manuell mit Liquid eingeben. 

1. Geben Sie im Nachrichten-Editor Werte für Ihre angepassten Event-Eigenschaften ein.
2. Wählen Sie den Tab **Vorschau als Nutzer:innen**, um zu überprüfen, ob die richtige Nachricht angezeigt wird.

{% endtab %}
{% endtabs %}

## Fehlersuche

### In-App-Nachrichten

Wenn Ihre In-App Messaging-Kampagne nicht durch eine Push-Kampagne getriggert wird, überprüfen Sie die Segmentierung der In-App-Kampagne, um sicherzustellen, dass der oder die Nutzer:in die Zielgruppe erfüllt, **bevor** er oder sie die Push-Nachricht erhält.

Bei Testübertragungen unter Android und iOS werden die In-App-Nachrichten, die die **Push-Erlaubnis per Klick anfordern**, auf einigen Geräten möglicherweise nicht angezeigt. Workaround:
- **Android:** Die Geräte müssen mit Android 13 und unserem Android SDK Version 21.0.0 arbeiten. Ein weiterer Grund kann sein, dass das Gerät, auf dem die In-App-Nachricht angezeigt wird, bereits über eine Eingabeaufforderung auf Systemebene verfügt. Möglicherweise haben Sie die Option **Nicht mehr nachfragen** gewählt. Dann müssen Sie die App neu installieren, um die Benachrichtigungsberechtigungen zurückzusetzen, bevor Sie sie erneut testen können.
- **iOS:** Wir empfehlen Ihrem Entwicklerteam, die Implementierung von Push-Benachrichtigungen für Ihre App zu überprüfen und jeglichen Code, der Push-Berechtigungen anfordert, manuell zu entfernen. Weitere Informationen finden Sie unter [Push-Primer In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Damit eine aktionsbasierte In-App-Nachricht-Kampagne zugestellt werden kann, müssen Sie angepasste Events über das Braze SDK und nicht über REST APIs protokollieren, damit die Benutzer die in Frage kommenden In-App-Nachrichten direkt auf ihrem Gerät empfangen können. Nutzer:innen erhalten die In-App-Nachricht, wenn sie das Ereignis während der Sitzung ausführen.
