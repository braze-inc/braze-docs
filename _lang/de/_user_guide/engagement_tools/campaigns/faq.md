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

Nein, Kontrollgruppen in Kampagnen sind für die Nachrichtenübermittlung über einen einzigen Kanal gedacht, z. B. E-Mail A gegenüber E-Mail B. Versuchen Sie alternativ, [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) zum Testen verschiedener Kanäle, Nachrichteninhalte und Zustellungszeitpunkte zu verwenden. 

### Wie kann ich mit dem Testen und Optimieren von Kampagnen beginnen?

Multivariaten-Kampagnen und die Ausführung von Canvase mit mehreren Varianten sind ein guter Anfang! Sie können zum Beispiel eine [multivariate Kampagne]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) durchführen, um eine Nachricht mit verschiedenen Kopien oder Betreffzeilen zu testen. Mit Canvase mit mehreren Varianten können Sie ganze Arbeitsabläufe testen.

### Warum ist die Öffnungsrate für meine Kampagne gesunken?

Niedrige Öffnungsraten haben nicht immer etwas mit einem technischen Problem zu tun. Es kann Probleme mit dem Ausschneiden von E-Mails geben, was dazu führt, dass ein Tracking-Pixel fehlt. Es ist jedoch auch möglich, dass weniger Nutzer:innen ihre E-Mails aufgrund des Inhalts oder einer veränderten Zielgruppe öffnen. 

### Wie werden die Zielgruppen von Kampagnen bewertet?

Standardmäßig überprüfen Kampagnen die Zielgruppen-Filter bei der Eingabe. Bei aktionsbasierten Kampagnen mit Verzögerung besteht die Möglichkeit, die Segmentkriterien zum Zeitpunkt des Versands neu zu bewerten, um sicherzustellen, dass die Nutzer noch zur Zielgruppe gehören, wenn die Nachricht versendet wird. 

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger und der Anzahl der Sendungen für eine bestimmte Kampagne oder ein bestimmtes Canvas?

Eine mögliche Erklärung könnte sein, dass die Kampagne oder Canvas die Wiederzulassung aktiviert hat. Das bedeutet, dass Nutzer:innen, die für das Segment und die Zustellung in Frage kommen, die Nachricht mehr als einmal erhalten können. Wenn die erneute Qualifizierung nicht aktiviert ist, kann die wahrscheinliche Erklärung für den Unterschied zwischen gesendeten und eindeutigen Empfänger:innenn darin liegen, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben. 

Wenn Sie z.B. ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, könnte ein bestimmter Benutzer mit einem mobilen und einem Desktop-Gerät mehr als eine Nachricht erhalten.

### Warum kann die Anzahl der Konversionen bei Multichannel-Kampagnen die Anzahl der eindeutigen Nutzer:innen übersteigen?

Bei Multichannel-Kampagnen zählt Braze die Konversionen pro Kanal und nicht pro Nutzer:in. Wenn ein Nutzer innerhalb des Konversionsfensters eine einzelne Konversionsaktion durchführt, ordnet Braze diese Konversion jedem Kanal zu, von dem der Nutzer eine Nachricht erhalten hat. Dies bedeutet, dass, wenn eine Nutzer:in Nachrichten über mehrere Kanäle (z. B. sowohl per E-Mail als auch per Push-Benachrichtigung) erhält und konvertiert, Braze mehrere Konversionen zählt, eine für jeden Kanal. Infolgedessen kann die Gesamtzahl der Konversionen die Anzahl der eindeutigen Nutzer:innen, die eine Konversion durchgeführt haben, übersteigen.

Wenn beispielsweise im Rahmen einer Multichannel-Kampagne sowohl eine E-Mail als auch eine Push-Benachrichtigung an einen Nutzer gesendet werden und dieser Nutzer nach Erhalt beider Nachrichten und innerhalb des Conversion-Fensters eine Konversion durchführt, zählt Braze dies als zwei Konversionen, eine für die E-Mail und eine für die Push-Benachrichtigung, obwohl es sich um eine einzige Aktion desselben Nutzers handelt.

### Warum hat meine Kampagne eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Kampagne verwende?

Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) eingerichtet haben, verhindert dies, dass ein bestimmter Prozentsatz Ihrer erreichbaren Zielgruppe Kampagnen erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer für Ihre Kampagne, selbst wenn die Kampagne dasselbe Segment verwendet.

### Was bietet die Zustellung in der lokalen Zeitzone?

Die Zustellung zur Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen an ein Segment zuzustellen, das auf der individuellen Zeitzone eines Nutzers oder einer Nutzerin basiert. Ohne die Zustellung in der lokalen Zeitzone werden die Kampagnen auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant. 

Wenn beispielsweise ein in London ansässiges Unternehmen eine Kampagne um 12 Uhr mittags versendet, erreicht sie die Nutzer an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, Push-Benachrichtigungen am frühen Morgen nicht an Ihre Nutzer:innen zu senden.

### Wie erkennt Braze die Zeitzone eines Benutzers?

Braze ermittelt automatisch die Zeitzone eines Benutzers anhand seines Geräts. Dies gewährleistet die Genauigkeit der Zeitzone und die vollständige Abdeckung Ihrer Nutzer:innen. Benutzer, die über die Benutzer-API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App vom SDK erkannt werden. 

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) auf dem Dashboard überprüfen.

### Wann bewertet Braze die Benutzer für die Bereitstellung in der lokalen Zeitzone?

Braze überprüft die Teilnahmeberechtigung der Nutzer:innen unter:

- Samoa-Zeit (UTC+13) oder UTC+14 während der Sommerzeit
- Die Ortszeit des Tages gemäß dem Zeitplan

Damit ein:e Nutzer:in für einen Entry in Frage kommt, muss er für beide Prüfungen in Frage kommen. Wenn ein Canvas zum Beispiel am 7\. August 2021 um 14 Uhr Ortszeit gestartet werden soll, müssten für einen Nutzer in New York die folgenden Prüfungen durchgeführt werden, um die Berechtigung zu prüfen:

- New York am 6\. August 2021 um 9 Uhr
- New York am 7\. August 2021 um 2 Uhr nachmittags

Die Nutzer:innen müssen sich vor dem Start 24 Stunden lang im Segment befinden. Wenn die Nutzer:in bei der ersten Überprüfung nicht berechtigt ist, führt Braze keine zweite Überprüfung durch.

Wenn eine Kampagne beispielsweise um 19 Uhr UTC zugestellt werden soll, beginnen wir mit dem Versand der Kampagne in die Warteschlange, sobald eine Zeitzone (wie Samoa) zugewiesen wird. Das bedeutet, dass wir uns darauf vorbereiten, die Nachricht zu senden, nicht die Kampagne zu senden. Wenn Nutzer:innen bei der Eignungsprüfung keinem Filter entsprechen, gehören sie nicht zur Zielgruppe.

Ein weiteres Beispiel: Sie möchten zwei Kampagnen erstellen, die am selben Tag versendet werden sollen - eine am Morgen und eine am Abend - und fügen einen Filter hinzu, damit Benutzer die zweite Kampagne nur erhalten können, wenn sie die erste bereits erhalten haben. Bei der Zustellung in einer lokalen Zeitzone kann es vorkommen, dass einige Nutzer die zweite Kampagne nicht erhalten. Das liegt daran, dass wir die Berechtigung prüfen, wenn die Zeitzone des Nutzers identifiziert wird. Wenn der Zeitplan also noch nicht in seiner Zeitzone liegt, hat er die erste Kampagne noch nicht erhalten, was bedeutet, dass er nicht für die zweite Kampagne in Frage kommt.

### Wie plane ich eine Kampagne für eine lokale Zeitzone?

Wählen Sie bei der Zeitplanung einer Kampagne aus, dass diese zu einer bestimmten Zeit gesendet werden soll, und wählen Sie dann **Kampagne an Nutzer:innen in ihrer Ortszeit senden**.

Braze empfiehlt dringend, alle Kampagnen in der Ortszeit 24 Stunden im Voraus zu planen. Da eine solche Kampagne über einen ganzen Tag versendet werden muss, sorgt ein Zeitplan von 24 Stunden im Voraus dafür, dass Ihre Nachricht Ihr gesamtes Segment erreicht. Sie können diese Kampagnen jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Denken Sie daran, dass Braze keine Nachrichten an Nutzer:innen sendet, die die Sendezeit um mehr als 1 Stunde verpasst haben. 

Wenn es beispielsweise 13.00 Uhr ist und Sie eine Kampagne für die lokale Zeitzone für 15.00 Uhr planen, dann wird die Kampagne sofort an alle Nutzer:innen gesendet, deren Ortszeit zwischen 15.00 und 16.00 Uhr liegt, aber nicht an Nutzer:innen, deren Ortszeit 17.00 Uhr ist. Außerdem muss die Sendezeit, die Sie für Ihre Kampagne wählen, in der Zeitzone Ihres Unternehmens noch nicht stattgefunden haben.

Wenn Sie eine Kampagne in einer lokalen Zeitzone bearbeiten, die weniger als 24 Stunden im Voraus geplant wurde, wird der Zeitplan der Nachricht nicht geändert. Wenn Sie eine Kampagne in einer lokalen Zeitzone so bearbeiten, dass sie zu einem späteren Zeitpunkt versendet wird (z. B. um 19 Uhr statt um 18 Uhr), erhalten die Nutzer, die sich zum Zeitpunkt der ursprünglichen Sendezeit im Zielsegment befanden, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie eine lokale Zeitzone bearbeiten, um zu einer früheren Zeit zu senden (z. B. 16 Uhr statt 17 Uhr), wird die Kampagne trotzdem an alle Mitglieder des Segments zur ursprünglichen Zeit (17 Uhr) gesendet. 

{% alert note %}
Bei Canvas-Komponenten müssen Nutzer:innen nicht 24 Stunden lang in der Komponente sein, um die nächste Komponente in der Zustellung zur Ortszeit zu erhalten.
{% endalert %}

Wenn Sie den Nutzern erlaubt haben, sich erneut für die Kampagne zu qualifizieren, dann erhalten sie sie wieder zur ursprünglichen Zeit (17 Uhr). Bei allen weiteren Vorkommen Ihrer Kampagne werden Ihre Nachrichten jedoch nur zu der von Ihnen aktualisierten Zeit gesendet.

### Wann werden Änderungen an lokalen Zeitzonen-Kampagnen wirksam?

Zielsegmente für Kampagnen in lokalen Zeitzonen sollten mindestens ein 48-Stunden-Fenster für alle zeitbasierten Filter enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Nehmen wir zum Beispiel ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern zusammenstellt:

- Erstmals verwendet vor mehr als 1 Tag
- Erstmals vor weniger als 2 Tagen benutzt

Bei der Zustellung in der lokalen Zeitzone können Benutzer in diesem Segment aufgrund der Zustellungszeit und der lokalen Zeitzone des Benutzers fehlen. Das liegt daran, dass ein:e Nutzer:in das Segment zu dem Zeitpunkt verlassen kann, zu dem die jeweilige Zeitzone die Zustellung triggert.

### Welche Änderungen kann ich an geplanten Kampagnen vor dem Start vornehmen?

Wenn der Zeitplan für die Kampagne erstellt wurde, müssen Sie alle Änderungen, die nicht die Nachrichtenzusammensetzung betreffen, vornehmen, bevor wir die zu versendenden Nachrichten in die Warteschlange stellen. Wie bei allen Kampagnen können Sie Konversions-Events nach dem Start nicht mehr bearbeiten.

### Ich habe meine geplante Kampagne aktualisiert. Warum ist es nicht gestartet?

Dies kann passieren, wenn eine Kampagne genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde. Wenn es z.B. gerade 15:10 Uhr ist und Sie die Kampagne so geändert haben, dass sie um 15:10 Uhr startet, und dann **Kampagne aktualisieren** ausgewählt haben, ist es jetzt nach 15:10 Uhr, d.h. der Zeitplan für den Start ist abgelaufen. Anstatt die Kampagne für denselben Zeitpunkt zu planen, wählen Sie **Senden, sobald die Kampagne startet**.

### Was ist die „sichere Zone“, bevor Nachrichten in einer geplanten Kampagne in die Warteschlange gestellt werden?

Wir empfehlen, Änderungen an Nachrichten innerhalb der folgenden Zeiten vorzunehmen:

- **Einmalig geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Wiederkehrende geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Lokale Kampagnen zur Sendezeit:** Bearbeiten Sie bis zu 24 Stunden vor der geplanten Sendezeit.
- **Optimale Kampagnen zur Sendezeit:** Bearbeiten Sie bis zu 24 Stunden vor dem Tag, an dem die Kampagne gesendet werden soll.

Wenn Sie außerhalb dieser Empfehlungen Änderungen an Ihrer Nachricht vornehmen, werden diese Updates möglicherweise nicht in der gesendeten Nachricht angezeigt. Wenn Sie beispielsweise die Sendezeit drei Stunden vor dem geplanten Versand einer Kampagne um 12 Uhr Ortszeit bearbeiten, kann Folgendes passieren:

- Braze versendet keine Nachrichten an Nutzer:innen, die den Versandzeitpunkt um mehr als eine Stunde verpasst haben.
- Nachrichten, die sich in der Warteschlange befinden, werden möglicherweise immer noch zu der ursprünglich eingestellten Zeit gesendet und nicht zu der angepassten Zeit.

Sollten Änderungen erforderlich sein, empfehlen wir, die aktuelle Kampagne zu beenden (dadurch werden alle in der Warteschlange befindlichen Nachrichten storniert). Sie können dann die Kampagne duplizieren, die erforderlichen Änderungen vornehmen und die neue Kampagne starten. Möglicherweise müssen Sie Nutzer von dieser Kampagne ausschließen, die bereits die erste Kampagne erhalten haben. Stellen Sie sicher, dass Sie den Kampagnenzeitplan so anpassen, dass der Versand in der jeweiligen Zeitzone zulässig ist.

### Warum haben am Tag der Zeitumstellung keine Nutzer:innen an meiner täglich geplanten Kampagne teilgenommen?

An Tagen, an denen die Sommerzeit beginnt oder endet, können täglich im Zeitplan stehende Kampagnen bis zu einer Stunde früher oder später als üblich ausgeführt werden, je nachdem, ob die Uhren vor- oder zurückgestellt werden. Wenn Ihr Segment auf benutzerdefinierten Attributen oder Ereignissen mit Zeitstempeln basiert, die innerhalb einer Stunde vor dem geplanten Versandzeitpunkt liegen, sind diese Nutzer:innen möglicherweise noch nicht qualifiziert, wenn die Kampagne die Berechtigung am Tag der Sommerzeitumstellung bewertet.

Nehmen wir beispielsweise an, dass Nutzer:innen in der Regel um 15:00 Uhr UTC ein Update für die angepassten Attribute erhalten und Ihre Kampagne täglich um 10:30 Uhr in New York (Eastern Time) läuft. Während New York der Standardzeit (UTC-5) unterliegt, entspricht 10:30 Uhr ET 15:30 Uhr UTC, sodass die Kampagne nach der Protokollierung des Attributs durchgeführt wird. Wenn New York auf Sommerzeit (UTC-4) umstellt, entspricht 10:30 Uhr ET 14:30 Uhr UTC, sodass die Kampagne am Tag der Zeitumstellung auf Sommerzeit vor dem Update des Attributs um 15:00 Uhr UTC ausgeführt werden kann. Da das qualifizierende Attribut noch nicht vorhanden ist, werden diese Nutzer:innen herausgefiltert. Wenn die Wiederteilnahme deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen teilgenommen haben, nicht erneut teilnehmen, was zu null Eingängen für diesen Tag führt.

Um dies zu vermeiden, stellen Sie bitte sicher, dass Ihre benutzerdefinierten Attribut- oder Ereignis-Updates mehr als eine Stunde vor der geplanten Versandzeit der Kampagne erfolgen.

### Warum stimmt die Anzahl der Nutzer, die eine Kampagne betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer, die eine Kampagne betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Dies führt dazu, dass Nutzer:innen aus der Kampagne aussteigen, wenn sie nicht zu Ihrer ausgewählten Zielgruppe gehören, bevor irgendwelche Aktionen triggern.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung in Kampagnen benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach dem Vorkommen des Problems an den Braze Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Was ist der Unterschied zwischen den Optionen „CSV-Export von Nutzerdaten“ und „CSV-Export von E-Mail-Adressen“ auf meiner Seite der Kampagnen-Analytics?

Durch Auswahl der Option **„E-Mail-Adressen für CSV-Export** auswählen“ werden nur die Daten von Nutzern:innen mit E-Mail-Adressen heruntergeladen. Wenn Sie beispielsweise ein Segment mit 100.000 Nutzern haben, aber nur 50.000 dieser Nutzer über E-Mail-Adressen verfügen, und Sie auf **„E-Mail-Adressen als CSV exportieren“** klicken, enthält der Export nur 50.000 Datenzeilen. Im Vergleich dazu werden bei der Auswahl von **„CSV-Export Nutzerdaten“** alle Nutzerdaten exportiert.

### Kann ich nach einer Kampagne anhand ihrer API-Kennung suchen?

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der Seite **Kampagnen**, um nach einer Kampagne anhand ihrer API-Kennung zu suchen. Weitere Informationen finden Sie unter [Suche nach Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Warum werden Leerzeichen in Eingabefeldern anders dargestellt als im angezeigten Text? 

Die Behandlung von Leerzeichen unterscheidet sich aufgrund der CSS-Formatierung zwischen Eingabefeldern und angezeigten Textkomponenten. In Textkomponenten mit dem `white-space: normal`Standard-CSS werden mehrere aufeinanderfolgende Leerzeichen bei der Anzeige zu einem einzigen Leerzeichen zusammengefasst. Dies entspricht dem Standardverhalten von HTML für gerenderten Text. 

Eingabefelder behalten mehrere Leerzeichen genau so bei, wie Sie sie eingeben, da Sie den genauen Abstand für korrekte Daten-Eingaben sehen und bearbeiten müssen. Dies bedeutet, dass Text mit mehreren Leerzeichen in einem Eingabefeld (wo alle Leerzeichen beibehalten werden) anders dargestellt werden kann als in anderen Bereichen des Dashboards (wo CSS mehrere Leerzeichen zusammenfassen kann). 

Wenn Sie beispielsweise einen Namen für eine Kampagne oder einen UTM-Parameter mit mehreren Leerzeichen in ein Eingabefeld eingeben, werden alle Leerzeichen beibehalten. Wenn derselbe Text jedoch in Suchergebnissen, Listen mit Kampagnen oder anderen Textkomponenten erscheint, können aufgrund der CSS-Leerzeichenbehandlung mehrere Leerzeichen als ein einziges Leerzeichen angezeigt werden. 

### Was ist der Unterschied zwischen API-Kampagnen und API-getriggerten Kampagnen?

Mit API-ausgelösten Kampagnen können Sie im Braze-Dashboard Kampagnentexte, multivariate Tests und Wiederzulassungsregeln verwalten und gleichzeitig die Zustellung dieser Inhalte von Ihren eigenen Servern und Systemen triggern. Diese Nachrichten können auch zusätzliche Daten enthalten, die als Template in die Nachrichten in Realtime eingefügt werden.

API-Kampagnen dienen dem Tracking der Nachrichten, die über die API versendet werden. Anders als bei den meisten Kampagnen geben Sie nicht die Nachricht, die Empfänger:innen oder den Zeitplan an, sondern übergeben die Bezeichner an Ihre API-Aufrufe. 

### Was ist der Unterschied zwischen aktionsbasierten und API-gesteuerten Kampagnen?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Aktionsbasiert

Aktionsbasierte Zustellungskampagnen oder Event-gesteuerte Kampagnen sind sehr effektiv für transaktions- oder leistungsbezogene Nachrichten und ermöglichen es Ihnen, diese zu triggern, nachdem ein:e Nutzer:in ein bestimmtes Event abgeschlossen hat. 

| Profis | Nachteile | 
| ---- | ---- |
| • Sichtbarkeit von eingehenden JSON-Payloads in die Plattform (wenn das Event von einem oder einer Testnutzer:in getriggert wurde) über das **Nachrichten-Aktivitätsprotokoll**<br><br>\- Personalisierungselemente sind in den benutzerdefinierten Ereigniseigenschaften enthalten<br><br>• Mit angepassten Events können Sie Segmente von Nutzern:innen erstellen, die für die Nachricht in Frage kommen. | \- Verbraucht Datenpunkte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### API-getriggert

API-getriggerte und Server-getriggerte Kampagnen sind ideal für die Abwicklung von fortschrittlicheren Transaktionen und erlauben es Ihnen, die Zustellung von Kampagneninhalten von Ihren eigenen Servern und Systemen aus zu triggern. Die API-Anfrage zum Auslösen der Nachricht kann auch zusätzliche Daten enthalten, die als Template in die Nachricht in Realtime eingefügt werden.

| Vorteile | Überlegungen | 
| ---- | ---- |
| • Protokolliert keine Datenpunkte<br><br>\- Personalisierungselemente sind in den JSON-Nutzdateneigenschaften enthalten | • Es ist nicht möglich, in den Eigenschaften der JSON-Payload ein Segment von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind<br><br>\- Eingehende JSON-Payloads können mit dem **Message Activity Log** nicht angezeigt werden|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

