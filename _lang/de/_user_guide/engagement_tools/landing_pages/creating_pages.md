---
nav_title: Landing Pages erstellen
article_title: Landing Pages erstellen
description: "In diesem Artikel erfahren Sie, wie Sie Landing Pages von Braze mit dem Drag-and-Drop-Editor erstellen und anpassen können."
page_order: 0
---

# Landing Pages erstellen

> Lernen Sie, wie Sie eine Landing Page mit dem Drag-and-Drop-Editor erstellen und anpassen, damit Sie Ihre Zielgruppe vergrößern und Präferenzen direkt in Braze sammeln können.

## Erstellen einer Landing Page

### Schritt 1: Einen neuen Entwurf erstellen

Gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie dann **Landing Page erstellen**. Sie können auch auf den Namen einer bestehenden Landing Page klicken, um sie zu duplizieren oder zu ändern.

![Der Bereich Landing Pages im Braze-Dashboard.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Schritt 2: Geben Sie die Seitendetails ein

#### Allgemeine Details

Der Name und die Beschreibung der Zielseite werden für die Suche nach der Seite in Ihrem internen Arbeitsbereich verwendet. Diese werden für Ihre Kunden nicht sichtbar sein.

#### Details zur Website

Richten Sie Metatags ein, um die Darstellung Ihrer Seite auf der Browser-Registerkarte anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese werden für Ihre Kunden sichtbar sein.

Wir empfehlen Ihnen, diese bewährten Verfahren zu befolgen:

| Detail | Beschreibung | Empfehlungen |
| --- | --- |
| Website-Titel | Der Titel, der auf der Browser-Registerkarte angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Meta-Beschreibung | Ein Textausschnitt, der in den Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140-160 Zeichen.|
| Favicon | Das Symbol, das neben dem Titel der Website auf dem Tab des Browsers erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| Seiten-URL | Dies ist der URL-Pfad zu Ihrer Landing Page. Dieser Wert wird auch referenziert, wenn Sie [Liquid-Tags für Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) verwenden, die Sie in eine Nachricht einbetten können, um automatisch zu erkennen, wenn Ihr Formular abgeschickt wurde.| Dieser Wert muss in Ihrem Workspace eindeutig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Die Seite anpassen

Falls Sie das noch nicht getan haben, wählen Sie **Als Entwurf speichern**. Um mit der Anpassung Ihrer Seite zu beginnen, wählen Sie **Landing Page bearbeiten**. Der Drag-and-Drop-Editor wird mit einem Standard Template vorgeladen, das Sie an Ihren Anwendungsfall anpassen können.

![Ein Beispiel für eine Landing Page, die im Drag-and-Drop-Editor erstellt wird.]({% image_buster /assets/img/landing_pages/template.png %})

Der Editor verwendet zwei Arten von Komponenten für die Gestaltung von Landing Pages: [Basisblöcke](#basic-blocks) und [Formularblöcke](#form-blocks). Alle Blöcke müssen in einer Reihe platziert werden.

![Der Bereich 'Bauen' mit 'Zeilen' und 'Formularblöcken'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Grundlegende Blöcke

Sie können diese Blöcke verwenden, um Inhalte hinzuzufügen und das Layout Ihrer Landing Page anzupassen.

| Block Typ   | Beschreibung |
|-------------|-------------|
| Titel       | Ein Textblock zum Hinzufügen einer Überschrift oder eines Titels zu Ihrem Inhalt. Nützlich für die Strukturierung von Abschnitten und zur Verbesserung der Lesbarkeit. |
| Absatz   | Ein Textblock für längere Beschreibungen oder zusätzlichen Kontext. Unterstützt die Formatierung von Rich Text. |
| Button      | Ein anklickbares Element, das Nutzer:innen zu einer bestimmten Aktion leitet, z.B. zum Öffnen eines Links oder zum Absenden eines Formulars. |
| Bild       | Ein Block für die Anzeige von Bildern. Sie können ein Bild hochladen oder eine URL angeben, um auf eine externe Quelle zu referenzieren. |
| Link        | Ein Hyperlink, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in einen Text eingebettet oder eigenständig sein. |
| Spacer      | Ein unsichtbarer Block, der den vertikalen Abstand zwischen Elementen für ein besseres Layout und bessere Lesbarkeit hinzufügt. |
| Angepasster Code | Ein Block, mit dem Sie angepasstes HTML, CSS oder JavaScript einfügen und ausführen können, um Fortschritte bei der Anpassung zu erzielen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Blöcke formen

Mit diesen Blöcken können Sie ein Formular erstellen, das von Nutzern:innen übermittelte Daten mit ihrem Profil in Braze verknüpft. Denken Sie daran, dass Sie bei Verwendung von Formularblöcken auch eine zusätzliche Landing Page für den Bestätigungsstatus erstellen müssen.

![Ein Formularblock, der eine neue Kund:in registriert und einen Rabattcode an ihre E-Mail sendet.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Block Typ     | Beschreibung |
|---------------|-------------|
| E-Mail-Erfassung | Ein Formularfeld für E-Mail-Adressen. Nach der Übermittlung wird die E-Mail Adresse dem Profil des Nutzers:in in Braze hinzugefügt. |
| Erfassung von Telefonnummern | Ein Formularfeld für Telefonnummern. Nach dem Absenden ist der Nutzer:in Ihrer SMS- oder Whatsapp-Abo-Gruppe angemeldet. |
| Eingabefeld   | Ein Formularfeld, das Standardattribute (z.B. Vor- und Nachname) oder einen angepassten Attribut String Ihrer Wahl unterstützt. |
| Dropdown      | Nutzer:innen können einen Artikel aus einer vordefinierten Liste auswählen. Sie können der Liste beliebige angepasste Attribute Strings hinzufügen. |
| Kontrollkästchen      | Wenn ein Nutzer:innen das Kästchen markiert, wird das Attribut des Blocks auf `true` gesetzt. Wenn es nicht markiert ist, wird sein Attribut auf `false` gesetzt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Nachdem Sie eine Landing Page mit einem Formular erstellt haben, sollten Sie den [Liquid-Tag]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) der Landing Page in Ihre Nachricht einbetten. Mit diesem Tag kann Braze bestehende Nutzer:innen-Profile automatisch identifizieren und aktualisieren, wenn sie das Formular abschicken.
{% endalert %}

#### Stile für Seitencontainer

Auf der Registerkarte **Seitencontainer** können Sie Stile festlegen, die auf alle relevanten Komponentenblöcke in Ihrer Landing Page angewendet werden. Diese Stile werden überall auf Ihrer Seite verwendet, es sei denn, Sie setzen sie mit einem bestimmten Block außer Kraft.

Wir empfehlen, die Stile auf der Ebene der Seitencontainer einzurichten, bevor Sie die Stile auf der Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Bereich 'Seitencontainer' mit Optionen zum Anpassen von Hintergrundbildern, Farben, Rahmendetails und der Gestaltung des Inhalts.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Schritt 4: Erstellen Sie eine Bestätigungsseite

Wenn Sie im vorherigen Schritt ein [Formular](#form-block) zu Ihrer Landing Page hinzugefügt haben, erstellen Sie eine zusätzliche Landing Page für den Bestätigungsstatus und fügen Sie dann den Link **Internet-URL öffnen** zu dem Button hinzu, der das Formular absendet. Andernfalls fahren Sie mit dem nächsten Schritt fort.

### Schritt 5: Vorschau auf die Seite

Auf der Registerkarte **Vorschau** des Editors können Sie eine Vorschau Ihrer Landing Page anzeigen. Nachdem Sie Ihre Landing Page als Entwurf gespeichert haben, können Sie die URL aufrufen, indem Sie zu **Landing Pages** gehen und **URL kopieren** neben Ihrer Landing Page wählen. Sie können die URL auch mit anderen Personen teilen.

![Eine Landing Page mit geöffnetem Menü, das die Option "URL kopieren" anzeigt.]({% image_buster /assets/img/landing_pages/copy-url.png %})

Wenn Sie bereit sind, wählen Sie **Landing Page veröffentlichen**.

## Behandlung von Fehlern bei der Formularübermittlung

Wenn ein Benutzer einen ungültigen Formularwert eingibt (z.B. nicht akzeptierte Sonderzeichen), wird eine allgemeine Fehlermeldung angezeigt, die nicht angepasst werden kann, und er kann das Formular nicht abschicken. Sie können das Fehlerverhalten in der Vorschau der Landing Page sehen.

## Analytik anzeigen

Um die Effektivität Ihrer Landing Page zu analysieren, gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie dann eine Landing Page aus, die Sie veröffentlicht haben. Hier können Sie die Anzahl der Seitenaufrufe, Seitenklicks, Seitenübermittlungen und die Übermittlungsraten für Ihre Landing Page verfolgen.

![Der Analytics-Bereich für eine Landing Page.]({% image_buster /assets/img/landing_pages/analytics.png %})
