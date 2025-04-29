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

Mit Dashboard Builder können Sie angepasste analytische Dashboards von Grund auf und aus von Braze bereitgestellten Templates zusammenstellen und visualisieren. Sie können entweder eine Datenquelle ohne Code (Berichts-Builder) oder eine SQL-Datenquelle (Abfrage-Builder) verwenden, um Ihr Dashboard zu betreiben, oder von einer der vielen Braze-Vorlagen ausgehen.

## Erstellen eines angepassten Dashboards

1. Gehen Sie zu **Analytics** > **Dashboard Builder**.
2. Wählen Sie **Dashboard erstellen**.
3. Wählen Sie aus, welche Datenquelle für Ihre Berichte verwendet werden soll:
- **Berichte**, die mit Report Builder erstellt wurden
- **Angepasste Abfragen**, die in Query Builder erstellt wurden<br><br>![Fenster zum Auswählen der Datenquelle für Ihr Dashboard.][4]<br><br>

Führen Sie nun die entsprechenden Schritte für Ihre Datenquelle aus:

{% tabs %}
{% tab Berichte %}

{: start="4"}
4\. Wählen Sie **\+ Kachel hinzufügen** und wählen Sie dann einen der Berichte aus, die Sie in [Report Builder (Neu)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) erstellt haben.
5\. Wählen Sie das Bleistiftsymbol aus, um die Anzeige des Titels und des Chart-Typs in der Kachel zu ändern.
    \- Sie können zwischen verschiedenen Chart-Typen unterhalb der Standard-Darstellung umschalten. Zu den aktuellen Optionen gehören Balkendiagramme (horizontal oder vertikal) und Liniendiagramme (nur verfügbar, wenn Sie bei der Einrichtung des Berichts-Builders das **Datum** als Drilldown-Option ausgewählt haben).<br><br>![Schaltet zwischen verschiedenen Chart-Typen um.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Verwenden Sie das Dropdown-Menü Metriken, um die Metriken auszuwählen, die Sie in Ihre Visualisierung aufnehmen möchten. Standardmäßig wird in der ersten Spalte des Berichts die Standard-Metrik angezeigt.
6\. Wählen Sie **Speichern**, nachdem Sie die Visualisierung nach Ihren Wünschen geändert haben.
7\. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Sie Ihr Dashboard später leichter wiederfinden können.
{% endtab %}
{% tab Angepasste Abfragen %}
{: start="4"}
4\. Wählen Sie **\+ Kachel hinzufügen** und wählen Sie dann eine Abfrage aus, die Sie in Query Builder ausgeführt haben.
5\. Um zu bearbeiten, wie die Abfrageergebnisse in der Kachel angezeigt werden, wählen Sie das Stiftsymbol aus, um den Titel und den Chart-Typ zu ändern.
    \- Sie können zwischen verschiedenen Chart-Typen unterhalb der Standard-Darstellung umschalten. Zu den Currents-Optionen gehören Tabellen, Balkendiagramme (horizontal oder vertikal) und Liniendiagramme.<br><br>![Schaltet zwischen verschiedenen Chart-Typen um.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Wenn Sie eine der Chart-Optionen wählen, verwenden Sie das Dropdown-Menü **X-Achse**, um eine einzelne Spalte aus Ihren Abfrageergebnissen auszuwählen, die Sie als X-Achse verwenden möchten.
        \- Verwenden Sie das Dropdown-Menü der **Y-Achse**, um auszuwählen, welche Metriken Sie in Ihre Visualisierung aufnehmen möchten. Standardmäßig werden alle Spalten aus Ihren Abfrageergebnissen angezeigt. Deaktivieren Sie also die Spalten, die Sie nicht anzeigen möchten.<br><br>![Schaltet zwischen verschiedenen Chart-Typen um.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
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

Passen Sie die Größe der Kachel an, indem Sie an der unteren rechten Ecke der Kachel ziehen, und passen Sie die Position der Kachel auf dem Dashboard an, indem Sie den Griff an der oberen rechten Ecke der Kachel ziehen.

## Ausführen eines Dashboard Templates

1. Gehen Sie zu **Analytics** > **Dashboard Builder**. Auf der Startseite werden alle vorhandenen Dashboards in Ihrem Workspace aufgelistet, wobei die von Braze erstellten Templates ganz oben stehen. Diese sind mit "(Braze)" im Titel gekennzeichnet.
2. Wählen Sie das Dashboard aus, an dem Sie interessiert sind.
3. Wählen Sie **Dashboard ausführen**, um das entsprechende Dashboard mit dieser Vorlage zu laden.

### Verfügbare Dashboard Templates

Braze bietet vorgefertigte Dashboard-Templates für häufige Anwendungsfälle, wie z.B. die Analyse des Umsatzes unter Verwendung der Last-Touch Attribution. Beachten Sie, dass die Möglichkeit, ein Template Dashboard zu bearbeiten, noch nicht verfügbar ist. Wenden Sie sich an Ihren Customer-Success-Manager:in, wenn Sie bestimmte Dashboard-Vorlagen in zukünftigen Templates sehen möchten.

#### Umsatz – Letztkontakt-Attribution

Das **Revenue - Last Touch Attribution** Template bietet einen Überblick über den Umsatz über Kampagnen, Canvase und Kanäle hinweg. Alle Umsatzdaten werden der zuletzt berührten Nachricht während des Attributionsfensters zugeordnet.

Dazu gehören _E-Mail-Klick_, _Content-Card-Klick_, _In-App-Nachricht-Klick_, _SMS-Zustellung_, _WhatsApp-Lesen_ und _Webhook-Senden_.

| Metriken | Definition |
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

| Metriken | Definition |
| --- | --- |
| Geräteträger | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Geräteträger. |
| Gerätemodell | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Gerätemodell. |
| Betriebssystem des Geräts | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Betriebssystem des Geräts. |
| Gerät Bildschirmgröße | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Bildschirmauflösung (Größe) des Geräts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Teilen Sie Ihr Feedback mit uns

Wählen Sie den Button **Feedback senden** oder kontaktieren Sie Ihren Customer-Success-Manager:in, um uns Ihr Feedback mitzuteilen.

[1]: {% image_buster /assets/img/chart_type.png %}
[2]: {% image_buster /assets/img/sample_tile.png %}
[3]: {% image_buster /assets/img/drag_tile.png %}
[4]: {% image_buster /assets/img/select_data_source.png %}