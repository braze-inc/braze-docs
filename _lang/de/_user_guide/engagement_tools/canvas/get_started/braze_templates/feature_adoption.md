---
nav_title: Übernahme von Features
article_title: Übernahme von Features
page_order: 3
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze Canvas-Vorlage verwenden können, um rechtzeitig personalisierte Nachrichten zu versenden, die die Vorteile und Nutzungstipps hervorheben."
tool: Canvas
---

# Übernahme von Features

> Diese Vorlage wurde entwickelt, um die Nutzung Ihrer neuen Funktionen, bestehenden Produkte, zusätzlichen Angebote oder jedes anderen Bereichs, den Sie Ihren Kunden näher bringen möchten, zu fördern. Durch den Einsatz personalisierter Kommunikation und strukturierter Nachrichten können Sie den Nutzern nahtlos neue Funktionen vorstellen und wertvolles Feedback von ihnen erhalten. 

In diesem Artikel führen wir Sie durch einen Anwendungsfall für die Vorlage **Feature Adoption**, die für die Phasen der Benutzerbindung und -loyalität im Lebenszyklus gedacht ist. Nach diesem Artikel werden Sie eine Customer Journey angepasst haben, die Nutzer:innen zur Nutzung neuer Features anregt und die Stimmung der Nutzer:innen erfasst.

## Voraussetzungen

Um diese Vorlage erfolgreich zu verwenden, müssen Sie ein [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) erstellen, das darauf verweist, wenn Benutzer die Funktion verwendet haben.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, Sie arbeiten bei Calorie Rocket, einer App für Essenslieferungen, die vor kurzem Cruise Control eingeführt hat, eine Funktion zur Planung von wiederkehrenden Essenslieferungen, und Sie möchten mehr Nutzer dazu ermutigen, diese neue Funktion zu nutzen. In unserem Beispiel verwenden wir das angepasste Event `scheduled_delivery`, um zu verfolgen, wann Nutzer:innen das Feature Cruise Control ausprobiert haben.

Um auf die vorrätige Vorlage zuzugreifen, wählen Sie bei der Erstellung eines neuen Canvas die Option **Eine Canvas-Vorlage verwenden** > **Lötvorlagen**. Wählen Sie dann neben **Feature Adoption** die Option **Vorlage anwenden**. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

\![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen des Canvas, um anzugeben, dass das Canvas für das Targeting von Nutzer:innen gedacht ist, um deren Feedback zu sammeln.
3\. Aktualisieren Sie die Beschreibung, um klarzustellen, dass das Canvas dazu dient, Benutzer zu ermutigen, Feedback zu übermitteln und die Stimmung der Benutzer für die neue Funktion Tempomat zu verfolgen.
4\. Fügen Sie den Tag **Feature-Übernahme** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

\![Der neue Name und die Beschreibung für das Canvas. In der neuen Beschreibung heißt es: A feature adoption Canvas to track adoption and user sentiment for Cruise Control, a feature for scheduling recurring food deliveries.']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Schritt 2: Konversions-Event zuweisen

Als nächstes fügen wir ein Konversions-Event für unser Canvas hinzu, um die Übernahme eines Features zu signalisieren. Dies ist zulässig, damit wir den Experimentffad in unserer Nutzer:innen später anpassen können.

1. Wählen Sie unter **Konvertierungsereignisse zuweisen** die Option **Konvertierungsereignis hinzufügen**.
2. Wählen Sie unter **Primäres Konvertierungsereignis - A** die Option **Benutzerdefiniertes Ereignis durchführen** als **Ereignistyp Konvertierung**.
3. Wählen Sie unser angepasstes Event `scheduled_delivery` aus.
4. Wir werden die Frist für die Umstellung auf drei Tage festsetzen.

\![Das Konversions-Event-Fenster im Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Schritt 3: Entry-Zeitplan anpassen

Unser Ziel ist es, unsere Nutzer zu ermutigen, den Tempomat zu übernehmen, aber wir möchten nicht, dass unsere Nachrichten zu häufig erscheinen. Wir behalten diese Leinwand also als geplante Lieferung bei und nehmen die folgenden Anpassungen im Abschnitt **Zeitabhängige Optionen** vor.

1. Aktualisieren Sie die **Eintragsfrequenz** auf **Wöchentlich**.
2. Behalten Sie die Wiederholung so bei, wie sie ist.
3. Wählen Sie **Mo**, um Nutzer am Anfang der Woche anzusprechen.
4. Wählen Sie die Startzeit für unser Canvas.
5. Aktualisieren Sie die **Beendigungsparameter**, um das Canvas am letzten Tag des Jahres zu beenden.

Wir werden die Option beibehalten, die es Nutzern:innen erlaubt, den Canvas in ihrer Ortszeit einzugeben.

### Schritt 4: Zielgruppe auswählen

Lassen Sie uns nun unsere Zielgruppe einrichten, indem wir die folgenden Details in der Template aktualisieren:

1. Wählen Sie das Segment **Alle Benutzer**.
2. Entfernen Sie die zusätzlichen Filter der Vorlage. 
3. Erstellen Sie diesen Filter mit unserem benutzerdefinierten Ereignis: `Has scheduled_delivery for exactly 0 times`. Dies erlaubt es uns, Nutzer:innen, die das Feature bereits verwendet haben, vom Zugang zu unserem Canvas auszuschließen.

\![Das Segment für alle Nutzer:innen, die den Tempomat nicht benutzt haben.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Da Calorie Rocket zuvor einigen Benutzern erlaubt hat, die neue Funktion Cruise Control zu testen, werden wir die Ausstiegskriterien aktualisieren, um diese Benutzer von der Teilnahme am Canvas auszuschließen.

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standardeinstellungen für Abonnements bei, d.h. wir senden nur an Benutzer, die Nachrichten oder Benachrichtigungen abonniert oder sich dafür entschieden haben, und überspringen die anderen Einstellungen (Häufigkeitsbegrenzung, ruhige Stunden und Seed-Gruppen).

### Schritt 6: Canvas anpassen

#### Aktionspfad weiterentwickeln

Als Nächstes erstellen wir den ersten Aktions-Pfad, der anzeigen soll, ob unsere Nutzer:innen Interesse an dem neuen Feature haben. Wir werden die folgenden Anpassungen an der Vorlage vornehmen:

1. Da die Funktion Cruise Control erst verfügbar ist, nachdem eine Bestellung in den Warenkorb gelegt wurde, nennen wir die erste Aktionsgruppe **In den Warenkorb gelegt** und wählen `added_to_cart` für das benutzerdefinierte Ereignis.

\![Der Name der Aktionsgruppe wurde auf "In den Warenkorb gelegt" und das "Angepasste Event durchführen" auf "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Behalten Sie die zweite App-Gruppe **Taken Tour** bei, da wir auswerten möchten, ob Nutzer:innen eine Tour durch die App gemacht haben. Wenn ja, werden sie zum zweiten Aktions-Pfad vorgebracht.
3\. Für den nachfolgenden Aktionspfad mit dem Namen **Nutzung bewerten** ersetzen Sie **Genutzte Funktion >3x** durch **Gesehene Tempomateinstellungen**.
4\. Wählen Sie das Dropdown-Menü **Angepasstes Event durchführen** und dann `scheduled_delivery` für das angepasste Event aus.

\![Der Name der Aktionsgruppe wurde auf 'Verwendetes Feature >3x' und das Feld 'Angepasstes Event durchführen' auf 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Feedback-Umfrage einrichten

Als Nächstes gehen wir zum Schritt Nachricht mit dem Namen **Feedback-Umfrage**, um unsere Feedback-Umfrage einzufügen, die unsere Benutzer ausfüllen können, nachdem sie Cruise Control zum ersten Mal verwendet haben. Unsere Umfrage-Antwortmöglichkeiten für unsere Nutzer:innen sind:

- **Ich habe es geliebt!**
- **Nicht für mich.**

1. Für die beiden Umfragen wählen Sie **Experience Feedback** als angepasstes Attribut aus, um Feedback zu Cruise Control zu erfassen und zu tracken. Dieses benutzerdefinierte Attribut hat zwei Werte, die die Umfrageantworten darstellen (`good` und `bad`).
2. Aktualisieren Sie die Attributwerte, damit sie mit den Umfrageoptionen übereinstimmen. So können wir die Reaktion eines Nutzers:innen tracken.

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Canvas starten**, um das Canvas zu starten. Jetzt können wir Nutzer mit einer personalisierten User Journey ansprechen, um sie zu ermutigen, unsere neue Funktion Cruise Control zu nutzen.

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}
