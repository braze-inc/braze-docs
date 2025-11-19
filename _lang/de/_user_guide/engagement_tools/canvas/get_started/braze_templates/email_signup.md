---
nav_title: E-Mail Registrierung mit doppeltem Opt-in
article_title: E-Mail Registrierung mit Double Opt-in
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze-Canvas-Vorlage verwenden können, um Ihre Reichweite mit überprüften E-Mail-Registrierungen zu vergrößern."
tool: Canvas
---

# E-Mail Registrierung mit doppeltem Opt-in

> Verwenden Sie das Template für die E-Mail-Registrierung mit doppeltem Opt-in, um Ihre Reichweite mit überprüften E-Mail-Registrierungen zu vergrößern. Targeting neuer Nutzer:innen, um ihre E-Mail zu erfassen, ihr Abo zu bestätigen und einen Aktionscode zu erhalten - alles in einem einzigen, nahtlosen Prozess.

Dieser Artikel zeigt Ihnen einen Anwendungsfall für das Template **E-Mail Registrierung mit Double Opt-in**, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus gedacht ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das E-Mails und In-App-Nachrichten an Nutzer:innen sendet, wenn sie eine Sitzung beginnen oder wenn sie ihr Onboarding noch nicht abgeschlossen haben.

## Voraussetzungen

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Eine [mehrseitige In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) mit einer Seite, um die E-Mails Ihrer Nutzer:innen zu erfassen, und einer weiteren, um eine Erfolgsmeldung zu übermitteln.
- Eine E-Mail zur Bestätigung der Nutzer:innen, um ihre E-Mail-Adresse zu überprüfen.
- Eine Willkommens-E-Mail mit einem exklusiven Aktionscode für Nutzer:innen, die ein Double Opt-in durchführen.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten für Steppington, eine Gesundheits-App, die für ihre Features wie Kalorien-Tracking, digitale Trainingskurse und Flashmob-Marathons bekannt ist. Vor der Erstellung des Canvas haben wir [mehrseitige In-App- und In-Browser-Nachrichten erstellt]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), die eine Reihe von engagierten Fragen enthalten, um die Erfahrungen und Impressionen eines Nutzers:innen bei seiner ersten Fahrt mit der App zu ermitteln.

Um auf die Vorlage zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **E-Mail-Registrierung mit doppeltem Opt-in** das **Template anwenden** aus. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen bei der ersten Verwendung der App gedacht ist.
3\. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisierte Nachrichten für Nutzer:innen zum doppelten Opt-in enthält.
4\. Fügen Sie das Tag **E-Mail** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Schritt 2: Konversions-Events zuweisen

Lassen Sie uns nun unsere Konversions-Events zuweisen. Konversions-Events sind eine Art Metrik, mit der Sie den Erfolg des Canvas messen können. Für den **Ereignistyp Konversion** wählen Sie **Angepasstes Event durchführen**. Wählen Sie dann **email_opt_in** für den **Namen des angepassten Events**.

!["Konversions-Events zuweisen" für den Konversions-Event-Typ des Opt-in für E-Mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Wir behalten die Frist für die Konversion des Templates von drei Tagen bei, da wir unsere jüngsten Nutzer:innen ansprechen wollen.

### Schritt 3: Entry-Zeitplan anpassen

Behalten wir den Zeitplan für den Eingang als **aktionsbasiert** bei, damit die Nutzer:innen unser Canvas betreten, wenn sie eine Sitzung in der App starten. Auf diese Weise können wir beginnen, unsere Beziehungen mit rechtzeitigem Engagement aufzubauen.

Wir werden auch die **aktionsbasierten Optionen** beibehalten, so dass Nutzer:innen den Canvas nur betreten, wenn sie eine Sitzung starten.

![Ein aktionsbasierter Zeitplan für den Eingang von Nutzer:innen, die eine beliebige Sitzung beginnen, in den Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Für das **Fenster Eingang** aktualisieren wir die **Startzeit (erforderlich)** auf das gewünschte Datum und die Uhrzeit.

![Ein Eingangsfenster mit der Startzeit 16\. Januar 2025 um 12:30 Uhr. Nutzer:innen werden diese Nachricht in ihrer Ortszeit eingeben.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Schritt 4: Wählen Sie die Zielgruppe aus

Wir definieren unsere Zielgruppe als Nutzer:innen von Steppington, die keine E-Mail Adresse in ihrem Nutzerprofil haben. Dazu behalten wir den Standard Filter für die Segmentierung des Templates `Email Available is false` bei.

![Eingang Zielgruppe mit dem Filter "E-Mail verfügbar ist falsch".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standardeinstellungen für Abonnements bei, d.h. wir senden nur an Benutzer, die Nachrichten oder Benachrichtigungen abonniert oder sich dafür entschieden haben, und überspringen die anderen Einstellungen (Häufigkeitsbegrenzung, ruhige Stunden und Seed-Gruppen).

![Standard-Sendeoptionen, um nur an Nutzer:in zu senden, die ein Abonnent:in sind oder ein Opt-in haben.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Schritt 6: Canvas anpassen

Jetzt bauen wir unser Canvas auf, indem wir die Kanäle und Inhalte anpassen, die an die Nutzer:innen gesendet werden sollen. Da wir uns auf das Überprüfen unserer E-Mail Registrierungen konzentrieren, müssen wir keine der Canvas-Schritte und Kanäle des Templates hinzufügen oder entfernen.

1. Wählen Sie den ersten Schritt der Nachricht mit dem Namen **E-Mail-Registrierung**. Hier werden wir das Template aktualisieren, um unsere mehrseitige In-App-Nachricht (und In-Browser-Nachricht) zu verwenden.

- Seite 1 wird die E-Mails erfassen.
- Auf Seite 2 wird eine Nachricht zur Bestätigung angezeigt.

![Zwei Seiten einer In-App-Nachricht, um die E-Mails der Nutzer:innen zu erfassen und eine Erfolgsmeldung anzuzeigen.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. Ab hier behalten wir den Schritt **Abonnent**:in Aktions-Pfad unverändert bei. Bei diesem Schritt werden unsere Nutzer:innen innerhalb eines Tagesfensters in zwei Gruppen aufgeteilt:

- Nutzer:innen, die Steppington mit ihrer E-Mail abonniert haben
- Nutzer:innen, die Steppington nicht mit ihrer E-Mail abonniert haben

{:start="3"}
3\. Als Nächstes ersetzen Sie die E-Mail durch unsere gebrandete Bestätigungs-E-Mail für den Schritt **E-Mail** Nachricht **überprüfen**. Dies sendet eine E-Mail an unsere abonnierten Nutzer:innen und fordert sie auf, ihre E-Mail-Adresse zu bestätigen und sich für unser Messaging anzumelden.
4\. Behalten Sie den Schritt Aktions-Pfad für **das Abo bestätigen** unverändert bei. Bei diesem Schritt werden unsere Nutzer:innen in diejenigen unterteilt, die ihre E-Mail bestätigt haben, und in diejenigen, die dies nicht getan haben, mit einem Zeitfenster von einer Woche.
5\. Zum Schluss aktualisieren Sie den Schritt **Willkommen + Rabattnachricht** mit unserer E-Mail zur Bestätigung, die einen exklusiven Aktionscode enthält.  

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Canvas starten** auswählen.

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}