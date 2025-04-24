---
nav_title: Segment Daten
article_title: Anzeigen und Verstehen von Segmentdaten
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt den Abschnitt Segmente in Ihrem Braze Dashboard und enthält eine Zusammenfassung der bereitgestellten Statistiken."
tool: 
  - Segments
  - Reports
  
---
# Segment Daten

> Dieser Referenzartikel erklärt den Abschnitt Segmente Ihres Braze Dashboards und enthält eine Zusammenfassung der bereitgestellten Statistiken.

## Zugriff auf Daten über Ihre Segmente und Zugehörigkeit

Die Seite **Segmente** Ihres Braze-Dashboards enthält eine Zusammenfassung aller Ihrer Segmente und ermöglicht es Ihnen, detaillierte Daten für jedes einzelne Segment zu prüfen. Suchen Sie auf dieser Seite nach einem Segment und klicken Sie auf den Namen des Segments, um dessen Daten zu bearbeiten und anzuzeigen. Wie Sie ein Segment erstellen können, erfahren Sie unter [Erstellen eines Segments][3].

![Seite „Segmente“][1]

Nachdem Sie auf den Namen eines Segments geklickt haben, können Sie sich die Segmentstatistiken und Filter ansehen. Sie können Ihr Segment durch Hinzufügen oder Löschen von Filtern bearbeiten. Achten Sie darauf, alle Änderungen zu speichern!

![Segmentdaten][2]

Wenn Sie [analytics tracking] für ein Segment][9] einschalten, können Sie mit Braze-Sitzungen, angepasste Events und Umsätze über einen bestimmten Zeitraum für dieses Segment anzeigen.

### Segment-Statistiken

Sie sehen die folgenden Segmentstatistiken, die in Echtzeit aktualisiert werden, wenn Sie Filter hinzufügen oder löschen:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Statistik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Nutzer:innen insgesamt</td>
            <td class="no-split">Wie viele Nutzer:innen Ihre App insgesamt hat.</td>
        </tr>
        <tr>
            <td class="no-split">Ausgewählte Nutzer:innen</td>
            <td class="no-split">Wie viele Nutzer:innen in Ihrem Segment sind und wie viel Prozent Ihrer gesamten Nutzerbasis sie ausmachen.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (Zahlende Nutzer:innen)</td>
            <td class="no-split">Der Lifetime-Value pro Nutzer:innen (LTV) in diesem Segment und der Lifetime-Value pro zahlenden Nutzer:innen in diesem Segment. Der LTV wird berechnet, indem Sie Ihren Lifetime-Umsatz durch die Lifetime-Nutzer:innen teilen.</td>
        </tr>
        <tr>
            <td class="no-split">Per E-Mail erreichbar (Opted-In)</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Emailable' %} Aufgrund von <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">Spam-Bestimmungen</a> ist es oft eine gute Idee, Ihre Nutzer:innen aufzufordern, sich explizit anzumelden, indem Sie eine Double-Opt-In-Richtlinie einführen, bei der die Nutzer:innen auf einen Link in einer ersten Bestätigungs-E-Mail klicken müssen. Um mehr Nutzer zum Opt-in zu ermutigen, können Sie eine Nachricht an <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">diejenigen</a> richten, die <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">sich weder an- noch abgemeldet haben</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push Enablement (Opt-in)</td>
            <td class="no-split">„Push aktiviert“ bezieht sich auf die Anzahl der Nutzer:innen mit mindestens einem Push-Token. Einige Nutzer haben möglicherweise mehrere Push-Token (z. B. wenn sie ein iPhone und ein iPad besitzen), so dass die Anzahl der Push-Benachrichtigungen, die Sie an dieses Segment senden, größer sein kann als die Anzahl der "Push-fähigen" Nutzer. „Opt-In“ bezieht sich auf die Anzahl der Nutzer:innen, die sich ausdrücklich für Push-Benachrichtigungen entschieden haben. Die Nutzer müssen sich immer explizit dafür entscheiden, dass Sie ihnen Push-Nachrichten senden dürfen.</td>
        </tr>
    </tbody>
</table>

### Segment-Insights

Auf der Seite [Segment-Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) in Ihrem Dashboard können Sie sehen, wie die Performance eines Segments im Vergleich zu einem anderen Segment bei einer Reihe von vordefinierten KPIs ist.

### Messaging-Nutzung
Der Abschnitt **Messaging-Nutzung** zeigt, welche Segmente, derzeit aktivierten Kampagnen und derzeit aktivierten Canvase auf Ihr Segment abzielen.

![Unter Messaging-Verwendung sehen Sie die Kampagnen, in denen Ihr Segment verwendet wird.][4]

### Historische Mitgliedschaft
Der Abschnitt **Historische Mitgliedschaft** zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentzugehörigkeit nach Datumsbereich zu filtern. 

Die historische Anzahl der Segmentmitglieder ist eine Schätzung, ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie auf **Exakte Statistik berechnen** klicken. Braze schätzt die Zugehörigkeitsanzahl, indem es die Nutzer:innen in einem zufälligen Bucket-Bereich abfragt. Das bedeutet, dass an einem Tag die Zugehörigkeitsanzahl auf Nutzern und Nutzerinnen mit einer zufälligen Bucket-Nummer von 111-120 basieren könnte und an einem anderen Tag auf Nutzern und Nutzerinnen mit einer zufälligen Bucket-Nummer von 8.452-8.455. Daher kann das Diagramm an jedem Datum leichte Schwankungen aufweisen, da unterschiedlich viele Nutzer:innen innerhalb der zufälligen Bucket-Bereiche landen.

![Verwenden Sie das Dropdown-Menü „Bisherige Zugehörigkeit“, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.][10]

### Nutzervorschau

Um detaillierte, benutzerspezifische Informationen über Ihre Segmente anzuzeigen, klicken Sie auf **Nutzerdaten** und wählen Sie **Nutzer:innen Vorschau**.

![Nutzer:innen-spezifische Informationen][7]

Auf dieser Seite können Sie eine Reihe von angepassten Attributen einsehen, z. B. Geschlecht, Alter, Anzahl der Sitzungen und ob der oder die Nutzer:in sich für Push und E-Mail entschieden hat.

![Nutzervorschau][8]

## Leistungsdaten nach Segmenten

Verwenden Sie die [Berichtsvorlagen des Query Builders]({{site.baseurl}}/user_guide/data_and_analytics/reporting/data_by_segments/), um Leistungskennzahlen für Kampagnen, Canvas, Varianten und Schritte nach Segmenten aufzuschlüsseln.

## Erstellen eines Berichts zur Segmentaufschlüsselung mit dem Abfrage-Builder

Um einen Bericht aus einer [Query Builder-Vorlage]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) zu erstellen, gehen Sie zu **Query Builder** und gehen Sie wie folgt vor:

1. Wählen Sie **SQL-Abfrage erstellen** > **Abfrage-Template**.
2. Filtern Sie Templates für diejenigen, die Metriken mit „Segmentaufschlüsselungen“ haben.
3. Wählen Sie das Template aus, das Sie verwenden möchten.
4. Füllen Sie die Variablen in Ihrer SQL-Vorlage auf der Registerkarte [Variablen](#variables) aus.
5. (optional) Bearbeiten Sie direkt die SQL in der Vorlage.
6. Klicken Sie auf **Abfrage ausführen**. Ihre Ergebnisse werden in einer Tabelle angezeigt.

## Variablen {#variables}

Bevor Sie Ihren Bericht erstellen, gehen Sie auf den Tab **Variablen**, um Informationen für das Template des Berichts-Builders bereitzustellen, einschließlich der erforderlichen Variablen, die je nach Bericht variieren werden. 

![][11]

Die Variablen umfassen:

- **Kampagne oder Canvas:** Sie können eine oder mehrere Kampagnen oder Canvase einbeziehen (es gibt kein Maximum für die Anzahl der Kampagnen oder Canvase, die Sie angeben können). Wenn Sie keine Kampagnen oder Canvase angeben, enthält der Bericht alle Kampagnen oder Canvase aus dem von Ihnen gewählten Zeitrahmen.
- **Variante:** Wenn Sie eine Vorlage verwenden, die eine Untergliederung nach Varianten bietet, können Sie nach der Auswahl einer Kampagne oder eines Canvas Varianten aus dieser Kampagne oder diesem Canvas auswählen. Wenn Sie mehrere Varianten auswählen, werden Ihre Ergebnisse nach Varianten gruppiert.
- **Schritt:** Wenn Sie eine Canvas-Variante wählen, können Sie einen Canvas-Schritt auswählen. Sie können keinen Schritt auswählen, ohne vorher eine Canvas-Variante zu wählen. 
- **Zeitspanne:** Bestimmen Sie den Zeitraum, aus dem Sie Daten abrufen möchten. Wenn Sie keine Zeitspanne angeben, werden standardmäßig die letzten 30 Tage angezeigt.
- **Produktname:** Wenn Sie einen Bericht für Einkaufsdaten erstellen, können Sie ein bestimmtes Produkt auswählen, für das Sie Daten abrufen möchten.
- **Konversion-Fenster:** Immer erforderlich für Berichte mit Umsatz- und Kaufdaten. Die Anzahl der Tage nach dem E-Mail-Empfang oder Klick, die Braze den Käufen oder Umsätzen zuordnen soll.
- **Segmente:** Identifizieren Sie die Segmente, nach denen Sie die Daten aufschlüsseln möchten. Wenn Sie nichts angeben, wird der Bericht für alle Segmente ausgeführt, für die die Analysefunktion aktiviert ist.
- **Tags:** Geben Sie Tags in **Variablen** an, um Ihren Bericht für alle Kampagnen oder Canvase mit bestimmten Tags auszuführen. Sie können mehrere Tags einfügen. Wenn Sie sowohl Tags als auch bestimmte Kampagnen oder Canvase zu einem Bericht hinzufügen, wird Ihr Bericht Daten aus Ihren Tags und den angegebenen Kampagnen oder Canvase enthalten. 

## Verfügbarkeit der Daten

Es sind Daten für Zeiträume verfügbar, in denen beide Bedingungen erfüllt sind:

1. Das [Analytics Tracking für Segmente]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/) ist für die Segmente aktiviert, für die Sie Daten sehen möchten.
2. Die Funktion Leistungsdaten nach Segment ist aktiviert. Während der Early-Access-Phase werden wir diese Funktion schrittweise an unsere Kund:innen weitergeben. 

Sie können nicht auf Daten aus Zeiträumen zugreifen, die vor dem Zeitpunkt liegen, an dem diese Funktion für Ihr Unternehmen aktiviert wurde. Wenn beispielsweise das Analyse-Tracking für Segment A am 1\. Oktober aktiviert ist und diese Funktion für Ihr Unternehmen am 2\. Oktober eingeschaltet wird, können Sie die Daten für Segment A nur für die Kampagnen und Canvases sehen, die nach dem 2\. Oktober Metriken aufgezeichnet haben. 

Wenn Ihr Unternehmen diese Funktion am 2\. Oktober aktiviert hat und das Analytics-Tracking für Segment B am 3\. Oktober eingeschaltet hat, können Sie die Daten für Segment B nur für die Kampagnen und Canvase sehen, die nach dem 3\. Oktober aufgezeichnet wurden.


[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[11]:{% image_buster /assets/img_archive/variables_panel.png %}