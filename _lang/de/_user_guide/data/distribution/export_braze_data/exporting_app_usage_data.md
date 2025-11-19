---
nav_title: Nutzungsanalysen exportieren
article_title: Exportieren Sie Usage Analytics
page_order: 3

page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie allgemeine Daten zur App-Nutzung exportieren können."
tool: 
  - Reports

---

# Exportieren von Nutzungsanalysen

> Auf dieser Seite finden Sie die **Startseite** des Dashboards, die sowohl Daten über die Nutzung der App auf hoher Ebene als auch detaillierte Statistiken über verschiedene KPIs nach Datum enthält.

So exportieren Sie CSVs von Daten von dieser Seite:

1. Legen Sie den Zeitspanne und die Apps fest, für die Sie Daten anzeigen möchten. Standardmäßig zeigt das Dashboard die Daten der letzten 30 Tage für alle Apps an.

![Zeitspanne und App-Felder auf dem Home Dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Scrollen Sie nach unten zum Diagramm **Performance über Zeit**.
3\. Wählen Sie die Daten, die Sie exportieren möchten, im Feld **Statistik für** aus. Sehen Sie die [verfügbaren Daten](#available-data), die Sie exportieren können.

![Grafik Performance im Zeitverlauf auf dem Home Dashboard.]({% image_buster /assets/img_archive/home_dashboard_export.png %})

{:start="4"}
4\. Wählen Sie <i class="fas fa-bars" title="Diagramm-Kontextmenü"></i> und dann eine Exportoption.

## Verfügbare Daten

Sie können CSV-Dateien mit den folgenden Daten exportieren:

- Sitzungsanzahl nach Datum
    - (Optional) Anzahl der Sitzungen für verschiedene Segmente
    - (Optional) Sitzungsanzahl für verschiedene App-Versionen
- DAUs nach Datum
    - (Optional) DAUs für verschiedene Segmente
- E-Mail Statistik nach Datum
    - Anzahl der gesendeten E-Mails
    - Anzahl der zugestellten E-Mails
    - Anzahl der geöffneten E-Mails
    - Anzahl E-Mail-Klicks
    - Anzahl E-Mail Bounces
    - Anzahl der als Spam gemeldeten E-Mails
- In-App-Nachrichten nach Datum
    - Anzahl der gesendeten In-App-Nachrichten
    - In-App-Nachricht-Impressionen
    - Anzahl der geöffneten In-App-Nachrichten
- MAUs nach Datum
- Anzahl der neuen Nutzer:innen nach Datum
- Push-Benachrichtigungen nach Datum
    - (Optional) Push-Benachrichtigungen für verschiedene App-Plattformen
    - Anzahl der gesendeten Push-Benachrichtigungen
    - Öffnungen gesamt
    - Direkte Öffnungen
    - Absprünge
- Sitzungsanzahl pro Stunde
- Sitzungsanzahl je MAU nach Datum
- Klebrigkeit nach Datum

{% alert tip %}
Hilfe bei CSV- und API-Exporten finden Sie in unserem Artikel zur [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

