---
nav_title: Versenden von Testnachrichten
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

Eine bequeme Möglichkeit, Ihre Testnutzer zu organisieren, ist die Erstellung einer [Content-Test-Gruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), die eine Gruppe von Nutzern umfasst, die Testnachrichten von Kampagnen erhalten werden. Sie können diese Testgruppe in das Feld **Inhaltstestgruppen hinzufügen** unter **Testempfänger** in Ihrer Kampagne hinzufügen und Ihre Tests starten, ohne einzelne Testbenutzer zu erstellen oder hinzuzufügen.

## Schritt 2: Kanalspezifische Testnachrichten senden

Die Schritte zum Senden von Testnachrichten finden Sie im folgenden Abschnitt für Ihren jeweiligen Kanal.

{% tabs %}
{% tab E-Mail %}

1. Verfassen Sie Ihre E-Mail Nachricht.
2. Klicken Sie auf **Vorschau und Test**.
3. Wählen Sie die Registerkarte **Test senden** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein. 
4. Klicken Sie auf **Test senden**, um Ihre entworfene E-Mail an Ihren Posteingang zu senden.

![Test E-Mail]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Mobiler Push

1. Entwerfen Sie Ihren mobilen Push.
2. Wählen Sie die Registerkarte **Einstellungen** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein.
3. Klicken Sie auf **Test senden**, um Ihre gezeichnete Nachricht an Ihr Gerät zu senden.

![Testen Sie Push]({% image_buster /assets/img_archive/testpush.png %})

#### Web-Push

1. Erstellen Sie Ihren Web-Push.
2. Wählen Sie die Registerkarte **Test**. 
3. Prüfen Sie **Test an mich selbst senden**.
4. Klicken Sie auf **Test senden**, um Ihren Web-Push an Ihren Webbrowser zu senden.

![Testen Sie Web-Push]({% image_buster /assets/img_archive/testwebpush.png %})

Wenn Sie bereits Push-Nachrichten aus dem Braze Dashboard akzeptiert haben, wird der Push in der Ecke Ihres Bildschirms angezeigt. Andernfalls klicken Sie auf **Zulassen**, wenn Sie dazu aufgefordert werden, und die Meldung wird angezeigt.

{% endtab %}
{% tab In-App-Nachricht %}

Wenn Sie in Ihrer App und auf Ihrem Testgerät Push-Benachrichtigungen eingerichtet haben, können Sie In-App-Nachrichten an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht. 

1. Verfassen Sie Ihre In-App-Nachricht.
2. Wählen Sie die Registerkarte **Test** und fügen Sie Ihre E-Mail-Adresse oder Benutzer-ID in das Feld **Einzelne Benutzer hinzufügen** ein. 
3. Klicken Sie auf **Test senden**, um Ihre Push-Nachricht an Ihr Gerät zu senden.

Am oberen Rand des Bildschirms Ihres Geräts erscheint eine Push-Nachricht zum Test.

![Test In App]({% image_buster /assets/img_archive/test-in-app.png %})

Wenn Sie direkt auf die Push-Nachricht klicken und sie öffnen, werden Sie zu Ihrer App weitergeleitet, wo Sie Ihren In-App-Nachrichtentest sehen können. Beachten Sie, dass dieses Feature zum Testen von In-App-Nachricht darauf beruht, dass der oder die Nutzer:in auf eine Push-Benachrichtigung zum Testen klickt, um die In-App Nachricht zu triggern. Für die erfolgreiche Zustellung der Push-Benachrichtigung muss der oder die Nutzer:in in der entsprechenden App zum Empfang von Push-Benachrichtigungen berechtigt sein.

#### Fehlersuche

* Wenn Ihre In-App Messaging-Kampagne nicht durch eine Push-Kampagne getriggert wird, überprüfen Sie die Segmentierung der In-App-Kampagne, um sicherzustellen, dass der oder die Nutzer:in die Zielgruppe erfüllt, **bevor** er oder sie die Push-Nachricht erhält.
* Bei Testübertragungen unter Android und iOS werden die In-App-Nachrichten, die die **Push-Erlaubnis per Klick anfordern**, auf einigen Geräten möglicherweise nicht angezeigt. Workaround:
  * **Android:** Die Geräte müssen mit Android 13 und unserem Android SDK Version 21.0.0 arbeiten. Ein weiterer Grund kann sein, dass das Gerät, auf dem die In-App-Nachricht angezeigt wird, bereits über eine Eingabeaufforderung auf Systemebene verfügt. Möglicherweise haben Sie die Option **Nicht mehr nachfragen** gewählt. Dann müssen Sie die App neu installieren, um die Benachrichtigungsberechtigungen zurückzusetzen, bevor Sie sie erneut testen können.
  * **iOS:** Wir empfehlen Ihrem Entwicklerteam, die Implementierung von Push-Benachrichtigungen für Ihre App zu überprüfen und jeglichen Code, der Push-Berechtigungen anfordert, manuell zu entfernen. Weitere Informationen finden Sie unter [Push-Primer In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
* Damit eine aktionsbasierte In-App-Nachrichtenkampagne zugestellt werden kann, müssen benutzerdefinierte Ereignisse über das Braze SDK und nicht über REST-APIs protokolliert werden, damit der Benutzer geeignete In-App-Nachrichten direkt auf seinem Gerät empfangen kann. Nutzer:innen können die In-App-Nachricht erhalten, wenn sie das Event während der Sitzung ausführen.

{% endtab %}
{% tab Content-Card %}

Nachdem Sie Ihre Content-Card erstellt haben, können Sie eine Test-Content-Card an Ihre App senden, um zu sehen, wie sie in Echtzeit aussieht.

1. Entwerfen Sie Ihre Content-Card.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Klicken Sie auf **Test senden**, um Ihre Inhaltskarte an Ihre App zu senden.

![Content-Card testen]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Nachdem Sie Ihre SMS- oder MMS-Nachricht erstellt haben, können Sie eine Testnachricht an Ihr Telefon senden, um zu sehen, wie sie in Echtzeit aussehen wird. 

1. Entwerfen Sie Ihre SMS- oder MMS-Nachricht.
2. Wählen Sie die Registerkarte **Test** und wählen Sie mindestens eine Inhaltstestgruppe oder einen einzelnen Benutzer, der diese Testnachricht erhalten soll. 
3. Klicken Sie auf **Test senden**, um Ihre Testnachricht zu versenden.

![Content-Card testen]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Nachdem Sie Ihren Webhook erstellt haben, können Sie einen Testversand durchführen, um die Antwort des Webhooks zu überprüfen. Wählen Sie die Registerkarte **Test** und wählen Sie **Test senden**, um eine Testübertragung an die angegebene Webhook-URL zu senden. Sie können auch eine:n einzelne:n Nutzer:in auswählen, um eine Vorschau der Antwort zu erhalten. 

![Content-Card testen]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab News Feed %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Um eine Test-Newsfeed-Karte zu versenden, müssen Sie ein Testsegment einrichten und anschließend eine Testkampagne versenden.

##### Schritt 1: Bestimmtes Testsegment erstellen

Sobald Sie ein Testsegment eingerichtet haben, können Sie diese Nachrichtenkanäle nutzen. Der Vorgang dauert nur ein paar kurze Schritte und muss bei richtiger Konfiguration nur einmal durchgeführt werden.

1. Gehen Sie auf die Seite **Segmente** und [erstellen Sie ein neues Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 
2. Klicken Sie auf das Dropdown-Menü unter **Filter hinzufügen** und suchen Sie die Testfilter am Ende der Liste. <br><br>![Testen von Filtern]({% image_buster /assets/img_archive/testmessages1.png %})<br><br>
3. Verwenden Sie die Testfilter, um Nutzer:innen mit bestimmten E-Mail-Adressen oder externen [IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift) auszuwählen.<br><br>![Filteroptionen testen]({% image_buster /assets/img_archive/testmessages2.png %})
<br><br>Diese Filter haben die folgenden Optionen:
- **Ist gleich**: Sucht nach einer genauen Übereinstimmung mit der von Ihnen angegebenen E-Mail oder Benutzer-ID. Verwenden Sie diese Option, wenn Sie die Testkampagnen nur an Geräte senden möchten, die mit einer einzigen E-Mail oder Benutzer-ID verbunden sind.
- **Ist nicht gleichbedeutend**: Schließt eine bestimmte E-Mail oder Benutzer-ID von Testkampagnen aus.
- **Übereinstimmungen**: Findet Benutzer mit E-Mail-Adressen oder Benutzer-IDs, die einem Teil des von Ihnen angegebenen Suchbegriffs entsprechen. Damit können Sie nur die Nutzer:innen mit der Adresse "@yourcompany.com" finden, was es Ihnen erlaubt, Nachrichten an alle Mitglieder Ihres Teams zu senden.
<br><br>
Diese Filter können auch zusammen verwendet werden, um Ihre Liste der Testnutzer:innen einzugrenzen. Das Testsegment könnte zum Beispiel einen Filter für E-Mail-Adressen enthalten, der `matches` „@braze.com“ und einen anderen Filter, der `does not equal` „sales@braze.com“. Sie können auch mehrere bestimmte E-Mails auswählen, indem Sie die Option `matches` verwenden und die E-Mail-Adressen mit einem „|“-Zeichen trennen (zum Beispiel `matches` „email1@braze.com|email2@braze.com“).
<br><br>
4. Fügen Sie die Testfilter zu Ihrem Testsegment hinzu.
5. Klicken Sie oben im Segmenteditor auf **Vorschau** oder exportieren Sie die Benutzerdaten dieses Segments in eine CSV-Datei, um zu überprüfen, ob Sie nur die gewünschten Benutzer ausgewählt haben.
6. Klicken Sie auf das Dropdown-Menü **Benutzerdaten** und wählen Sie **CSV-Export aller Benutzerdaten**, um die Segment-Benutzerdaten zu exportieren. 

![Testsegment überprüfen]({% image_buster /assets/img_archive/testmessages3.png %})

> Wenn Sie die Benutzerdaten des Segments in eine CSV-Datei exportieren, erhalten Sie ein möglichst genaues Bild davon, wer unter dieses Segment fällt. Die Registerkarte **Vorschau** zeigt nur eine Auswahl von Benutzern in dem Segment und kann daher den Eindruck erwecken, dass nicht alle vorgesehenen Mitglieder ausgewählt wurden. Weitere Informationen finden Sie unter [Betrachten und Verstehen von Segmentdaten][7].

Nachdem Sie bestätigt haben, dass Sie nur die Nutzer ansprechen, die die Testnachricht erhalten sollen, können Sie dieses Segment entweder in einer bestehenden Kampagne auswählen, die Sie testen möchten, oder Sie klicken im Segmentmenü auf die Schaltfläche **Kampagne starten**.

##### Schritt 2: Testkampagne senden

Um Test-Newsfeed-Karten zu versenden, müssen Sie Ihr zuvor erstelltes Testsegment als Zielgruppe auswählen. Beginnen Sie mit der Erstellung einer Multichannel-Kampagne und folgen Sie den üblichen Schritten. Wenn Sie den Schritt **Zielbenutzer** erreichen, wählen Sie Ihr Testsegment aus, wie in der folgenden Abbildung gezeigt.

![Testsegment]({% image_buster /assets/img_archive/test_segment.png %})

Bestätigen Sie Ihre Kampagne und starten Sie sie, um Ihre News Feed-Karten zu testen.

> Wenn Sie eine einzelne Kampagne verwenden möchten, um eine Nachricht mehrmals an sich selbst zu senden, aktivieren Sie im **Zeitplan** des Nachrichten-Editors das Kontrollkästchen „Nutzer:innen dürfen sich erneut für den Erhalt der Kampagne qualifizieren“.

{% endtab %}
{% endtabs %}

## Personalisierte Kampagnen testen 

Wenn Sie Kampagnen testen, die Nutzerdaten enthalten oder angepasste Event-Eigenschaften verwenden, müssen Sie zusätzliche oder andere Schritte unternehmen.

### Testen von mit Benutzerattributen personalisierten Kampagnen

Wenn Sie [Personalisierung][26] in Ihrer Nachricht verwenden, müssen Sie zusätzliche Schritte unternehmen, um eine Vorschau Ihrer Kampagne zu erstellen und zu überprüfen, ob die Nutzerdaten den Inhalt richtig auffüllen.

Wenn Sie eine Testnachricht senden, wählen Sie entweder die Option **Vorhandene:n Nutzer:in auswählen** oder die Vorschau-Option **Angepassten Nutzer:innen** aus.

![Testen einer personalisierten Nachricht][23]{: style="max-width:70%;" }

#### Einen bestehenden Benutzer auswählen

Wenn Sie eine:n bestehende:n Nutzer:in auswählen, geben Sie die ID oder E-Mail des Nutzers oder der Nutzerin in das Suchfeld ein. Verwenden Sie dann die Dashboard-Vorschau, um zu sehen, wie Ihre Nachricht für diesen Benutzer aussehen würde, und senden Sie eine Testnachricht an Ihr Gerät, die widerspiegelt, was dieser Benutzer sehen würde.

![Nutzer:in auswählen][24]

#### Einen angepassten Nutzer:innen auswählen

Wenn Sie eine Vorschau als angepasste:r Nutzer:in anzeigen, geben Sie den Text für die verschiedenen Felder ein, die für die Personalisierung zur Verfügung stehen, z. B. den Vornamen des Nutzers oder der Nutzerin und alle angepassten Attribute. Auch hier können Sie Ihre eigene E-Mail-Adresse eingeben, um einen Test an Ihr Gerät zu senden.

![Angepasste:r Nutzer:in][25]

### Personalisierte Kampagnen mit benutzerdefinierten Ereigniseigenschaften testen

Das Testen von Kampagnen, die mit [angepassten Event-Eigenschaften][19] personalisiert wurden, unterscheidet sich geringfügig vom Testen anderer Arten von Kampagnen, die hier beschrieben werden. Der robusteste Weg, um mit angepassten Event-Eigenschaften personalisierte Kampagnen zu testen, ist, die Kampagne selbst zu triggern, indem Sie Folgendes tun:

1. Schreiben Sie die Kopie mit den Eigenschaften des Events auf. ![Testnachricht mit Eigenschaften zusammenstellen][15]
2. Verwenden Sie [aktionsbasierte Zustellung][21], um die Kampagne bei Eintreten des Events zuzustellen.

{% alert note %}
Wenn Sie eine Kampagne für iOS testen, müssen Sie den Delay auf 1 Minute einstellen, damit Sie Zeit haben, die App zu verlassen, da iOS keine Push-Benachrichtigungen für die aktuell geöffnete App zustellt. Andere Arten von Kampagnen können so eingestellt werden, dass sie sofort geliefert werden.
{% endalert %}

![Zustellung von Testnachrichten][16]

{: start="3"}
3\. Stellen Sie die Nutzer:innen wie zu Testzwecken zusammen, indem Sie einen Testfilter verwenden oder Ihre eigene E-Mail Adresse als Targeting verwenden, und schließen Sie die Erstellung der Kampagne ab. 

![Targeting von Testnachrichten][17]

{: start="4"}
4\. Gehen Sie in Ihre App und schließen Sie das angepasste Event ab.

Die Kampagne wird getriggert und zeigt die mit der Eigenschaft Event angepasste Nachricht an.

![Beispiel für eine Testnachricht][18]

Wenn Sie angepasste Nutzer:innen-IDs speichern, können Sie die Kampagne auch testen, indem Sie eine angepasste Nachricht an sich selbst senden.

1. Schreiben Sie den Text für Ihre Kampagne.
2. Wählen Sie die Registerkarte **Test** und wählen Sie **Benutzerdefiniert**. 
3. Fügen Sie die angepasste Event-Eigenschaft unten auf der Seite hinzu, und fügen Sie Ihre:n Nutzer:in oder Ihre E-Mail Adresse in das obere Feld ein.
4. Klicken Sie auf **Test senden**, um eine personalisierte Nachricht mit der Eigenschaft zu erhalten.

![Testen mit angepassten Benutzern][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/
