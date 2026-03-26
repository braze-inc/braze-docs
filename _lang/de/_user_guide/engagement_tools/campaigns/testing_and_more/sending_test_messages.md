---
nav_title: Testnachrichten senden
article_title: Testnachrichten senden
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Testnachrichten über die verschiedenen Braze-Kanäle senden und wie Sie angepasste Event-Eigenschaften oder Nutzerattribute einbinden."

---

# Testnachrichten senden

> Bevor Sie eine Messaging-Kampagne an Ihre Nutzer:innen verschicken, empfehlen wir Ihnen als Best Practice, die Kampagne zu testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Sie können mit den Tools im Braze-Dashboard Testnachrichten erstellen und an ausgewählte Geräte oder Teammitglieder senden.

{% alert important %}
Stellen Sie sicher, dass Sie Ihren Kampagnenentwurf nach dem Testen speichern, damit Ihre Kampagne nicht gelöscht wird. Sie können Testnachrichten senden, ohne die Nachricht als Entwurf zu speichern.
{% endalert %}

## 1. Schritt: Testnutzer:innen identifizieren

Bevor Sie Ihre Messaging-Kampagne testen, ist es wichtig, Ihre Testnutzer:innen zu identifizieren. Bei diesen Nutzer:innen kann es sich entweder um bestehende Nutzer-IDs oder E-Mail-Adressen handeln oder um neue Nutzer:innen, die ausschließlich zum Testen von Messaging-Kampagnen verwendet werden. 

### Optional: Erstellen Sie eine Content-Test-Gruppe

Eine bequeme Möglichkeit, Ihre Testnutzer:innen zu organisieren, ist die Erstellung einer [Content-Test-Gruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), die eine Gruppe von Nutzer:innen umfasst, die Testnachrichten von Kampagnen erhalten werden. Sie können diese Testgruppe in das Feld **Content-Test-Gruppen hinzufügen** unter **Testempfänger:innen** in Ihrer Kampagne hinzufügen und Ihre Tests starten, ohne einzelne Testnutzer:innen zu erstellen oder hinzuzufügen.

## 2. Schritt: Kanalspezifische Testnachrichten senden

Die Schritte zum Senden von Testnachrichten finden Sie im folgenden Abschnitt für Ihren jeweiligen Kanal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Bevor Sie Banner-Nachrichten in Braze testen können, müssen Sie eine Banner-Kampagne in Braze erstellen. Überprüfen Sie außerdem, ob die Platzierung, die Sie testen möchten, bereits [in Ihrer App oder Website platziert]({{site.baseurl}}/developer_guide/banners/placements) ist.
{% endalert %}

Nachdem Sie Ihre Banner-Nachricht erstellt haben, können Sie eine Vorschau Ihres Banners anzeigen oder eine Testnachricht senden.

1. Entwerfen Sie Ihre Banner-Nachricht.
2. Wählen Sie **Vorschau**, um eine Vorschau Ihres Banners anzuzeigen oder eine Testnachricht zu senden.
3. Um eine Testnachricht zu senden, fügen Sie entweder eine Content-Test-Gruppe oder eine:n oder mehrere einzelne Nutzer:innen als **Testempfänger:innen** hinzu und wählen dann **Test senden**. 

Sie können Ihre Testnachricht bis zu 5 Minuten lang auf dem Gerät sehen.

![Tab „Vorschau" des Banner-Composers.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Beachten Sie, dass Ihre Vorschau aufgrund von Unterschieden in der Hardware möglicherweise nicht mit der endgültigen Darstellung auf dem Gerät der Nutzer:innen identisch ist.
{% endalert %}

### Test-Checkliste

- Ist Ihre Banner-Kampagne einer Platzierung zugewiesen?
- Werden die Bilder und Medien auf den von Ihnen anvisierten Gerätetypen und Bildschirmgrößen wie erwartet angezeigt und funktionieren sie?
- Führen Ihre Links und Buttons die Nutzer:innen dorthin, wohin sie sollen?
- Funktioniert Liquid wie erwartet? Haben Sie einen Standard-Attributwert für den Fall vorgesehen, dass Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
Um einen Test entweder an [Content-Test-Gruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder an einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten aktiviert sein und es müssen gültige Push-Token für die Testnutzer:innen registriert sein, bevor Sie den Test senden. Für iOS-Nutzer:innen müssen Sie auf die von Braze gesendete Push-Benachrichtigung tippen, um die Test-Content-Card anzuzeigen. Dieses Verhalten gilt nur für Test-Content-Cards.
{% endalert %}

Test-Content-Cards werden über eine Push-Benachrichtigung zugestellt. Die Karte ist in der Push-Payload verpackt, und das SDK extrahiert und speichert sie lokal zwischen, wenn der Push empfangen wird.

Dieser Prozess umgeht das normale Kartenzustellungssystem, weshalb Push aktiviert sein muss, auch wenn Sie eine Content-Card testen.

Test-Content-Cards laufen ungefähr fünf Minuten nach dem Senden ab.

Nachdem Sie Ihre Content-Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um zu sehen, wie sie in Realtime aussieht.

1. Entwerfen Sie Ihre Content-Card.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Test-Gruppe oder eine:n einzelne:n Nutzer:in aus, die diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Content-Card an Ihre App zu senden.

![Content-Card testen]({% image_buster /assets/img/contentcard_test.png %})

### Vorschau

Auf dem Tab **Vorschau** können Sie eine Vorschau Ihrer Karte sehen, während Sie sie zusammenstellen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird.

{% alert note %}
Auf dem Tab **Vorschau** Ihres Composers ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen identisch. Wir empfehlen, immer eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Haben Ihre Testnutzer:innen Push mit einem gültigen Push-Token aktiviert?
- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standard-Attributwert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) vorgesehen, wenn Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Führen Ihre Links die Nutzer:innen dorthin, wohin sie sollen?

### Debuggen

Nachdem Ihre Content-Cards versendet wurden, können Sie im [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) in der Entwicklungskonsole eventuelle Probleme aufschlüsseln oder beheben. 

Ein häufiger Anwendungsfall ist die Fehlersuche, wenn Nutzer:innen eine bestimmte Content-Card nicht sehen können. Dazu können Sie in den **Event-Benutzerprotokollen** nach den Content-Cards suchen, die dem SDK beim Sitzungsstart, aber vor einer Impression zugestellt wurden, und diese zu einer bestimmten Kampagne zurückverfolgen:

1. Gehen Sie zu **Einstellungen** > **Event-Benutzerprotokoll**.
2. Suchen Sie die SDK-Anfrage für Ihre Testnutzer:innen und erweitern Sie sie.
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
5. Verwenden Sie ein Dekodierungstool wie [Base64 Decode and Encode](https://www.base64decode.org/), um die `id` aus dem Base64-Format zu dekodieren und die zugehörige `campaign_id` zu finden. In unserem Beispiel ergibt sich daraus Folgendes:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Wobei `4861692e-6fce-4215-bd05-3254fb9e9057` die `campaign_id` ist.<br><br>

6. Gehen Sie auf die Seite **Kampagnen** und suchen Sie nach der `campaign_id`.

![Suche nach campaign_id auf der Seite „Kampagnen"]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Von dort aus können Sie Ihre Nachrichteneinstellungen und Inhalte überprüfen, um herauszufinden, warum Nutzer:innen eine bestimmte Content-Card nicht sehen können.

{% endtab %}
{% tab Email %}

1. Verfassen Sie Ihre E-Mail-Nachricht.
2. Wählen Sie **Vorschau und Test**.
3. Wählen Sie den Tab **Test senden** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID in das Feld **Einzelne Nutzer:innen hinzufügen** ein. 
4. Wählen Sie **Test senden**, um Ihre entworfene E-Mail an Ihren Posteingang zu senden.

![E-Mail testen]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Um einen Test entweder an [Content-Test-Gruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert werden. Sie müssen zum Beispiel Push auf Ihrem iOS-Gerät aktiviert haben, um auf die Benachrichtigung zu tippen, bevor die Testnachricht angezeigt wird. {% endalert %}

Wenn Sie in Ihrer App und auf Ihrem Testgerät Push-Benachrichtigungen eingerichtet haben, können Sie Test-In-App-Nachrichten an Ihre App senden, um zu sehen, wie sie in Realtime aussehen. 

1. Verfassen Sie Ihre In-App-Nachricht.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID in das Feld **Einzelne Nutzer:innen hinzufügen** ein. 
3. Wählen Sie **Test senden**, um Ihre Push-Nachricht an Ihr Gerät zu senden.

Am oberen Rand des Bildschirms Ihres Geräts erscheint eine Test-Push-Nachricht.

![In-App testen]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Bei Testsendungen kann es vorkommen, dass mehr als eine In-App-Nachricht an jede:n Empfänger:in gesendet wird. 
{% endalert %}

Wenn Sie direkt auf die Push-Nachricht klicken und sie öffnen, werden Sie zu Ihrer App weitergeleitet, wo Sie Ihren In-App-Nachrichtentest sehen können. Beachten Sie, dass dieses Feature zum Testen von In-App-Nachrichten darauf beruht, dass Nutzer:innen auf eine Test-Push-Benachrichtigung klicken, um die In-App-Nachricht zu triggern. Für die erfolgreiche Zustellung der Test-Push-Benachrichtigung müssen die Nutzer:innen in der entsprechenden App zum Empfang von Push-Benachrichtigungen berechtigt sein.

### Vorschau

Auf dem Tab **Vorschau** können Sie eine Vorschau Ihrer In-App-Nachricht sehen, während Sie sie verfassen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Perspektive Ihrer Nutzer:innen aussehen wird. Sie können eine Vorschau anzeigen, wie Ihre Nachricht bei zufälligen Nutzer:innen, bestimmten Nutzer:innen oder angepassten Nutzer:innen aussehen wird. Sie können auch eine Vorschau der Nachrichten für Mobilgeräte oder Tablets anzeigen.

![Tab „Verfassen" beim Erstellen einer In-App-Nachricht mit einer Vorschau, wie die Nachricht aussehen wird. Es sind keine Nutzer:innen ausgewählt, sodass das im Body-Bereich hinzugefügte Liquid so angezeigt wird, wie es ist.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze verfügt über drei Generationen von In-App-Nachrichten. Sie können genau festlegen, an welche Geräte Ihre Nachrichten gesendet werden sollen, je nachdem, welche Generation sie unterstützen.

![Umschalten zwischen den Generationen bei der Vorschau einer In-App-Nachricht.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
In der **Vorschau** ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät der Nutzer:innen identisch. Wir empfehlen immer, eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und angepassten Attribute korrekt generiert werden.
{% endalert %}

### Test-Checkliste

- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert Liquid wie erwartet? Haben Sie einen [Standard-Attributwert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) vorgesehen, wenn Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Führen Ihre Buttons die Nutzer:innen dorthin, wohin sie sollen?

### Barrierefreiheits-Scanner

Um Best Practices für Barrierefreiheit zu unterstützen, scannt Braze automatisch den Inhalt von In-App-Nachrichten, die mit dem traditionellen HTML-Editor erstellt wurden, anhand von Barrierefreiheitsstandards. Dieser Scanner hilft dabei, Inhalte zu identifizieren, die möglicherweise nicht den Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) entsprechen. WCAG ist eine Reihe von international anerkannten technischen Standards, die vom World Wide Web Consortium (W3C) entwickelt wurden, um Webinhalte für Menschen mit Behinderungen zugänglicher zu machen.

![Ergebnisse des Barrierefreiheits-Scans]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
Der Barrierefreiheits-Scanner für In-App-Nachrichten wird nur bei Nachrichten ausgeführt, die mit benutzerdefiniertem HTML erstellt wurden. 
{% endalert %}

#### So funktioniert es

Der Scanner wird automatisch bei benutzerdefinierten HTML-Nachrichten ausgeführt und überprüft Ihre gesamte HTML-Nachricht anhand des vollständigen [WCAG 2.1 AA-Regelwerks](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Für jedes erkannte Problem zeigt er:

- Das betroffene HTML-Element
- Eine Beschreibung des Barrierefreiheitsproblems
- Einen Link zu zusätzlichem Kontext oder Anleitungen zur Behebung

#### Verständnis der automatisierten Barrierefreiheitstests

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Erstellen Sie Ihre LINE-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Test-Gruppe oder eine:n einzelne:n Nutzer:in aus, die diese Testnachricht erhalten soll.
3. Wählen Sie **Test senden**, um Ihre Nachricht zu versenden.

![LINE-Nachricht testen.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Mobiler Push

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie den Tab **Test** und fügen Sie Ihre E-Mail-Adresse oder Nutzer-ID in das Feld **Einzelne Nutzer:innen hinzufügen** ein.
3. Wählen Sie **Test senden**, um Ihre entworfene Nachricht an Ihr Gerät zu senden.

![Push testen]({% image_buster /assets/img_archive/testpush.png %})

#### Web-Push

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie den Tab **Test**. 
3. Wählen Sie **Test an mich selbst senden**.
4. Wählen Sie **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Web-Push testen]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie bereits Push-Nachrichten aus dem Braze-Dashboard akzeptiert haben, wird der Push in der Ecke Ihres Bildschirms angezeigt. Andernfalls klicken Sie auf **Zulassen**, wenn Sie dazu aufgefordert werden, und die Nachricht wird angezeigt.

{% endtab %}
{% tab SMS/MMS and RCS %}

Nachdem Sie Ihre SMS-, MMS- oder RCS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um zu sehen, wie sie in Realtime aussehen wird. 

1. Entwerfen Sie Ihre SMS-, MMS- oder RCS-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Test-Gruppe oder eine:n einzelne:n Nutzer:in aus, die diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Testnachricht zu versenden.

![Content-Card testen]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Antwort des Webhooks zu überprüfen. Wählen Sie den Tab **Test** und wählen Sie **Test senden**, um einen Testversand an die angegebene Webhook-URL zu senden. Sie können auch eine:n einzelne:n Nutzer:in auswählen, um eine Vorschau der Antwort als bestimmte:r Nutzer:in zu erhalten. 

![Content-Card testen]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. Erstellen Sie Ihre WhatsApp-Nachricht.
2. Wählen Sie den Tab **Test** und wählen Sie mindestens eine Content-Test-Gruppe oder eine:n einzelne:n Nutzer:in aus, die diese Testnachricht erhalten soll.
3. Initiieren Sie ein Gesprächsfenster, indem Sie eine WhatsApp-Nachricht an die Telefonnummer senden, die mit der Abo-Gruppe verbunden ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer wird in der Benachrichtigung auf dem Tab **Test** aufgeführt.
4. Wählen Sie **Test senden**, um Ihre Nachricht zu versenden.

![WhatsApp-Nachricht testen.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Kampagnen testen 

Wenn Sie Kampagnen testen, die Nutzerdaten enthalten oder angepasste Event-Eigenschaften verwenden, müssen Sie zusätzliche oder andere Schritte unternehmen.

### Testen von Kampagnen, die mit Nutzerattributen personalisiert sind

Wenn Sie [Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) in Ihrer Nachricht verwenden, müssen Sie zusätzliche Schritte unternehmen, um eine Vorschau Ihrer Kampagne zu erstellen und zu überprüfen, ob die Nutzerdaten den Inhalt richtig füllen.

Wenn Sie eine Testnachricht senden, wählen Sie entweder die Option **Vorhandene:n Nutzer:in auswählen** oder die Vorschau als **Angepasste:r Nutzer:in**.

![Testen einer personalisierten Nachricht]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Bestehende:n Nutzer:in auswählen

Wenn Sie bestehende Nutzer:innen auswählen, geben Sie die spezifische Nutzer-ID oder E-Mail in das Suchfeld ein. Verwenden Sie dann die Dashboard-Vorschau, um zu sehen, wie Ihre Nachricht für diese:n Nutzer:in aussehen würde, und senden Sie eine Testnachricht an Ihr Gerät, die widerspiegelt, was diese:r Nutzer:in sehen würde.

![Nutzer:in auswählen]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Angepasste:n Nutzer:in auswählen

Wenn Sie eine Vorschau als angepasste:r Nutzer:in anzeigen, geben Sie den Text für die verschiedenen Felder ein, die für die Personalisierung zur Verfügung stehen, z. B. den Vornamen und alle angepassten Attribute. Auch hier können Sie Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste:r Nutzer:in]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Bestehende:n Nutzer:in anpassen

Sie können einzelne Felder von zufälligen oder bestehenden Nutzer:innen bearbeiten, um dynamischen Content in Ihrer Nachricht zu testen. Wählen Sie **Bearbeiten**, um die ausgewählten Nutzer:innen in angepasste Nutzer:innen umzuwandeln, die Sie ändern können.

![Der Tab „Vorschau als Nutzer:in" mit einem Button „Bearbeiten".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Personalisierte Kampagnen mit angepassten Event-Eigenschaften testen

Das Testen von Kampagnen, die mit [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) personalisiert sind, unterscheidet sich geringfügig vom Testen anderer Arten von Kampagnen, die hier beschrieben werden. 

{% tabs local %}
{% tab Trigger manually %}

#### Methode 1: Kampagne manuell triggern

Sie können die Kampagne selbst triggern, um Kampagnen zu testen, die mit angepassten Event-Eigenschaften personalisiert sind:

1. Schreiben Sie den Text mit den Event-Eigenschaften. 

![Testnachricht mit Eigenschaften verfassen]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Verwenden Sie die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/), um die Kampagne zuzustellen, wenn das Event eintritt.

{% alert note %}
Wenn Sie eine iOS-Push-Kampagne testen, müssen Sie die Verzögerung auf eine Minute einstellen, damit Sie Zeit haben, die App zu verlassen, denn iOS stellt keine Push-Benachrichtigungen für die aktuell geöffnete App zu. Andere Arten von Kampagnen können so eingestellt werden, dass sie sofort zugestellt werden.
{% endalert %}

![Zustellung von Testnachrichten]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Richten Sie das Targeting der Nutzer:innen wie zu Testzwecken ein, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail-Adresse als Zielgruppe verwenden, und schließen Sie die Erstellung der Kampagne ab. 

![Targeting von Testnachrichten]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Gehen Sie in Ihre App und führen Sie das angepasste Event aus.

Die Kampagne wird getriggert und zeigt die mit der Event-Eigenschaft angepasste Nachricht an.

![Beispiel für eine Testnachricht]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Methode 2: Sich selbst eine Testnachricht senden

Wenn Sie angepasste Nutzer-IDs speichern, können Sie die Kampagne auch testen, indem Sie eine angepasste Testnachricht an sich selbst senden.

1. Schreiben Sie den Text für Ihre Kampagne.
2. Wählen Sie den Tab **Test** und wählen Sie **Angepasste:r Nutzer:in**. 
3. Fügen Sie die angepasste Event-Eigenschaft unten auf der Seite hinzu und fügen Sie Ihre Nutzer-ID oder E-Mail-Adresse in das obere Feld ein.
4. Wählen Sie **Test senden**, um eine mit der Eigenschaft personalisierte Nachricht zu erhalten.

![Testen mit angepassten Nutzer:innen]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Methode 3: Liquid verwenden

Sie können angepasste Event-Eigenschaften testen, indem Sie die Werte manuell mit Liquid eingeben. 

1. Geben Sie im Nachrichten-Editor Werte für Ihre angepassten Event-Eigenschaften ein.
2. Wählen Sie den Tab **Vorschau als Nutzer:in**, um zu überprüfen, ob die richtige Nachricht angezeigt wird.

{% endtab %}
{% endtabs %}

## Fehlerbehebung

### In-App-Nachrichten

Wenn Ihre In-App-Nachricht-Kampagne nicht durch eine Push-Kampagne getriggert wird, überprüfen Sie die Segmentierung der In-App-Kampagne, um sicherzustellen, dass die Nutzer:innen die Zielgruppe erfüllen, **bevor** sie die Push-Nachricht erhalten.

Bei Testsendungen unter Android und iOS werden die In-App-Nachrichten, die das On-Click-Verhalten **Push-Berechtigung anfordern** verwenden, auf einigen Geräten möglicherweise nicht angezeigt. Als Workaround:
- **Android:** Die Geräte müssen mit Android 13 und unserem Android SDK Version 21.0.0 arbeiten. Ein weiterer Grund kann sein, dass das Gerät, auf dem die In-App-Nachricht angezeigt wird, bereits über eine Eingabeaufforderung auf Systemebene verfügt. Möglicherweise haben Sie die Option **Nicht mehr nachfragen** gewählt, sodass Sie die App neu installieren müssen, um die Benachrichtigungsberechtigungen zurückzusetzen, bevor Sie erneut testen können.
- **iOS:** Wir empfehlen Ihrem Entwicklerteam, die Implementierung von Push-Benachrichtigungen für Ihre App zu überprüfen und jeglichen Code, der Push-Berechtigungen anfordert, manuell zu entfernen. Weitere Informationen finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Damit eine aktionsbasierte In-App-Nachricht-Kampagne zugestellt werden kann, müssen Sie angepasste Events über das Braze SDK und nicht über REST APIs protokollieren, damit die Nutzer:innen die berechtigten In-App-Nachrichten direkt auf ihrem Gerät empfangen können. Nutzer:innen erhalten die In-App-Nachricht, wenn sie das Event während der Sitzung ausführen.