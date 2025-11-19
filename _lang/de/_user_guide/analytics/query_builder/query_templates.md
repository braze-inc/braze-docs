---
nav_title: Templates für Abfragen
article_title: Query Builder Templates
page_order: 1
page_type: reference
toc_headers: h2
description: "Dieser referenzierte Artikel listet die Arten von Berichten auf, die Sie mit Braze-Daten aus Snowflake im Query Builder erstellen können."
tool: Reports
---

# Query Builder Templates

> Greifen Sie auf die Templates des [Query Builders]({{site.baseurl}}/user_guide/analytics/query_builder/) zu, indem Sie beim Erstellen eines Berichts die **Abfragevorlage** auswählen. Alle Templates zeigen Daten bis zu den letzten 60 Tagen an, aber Sie können diese und andere Werte direkt im Editor bearbeiten.<br><br>Definitionen der Metriken, die in Ihren Query Builder-Berichten erscheinen können, finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/), und filtern Sie nach dem jeweiligen Kanal.

## Kanal Templates

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| Kanal-Engagement und -Umsatz | Dieser Bericht zeigt für jeden Kanal alle Metriken für das Engagement (wie Öffnungen und Klicks), den Umsatz, die Anzahl der Transaktionen und den Durchschnittspreis. {::nomarkdown} <ul> <li> <i>Anzahl der Transaktionen:</i> Anzahl der Kauf-Events </li> <li> <i>Durchschnittlicher Preis:</i> Umsatz geteilt durch Transaktionen </li> </ul> {:/} ![]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Käufe und Umsatz nach Segment | Dieser Bericht zeigt Metriken für die Nachrichten, die für ein bestimmtes Segment gesendet wurden. <br><br> Die Metriken für Käufe sind während des gesamten Berichtszeitraums eindeutig. Ein Nutzer:in kann höchstens einen Kauf tätigen. Die Einnahmen berücksichtigen alle Käufe des Berichtszeitraums. |
| Käufe und Umsatz für Varianten oder Schritte nach Segment | Dieser Bericht zeigt Metriken für die Varianten oder Canvas-Schritte der Nachrichten, die an jedes Segment gesendet wurden. <br><br> Die Metriken für Käufe sind während des gesamten Berichtszeitraums eindeutig. Ein Nutzer:in kann höchstens einen Kauf tätigen. Die Einnahmen berücksichtigen alle Käufe des Berichtszeitraums. |
| Top/Bottom-Messaging für Käufe | Dieser Bericht zeigt die Metriken der Käufe für die obersten oder untersten Kampagnen, Canvase oder Canvas-Schritte. Jede Zeile ist eine Kampagne, ein Canvas oder ein Canvas-Schritt. Sie müssen angeben, ob Sie die Top- oder die Bottom-Performer anzeigen möchten und für welche Metriken diese Analyse durchgeführt werden soll (z. B. *Eindeutige Käufe bei Erhalt*, *Einnahmen bei Erhalt*, *Eindeutige Empfänger*:innen). <br><br> Die Zeilen in den Berichten über die Top-Performer werden von den besten zu den schlechtesten sortiert, während die Zeilen in den Berichten über die Bottom-Performer von den schlechtesten zu den besten sortiert werden. |
{: .reset-td-br-1 .reset-td-br-2 }

## Templates für Kampagnen

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| Kampagnenumsatz nach Land | Dieser Bericht zeigt die Einnahmen pro Land für eine bestimmte Kampagne. Um diesen Bericht auszuführen, müssen Sie den API-Bezeichner für eine Kampagne angeben. Den API-Bezeichner einer Kampagne finden Sie am Ende der Detailseite dieser Kampagne. <br><br> Dieser Bericht zeigt für jedes Land die Höhe des erzielten Umsatzes, die Anzahl der Bestellungen, die Anzahl der Retouren, den Nettoumsatz und den Bruttoumsatz.<br><br> {::nomarkdown} <ul> <li> <i>Bestellungen:</i> Anzahl der Kauf-Events </li> <li><i> Retouren:</i> Anzahl der Kauf-Events mit negativen Umsatzwerten </li> <li><i> Nettoeinnahmen:</i> Einnahmen aus allen nicht zurückgegebenen Waren </li> <li><i> Bruttoeinnahmen:</i> Einnahmen, die den Wert der Rückgaben enthalten </li></ul>{:/} ![]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Canvas-Templates

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| Kampagnenumsatz nach Land | Dieser Bericht zeigt die Einnahmen pro Land für ein bestimmtes Canvas. Um diesen Bericht auszuführen, müssen Sie den API-Bezeichner für ein Canvas angeben. Den Bezeichner der Canvas APIs finden Sie unter **Varianten analysieren**. <br><br> Dieser Bericht zeigt für jedes Land die Höhe des erzielten Umsatzes, die Anzahl der Bestellungen, die Anzahl der Retouren, den Nettoumsatz und den Bruttoumsatz.<br><br> {::nomarkdown} <ul> <li> <i>Bestellungen:</i> Anzahl der Kauf-Events </li> <li><i> Retouren:</i> Anzahl der Kauf-Events mit negativen Umsatzwerten </li> <li><i> Nettoeinnahmen:</i> Einnahmen aus allen nicht zurückgegebenen Waren </li> <li><i> Bruttoeinnahmen:</i> Einnahmen, die den Wert der Rückgaben enthalten </li></ul>{:/} ![]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## E-Mail-Templates

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| E-Mail-Absprünge pro Domain | Die Anzahl der Bounces pro E-Mail Domain, aufgeschlüsselt in Bounces insgesamt, Hard Bounces und Soft Bounces. <br> ![]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| E-Mail-Zustellungsmetriken nach Tag | Dieser Bericht zeigt Metriken für die an jedem Tag gesendeten Nachrichten an, z.B. wie viele E-Mails gesendet, zugestellt, soft bounced und hard bounced wurden. <br><br> Alle Metriken sind während des gesamten Berichtszeitraums eindeutig. Wenn zum Beispiel eine Willkommens-E-Mail einmal am 21\. November und zweimal am 22\. November gebounced und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21\. November erhöht sich um eins.</li><li> Die Metrik <i>Soft Bounces</i> für den 22\. November ist davon nicht betroffen. </li></ul>{:/} ![]({% image_buster /assets/img_archive/email_delivery_day.png %})|
|  E-Mail-Engagement-Metriken nach Segment | Dieser Bericht zeigt Metriken für die an die einzelnen Segmente gesendeten Nachrichten an, z. B. wie viele E-Mails gesendet, zugestellt, soft bounced und hard bounced wurden. <br><br> Alle Metriken sind während des gesamten Berichtszeitraums eindeutig. Wenn zum Beispiel eine Willkommens-E-Mail einmal am 21\. November und zweimal am 22\. November gebounced und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21\. November erhöht sich um eins. </li><li> Die Metrik <i>Soft Bounces</i> für den 22\. November ist davon nicht betroffen.</li></ul>{:/} ![]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| E-Mail-Engagement-Metriken für Varianten oder Schritte nach Segment | Dieser Bericht zeigt Metriken für die Varianten oder Canvas-Schritte der Nachrichten, die an jedes Segment gesendet wurden. Diese Metriken beinhalten, wie viele E-Mails gesendet, zugestellt, soft bounced und hard bounced wurden. <br><br> Alle Metriken sind während des gesamten Berichtszeitraums eindeutig. Wenn zum Beispiel eine Willkommens-E-Mail einmal am 21\. November und zweimal am 22\. November gebounced und nie zugestellt wurde: {::nomarkdown} <ul><li> Die Metrik <i>Soft Bounces</i> für den 21\. November erhöht sich um eins. </li> <li> Die Metrik <i>Soft Bounces</i> für den 22\. November ist davon nicht betroffen.</li></ul> {:/} |
| E-Mail-Performance nach Land | Dieser Bericht zeigt die folgenden Metriken für jedes Land: Versendungen, indirekte Öffnungsrate und direkte Öffnungsrate. Land ist das Land des Nutzers:innen zum Zeitpunkt des Push-Versands. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Änderungsprotokolle für E-Mail-Abos | Dieser Bericht zeigt die Metriken, die über die Änderung des Abos eines jeden Nutzers:innen protokolliert wurden, wie z.B. die E-Mail Adresse, den Status des Abos, den Zeitpunkt der Statusänderung und das zugehörige Canvas oder die Kampagne. |
| Opt-in und Opt-out von Abo-Gruppen für E-Mails | Dieser Bericht zeigt die Anzahl der eindeutigen Opt-Ins und Opt-Outs von Nutzern:innen jeder Abo-Gruppe für jede Woche. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| E-Mail-URLs angeklickt | Dieser Bericht zeigt die Anzahl der Klicks auf die einzelnen Links in einer E-Mail an. Um diesen Bericht auszuführen, müssen Sie den Bezeichner der API für eine Kampagne oder ein Canvas angeben. Den API-Bezeichner einer Kampagne finden Sie unten auf der Detailseite dieser Kampagne und den Canvas-API-Bezeichner unter **Varianten analysieren**. <br><br> Dieser Bericht zeigt de-personalisierte Links und die Anzahl der Klicks für jeden Link. Ihr CSV-Download enthält die IDs aller Nutzer:innen, die geklickt haben, den Link, auf den sie geklickt haben, und einen Zeitstempel, wann sie geklickt haben. <br><br> *De-personalisierte URLs:* URLs, bei denen Liquid-Tags entfernt wurden. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Top/Bottom-Messaging für E-Mail-Engagement | Dieser Bericht zeigt die Metriken für das E-Mail-Engagement für die oberen oder unteren Kampagnen, Canvase oder Canvas-Schritte. Sie müssen angeben, ob Sie die Top- oder die Bottom-Performer anzeigen möchten und für welche Metriken diese Analyse durchgeführt werden soll (z. B. *Gesendet*, *Soft Bounces* und *eindeutige Öffnungen*). <br><br> Die Zeilen in den Berichten über die Top-Performer werden von den besten zu den schlechtesten sortiert, während die Zeilen in den Berichten über die Bottom-Performer von den schlechtesten zu den besten sortiert werden. <br><br> ![]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 }

## Mobile Templates

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| Geräte-Netzbetreiber | Die Anzahl der Nutzer:innen pro Gerät und Anbieter, z. B. Verizon und T-Mobile. <br><br> ![]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Gerätemodelle | Die Anzahl der Nutzer:innen pro Gerätemodell, z. B. iPhone 15 Pro und Pixel 7. <br><br> ![]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Geräte-Betriebssysteme | Die Anzahl der Nutzer:innen pro Betriebssystem, z.B. 17.4 und Android 14. <br><br> ![]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Geräte-Bildschirmauflösungen | Die Anzahl der Nutzer:innen pro Gerät und Bildschirmauflösung, z.B. 1179x2556 und 750x1334. <br><br> ![]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| SMS-Fehlercodes | Dieser Bericht zeigt die Fehlerart und die Anzahl der Fehler für jeden SMS Fehlercode an. <br><br>![]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| SMS Fehler nach Nutzer:innen bereitstellen | Dieser Bericht zeigt die SMS Fehlercodes für einen bestimmten Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 }

## Push-Vorlagen

| Name der Abfrage | Beschreibung | 
| --- | --- | 
| Push-Performance nach Land | Dieser Bericht zeigt die folgenden Metriken für jedes Land: Zustellungen, Öffnungsrate und Klickrate. Land ist das Land des Nutzers:innen zum Zeitpunkt des Versendens der E-Mail. <br><br> ![]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 }

## Segmentierung

| Name der Abfrage | Beschreibung |
| -- | -- |
| E-Mail-Engagement-Metriken nach Segment | Dieser Bericht zeigt die Metriken zur E-Mail Performance, aufgeschlüsselt nach Segmenten auf Ebene der Kampagne oder des Canvas. |
| Käufe und Umsatz nach Segment | Dieser Bericht zeigt Metriken zu Käufen und Umsätzen, aufgeschlüsselt nach Segmenten für eine bestimmte Kampagne oder ein bestimmtes Canvas. |
| Top/Bottom-Messaging für E-Mail-Engagement | Dieser Bericht zeigt die Kampagnen, Canvase oder Canvas-Schritte mit der höchsten oder niedrigsten Performance für eine bestimmte E-Mail Engagement-Metrik.|
| Top/Bottom-Messaging für Käufe | Dieser Bericht zeigt die Kampagnen, Canvase oder Canvas-Schritte mit der höchsten oder niedrigsten Performance für eine bestimmte Kauf- oder Umsatzmetrik. |
| Push-Performance nach Segment | Dieser Bericht zeigt Push-Metriken, die nach Segmenten aufgeschlüsselt sind.|
{: .reset-td-br-1 .reset-td-br-2 }