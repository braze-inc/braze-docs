---
nav_title: Eine Canvas-Vorlage erstellen
article_title: Eine Canvas-Vorlage erstellen
alias: "/canvas_templates/"
page_order: 0.5
description: "In diesem Referenzartikel erfahren Sie, wie ein Template für ein Canvas erstellen."
page_type: reference
---

# Eine Canvas-Vorlage erstellen

> In diesem Referenzartikel erfahren Sie, wie Sie Templates für ein Canvas erstellen und verwalten. Mit Hilfe von Templates können Sie Ihr Messaging verfeinern, indem Sie einen konsistenten Rahmen schaffen, der sich leicht an Ihre spezifischen Ziele auf Ihren Canvase anpassen lässt.

{% alert tip %}
Sparen Sie Zeit und rationalisieren Sie Ihre Canvas-Erstellung mit den [Braze Canvas-Vorlagen](#available-braze-templates)! Durchsuchen Sie unsere Bibliothek mit vorgefertigten Vorlagen, um eine für Ihren Anwendungsfall passende Vorlage zu finden, und passen Sie sie an Ihre speziellen Bedürfnisse an.
{% endalert %}

## Methode 1: Aus einem bestehenden Canvas erstellen

### Schritt 1: Wählen Sie Ihr vorhandenes Canvas

Gehen Sie im Braze-Dashboard zu **Messaging** > **Canvas** und wählen Sie ein bestehendes Canvas aus, das Sie als Vorlage verwenden möchten.

### Schritt 2: Template erstellen

Wählen Sie im Canvas-Editor die Option **Canvas bearbeiten** oder **Entwurf bearbeiten**, je nachdem, ob Ihr Canvas aktiv ist oder sich in einem Entwurf befindet. Erweitern Sie das Dropdown-Menü **Als Entwurf speichern** in der Fußzeile und wählen Sie **Als Vorlage speichern**.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Schritt 3: Template speichern

Als nächstes geben Sie Ihrer Vorlage einen Namen und fügen alle relevanten Tags hinzu. Wählen Sie dann **Speichern**. Ihr Template ist nun bereit für die Erstellung eines Canvas, sodass Sie bereits über die grundlegenden Einstellungen und Schritte verfügen.

## Methode 2: Erstellen über den Canvas-Vorlageneditor

### Schritt 1: Rufen Sie den Editor für Canvas-Vorlagen auf

Gehen Sie im Braze-Dashboard zu **Vorlagen** > **Canvas-Vorlagen**.

{% alert note %}
Wenn Sie die ältere Navigation verwenden, finden Sie diese Seite unter **Engagement** > **Templates & Medien** > Canvas Templates.
{% endalert %}

### Schritt 2: Eine neue Vorlage erstellen

Wählen Sie **Vorlage erstellen** und beginnen Sie mit dem Einrichten Ihrer Canvas-Details. Sie können damit beginnen, Ihrer Canvas-Vorlage einen Namen zu geben.

![Eine Canvas-Template-Beispiel mit dem Namen „Canvas-Template für jährlichen Verkauf“ mit der Beschreibung „Für die jährliche Aktion im Frühjahr verwenden“.]({% image_buster /assets/img/canvas_template_example.png %})

### Schritt 3: Template anpassen

Als nächstes passen Sie Ihr Template an, indem Sie [Ihr Canvas einrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-set-up-your-canvas). Sie können entscheiden, wann Nutzer:innen das Canvas betreten sollen, festlegen, welche Nutzer:innen dieses Canvas betreten können, Ihre Sendeeinstellungen anpassen und Ihre User Journey für das Template aufbauen.

### Schritt 4: Template speichern

Wenn Sie die Anpassung Ihrer Vorlage abgeschlossen haben, klicken Sie auf die Schaltfläche **Vorlage speichern**. Auf der Seite **Canvas-Vorlage** können Sie die Details Ihrer Canvas-Vorlage anzeigen, indem Sie <i class="fas fa-list"></i> **Vorlagendetails** wählen. 

## Canvas-Vorlagen verwenden

Es gibt zwei Möglichkeiten, Ihr Template beim Erstellen eines Canvas zu verwenden:

- **Aus Messaging**: Gehen Sie zu **Messaging** > **Canvas**. Wählen Sie die Schaltfläche **Leinwand erstellen** und **Verwenden Sie eine Leinwandvorlage**.
- **Über Templates**: Gehen Sie zu **Vorlagen** > **Canvas-Vorlagen** und suchen Sie die gewünschte Vorlage. Wählen Sie dann das Menü <i class="fas fa-ellipsis-vertical"></i>, gefolgt von **Vorlage anwenden**. Dies führt Sie zu einem neuen Canvas mit der im Canvas Composer angewendeten Vorlage.

### Verfügbare Lötvorlagen

Eine Liste der verfügbaren Canvas Templates finden Sie unter [Canvas Templates]({{site.baseurl}}/canvas_templates/templates/). Einzelheiten zur Verwendung von E-Commerce Canvas-Templates finden Sie unter [Empfohlene Ereignisse im E-Commerce verwenden]({{site.baseurl}}/ecommerce_use_cases/).

## Canvas-Vorlagen verwalten

Canvas-Vorlagen können dupliziert und archiviert werden, ähnlich wie ein echtes Canvas. Um eine Canvas-Vorlage zu bearbeiten, wählen Sie die Vorlage aus und klicken dann **auf<i class="fas fa-pencil-alt"></i>Bearbeiten**.

Auf Arbeitsbereichsebene können Sie die Benutzerrechte aktualisieren, um den Zugriff auf das Erstellen, Bearbeiten, Anzeigen oder Archivieren von Canvas-Vorlagen zu erlauben oder einzuschränken.

### Berechtigungen für Teams und Arbeitsbereiche

Um nur bestimmten Benutzern den Zugriff auf bestimmte Canvas-Vorlagen und deren Verwendung zu gestatten, [fügen Sie ein Team]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) zu den Vorlagen [hinzu]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und weisen dann auf Teamebene die Berechtigung "Zugriff auf Kampagnen, Canvases, Content Cards, Content Blocks, Feature Flags, Segmente, Mediathek und Preference Center" zu.

Wenn Sie eine der folgenden Berechtigungen auf Team-, aber nicht auf Workspace-Ebene zuweisen, können Sie nur das tun, was Ihrem Team zugewiesen ist:

- Canvas-Vorlagen erstellen und bearbeiten
- Canvas-Vorlagen ansehen
- Archivieren Sie Canvas-Vorlagen

Wenn Berechtigungen sowohl auf Workspace- als auch auf Team-Ebene erteilt werden, haben die Berechtigungen auf Workspace-Ebene Vorrang.

## Häufig gestellte Fragen

### Kann ich einen unvollständigen Schritt in einer Canvas-Vorlage speichern?

Ja, Sie können unvollständige Schritte als Canvas-Vorlage speichern. Wenn die Vorlage jedoch verwendet wird, erscheint auf der Schaltfläche **Vorlage speichern** eine Fehlermeldung, die angibt, was zum Starten des Canvas erforderlich ist.

### Kann ich meine Einstellungen für den Canvas-Builder als Vorlage speichern, oder kann ich nur Schritte speichern? 

Ja, Sie können die Einstellungen im Canvas-Builder innerhalb eines Canvas-Templates speichern. Wenn Sie beispielsweise planen, häufig eine Kombination aus Segmenten und Filtern zu verwenden, können Sie diese **Zielgruppeneinstellungen** als Teil Ihrer Canvas-Vorlage speichern.

