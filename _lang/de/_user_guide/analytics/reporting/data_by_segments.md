---
nav_title: Metriken nach Segmenten
article_title: Metriken nach Segmenten
page_order: 2.5
page_type: reference
description: "Auf dieser Seite wird beschrieben, wie Sie mit den Berichtsvorlagen des Query Builders Performance-Metriken für Kampagnen, Canvas, Varianten und Segmente aufschlüsseln können."
tool: 
  - Segments
  - Reports
  
---

# Metriken nach Segmenten

> Verwenden Sie die [Berichts-Builder-Templates des Query Builders]({{site.baseurl}}/user_guide/analytics/query_builder/), um die Performance-Metriken für Kampagnen, Canvas, Varianten und Segmente aufzuschlüsseln.

Das [Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) muss für die Segmente aktiviert sein, für die Sie Metriken abrufen möchten.

Um diese Berichte auszuführen, gehen Sie wie folgt vor:
1. Wählen Sie in **Query Builder** die Option, einen neuen SQL-Bericht mit einem Template zu erstellen. 
2. Wählen Sie **Segmentaufschlüsselungen** für die Metriken aus. Dadurch werden Templates für diejenigen gefiltert, bei denen die Metriken Aufschlüsselungen von Segmenten enthalten, die sind:
- Metriken für die E-Mail Performance nach Segmenten
- E-Mail-Engagement-Metriken für Varianten oder Schritte nach Segment
- Käufe und Umsatz nach Segment
- Käufe und Umsatz für Varianten oder Schritte nach Segment
- Push-Performance nach Segment

![Die Seite Segmentaufschlüsselung enthält einen SQL-Editor, ein seitliches Panel mit Tabs für Variablen, verfügbare Datentabellen, Abfrageverlauf und den KI Query Builder sowie einen Ergebnisbereich.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Vorlagen für Berichte

{% tabs %}
{% tab Email engagement metrics by segment %}

### Anzeigen von Metriken für Kampagnen oder Canvase {#campaign-canvas-email}

Um die Metriken zur E-Mail Performance auf Kampagnen- oder Canvas-Ebene nach Segmenten aufgeschlüsselt anzuzeigen, verwenden Sie den Tab [Variablen](#variables), um die Kampagnen oder Canvase und einen Zeitrahmen für die Abfrage der Daten anzugeben. Wenn keine Kampagnen oder Canvase angegeben werden, enthält der Bericht E-Mails aus allen Kampagnen und Canvase aus dem angegebenen Zeitraum. Sie können sich auch alle Kampagnen und Canvase mit bestimmten Tags anzeigen lassen.

Die folgenden Metriken für E-Mails sind in diesem Bericht verfügbar:
- Sendungen
- Zustellungen
- Reklamationen
- Eindeutige Öffnungen
- Eindeutige Öffnungen der Maschine
- Eindeutige nicht-maschinelle Öffnungen
- Eindeutige Klicks
- Abmeldungen
- Absprünge
- Weiche Sprünge
- Aufgeschoben

#### Ergebnisse

Ihre Ergebnisse zeigen die Metriken für das E-Mail Engagement nach Segmenten für die von Ihnen ausgewählten Kampagnen oder Canvase. Wenn Sie keine bestimmten Kampagnen oder Canvase ausgewählt haben, zeigt Ihr Bericht die E-Mail-Metriken für jedes Segment über alle E-Mail-Kampagnen und Canvase innerhalb des Zeitrahmens Ihres Berichts. 

- **Reihen:** Segmente
- **Kolumnen:** Metriken für das Engagement bei E-Mails

### Anzeigen von Metriken für Varianten oder Schritte

Um die E-Mail Performance nach Segmenten auf Ebene der Kampagnenvariante, der Canvas-Variante oder des Canvas-Schrittes zu betrachten, wählen Sie zunächst einen Bericht auf Ebene der Variante oder des Schrittes aus (dies sind Berichte, die im Titel "für Varianten oder Schritte" enthalten), und legen Sie dann auf dem Tab **Variablen** Folgendes fest:

- Spezifische Kampagne oder Canvas (erforderlich bei Verwendung eines Berichts auf Varianten- oder Schrittsebene) 
- Varianten (erforderlich, wenn Sie einen Bericht auf Varianten- oder Schrittebene verwenden)
- Canvas-Schritt (optional)

Die Metriken sind die gleichen wie die, die für die [Kampagnen- oder Canvas-Ebene des](#campaign-canvas-email) Templates angeboten werden. Wenn Sie mehrere Varianten auswählen, werden Ihre Ergebnisse nach Varianten gruppiert.

#### Ergebnisse

Ihre Ergebnisse zeigen die Metriken für das E-Mail Engagement nach Segmenten für die von Ihnen ausgewählten Varianten oder Schritte. 

- **Reihen:** Segmente
- **Kolumnen:** Metriken für das Engagement bei E-Mails

{% endtab %}

{% tab Purchases and revenue by segment %}
### Anzeigen von Metriken für Kampagnen oder Canvase

Um die Metriken zu Käufen und Umsätzen für eine bestimmte Kampagne oder ein bestimmtes Canvas nach Segmenten aufzuschlüsseln, verwenden Sie den Tab [Variablen](#variables), um Folgendes anzugeben:

- Konversions-Fenster (die Anzahl der Tage nach dem Erhalt einer E-Mail oder einem Klick, die Braze Käufen oder Einnahmen attributieren soll)
- Spezifisches Produkt (optional) 

Verwenden Sie außerdem den Tab **Variablen**, um anzugeben, ob der Bericht für eine oder mehrere Kampagnen oder Canvase oder für einen oder mehrere Tags ausgeführt werden soll. Wenn Sie keine Kampagnen, Canvase oder Tags ausgewählt haben, wird der Bericht für alle E-Mails aus Kampagnen oder Canvase in dem von Ihnen gewählten Zeitrahmen ausgeführt.

Derzeit bezieht dieser Bericht Metriken nur aus dem E-Mail-Kanal. Umsatz- oder Kaufdaten aus anderen Kanälen als E-Mails werden in dem Bericht nicht berücksichtigt. 

Die folgenden Metriken sind für E-Mails verfügbar:

- Eindeutige Käufe bei Erhalt
- Einnahmen bei Erhalt
- Eindeutige Käufe auf Klick
- Einnahmen bei Klick
- Eindeutige Empfänger:innen
- Eindeutige Klicks auf E-Mails

Alle Metriken verwenden eindeutige E-Mail Empfänger:innen als Nenner.

#### Definitionen

- "Bei Erhalt" bezieht sich auf Kauf-Events oder Einnahmen, die innerhalb des von Ihnen angegebenen Konversions-Fensters stattgefunden haben, nachdem Nutzer:innen die angegebenen Kampagnen oder Canvase erhalten haben. 
- "Bei Klick" referenziert auf die Kauf-Events oder Umsätze, die nach den Kauf-Events innerhalb des von Ihnen festgelegten Konversions-Fensters eingetreten sind, nachdem Nutzer:innen auf die angegebenen Kampagnen oder Canvase geklickt haben.

Nehmen wir zum Beispiel an, ein Segment enthält 10 Nutzer:innen und fünf von ihnen haben nach Erhalt Ihrer E-Mail einen Kauf getätigt. Wenn einer dieser fünf einen Kauf getätigt hat, nachdem er auf Ihre E-Mail geklickt hat, würde Ihre "Eindeutige Kaufrate bei Erhalt" 50% und Ihre "Eindeutige Kaufrate bei Klick" 10% betragen.

Der Bericht zeigt Metriken für E-Mails, darunter eindeutige Käufe bei Erhalt, Einnahmen bei Erhalt, eindeutige Käufe bei Klick, Einnahmen bei Klick, eindeutige Empfänger und eindeutige Klicks auf E-Mails.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Ergebnisse

Ihre Ergebnisse zeigen Metriken zum Kauf nach Segmenten für Ihre ausgewählten Kampagnen oder Canvase. Wenn Sie keine bestimmten Kampagnen oder Canvase ausgewählt haben, zeigt Ihr Bericht die Kaufmetriken für jedes Segment über alle E-Mail Kampagnen oder Canvase innerhalb des Zeitrahmens Ihres Berichts. 

- **Reihen:** Segmente
- **Kolumnen:** Metriken zum Kauf


### Anzeigen von Metriken für Varianten oder Schritte

Um die nach Segmenten aufgeschlüsselten Kauf- und Umsatzmetriken für eine bestimmte Kampagnenvariante, Canvas-Variante oder einen Canvas-Schritt anzuzeigen, verwenden Sie den Tab [Variablen](#variables), um Folgendes anzugeben:

- Spezifische Kampagne oder Canvas
- Varianten 
- Canvas-Schritt (optional) 
- Zeitspanne
- Spezifisches Produkt (optional) 

#### Ergebnisse

Ihre Ergebnisse zeigen die Metriken nach Segmenten für die von Ihnen ausgewählten Varianten oder Schritte.

- **Reihen:** Segmente
- **Kolumnen:** Metriken zum Kauf

{% endtab %}
{% tab Top or bottom messaging for email engagement %}

### Anzeige der Metriken für die besten oder schlechtesten Performer

Dieser Bericht auf dem Tab [Variablen](#variables) zeigt die Kampagnen, Canvase oder Canvas-Schritte mit der höchsten oder niedrigsten Performance für eine bestimmte E-Mail Engagement-Metrik an. 

Anwendungsfälle umfassen: 
- 10 Kampagnen mit den eindeutigsten Öffnungszeiten von E-Mails
- 25 Canvase mit den meisten Abmeldungen per E-Mail
- 50 Canvas-Schritte mit den meisten eindeutigen Klicks

Die folgenden Metriken für E-Mails sind in diesem Bericht verfügbar:
- Sendungen
- Zustellungen
- Reklamationen
- Eindeutige Öffnungen
- Eindeutige Öffnungen der Maschine
- Eindeutige nicht-maschinelle Öffnungen
- Eindeutige Klicks
- Abmeldungen
- Absprünge
- Weiche Sprünge
- Reklamationen

Um diesen Bericht anzuzeigen, müssen Sie die folgenden Variablen auf dem Tab **Variablen** angeben:
- **Metriken:** Wählen Sie eine der Metriken aus, nach denen Sie Ihre Ergebnisse bewerten möchten
- **Anzahl der Berichte:** Wählen Sie die obersten oder untersten Ergebnisse und die Anzahl der Ergebnisse aus, z. B. die obersten 10 oder die untersten 15.
- **Art der Nachricht:** Geben Sie an, ob Ihre Ergebnisse Kampagnen, Canvase oder Canvas-Schritte sind.

#### Ergebnisse

Ihre Ergebnisse zeigen die obersten (oder untersten) Kampagnen, Canvase oder Canvas-Schritte, die Sie ausgewählt haben. Wenn Sie z.B. die Top 10 Kampagnen für die Klickrate ausgewählt haben, werden Ihre Ergebnisse die Top 10 Kampagnen in der Reihenfolge der höchsten bis niedrigsten Klickrate anzeigen. In Ihren Spalten werden alle Metriken für das Engagement per E-Mail für jede Zeile (Kampagnen, Canvase oder Nachrichtenschritte) angezeigt.

{% endtab %}
{% tab Top or bottom messaging for purchases %}

### Anzeige der Metriken für die besten oder schlechtesten Performer

Dieser Bericht auf dem Tab [Variablen](#variables) zeigt die Kampagnen, Canvase oder Canvas-Schritte mit der höchsten oder niedrigsten Performance für eine bestimmte Kauf- oder Umsatzmetrik an.

Anwendungsfälle umfassen:
- 20 Kampagnen mit den höchsten Kaufraten für ein bestimmtes Produkt
- 25 Canvase mit den meisten Einnahmen
- 10 Canvas-Schritte mit der niedrigsten Kaufrate für ein Produkt

Die folgenden Metriken für E-Mails sind in diesem Bericht verfügbar:
- Eindeutige Käufe bei Erhalt
- Einnahmen bei Erhalt
- Eindeutige Käufe auf Klick
- Einnahmen bei Klick
- Eindeutige Empfänger:innen
- Eindeutige Klicks auf E-Mails

Um diesen Bericht anzuzeigen, müssen Sie die folgenden Variablen auf dem Tab **Variablen** angeben:
- **Metriken:** Wählen Sie eine der Metriken aus, nach denen Sie Ihre Ergebnisse bewerten möchten
- **Anzahl der Berichte:** Wählen Sie die obersten oder untersten Ergebnisse und die Anzahl der Ergebnisse aus, z. B. die obersten 10 oder die untersten 15.
- **Art der Nachricht:** Geben Sie an, ob Ihre Ergebnisse Kampagnen, Canvase oder Canvas-Schritte sind.
- **Konversion-Fenster:** Die Anzahl der Tage nach dem Erhalt einer E-Mail oder einem Klick, denen Braze Käufe oder Einnahmen attributiert 

#### Definitionen

- "Bei Erhalt" bezieht sich auf Kauf-Events oder Einnahmen, die innerhalb des von Ihnen angegebenen Konversions-Fensters stattgefunden haben, nachdem Nutzer:innen die angegebenen Kampagnen oder Canvase erhalten haben. 
- "Bei Klick" referenziert auf die Kauf-Events oder Umsätze, die nach den Kauf-Events innerhalb des von Ihnen festgelegten Konversions-Fensters eingetreten sind, nachdem Nutzer:innen auf die angegebenen Kampagnen oder Canvase geklickt haben.

Nehmen wir zum Beispiel an, ein Segment enthält 10 Nutzer:innen und fünf von ihnen haben nach Erhalt Ihrer E-Mail einen Kauf getätigt. Wenn einer dieser fünf einen Kauf tätigte, nachdem er auf Ihre E-Mail geklickt hatte, läge Ihre Rate der eindeutigen Käufe bei Erhalt bei 50% und Ihre Rate der eindeutigen Käufe bei Klick bei 10%.

#### Ergebnisse

Ihre Ergebnisse zeigen die obersten (oder untersten) Kampagnen, Canvase oder Canvas-Schritte, die Sie ausgewählt haben. Wenn Sie z.B. die Top 10 Kampagnen für "Umsatz bei Klick" ausgewählt haben, werden Ihre Ergebnisse die Top 10 Kampagnen in der Reihenfolge vom höchsten zum niedrigsten "Umsatz bei Klick" anzeigen. In Ihren Spalten werden alle Metriken für jede Zeile (Kampagnen, Canvase oder Nachrichtenschritte) angezeigt.

{% endtab %}
{% tab Push performance by segment %}

### Anzeigen von Push-Metriken für Segmente

Dieser Bericht auf dem Tab [Variablen](#variables) zeigt Push-Metriken nach Segmenten aufgeschlüsselt an. 

Auf dem Tab **Variablen** geben Sie die Kampagnen oder Canvase an, für die Sie Metriken anzeigen möchten, sowie einen Zeitrahmen für das Abrufen der Daten. Wenn Sie keine Kampagnen oder Canvase auswählen, zeigt der Bericht Pushs aus allen Kampagnen und Canvase in dem von Ihnen angegebenen Zeitraum an. Sie können sich auch alle Kampagnen und Canvase mit bestimmten Tags anzeigen lassen.

Die folgenden Push-Metriken sind in diesem Bericht verfügbar:

- Sendungen
- Absprünge
- Zustellungen
- Direkt öffnen

#### Ergebnisse

Ihr Bericht wird die folgenden Ergebnisse anzeigen:

- **Reihen:** Segmente
- **Kolumnen:** Push-Metriken
{% endtab %}
{% endtabs %}