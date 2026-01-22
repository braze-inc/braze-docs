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

Um eine Multichannel-Kampagne zu erstellen, wählen Sie **Messaging** > **Kampagnen**. Wählen Sie dann **Kampagne erstellen** > **Multichannel**. Von hier aus können Sie aus den folgenden Messaging-Kanälen auswählen: Content-Cards, E-Mail, LINE, Push-Benachrichtigungen, SMS/MMS/RCS, Webhook, oder WhatsApp.

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

### Warum hat meine Kampagne eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Kampagne verwende?

Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) eingerichtet haben, verhindert dies, dass ein bestimmter Prozentsatz Ihrer erreichbaren Zielgruppe Kampagnen erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer für Ihre Kampagne, selbst wenn die Kampagne dasselbe Segment verwendet.

### Was bietet die Zustellung in der lokalen Zeitzone?

Die Zustellung zur Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen an ein Segment zuzustellen, das auf der individuellen Zeitzone eines Nutzers oder einer Nutzerin basiert. Ohne die Zustellung in der lokalen Zeitzone werden die Kampagnen auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant. 

Wenn beispielsweise ein in London ansässiges Unternehmen eine Kampagne um 12 Uhr mittags versendet, erreicht sie die Nutzer an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, Push-Benachrichtigungen am frühen Morgen nicht an Ihre Nutzer:innen zu senden.

### Wie erkennt Braze die Zeitzone eines Benutzers?

Braze ermittelt automatisch die Zeitzone eines Benutzers anhand seines Geräts. Dies gewährleistet die Genauigkeit der Zeitzone und die vollständige Abdeckung Ihrer Nutzer:innen. Benutzer, die über die Benutzer-API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App vom SDK erkannt werden. 

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) auf dem Dashboard überprüfen.

### Wann bewertet Braze die Benutzer für die Bereitstellung in der lokalen Zeitzone?

Für die Zustellung zur Ortszeit prüft Braze die Nutzer:innen während dieser beiden Instanzen auf ihre Zugangsberechtigung:

- Um Samoa-Zeit (UTC+13) des geplanten Tages
- Zur Ortszeit des geplanten Tages

Damit ein:e Nutzer:in für einen Entry in Frage kommt, muss er für beide Prüfungen in Frage kommen. Wenn ein Canvas zum Beispiel am 7\. August 2021 um 14 Uhr Ortszeit gestartet werden soll, müssten für einen Nutzer in New York die folgenden Prüfungen durchgeführt werden, um die Berechtigung zu prüfen:

- New York am 6\. August 2021 um 9 Uhr
- New York am 7\. August 2021 um 2 Uhr nachmittags

Beachten Sie, dass der oder die Nutzer:in 24 Stunden vor dem Start in dem Segment sein muss. Wenn der oder die Nutzer:in bei der ersten Prüfung nicht teilnahmeberechtigt ist, führt Braze die zweite Prüfung nicht durch.

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

Wenn die Kampagne geplant ist, müssen außer der Zusammensetzung der Nachricht noch andere Änderungen vorgenommen werden, bevor wir die Nachrichten in die Warteschlange stellen. Wie bei allen Kampagnen können Sie Konversions-Events nicht mehr bearbeiten, nachdem sie gestartet wurden.

### Ich habe meine geplante Kampagne aktualisiert. Warum ist es nicht gestartet?

Dies kann passieren, wenn eine Kampagne genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde. Wenn es z.B. gerade 15:10 Uhr ist und Sie die Kampagne so geändert haben, dass sie um 15:10 Uhr startet, und dann **Kampagne aktualisieren** ausgewählt haben, ist es jetzt nach 15:10 Uhr, d.h. der Zeitplan für den Start ist abgelaufen. Anstatt die Kampagne für denselben Zeitpunkt zu planen, wählen Sie **Senden, sobald die Kampagne startet**.

### Was ist die „sichere Zone“, bevor Nachrichten in einer geplanten Kampagne in die Warteschlange gestellt werden?

Wir empfehlen, Änderungen an Nachrichten innerhalb der folgenden Zeiten vorzunehmen:

- **Einmalig geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Wiederkehrende geplante Kampagnen:** Bearbeiten Sie bis zur geplanten Sendezeit.
- **Lokale Kampagnen zur Sendezeit:** Bearbeiten Sie bis zu 24 Stunden vor der geplanten Sendezeit.
- **Optimale Kampagnen zur Sendezeit:** Bearbeiten Sie bis zu 24 Stunden vor dem Tag, an dem die Kampagne gesendet werden soll.

Wenn Sie außerhalb dieser Empfehlungen Änderungen an Ihrer Nachricht vornehmen, werden diese Updates möglicherweise nicht in der gesendeten Nachricht angezeigt. Wenn Sie beispielsweise die Sendezeit drei Stunden vor dem geplanten Versand einer Kampagne um 12 Uhr Ortszeit bearbeiten, kann Folgendes passieren:

- Braze sendet keine Nachrichten an Benutzer, die die Sendezeit um mehr als eine Stunde überschritten haben.
- Nachrichten, die sich in der Warteschlange befinden, werden möglicherweise immer noch zu der ursprünglich eingestellten Zeit gesendet und nicht zu der angepassten Zeit.

Wenn Sie Änderungen vornehmen müssen, empfehlen wir Ihnen, die aktuelle Kampagne zu stoppen (dadurch werden alle Nachrichten in der Warteschlange gelöscht). Sie können dann die Kampagne duplizieren, die erforderlichen Änderungen vornehmen und die neue Kampagne starten. Möglicherweise müssen Sie Nutzer von dieser Kampagne ausschließen, die bereits die erste Kampagne erhalten haben. Stellen Sie sicher, dass Sie die Zeitpläne der Kampagnen so anpassen, dass das Senden in der Zeitzone zulässig ist.

### Warum stimmt die Anzahl der Nutzer, die eine Kampagne betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer, die eine Kampagne betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Dies führt dazu, dass Nutzer:innen aus der Kampagne aussteigen, wenn sie nicht zu Ihrer ausgewählten Zielgruppe gehören, bevor irgendwelche Aktionen triggern.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung in Kampagnen benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach dem Vorkommen des Problems an den Braze Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Was ist der Unterschied zwischen den Optionen CSV-Export von Benutzerdaten und CSV-Export von E-Mail-Adressen auf meiner Kampagnenanalyseseite?

Wenn Sie die Option **CSV-Export von E-Mail-Adressen** wählen, werden nur Daten für Benutzer mit E-Mail-Adressen heruntergeladen. Wenn Sie z.B. ein Segment mit 100.000 Benutzern haben, aber nur 50.000 dieser Benutzer E-Mail-Adressen haben und Sie auf **CSV-Export von E-Mail-Adressen** klicken, dann sollten Sie nur 50.000 Datenzeilen in der CSV-Datei sehen. Wenn Sie dagegen **CSV Benutzerdaten exportieren** wählen, werden alle Benutzerdaten exportiert.

### Kann ich nach einer Kampagne anhand ihrer API-Kennung suchen?

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der Seite **Kampagnen**, um nach einer Kampagne anhand ihrer API-Kennung zu suchen. Weitere Informationen finden Sie unter [Suche nach Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

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
| \- Zeichnet keine Datenpunkte auf<br><br>\- Personalisierungselemente sind in den JSON-Nutzdateneigenschaften enthalten | • Es ist nicht möglich, in den Eigenschaften der JSON-Payload ein Segment von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind<br><br>\- Eingehende JSON-Payloads können mit dem **Message Activity Log** nicht angezeigt werden|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

