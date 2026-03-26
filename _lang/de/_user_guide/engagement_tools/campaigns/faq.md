---
nav_title: FAQ
article_title: Kampagnen FAQ
page_order: 10
page_type: FAQ
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Kampagnen."
tool: Campaigns

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Kampagnen.

### Wie erstelle ich eine Multichannel-Kampagne?

Um eine Multichannel-Kampagne zu erstellen, wählen Sie **Messaging** > **Kampagnen**. Wählen Sie dann **Kampagne erstellen** > **Multichannel**. Von hier aus können Sie aus den folgenden Messaging-Kanälen auswählen: Content-Cards, E-Mail, LINE, Push-Benachrichtigungen, SMS/MMS/RCS, Webhook oder WhatsApp.

### Kann ich eine Kontrollgruppe zu meiner Multichannel-Kampagne hinzufügen?

Nein, Kontrollgruppen in Kampagnen sind für das Messaging über einen einzigen Kanal gedacht, z. B. E-Mail A gegenüber E-Mail B. Versuchen Sie alternativ, [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) zum Testen verschiedener Kanäle, Nachrichteninhalte und Zustellungszeitpunkte zu verwenden. 

### Wie kann ich mit dem Testen und Optimieren von Kampagnen beginnen?

Multivariate Kampagnen und die Ausführung von Canvase mit mehreren Varianten sind ein guter Anfang! Sie können zum Beispiel eine [multivariate Kampagne]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) durchführen, um eine Nachricht mit verschiedenen Textvarianten oder Betreffzeilen zu testen. Mit Canvase mit mehreren Varianten können Sie ganze Workflows testen.

### Warum ist die Öffnungsrate für meine Kampagne gesunken?

Niedrige Öffnungsraten haben nicht immer etwas mit einem technischen Problem zu tun. Es kann Probleme mit dem Abschneiden von E-Mails geben, was dazu führt, dass ein Tracking-Pixel fehlt. Es ist jedoch auch möglich, dass weniger Nutzer:innen ihre E-Mails aufgrund des Inhalts oder einer veränderten Zielgruppengröße öffnen. 

### Wie werden die Zielgruppen von Kampagnen bewertet?

Standardmäßig überprüfen Kampagnen die Zielgruppen-Filter beim Eingang. Bei aktionsbasierten Kampagnen mit Verzögerung besteht die Möglichkeit, die Segmentkriterien zum Zeitpunkt des Versands neu zu bewerten, um sicherzustellen, dass die Nutzer:innen noch zur Zielgruppe gehören, wenn die Nachricht versendet wird. 

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger:innen und der Anzahl der Sendungen für eine bestimmte Kampagne oder ein bestimmtes Canvas?

Eine mögliche Erklärung könnte sein, dass bei der Kampagne oder dem Canvas die Wiederzulassung aktiviert ist. Das bedeutet, dass Nutzer:innen, die für das Segment und die Zustellungseinstellungen in Frage kommen, die Nachricht mehr als einmal erhalten können. Wenn die Wiederzulassung nicht aktiviert ist, kann die wahrscheinliche Erklärung für den Unterschied zwischen Sendungen und eindeutigen Empfänger:innen darin liegen, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben. 

Wenn Sie z. B. ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, könnte ein:e bestimmte:r Nutzer:in mit einem mobilen und einem Desktop-Gerät mehr als eine Nachricht erhalten.

### Warum kann die Anzahl der Konversionen bei Multichannel-Kampagnen die Anzahl der eindeutigen Nutzer:innen übersteigen?

Bei Multichannel-Kampagnen zählt Braze die Konversionen pro Kanal und nicht pro Nutzer:in. Wenn ein:e Nutzer:in innerhalb des Konversionsfensters eine einzelne Konversionsaktion durchführt, ordnet Braze diese Konversion jedem Kanal zu, über den der/die Nutzer:in eine Nachricht erhalten hat. Das bedeutet: Wenn ein:e Nutzer:in Nachrichten über mehrere Kanäle (z. B. sowohl per E-Mail als auch per Push-Benachrichtigung) erhält und konvertiert, zählt Braze mehrere Konversionen – eine für jeden Kanal. Infolgedessen kann die Gesamtzahl der Konversionen die Anzahl der eindeutigen Nutzer:innen, die eine Konversion durchgeführt haben, übersteigen.

Wenn beispielsweise im Rahmen einer Multichannel-Kampagne sowohl eine E-Mail als auch eine Push-Benachrichtigung an eine:n Nutzer:in gesendet werden und diese:r Nutzer:in nach Erhalt beider Nachrichten und innerhalb des Konversionsfensters eine Konversion durchführt, zählt Braze dies als zwei Konversionen – eine für die E-Mail und eine für die Push-Benachrichtigung –, obwohl es sich um eine einzige Aktion desselben Nutzers bzw. derselben Nutzerin handelt.

### Warum hat meine Kampagne eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Kampagne verwende?

Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) eingerichtet haben, verhindert dies, dass ein bestimmter Prozentsatz Ihrer erreichbaren Zielgruppe Kampagnen erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer:innen für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer:innen für Ihre Kampagne, selbst wenn die Kampagne dasselbe Segment verwendet.

### Was bietet die Zustellung zur Ortszeit?

Die Zustellung zur Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen an ein Segment basierend auf der individuellen Zeitzone der jeweiligen Nutzer:innen zuzustellen. Ohne die Zustellung zur Ortszeit werden die Kampagnen auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant. 

Wenn beispielsweise ein in London ansässiges Unternehmen eine Kampagne um 12 Uhr mittags versendet, erreicht sie die Nutzer:innen an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, keine Push-Benachrichtigungen am frühen Morgen an Ihre Nutzerbasis zu senden.

### Wie erkennt Braze die Zeitzone eines Nutzers bzw. einer Nutzerin?

Braze ermittelt automatisch die Zeitzone anhand des Geräts der Nutzer:innen. Dies gewährleistet die Genauigkeit der Zeitzone und die vollständige Abdeckung Ihrer Nutzer:innen. Nutzer:innen, die über die User-API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App vom SDK erkannt werden. 

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) im Dashboard überprüfen.

### Wann bewertet Braze die Nutzer:innen für die Zustellung zur Ortszeit?

Braze überprüft die Eingangsberechtigung der Nutzer:innen zu folgenden Zeitpunkten:

- Samoa-Zeit (UTC+13) oder UTC+14 während der Sommerzeit
- Die Ortszeit des geplanten Tages

Damit ein:e Nutzer:in für den Eingang in Frage kommt, muss er oder sie beide Prüfungen bestehen. Wenn ein Canvas zum Beispiel am 7. August 2021 um 14 Uhr Ortszeit gestartet werden soll, müssten für eine:n Nutzer:in in New York die folgenden Berechtigungsprüfungen durchgeführt werden:

- New York am 6. August 2021 um 21 Uhr
- New York am 7. August 2021 um 14 Uhr

Die Nutzer:innen müssen sich 24 Stunden vor dem Start im Segment befinden. Wenn der/die Nutzer:in bei der ersten Überprüfung nicht berechtigt ist, führt Braze die zweite Überprüfung nicht durch.

Wenn eine Kampagne beispielsweise um 19 Uhr UTC zugestellt werden soll, beginnen wir mit dem Einreihen der Kampagnensendungen in die Warteschlange, sobald eine Zeitzone identifiziert wird (z. B. Samoa). Das bedeutet, dass wir uns darauf vorbereiten, die Nachricht zu senden – nicht, dass die Kampagne bereits versendet wird. Wenn Nutzer:innen bei der Berechtigungsprüfung keinem Filter entsprechen, gehören sie nicht zur Zielgruppe.

Ein weiteres Beispiel: Angenommen, Sie möchten zwei Kampagnen erstellen, die am selben Tag versendet werden sollen – eine am Morgen und eine am Abend – und fügen einen Filter hinzu, damit Nutzer:innen die zweite Kampagne nur erhalten können, wenn sie die erste bereits erhalten haben. Bei der Zustellung zur Ortszeit kann es vorkommen, dass einige Nutzer:innen die zweite Kampagne nicht erhalten. Das liegt daran, dass wir die Berechtigung prüfen, wenn die Zeitzone der Nutzer:innen identifiziert wird. Wenn die geplante Zeit in ihrer Zeitzone noch nicht erreicht ist, haben sie die erste Kampagne noch nicht erhalten und kommen daher nicht für die zweite Kampagne in Frage.

### Wie plane ich eine Kampagne mit Zustellung zur Ortszeit?

Wählen Sie bei der Zeitplanung einer Kampagne aus, dass diese zu einer bestimmten Zeit gesendet werden soll, und wählen Sie dann **Kampagne an Nutzer:innen in ihrer Ortszeit senden**.

Braze empfiehlt dringend, alle Kampagnen mit Zustellung zur Ortszeit 24 Stunden im Voraus zu planen. Da eine solche Kampagne über einen ganzen Tag hinweg versendet werden muss, sorgt eine Planung von 24 Stunden im Voraus dafür, dass Ihre Nachricht Ihr gesamtes Segment erreicht. Sie können diese Kampagnen jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Denken Sie daran, dass Braze keine Nachrichten an Nutzer:innen sendet, die die Sendezeit um mehr als 1 Stunde verpasst haben. 

Wenn es beispielsweise 13:00 Uhr ist und Sie eine Kampagne mit Zustellung zur Ortszeit für 15:00 Uhr planen, wird die Kampagne sofort an alle Nutzer:innen gesendet, deren Ortszeit zwischen 15:00 und 16:00 Uhr liegt, aber nicht an Nutzer:innen, deren Ortszeit 17:00 Uhr ist. Außerdem muss die Sendezeit, die Sie für Ihre Kampagne wählen, in der Zeitzone Ihres Unternehmens noch nicht verstrichen sein.

Wenn Sie eine Kampagne mit Zustellung zur Ortszeit bearbeiten, die weniger als 24 Stunden im Voraus geplant wurde, wird der Zeitplan der Nachricht nicht geändert. Wenn Sie eine solche Kampagne so bearbeiten, dass sie zu einem späteren Zeitpunkt versendet wird (z. B. um 19 Uhr statt um 18 Uhr), erhalten die Nutzer:innen, die sich zum Zeitpunkt der ursprünglichen Sendezeit im Zielsegment befanden, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie die Kampagne so bearbeiten, dass sie zu einer früheren Zeit gesendet wird (z. B. 16 Uhr statt 17 Uhr), wird die Kampagne trotzdem an alle Mitglieder des Segments zur ursprünglichen Zeit (17 Uhr) gesendet. 

{% alert note %}
Bei Canvas-Komponenten müssen Nutzer:innen nicht 24 Stunden lang in der Komponente sein, um die nächste Komponente im User Journey bei der Zustellung zur Ortszeit zu erhalten.
{% endalert %}

Wenn Sie den Nutzer:innen erlaubt haben, sich erneut für die Kampagne zu qualifizieren, erhalten sie diese wieder zur ursprünglichen Zeit (17 Uhr). Bei allen weiteren Vorkommen Ihrer Kampagne werden Ihre Nachrichten jedoch nur zu der von Ihnen aktualisierten Zeit gesendet.

### Wann werden Änderungen an Kampagnen mit Zustellung zur Ortszeit wirksam?

Zielsegmente für Kampagnen mit Zustellung zur Ortszeit sollten mindestens ein 48-Stunden-Fenster für alle zeitbasierten Filter enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Nehmen wir zum Beispiel ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern anspricht:

- Erstmals App verwendet vor mehr als 1 Tag
- Erstmals App verwendet vor weniger als 2 Tagen

Bei der Zustellung zur Ortszeit können Nutzer:innen in diesem Segment aufgrund der Zustellungszeit und der lokalen Zeitzone verfehlt werden. Das liegt daran, dass ein:e Nutzer:in das Segment zu dem Zeitpunkt verlassen kann, zu dem die jeweilige Zeitzone die Zustellung triggert.

### Welche Änderungen kann ich an geplanten Kampagnen vor dem Start vornehmen?

Wenn die Kampagne geplant ist, müssen Sie alle Änderungen, die nicht die Nachrichtenzusammensetzung betreffen, vornehmen, bevor wir die zu versendenden Nachrichten in die Warteschlange stellen. Wie bei allen Kampagnen können Sie Konversions-Events nach dem Start nicht mehr bearbeiten.

### Ich habe meine geplante Kampagne aktualisiert. Warum ist sie nicht gestartet?

Dies kann passieren, wenn eine Kampagne genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde. Wenn es z. B. gerade 15:10 Uhr ist und Sie die Kampagne so geändert haben, dass sie um 15:10 Uhr startet, und dann **Kampagne aktualisieren** ausgewählt haben, ist es jetzt nach 15:10 Uhr – d. h. der geplante Startzeitpunkt ist bereits verstrichen. Anstatt die Kampagne für denselben Zeitpunkt zu planen, wählen Sie **Senden, sobald die Kampagne startet**.

### Was ist die „sichere Zone", bevor Nachrichten einer geplanten Kampagne in die Warteschlange gestellt werden?

Wir empfehlen, Änderungen an Nachrichten innerhalb der folgenden Zeiträume vorzunehmen:

- **Einmalig geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Wiederkehrende geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Kampagnen mit Zustellung zur Ortszeit:** Bearbeiten Sie bis zu 24 Stunden vor der geplanten Sendezeit.
- **Kampagnen mit optimaler Sendezeit:** Bearbeiten Sie bis zu 24 Stunden vor dem Tag, an dem die Kampagne gesendet werden soll.

Wenn Sie außerhalb dieser Empfehlungen Änderungen an Ihrer Nachricht vornehmen, werden die Updates möglicherweise nicht in der gesendeten Nachricht widergespiegelt. Wenn Sie beispielsweise die Sendezeit drei Stunden vor dem geplanten Versand einer Kampagne um 12 Uhr Ortszeit bearbeiten, kann Folgendes passieren:

- Braze versendet keine Nachrichten an Nutzer:innen, die den Versandzeitpunkt um mehr als eine Stunde verpasst haben.
- Nachrichten, die sich bereits in der Warteschlange befinden, werden möglicherweise weiterhin zur ursprünglich eingereihten Zeit gesendet und nicht zur angepassten Zeit.

Sollten Änderungen erforderlich sein, empfehlen wir, die aktuelle Kampagne zu beenden (dadurch werden alle in der Warteschlange befindlichen Nachrichten storniert). Sie können dann die Kampagne duplizieren, die erforderlichen Änderungen vornehmen und die neue Kampagne starten. Möglicherweise müssen Sie Nutzer:innen von dieser Kampagne ausschließen, die bereits die erste Kampagne erhalten haben. Stellen Sie sicher, dass Sie den Kampagnenzeitplan so anpassen, dass der Versand in der jeweiligen Zeitzone berücksichtigt wird.

### Warum haben am Tag der Zeitumstellung keine Nutzer:innen an meiner täglich geplanten Kampagne teilgenommen?

An Tagen, an denen die Sommerzeit beginnt oder endet, können täglich geplante Kampagnen bis zu einer Stunde früher oder später als üblich ausgeführt werden, je nachdem, ob die Uhren vor- oder zurückgestellt werden. Wenn Ihr Segment auf angepassten Attributen oder Events mit Zeitstempeln basiert, die innerhalb einer Stunde vor dem geplanten Versandzeitpunkt liegen, sind diese Nutzer:innen möglicherweise noch nicht qualifiziert, wenn die Kampagne die Berechtigung am Tag der Zeitumstellung bewertet.

Nehmen wir beispielsweise an, dass Nutzer:innen in der Regel um 15:00 Uhr UTC ein Update für angepasste Attribute erhalten und Ihre Kampagne täglich um 10:30 Uhr in New York (Eastern Time) läuft. Während New York in der Standardzeit (UTC-5) ist, entspricht 10:30 Uhr ET 15:30 Uhr UTC, sodass die Kampagne nach der Protokollierung des Attributs ausgeführt wird. Wenn New York auf Sommerzeit (UTC-4) umstellt, entspricht 10:30 Uhr ET 14:30 Uhr UTC, sodass die Kampagne am Tag der Zeitumstellung vor dem Attribut-Update um 15:00 Uhr UTC ausgeführt werden kann. Da das qualifizierende Attribut noch nicht vorhanden ist, werden diese Nutzer:innen herausgefiltert. Wenn die Wiederteilnahme deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen teilgenommen haben, nicht erneut teilnehmen, was zu null Eingängen für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre angepassten Attribut- oder Event-Updates mehr als eine Stunde vor der geplanten Versandzeit der Kampagne erfolgen.

### Warum stimmt die Anzahl der Nutzer:innen, die eine Kampagne betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer:innen, die eine Kampagne betreten, kann von der erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Dies führt dazu, dass Nutzer:innen aus der Kampagne ausscheiden, wenn sie nicht zu Ihrer ausgewählten Zielgruppe gehören, bevor Trigger-Aktionen ausgewertet werden.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung in Kampagnen benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach dem Vorkommen des Problems an den Braze Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Was ist der Unterschied zwischen den Optionen „CSV-Export von Nutzerdaten" und „CSV-Export von E-Mail-Adressen" auf meiner Seite der Kampagnen-Analytics?

Durch Auswahl der Option **CSV-Export von E-Mail-Adressen** werden nur die Daten von Nutzer:innen mit E-Mail-Adressen heruntergeladen. Wenn Sie beispielsweise ein Segment mit 100.000 Nutzer:innen haben, aber nur 50.000 davon über E-Mail-Adressen verfügen, und Sie auf **CSV-Export von E-Mail-Adressen** klicken, enthält der Export nur 50.000 Datenzeilen. Im Vergleich dazu werden bei der Auswahl von **CSV-Export von Nutzerdaten** alle Nutzerdaten exportiert.

### Kann ich nach einer Kampagne anhand ihrer API-ID suchen?

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der Seite **Kampagnen**, um nach einer Kampagne anhand ihrer API-ID zu suchen. Weitere Informationen finden Sie unter [Suche nach Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Warum werden Leerzeichen in Eingabefeldern anders dargestellt als im angezeigten Text? 

Die Behandlung von Leerzeichen unterscheidet sich aufgrund der CSS-Formatierung zwischen Eingabefeldern und angezeigten Textkomponenten. In Textkomponenten mit dem Standard-CSS `white-space: normal` werden mehrere aufeinanderfolgende Leerzeichen bei der Anzeige zu einem einzigen Leerzeichen zusammengefasst. Dies entspricht dem Standardverhalten von HTML für gerenderten Text. 

Eingabefelder behalten mehrere Leerzeichen genau so bei, wie Sie sie eingeben, da Sie den genauen Abstand für eine korrekte Dateneingabe sehen und bearbeiten müssen. Das bedeutet, dass Text mit mehreren Leerzeichen in einem Eingabefeld (wo alle Leerzeichen beibehalten werden) anders dargestellt werden kann als in anderen Bereichen des Dashboards (wo CSS mehrere Leerzeichen zusammenfassen kann). 

Wenn Sie beispielsweise einen Kampagnennamen oder einen UTM-Parameter mit mehreren Leerzeichen in ein Eingabefeld eingeben, werden alle Leerzeichen beibehalten. Wenn derselbe Text jedoch in Suchergebnissen, Kampagnenlisten oder anderen Textkomponenten erscheint, können aufgrund der CSS-Leerzeichenbehandlung mehrere Leerzeichen als ein einziges Leerzeichen angezeigt werden. 

### Was ist der Unterschied zwischen API-Kampagnen und API-getriggerten Kampagnen?

Mit API-getriggerten Kampagnen können Sie im Braze-Dashboard Kampagnentexte, multivariate Tests und Wiederzulassungsregeln verwalten und gleichzeitig die Zustellung dieser Inhalte von Ihren eigenen Servern und Systemen triggern. Diese Nachrichten können auch zusätzliche Daten enthalten, die in Echtzeit als Template in die Nachrichten eingefügt werden.

API-Kampagnen dienen dem Tracking der Nachrichten, die über die API versendet werden. Anders als bei den meisten Kampagnen geben Sie nicht die Nachricht, die Empfänger:innen oder den Zeitplan an, sondern übergeben die Bezeichner an Ihre API-Aufrufe. 

### Was ist der Unterschied zwischen aktionsbasierten und API-getriggerten Kampagnen?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Aktionsbasiert

Kampagnen mit aktionsbasierter Zustellung oder Event-getriggerte Kampagnen sind sehr effektiv für transaktions- oder leistungsbezogene Nachrichten und ermöglichen es Ihnen, den Versand zu triggern, nachdem ein:e Nutzer:in ein bestimmtes Event abgeschlossen hat. 

| Vorteile | Nachteile | 
| ---- | ---- |
| • Sichtbarkeit von eingehenden JSON-Payloads in der Plattform (wenn das Event von einem/einer Testnutzer:in getriggert wurde) über das **Nachrichten-Aktivitätsprotokoll**<br><br>• Personalisierungselemente sind in den angepassten Event-Eigenschaften enthalten<br><br>• Mit angepassten Events können Sie Segmente von Nutzer:innen erstellen, die für die Nachricht in Frage kommen | • Verbraucht Datenpunkte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### API-getriggert

API-getriggerte und Server-getriggerte Kampagnen sind ideal für die Abwicklung komplexerer Transaktionen und ermöglichen es Ihnen, die Zustellung von Kampagneninhalten von Ihren eigenen Servern und Systemen aus zu triggern. Die API-Anfrage zum Auslösen der Nachricht kann auch zusätzliche Daten enthalten, die in Echtzeit als Template in die Nachricht eingefügt werden.

| Vorteile | Überlegungen | 
| ---- | ---- |
| • Protokolliert keine Datenpunkte<br><br>• Personalisierungselemente sind in den JSON-Payload-Eigenschaften enthalten | • Es ist nicht möglich, in den Eigenschaften der JSON-Payload ein Segment von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind<br><br>• Eingehende JSON-Payloads können mit dem **Nachrichten-Aktivitätsprotokoll** nicht angezeigt werden|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out"-Fehler einreiche?

Wenn Sie beim Erstellen oder Bearbeiten einer Kampagne oder eines Canvas auf einen „Request Timed Out"-Fehler stoßen und den [Braze Support]({{site.baseurl}}/braze_support/) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

- **Bildschirmaufnahme:** Eine Aufnahme der Schritte, die Sie vor dem Auftreten des Fehlers durchgeführt haben, einschließlich aller Seitenwechsel.
- **Zeitstempel und Zeitzone:** Der genaue Zeitpunkt, zu dem der Fehler aufgetreten ist, und Ihre Zeitzone.
- **Browser und Version:** Der von Ihnen verwendete Browser (z. B. Chrome 120, Safari 17) und ob Sie versucht haben, den Fehler in einem anderen Browser zu reproduzieren.
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler auslösen, einschließlich aller spezifischen Kampagnen- oder Canvas-Einstellungen.
- **Netzwerkprotokolle (optional):** Öffnen Sie die Entwicklertools Ihres Browsers (Tab **Netzwerk**), reproduzieren Sie den Fehler und exportieren Sie das Netzwerkprotokoll als HAR-Datei (HTTP Archive). Dies hilft dem Support-Team zu identifizieren, welcher API-Aufruf das Timeout verursacht.

### Warum stimmen meine Versand-Analytics nicht mit dem von mir festgelegten maximalen Empfängerlimit überein?

Wenn Sie ein maximales Empfängerlimit zu einer aktiven Kampagne hinzufügen oder ändern, wird das Limit aus folgenden Gründen möglicherweise nicht in Ihren Versand-Analytics widergespiegelt:

- **Limit nach dem Start hinzugefügt:** Wenn das maximale Empfängerlimit beim Start der Kampagne nicht festgelegt ist, werden Nachrichten, die bereits in die Warteschlange gestellt wurden, bevor Sie das Limit anwenden, trotzdem gesendet. Das Limit gilt nur für Sendungen, die Sie nach dem Speichern der Änderung in die Warteschlange stellen.
- **Interaktion mit Rate-Limiting:** Wenn eine Kampagne auch Rate-Limits hat, können Nachrichten über ein längeres Zeitfenster verteilt werden. Das maximale Empfängerlimit wird bewertet, wenn Nachrichten in die Warteschlange gestellt werden, nicht wenn sie zugestellt werden. Wenn das Limit geändert wird, während sich Nachrichten bereits in der Warteschlange befinden, gilt das ursprüngliche Limit für diese Nachrichten.
- **Wiederkehrende Kampagnen:** Bei wiederkehrenden Kampagnen wird das maximale Empfängerlimit bei jedem geplanten Versand unabhängig bewertet. Eine Änderung des Limits zwischen den Sendungen passt die vorherigen Versandzahlen nicht rückwirkend an.

Um Abweichungen zu vermeiden, legen Sie das maximale Empfängerlimit vor dem Start der Kampagne fest und vermeiden Sie Änderungen, während Sendungen in Bearbeitung sind.