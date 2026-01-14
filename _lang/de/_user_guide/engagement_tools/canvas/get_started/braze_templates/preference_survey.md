---
nav_title: Onboarding mit Umfrage zu den Präferenzen
article_title: Onboarding mit Umfrage zu den Präferenzen
page_order: 5.5
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Braze-Canvas-Vorlage verwenden, um die Akzeptanz mit einem geführten Onboarding-Flow zu fördern, um neue Nutzer:innen mit Ihrer Marke vertraut zu machen und Präferenzen zu sammeln, um sie langfristig zu binden."
tool: Canvas
---

# Onboarding mit Umfrage zu den Präferenzen

> Verwenden Sie die Vorlage für Umfragen zum Onboarding mit Präferenzen, um einen geführten Onboarding-Workflow zu erstellen, der sich an neue Nutzer:innen richtet. Machen Sie sie mit Ihrer Marke bekannt, helfen Sie ihnen beim Einstieg und sammeln Sie ihre Vorlieben, um sie langfristig zu binden.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template für die **Umfrage Onboarding mit Präferenzen**, die für die Überlegungsphase des Nutzer:innen-Lebenszyklus konzipiert ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das E-Mails und In-App-Nachrichten an Nutzer:innen sendet, wenn diese eine Sitzung beginnen und wenn sie ihr Onboarding noch nicht abgeschlossen haben.

## Voraussetzungen

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Eine Willkommens-E-Mail, die Nutzer:innen auffordert, mit dem Onboarding zu beginnen.
- Eine E-Mail mit Tipps für den Einstieg in die App für Nutzer:innen, die Onboarding gemacht haben.
- Eine E-Mail, die Nutzer:innen auffordert, ihr Onboarding abzuschließen.
- Eine [Umfrage]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) mit mehreren Fragen zur Ermittlung der Präferenzen der Nutzer:innen.

## Anpassen des Templates an Ihre Bedürfnisse

Nehmen wir an, wir arbeiten für StyleRyde, eine App für Mitfahrgelegenheiten auf Abruf, die Menschen dorthin bringt, wo sie hinmüssen. Vor der Erstellung des Canvas haben wir [eine einfache Umfrage]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) mit einer Reihe von engagierten Fragen [erstellt]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog), um die Erfahrungen und Impressionen eines Nutzers:innen bei der ersten Fahrt mit der App zu ermitteln.

Um auf die Vorlage zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Canvas-Vorlage verwenden** > **Braze-Vorlagen**. Wählen Sie dann neben **Onboarding mit Umfrage nach Präferenzen** die **Vorlage anwenden** aus. Jetzt können wir das Template durchgehen, um es an unsere Bedürfnisse anzupassen.

### Schritt 1: Details einrichten

Passen wir die Canvas-Details an, um unser Ziel zu erreichen.

1. Wählen Sie **Bearbeiten** neben dem Namen der Vorlage.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen bei der ersten Verwendung der App gedacht ist.
3\. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisierte Nachrichten enthält.
4\. Fügen Sie das Tag **Onboarding** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Schritt 2: Konversions-Events zuweisen

Aktualisieren Sie das **primäre Konversions-Event - A** auf **Performs Custom Event**. Wählen Sie dann die **zuletzt verwendete App** für das angepasste Event aus.

![Zuletzt verwendete App als ausgewählter angepasster Event-Name für das Konversions-Event.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Schritt 3: Entry-Zeitplan anpassen

Behalten wir den Zeitplan für den Eingang als **aktionsbasiert** bei, damit die Nutzer:innen unser Canvas betreten, wenn sie eine Sitzung in der App starten. Auf diese Weise können wir beginnen, unsere Beziehungen mit rechtzeitigem Engagement aufzubauen.

Wir nehmen ein Update in diesem Abschnitt vor, indem wir das **Fenster Eingang** auf das gewünschte Datum und die Uhrzeit anpassen.

!["Eingangsfenster" Abschnitt mit der Startzeit 30\. Januar 2025 um 12 Uhr.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Schritt 4: Wählen Sie die Zielgruppe aus

Wir werden die Zielgruppe unverändert beibehalten, um unsere Nutzer:innen anzusprechen, die die StyleRyde App vor weniger als einem Tag zum ersten Mal genutzt haben.

![Der Filter "Diese Apps wurden vor weniger als 1 Tag zum ersten Mal verwendet" wurde ausgewählt, um die Zielgruppe für den Eingang anzusprechen.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Schritt 5: Wählen Sie Ihre Sendeeinstellungen aus

Wir behalten die Standard Abo-Einstellungen bei, d.h. wir senden nur an Nutzer:innen, die Nachrichten oder Benachrichtigungen mit aktivierten Ruhezeiten abonniert oder sich dafür entschieden haben, und überspringen die anderen Einstellungen (Frequency-Capping und Seed-Gruppen).

!["Sendeeinstellungen" mit den Abo-Einstellungen für Nutzer:in, die ein Abonnement oder Opt-in mit eingeschalteten Ruhezeiten zwischen 12 und 20 Uhr haben.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Schritt 6: Canvas anpassen

Jetzt bauen wir unser Canvas auf, indem wir die Inhalte anpassen, die an die Nutzer:innen gesendet werden sollen. 

1. Für den ersten Schritt der Nachricht **Willkommens-E-Mail** werden wir diesen Schritt aktualisieren, um unsere StyleRyde Willkommens-E-Mail einzubeziehen.
2. Als nächstes lassen wir den Schritt Aktions-Pfad unverändert. Bei diesem Schritt werden unsere Nutzer:innen innerhalb eines Zeitfensters von drei Tagen in zwei Gruppen aufgeteilt:

- Nutzer:innen, die eine Sitzung begonnen oder auf die Onboarding E-Mail geklickt haben
- Nutzer:innen, die keine Sitzung begonnen oder auf die Onboarding E-Mail geklickt haben

![Ein Aktions-Pfad-Schritt, der in zwei Pfade aufgeteilt ist, einen für Nutzer:innen, die eine Sitzung begonnen haben, und einen für alle anderen.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

Von hier aus werden wir unsere Nutzer:innen und Nachrichten auf der Grundlage der oben genannten Gruppen zusammenstellen.

#### Stellen Sie Ihre engagierten Nutzer:innen gezielt zusammen

Für unsere Nutzer:innen, die eine Sitzung begonnen oder sich im ersten Schritt des Messagings mit unserer Onboarding E-Mail engagiert haben, aktualisieren wir den Schritt **Tipps für den Einstieg**, um die wichtigsten Reise- und Sicherheitstipps für unsere neuen Nutzer:innen aufzunehmen.

Nachdem ein Nutzer:innen sein Onboarding abgeschlossen hat, verlässt er den Canvas.

Als Nächstes aktualisieren Sie den Schritt Nachricht **über die Umfrage zu den Inhaltspräferenzen**, um unsere Umfrage zu den Präferenzen einzubeziehen, bei der unsere Nutzer:innen auswählen können, zu welchen Themen sie in Zukunft Informationen erhalten möchten.

![Eine Vorschau auf die Umfrage zu den Präferenzen, in der die Nutzer:innen aufgefordert werden, alle zutreffenden Interessen auszuwählen.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Nutzer:innen anstupsen, die noch nicht mit dem Onboarding begonnen haben 

Für unsere anderen Nutzer:innen aktualisieren wir den Schritt **Winback Nudge** Message mit unserer Followup E-Mail, um die Nutzer:innen aufzufordern, ihr Onboarding abzuschließen.

Als letzten Schritt für erneutes Engagement benennen wir **Schritt 2** in **Final Winback Nudge** um und aktualisieren den Schritt mit unserer In-App-Nachricht, um unsere neuen Nutzer:innen aufzufordern, ihr Onboarding abzuschließen.

### Schritt 7: Testen und starten Sie Ihr Canvas

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Canvas starten** auswählen.

{% alert tip %}
In unserer [Checkliste für die Zeit vor und nach dem Start eines]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) Canvas finden Sie die Dinge, die Sie beachten sollten, bevor und nachdem Sie ein Canvas starten.
{% endalert %}