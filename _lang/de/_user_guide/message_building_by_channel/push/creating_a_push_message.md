---
nav_title: "Erstellen einer Push Nachricht"
article_title: Erstellen einer Push-Kampagne
page_order: 4
page_type: tutorial
description: "Diese Tutorial-Seite behandelt die verschiedenen Komponenten, die bei der Erstellung einer Push-Nachricht eine Rolle spielen, einschließlich Konfiguration, Versand, Zielgruppen und mehr."
channel: push
tool:
  - Campaigns
  
---

# Push-Benachrichtigungen erstellen

> Push-Benachrichtigungen eignen sich hervorragend für zeitkritische Handlungsaufforderungen und um Nutzer, die die App schon länger nicht mehr besucht haben, wieder zu aktivieren. Erfolgreiche Push-Kampagnen führen den Nutzer direkt zum Inhalt und demonstrieren den Wert Ihrer App. Beispiele für Push-Benachrichtigungen finden Sie in unseren [Anwendungsbeispielen][8].

## Schritt 1: Entscheiden Sie, wo Sie Ihre Nachrichten erstellen möchten {#create-new-campaign-push}

{% alert tip %}
Sie sind sich nicht sicher, ob Sie eine Kampagne oder ein Canvas verwenden sollen? Kampagnen eignen sich besser für einfache, einmalige Messaging-Kampagnen, während Canvase besser für mehrstufige User Journeys geeignet sind.
{% endalert %}

{% tabs %}
{% tab Kampagne %}
1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie dann **Kampagne erstellen**.
2. Für Kampagnen auf mehreren Kanälen wählen Sie **Multichannel**. Andernfalls wählen Sie **Push-Benachrichtigung**. Wenn Sie sich immer noch nicht sicher sind, lesen Sie den Abschnitt **Entscheidung zwischen regulärer oder Multichannel-Push-Kampagne** weiter unten.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu. **Tipp:** Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Auswahl zwischen regulärer und kanalübergreifender Push-Kampagne %}

Wenn Sie beabsichtigen, mehrere Geräte und Plattformen anzusprechen, z. B. eine beliebige Kombination aus Mobile, Web, Kindle, iOS und Android, kann Ihre Auswahl in diesem Schritt die Verfügbarkeit einiger Funktionen und Einstellungen später beeinflussen.

Bevor Sie eine Multichannel- oder Push-Kampagne erstellen, beachten Sie auf diesen Chart:

!["Flussdiagramm für die Auswahl der Kampagnenart. Entscheiden Sie zunächst, ob Sie mehrere Geräte und Plattformen ansprechen wollen. Falls nicht, gehen Sie auf "Push-Benachrichtigung auswählen". Falls ja, wird die Frage "Welche Art von Push-Benachrichtigung?" gestellt. Die Optionen sind "Standard-Push" und die Frage "Gerätespezifische Einstellungen verwenden?". Falls nicht, erscheint die Meldung "Push-Benachrichtigung auswählen und Quick-Push verwenden". Falls ja, gehen Sie zu "Multichannel auswählen". Zurück zu "Welche Art von Push-Benachrichtigung?": Wenn die Antwort "Push-Storys oder Inline-Bild" lautet, wird auf "Multichannel auswählen" verwiesen.]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Wenn Sie **Push-Benachrichtigung** auswählen und mehrere Geräte und Plattformen als Ziel wählen, erstellen Sie automatisch eine schnelle Push-Kampagne. Bei Quick Push sind bestimmte gerätespezifische Einstellungen nicht verfügbar:

- Push-Action-Buttons
- Benachrichtigungskanäle und Gruppen
- Push-Time-to-Live (TTL)
- Priorität anzeigen
- Töne

Sehen Sie sich die [Quick-Push-Kampagnen]({{site.baseurl}}/quick_push) an, um zu verstehen, was bei dieser Bearbeitungsmethode anders ist, bevor Sie fortfahren.

{% enddetails %}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie die Zielgruppe für diesen Schritt nach Bedarf. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie andere Messaging-Kanäle, die Sie mit Ihrer Nachricht verknüpfen möchten.

{% endtab %}
{% endtabs %}

## Schritt 2: Plattformen für die Zustellung angeben

Wählen Sie zunächst aus, welche Kombination aus Gerät und Plattform den Push erhalten soll. Verwenden Sie diese Auswahl, um die Zustellung einer Push-Benachrichtigung auf eine bestimmte Gruppe von Apps zu beschränken.

Es gibt verschiedene Möglichkeiten, dies zu tun, je nachdem, was Sie zuvor ausgewählt haben:

| Vorherige Auswahl | Optionen |
| --- | --- | 
| Push-Benachrichtigungskampagne | Wählen Sie eine oder mehrere Plattformen und Geräte aus. Wenn Sie sich für das Targeting mehrerer Geräte und Plattformen entscheiden, erstellen Sie automatisch eine schnelle Push-Kampagne. Diese ermöglicht eine optimierte Anpassung der Nachricht an die ausgewählten Plattformen in einem Editor. Unter [Schnelle Push-Kampagnen]({{site.baseurl}}/quick_push) erfahren Sie, was hier bei der Bearbeitung anders ist. |
| Multichannel-Kampagne | Wählen Sie **Messaging-Kanal hinzufügen**, um weitere Push-Plattformen hinzuzufügen. Da die Plattformauswahl variantenspezifisch ist, können Sie das Nachrichtenengagement auf den einzelnen Plattformen testen.
| Canvas | Wählen Sie in Ihrem Schritt Nachricht **\+ Weitere hinzufügen**, um weitere Push-Plattformen hinzuzufügen. Ähnlich wie bei Multichannel-Kampagnen ist die Plattformauswahl variantenspezifisch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 3: Benachrichtigungstyp auswählen (iOS und Android)

Wenn Sie eine Quick-Push-Kampagne erstellen, ist der Benachrichtigungstyp automatisch auf Standard-Push eingestellt und kann nicht geändert werden.

![Benachrichtigungstyp mit der Auswahl Standard-Push als Beispiel.][3]{: style="float:right;max-width:40%;margin-left:15px;"}

Andernfalls wählen Sie für iOS und Android Ihre Benachrichtigungsart aus:

- Standard-Push
- [Push-Storys]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Inline-Bild (nur Android)

Wenn Sie Bilder in Ihre Push-Kampagne einbinden möchten, lesen Sie die folgenden Anleitungen zur Erstellung einer Rich Notification für [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) oder [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## Schritt 4: Verfassen Sie Ihre Push-Nachricht

Jetzt ist es an der Zeit, Ihre Push-Nachricht zu schreiben! Auf der Registerkarte **Verfassen** können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Registerkarte "Verfassen" zum Erstellen einer Push-Benachrichtigung.]({% image_buster /assets/img_archive/push_compose.png %})

Der Inhalt der Registerkarte **Verfassen** hängt von der Art der Benachrichtigung ab, die Sie im vorherigen Schritt ausgewählt haben, kann aber eine der folgenden Optionen enthalten:

#### Benachrichtigungskanal oder Gruppe (iOS und Android)

Weitere Informationen zu plattformspezifischen Benachrichtigungsoptionen finden Sie unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) oder [Android-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Sprache

Fügen Sie über den Button **Sprachen hinzufügen** Texte in mehreren Sprachen hinzu. Wir empfehlen, die Sprachen auszuwählen, bevor Sie den Inhalt verfassen, damit Sie Ihren Text dort einfügen können, wo er im Liquid hingehört. Eine vollständige Liste der Sprachen, die Sie verwenden können, finden Sie unter [Unterstützte Sprachen][18]].

Wenn Sie Texte in einer Sprache hinzufügen, die von rechts nach links geschrieben ist, beachten Sie, dass das endgültige Aussehen von Nachrichten von rechts nach links weitgehend davon abhängt, wie die Dienste sie darstellen. 

#### Titel und Text

{% tabs local %}
{% tab ios %}
Beginnen Sie mit der Eingabe in das Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld auf der linken Seite erscheint. Push-Nachrichten müssen im Klartext formatiert sein. 

Fügen Sie eine Überschrift in das Feld **Titel** ein. Um Ihre Push-Nachrichten personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) einbeziehen.
{% endtab %}

{% tab android %}
Beginnen Sie mit der Eingabe in das Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld auf der linken Seite erscheint. Push-Nachrichten müssen im Klartext formatiert sein. 

Um Ihre Push-Nachrichten personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) einbeziehen.

{% alert important %}
Sie **können** eine Android-Push-Nachricht **nicht** ohne Titel versenden. Sie können jedoch stattdessen ein einzelnes Leerzeichen eingeben. Denken Sie daran: Wenn Ihre Nachricht nur ein einziges Leerzeichen enthält, wird sie als stille Push-Benachrichtigung gesendet. 
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein und die KI generiert menschenähnliche Marketingtexte für Ihre Werbebotschaften.

![Gehen Sie auf den Button "KI-Texter" im Textfeld des Push-Editors.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Bild

Wo dies unterstützt wird, wird Ihr App-Symbol automatisch als Bild für Ihre Push-Benachrichtigung hinzugefügt. Sie haben auch die Möglichkeit, Rich Notifications zu versenden, mit denen Sie Ihre Push-Benachrichtigungen noch individueller gestalten können, indem Sie neben dem Text zusätzliche Inhalte hinzufügen.

Weitere Hinweise zur Verwendung von Bildern in Ihren Push-Benachrichtigungen finden Sie in den folgenden Artikeln:

- [Rich-Benachrichtigungen für iOS erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Rich-Benachrichtigungen für Android erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

#### On-Click-Verhalten

Legen Sie mit **On-Click Behavior** fest, was passiert, wenn ein Benutzer den Text einer Push-Benachrichtigung auswählt. Sie können Kunden beispielsweise auffordern, Ihre Anwendung zu öffnen, Kunden zu einer bestimmten Web-URL umleiten oder sogar eine bestimmte Seite Ihrer Anwendung mit einem [Deep Link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) öffnen.

Hier können Sie auch Button-Aufforderungen innerhalb Ihrer Push-Benachrichtigung einrichten, wie z.B.:

- Akzeptieren/Ablehnen
- Ja/Nein
- Bestätigen/Abbrechen
- Mehr 

#### Geräteoptionen

Wenn ein Benutzer Ihre App auf mehreren Geräten installiert hat, wird Ihre Push-Nachricht standardmäßig an alle Geräte gesendet, denen ein gültiges Push-Token zugewiesen wurde. Falls gewünscht, können Sie auswählen, dass **dieser Push nur an das zuletzt verwendete Gerät des Nutzers:innen gesendet wird**.

![Aktivieren Sie das Kontrollkästchen Geräteoptionen, um diesen Push nur an das zuletzt verwendete Gerät des Nutzers:innen zu senden.][9]{: style="max-width:70%;" }

Für diese Einstellung gibt es einige Nuancen. Wenn Sie diese Option auswählen, schränkt Braze Mehrfachsendungen ein, sofern die Kampagne nicht auf mehrere Plattformen abzielt, also z. B. sowohl auf iOS als auch auf Android. Wenn der Nutzer Ihre App sowohl auf einem iOS- als auch auf einem Android-Gerät hat, erhält er einen Push für beide Plattformen. Wenn das zuletzt verwendete Gerät eines Benutzers nicht [Push-fähig]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-enabled) ist, wird die Nachricht nicht gesendet.

Für iOS können Sie das Messaging weiter einschränken, indem Sie Push-Benachrichtigungen nur an iPads oder nur an iPhones und iPods senden.

## Schritt 5: Nachrichtenvorschau anzeigen und testen (optional)

![Push-Nachrichten testen][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Das Testen ist wohl einer der wichtigsten Schritte. Nachdem Sie Ihre perfekte Push-Nachricht verfasst haben, testen Sie sie, bevor Sie sie verschicken. Wählen Sie die Registerkarte **Test** und verwenden Sie **Vorschau der Nachricht als Benutzer**, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht auf dem Handy aussehen könnte. Verwenden Sie **Test senden**, um einen Test-Push zu senden und sicherzustellen, dass Ihre Nachricht richtig angezeigt wird.

## Schritt 6: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Kampagne %}

Erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools zur Erstellung von Push-Benachrichtigungen am besten einsetzen.

#### Wählen Sie einen Zeitplan für die Zustellung oder triggern Sie

Push-Benachrichtigungen können nach Zeitplan oder abhängig von einer Aktion oder einem API-Trigger zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. dass Nutzer:innen [wieder für]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) den Empfang der Kampagne [zugelassen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) werden oder [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) aktiviert werden.

#### Wählen Sie Benutzer als Zielgruppe aus

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/). Sie erhalten automatisch einen Überblick über die ungefähre Zusammensetzung dieses Segments. Detaillierte Zielgruppenstatistiken für die angesprochenen Kanäle finden Sie in der Fußzeile. Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird und wie hoch der Lifetime Value für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.

{% details Warum stimmt meine Metrik "Erreichbare Benutzer insgesamt" nicht mit der Summe aller Kanäle überein? %}

Wenn Sie die Gesamtzahl der erreichbaren Nutzer für Ihre gefilterte Zielgruppe ansehen, werden Sie feststellen, dass die Summe der einzelnen Spalten kleiner ist als die Gesamtzahl der erreichbaren Nutzer. Diese Lücke ist in der Regel darauf zurückzuführen, dass es eine Reihe von Nutzern gibt, die sich für das Segment oder die Filter in der Kampagne qualifizieren, aber nicht über Push erreichbar sind (z. B. weil sie keine gültigen oder aktiven [Push-Tokens]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) haben).

{% enddetails %}

![Tabelle mit detaillierten Zielgruppenstatistiken für erreichbare Nutzer:innen.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Nachrichtenversand ermittelt wird.

Sie können Ihre Kampagne auch nur an Benutzer mit einem bestimmten [Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) senden, z. B. an diejenigen, die ein Abonnement abgeschlossen und sich für Push-Nachrichten angemeldet haben.

Optional können Sie auch die Zustellung auf eine bestimmte Anzahl von Nutzern innerhalb des Segments beschränken oder zulassen, dass Nutzer die gleiche Nachricht bei einer Wiederholung der Kampagne zweimal erhalten.

##### Mehrkanalige Kampagnen mit E-Mail und Push

Bei Multichannel-Kampagnen, die sowohl auf E-Mail- als auch auf Push-Kanäle abzielen, möchten Sie Ihre Kampagne möglicherweise so einschränken, dass nur die Nutzer, die sich explizit dafür entschieden haben, die Nachricht zu erhalten (unter Ausschluss der abonnierten oder abgemeldeten Nutzer). Nehmen wir an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzerin A** hat E-Mails abonniert und ist Push-aktiviert. Diese Nutzer:innen erhalten die E-Mail nicht, aber den Push.
- **Benutzer B** hat sich für E-Mails entschieden, ist aber nicht für Push aktiviert. Dieser Benutzer erhält die E-Mail, aber nicht die Push-Mitteilung.
- **Nutzer C** hat in E-Mails eingewilligt und ist Push-aktiviert. Dieser Benutzer erhält sowohl die E-Mail als auch die Push-Mitteilung.

Wählen Sie dazu unter **Zusammenfassung der Zielgruppe** aus, dass diese Kampagne nur an "Opt-in Nutzer:innen" gesendet werden soll. Mit dieser Option stellen Sie sicher, dass nur Nutzer, die sich dafür entschieden haben, Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachrichten nur an Nutzer, die standardmäßig für Push aktiviert sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielbenutzer** ein, die die Zielgruppe auf einen einzigen Kanal beschränken (z. B. `Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

#### Wählen Sie Konversionsereignisse aus

 Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 7: Überprüfen und loslegen {#review-and-deploy-push}

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details. Bei Kampagnen erhalten Sie auf der letzten Seite eine Zusammenfassung der Kampagne, die Sie gerade entworfen haben. Überprüfen Sie alle wichtigen Details und vergewissern Sie sich, dass Sie die Nachricht getestet haben. Nun können Sie sie absenden und beobachten, wie die Daten bei Ihnen eintrudeln!

Sehen Sie sich als nächstes die [Push-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Push-Kampagne zugreifen können. Für Push-Benachrichtigungen können Sie Statistiken über die Anzahl der gesendeten, zugestellten, abgeprallten, geöffneten und direkt geöffneten Nachrichten einsehen.

[1]: {% image_buster /assets/img_archive/new_campaign_push.png %}
[2]: {% image_buster /assets/img_archive/push_1.png %}
[3]: {% image_buster /assets/img_archive/push_2.png %}
[4]: {% image_buster /assets/img_archive/schedule.png %}
[5]: {% image_buster /assets/img_archive/confirmation_page.png %}
[6]: {% image_buster /assets/img_archive/push-results-statistics.png %}
[7]: {% image_buster /assets/img_archive/push_3.png %}
[8]: https://www.braze.com/customers
[9]: {% image_buster /assets/img_archive/push_recent_device.png %}
[15]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %} 
