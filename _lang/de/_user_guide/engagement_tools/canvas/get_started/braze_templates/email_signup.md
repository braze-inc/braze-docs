---
nav_title: E-Mail Registrierung mit doppeltem Opt-in
article_title: E-Mail Registrierung mit Double Opt-in
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze-Canvas-Vorlage verwenden können, um Ihre Reichweite mit überprüften E-Mail Registrierungen zu vergrößern."
tool: Canvas
---

# E-Mail Registrierung mit doppeltem Opt-in

> Verwenden Sie das Template für die E-Mail-Registrierung mit doppeltem Opt-in, um Ihre Reichweite mit überprüften E-Mail-Registrierungen zu vergrößern. Targeting neuer Nutzer:innen, um ihre E-Mail zu erfassen, ihr Abo zu bestätigen und einen Aktionscode zu erhalten - alles in einem einzigen, nahtlosen Prozess.

Dieser Artikel zeigt Ihnen einen Anwendungsfall für das Template **E-Mail Registrierung mit Double Opt-in**, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus gedacht ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das E-Mails und In-App-Nachrichten an Nutzer:innen sendet, wenn sie eine Sitzung beginnen oder wenn sie ihr Onboarding noch nicht abgeschlossen haben.

## Voraussetzungen

Um diese Vorlage erfolgreich zu verwenden, benötigen Sie Folgendes:

- Eine [mehrseitige In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) mit einer Seite, um die E-Mails Ihrer Nutzer:innen zu erfassen, und einer weiteren, um eine Erfolgsmeldung zu übermitteln. 
- Eine E-Mail zur Bestätigung der Nutzer:innen, um ihre E-Mail-Adresse zu überprüfen.
- Eine Willkommens-E-Mail mit einem exklusiven Aktionscode für Nutzer:innen, die ein Double Opt-in durchführen.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, Sie arbeiten für Steppington, eine Gesundheits-App, die für ihre Features wie Kalorien-Tracking, digitale Trainingskurse und Flashmob-Marathons bekannt ist. Bevor Sie das Canvas erstellen, [richten Sie mehrseitige In-App- und In-Browser-Nachrichten ein]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), die eine Reihe von engagierten Fragen enthalten, um die Erfahrungen und Eindrücke eines Nutzers:innen bei seiner ersten Fahrt mit der App zu ermitteln.

Um auf die Vorlage zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **E-Mail-Registrierung mit doppeltem Opt-in** das **Template anwenden** aus. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen Sie die Details im Canvas an Ihr Ziel an.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen bei der ersten Verwendung der App gedacht ist.
3\. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisierte Nachrichten für Nutzer:innen enthält, die ein Double-Opt-in durchführen möchten.
4\. Fügen Sie das Tag **E-Mail** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Schritt 2: Konversions-Events zuweisen

Als nächstes weisen Sie unsere Konversions-Events zu. Konversions-Events sind eine Art von Metrik, mit der Sie den Erfolg des Canvas messen können. Für den **Ereignistyp Konversion** wählen Sie **Angepasstes Event durchführen**. Wählen Sie dann **email_opt_in** für den **Namen des angepassten Events**.

!["Konversions-Ereignisse zuweisen" für den Konversions-Ereignistyp des Opt-in für E-Mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Behalten Sie die Frist für die Konversion des Templates von drei Tagen bei, da Sie Ihre jüngsten Nutzer:innen targetieren möchten.

### Schritt 3: Entry-Zeitplan anpassen

Halten Sie den Zeitplan für den Eingang als **aktionsbasiert**, damit Nutzer:innen Ihr Canvas betreten, wenn sie eine Sitzung in der App beginnen. Auf diese Weise können Sie beginnen, Ihre Beziehungen mit rechtzeitigem Engagement aufzubauen.

Ziehen Sie außerdem in Erwägung, die **aktionsbasierten Optionen** unverändert beizubehalten, damit Nutzer:innen den Canvas nur dann betreten, wenn sie eine Sitzung beginnen.

![Ein aktionsbasierter Zeitplan für den Eingang von Nutzer:innen, die eine beliebige Sitzung beginnen, in den Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Aktualisieren Sie für das **Eingangsfenster** die **Startzeit (erforderlich)** auf das gewünschte Datum und die Uhrzeit.

![Ein Eingabefenster mit der Startzeit 16\. Januar 2025 um 12:30 Uhr. Nutzer:innen werden diese Nachricht in ihrer Ortszeit eingeben.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Schritt 4: Wählen Sie die Zielgruppe aus

Definieren Sie Ihre Zielgruppe als Nutzer:innen von Steppington, die keine E-Mail Adresse in ihrem Nutzerprofil haben, indem Sie den Standard Filter für die Segmentierung des Templates `Email Available is false` beibehalten.

![Eingang Zielgruppe mit dem Filter "E-Mail verfügbar ist falsch".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Behalten Sie die Standard Abo-Einstellungen bei, so dass Sie nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert oder sich dafür entschieden haben, und überspringen Sie die anderen Einstellungen (Frequency-Capping, Ruhezeiten und Seed-Gruppen).

![Standard-Sendeoptionen, um nur an Nutzer:innen zu senden, die Abonnent:in sind oder ein Opt-in haben.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Schritt 6: Canvas anpassen

Als nächstes erstellen Sie das Canvas, indem Sie die Kanäle und Inhalte anpassen, die Sie an Nutzer:innen senden möchten. Da Sie sich auf das Überprüfen von E-Mail Registrierungen konzentrieren, müssen Sie keine der Canvas-Schritte und Kanäle des Templates hinzufügen oder entfernen.

1. Wählen Sie den ersten Schritt der Nachricht mit dem Namen **E-Mail-Registrierung**. Hier aktualisieren Sie das Template, um unsere mehrseitigen In-App- (und In-Browser-) Nachrichten zu verwenden.

- Seite 1 fängt die E-Mails ein.
- Auf Seite 2 wird eine Nachricht zur Bestätigung angezeigt.

![Zwei Seiten einer In-App-Nachricht, um die E-Mails der Nutzer:innen zu erfassen und eine Erfolgsmeldung anzuzeigen.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. Behalten Sie ab hier den Schritt **Abonnent**:in Aktions-Pfad bei. Bei diesem Schritt werden unsere Nutzer:innen innerhalb eines Tagesfensters in zwei Gruppen aufgeteilt:

- Nutzer:innen, die Steppington mit ihrer E-Mail abonniert haben
- Nutzer:innen, die Steppington nicht mit ihrer E-Mail abonniert haben

{:start="3"}
3\. Als Nächstes ersetzen Sie die E-Mail durch unsere gebrandete Bestätigungs-E-Mail für den Schritt **E-Mail** Nachricht **überprüfen**. Dies sendet eine E-Mail an unsere abonnierten Nutzer:in und fordert sie auf, ihre E-Mail-Adresse zu bestätigen und sich für unser Messaging zu registrieren.
4\. Behalten Sie den Schritt Aktions-Pfad für **das Abo bestätigen** unverändert bei. Bei diesem Schritt werden unsere Nutzer:innen in diejenigen unterteilt, die ihre E-Mail bestätigt haben, und in diejenigen, die dies nicht getan haben, mit einem Zeitfenster von einer Woche.
5\. Zum Schluss aktualisieren Sie den Schritt **Willkommen + Rabattnachricht** mit unserer E-Mail zur Bestätigung, die einen exklusiven Aktionscode enthält.

{% alert note %}
Der Schritt **E-Mail** Nachricht **überprüfen** wird bei der zweiten Sitzung des Nutzers:innen ausgelöst. Der Grund dafür ist, dass das erste Sitzungsstart-Ereignis das Canvas triggern würde, aber ein zweiter Sitzungsstart, nachdem der Nutzer:innen den ersten **E-Mail-Anmeldeschritt** erreicht hat, ist erforderlich, damit der Nutzer:innen die zweite In-App-Nachricht triggern kann.
{% endalert %}

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem Sie Ihr Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten Sie es, indem Sie **Canvas starten** auswählen.

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}
