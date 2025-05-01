---
nav_title: Fehlersuche
article_title: Fehlerbehebung bei In-App-Nachrichten für iOS
platform: iOS
page_order: 7
description: "Dieser Referenzartikel befasst sich mit der möglichen Fehlerbehebung bei iOS In-App-Nachrichten."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fehlersuche bei In-App-Nachrichten

## Impressionen

#### Impressions- oder Klick-Analysen werden nicht protokolliert

Wenn Sie einen Delegaten für In-App-Nachrichten so festgelegt haben, dass die Anzeige von Nachrichten oder Klickaktionen manuell gesteuert wird, müssen Sie Klicks und Impressionen für die In-App-Nachricht manuell protokollieren.

#### Die Eindrücke sind geringer als erwartet

Die Synchronisierung der Auslöser mit dem Gerät beim Start der Sitzung nimmt einige Zeit in Anspruch, so dass es zu einer Race-Condition kommen kann, wenn Benutzer ein Event oder einen Kauf direkt nach dem Start einer Sitzung protokollieren. Ein möglicher Ausweg könnte darin bestehen, die Kampagne so zu ändern, dass sie beim Start der Sitzung getriggert wird, und dann nach dem beabsichtigten Event oder Kauf zu segmentieren. Beachten Sie, dass dies die In-App-Nachricht beim nächsten Sitzungsstart nach Eintreten des Events liefern würde.

## Die erwartete In-App-Nachricht wurde nicht angezeigt

Die meisten Probleme mit In-App-Nachrichten lassen sich in zwei Hauptkategorien unterteilen: Zustellung und Anzeige. Um herauszufinden, warum eine erwartete In-App-Nachricht nicht auf Ihrem Gerät angezeigt wurde, sollten Sie zunächst sicherstellen, dass die [In-App-Nachricht an das Gerät übermittelt wurde](#troubleshooting-in-app-message-delivery), und dann [das Problem mit der Anzeige der Nachricht beheben](#troubleshooting-in-app-message-display).

### Zustellung von In-App-Nachrichten {#troubleshooting-in-app-message-delivery}

Das SDK fordert beim Start der Sitzung In-App-Nachrichten von den Braze-Servern an. Um zu überprüfen, ob In-App-Nachrichten an Ihr Gerät geliefert werden, müssen Sie sicherstellen, dass In-App-Nachrichten sowohl vom SDK angefordert als auch von den Braze-Servern zurückgegeben werden.

#### Prüfen Sie, ob Nachrichten angefordert und zurückgeschickt werden

1. Fügen Sie sich als [Testbenutzer]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) auf dem Dashboard hinzu.
2. Richten Sie eine In-App-Nachrichtenkampagne ein, die sich an Ihren Nutzer richtet.
3. Stellen Sie sicher, dass in Ihrer Anwendung eine neue Sitzung stattfindet.
4. Verwenden Sie das [Event Benutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu überprüfen, ob Ihr Gerät beim Start der Sitzung In-App-Nachrichten anfordert. Suchen Sie die SDK-Anfrage, die mit dem Sitzungsstart-Event Ihres Testbenutzers verbunden ist.
  - Wenn Ihre App ausgelöste In-App-Nachrichten anfordern sollte, sollten Sie `trigger` im Feld **Angeforderte Antworten** unter **Antwortdaten** sehen.
  - Wenn Ihre App dazu gedacht war, originale In-App-Nachrichten anzufordern, sollten Sie `in_app` im Feld **Angeforderte Antworten** unter **Antwortdaten** sehen.
5. Verwenden Sie die [Event-Benutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu überprüfen, ob die richtigen In-App-Nachrichten in den Antwortdaten zurückgegeben werden.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Fehlerbehebung bei nicht angeforderten Nachrichten

Wenn Ihre In-App-Nachrichten nicht angefordert werden, kann es sein, dass Ihre App die Sitzungen nicht korrekt verfolgt, da die In-App-Nachrichten beim Start der Sitzung aktualisiert werden. Vergewissern Sie sich außerdem, dass Ihre App tatsächlich eine Sitzung gemäß der Semantik des Sitzungs-Timeouts Ihrer App startet:

![Die SDK-Anfrage, die in den Ereignisbenutzerprotokollen gefunden wurde, die ein erfolgreiches Sitzungsstart-Event anzeigen.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Fehlerbehebung bei nicht zurückgegebenen Nachrichten

Wenn Ihre In-App-Nachrichten nicht zurückgeschickt werden, liegt wahrscheinlich ein Problem mit dem Targeting Ihrer Kampagne vor:

- Ihr Segment enthält nicht Ihren Benutzer.
  - Überprüfen Sie auf der Registerkarte [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab), ob das richtige Segment unter **Segmente** erscheint.
- Ihr Nutzer hat die In-App-Nachricht bereits erhalten und war nicht berechtigt, sie erneut zu erhalten.
  - Überprüfen Sie die [Einstellungen für die Wiederzulassung von Kampagnen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) unter dem Schritt **Zustellung** des **Campaign Composers** und stellen Sie sicher, dass die Einstellungen für die Wiederzulassung mit Ihrer Testkonfiguration übereinstimmen.
- Ihr Benutzer hat die Höchstfrequenz für die Kampagne erreicht.
  - Überprüfen Sie die Einstellungen für die Kampagne [Frequenzobergrenze]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) und stellen Sie sicher, dass sie mit Ihrer Testkonfiguration übereinstimmen.
- Wenn es in der Kampagne eine Kontrollgruppe gab, könnte Ihr Benutzer in die Kontrollgruppe gefallen sein.
  - Sie können überprüfen, ob dies geschehen ist, indem Sie ein Segment mit einem Filter für empfangene Kampagnenvarianten erstellen, bei dem die Kampagnenvariante auf **Kontrolle** eingestellt ist, und überprüfen, ob Ihr Nutzer in dieses Segment fällt.
  - Wenn Sie Kampagnen für Integrationstests erstellen, achten Sie darauf, dass Sie keine Kontrollgruppe hinzufügen.

### Anzeige von In-App-Nachrichten {#troubleshooting-in-app-message-display}

Wenn Ihre App erfolgreich In-App-Nachrichten anfordert und empfängt, diese aber nicht angezeigt werden, verhindert möglicherweise eine geräteseitige Logik die Anzeige:

- Getriggerte In-App-Nachrichten werden auf der Grundlage des [minimalen Zeitintervalls zwischen den Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), das standardmäßig 30 Sekunden beträgt, begrenzt.
- Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, überprüfen Sie Ihren Delegaten, um sicherzustellen, dass er die Anzeige der In-App-Nachrichten nicht beeinträchtigt.
- Wenn das Herunterladen von Bildern fehlschlägt, werden In-App-Nachrichten mit Bildern nicht mehr angezeigt. Das Herunterladen von Bildern schlägt immer fehl, wenn das Framework `SDWebImage` nicht richtig integriert ist. Überprüfen Sie Ihre Geräteprotokolle, um sicherzustellen, dass das Herunterladen von Bildern nicht fehlschlägt.
- Wenn die Ausrichtung des Geräts nicht mit der von der In-App-Nachricht angegebenen Ausrichtung übereinstimmt, wird die In-App-Nachricht nicht angezeigt. Vergewissern Sie sich, dass Ihr Gerät richtig ausgerichtet ist.


