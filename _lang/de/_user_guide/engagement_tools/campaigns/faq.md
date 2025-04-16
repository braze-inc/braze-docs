---
nav_title: FAQ
article_title: ""
page_order: 10
page_type: FAQ
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Kampagnen."
tool: Campaigns

---

# 

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Kampagnen.

### 

   

### Kann ich eine Kontrollgruppe zu meiner Multichannel-Kampagne hinzufügen?

Nein, Kontrollgruppen in Kampagnen sind für die Nachrichtenübermittlung über einen einzigen Kanal gedacht, z. B. E-Mail A gegenüber E-Mail B. Versuchen Sie alternativ, [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) zum Testen verschiedener Kanäle, Nachrichteninhalte und Zustellungszeitpunkte zu verwenden. 

### Wie kann ich mit dem Testen und Optimieren von Kampagnen beginnen?

Multivariaten-Kampagnen und die Ausführung von Canvase mit mehreren Varianten sind ein guter Anfang! Sie können zum Beispiel eine [multivariate Kampagne]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) durchführen, um eine Nachricht mit verschiedenen Kopien oder Betreffzeilen zu testen. 

### Warum ist die Öffnungsrate für meine Kampagne gesunken?

Niedrige Öffnungsraten haben nicht immer etwas mit einem technischen Problem zu tun. Es kann Probleme mit dem Ausschneiden von E-Mails geben, was dazu führt, dass ein Tracking-Pixel fehlt. Es ist jedoch auch möglich, dass weniger Nutzer:innen ihre E-Mails aufgrund des Inhalts oder einer veränderten Zielgruppe öffnen. 

### Wie werden die Zielgruppen von Kampagnen bewertet?

Standardmäßig überprüfen Kampagnen die Zielgruppen-Filter bei der Eingabe. Bei aktionsbasierten Kampagnen mit Verzögerung besteht die Möglichkeit, die Segmentkriterien zum Zeitpunkt des Versands neu zu bewerten, um sicherzustellen, dass die Nutzer noch zur Zielgruppe gehören, wenn die Nachricht versendet wird. 

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger und der Anzahl der Sendungen für eine bestimmte Kampagne oder ein bestimmtes Canvas?

Eine mögliche Erklärung für diesen Unterschied könnte darin liegen, dass in der Kampagne oder im Canvas die erneute Qualifizierung aktiviert ist. Wenn Sie diese Option aktivieren, können Benutzer, die sich für das Segment und die Zustellungseinstellungen qualifizieren, die Nachricht mehr als einmal erhalten. Wenn die erneute Qualifizierung nicht aktiviert ist, kann die wahrscheinliche Erklärung für den Unterschied zwischen gesendeten und eindeutigen Empfänger:innenn darin liegen, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben. 

Wenn Sie z.B. ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, könnte ein bestimmter Benutzer mit einem mobilen und einem Desktop-Gerät mehr als eine Nachricht erhalten.

### Warum hat meine Kampagne eine kleinere erreichbare Nutzerbasis als das Segment, das ich für die Kampagne verwende?

Wenn Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) eingerichtet haben, verhindert dies, dass ein bestimmter Prozentsatz Ihrer erreichbaren Zielgruppe Kampagnen erhält. Das bedeutet, dass die Anzahl der erreichbaren Nutzer für Ihr Segment manchmal größer sein kann als die Anzahl der erreichbaren Nutzer für Ihre Kampagne, selbst wenn die Kampagne dasselbe Segment verwendet.

### Was bietet die Zustellung in der lokalen Zeitzone?

Die Zustellung zur Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen an ein Segment zuzustellen, das auf der individuellen Zeitzone eines Nutzers oder einer Nutzerin basiert. Ohne die Zustellung in der lokalen Zeitzone werden die Kampagnen auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant. 

Wenn beispielsweise ein in London ansässiges Unternehmen eine Kampagne um 12 Uhr mittags versendet, erreicht sie die Nutzer an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, das Versenden von Push-Benachrichtigungen am frühen Morgen an Ihre Nutzer zu vermeiden!

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

Wenn eine Kampagne beispielsweise um 19 Uhr UTC zugestellt werden soll, beginnen wir mit dem Versand der Kampagne in die Warteschlange, sobald eine Zeitzone (wie Samoa) zugewiesen wird.  

Ein weiteres Beispiel: Sie möchten zwei Kampagnen erstellen, die am selben Tag versendet werden sollen - eine am Morgen und eine am Abend - und fügen einen Filter hinzu, damit Benutzer die zweite Kampagne nur erhalten können, wenn sie die erste bereits erhalten haben. Bei der Zustellung in einer lokalen Zeitzone kann es vorkommen, dass einige Nutzer die zweite Kampagne nicht erhalten. 

### Wie plane ich eine Kampagne für eine lokale Zeitzone?



Braze empfiehlt dringend, alle Kampagnen in der Ortszeit 24 Stunden im Voraus zu planen.  Sie können diese Kampagnen jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Denken Sie daran, dass Braze keine Nachrichten an Nutzer:innen sendet, die die Sendezeit um mehr als 1 Stunde überschritten haben. 

 Außerdem muss die Sendezeit, die Sie für Ihre Kampagne wählen, in der Zeitzone Ihres Unternehmens noch nicht stattgefunden haben.

Wenn Sie eine Kampagne in einer lokalen Zeitzone bearbeiten, die weniger als 24 Stunden im Voraus geplant wurde, wird der Zeitplan der Nachricht nicht geändert. Wenn Sie eine Kampagne in einer lokalen Zeitzone so bearbeiten, dass sie zu einem späteren Zeitpunkt versendet wird (z. B. um 19 Uhr statt um 18 Uhr), erhalten die Nutzer, die sich zum Zeitpunkt der ursprünglichen Sendezeit im Zielsegment befanden, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie eine lokale Zeitzone bearbeiten, um zu einer früheren Zeit zu senden (z. B. 16 Uhr statt 17 Uhr), wird die Kampagne trotzdem an alle Mitglieder des Segments zur ursprünglichen Zeit (17 Uhr) gesendet. 

{% alert note %}
Bei Canvas-Komponenten müssen Nutzer:innen nicht 24 Stunden lang in der Komponente sein, um die nächste Komponente in der Zustellung zur Ortszeit zu erhalten.
{% endalert %}

Wenn Sie den Nutzern erlaubt haben, sich erneut für die Kampagne zu qualifizieren, dann erhalten sie sie wieder zur ursprünglichen Zeit (17 Uhr). 

### Wann werden Änderungen an lokalen Zeitzonen-Kampagnen wirksam?

Zielsegmente für Kampagnen in lokalen Zeitzonen sollten mindestens ein 48-Stunden-Fenster für alle zeitbasierten Filter enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Nehmen wir zum Beispiel ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern zusammenstellt:

- Erstmals verwendet vor mehr als 1 Tag
- Erstmals vor weniger als 2 Tagen benutzt

Bei der Zustellung in der lokalen Zeitzone können Benutzer in diesem Segment aufgrund der Zustellungszeit und der lokalen Zeitzone des Benutzers fehlen. Das liegt daran, dass ein:e Nutzer:in das Segment zu dem Zeitpunkt verlassen kann, zu dem die jeweilige Zeitzone die Zustellung triggert.

### Welche Änderungen kann ich an geplanten Kampagnen vor dem Start vornehmen?

Wenn die Kampagne geplant ist, müssen außer der Zusammensetzung der Nachricht noch andere Änderungen vorgenommen werden, bevor wir die Nachrichten in die Warteschlange stellen. Wie bei allen Kampagnen können Sie Konversions-Events nicht mehr bearbeiten, nachdem sie gestartet wurden.

### Ich habe meine geplante Kampagne aktualisiert. Warum ist es nicht gestartet?

Dies kann passieren, wenn eine Kampagne genau zu dem Zeitpunkt gestartet werden soll, zu dem sie aktualisiert wurde.  Anstatt die Kampagne für denselben Zeitpunkt zu planen, wählen Sie **Senden, sobald die Kampagne startet**.

### Was ist die „sichere Zone“, bevor Nachrichten in einer geplanten Kampagne in die Warteschlange gestellt werden?

Sie können Änderungen an Nachrichten innerhalb der folgenden Sicherheitszonen vornehmen:

- **Einmalig geplante Kampagnen** können bis zum geplanten Sendezeitpunkt bearbeitet werden.
- **Wiederkehrende geplante Kampagnen** können bis zur geplanten Sendezeit bearbeitet werden.
- 
- 

### Was passiert, wenn ich die Sendezeit innerhalb der "sicheren Zone" ändere?

Eine Änderung des Sendezeitpunkts von Kampagnen innerhalb dieses Zeitraums kann zum Beispiel zu unerwünschtem Verhalten führen:

- Braze sendet keine Nachrichten an Benutzer, die die Sendezeit um mehr als eine Stunde überschritten haben.
- Nachrichten, die sich in der Warteschlange befinden, werden möglicherweise immer noch zu der ursprünglich eingestellten Zeit gesendet und nicht zu der angepassten Zeit.

### Was soll ich tun, wenn die "sichere Zone" bereits überschritten ist?

Um sicherzustellen, dass die Kampagnen wie gewünscht funktionieren, empfehlen wir, die aktuelle Kampagne zu stoppen (dadurch werden alle Nachrichten in der Warteschlange gelöscht).  Möglicherweise müssen Sie Nutzer von dieser Kampagne ausschließen, die bereits die erste Kampagne erhalten haben.

Stellen Sie sicher, dass Sie die Zeitpläne der Kampagnen so anpassen, dass das Senden in der Zeitzone zulässig ist.

### Warum stimmt die Anzahl der Nutzer, die eine Kampagne betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer, die eine Kampagne betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen [Änderung des Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)-Trigger). 

{% alert tip %}

{% endalert %}

### Was ist der Unterschied zwischen den Optionen CSV-Export von Benutzerdaten und CSV-Export von E-Mail-Adressen auf meiner Kampagnenanalyseseite?

Wenn Sie die Option **CSV-Export von E-Mail-Adressen** wählen, werden nur Daten für Benutzer mit E-Mail-Adressen heruntergeladen. Wenn Sie z.B. ein Segment mit 100.000 Benutzern haben, aber nur 50.000 dieser Benutzer E-Mail-Adressen haben und Sie auf **CSV-Export von E-Mail-Adressen** klicken, dann sollten Sie nur 50.000 Datenzeilen in der CSV-Datei sehen. Wenn Sie dagegen **CSV Benutzerdaten exportieren** wählen, werden alle Benutzerdaten exportiert.

### Kann ich nach einer Kampagne anhand ihrer API-Kennung suchen?

Ja, verwenden Sie den Filter `api_id:YOUR_API_ID` auf der Seite **Kampagnen**, um nach einer Kampagne anhand ihrer API-Kennung zu suchen. Weitere Informationen finden Sie unter [Suche nach Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### 

 

API-Kampagnen dienen dem Tracking der Nachrichten, die Sie über die API versenden.  

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

 

| Profis | Nachteile | 
| ---- | ---- |
| \- Verbraucht keine Datenpunkte<br><br>\- Personalisierungselemente sind in den JSON-Nutzdateneigenschaften enthalten | • Es ist nicht möglich, in den Eigenschaften der JSON-Payload ein Segment von Nutzer:innen zu erstellen, die für die Nachricht berechtigt sind<br><br>|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

