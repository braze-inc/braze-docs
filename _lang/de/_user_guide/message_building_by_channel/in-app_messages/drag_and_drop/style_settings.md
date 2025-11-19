---
nav_title: Stil-Einstellungen
article_title: "In-App Nachrichtenstil-Einstellungen"
description: "Dieser Referenzartikel behandelt die verfügbaren Gestaltungsoptionen beim Erstellen einer In-App-Nachricht mit dem Drag-and-Drop-Editor."
page_order: 3
---

# Einstellungen für den In-App-Nachrichtenstil

> Die Drag-and-Drop-Bearbeitung ist in zwei Bereiche unterteilt: **Build** und **Vorschau & Test**. In diesem Artikel erfahren Sie, was Sie für die Arbeit auf der Registerkarte " **Erstellen"** des Editors wissen müssen. Wir gehen davon aus, dass Sie bereits [eine In-App-Nachricht erstellt]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) haben.

!["Tab "Nachrichten-Stile".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Stile auf Nachrichtenebene

Auf der Registerkarte **Nachrichtenstile** können Sie bestimmte Stile festlegen, die auf alle relevanten Blöcke in Ihrer In-App-Nachricht angewendet werden. So können Sie beispielsweise die Schriftart des gesamten Textes oder die Farbe aller Links in Ihrer Nachricht anpassen.

Die Stile in diesem Abschnitt werden überall in Ihrer Nachricht verwendet, es sei denn, Sie setzen sie für einen bestimmten Block außer Kraft. Wenn Ihre Nachricht aus [mehreren Seiten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) besteht, können Sie auch die Stile auf Nachrichtenebene für die einzelnen Seiten außer Kraft setzen, mit Ausnahme des Anzeigetyps und der maximalen Breite.

Um das Design zu vereinfachen, empfehlen wir Ihnen, die Stile auf Nachrichtenebene einzurichten, bevor Sie die Stile auf Blockebene anpassen.

Sie können jederzeit zur Registerkarte **Nachrichtenstile** zurückkehren:

- Klicken Sie auf den Button „Schließen“ (X) in den einzelnen Blockeigenschaften.
- Wählen Sie den Nachrichten-Container, den Button zum Schließen der Nachricht X oder den Editor-Hintergrund aus.

### Benutzerdefinierte Schriftarten

Wir akzeptieren die folgenden Dateitypen für Schriftarten: `.ttf`, `.woff`, `.otf` und `.woff2`. Weitere Informationen finden Sie unter [Asset-Dateien]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Sie können mehrere Varianten einer Schriftfamilie hinzufügen, da einige Styling-Optionen für benutzerdefinierte Schriftarten nicht verfügbar sind. Derzeit unterstützen wir das Hinzufügen von Schriftarten über eine URL nicht.

Um eine benutzerdefinierte Schriftart hinzuzufügen:

1. Gehen Sie zum Abschnitt **Inhalt** auf der Registerkarte **Nachrichtenstile**.
2. Klicken Sie auf **Benutzerdefinierte Schriftart hinzufügen**.
3. Laden Sie Ihre Schriftart über die Mediathek hoch. 

{% alert note %}
Die Schriftart auf Nachrichtenebene gilt nur für die aktuelle Nachricht und alle duplizierten Nachrichten, aber nicht für zukünftige Vorlagen.
{% endalert %}

## Messaging-Komponenten

![Ein GIF, das die Erstellung einer In-App-Nachricht zu Werbezwecken zeigt.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

Der Drag-and-Drop-Editor verwendet zwei Schlüsselkomponenten zum Verfassen von In-App-Nachrichten: **Zeilen** und **Blöcke**. Alle Blöcke müssen in einer Reihe platziert werden.

### Button x schließen

Für Modal- und In-App-Nachrichten im Vollbildmodus können Sie den Button zum Schließen anpassen, der als <i class="fa-solid fa-xmark"></i> in der oberen rechten Ecke Ihrer Nachricht angezeigt wird. Zu den Anpassungsoptionen gehören Position, Größe, Füllfarbe, Hintergrundfarbe, Rahmenstil und Rahmenradius.

Optionen zum Anpassen des Close X Buttons in In-App-Nachrichten, einschließlich Buttongröße, Füllfarbe, Hintergrundfarbe, Rahmenstil und Rahmenradius.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Spanne Styling

Das Hinzufügen von span styling zu Text in In-App-Nachrichten erlaubt eine bessere Anpassung des Erscheinungsbildes von Nachrichten und ermöglicht die Verwendung verschiedener Textfarben, Schriftarten und -größen. Span Styling bietet Ihren Nutzer:innen ein einnehmendes und visuell ansprechendes Erlebnis, indem es die Aufmerksamkeit auf die wichtigsten Informationen lenkt und die Klarheit der Nachrichten insgesamt verbessert.

![Option, die angezeigt wird, wenn Sie Text in einer In-App-Nachricht hervorheben. Ein kleines Pinselsymbol zeigt an, dass Sie mit der Spanne für Stil umbrechen können.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Side Panel für "Span Properties", mit dem der Endnutzer:in die Lage versetzt wird, die Schriftfamilie, das Schriftgewicht, die Schriftgröße, den Buchstabenabstand und die Textfarbe anzupassen.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Zeilen

Zeilen sind Struktureinheiten, die den horizontalen Aufbau eines Abschnitts der Nachricht mit Hilfe von Zellen definieren.

![Zeilen, die Sie in Ihrer In-App-Nachricht hinzufügen können.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Wenn eine Zeile ausgewählt ist, können Sie im Bereich **Spaltenanpassung** die gewünschte Anzahl von Spalten hinzufügen oder entfernen, um verschiedene Inhaltselemente nebeneinander anzuordnen. 

Die Größe der Spalten können Sie mit dem Schieberegler anpassen.

![Anpassen von Spalten aus dem Bereich "Spaltenanpassung".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Es empfiehlt sich, die Eigenschaften Ihrer Zeilen und Spalten zu formatieren, bevor Sie die Blöcke innerhalb der Zeilen formatieren. Es gibt viele Stellen, an denen Sie die Abstände und die Ausrichtung anpassen können. Wenn Sie also von der Basis ausgehen, ist es einfacher, sie nach und nach zu bearbeiten.

### Blöcke

Blöcke stehen für verschiedene Arten von Nachrichteninhalten. Ziehen Sie eine Zeile in ein bestehendes Zeilensegment, und sie passt sich automatisch an die Zellenbreite an.

{% alert tip %}
Bevor Sie Blöcke hinzufügen, richten Sie [auf Nachrichtenebene Stile](#set-message-level-styles) für den Nachrichtencontainer, die Schriftart, die Farben und alles andere ein, was Sie anpassen möchten. Sie können dann die einzelnen Blöcke nach Bedarf anpassen. Die **Schaltfläche Schließen** verbleibt im oberen Bereich Ihrer Nachricht, so dass die Nutzer jederzeit die Möglichkeit haben, die Nachricht zu schließen.
{% endalert %}

![Per Drag-and-Drop können Sie aus verschiedenen Feldern auswählen.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Jeder Block hat seine eigenen Einstellungen, wie z.B. die granulare Steuerung des Paddings. Das Bedienfeld auf der rechten Seite wechselt automatisch zu einem Styling-Bedienfeld für das ausgewählte Inhaltselement. Weitere Informationen finden Sie unter [Editor-Blockeigenschaften]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/drag_and_drop_editor_blocks/?sdktab=in-app%20messages#inappmessages_properties).

Während Sie Ihre In-App-Nachricht erstellen, können Sie in der Symbolleiste eine Mobil-, Tablet- oder Desktop-Ansicht auswählen, um eine Vorschau darauf zu erhalten, wie Ihre In-App-Nachrichten für Ihre Nutzer:innen aussehen werden. So können Sie sicherstellen, dass Ihre Inhalte responsiv sind und können ggf. Anpassungen vornehmen.

## Kreative Details

### Vollbildmodus auf größeren Bildschirmen {#fullscreen}

Auf einem Tablet oder einem Desktop-Browser wird eine bildschirmfüllende In-App-Nachricht in der Mitte des App-Bildschirms angezeigt. Alle Änderungen an der maximalen Breite der Vollbildnachricht gelten nur für Tablet- und Desktop-Geräte. 

![Beispiel für eine In-App-Nachricht im Vollbildmodus.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Hinzufügen eines Hintergrundbildes

Auf der Registerkarte **Nachrichtenstile** können Sie ein Bild als Hintergrund für Ihre Nachricht hinzufügen. 

1. Wählen Sie im Canvas-Bereich den Hintergrund-Container aus. Dies ist der Bildlaufbereich Ihrer Nachricht.
2. Aktivieren Sie auf der Registerkarte **Nachrichtenstile** die Option **Hintergrundbild**.
3. Fügen Sie ein Bild aus Ihrer Mediathek hinzu, oder geben Sie die URL ein, unter der Ihr Bild gehostet wird.

{% alert tip %}
Wenn Sie Probleme bei der Auswahl eines bestimmten Blocks haben, können Sie den Aufwärtspfeil in der Inline-Symbolleiste des Blocks verwenden, um den Fokus nach oben zu jedem übergeordneten Block zu verschieben.
{% endalert %}

### Hinzufügen von Flüssigkeit

![Symbol zum Hinzufügen von Liquid Personalisierung.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Um [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) zu Ihrer In-App-Nachricht hinzuzufügen, wählen Sie <i class="fa-solid fa-circle-plus"></i> **Personalisierung hinzufügen** aus der Symbolleiste des Editors. Hier können Sie verschiedene Personalisierungsarten wie Standardattribute, Geräteattribute, benutzerdefinierte Attribute und mehr hinzufügen.

Als Nächstes nehmen Sie Ihr generiertes Liquid-Snippet und fügen es in Ihre Nachricht ein. Nachdem Sie Ihre In-App-Nachricht entworfen und erstellt haben, gehen Sie auf **Vorschau & Test**, um eine Vorschau Ihrer Nachricht zu erhalten.

### Verwendung des KI-Copywriter

Wenn ein Textblock in Ihrer In-App-Nachricht ausgewählt ist, klicken Sie auf <i class="fa-solid fa-wand-magic-sparkles" title="KI-Textschreiber"></i> in der Blocksymbolleiste, um den [KI-gestützten Texterstellungsassistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) zu starten. Der KI-Copywriter übergibt einen kurzen Produktnamen oder eine kurze Beschreibung an das GPT3-Tool von OpenAI, um menschenähnliche Marketingtexte für Ihr Messaging zu erstellen.

{% alert tip %}
Sie können ein paar Klicks sparen, indem Sie den Text innerhalb des Blocks markieren, bevor Sie auf das Symbol klicken. Der markierte Text wird dem Werkzeug hinzugefügt und die Kopie wird sofort erstellt.
{% endalert %}

![GIF des KI Werbetexters.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Stile auf Standard zurücksetzen

Eigenschaften, die Sie abweichend vom Standarddesign geändert haben, sind mit einem orangefarbenen Punkt markiert. Um eine bestimmte Eigenschaft auf ihren Standardstil zurückzusetzen, bewegen Sie den Mauszeiger über das Feld und wählen **Auf Standard zurücksetzen**.

![Oranger Punkt, der eine Textgröße auf die Standardgröße zurücksetzt.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Sie können auch das gesamte Styling für ein ausgewähltes Element zurücksetzen, indem Sie die Schaltfläche <i class="fas fa-paintbrush" title="Schaltfläche Stile kopieren oder einfügen"></i> neben dem Namen des Eigenschaftsfensters klicken und die Option **Auf Standardstile zurücksetzen** wählen.

### Kopieren und Einfügen von Stilen

Nachdem Sie Änderungen an der Gestaltung eines Elements vorgenommen haben, können Sie diese Stile kopieren und in ein anderes Element einfügen. Beim Einfügen von Stilen werden nur die für dieses Element relevanten Eigenschaften angewendet.

![Dropdown-Menü mit Option zum Kopieren von Stilen.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Wenn das Element ausgewählt ist, wählen Sie <i class="fas fa-paintbrush" title="Stile kopieren oder einfügen"></i> neben dem Namen des Eigenschaftsfensters (wenn Sie zum Beispiel eine Schaltfläche ausgewählt haben, neben "Eigenschaften der Schaltfläche").
2. Klicken Sie auf **Stile kopieren** und wählen Sie das Element, auf das Sie den kopierten Stil anwenden möchten.
3. Wählen Sie <i class="fas fa-paintbrush" title="Stile kopieren oder einfügen"></i> und wählen Sie **Stile einfügen**.

#### Tastaturkürzel

Sie können auch Tastaturkürzel zum Kopieren und Einfügen von Stilen verwenden:

| Aktion       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Stile kopieren  | <kbd>⌘</kbd> + <kbd>Umschalttaste</kbd> + <kbd>c</kbd> | <kbd>Strg</kbd> + <kbd>Umschalt</kbd> + <kbd>c</kbd> |
| Stile einfügen | <kbd>⌘</kbd> + <kbd>Umschalttaste</kbd> + <kbd>v</kbd> | <kbd>Strg</kbd> + <kbd>Umschalt</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
