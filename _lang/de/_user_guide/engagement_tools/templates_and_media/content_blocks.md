---
nav_title: Content-Block-Bibliothek
article_title: Content-Block-Bibliothek
page_order: 1
page_type: reference
description: "In diesem Referenzartikel wird erklärt, wie Sie die Content-Block-Bibliothek verwenden, um Ihren wiederverwendbaren, kanalübergreifenden Content an einem einzigen, zentralen Standort zu verwalten."
tool: 
  - Templates
  - Media

---

# Content-Block-Bibliothek

> Die Content-Block-Bibliothek erlaubt es Ihnen, Ihren wiederverwendbaren, kanalübergreifenden Content an einem einzigen, zentralen Standort zu verwalten.

Mit Content-Blöcken haben Sie folgende Möglichkeiten:

- Schaffen Sie ein einheitliches Erscheinungsbild für Ihre E-Mail-Kampagnen, indem Sie sie als Kopf- und Fußzeilen verwenden.
- Verteilen Sie die gleichen Angebotscodes über verschiedene Kanäle.
- Erstellen Sie vordefinierte Assets, die Sie zum Aufbau von Nachrichten mit konsistenten Informationen und Assets verwenden können.
- Kopieren Sie ganze Nachrichtenteile in andere Nachrichten.

## Content-Block erstellen

Es gibt zwei Arten von Editoren, mit denen Sie einen Inhaltsblock erstellen können: klassisch und per Drag&Drop. Diese beiden Typen von Editoren entsprechen dem Typ des Content-Blocks: HTML und Drag-and-Drop. Sie können Ihre Content-Blöcke auch [über die API]({{site.baseurl}}/api/endpoints/templates/) erstellen und verwalten.

{% tabs %}
{% tab Drag-and-drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Content-Block-Spezifikationen

| Content-Block-Attribut | Spezifikationen |
|---|---|
| Name | Pflichtfeld mit maximal 100 Zeichen. Dieses Feld kann nicht umbenannt werden, nachdem der Content-Block gespeichert wurde. Außerdem können Sie einem neuen Content-Block nicht denselben Namen geben wie einem früheren Content-Block, selbst wenn der vorherige archiviert wurde. |
| Beschreibung | (optional) Maximal 250 Zeichen. Beschreiben Sie den Content-Block, damit andere Nutzer:innen von Braze wissen, wofür er gedacht ist und wo er verwendet wird. |
| Content-Größe | Maximal 50 KB. |
| Platzierung | Inhaltsblöcke können nicht in einer E-Mail-Fußzeile verwendet werden. |
| Erstellung | HTML-Editor oder Drag-and-Drop-Editor. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Bei der Erstellung von Content-Blöcken kann es von Vorteil sein, HTML und Liquid durch Hinzufügen von Zeilenumbrüchen zu visualisieren. Wenn diese Zeilenumbrüche beim Senden nicht berücksichtigt werden, riskieren Sie überflüssige Leerzeichen, die die Darstellung des Blocks beeinträchtigen können. Um dies zu vermeiden, verwenden Sie das Tag **Erfassen** in Ihrem Block zusammen mit dem Filter **| strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Inhaltsblöcke verwenden

Nachdem Sie Ihren Content-Block erstellt haben, können Sie ihn in Ihre Nachrichten einfügen, indem Sie die folgenden Schritte ausführen: 

1. Kopieren Sie das **Content Block Liquid Tag** aus dem Abschnitt **Content Block Details**.
2. Fügen Sie das Liquid-Tag für Content-Block in die Nachricht ein. Sie können auch mit der Eingabe der Flüssigkeit beginnen und den Tag automatisch ausfüllen lassen.

### Was Sie wissen sollten

- Die Verwendung von HTML Content-Blöcken in E-Mails per Drag-and-Drop **oder von** Content-Blöcken in HTML-E-Mails kann zu unerwarteten Darstellungsproblemen führen. Das liegt daran, dass der Drag-and-Drop-Editor HTML und CSS generiert, die den Inhalt dynamisch wiedergeben, während der HTML-Editor eher statisch ist.
- Canvas Event-Eigenschaften werden nur in einem Canvas unterstützt. Wenn Sie einen Content-Block mit Canvas-Eingangs-Eigenschaften in einer Kampagne referenzieren, wird er nicht aufgefüllt.

### Aktualisieren und Kopieren von Inhaltsblöcken

Wenn Sie einen Content-Block aktualisieren möchten, wird er in allen Nachrichten aktualisiert, in denen der Content-Block verwendet wird, wenn er über Liquid eingefügt wird. Wenn der Inhaltsblock über das Dropdown-Menü **Inhaltsblöcke** unter **Zeilen** im Drag-and-Drop-Editor importiert wird, wird er nicht in allen Nachrichten aktualisiert.

Wenn Sie einen Inhaltsblock für eine einzelne Nachricht aktualisieren oder eine Kopie zur Verwendung in anderen Nachrichten erstellen möchten, können Sie entweder den HTML-Code aus der ursprünglichen Nachricht in Ihre neue Nachricht kopieren oder den ursprünglichen Inhaltsblock bearbeiten (er muss bereits in einer Nachricht verwendet worden sein) und speichern. Sie erhalten eine Aufforderung, die es Ihnen erlaubt, ihn als neuen Content-Block zu speichern.

Nachdem Sie Änderungen an einem Content-Block vorgenommen haben, können Sie den aktualisierten Content-Block speichern und starten, indem Sie **Content-Block starten** auswählen. Oder Sie können **Mehr** > **Duplizieren** wählen, um ein Duplikat Ihres Inhaltsblocks zu erstellen.

\![Ein Content-Block mit der Aufschrift "Willkommen zu unserem Newsletter".]({% image_buster /assets/img/copy-content-block.png %})

Sie können einen Content-Block auch [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/). Dadurch wird eine Entwurfskopie des Inhaltsblocks erstellt.

### Vorschau von Inhaltsblöcken

Nachdem Sie einen Inhaltsblock in einer aktiven Kampagne oder einem Canvas hinzugefügt haben, können Sie eine Vorschau dieses Inhaltsblocks in der Inhaltsblock-Bibliothek anzeigen, indem Sie den Mauszeiger über den Inhaltsblock bewegen und das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** auswählen. 

Diese Vorschau enthält Informationen zum Content-Block, z. B. wer ihn erstellt hat, Tags, Erstellungsdatum, Datum der letzten Bearbeitung, Beschreibung, Editor-Typ, Anzahl der Einschlüsse mit Details und eine aktuelle Vorschau des Content-Blocks.

\![Eine Vorschau auf einen Content-Block "Workout_Promo" für Radfahren und Tanzen, der sechs Einschlüsse hat.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### Verschachtelte Content-Blöcke

Inhaltsblöcke können verschachtelt werden, aber nur einmal. Sie können Content-Block A in Content-Block B verschachteln, aber Sie können Content-Block B nicht in Content-Block C verschachteln.

{% alert warning %}
Sie können eine dritte Ebene von Content Block einfügen. Allerdings wird der Content in den Ebenen nach der zweiten nicht erweitert. Der Inhalt und das Liquid-Snippet werden aus der Nachricht entfernt.
{% endalert %}

Außerdem können Inhaltsblöcke nicht innerhalb einer E-Mail-Fußzeile verwendet werden, obwohl E-Mail-Fußzeilen innerhalb von Inhaltsblöcken verwendet werden können.

### Inhaltsblöcke archivieren

\![Erweitertes Dropdown-Menü Einstellungen, das drei Optionen anzeigt: Archivieren, Duplizieren und In Arbeitsbereich kopieren.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Wenn Sie die Verwendung eines Content-Blocks beendet haben, können Sie ihn auf der Seite [Templates & Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) archivieren. Archivierte Content-Blöcke sind schreibgeschützt. Dearchivieren Sie also den Content-Block, bevor Sie ihn bearbeiten. Content-Blöcke können nicht archiviert werden, wenn sie in Nachrichten verwendet werden.

#### Bewährte Praktiken

- Wenn Ihr Block nur in wenigen E-Mails verwendet wird, empfehlen wir Ihnen, den veralteten Block zu archivieren und Ihre Live-Nachrichten mit einem neueren Block zu aktualisieren, der nicht archiviert wurde.
- Wenn Ihr Block nur einen Tippfehler hat oder eine kleine Änderung benötigt, empfehlen wir nicht, den Block zu archivieren. Aktualisieren Sie stattdessen den Block und schicken Sie ihn ab!
- Wenn Ihr Block in mehr Nachrichten verwendet wird, als Sie mit dem ersten Vorschlag in dieser Liste vernünftig verwalten können, empfehlen wir, alle Inhalte aus dem Block zu entfernen und ihn zu archivieren. So stellen Sie sicher, dass keine veralteten Informationen in neu versendeten E-Mails enthalten sind.
- Wenn Sie versehentlich einen Content-Block archiviert haben, können Sie die Archivierung aufheben.

\![Panel für gespeicherte Content-Blöcke, in dem das Dropdown-Menü für die Einstellungen für "Test_32" erweitert wird und drei Optionen anzeigt: Entarchivieren, Duplizieren und Kopieren in den Arbeitsbereich]({% image_buster /assets/img/unarchive-content-block.png %})

