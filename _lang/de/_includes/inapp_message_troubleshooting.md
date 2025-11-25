## Grundlegende Checks

### Meine In-App-Nachricht wurde bei einem Benutzer nicht angezeigt

1. War der Benutzer zu Beginn der Sitzung im Segment, als das SDK neue In-App-Nachrichten anforderte?
2. War der Nutzer berechtigt oder erneut berechtigt, die In-App-Nachricht gemäß den Regeln der Kampagnenausrichtung zu erhalten?
3. War der Benutzer von einer Frequenzbegrenzung betroffen?
4. War der Benutzer in einer Kontrollgruppe? Prüfen Sie, ob Ihre Kampagne für AB-Tests konfiguriert ist.
5. Wurde eine andere In-App-Nachricht mit höherer Priorität anstelle der erwarteten Nachricht angezeigt?
6. War mein Gerät in der von der Kampagne vorgegebenen Ausrichtung?
7. Wurde meine Nachricht durch das standardmäßige 30-Sekunden-Mindestzeitintervall zwischen Triggern unterdrückt, das vom SDK erzwungen wird?

### Meine In-App-Nachricht wurde nicht allen Benutzern auf dieser Plattform angezeigt

1. Ist Ihre Kampagne so konfiguriert, dass sie entweder auf mobile Apps oder Webbrowser abzielt? Wenn Ihre Kampagne zum Beispiel nur auf Webbrowser abzielt, wird sie nicht an Android-Geräte gesendet.
2. Haben Sie eine benutzerdefinierte Benutzeroberfläche implementiert, und funktioniert sie wie gewünscht? Gibt es eine andere app-seitige benutzerdefinierte Behandlung oder Unterdrückung, die die Anzeige stören könnte? 
3. Hat diese bestimmte Plattform und App-Version jemals erfolgreich In-App-Nachrichten angezeigt?
4. Fand der Auslöser lokal auf dem Gerät statt? Beachten Sie, dass ein REST-Aufruf nicht verwendet werden kann, um eine In-App-Nachricht im SDK zu triggern.

### Meine In-App-Nachricht wurde nicht für alle Benutzer angezeigt

1. Wurde die Trigger-Aktion sowohl im Dashboard als auch in der App-Integration richtig eingerichtet?
2. Wurde eine andere In-App-Nachricht mit höherer Priorität anstelle der erwarteten Nachricht angezeigt?
3. Benutzen Sie eine aktuelle Version des SDK? Für einige Arten von In-App-Nachrichten ist eine SDK-Version erforderlich.
4. Wurden die Sitzungen ordnungsgemäß in Ihre Integration integriert? Funktioniert die Sitzungsanalyse für diese App?

### Meine In-App-Nachricht hat sehr lange gebraucht, um zu erscheinen

1. Wenn Sie große Bild- oder Videodateien von Ihrem CDN an eine HTML-basierte In-App-Nachricht senden, stellen Sie sicher, dass Ihre Dateien so klein wie möglich sind und dass Ihr CDN leistungsfähig ist.
2. Überprüfen Sie, ob Sie eine `delay` für Ihre In-App-Nachricht auf dem Dashboard konfiguriert haben.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Je nach den Umständen laden In-App-Nachrichten die entsprechenden Bilder vor der Anzeige entweder herunter oder laden sie von der Festplatte. Wenn Sie über eine langsame Netzwerkverbindung oder ein sehr leistungsschwaches Gerät verfügen, kann dieser Vorgang einige Zeit dauern. Achten Sie darauf, dass Ihre Bilder so klein wie möglich sind.
{% endcase %}

Eine ausführlichere Diskussion dieser Szenarien finden Sie im <a id="troubleshooting-in-app-advanced">Abschnitt Erweiterte Fehlerbehebung</a>.

## Probleme mit Impressionen und Click Analytics

{% if include.sdk == "iOS" %}
### Impressionen und Klicks werden nicht protokolliert

Wenn Sie einen Delegierten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie [Klicks und Impressionen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) auf die In-App-Nachricht manuell [protokollieren](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)).
{% elsif include.sdk == "Android" %}
### Impressionen und Klicks werden nicht protokolliert
Wenn Sie einen Delegaten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie Klicks und Impressionen auf die In-App-Nachricht manuell protokollieren.
{% endif %}

### Die Eindrücke sind geringer als erwartet

1. Die Synchronisierung der Auslöser mit dem Gerät beim Start der Sitzung nimmt einige Zeit in Anspruch, so dass es zu einer Race-Condition kommen kann, wenn Benutzer ein Event oder einen Kauf direkt nach dem Start einer Sitzung protokollieren. Ein möglicher Ausweg könnte darin bestehen, die Kampagne so zu ändern, dass sie beim Start der Sitzung getriggert wird, und dann nach dem beabsichtigten Event oder Kauf zu segmentieren. Beachten Sie, dass dies die In-App-Nachricht beim nächsten Sitzungsstart nach Eintreten des Events liefern würde.

2. Wenn die Kampagne durch den Beginn einer Sitzung oder ein benutzerdefiniertes Ereignis ausgelöst wird, müssen Sie sicherstellen, dass dieses Ereignis oder diese Sitzung häufig genug stattfindet, um die Nachricht auszulösen. Überprüfen Sie diese Daten auf den Seiten [Übersicht]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (für Sitzungsdaten) oder [Angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![Die Seite mit den angepassten Events zeigt in einem Diagramm an, wie oft das angepasste Event Zu den Favoriten hinzugefügt innerhalb eines Monats aufgetreten ist]({% image_buster /assets/img_archive/trouble5.png %})

### Die Impressionen sind geringer als früher

1. Stellen Sie sicher, dass niemand das Segment oder die Kampagne seit dem Start unbeabsichtigt verändert hat. Unsere Änderungsprotokolle für Segmente und Kampagnen geben Ihnen einen Einblick in die Änderungen, die vorgenommen wurden, wer die Änderung vorgenommen hat und wann sie erfolgt ist.

![Link zur Anzeige des Changelogs auf der Seite Kampagnendetails mit sieben Änderungen seit der letzten Ansicht der Kampagne durch den Nutzer:innen]({% image_buster /assets/img_archive/trouble4.png %})

2. Vergewissern Sie sich, dass Sie Ihr Trigger-Event nicht in einer separaten In-App-Nachrichtenkampagne mit einer höheren Priorität wiederverwendet haben.

## Erweiterte Fehlerbehebung {#troubleshooting-in-app-advanced}

Die meisten Probleme mit In-App-Nachrichten lassen sich in zwei Hauptkategorien unterteilen: Zustellung und Anzeige. Um herauszufinden, warum eine erwartete In-App-Nachricht nicht auf Ihrem Gerät angezeigt wurde, bestätigen Sie, dass die <a id="troubleshooting-in-app-message-delivery">In-App-Nachricht an das Gerät übermittelt wurde</a>, und <a id="troubleshooting-in-app-message-display">beheben Sie dann das Problem mit der Anzeige der Nachricht</a>.

### Fehlerbehebung bei der Zustellung {#troubleshooting-in-app-message-delivery}

Das SDK fordert beim Start der Sitzung In-App-Nachrichten von den Braze-Servern an. Um zu überprüfen, ob In-App-Nachrichten an Ihr Gerät geliefert werden, müssen Sie sicherstellen, dass In-App-Nachrichten sowohl vom SDK angefordert als auch von den Braze-Servern zurückgegeben werden.

#### Prüfen Sie, ob Nachrichten angefordert und zurückgeschickt werden

1. Fügen Sie sich als [Testbenutzer]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) auf dem Dashboard hinzu.
2. Richten Sie eine In-App-Nachrichtenkampagne ein, die sich an Ihren Nutzer richtet.
3. Stellen Sie sicher, dass in Ihrer Anwendung eine neue Sitzung stattfindet.
4. Verwenden Sie das [Event Benutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu überprüfen, ob Ihr Gerät beim Start der Sitzung In-App-Nachrichten anfordert. Suchen Sie die SDK-Anfrage, die mit dem Sitzungsstart-Event Ihres Testbenutzers verbunden ist.
  - Wenn Ihre App ausgelöste In-App-Nachrichten anfordern sollte, sollten Sie `trigger` im Feld **Angeforderte Antworten** unter **Antwortdaten** sehen.
  - Wenn Ihre App dazu gedacht war, originale In-App-Nachrichten anzufordern, sollten Sie `in_app` im Feld **Angeforderte Antworten** unter **Antwortdaten** sehen.
5. Verwenden Sie die [Event-Benutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um zu überprüfen, ob die richtigen In-App-Nachrichten in den Antwortdaten zurückgegeben werden.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Fehlerbehebung bei nicht angeforderten Nachrichten

Wenn Ihre In-App-Nachrichten nicht angefordert werden, kann es sein, dass Ihre App die Sitzungen nicht korrekt verfolgt, da die In-App-Nachrichten beim Start der Sitzung aktualisiert werden. Vergewissern Sie sich außerdem, dass Ihre App tatsächlich eine Sitzung gemäß der Semantik des Sitzungs-Timeouts Ihrer App startet:

![Die SDK-Anfrage, die in den Ereignisbenutzerprotokollen gefunden wurde, die ein erfolgreiches Sitzungsstart-Event anzeigen.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Fehlerbehebung bei nicht zurückgegebenen Nachrichten

Wenn Ihre In-App-Nachrichten nicht zurückgeschickt werden, liegt wahrscheinlich ein Problem mit dem Targeting Ihrer Kampagne vor:

1. Ihr Segment enthält nicht Ihren Benutzer.
  - Überprüfen Sie auf der Registerkarte [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab), ob das richtige Segment unter **Segmente** erscheint.
2. Ihr Nutzer hat die In-App-Nachricht bereits erhalten und war nicht berechtigt, sie erneut zu erhalten.
  - Überprüfen Sie die [Einstellungen für die Wiederzulassung von Kampagnen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) unter dem Schritt **Zustellung** des **Campaign Composers** und stellen Sie sicher, dass die Einstellungen für die Wiederzulassung mit Ihrer Testkonfiguration übereinstimmen.
3. Ihr Benutzer hat die Höchstfrequenz für die Kampagne erreicht.
  - Überprüfen Sie die Einstellungen für die Kampagne [Frequenzobergrenze]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) und stellen Sie sicher, dass sie mit Ihrer Testkonfiguration übereinstimmen.
4. Wenn es in der Kampagne eine Kontrollgruppe gab, könnte Ihr Benutzer in die Kontrollgruppe gefallen sein.
  - Sie können überprüfen, ob dies geschehen ist, indem Sie ein Segment mit einem Filter für empfangene Kampagnenvarianten erstellen, bei dem die Kampagnenvariante auf **Kontrolle** eingestellt ist, und überprüfen, ob Ihr Nutzer in dieses Segment fällt.
  - Wenn Sie Kampagnen für Integrationstests erstellen, achten Sie darauf, dass Sie keine Kontrollgruppe hinzufügen.


### Fehlerbehebungsanzeige {#troubleshooting-in-app-message-display}

Wenn Ihre App erfolgreich In-App-Nachrichten anfordert und empfängt, diese aber nicht angezeigt werden, kann die geräteseitige Logik die Anzeige verhindern:

1. Wird das Auslöseereignis wie erwartet ausgelöst? Um dies zu testen, konfigurieren Sie die Nachricht so, dass sie durch eine andere Aktion (z. B. Sitzungsstart) getriggert wird, und überprüfen Sie, ob sie angezeigt wird.
{% if include.sdk == "iOS" %}
2. Getriggerte In-App-Nachrichten werden auf der Grundlage des [minimalen Zeitintervalls zwischen den Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), das standardmäßig 30 Sekunden beträgt, begrenzt.
{% elsif include.sdk == "Android" %}
2. Getriggerte In-App-Nachrichten werden auf der Grundlage des [minimalen Zeitintervalls zwischen den Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), das standardmäßig 30 Sekunden beträgt, begrenzt.
{% elsif include.sdk == "Web" %}
2. Getriggerte In-App-Nachrichten werden auf der Grundlage des [minimalen Zeitintervalls zwischen den Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), das standardmäßig 30 Sekunden beträgt, begrenzt.
{% endif %}
3. Wenn das Herunterladen von Bildern fehlschlägt, werden In-App-Nachrichten mit Bildern nicht mehr angezeigt. Überprüfen Sie Ihre Geräteprotokolle, um sicherzustellen, dass das Herunterladen von Bildern nicht fehlschlägt. Versuchen Sie, Ihr Bild vorübergehend aus Ihrer Nachricht zu entfernen, um zu sehen, ob es dadurch angezeigt wird.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, überprüfen Sie Ihren Delegaten, um sicherzustellen, dass er die Anzeige der In-App-Nachrichten nicht beeinträchtigt.
  {% when "Web" %}
5. Wenn Sie eine angepasste Handhabung von In-App-Nachrichten über `braze.subscribeToInAppMessage` oder `appboy.subscribeToNewInAppMessages` verwenden, überprüfen Sie dieses Abonnement, um sicherzustellen, dass es die Anzeige von In-App-Nachrichten nicht beeinträchtigt.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Wenn die Ausrichtung des Geräts nicht mit der von der In-App-Nachricht angegebenen Ausrichtung übereinstimmt, wird die In-App-Nachricht nicht angezeigt. Vergewissern Sie sich, dass Ihr Gerät richtig ausgerichtet ist.
{% endcase %}
7. Wenn Ihre In-App-Nachricht durch den Sitzungsstart getriggert wird und Sie ein verlängertes Sitzungs-Timeout eingestellt haben, wirkt sich dies darauf aus, wie schnell Sie Nachrichten anzeigen können. Wenn Ihr Sitzungszeitlimit beispielsweise auf 300 Sekunden eingestellt ist, wird die Sitzung durch Schließen und erneutes Öffnen der App in weniger als dieser Zeit nicht aktualisiert, sodass eine durch einen Sitzungsstart getriggerte In-App-Nachricht nicht angezeigt wird.

