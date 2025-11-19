---
nav_title: Versenden von Test Nachrichten
article_title: Versenden von Testnachrichten
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Testnachrichten über die verschiedenen Braze-Kanäle senden und wie Sie benutzerdefinierte Ereigniseigenschaften oder Benutzerattribute einbinden."

---

# Versenden von Test Nachrichten

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
{% tab Email %}

1. Verfassen Sie Ihre E-Mail Nachricht.
2. Wählen Sie **Vorschau und Test**.
3. Wählen Sie den Tab **Test senden** und fügen Sie Ihre E-Mail Adresse oder Nutzer:innen in das Feld **Einzelne Nutzer:innen hinzufügen** ein. 
4. Wählen Sie **Test senden**, um Ihre entworfene E-Mail an Ihren Posteingang zu senden.

![Test E-Mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Mobiler Push

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie die Registerkarte **Einstellungen** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein.
3. Wählen Sie **Test senden**, um Ihre entworfene Nachricht an Ihr Gerät zu senden.

![Test Push]({% image_buster /assets/img_archive/testpush.png %})

#### Web-Push

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie die Registerkarte **Test**. 
3. Wählen Sie **Test an mich selbst senden**.
4. Wählen Sie **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Test Web-Push]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie bereits Push-Nachrichten aus dem Braze Dashboard akzeptiert haben, wird der Push in der Ecke Ihres Bildschirms angezeigt. Andernfalls klicken Sie auf **Zulassen**, wenn Sie dazu aufgefordert werden, und die Meldung wird angezeigt.

{% endtab %}
{% tab In-App Message %}

Wenn Sie in Ihrer App und auf Ihrem Testgerät Push-Benachrichtigungen eingerichtet haben, können Sie In-App-Nachrichten an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht. 

1. Verfassen Sie Ihre In-App-Nachricht.
2. Wählen Sie die Registerkarte **Test** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein. 
3. Wählen Sie **Test senden**, um Ihre Push Nachricht an Ihr Gerät zu senden.

Am oberen Rand des Bildschirms Ihres Geräts erscheint eine Push-Nachricht zum Test.

![Test in der App]({% image_buster /assets/img_archive/test-in-app.png %})

Wenn Sie direkt auf die Push-Nachricht klicken und sie öffnen, werden Sie zu Ihrer App weitergeleitet, wo Sie Ihren In-App-Nachrichtentest sehen können. Beachten Sie, dass dieses Feature zum Testen von In-App-Nachricht darauf beruht, dass der oder die Nutzer:in auf eine Push-Benachrichtigung zum Testen klickt, um die In-App Nachricht zu triggern. Für die erfolgreiche Zustellung der Push-Benachrichtigung muss der oder die Nutzer:in in der entsprechenden App zum Empfang von Push-Benachrichtigungen berechtigt sein.

{% endtab %}
{% tab Content Card %}

Nachdem Sie Ihre Content-Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht.

1. Entwerfen Sie Ihre Content-Card.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Content-Card an Ihre App zu senden.

![Test Content-Card]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Nachdem Sie Ihre SMS- oder MMS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um zu sehen, wie sie in Echtzeit aussehen wird. 

1. Entwerfen Sie Ihre SMS- oder MMS-Nachricht.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Wählen Sie **Test senden**, um Ihre Testnachricht zu versenden.

![Test Content-Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Antwort des Webhooks zu überprüfen. Wählen Sie die Registerkarte **Test** und wählen Sie **Test senden**, um eine Testübertragung an die angegebene Webhook-URL zu senden. Sie können auch eine:n einzelne:n Nutzer:in auswählen, um eine Vorschau der Antwort zu erhalten. 

![Test Content-Card]({% image_buster /assets/img/webhook_test.png %})

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

![Einen Nutzer:in auswählen]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Einen angepassten Nutzer:innen auswählen

Wenn Sie eine Vorschau als angepasste:r Nutzer:in anzeigen, geben Sie den Text für die verschiedenen Felder ein, die für die Personalisierung zur Verfügung stehen, z. B. den Vornamen des Nutzers oder der Nutzerin und alle angepassten Attribute. Auch hier können Sie Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste Nutzer:in]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

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

![Test Zustellung von Nachrichten]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Stellen Sie die Nutzer:innen wie zu Testzwecken zusammen, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail Adresse als Targeting verwenden, und schließen Sie die Erstellung der Kampagne ab. 

![Test Message Targeting]({% image_buster /assets/img_archive/testeventproperties-target.png %})

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

![Testen unter Verwendung angepasster Nutzer:innen]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

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

Damit eine aktionsbasierte In-App-Nachrichtenkampagne zugestellt werden kann, müssen benutzerdefinierte Ereignisse über das Braze SDK und nicht über REST-APIs protokolliert werden, damit der Benutzer geeignete In-App-Nachrichten direkt auf seinem Gerät empfangen kann. Nutzer:innen können die In-App-Nachricht erhalten, wenn sie das Event während der Sitzung ausführen.
