---
nav_title: Canvas-Analytik
article_title: Canvas-Analytik
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt die verschiedenen Analysen und Berichte, die Sie nutzen können, um die Leistung Ihres Canvas zu verstehen."
tool: 
  - Canvas
  - Reports
  
---

# Canvas-Analysen

> Sie müssen wissen, ob das, was Sie bauen, die Nadel bewegt. Mit Canvas-Analysen können Sie sich ein vollständiges Bild davon machen, wie sich die von Ihnen entwickelten Erlebnisse auf Ihre Ziele auswirken. 

Sobald Sie Ihr Canvas erstellt und in Betrieb genommen haben, navigieren Sie zur **Canvas-Seite** und wählen Ihr Canvas aus, um die Detailseite zu öffnen. Hier können Sie die Leistung Ihres Canvas messen und testen.

## Canvas Übersicht

Der obere Teil der Seite **Canvas-Details** enthält die wichtigsten Canvas-Statistiken. Dazu gehören die Anzahl der innerhalb des Canvas versendeten Nachrichten, die Gesamtzahl der Kunden, die das Canvas betreten haben, die Anzahl der Konvertierungen und Ihre Gesamtrate, der durch das Canvas generierte Umsatz und die geschätzte Gesamtzielgruppe. 

Hier können Sie sich einen Überblick verschaffen und überprüfen, wie Ihr Canvas im Vergleich zu Ihrem Ziel abschneidet.

![][24]

### Änderungen seit letztem Aufruf

Die Anzahl der Aktualisierungen des Canvas durch andere Mitglieder Ihres Teams wird durch die Metrik *Änderungen seit letzter Ansicht* auf der Canvas-Übersichtsseite verfolgt. Wählen Sie **Änderungen seit der letzten Ansicht**, um ein Änderungsprotokoll der Aktualisierungen des Canvas-Namens, des Zeitplans, der Tags, der Nachricht, der Zielgruppe, des Genehmigungsstatus oder der Teamzugriffskonfiguration anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Aktualisierung durchgeführt hat und wann. Mit diesem Changelog können Sie Änderungen an Ihren Canvase überprüfen.

## Visualisierung der Leistung

Auf der Seite mit **den Canvas-Details** können Sie die Leistung für jede Komponente sehen, z. B. wie viele Benutzer das Canvas betreten, zum nächsten Schritt fortfahren oder es verlassen haben. 

{% alert note %}
Bei Canvas Flow verlässt ein Benutzer das Canvas, nachdem er die Nutzlast der Nachricht im letzten Schritt der Benutzerreise eingegeben und erhalten hat.
{% endalert %}

Zu den Metriken gehören auch Impressionen, eindeutige Empfänger:innen, die Anzahl der Konversionen und der erzielte Umsatz. Sie können auf eine Komponente klicken, um Ihre Daten weiter aufzuschlüsseln und die kanalspezifische Performance zu sehen.

![Zwei Beispiele für Leistungsdetails für Canvas-Komponenten. Auf der linken Seite sehen Sie die Leistungsdetails für einen Benutzerpfad mit einer Canvas-Komponente. Rechts sehen Sie Performance-Details für eine erweiterte Canvas-Komponente und einen verschachtelten Schritt, der die Anzahl der Impressionen von In-App-Nachrichten anzeigt.][25]

## Aufschlüsselung der Leistung nach Variante

Klicken Sie unten auf der Seite **Canvas-Details** auf **Varianten analysieren**, um das Modal " **Canvas analysieren"** zu öffnen. Dieses Modal enthält drei Registerkarten: 

- Varianten analysieren
- Canvas-Funnel-Bericht
- Canvas-Bindungsbericht

### Varianten analysieren

Auf der Registerkarte **Varianten analysieren** sehen Sie eine Aufschlüsselung der Leistung nach Variante und Kontrollgruppe, wenn Sie mehr als eine haben. Sie können auch den Bezeichner der Canvas-APIs kopieren, eine CSV-Datei mit den Metriken herunterladen und die Zellen kopieren. Die Registerkarte **Varianten analysieren** enthält eine Tabelle, die Ihnen eine Aufschlüsselung der einzelnen Varianten auf mehreren Ebenen zeigt. 

Sie können schnell effektive Varianten ableiten und die richtige Kadenz, den richtigen Inhalt, die richtigen Auslöser, das richtige Timing und vieles mehr ermitteln.

![][26]

Zu den grundlegenden Metriken gehören die folgenden:  

- **Variante API Bezeichner:** Die API-Kennung Ihrer Variante, die Sie in Ihren API-Aufrufen verwenden können.
- **Eingänge insgesamt:** Die Gesamtzahl der Benutzer, die die Canvas-Variante eingegeben haben.
- **Sendungen insgesamt:** Die Gesamtzahl der gesendeten Nachrichten in der Canvas-Variante.
- **Schritte insgesamt:** Die Gesamtzahl der Schritte in der Canvas-Variante.
- **Gesamtumsatz:** Der Gesamtumsatz in Dollar von Canvas-Empfängern innerhalb des festgelegten primären Umrechnungsfensters.

{% alert note %}
Wie die Conversions wird auch der Umsatz technisch auf der Canvas-Ebene verfolgt, wird aber der letzten Komponente und der letzten Variante zugeordnet, von der der Benutzer eine Nachricht erhalten hat (oder eingegeben hat, wenn er noch keine Nachricht erhalten hat).<br><br>
Wenn ein Benutzer beispielsweise zwei Schritte durchläuft und dann einen Kauf tätigt, wird dieser Umsatz der zweiten Komponente und der von ihm eingegebenen Variante zugeordnet. Wenn sie das Canvas betreten, aber einen Kauf tätigen, bevor sie die erste Canvas-Komponente erhalten, wird dieser Umsatz der eingegebenen Variante zugerechnet, aber keiner Komponente.
{% endalert %}

Darüber hinaus können Sie eine genauere Aufschlüsselung der [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) sehen, einschließlich der folgenden:

- Konversionssummen und Konversionsraten für jedes Konversionsereignis
- Aufschwung gegenüber der Kontrollvariante
- Statistische Sicherheit für jedes Umwandlungsereignis

### Funnel-Bericht

Der Funnel-Bericht bietet einen visuellen Bericht, mit dem Sie die Reise Ihrer Kund:innen nach dem Erhalt eines Canvas analysieren können. Wenn Ihr Canvas eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie auf einer detaillierteren Ebene nachvollziehen, wie sich die verschiedenen Varianten auf den Konversionstrichter ausgewirkt haben, und auf der Grundlage dieser Daten optimieren. Weitere Informationen zu Trichterberichten finden Sie unter [Trichterberichte][2].

### Bindungsbericht

Die Nutzerbindung ist eine der wichtigsten Metriken für jeden Marketer. Wenn engagierte Nutzer immer wieder zurückkommen, ist das ein Zeichen dafür, dass das Geschäft gut läuft. Braze ermöglicht es Ihnen jetzt, die Benutzerbindung direkt auf der **Canvas Analytics-Seite** zu messen. Weitere Informationen über das Lesen und Interpretieren Ihres Retentionsberichts finden Sie unter [Retentionsberichte][1].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/
[24]:{% image_buster /assets/img_archive/Journey_5.png %}
[25]:{% image_buster /assets/img_archive/Journey_6.png %}
[26]:{% image_buster /assets/img_archive/analyze_variants.png %}
