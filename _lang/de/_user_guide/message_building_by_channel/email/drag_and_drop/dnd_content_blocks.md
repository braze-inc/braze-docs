---
nav_title: Content-Blöcke
article_title: Drag-and-Drop Editor Inhaltsblöcke
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Content-Blöcke im Drag-and-Drop-Editor erstellen und verwenden."
tool: Media

---

# Drag-and-Drop-Editor Inhaltsblöcke

> Die Content-Blöcke, die ausschließlich im Drag-and-Drop-Editor verwendet werden, ähneln in ihrer Funktionalität den [Content-Blöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), die in den verschiedenen Kanälen verwendet werden. Sie sind ein zentraler Speicherort für Informationen, auf die in verschiedenen E-Mail-Kampagnen Bezug genommen werden kann. So können Sie beispielsweise E-Mail-Kopfzeilen, Werbeaufrufe und vieles mehr in einer wiederverwendbaren Zeile zusammenfassen.

{% alert note %}
Drag-and-Drop-Inhaltsblöcke sind nur für die Verwendung in E-Mail-Kampagnen und E-Mail-Nachrichten in Canvas verfügbar.
{% endalert %}

## Erstellen eines Content-Blocks

Um einen Content-Block zu erstellen, gehen Sie wie folgt vor:

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Jeder Drag-and-Drop-Inhaltsblock ist auf eine Zeile beschränkt. Sie können den Content-Block jedoch mit Hilfe von Drag-and-Drop-Editor-Blöcken erstellen und an Ihre E-Mail-Nachrichten anpassen.
{% endalert %}

## Verwenden eines Content-Blocks

Es gibt zwei Möglichkeiten, den Content-Block zu Ihrer E-Mail hinzuzufügen: mit dem Editor oder mit Liquid.

### Verwenden des Editors zum Hinzufügen eines Inhaltsblocks

Um einen Content-Block im Editor hinzuzufügen, gehen Sie wie folgt vor:

1. Gehen Sie im Editor auf die Registerkarte **Zeilen** und wählen Sie **Inhaltsblöcke**. 
2. Ziehen Sie Ihren Content-Block per Drag & Drop in den E-Mail-Editor. 
3. (Optional) Passen Sie die Breite Ihres Content-Blocks an, indem Sie den Button im Navigationsmenü auswählen. Der Standardwert für die Breite ist 100%, wenn Sie in den globalen Einstellungen für den E-Mail-Stil nichts angegeben haben. Andernfalls werden die globalen Einstellungen beachtet. <br><br>\![Ein doppelseitiger Pfeil mit einer Option zum Bearbeiten der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

Nachdem Sie den Content-Block zum E-Mail-Editor hinzugefügt haben, können Sie Änderungen am Content-Block vornehmen, die sich nicht auf den ursprünglichen Content-Block auswirken, den Sie in **Templates & Medien** erstellt haben. Das liegt daran, dass Content-Blöcke, die per Drag-and-Drop hinzugefügt werden, nicht mit dem ursprünglichen Content-Block verknüpft sind. Um alle Änderungen am ursprünglichen Content-Block anzuzeigen, ziehen Sie ihn erneut in den E-Mail-Editor. 

Im Drag-and-Drop-Editor kann es zu Ausrichtungsfehlern kommen, wenn mehrere Content-Blöcke zu einem einzelnen Zeilenblock hinzugefügt werden. Versuchen Sie, separate Zeilenblöcke zu verwenden, um die Ausrichtung Ihres Contents auf Zeilenebene beizubehalten.

### Verwenden von Liquid zum Hinzufügen eines Content-Blocks

Um einen Content-Block mit Hilfe von Liquid hinzuzufügen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrer E-Mail-Kampagne und wählen Sie **E-Mail-Text bearbeiten**. 
2. Klicken Sie auf <i class="fas fa-plus"></i> **Personalisierung**.
3. Suchen Sie die Registerkarte **Personalisierung hinzufügen** und wählen Sie **Inhaltsblöcke** in der Dropdown-Liste **Personalisierungstyp**.
4. Wählen Sie den Namen Ihres Inhaltsblocks im Feld **Attribut**. Das Liquid Snippet-Feld wird mit Ihrem Content Block Liquid Tag gefüllt. 
5. Kopieren Sie das Liquid-Snippet und fügen Sie es in einen Texteditor-Block ein. <br>\![Der Tab Personalisierung hinzufügen mit Optionen.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Wenn Sie eine Vorschau Ihrer E-Mail-Nachrichten anzeigen, wird das Liquid-Snippet als Inhaltsblock des Drag-and-Drop-Editors angezeigt. 

{% alert important %}
Wenn ein Content-Block in den E-Mail-Editor mit Liquid eingefügt wird, ist dieser Content-Block mit dem ursprünglichen Content-Block verknüpft, der in **Templates & Medien** erstellt wurde. Das bedeutet, dass der Content-Block aktualisiert wird, um alle Änderungen an der ursprünglichen Content-Block-Template zu berücksichtigen.
{% endalert %}

## Aktualisieren von Content-Blöcken

Um einen vorhandenen Inhaltsblock zu aktualisieren, können Sie entweder den ursprünglichen Inhaltsblock auf der Seite **Inhaltsblöcke** bearbeiten oder den HTML-Code der ursprünglichen Nachricht in die neue Nachricht kopieren. Aktualisierungen einer Content-Block-Template werden in allen E-Mail-Nachrichten aktualisiert, in denen der Content-Block über Liquid hinzugefügt wurde.

Um einen Inhaltsblock zu archivieren, gehen Sie zu **Vorlagen** > **Inhaltsblöcke**, wählen das vertikale Ellipsen-Symbol <i class="fas fa-ellipsis-vertical"></i> für den Inhaltsblock und klicken auf **Archivieren**. Wenn Sie einen Content-Block archivieren, enthalten Ihre Nachrichten weiterhin den Content des archivierten Blocks. Archivierte Content-Blöcke sind jedoch schreibgeschützt. Dearchivieren Sie daher den Content-Block, bevor Sie ihn bearbeiten. 

