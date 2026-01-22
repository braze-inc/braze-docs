---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze-Canvas-Template verwenden, um Onboarding-Journeys zu erstellen, die eine starke anfängliche Akzeptanz und dauerhafte Beziehungen zu Ihren Nutzer:innen fördern."
tool: Canvas
---

# Onboarding

> Beginnen Sie Ihre Nutzer-Journey mit diesem Onboarding-Template. Dieses Template wurde entwickelt, um eine starke anfängliche Akzeptanz zu fördern und dauerhafte Beziehungen zu Ihren Nutzer:innen zu schaffen. Durch personalisierte Kommunikation und eine strukturierte Reihe von Nachrichten können Sie Ihre Nutzer nahtlos mit Ihrer Marke bekannt machen und den Beginn einer dauerhaften Beziehung einleiten.

In diesem Artikel stellen wir Ihnen einen Anwendungsfall für das **Onboarding**-Template vor, die für die Überlegungsphase des Nutzerlebenszyklus gedacht ist, um eine nahtlose Onboarding-Erfahrung für neue Nutzer:innen zu schaffen. Nach diesem Artikel werden Sie diese Braze Canvas-Vorlage mit personalisierten Nachrichten für diese neuen Benutzer angepasst haben.

## Voraussetzungen

Bevor Sie diese Vorlage verwenden, müssen Sie die folgenden [E-Mail-Vorlagen]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) erstellen, auf die Sie im Canvas verweisen können:

- Eine Willkommens-E-Mail an alle Benutzer Ihrer App
- Eine E-Mail mit Tipps zur Verwendung Ihrer App
- Eine Feedback-E-Mail, die eine Benutzerumfrage enthält

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten bei PantsLabyrinth und unser Ziel ist es, das Engagement der Benutzer zu erhöhen, Vertrauen und Loyalität bei unseren Benutzern aufzubauen und sie zu ermutigen, sich weiter zu engagieren. Dazu wollen wir uns darauf konzentrieren, Nachrichten zu verfassen, die neue Nutzer ansprechen, die noch nicht mit der App interagiert haben.

Um auf die Onboarding-Vorlage zuzugreifen, wählen Sie bei der Erstellung eines neuen Canvas die Option **Eine Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **Onboarding** die Option **Vorlage anwenden**. Beginnen wir damit, diese Vorlage an unseren Anwendungsfall anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

\![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Aktualisieren Sie den Namen von Canvas, um anzugeben, dass Canvas für die Aufnahme neuer Nutzer:innen gedacht ist.
3\. Aktualisieren Sie die Beschreibung und geben Sie an, dass das Canvas eine Abbildung einer Nutzer-Journey enthält, die Vertrauen und Loyalität fördert.
4\. Fügen Sie das Tag **Onboarding** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

\![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Schritt 2: Konversions-Events zuweisen

Als nächstes weisen wir unsere Konvertierungsereignisse zu. Konversions-Events sind eine Art Metrik, mit der Sie den Erfolg des Canvas messen können. Wählen Sie für **Benutzerdefinierter Ereignisname** die Option **E-Mail-Klick** als benutzerdefiniertes Ereignis.

\![Primäre Konversion-Event - A mit dem Konversionstyp "Führt angepasstes Event durch" mit dem angepassten Event-Namen "E-Mail Klick". Es gibt eine Frist von 4 Tagen für die Konversion.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Das bedeutet, dass neue Nutzer:innen bis zu vier Tage Zeit haben, die Willkommens-E-Mail anzuklicken. In diesem Fall möchten wir, dass unsere neuen Kunden ein Gefühl der Dringlichkeit verspüren, sich bei PantsLabyrinth zu engagieren und eine wiederkehrende Lieferung von saisonaler Kleidung zu abonnieren.

### Schritt 3: Entry-Zeitplan festlegen

Da das Ziel darin besteht, neue Benutzer von PantsLabyrinth anzusprechen, werden wir den Canvas handlungsorientiert gestalten. Wählen Sie für **Sitzung starten** die Option **Sitzung in einer beliebigen App starten**, damit Benutzer, die eine Sitzung in einer beliebigen App starten, den Canvas betreten können.

Als nächstes passen Sie das **Eingabefenster** an, um festzulegen, wann Benutzer das Canvas betreten können. Nehmen wir an, es gibt Ende Oktober ein neues HosenLabyrinth-Abonnement. Hier stellen wir die Startzeit auf **2024/10/28 8:00 Uhr** ein. Optional können wir den Nutzer:innen auch erlauben, den Canvas in ihrer lokalen Zeitzone aufzurufen.

\![Ein Eingangsfenster mit der Startzeit 28\. Oktober 2024 um 8 Uhr. Nutzer:innen werden diese Nachricht in ihrer Ortszeit eingeben.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Schritt 4: Targeting Ihrer Zielgruppe

Indem wir die richtige Zielgruppe zusammenstellen, können wir neue Nutzer:innen effektiv ansprechen. Diese Vorlage zielt beispielsweise auf alle Benutzer ab, die eine App vor weniger als einem Tag zum ersten Mal genutzt haben, was für unseren Anwendungsfall genau richtig ist. Also lassen wir diesen Abschnitt so, wie er ist.

### Schritt 5: Sendeeinstellungen festlegen

Standardmäßig wird diese Canvas an Benutzer gesendet, die abonniert oder angemeldet sind, und folgt den Regeln für die Häufigkeitsbegrenzung. Wir lassen diese Einstellungen so wie sie sind.

### Schritt 6: Canvas anpassen

Lassen Sie uns nun das Canvas erstellen, indem wir die Template-Schritte anpassen.

#### Einrichten der Willkommens-E-Mail

1. Wählen Sie den Nachrichtenschritt „Willkommens-E-Mail“ aus.
2. Wählen Sie **Nachricht bearbeiten**, um die E-Mail der Vorlage durch unsere Willkommens-E-Mail zu ersetzen.
3. Wählen Sie **Erledigt**.

Jetzt erhalten unsere Benutzer diese Willkommens-E-Mail, nachdem sie eine Sitzung in unserer App gestartet haben. Um die Nutzer:innen nicht mit wiederholtem Messaging zu überfordern, empfehlen wir, den Schritt „Delay“ als Teil der User Journey zu verwenden.

#### Zielgruppenpfad anpassen

Im Schritt „Zielgruppenpfad“ namens **Zielgruppen-Split** können wir den Filter für unsere engagierten Nutzer:innen anpassen. In der Vorlage ist der Filter **Hat geklickt für den Schritt Willkommens-E-Mail**, was bedeutet, dass die Benutzer in zwei Gruppen aufgeteilt werden: Benutzer, die die Willkommens-E-Mail angeklickt haben, und diejenigen, die dies nicht getan haben.

\![Ein Schritt zur Aufteilung der Zielgruppe mit einem Pfad für engagierte Nutzer:innen und einem Pfad für alle anderen.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Als Online-Kleiderhändler hat PantsLabyrinth auch eine aktive Gruppe von mobilen Nutzern. In einem separaten Onboarding-Canvas können wir also auch den folgenden Filter auswählen, um unsere mobilen Nutzer:innen zu identifizieren und in diese Segmente aufzuteilen:

- **Hat die Inhaltskarte für den Schritt Willkommens-Inhaltskarte angeklickt**
- **Alle anderen**

#### Targeting für mehr Nutzer:innen mit Zielgruppenpfaden

Aus der Gruppe der Nutzer, die nicht mit unserer App interagiert haben, können wir diese Nutzer weiter ansprechen, indem wir den Schritt "Auf Klicks prüfen" und den Schritt "Winback Nudge" bearbeiten.

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Canvas starten**, um das Canvas zu starten. Jetzt können wir unseren neuen Nutzer:innen ein personalisiertes Onboarding-Erlebnis bieten, um eine dauerhafte Beziehung zu fördern!

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}

