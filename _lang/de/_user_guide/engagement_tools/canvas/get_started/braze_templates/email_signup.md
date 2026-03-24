---
nav_title: E-Mail Registrierung mit doppeltem Opt-in
article_title: E-Mail Registrierung mit Double Opt-in
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie mithilfe eines Braze-Canvas-Templates Ihre Reichweite durch verifizierte Registrierungen mit E-Mails erweitern können."
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

Angenommen, Sie arbeiten für Steppington, eine Gesundheits-App, die für ihre Features wie Kalorien-Tracking, digitale Fitnesskurse und Flashmob-Marathons bekannt ist. Bevor Sie die Canvas erstellen, [richten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) Sie [mehrseitige In-App- und In-Browser-Nachrichten ein,]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) die eine Reihe von ansprechenden Fragen enthalten, um die Erfahrungen und Impressionen eines Nutzers bei seiner ersten Nutzung der App zu erfassen.

Um auf die Vorlage zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **E-Mail-Registrierung mit doppeltem Opt-in** das **Template anwenden** aus. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Adjust the Canvas-Details entsprechend Ihrem Ziel.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen bei der ersten Verwendung der App gedacht ist.
3\. Bitte aktualisieren Sie die Beschreibung, um zu erläutern, dass diese Canvas personalisierte Nachrichten für Nutzer:innen enthält, die ein Opt-in durchführen müssen.
4\. Fügen Sie das Tag **E-Mail** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und das Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Schritt 2: Konversions-Events zuweisen

Als nächstes weisen Sie unsere Konversions-Events zu. Konversions-Events sind eine Art von Metrik, mit der Sie den Erfolg von Canvas messen können. Für den **Ereignistyp Konversion** wählen Sie **Angepasstes Event durchführen**. Wählen Sie anschließend**email_opt_in** für das **angepasste Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event-Event**

![Abschnitt „Konversions-Events zuweisen“ für den Typ des Konversions-Events „Opt-in für E-Mails“.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Bitte beachten Sie die dreitägige Frist für die Konversion des Templates, da Sie Ihre neuesten Nutzer:innen ansprechen möchten.

### Schritt 3: Entry-Zeitplan anpassen

Bitte stellen Sie sicher, dass der Zeitplan für den Eingang als **„aktionsbasiert“** konfiguriert bleibt, damit Nutzer:innen Ihr Canvas betreten, wenn sie eine Sitzung in der App starten. Auf diese Weise können Sie beginnen, Ihre Beziehung durch zeitnahes Engagement aufzubauen.

Bitte beachten Sie auch, die **aktionsbasierten Optionen** unverändert zu lassen, damit Nutzer:innen den Canvas nur betreten, wenn sie eine Sitzung starten.

![Ein aktionsbasierter Zeitplan für den Eingang von Nutzern:innen, die eine beliebige Sitzung starten, in Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Bitte führen Sie im Eingangsfenster ein Update der **Startzeit (erforderlich)** auf das gewünschte Datum und die gewünschte Uhrzeit durch.

![Ein Eingabefenster mit der Startzeit 16\. Januar 2025 um 12:30 Uhr. Die Nutzer:innen geben diese Nachricht in ihrer Ortszeit ein.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Schritt 4: Wählen Sie die Zielgruppe aus

Definieren Sie Ihre Zielgruppe als Steppington-Nutzer:innen, die keine E-Mail-Adresse in ihrem Nutzerprofil angegeben haben, indem Sie den Standard[-Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) [für die Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) der`Email Available is false` Vorlage beibehalten.

![Zielgruppe mit dem Filter „E-Mail verfügbar ist falsch”.]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Bitte behalten Sie die Standard-Abonnement-Einstellungen bei, damit Sie nur an Nutzer:innen senden, die sich für den Empfang von Nachrichten oder Benachrichtigungen angemeldet oder Opt-in gemacht haben, und überspringen Sie die anderen Einstellungen (Frequency-Capping, Ruhezeiten und Seed-Gruppen).

![Standardversandoptionen, um nur an Nutzer:innen zu senden, die sich angemeldet oder durch Opt-in eingetragen haben.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Schritt 6: Canvas anpassen

Anschließend erstellen Sie die Canvas, indem Sie die Kanäle und Inhalte anpassen, die Sie an die Nutzer:innen senden möchten. Da Sie sich auf die Überprüfung von Registrierungen per E-Mail konzentrieren, müssen Sie keine Canvas-Schritte und -Kanäle des Templates hinzufügen oder entfernen.

1. Wählen Sie den ersten Schritt der Nachricht mit dem Namen **E-Mail-Registrierung**. Hier aktualisieren Sie das Template, um unsere mehrseitige In-App- (und In-Browser-)Nachricht zu verwenden.

- Seite 1 enthält die E-Mails.
- Auf Seite 2 wird eine Bestätigungsnachricht angezeigt.

![Zwei Seiten einer In-App-Nachricht zum Erfassen von Benutzer-E-Mails und zum Anzeigen einer Erfolgsmeldung.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. Bitte lassen Sie den Schritt **„Subscribed** Action Path“ unverändert. Bei diesem Schritt werden unsere Nutzer:innen innerhalb eines Tagesfensters in zwei Gruppen aufgeteilt:

- Nutzer:innen, die Steppington mit ihrer E-Mail abonniert haben
- Nutzer:innen, die Steppington nicht mit ihrer E-Mail abonniert haben

{:start="3"}
3\. Als Nächstes ersetzen Sie die E-Mail durch unsere gebrandete Bestätigungs-E-Mail für den Schritt **E-Mail** Nachricht **überprüfen**. Dadurch wird eine E-Mail an unsere registrierten Abonnent:innen versendet, in der sie aufgefordert werden, ihre E-Mail-Adresse zu bestätigen und sich für das Messaging anzumelden.
4\. Behalten Sie den Schritt Aktions-Pfad für **das Abo bestätigen** unverändert bei. Dieser Schritt unterteilt unsere Nutzer:innen weiter in diejenigen, die ihre E-Mail-Adresse bestätigt haben, und diejenigen, die dies noch nicht getan haben, mit einem Zeitfenster von einer Woche.
5\. Zum Schluss aktualisieren Sie den Schritt **Willkommen + Rabattnachricht** mit unserer E-Mail zur Bestätigung, die einen exklusiven Aktionscode enthält.

{% alert note %}
Der Schritt **„E-Mail**-Nachricht **überprüfen“** wird bei der zweiten Sitzung der Nutzer:innen ausgelöst. Dies liegt daran, dass das erste Sitzungsstart-Ereignis zwar die Canvas auslöst, jedoch ein zweiter Sitzungsstart erforderlich ist, nachdem der Nutzer den ersten Schritt **„Registrierung**“ erreicht hat, damit der Nutzer berechtigt ist, die zweite In-App-Nachricht zu triggern.
{% endalert %}

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem Sie Ihr Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten Sie es, indem Sie **„Launch Canvas“** auswählen.

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}
