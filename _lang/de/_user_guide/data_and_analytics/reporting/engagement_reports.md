---
nav_title: Engagement-Berichte
article_title: Engagement-Berichte
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Diese Anleitung führt Sie durch die Erstellung, Personalisierung und Zeitplanung von Engagement-Berichten für Kampagnen und Canvase."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Engagement-Berichte

> Mit Engagement-Berichten können Sie Engagement-Statistiken für bestimmte Nachrichten aus Kampagnen und Canvase abrufen, die Sie zu einem von Ihnen gewünschten Zeitpunkt als E-Mail erhalten.

{% alert note %}
Sie benötigen die Berechtigung "Benutzerdaten exportieren", um Engagement-Berichte auszuführen.
{% endalert %}

## Übersicht

Mit Engagement Reports können Sie manuell Kampagnen und Canvases auswählen, die in Ihren E-Mail-Bericht aufgenommen werden sollen, oder Regeln festlegen, um relevante Kampagnen und Canvases automatisch auszuwählen.

Unabhängig von der Anzahl der Kampagnen oder Canvase, die Sie auswählen, werden bis zu zwei CSV-Dateien erstellt - eine für alle Kampagnendaten und eine für alle Canvas-Daten. Sie können auf diese CSV-Dateien über den in Ihrer E-Mail mit dem Bericht eingebetteten Link zugreifen. Engagement-Berichte werden nicht im Braze-Dashboard gespeichert.

Bestimmte Daten werden auf Kampagnen- oder Canvas-Ebene im Gegensatz zur Ebene der einzelnen Kampagnenvarianten oder Canvas-Schritte zusammengefasst. Wenn Sie [einen Canvas-Schritt nach dem Start löschen]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), werden auch die Daten aus den Engagement-Berichten entfernt.

{% alert tip %}
Sie können den Bericht erneut erstellen, um aktuelle Statistiken zu erhalten.
{% endalert %}

## Einen neuen Bericht erstellen

### Schritt 1: Einen Bericht erstellen

Navigieren Sie in Ihrem Dashboard-Konto zu **Analytics** > **Engagement Reports**. Klicken Sie auf **\+ Neuen Bericht erstellen**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Engagement Reports** unter **Daten**.
{% endalert %}

### Schritt 2: Nachrichten hinzufügen

Fügen Sie die Kampagnen und Canvas-Nachrichten hinzu, die Sie in Ihrem Bericht zusammenstellen möchten. Sie können Ihre Nachrichten auf zwei Arten auswählen:

- Kampagnen und Canvase manuell auswählen
- Wählen Sie Kampagnen und Canvase automatisch nach bestimmten Regeln aus.

![engagement_reports_message_selection][2]

#### Kampagnen oder Canvase manuell auswählen

Mit dieser Option können Sie Kampagnen und Canvase für Ihren Bericht auswählen.

#### Automatisch Kampagnen oder Canvase auswählen

Mit dieser Option können Sie automatisch alle Nachrichten aufnehmen, die einen bestimmten [Tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) enthalten. Sie können Nachrichten anvisieren, die einen oder alle der aufgeführten Tags enthalten. Diese Option ist nützlich, wenn Sie regelmäßige Berichte konfigurieren und Ihre Engagement-Nachrichten regelmäßig verschlagworten.

### Schritt 3: Statistiken hinzufügen {#add-statistics-to-your-reports}

Der Schritt **Statistiken hinzufügen** zeigt Ihnen Statistiken für die von Ihnen ausgewählten Kampagnen- oder Werbeträgerarten an. Wenn Sie z.B. E-Mail-Nachrichten ausgewählt haben, werden nur relevante E-Mail-Statistiken angezeigt. Wenn Sie eine Kombination aus E-Mail und Push gewählt haben, sehen Sie die Statistiken für diese beiden Kanäle.

![engagement_report_add_stats][3]

| Kanal | Verfügbare Statistiken |
| ------| --------------|
| E-Mail | Sendungen, Öffnungen, Eindeutige Öffnungen, Klicks, Eindeutige Klicks, Click to Open, Abmeldungen, Bounces, Zustellungen, Spam-Meldungen |
| Push  | Sendungen, Öffnungen, Beeinflusste Öffnungen, Bounces, Body Clicks |
| Web-Push | Sendungen, Öffnungen, Bounces, Body Clicks |
| In-App-Nachricht | Impressionen, Klicks, Erste Schaltflächenklicks, Zweite Schaltflächenklicks |
| Webhook  |  Sendungen, Fehler |
| SMS | Zustellungen, Zustellungen an den Spediteur, Bestätigte Zustellungen, Misslungene Zustellungen, Ablehnungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
*Sendungen an Netzbetreiber* ist veraltet, wird aber für Benutzer, die es bereits haben, weiterhin unterstützt.
{% endalert %}

### Schritt 4: Vollständige Einrichtung des Berichts

Geben Sie Ihrem Bericht einen Namen, wählen Sie die Formatierung und wählen Sie Ihre Empfänger:innen aus. Standardmäßig werden Engagement-Berichte als ZIP-Datei versandt, in der die Daten durch Kommata getrennt sind (wobei die einzelnen Daten durch ein Komma getrennt sind).

Sie können aus den folgenden Komprimierungs- und Begrenzungsoptionen auswählen:

- **Komprimierung:** ZIP, Unkomprimiert, oder gzip
- **Trennzeichen:** Komma (`,`), Doppelpunkt (`:`), Semikolon (`;`), oder Pipe (`|`)

{% alert note %}
Statistiken werden nur für den im Bericht angegebenen Datumsbereich gesammelt. Um genaue Statistiken über die Öffnungs- und Klickraten zu erhalten, wählen Sie einen Datumsbereich aus, der die Zeitspanne umfasst, in der die Sendevorgänge für Ihre Kampagnen und Canvase durchgeführt wurden.
{% endalert %}

#### Zeitrahmen wählen

Standardmäßig basiert der angezeigte Datenbereich auf der Zeitzone Ihres Unternehmens und reicht von der frühesten ausgewählten Nachricht bis zum aktuellen Datum. Sie können dies anpassen, indem Sie das Datums-Dropdown auswählen und die benutzerdefinierte Bereichsauswahl verwenden ODER indem Sie den nächsten Radio-Button auswählen und Ihren Datumsbereich mit den verfügbaren Dropdown-Optionen definieren.

#### Datenanzeige auswählen

Die in den Engagement-Berichten angezeigten Daten sind standardmäßig täglich (1 Tag). Wenn Sie diese Daten über verschiedene Intervalle hinweg betrachten möchten, können Sie eine bestimmte Anzahl von Tagen oder Wochen auswählen, um die Daten für den Bericht zu aggregieren. So können Sie Ihr Engagement nicht nur täglich, sondern auch pro Woche, Monat, Quartal usw. betrachten. Sollte eine zeitgebundene Aggregation nicht ausreichen, können Sie die Daten auch auf Kampagnen- oder Canvas-Ebene exportieren.

![engagement_reports_data_coverage][4]

#### Bericht planen

Es gibt zwei Berichtszeitpläne:

- **Sofort:** Wenn der Bericht gestartet wird, versendet Braze ihn sofort.
- **Mit Termin:** Bei dieser Option können Sie selbst festlegen, wie oft Sie den Bericht erhalten möchten. Sie können wählen, ob Sie ihn alle paar Tage, Wochen oder Monate versenden möchten. Sie können auch festlegen, wann der Berichtsversand beendet werden soll.

![engagement_reports_schedule_report][5]{: style="max-width:65%;" }

### Schritt 5: Überprüfen und starten

Der letzte Schritt bei der Einrichtung Ihres Berichts zeigt eine reine Übersicht über Ihre konfigurierten Optionen. Überprüfen Sie Ihren Bericht. Wenn Sie zufrieden sind, klicken Sie auf **Bericht starten**.

### Schritt 6: Prüfen Sie Ihre E-Mail  

Sie erhalten eine E-Mail mit Links zu Ihren Berichten zu dem von Ihnen gewählten Zeitpunkt oder Zeitplan. **Diese Links laufen eine Stunde nach dem Versand des Berichts ab.** Wenn Sie auf die angegebenen Links klicken, laden Sie automatisch eine ZIP-Datei mit Ihren CSV-Dateien herunter - eine für alle Kampagnen.

Der Bericht enthält alle Statistiken, die im Abschnitt [Statistiken hinzufügen](#add-statistics-to-your-reports) des Einrichtungsvorgangs ausgewählt wurden.


[2]: {% image_buster /assets/img_archive/engagement_report_add_messages.png %}
[3]: {% image_buster /assets/img_archive/engagement_report_add_stats.png %}
[4]: {% image_buster /assets/img_archive/engagement_report_datacoverage.png %}
[5]: {% image_buster /assets/img_archive/engagement_report_reportschedule.png %}
