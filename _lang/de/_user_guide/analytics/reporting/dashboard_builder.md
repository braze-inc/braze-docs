---
nav_title: Dashboard-Builder
article_title: Dashboard-Builder
alias: "/dashboard_builder/"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie mit Dashboard Builder Dashboards und Visualisierungen anhand von Berichten erstellen können, die mit Query Builder erstellt wurden."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Dashboard-Builder

> Verwenden Sie Dashboard Builder, um Dashboards und Visualisierungen mit Berichten zu erstellen, die in Report Builder oder Query Builder erstellt wurden.

Mit dem Dashboard Builder können Sie benutzerdefinierte Analyse-Dashboards von Grund auf neu erstellen und visualisieren, auch auf Basis der von Braze bereitgestellten Dashboards. Sie können entweder eine No-Code-Datenquelle (Berichts-Builder) oder eine SQL-Datenquelle (Query Builder) für Ihr Dashboard verwenden oder mit einem der zahlreichen von Braze bereitgestellten Dashboards beginnen.

## Erstellen eines angepassten Dashboards

1. Gehen Sie zu **Analytics** > **Dashboard Builder**.
2. Wählen Sie **Dashboard erstellen**.
3. Wählen Sie aus, welche Datenquelle für Ihre Berichte verwendet werden soll:
- **Berichte**, die mit Report Builder erstellt wurden
- **Angepasste Abfragen**, die in Query Builder erstellt wurden<br><br>![Fenster zum Auswählen der Datenquelle für Ihr Dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Führen Sie nun die entsprechenden Schritte für Ihre Datenquelle aus:

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Wählen Sie **\+ Kachel hinzufügen** und wählen Sie dann einen der Berichte aus, die Sie in [Report Builder (Neu)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) erstellt haben.

{% alert important %}
Nachdem ein Berichts-Builder-Bericht zu einer Dashboard Builder-Kachel hinzugefügt wurde, ist die Kachel nicht mehr mit dem ursprünglichen Bericht verbunden. Wenn Sie den ursprünglichen Bericht im Berichts-Builder bearbeiten, müssen Sie die vorhandene Dashboard-Kachel löschen und eine neue erstellen, wobei Sie den aktualisierten Bericht als Datenquelle verwenden.
{% endalert %}

{: start="5"}
5\. Wählen Sie das Bleistiftsymbol aus, um die Anzeige des Titels und des Chart-Typs in der Kachel zu ändern.
    \- Sie können zwischen verschiedenen Chart-Typen unterhalb der Standard-Darstellung umschalten. Zu den aktuellen Optionen gehören Balkendiagramme (horizontal oder vertikal) und Liniendiagramme (nur verfügbar, wenn Sie bei der Einrichtung des Berichts-Builders das **Datum** als Drilldown-Option ausgewählt haben).<br><br>![Umschaltflächen für verschiedene Chart-Typen.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Verwenden Sie das Dropdown-Menü Metriken, um die Metriken auszuwählen, die Sie in Ihre Visualisierung aufnehmen möchten. Standardmäßig wird in der ersten Spalte des Berichts die Standard-Metrik angezeigt.
6\. Wählen Sie **Speichern**, nachdem Sie die Visualisierung nach Ihren Wünschen geändert haben.
7\. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Sie Ihr Dashboard später leichter wiederfinden können.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Wählen Sie **\+ Kachel hinzufügen** und wählen Sie dann eine Abfrage aus, die Sie in Query Builder ausgeführt haben.
5\. Um zu bearbeiten, wie die Abfrageergebnisse in der Kachel angezeigt werden, wählen Sie das Stiftsymbol aus, um den Titel und den Chart-Typ zu ändern.
    \- Sie können zwischen verschiedenen Chart-Typen unterhalb der Standard-Darstellung umschalten. Zu den Currents-Optionen gehören Tabellen, Balkendiagramme (horizontal oder vertikal) und Liniendiagramme.<br><br>![Umschaltflächen für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        Wenn Sie eine der Chart-Optionen auswählen, verwenden Sie das Dropdown-Menü **der X-Achse,** um eine einzelne Spalte aus Ihren Abfrageergebnissen auszuwählen, die als X-Achse verwendet werden soll.
        \- Verwenden Sie das Dropdown-Menü der **Y-Achse**, um auszuwählen, welche Metriken Sie in Ihre Visualisierung aufnehmen möchten. Standardmäßig werden alle Spalten aus Ihren Abfrageergebnissen angezeigt. Deaktivieren Sie also die Spalten, die Sie nicht anzeigen möchten.<br><br>![Umschaltflächen für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Optional) Sie können die Dropdown-Liste **Gruppierung** verwenden, um Ihre Abfrageergebnisse zu gruppieren. Wenn Sie zum Beispiel die ID einer Kampagne als Spaltenergebnis haben und alle Zeilen mit diesem Wert addieren möchten, verwenden Sie das Dropdown-Menü **Gruppierung**.  
        \- (Optional) Um die angezeigten Daten zu bearbeiten, wählen Sie die Abfrage aus, die mit dem Bildmaterial verknüpft ist, und nehmen Sie Ihre Änderungen im [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) vor.
6\. Wählen Sie **Speichern**, nachdem Sie die Visualisierung nach Ihren Wünschen geändert haben.
7\. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Sie Ihr Dashboard später leichter wiederfinden können.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Wiederholen Sie die Schritte 4-7 für Ihre jeweilige Methode, bis Sie Ihr gewünschtes Dashboard erstellt haben.
9\. Wählen Sie **Dashboard anzeigen** > wählen Sie **Dashboard ausführen**. 

Es kann einige Minuten dauern, bis Ihr Dashboard die Erstellung der Berichte abgeschlossen hat.

{% alert note %}
Sie können bis zu 10 Kacheln zu einem Dashboard hinzufügen.
{% endalert %}

## Dashboard-Kacheln verwalten

### Kacheln löschen

Löschen Sie eine Dashboard-Kachel, indem Sie unten auf der Kachel **"Kachel löschen"** auswählen. **Diese Aktion kann nicht rückgängig gemacht werden.**

### Kacheln duplizieren

Erstellen Sie eine Kopie Ihrer Kachel, indem Sie **Kachel duplizieren** am unteren Rand der Kachel auswählen.

### Größe und Position der Kacheln anpassen

Adjust die Kachelgröße, indem Sie die rechte untere Ecke der Kachel ziehen, und Adjust die Position der Kachel auf dem Dashboard, indem Sie den Griff in der rechten oberen Ecke der Kachel ziehen.

## Ausführen eines Dashboards

1. Gehen Sie zu **Analytics** > **Dashboard Builder**. Auf der Startseite werden alle in Ihrem Workspace vorhandenen Dashboards aufgelistet, wobei die von Braze erstellten Dashboards oben angezeigt werden. Diese sind mit "(Braze)" im Titel gekennzeichnet.
2. Wählen Sie das Dashboard aus, an dem Sie interessiert sind.
3. Bitte wählen Sie **„Dashboard ausführen“,** um das entsprechende Dashboard zu laden.

### Verfügbare Dashboards

Braze stellt vorgefertigte Dashboards für häufig verwendete Anwendungsfälle bereit, beispielsweise für die Analyse von Umsätzen unter Verwendung der Last-Touch-Attribution. Bitte beachten Sie, dass die Möglichkeit, ein Dashboard zu bearbeiten, derzeit noch nicht verfügbar ist. Bitte wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie in Zukunft ein bestimmtes Dashboard sehen möchten.

#### Umsatz – Letztkontakt-Attribution

Das Dashboard **„Umsatz – Last-Touch-Attribution“** bietet einen Überblick über den Umsatz über Kampagnen, Canvases und Kanäle hinweg. Alle Umsatzdaten werden der zuletzt berührten Nachricht während des Attributionsfensters zugeordnet.

Zu den Interaktionen zählen _E-Mail-Klicks_ (Link-Klicks), _Klicks auf Content-Cards_, _Klicks auf In-App-Nachrichten_ (ausgenommen Schließen-Buttons), _Push-Öffnungen_, _Klicks auf SMS-Kurzlinks_, _WhatsApp-Lesungen_ und _Webhook-Sendungen_.

| Metrisch | Definition |
| --- | --- |
| Gesamte Einnahmen von Last Touch | Eine Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem Last-Touch-Ereignis innerhalb des ausgewählten Datumsbereichs und Attributionsfensters. |
| Kaufkonversionen insgesamt | Eine Zählung aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis. |
| Durchschnittliche Tage bis zur Konvertierung | Die durchschnittliche Zeit zwischen allen Kampagnen- und Canvas-Kauf-Events mit einem qualifizierenden Last-Touch-Ereignis. |
| Umsatz pro Empfänger:in | Summe der Einnahmen aus qualifizierten Umsatzereignissen geteilt durch die Anzahl eindeutiger Nutzer:innen, die eine Nachricht innerhalb des Datumsbereichs erhalten haben. |
| Eindeutige Käufer | Anzahl der eindeutigen Nutzer:innen mit einem qualifizierten Umsatzereignis. |
| Umsatz nach Land | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem Last-Touch-Ereignis, gruppiert nach Land. |
| Einnahmen nach Kampagnen | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Kampagnen. |
| Umsatz nach Kampagnenvariante | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Kampagnenvarianten. |
| Einnahmen durch Canvas | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Canvas. |
| Einnahmen durch Canvas-Variante | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Canvas-Variante. |
| Einkäufe pro Produkt | Eine Zählung aller Käufe, gruppiert nach Produkt. |
| Umsatz nach Kanal | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Kanal. | 
| Zeitreihen zu den Einnahmen | Summe aller Kampagnen- und Canvas-Umsatzereignisse mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Tag in UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Geräte und Träger

| Metrisch | Definition |
| --- | --- |
| Geräteträger | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Geräteträger. |
| Gerätemodell | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Gerätemodell. |
| Betriebssystem des Geräts | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Betriebssystem des Geräts. |
| Gerät Bildschirmgröße | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Bildschirmauflösung (Größe) des Geräts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segment-Insights – E-Mail

| Metrisch  | Definition  |
|---|---|
| Wöchentliche E-Mail-Metriken (Raten) | E-Mail-Engagement-Raten (Zustellungs-, Bounce-, Öffnungs-, Klick- und Abmelderaten), gruppiert nach Segmenten und dargestellt als wöchentliche Zeitreihe.|
| Wöchentliche E-Mail-Metriken (Anzahl) | E-Mail-Engagement-Zahlen (gesendet, zugestellt, Bounces, Öffnungen, Klicks, Abmeldungen) werden nach Segmenten gruppiert und als wöchentliche Zeitreihe dargestellt.|
| Wöchentliche Metriken (Raten) | Konversionsraten (Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und Klicks, gruppiert nach Segmenten und dargestellt als wöchentliche Zeitreihe.|
| Wöchentliche Metriken (Anzahl) | Kaufzahlen und Umsatzsummen aus E-Mail-Öffnungen und Klicks, gruppiert nach Segmenten und dargestellt als wöchentliche Zeitreihe.|
| E-Mail-Engagement nach Segment | Übersichtstabelle mit den Gesamtmetriken zum E-Mail-Engagement (gesendet, zugestellt, Bounces, Öffnungen, Klicks, Abmeldungen und deren Raten), aggregiert nach Segment.|
| Einkäufe&  Umsatz nach Segmenten | Übersichtstabelle mit den Gesamtkaufmetriken (Käufe, Umsatz und Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und Klicks, aggregiert nach Segmenten.|
| Die 10 besten Kampagnen für Metriken zum Engagement | Rangliste der Kampagnen mit den höchsten Metriken zum E-Mail-Engagement (konfigurierbare Metrik für das Ranking).|
| Die 10 Kampagnen mit den niedrigsten Metriken zum Engagement | Rangliste der Kampagnen mit den niedrigsten Metriken zum Engagement bei E-Mails (konfigurierbare Kennzahl für die Rangliste).|
| Die 10 besten Canvases für Metriken des Engagements | Rangliste der Canvases mit den höchsten E-Mail-Engagement-Metriken (konfigurierbare Metrik für das Ranking).|
| Die 10 schlechtesten Canvases für Metriken zum Engagement | Rangliste der Canvases mit den niedrigsten Metriken zum E-Mail-Engagement (konfigurierbare Metrik für die Rangliste).|
| Die zehn besten Kampagnen für Kaufmetriken | Rangliste der Kampagnen mit den höchsten Metriken zur Kaufkonversion aus E-Mail-Engagement (konfigurierbare Metrik für das Ranking).|
| Die 10 schlechtesten Kampagnen für Metriken zum Kauf | Rangliste der Kampagnen mit den niedrigsten Metriken zur Kaufkonversion aus E-Mail-Engagement (konfigurierbare Metrik für das Ranking).|
| Die 10 beliebtesten Canvases zum Kauf – Metriken | Rangliste der Canvases mit den höchsten Metriken zur Kaufkonversion aus E-Mail-Engagement (konfigurierbare Metrik für das Ranking).|
| Die 10 beliebtesten Canvases zum Kauf – Metriken | Rangliste der Canvases mit den niedrigsten Metriken der Kaufkonversion aus E-Mail-Engagement (konfigurierbare Metrik für die Rangliste).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### SitzungsAnalytics

| Metrisch | Definition  |
|---|---|
| Anzahl der Sitzungen pro Tag (Zeitreihen) | Anzahl der eindeutigen Sitzungen, gruppiert nach Tag innerhalb des ausgewählten Datumsbereichs, dargestellt als Zeitreihe.|
| Durchschnittliche Anzahl von Sitzungen pro Nutzer:in | Die durchschnittliche Anzahl der Sitzungen pro Nutzer:in wird berechnet, indem die Gesamtzahl der Sitzungen durch die Anzahl der eindeutigen Nutzer:innen innerhalb des ausgewählten Datumsbereichs dividiert wird.|
| Kampagnen werden in Sitzungen umgewandelt | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Konversionen einer Kampagne stattfanden, gruppiert nach ID der Kampagne und sortiert nach Sitzungsanzahl.|
| Canvases werden in Sitzungen umgewandelt | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Canvas-Konversionen stattfanden, gruppiert nach Canvas-ID und sortiert nach Sitzungsanzahl.|
| Gesamtzahl der Sitzungen pro Nutzer:in | Liste der 1.000 Nutzer:innen mit den meisten Sitzungen innerhalb des ausgewählten Zeitraums.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Teilen Sie Ihr Feedback mit uns

Wählen Sie den Button **Feedback senden** oder kontaktieren Sie Ihren Customer-Success-Manager:in, um uns Ihr Feedback mitzuteilen.

