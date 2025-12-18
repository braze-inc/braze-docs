---
nav_title: "Passive Nutzer:innen"
article_title: "Passive Nutzer:innen"
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze-Canvas-Template verwenden, um Nutzer:innen mit Anreizen auf der Grundlage ihres früheren Engagements zu Ihrer App zurückzubringen."
tool: Canvas
---

# Passive Nutzer:innen

> Verwenden Sie die Vorlage für abgelaufene Nutzer, um sie an den Wert zu erinnern, den Ihre Marke für sie hat, und ermutigen Sie sie mit interessanten Angeboten und Anreizen, die auf ihren früheren Engagements basieren, zur Rückkehr.

Dieser Artikel führt Sie durch einen Anwendungsfall für die Vorlage **Lapsed User**, die für die Phase der Benutzerbindung und -loyalität im Lebenszyklus eines Benutzers konzipiert ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das die Benutzer mit Werbeaktionen, die sich nach ihrem Verhalten richten, dazu anregt, zu Ihrer App zurückzukehren, z. B. ob sie nach dem Erhalt einer Werbebotschaft eine Sitzung in Ihrer App begonnen haben.

## Voraussetzungen

Um die Vorlage für abgelaufene Benutzer erfolgreich zu nutzen, müssen Sie [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) mit den von Ihnen verwendeten Partnern und Zielgruppen konfigurieren.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten für MovieCanon, einen Streaming-Dienst, der exklusive Inhalte für Filme und Serien anbietet. Wir können die Vorlage für abgelaufene Benutzer verwenden, um Vergünstigungen und Premium-Inhalte für Benutzer zu bewerben, die unsere App seit 30 Tagen nicht mehr besucht haben.

Bevor wir das Canvas erstellen, richten wir die [Braze Audience Sync to Google-Integration]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) ein, damit wir Nutzerdaten von Braze zu Google Audiences hinzufügen können, um Werbung auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu senden.

Um auf die Vorlage für verfallende Benutzer zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas die Option **Eine Canvas-Vorlage verwenden** > **Lötvorlagen**. Wählen Sie dann neben **Lapsing User** die Option **Vorlage anwenden**. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten 

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen des Canvas, um festzulegen, dass dieser Canvas Benutzer mit Werbeaktionen benachrichtigt und eine Synchronisierung der Zielgruppe für diejenigen vornimmt, die eine Sitzung beginnen.
3\. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieser Canvas Vergünstigungen und Aktionen enthält.
4\. Fügen Sie das Tag **Passivität/Bindung** hinzu, damit wir auf der Canvas-Startseite nach diesem Canvas filtern können.

!["Canvas-Details einrichten"-Schritt mit dem Canvas-Namen "Verfallene Nutzer:innen - App besuchen" und einer kurzen Canvas-Beschreibung]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Schritt 2: Konversions-Events zuweisen

Aktualisieren Sie das **primäre Konversions-Event - A**, um Nutzer:innen aus unserer App (MovieCanon) zusammenzustellen, und belassen Sie das **primäre Konversions-Event - B** als Standard, wenn Sie einen Kauf tätigen.

!["Konversions-Events zuweisen" mit einem primären Konversions-Event eines Nutzers:in, der eine Sitzung in einer bestimmten App beginnt.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Schritt 3: Entry-Zeitplan anpassen

Behalten wir den Entry-Zeitplan als **Geplant** und die standardmäßigen zeitbasierten Optionen beibehalten, damit Canvas täglich nach passiven Nutzer:innen sucht.

In diesem Schritt nehmen wir zwei Anpassungen vor: 

1. Wählen Sie ein Startdatum und eine Startzeit aus.
2. Wählen Sie die Endparameter **An einem bestimmten Datum** und ein Datum in zwei Monaten. Nehmen wir an, wir haben einen weiteren passiven Nutzer-Canvas, den wir nach diesem starten möchten.

!["Eingang Zeitplan"-Schritt für einen geplanten Canvas, der Nutzer:innen zu einer bestimmten Zeit einlässt.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Schritt 4: Zielgruppe auswählen

Wir behalten die Standardeinstellungen für das Einstiegspublikum bei, das auf Benutzer eingestellt ist, die unsere App seit mehr als 30 Tagen nicht mehr verwendet haben. Wir behalten auch die Standard-Entry-Kontrollen bei, sodass Nutzer:innen den Canvas nach vier Wochen erneut aufrufen können. Das bedeutet, dass jedes Mal, wenn ein Benutzer unsere App mehr als 30 Tage lang nicht besucht hat, er in den Canvas aufgenommen wird.

!["Zielgruppe" Schritt Targeting der Nutzer:innen, die die Apps zuletzt vor 30 Tagen genutzt haben.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die meisten Standardeinstellungen für Abonnements bei:

- Senden Sie nur an Benutzer, die sich für den Empfang von Nachrichten oder Benachrichtigungen angemeldet oder entschieden haben.
- Wenden Sie unsere [Regeln für die Begrenzung der Häufigkeit an]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping), damit wir unser Publikum nicht mit der Anzahl der Nachrichten überfordern, die es erhält. In diesem Fall haben wir unser Frequency-Capping so eingestellt, dass die Anzahl der Kampagnen oder Canvas-Schritte mit dem Tag „Passivität/Bindung“, die ein:e Nutzer:in erhalten kann, auf zwei pro Woche begrenzt ist.
- Senden Sie keine Nachrichten während der Ruhezeiten in der Ortszeit des Benutzers (12 bis 8 Uhr).

Die einzige Einstellung, die wir ändern werden, ist, was zu tun ist, wenn eine Nachricht während der Ruhezeiten ausgelöst wird. Anstatt die Nachricht abzubrechen, wählen Sie **Senden zum nächstmöglichen Zeitpunkt**, damit unsere Nutzer keine Werbeaktion verpassen.

!["Ruhezeiten"-Abschnitt mit einer Startzeit von 12 Uhr und einer Endzeit von 8 Uhr.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Schritt 6: Canvas anpassen

Jetzt bauen wir unser Canvas auf, indem wir die in der Vorlage enthaltenen Schritte anpassen:

1. Passen Sie die erste E-Mail an, die an alle Benutzer gesendet wird, die unsere App seit mehr als 30 Tagen nicht mehr besucht haben. Für unseren Anwendungsfall passen wir eine E-Mail an, die den Benutzern mitteilt, dass sie neue Vergünstigungen erhalten, wenn sie heute unsere App besuchen. 

![Canvas Nachrichten-Schritt für eine E-Mail, die Nutzer:innen darauf hinweist, neue Vergünstigungen freizuschalten, wenn sie heute kommen.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. Passen Sie die Aktionsffad-Komponente mit der Bezeichnung „Sitzung starten?“ an, indem Sie unsere App für den Pfad **Gestartete Sitzung** auswählen. 

![Aktions-Pfad für Sitzungen, die in einer bestimmten App gestartet werden.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. Behalten Sie die Standardeinstellung für den Decision-Split-Schritt mit dem Namen „Sitzungen?“ bei, die die Gruppe „>1 Sitzung“ als Nutzer:innen definiert, die unsere App am letzten Kalendertag mehr als einmal verwendet haben.
4\. Passen Sie den Nachrichtenschritt für Nutzer:innen an, die zur Gruppe „>1 Sitzung“ gehören. In unserem Anwendungsfall bedanken wir uns bei den Nutzern für den Besuch unserer App und heben die Vorteile hervor, die sie freigeschaltet haben.
5\. Stellen Sie sicher, dass unsere Google Audience-Synchronisierung im Schritt Ad Audience Update eingerichtet ist, damit wir die Nutzerdaten von Nutzern aktualisieren und synchronisieren, die nach Erhalt unserer ersten E-Mail mehrere Sitzungen hatten.
6\. Behalten Sie den Standard für die Komponente [Experimentpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) namens „A/B-Test“ bei. Dadurch wird zufällig eine von zwei Aktionen (die wir im nächsten Schritt anpassen) an Nutzer:innen gesendet, die weniger als zwei Sitzungen hatten.
7\. Passen Sie die beiden Aktionen an, die im Rahmen des Experimentpfads an Nutzer:innen gesendet werden. In unserem Anwendungsfall machen wir aus einem eine 20 %-Aktion für ein dreimonatiges Abo und aus dem anderen eine 10 %-Aktion für ein einmonatiges Abo.

![Canvas-Schritte mit Verzweigungspfaden basierend auf der Anzahl der Sitzungen eines Nutzer:innen.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Schritt 7: Testen und starten Sie den Canvas

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Canvas starten** wählen. Jetzt erhalten unsere Benutzer, die unsere App seit mehr als 30 Tagen nicht mehr besucht haben und unsere Nachrichtenkanäle abonniert haben, E-Mails, die sie zur Rückkehr ermutigen!

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}

