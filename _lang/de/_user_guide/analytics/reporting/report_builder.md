---
nav_title: Berichts-Builder
article_title: Berichts-Builder
alias: /report_builder/
page_type: reference
description: "Dieser referenzierte Artikel beschreibt das Feature Report Builder."
tool:
    - Reports
page_order: 6.2
---

# Berichts-Builder

> Auf dieser Seite erfahren Sie, wie Sie mit dem Berichts-Builder granulare Berichte mit Braze-Daten erstellen und anzeigen und wie Sie Berichte zu Dashboards hinzufügen.

## Verwendung einer Berichtsvorlage

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Klicken Sie auf den Pfeil für **weitere Optionen** neben dem Button **Neuen Bericht erstellen** und wählen Sie dann **eine Berichtsvorlage verwenden**.<br><br>!["Neuen Bericht erstellen" Button Dropdown mit Optionen zum Erstellen eines angepassten Berichts oder zur Verwendung einer Vorlage.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Wählen Sie eine der Berichtsvorlagen aus der Bibliothek für Braze-Vorlagen aus.
    - Verwenden Sie das Dropdown-Menü **Artikel** und **Tags**, um relevante Berichte für Ihre Anwendungsfälle zu finden.<br><br>!["Braze Berichtsvorlagen" Fenster mit einer Liste von Braze Templates zum Auswählen.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Folgen Sie Schritt 3 und weiter unter [Erstellen eines Berichts](#creating-a-report), um den Bericht weiter an Ihren Anwendungsfall anzupassen.

## Einen Bericht erstellen

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Wählen Sie **Neuen Bericht erstellen**.
3. Wählen Sie in der Dropdown-Liste **Zeilen** aus, worüber Sie berichten möchten:
    - Kampagnen
    - Canvase
    - Kampagnen und Canvase
    - Kanäle
    - Tags

    Beachten Sie, dass sich Ihre Auswahl an **Zeilen** auf [die Metriken](#metrics-availability) auswirkt [, die Sie sehen können](#metrics-availability). Zum Beispiel können Sie multivariate Metriken nur anzeigen, wenn Sie über **Canvase** oder **Kampagnen** mit einem **Varianten-Drilldown** berichten. Sie können diese Metriken nicht anzeigen, wenn Sie über **Kampagnen und Canvase** berichten, selbst wenn diese Kampagnen und Canvase über multivariate Tests verfügen. 

![Der Abschnitt "Zeilen und Spalten" mit Feldern zum Auswählen der Zeilen und Gruppierungen für Ihren Bericht.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Optional) Wählen Sie **Drilldown hinzufügen**, um Ihre Daten in detailliertere Ansichten aufzuschlüsseln:
    \- Kanäle
    \- Datum
        \- Verwenden Sie dies, um Ihre Daten in kleinere Zeitbereiche aufzuteilen. Wenn Sie sich zum Beispiel für die Performance Ihrer Kampagnen pro Tag interessieren, wählen Sie die folgende Konfiguration aus:
            - **Reihen**: Kampagnen
            - **Gruppierung:** Datum
            - **Intervall:** Tage
    \- Varianten
    \- Kampagnen und Canvase

{% alert tip %}
Probieren Sie verschiedene Konfigurationen von Drilldown-Optionen aus, um die [vielen Möglichkeiten zu erkunden, wie Sie Ihre Daten aufschlüsseln können](#metrics-availability).
{% endalert %}

{: start="5"}
5\. Wählen Sie im Abschnitt **Spalten** die Option **Metriken anpassen**.

![Der Bereich "Metriken anpassen" mit Optionen zum Auswählen mehrerer Metriken.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Durchsuchen Sie Metriken nach Kategorien und wählen Sie das entsprechende Kontrollkästchen aus, um eine Metrik zu Ihrem Bericht hinzuzufügen.
    \- Ordnen Sie die Metriken und Spalten neu an, indem Sie das gepunktete Symbol nach oben oder unten ziehen.
7\. In **Berichtsinhalt** konfigurieren Sie den Datumsbereich, für den Sie Daten in Ihren Bericht aufnehmen möchten.
8\. Wählen Sie dann je nach Ihrer Auswahl in Schritt 3, ob Sie Ihrem Bericht manuell oder automatisch Kampagnen, Canvase oder beides hinzufügen möchten.
    - **Manuell hinzufügen:** Wählen Sie die einzelnen Kampagnen oder Canvas aus, die in den Bericht aufgenommen werden sollen, indem Sie die Filter für das Datum der **letzten Sendung** und die Tags oder Kanäle verwenden oder den Namen der Kampagne oder des Canvas suchen.<br><br>![Der Bereich "Kampagnen und Canvases manuell hinzufügen" mit einer Liste von Kampagnen zum Auswählen.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Automatisch hinzufügen:** Legen Sie Regeln dafür fest, welche Kampagnen oder Canvase in den Bericht aufgenommen werden sollen. Sie müssen auf dieser Seite nur ein Feld auswählen.
        \- Beachten Sie, dass zusätzliche Kampagnen oder Canvase, die die Bedingungen erfüllen, die Sie auf diesem Bildschirm festgelegt haben, automatisch zu zukünftigen Ausführungen Ihres Berichts hinzugefügt werden.<br><br>![Der Abschnitt "Kampagnen und Canvase automatisch hinzufügen" mit Feldern zum Festlegen von Regeln, welche Kampagnen und Canvase dem Bericht hinzugefügt werden sollen.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Führen Sie den Bericht aus, indem Sie **Speichern** auswählen ** & Ausführen**.

{% alert note %}
Die Ausführung des Berichts kann bis zu einigen Minuten dauern, je nach Datumsbereich und Anzahl der Kampagnen oder Canvase, die Sie in der Konfigurationsphase ausgewählt haben.
{% endalert %}

## Verfügbarkeit von Metriken

Ihre Auswahl für **Zeilen** wirkt sich auf die Metriken aus, die Sie auswählen können.

{% alert tip %}
Wenn Sie über Canvas-Varianten oder -Schritte berichten möchten, wählen Sie **Canvase** für Zeilen und lassen Sie das Feld entweder leer oder wählen Sie **Datum** als Aufriss. Damit wird ein Dropdown-Menü für die **Canvas-Ansicht** erstellt, in dem Sie Metriken nur für den Canvas anzeigen oder Metriken nach Variante, Schritt oder Nachricht gruppieren können. 

![Das geöffnete Dropdown-Menü "Canvas-Ansicht".]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Metrisch | Beschreibung |
| --- | --- |
| Metriken für die Konversion | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase. |
| Entrys | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase, Tags. |
| Zuletzt gesendetes Datum | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase. Wird nur für geplante Kampagnen angezeigt - bei aktionsbasierten oder API-getriggerten Kampagnen wird es nicht ausgefüllt. |
| Sendungen | Verfügbar für jeden relevanten Kanal. |
| Nachrichten gesendet | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase, Tags. |
| Betreffzeile | Verfügbar für E-Mail-Kampagnen mit **Varianten-Drilldown**, Canvase und Canvase mit **Varianten-Drilldown**. |
| Umsatz gesamt | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase, Tags. Nicht verfügbar mit dem Drilldown **Kanäle**. |
| Eindeutige Impressionen | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase, Tags. |
| Eindeutige Empfänger:innen | Verfügbar für Kampagnen, Canvase, Kampagnen und Canvase, Tags. Nicht verfügbar mit dem Drilldown **Kanäle**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Anzeigen eines Berichts

Nachdem Sie Ihren Bericht ausgeführt haben, können Sie die Ergebnisse in Tabellenform auf der Berichtsseite einsehen. 

![Eine Tabelle mit den Berichtsdaten für die Metriken der einzelnen Kampagnen.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Erstellen eines Berichts-Charts

Unten auf der Seite können Sie ein Chart für Ihre Daten erstellen, indem Sie einen **Chart-Typ** auswählen und die Metriken des Charts konfigurieren. Standardmäßig sehen Sie die erste Metrik.

![Ein Chart der Berichtsdaten mit Optionen zur Konfiguration der x-Achse, der y-Achse, des Chart-Typs und mehr.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Um ein Liniendiagramm zu erstellen, wählen Sie bei der Konfiguration des Berichts **Datum** als Drilldown-Option aus. Dies zeigt Trends im Laufe der Zeit an.
{% endalert %}

#### Herunterladen eines Berichts-Charts

Um ein Bild des Berichts-Charts herunterzuladen, wählen Sie das gepunktete Symbol und dann eine Download-Option.

![Ein Menü mit Download-Optionen für verschiedene Dateiformate.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Einen Bericht teilen

Sie können einen Dashboard-Link zum Bericht freigeben, indem Sie **Teilen** und eine dieser Optionen auswählen:
- **Teilen Sie einen Link:** Kopieren und teilen Sie den Link.

!["Link freigeben"-Dropdown mit einem Link zu dem Bericht.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Senden oder planen Sie eine E-Mail:** Senden Sie sofort oder zu einem bestimmten Zeitpunkt eine E-Mail, die einen Download-Link enthält, der nach einer Stunde abläuft. Sie können Empfänger:innen aus den Nutzern:innen des Dashboards auswählen, die in der Dropdown-Liste **E-Mail-Empfänger** aufgeführt sind, oder eine beliebige andere E-Mail-Adresse eingeben.

!["Zeitplan für eine E-Mail" Fenster mit Feldern, in denen Sie auswählen können, wie der Bericht formatiert wird, wer ihn erhalten soll und wann er gesendet werden soll.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **CSV herunterladen:** Laden Sie eine CSV-Datei des Berichts herunter.

## Einem Dashboard einen Bericht hinzufügen

1. Wählen Sie das gepunktete Symbol am oberen Rand der Berichtstabelle aus.
2. Wählen Sie **Zum Dashboard hinzufügen**.
3. Wählen Sie aus, ob Sie ein neues Dashboard erstellen oder zu einem bestehenden Dashboard hinzufügen möchten.<br><br>![Fenster mit Optionen zum Auswählen, ob Sie den Bericht zu einem neuen oder bestehenden Dashboard hinzufügen möchten.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Folgen Sie den Schritten in [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/), um mehr über die Erstellung eines Dashboards zu erfahren.

