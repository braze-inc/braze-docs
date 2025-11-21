---
nav_title: Segmente Daten
article_title: Anzeigen und Verstehen von Segmenten Daten
page_order: 4
page_type: reference
description: "Diese Seite erklärt den Abschnitt Segmente Ihres Braze-Dashboards und enthält eine Zusammenfassung der bereitgestellten Statistiken."
alias: /viewing_and_understanding_segment_data/
tool: 
  - Segments
  - Reports
  
---
# Segmente Daten

> Diese Seite erklärt den Abschnitt Segmente Ihres Braze-Dashboards und enthält eine Zusammenfassung der bereitgestellten Statistiken.

## Zugriff auf Daten über Ihre Segmente und Zugehörigkeit

Die Seite **Segmente** Ihres Braze-Dashboards enthält eine Zusammenfassung aller Ihrer Segmente und erlaubt es Ihnen, detaillierte Daten für jedes einzelne Segment zu prüfen. Suchen Sie auf dieser Seite nach einem Segment und wählen Sie den Namen des Segments aus, um dessen Daten zu bearbeiten und anzuzeigen. Wie Sie ein Segment erstellen können, erfahren Sie unter [Erstellen eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment).

![Segmente Seite]({% image_buster /assets/img_archive/segments.png %})

Nachdem Sie den Namen eines Segments ausgewählt haben, können Sie Segmentstatistiken und Filter anzeigen und das Segment bearbeiten, indem Sie Filter hinzufügen oder löschen. Achten Sie darauf, alle Änderungen zu speichern!

Wenn Sie das [Analytics Tracking für ein Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) einschalten, können Sie Sitzungen, angepasste Events und Umsätze im Zeitverlauf für dieses Segment einsehen.

![Analytics Tracking für ein Segment umschalten]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Segmente Statistik

Sie können die folgenden Segmentstatistiken einsehen, die in Realtime aktualisiert werden, wenn Sie Filter hinzufügen oder löschen:

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
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Aufgrund von <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">Spam-Bestimmungen</a> ist es eine gute Idee, Ihre Nutzer:in explizit zum Opt-in aufzufordern, indem Sie eine Richtlinie zum doppelten Opt-in einführen, bei der die Nutzer:innen auf einen Link in einer ersten Bestätigungs-E-Mail klicken müssen. Um mehr Nutzer:innen zum Opt-in zu bewegen, können Sie eine Nachricht an <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">diejenigen</a> richten, <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">die weder Opt-in noch Opt-out gewählt haben</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push Enablement (Opt-in)</td>
            <td class="no-split">„Push aktiviert“ bezieht sich auf die Anzahl der Nutzer:innen mit mindestens einem Push-Token. Einige Nutzer:innen haben möglicherweise mehrere Push-Token (z.B. wenn sie ein iPhone und ein iPad besitzen), so dass die Anzahl der Push-Benachrichtigungen, die Sie an dieses Segment senden, größer sein kann als die Anzahl der Nutzer:innen, die "Push enabled" sind. "Opt-in" referenziert die Anzahl der Nutzer:in, die sich ausdrücklich für Push-Benachrichtigungen entschieden haben. Nutzer:innen müssen immer explizit ihr Opt-in geben, damit Sie ihnen Push-Nachrichten senden können.</td>
        </tr>
    </tbody>
</table>

### Segment-Insights

Auf der Seite [Segment-Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) in Ihrem Dashboard können Sie sehen, wie die Performance eines Segments im Vergleich zu einem anderen Segment bei einer Reihe von vordefinierten KPIs ist.

### Messaging-Nutzung
Der Abschnitt **Messaging-Nutzung** zeigt, welche Segmente, derzeit aktivierten Kampagnen und derzeit aktivierten Canvase auf Ihr Segment abzielen.

### Historische Mitgliedschaft

Der Abschnitt **Historische Mitgliedschaft** zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.

Wenn Sie mehr über die Überwachung der Mitgliedschaft und Größe Ihres Segments erfahren möchten, referenzieren Sie auf [Messung der Segmentgröße]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

### Nutzervorschau

Um detaillierte, benutzerspezifische Informationen über Ihre Segmente anzuzeigen, klicken Sie auf **Nutzerdaten** und wählen Sie **Nutzer:innen Vorschau**.

Auf dieser Seite können Sie eine Reihe von angepassten Attributen einsehen, z. B. Geschlecht, Alter, Anzahl der Sitzungen und ob der oder die Nutzer:in sich für Push und E-Mail entschieden hat.

Beachten Sie, dass es in Fällen, in denen Ihr Segment im Verhältnis zur Größe Ihres Workspace sehr klein ist, möglich ist, dass die Vorschau keine Nutzer:innen anzeigt. Dies bedeutet nicht zwangsläufig, dass sich in Ihrem Segment keine Nutzer:innen befinden. Führen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) aus, um die genaue Größe Ihres Segments zu ermitteln.

![Nutzer:in Vorschau]({% image_buster /assets/img_archive/user_preview.png %})

## Anzeigen von Performance-Daten nach Segmenten

Verwenden Sie die [Berichts-Builder-Templates des Query Builders]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/), um die Performance-Metriken für Kampagnen, Canvas, Varianten und Segmente aufzuschlüsseln.

## Erstellen eines Berichts zur Segmentaufschlüsselung mit dem Abfrage-Builder

Um einen Bericht aus einer [Query Builder-Vorlage]({{site.baseurl}}/user_guide/analytics/query_builder/) zu erstellen, gehen Sie zu **Query Builder** und gehen Sie wie folgt vor:

1. Wählen Sie **SQL-Abfrage erstellen** > **Abfrage-Template**.
2. Filtern Sie Templates für diejenigen, die Metriken mit „Segmentaufschlüsselungen“ haben.
3. Wählen Sie das Template aus, das Sie verwenden möchten.
4. Füllen Sie die Variablen in Ihrem SQL Template auf dem Tab [Variablen](#variables) aus.
5. (Optional) Bearbeiten Sie direkt die SQL in der Vorlage.
6. Wählen Sie **Abfrage ausführen**. Ihre Ergebnisse werden in einer Tabelle angezeigt.

## Variablen {#variables}

Bevor Sie Ihren Bericht erstellen, gehen Sie auf den Tab **Variablen**, um Informationen für das Template des Berichts-Builders bereitzustellen, einschließlich der erforderlichen Variablen, die je nach Bericht variieren werden. 

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

1. Das [Analytics Tracking für Segmente]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) ist für die Segmente aktiviert, für die Sie Daten sehen möchten.
2. Das Feature Performance-Daten nach Segmenten ist eingeschaltet.

Sie können nicht auf Daten aus Zeiträumen zugreifen, die vor dem Zeitpunkt liegen, an dem dieses Feature für Ihr Unternehmen aktiviert wurde. Wenn beispielsweise das Analytics Tracking für Segment A am 1\. Oktober eingeschaltet ist und dieses Feature für Ihr Unternehmen am 2\. Oktober aktiviert wird, dann können Sie nur Daten für Segment A für die Kampagnen und Canvase einsehen, die nach dem 2\. Oktober Metriken aufgezeichnet haben. 

Wenn Ihr Unternehmen diese Funktion am 2\. Oktober aktiviert hat und das Analytics-Tracking für Segment B am 3\. Oktober eingeschaltet hat, können Sie die Daten für Segment B nur für die Kampagnen und Canvase sehen, die nach dem 3\. Oktober aufgezeichnet wurden.


