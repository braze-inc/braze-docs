---
nav_title: Grundlagen der Kampagne
article_title: Grundlagen der Kampagne
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen von Kampagnen und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihrer ersten Kampagnen stellen sollten."
tool: Campaigns

---

# Kampagnen Grundlagen

> Dieser Referenzartikel behandelt die Grundlagen von Kampagnen und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihrer ersten Kampagnen stellen sollten.

## Die Struktur der Kampagne verstehen

Bevor wir uns mit den Feinheiten der Einrichtung von Kampagnen befassen, sollten wir die wichtigsten Details herausarbeiten, um zu verstehen, wie Kampagnen über verschiedene Nachrichtenkanäle funktionieren.

Kampagnen sind ein einziger Nachrichtenschritt, um mit Ihren Nutzern auf Kanälen, oder besser gesagt, auf Nachrichtenkanälen, in Kontakt zu treten. Zu diesen Nachrichtenkanälen gehören Content Cards, E-Mail, In-App-Nachrichten, Push, SMS und MMS sowie Webhooks. Wenn Sie herausfinden, wo sich Ihre Zielgruppe aufhält, können Sie immer die geeigneten Kommunikationskanäle nutzen.

## Customer Journey aufbauen

Da Kampagnen je nach Nachrichtenkanal ganz unterschiedlich aufgebaut sein können, können Sie diese fünf W's der Visualisierung nutzen, um Ihre Strategien und Ziele für die Kundenbindung zu identifizieren und zu konzipieren.

### Worum geht es? Benennen Sie Ihre Kampagne

> Was wollen Sie dem Benutzer helfen zu tun oder zu verstehen?

Unterschätzen Sie niemals die Macht des Namens. Braze wurde für die Zusammenarbeit entwickelt. Dies ist also ein hervorragender Zeitpunkt, um sich darüber klar zu werden, wie Sie Ihre Ziele mit Ihrem Team kommunizieren werden. Wenn Sie mehr über Customer Journeys erfahren möchten, sehen Sie sich unseren Braze Learning-Kurs [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles) an!

### Das "wenn": Startbedingungen schaffen

> Wann wird ein Kunde auf diese Kampagne stoßen? 

Benutzer können Ihrer Kampagne auf drei Arten beitreten: zu einem bestimmten Datum und einer bestimmten Uhrzeit (geplant), wenn sie eine bestimmte Aktion ausführen (aktionsbasiert) oder wenn sie etwas tun, das einen API-Aufruf auslöst (API-ausgelöst). 

Bei der zeitgesteuerten Zustellung werden Ihre Kampagnen so eingestellt, dass sie zu einem bestimmten Zeitpunkt und optional in einem bestimmten Rhythmus versendet werden. Aktionsbasierte Kampagnen reagieren in Echtzeit auf bestimmtes Kundenverhalten. Dies kann einen Kauf oder eine Interaktion mit einer anderen Kampagne beinhalten. API-ausgelöste Kampagnen können eingerichtet werden, um wichtige Kundenaktionen auf Ihrer Plattform zu bestimmen, die, wenn sie ausgeführt werden, einen API-Aufruf an Braze auslösen und Ihre Kampagnen senden.

### Wen sprechen Sie an? Wählen Sie eine Entry-Zielgruppe aus

> Wen versuchen Sie zu erreichen? 

Sie können vordefinierte [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments) verwenden, um Benutzer auf der Grundlage ihrer demografischen, verhaltensbezogenen oder technischen Merkmale und Aktionen anzusprechen. Fügen Sie bei der Erstellung Ihrer Kampagne weitere Filter hinzu, um die Segmentierung weiter anzupassen. Nur wer diese Kriterien erfüllt, kann die User Journey beginnen. In dieser Tabelle finden Sie eine kurze Übersicht über die verfügbaren Filtertypen.

| Filter | Beschreibung |
|---|---|
| Benutzerdefinierte Daten | Segmentieren Sie Nutzer:innen auf der Grundlage von Events und Attributen, die Sie definieren. Sie können spezielle Funktionen für Ihr Produkt verwenden. |
| Benutzer Aktivität | Segmentieren Sie Kund:innen auf der Grundlage ihrer Aktionen und Käufe. |
| Retargeting | Erstellen Sie Kundensegmente zu Personen, die frühere Kampagnen zugeschickt bekommen, erhalten oder mit ihnen interagiert haben. |
| Marketingaktivität | Segmentieren Sie Kunden auf der Grundlage universeller Verhaltensweisen, wie z.B. der letzten Kontaktaufnahme oder erhaltener Kampagnen. |
| Nutzerattribute | Segmentieren Sie Kunden nach ihren konstanten Eigenschaften und Merkmalen. |
| Install-Attribution | Segmentieren Sie Kunden nach ihrer ersten Quelle, Anzeigengruppe, Kampagne oder Anzeige. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Das "Warum": Konversions-Events bestimmen

> Warum führen Sie diese Kampagne durch? 

Man sollte immer ein klares Ziel vor Augen haben – und mit Kampagnen können Sie Ihre Performance anhand von KPIs wie Engagement, Käufe und angepasste Events beurteilen. Wenn Sie mindestens ein [Konversions-Event]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) auswählen, können Sie die Kampagnenperformance genauer nachvollziehen.

### Das "Wo": Meine Zielgruppe finden

> Wo kann ich mein Publikum am besten erreichen?

Hier geht es darum, welche Messaging-Kanäle am besten geeignet sind. Idealerweise möchten Sie Ihre Nutzer dort erreichen, wo sie am aktivsten sind.

### Das "Wie": Angebot erstellen

> Wie baut man eine Kampagne auf, wenn man alle W-Fragen beantwortet hat?

Ziehen Sie die Einrichtung von Varianten und A/B-Tests in Betracht, wenn Sie mehr Erfahrung mit der Erstellung von Kampagnen haben. Beachten Sie, dass bei Kampagnen bis zu acht Varianten mit Kontrollgruppe möglich sind. Nutzen Sie Ihre Kampagnenanalysen, um fundierte Entscheidungen zu treffen, während Sie Ihre Kampagne aufbauen, und passen Sie alles an, von der segmentierten Zielgruppe bis hin zum Inhalt Ihrer Botschaften.

