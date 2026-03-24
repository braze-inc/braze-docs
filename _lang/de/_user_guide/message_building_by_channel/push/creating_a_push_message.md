---
nav_title: Erstellen Sie eine Push-Nachricht
article_title: Erstellen Sie eine Push-Kampagne
page_order: 4
page_type: tutorial
description: "Diese Tutorial-Seite behandelt die verschiedenen Komponenten, die bei der Erstellung einer Push-Nachricht eine Rolle spielen, einschließlich Konfiguration, Versand, Zielgruppen und mehr."
channel: push
tool:
  - Campaigns
  
---

# Erstellen Sie eine Push-Nachricht

> Push-Benachrichtigungen eignen sich hervorragend für zeitkritische Handlungsaufforderungen und um Nutzer:innen, die die App schon länger nicht mehr besucht haben, wieder zu aktivieren. Erfolgreiche Push-Kampagnen führen Nutzer:innen direkt zum Inhalt und demonstrieren den Wert Ihrer App. Beispiele für Push-Benachrichtigungen finden Sie in unseren [Anwendungsbeispielen](https://www.braze.com/customers).

## 1. Schritt: Entscheiden Sie, wo Sie Ihre Nachricht erstellen möchten {#create-new-campaign-push}

{% alert tip %}
Sie sind sich nicht sicher, ob Sie eine Kampagne oder ein Canvas verwenden sollen? Kampagnen eignen sich besser für einzelne, zielgerichtete Messaging-Kampagnen, während Canvase besser für mehrstufige User Journeys geeignet sind.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie dann **Kampagne erstellen**.
2. Für Kampagnen auf mehreren Kanälen wählen Sie **Multichannel**. Andernfalls wählen Sie **Push-Benachrichtigung**. Wenn Sie sich immer noch nicht sicher sind, lesen Sie den Abschnitt **Entscheidung zwischen regulärer oder Multichannel-Push-Kampagne** weiter unten.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu. 

{% alert tip %} 
Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

{: start="5"}
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% details Entscheidung zwischen regulärer oder Multichannel-Push-Kampagne %}

Wenn Sie beabsichtigen, mehrere Geräte und Plattformen anzusprechen, z. B. eine beliebige Kombination aus Mobilgerät, Web, Kindle, iOS und Android, kann Ihre Auswahl in diesem Schritt die Verfügbarkeit einiger Features und Einstellungen später beeinflussen.

Bevor Sie eine Multichannel- oder Push-Benachrichtigungskampagne erstellen, beachten Sie das folgende Entscheidungsdiagramm:

![„Flussdiagramm für die Auswahl der Kampagnenart. Entscheiden Sie zunächst, ob Sie mehrere Geräte und Plattformen ansprechen wollen. Falls nicht, gehen Sie auf ‚Push-Benachrichtigung auswählen'. Falls ja, wird die Frage ‚Welche Art von Push-Nachricht?' gestellt. Die Optionen sind ‚Standard-Push' und die Frage ‚Gerätespezifische Einstellungen verwenden?'. Falls nicht, erscheint ‚Push-Benachrichtigung auswählen und Quick-Push verwenden'. Falls ja, gehen Sie zu ‚Multichannel auswählen'. Zurück zu ‚Welche Art von Push-Nachricht?'. Wenn die Antwort ‚Push-Storys oder Inline-Bild' lautet, werden Sie zu ‚Multichannel auswählen' weitergeleitet."]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Wenn Sie **Push-Benachrichtigung** auswählen und mehrere Geräte und Plattformen als Ziel wählen, erstellen Sie automatisch eine Quick-Push-Kampagne. Bei Quick Push sind bestimmte gerätespezifische Einstellungen nicht verfügbar:

- Push-Action-Buttons
- Benachrichtigungskanäle und -gruppen
- Push-Time-to-Live (TTL)
- Anzeigepriorität
- Töne

Bevor Sie fortfahren, lesen Sie bitte [Quick-Push-Kampagnen]({{site.baseurl}}/quick_push), um zu verstehen, was bei dieser Bearbeitung anders ist.

{% enddetails %}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie die Zielgruppe für diesen Schritt nach Bedarf. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppenoptionen werden nach der Verzögerung zum Versandzeitpunkt überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie weitere Messaging-Kanäle aus, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## 2. Schritt: Push-Plattformen auswählen

Wählen Sie als Nächstes, welche Kombination aus Plattform und Mobilgerät den Push erhalten soll. Verwenden Sie diese Auswahl, um die Zustellung einer Push-Benachrichtigung auf eine bestimmte Gruppe von Apps zu beschränken.

Es gibt verschiedene Möglichkeiten, dies zu tun, je nachdem, was Sie zuvor ausgewählt haben:

| Vorherige Auswahl | Optionen |
| --- | --- | 
| Push-Benachrichtigungskampagne | Wählen Sie eine oder mehrere Plattformen und Geräte aus. Wenn Sie sich für das Targeting mehrerer Geräte und Plattformen entscheiden, erstellen Sie automatisch eine Quick-Push-Kampagne. Diese ermöglicht eine optimierte Bearbeitung, um eine Nachricht für alle ausgewählten Plattformen in einem einzigen Editor zu erstellen. Unter [Quick-Push-Kampagnen]({{site.baseurl}}/quick_push) erfahren Sie, was bei dieser Bearbeitung anders ist. |
| Multichannel-Kampagne | Wählen Sie **Messaging-Kanal hinzufügen**, um weitere Push-Plattformen hinzuzufügen. Da die Plattformauswahl variantenspezifisch ist, können Sie das Nachrichten-Engagement auf den einzelnen Plattformen testen.
| Canvas | Wählen Sie in Ihrem Nachrichten-Schritt **+ Weitere hinzufügen**, um weitere Push-Plattformen hinzuzufügen. Ähnlich wie bei Multichannel-Kampagnen ist die Plattformauswahl variantenspezifisch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 3. Schritt: Benachrichtigungstyp auswählen (iOS und Android)

Wenn Sie eine Quick-Push-Kampagne erstellen, ist der Benachrichtigungstyp automatisch auf **Standard-Push** eingestellt und kann nicht geändert werden.

![Benachrichtigungstyp mit der Auswahl Standard-Push als Beispiel.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Andernfalls wählen Sie für iOS und Android Ihren Benachrichtigungstyp aus:

- Standard-Push
- [Push-Storys]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)
- Inline-Bild (nur Android)

Wenn Sie Bilder in Ihre Push-Kampagne einbinden möchten, lesen Sie die folgenden Anleitungen zur Erstellung einer Rich-Benachrichtigung für [iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) oder [Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/).

## 4. Schritt: Verfassen Sie Ihre Push-Nachricht

Jetzt ist es an der Zeit, Ihre Push-Nachricht zu schreiben! Auf dem Tab **Verfassen** können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Tab „Verfassen" zum Erstellen einer Push-Benachrichtigung.]({% image_buster /assets/img_archive/push_compose.png %})

Der Inhalt des Tabs **Verfassen** hängt von der Art der Benachrichtigung ab, die Sie im vorherigen Schritt ausgewählt haben, kann aber eine der folgenden Optionen enthalten:

#### Benachrichtigungskanal oder -gruppe (iOS und Android)

Weitere Informationen zu plattformspezifischen Benachrichtigungsoptionen finden Sie unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) oder [Android-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/).

#### Sprache

Fügen Sie über den Button **Sprachen hinzufügen** Texte in mehreren Sprachen hinzu. Wir empfehlen, die Sprachen auszuwählen, bevor Sie den Inhalt verfassen, damit Sie Ihren Text dort einfügen können, wo er im Liquid hingehört. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Wenn Sie Texte in einer Sprache hinzufügen, die von rechts nach links geschrieben wird, beachten Sie, dass das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten weitgehend davon abhängt, wie die Anbieter sie darstellen. Bewährte Methoden zur Erstellung von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Titel und Text

{% tabs local %}
{% tab ios %}
Beginnen Sie mit der Eingabe in das Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld auf der linken Seite erscheint. Push-Nachrichten müssen im Klartext formatiert sein. 

Fügen Sie eine Überschrift über das Feld **Titel** hinzu. Um Ihre Push-Nachrichten personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) einbeziehen.
{% endtab %}

{% tab android %}
Beginnen Sie mit der Eingabe in das Nachrichtenfeld und beobachten Sie, wie eine Vorschau im Vorschaufeld auf der linken Seite erscheint. Push-Nachrichten müssen im Klartext formatiert sein. 

Um Ihre Push-Nachrichten personalisiert und zielgerichtet zu gestalten, können Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) einbeziehen.

{% alert important %}
Sie **können** eine Android-Push-Nachricht **nicht** ohne Titel versenden – Sie können jedoch stattdessen ein einzelnes Leerzeichen eingeben. Beachten Sie: Wenn Ihre Nachricht nur ein einziges Leerzeichen enthält, wird sie als stille Push-Benachrichtigung gesendet. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihre Nachrichten.

![Button „KI-Textwerkstatt starten" im Textfeld des Push-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Bild

Wo dies unterstützt wird, wird Ihr App-Symbol automatisch als Bild für Ihre Push-Benachrichtigung hinzugefügt. Sie haben auch die Möglichkeit, Rich-Benachrichtigungen zu versenden, mit denen Sie Ihre Push-Benachrichtigungen noch individueller gestalten können, indem Sie neben dem Text zusätzliche Inhalte hinzufügen.

Weitere Hinweise zur Verwendung von Bildern in Ihren Push-Benachrichtigungen finden Sie in den folgenden Artikeln:

- [Rich-Benachrichtigungen für iOS erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)
- [Rich-Benachrichtigungen für Android erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### On-Click-Verhalten

Legen Sie mit **On-Click Behavior** fest, was passiert, wenn Nutzer:innen den Text einer Push-Benachrichtigung auswählen. Sie können beispielsweise Kund:innen auffordern, Ihre Anwendung zu öffnen, sie zu einer bestimmten Web-URL weiterleiten oder sogar eine bestimmte Seite Ihrer Anwendung mit einem [Deeplink]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) öffnen.

Hier können Sie auch Button-Aufforderungen innerhalb Ihrer Push-Benachrichtigung einrichten, wie z. B.:

- Akzeptieren/Ablehnen
- Ja/Nein
- Bestätigen/Abbrechen
- Mehr 

#### Sende-Optionen

Wenn Nutzer:innen Ihre App auf mehreren Geräten installiert haben, wird Ihre Push-Nachricht standardmäßig an alle Geräte gesendet, denen ein gültiges Push-Token zugewiesen wurde. Falls gewünscht, können Sie **Zuletzt verwendetes Gerät** auswählen.

![Kontrollkästchen für Geräteoptionen, um diesen Push nur an das zuletzt verwendete Gerät der Nutzer:innen zu senden.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }


Standardmäßig sendet Braze Nachrichten an jedes Gerät, das Nutzer:innen besitzen und das ein gültiges Push-Token hat. Für iOS können Sie Ihre Reichweite weiter eingrenzen, indem Sie Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

Falls gewünscht, können Sie das Push-Ziel auf **Zuletzt verwendetes Gerät** einstellen. 

##### Zuletzt verwendetes Gerät

„Zuletzt verwendet" ist ein technischer Status, kein verhaltensbezogener. Da Braze standardmäßig alle Geräte anspricht, schränkt der Wechsel zu dieser Einstellung Ihre Reichweite erheblich ein und basiert ausschließlich auf dem Status des einzelnen Geräts mit dem neuesten Token.

![Kontrollkästchen für Geräteoptionen, um diesen Push nur an das zuletzt verwendete Gerät der Nutzer:innen zu senden.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Das zuletzt verwendete Gerät wird anhand des Geräts mit dem zuletzt aktualisierten Push-Token bestimmt, nicht anhand des Geräts mit der letzten Sitzung. 
* Wenn ein Push-Token eines neuen Geräts über die API zu einem Nutzerprofil hinzugefügt wird, gilt dieses Gerät sofort als zuletzt verwendet, auch wenn die Nutzer:innen noch keine Sitzung darauf gestartet haben. 
* Wenn das zuletzt verwendete Gerät von Nutzer:innen nicht [Push-fähig]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#foreground-push-enabled) ist, wird die Nachricht überhaupt nicht gesendet.

Mehrfachsendungen können dennoch auftreten, wenn eine Kampagne verschiedene Plattformen anspricht, z. B. sowohl iOS als auch Android. Wenn Nutzer:innen die App auf beiden Plattformen haben, können sie einen Push für beide Plattformen erhalten.

Für iOS können Sie das Messaging weiter einschränken, indem Sie Push-Benachrichtigungen nur an iPad-Geräte oder nur an iPhone- und iPod-Geräte senden.

## 5. Schritt: Nachrichtenvorschau anzeigen und testen (optional)

Das Testen ist wohl einer der wichtigsten Schritte. Nachdem Sie Ihre perfekte Push-Nachricht verfasst haben, testen Sie sie, bevor Sie sie verschicken. Wählen Sie den Tab **Test** aus, um die Optionen zum Testen Ihrer Push-Nachricht anzuzeigen. Unter **Testempfänger:innen** können Sie eine Inhalts-Testgruppe oder einzelne Nutzer:innen auswählen. Sie können auch **Nachrichtenvorschau als Nutzer:in** verwenden, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht auf dem Mobilgerät für zufällige Nutzer:innen, bestehende Nutzer:innen, angepasste Nutzer:innen oder mehrsprachige Nutzer:innen aussehen könnte.

## 6. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools zur Erstellung von Push-Benachrichtigungen am besten einsetzen.

#### Wählen Sie einen Zeitplan für die Zustellung oder einen Trigger

Push-Nachrichten können nach Zeitplan, abhängig von einer Aktion oder über einen API-Trigger zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. dass Nutzer:innen wieder für den Empfang der Kampagne [zugelassen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) werden oder [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) aktiviert werden.

#### Zielgruppe auswählen

Als Nächstes müssen Sie die [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau, wie die ungefähre Segmentpopulation aussieht. Detaillierte Zielgruppenstatistiken für die angesprochenen Kanäle finden Sie in der Fußzeile. Um zu sehen, welcher Prozentsatz Ihrer Nutzerbasis angesprochen wird und wie hoch der Lifetime-Value für dieses Segment ist, wählen Sie **Zusätzliche Statistiken anzeigen**.

{% multi_lang_include target_audiences.md %}

{% details Warum stimmt meine Metrik „Gesamtzahl erreichbarer Nutzer:innen" nicht mit der Summe aller Kanäle überein? %}

Wenn Sie die Gesamtzahl der erreichbaren Nutzer:innen für Ihre gefilterte Zielgruppe ansehen, werden Sie möglicherweise feststellen, dass die Summe der einzelnen Spalten kleiner ist als die Gesamtzahl der erreichbaren Nutzer:innen. Diese Lücke entsteht in der Regel dadurch, dass es Nutzer:innen gibt, die sich für das Segment oder die Filter in der Kampagne qualifizieren, aber nicht über Push erreichbar sind (z. B. weil sie keine gültigen oder aktiven [Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) haben).

{% enddetails %}

![Tabelle mit detaillierten Zielgruppenstatistiken für erreichbare Nutzer:innen.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Bitte beachten Sie, dass die genaue Segmentzugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

Sie können Ihre Kampagne auch nur an Nutzer:innen mit einem bestimmten [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) senden, z. B. an diejenigen, die abonniert und für Push angemeldet sind.

Optional können Sie auch die Zustellung auf eine bestimmte Anzahl von Nutzer:innen innerhalb des Segments beschränken oder zulassen, dass Nutzer:innen die gleiche Nachricht bei einer Wiederholung der Kampagne zweimal erhalten.

##### Multichannel-Kampagnen mit E-Mail und Push

Bei Multichannel-Kampagnen, die sowohl auf E-Mail- als auch auf Push-Kanäle abzielen, möchten Sie Ihre Kampagne möglicherweise so einschränken, dass nur Nutzer:innen, die sich explizit dafür entschieden haben, die Nachricht erhalten (unter Ausschluss der abonnierten oder abgemeldeten Nutzer:innen). Nehmen wir an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in A** ist auf E-Mail abonniert und hat Push aktiviert. Diese Person erhält die E-Mail nicht, aber den Push.
- **Nutzer:in B** hat Opt-in für E-Mail, ist aber nicht für Push aktiviert. Diese Person erhält die E-Mail, aber nicht den Push.
- **Nutzer:in C** hat Opt-in für E-Mail und ist für Push aktiviert. Diese Person erhält sowohl die E-Mail als auch den Push.

Wählen Sie dazu unter **Zusammenfassung der Zielgruppe** aus, dass diese Kampagne nur an „Opt-in-Nutzer:innen" gesendet werden soll. Mit dieser Option stellen Sie sicher, dass nur Nutzer:innen mit Opt-in Ihre E-Mail erhalten, und Braze sendet Ihren Push standardmäßig nur an Nutzer:innen, die für Push aktiviert sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielgruppen** ein, die die Zielgruppe auf einen einzigen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

#### Wählen Sie Konversions-Events aus

Mit Braze können Sie nachverfolgen, wie oft Nutzer:innen nach Erhalt einer Kampagne bestimmte Aktionen, d. h. [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion durchführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte Ihrer Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## 7. Schritt: Überprüfen und loslegen {#review-and-deploy-push}

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details. Bei Kampagnen erhalten Sie auf der letzten Seite eine Zusammenfassung der von Ihnen gestalteten Kampagne. Überprüfen Sie alle wichtigen Details, vergewissern Sie sich, dass Sie Ihre Nachricht getestet haben, und senden Sie sie ab – dann beobachten Sie, wie die Daten eintrudeln!

Sehen Sie sich als Nächstes die [Push-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Push-Kampagne zugreifen können. Für Push-Benachrichtigungen können Sie Statistiken über die Anzahl der gesendeten, zugestellten, abgesprungenen, geöffneten und direkt geöffneten Nachrichten einsehen.