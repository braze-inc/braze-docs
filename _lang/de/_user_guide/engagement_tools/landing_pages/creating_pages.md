---
nav_title: Landing Pages erstellen
article_title: Landing Pages erstellen
description: "In diesem Artikel erfahren Sie, wie Sie Landing Pages von Braze mit dem Drag-and-Drop-Editor erstellen und anpassen können."
page_order: 0
---

# Landing Pages erstellen

> Lernen Sie, wie Sie eine Landing Page mit dem Drag-and-Drop-Editor erstellen und anpassen, damit Sie Ihre Zielgruppe vergrößern und Präferenzen direkt in Braze sammeln können.

## Voraussetzungen

Für den Zugriff auf den Landing Page Builder benötigen Sie [bestimmte Berechtigungen]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#prerequisites). Wenn Sie keinen Zugang haben, bitten Sie Ihren Braze-Administrator um Hilfe.

## Erstellen einer Landing Page

### Schritt 1: Einen neuen Entwurf erstellen

Gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie dann **Landing Page erstellen**. Sie können auch den Namen einer bestehenden Landing Page auswählen, um sie zu duplizieren oder zu ändern.

![Der Bereich Landing Pages im Braze-Dashboard.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Schritt 2: Geben Sie die Seitendetails ein

Fügen Sie interne und öffentliche Details hinzu, die Ihnen helfen, Ihre Landing Page zu organisieren, zu kennzeichnen und zu teilen.

#### Allgemeine Details

Geben Sie einen Namen und eine Beschreibung für die Landing Page ein. Diese Angaben werden für die Suche nach der Seite in Ihrem internen Workspace verwendet. Sie werden für Ihre Kund:innen nicht sichtbar sein.

#### Details zur Website

Richten Sie Metatags ein, um die Darstellung Ihrer Seite auf der Browser-Registerkarte anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese werden für Ihre Kunden sichtbar sein.

Wir empfehlen Ihnen, diese bewährten Verfahren zu befolgen:

| Feld | Beschreibung | Empfehlungen |
| --- | --- |
| Website-Titel | Der Titel, der auf der Browser-Registerkarte angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Meta-Beschreibung | Ein Textausschnitt, der in den Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140-160 Zeichen.|
| Favicon | Das Symbol, das neben dem Titel der Website auf dem Tab des Browsers erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| Seiten-URL | Dies ist der URL-Pfad zu Ihrer Landing Page. Dieser Wert wird auch referenziert, wenn Sie [Liquid-Tags für Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) verwenden, die Sie in eine Nachricht einbetten können, um automatisch zu erkennen, wenn Ihr Formular abgeschickt wurde.| Dieser Wert muss in Ihrem Workspace eindeutig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Die Seite anpassen

Falls Sie das noch nicht getan haben, wählen Sie **Als Entwurf speichern**. Um mit der Anpassung Ihrer Seite zu beginnen, wählen Sie **Landing Page bearbeiten**. Der Drag-and-Drop-Editor wird mit einem Standard Template vorgeladen, das Sie an Ihren Anwendungsfall anpassen können.

![Ein Beispiel für eine Landing Page, die per Drag-and-Drop-Editor erstellt wird.]({% image_buster /assets/img/landing_pages/template.png %})

Der Editor verwendet zwei Arten von Komponenten für die Gestaltung von Landing Pages: Basisblöcke und Formularblöcke. Alle Blöcke müssen in einer Reihe platziert werden.

![Der Abschnitt 'Erstellen' mit 'Zeilen' und 'Formularblöcken'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basic blocks %}

Sie können diese Blöcke verwenden, um Inhalte hinzuzufügen und das Layout Ihrer Landing Page anzupassen.

| Block Typ   | Beschreibung |
|-------------|-------------|
| Titel       | Ein Textblock zum Hinzufügen einer Überschrift oder eines Titels zu Ihrem Inhalt. Nützlich für die Strukturierung von Abschnitten und zur Verbesserung der Lesbarkeit. |
| Absatz   | Ein Textblock für längere Beschreibungen oder zusätzlichen Kontext. Unterstützt die Formatierung von Rich Text. |
| Button      | Ein anklickbares Element, das Nutzer:innen zu einer bestimmten Aktion leitet, z.B. zum Öffnen eines Links oder zum Absenden eines Formulars. |
| Radio-Button | Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen können. Bei der Übermittlung protokolliert das Nutzerprofil das zugehörige angepasste Attribut. |
| Bild       | Ein Block für die Anzeige von Bildern. Sie können ein Bild hochladen oder eine URL angeben, um auf eine externe Quelle zu referenzieren. |
| Link        | Ein Hyperlink, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in einen Text eingebettet oder eigenständig sein. |
| Spacer      | Ein unsichtbarer Block, der den vertikalen Abstand zwischen Elementen für ein besseres Layout und bessere Lesbarkeit hinzufügt. |
| Angepasster Code | Ein Block, mit dem Sie angepasstes HTML, CSS oder JavaScript einfügen und ausführen können, um Fortschritte bei der Anpassung zu erzielen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Text umspannen

{% multi_lang_include span_text.md %}

{% endtab %}
{% tab Form blocks %}

Mit diesen Blöcken können Sie ein Formular erstellen, das von Nutzern:innen übermittelte Daten mit ihrem Profil in Braze verknüpft. Denken Sie daran, dass Sie bei Verwendung von Formularblöcken auch eine zusätzliche Landing Page für den Bestätigungsstatus erstellen müssen.

![Ein Formularblock, der eine neue Kund:in registriert und einen Rabattcode an ihre E-Mail sendet.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Block Typ     | Beschreibung |
|---------------|-------------|
| E-Mail-Erfassung | Ein Formularfeld für E-Mail-Adressen. Nach der Übermittlung wird die E-Mail Adresse dem Profil des Nutzers:in in Braze hinzugefügt. |
| Erfassung von Telefonnummern | Ein Formularfeld für Telefonnummern. Nach dem Absenden ist der Nutzer:in Ihrer SMS- oder WhatsApp-Abo-Gruppe angemeldet. |
| Eingabefeld   | Ein Formularfeld, das Standardattribute (z.B. Vor- und Nachname) oder einen angepassten Attribut String Ihrer Wahl unterstützt. |
| Dropdown      | Nutzer:innen können einen Artikel aus einer vordefinierten Liste auswählen. Sie können der Liste beliebige angepasste Attribute Strings hinzufügen. |
| Kontrollkästchen      | Wenn ein Nutzer:innen das Kästchen markiert, wird das Attribut des Blocks auf `true` gesetzt. Wenn es nicht markiert ist, wird sein Attribut auf `false` gesetzt. |
| Kontrollkästchen-Gruppe| Nutzer:innen können aus mehreren angebotenen Möglichkeiten auswählen. Die Werte werden entweder festgelegt oder zu einem definierten Array angepasster Attribute hinzugefügt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Nachdem Sie eine Landing Page mit einem Formular erstellt haben, sollten Sie den [Liquid-Tag der Landing Page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) in Ihre Nachricht einbetten. Mit diesem Tag kann Braze bestehende Nutzer:innen-Profile automatisch identifizieren und aktualisieren, wenn sie das Formular abschicken.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Stile für Seitencontainer

Auf dem Tab **Seitencontainer** können Sie Stile festlegen, die auf alle relevanten Komponentenblöcke Ihrer Landing Page angewendet werden. Diese Stile werden überall auf Ihrer Seite verwendet, es sei denn, Sie setzen sie mit einem bestimmten Block außer Kraft.

Wir empfehlen, die Stile auf der Ebene der Seitencontainer einzurichten, bevor Sie die Stile auf der Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Abschnitt 'Seitencontainer' mit Optionen zum Anpassen von Hintergrundbildern, Farben, Rahmendetails und der Gestaltung des Inhalts.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsiv auf Nutzer:innen-Geräte

Sie können Ihre Landing Page responsiv an die Größe des Geräts eines Nutzers:innen anpassen, indem Sie die Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie eine Spalte in die Zeile ein, die responsiv sein soll, und schalten Sie dann im Bereich **Spalten anpassen** die Option **Vertikal stapeln auf kleineren Bildschirmen** um.

Wenn dieses Enablement aktiviert ist, können Sie auch die Stapelspalten umkehren, um die vertikale Reihenfolge von mehrspaltigen Inhalten auf kleineren Bildschirmen zu steuern. Dadurch sehen die Seiten auf dem Handy besser aus und fühlen sich besser an, ohne angepassten Code.

![Das Umschalten von "Vertikal stapeln auf kleineren Bildschirmen" in der Sektion "Spalten anpassen".]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Optionale und obligatorische Felder

Sie können wählen, ob ein Formularfeld erforderlich oder optional ist. Erforderliche Felder müssen ausgefüllt werden, bevor das Formular abgeschickt werden kann. Optionale Felder können leer bleiben oder von einem Nutzer:innen nicht ausgewählt werden.

Um beispielsweise die Erfassung von Einwilligungen vor dem Absenden des Formulars zu erzwingen, können Sie die Option **Erforderliche Feldeingabe** aktivieren, um ein Kontrollkästchen mit dem entsprechenden Disclaimer-Text als erforderlich zu definieren.

![Ein Formularfeld mit Kontrollkästchen, bei dem die Option "Erforderliches Eingabefeld" umgeschaltet wurde.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Schritt 4: Erstellen Sie eine Bestätigungsseite (optional)

Wenn Ihre Landing Page kein Formular enthält, fahren Sie mit dem nächsten Schritt fort.

Wenn Ihre Landing Page ein [Formular](#form-blocks) enthält, erstellen Sie eine zweite Landing Page, die als Bestätigungsseite dient. Diese Seite sollte sich bei den Nutzer:innen bedanken oder einen nächsten Schritt nach dem Absenden des Formulars anbieten.

Um die Bestätigungsseite zu verlinken:
- Wählen Sie den Button **Absenden** in Ihrem Formular aus
- Verwenden Sie die Aktion **Internet-URL öffnen**, um einen Link zu Ihrer Bestätigungsseite zu erstellen.

Wenn Sie keine Bestätigungsseite einfügen, wissen die Nutzer:innen möglicherweise nicht, dass ihr Formular erfolgreich abgeschickt wurde. Fügen Sie immer ein Bestätigungserlebnis hinzu, um die Reise abzuschließen.

{% alert note %}
Wenn Ihre Bestätigungsseite in einem neuen Tab geöffnet wird, kann ein Nutzer:innen, der zur ursprünglichen Landing Page zurückkehrt und eine erneute Anmeldung mit aktualisierten Daten vornimmt, die vorherige Anmeldung überschreiben, was zu inkonsistenten Daten führt.
{% endalert %}

### Schritt 5: Vorschau auf die Seite

Auf der Registerkarte **Vorschau** des Editors können Sie eine Vorschau Ihrer Landing Page anzeigen. Nachdem Sie Ihre Landing Page als Entwurf gespeichert haben, können Sie die URL aufrufen, indem Sie zu **Landing Pages** gehen und **URL kopieren** neben Ihrer Landing Page wählen. Sie können die URL auch mit anderen Personen teilen.

![Eine Landing Page, bei der das Menü geöffnet ist, um die Option "URL kopieren" anzuzeigen.]({% image_buster /assets/img/landing_pages/copy-url.png %})

Vergewissern Sie sich, bevor Sie veröffentlichen:

- Sie haben das Limit der veröffentlichten Landing Page Ihres Plans nicht überschritten
- Jede formularbasierte Seite ist mit einer [Bestätigungsseite](#step-4-create-a-confirmation-page) verlinkt, die die Aktion **Internet-URL öffnen** verwendet
- Alle erforderlichen Seitenfelder (wie URL-Pfad und Titel) sind ausgefüllt

Wenn Sie bereit sind, wählen Sie **Landing Page veröffentlichen**.

## Templates verwenden

Verwenden Sie Landing Page Templates, um Vorlagen für Ihre nächsten Kampagnen zu erstellen. Diese Templates können sowohl im Landing Page Editor als auch im Bereich **Templates** des Dashboards**(Templates** > **Landing Page Templates**) aufgerufen und verwaltet werden. Landing Page Templates benötigen einen Namen und optional eine Beschreibung. 

## Vorlagen verwalten

Sie können Landing Page Templates in der Vorschau anzeigen, archivieren, bearbeiten oder duplizieren. Wenn Sie eine Landing Page bearbeiten, können Sie Ihre Landing Page auch als Template speichern, Änderungen an dem Template vornehmen oder den Inhalt der Landing Page löschen. 

![Ein Dropdown-Menü mit Optionen zum Speichern, Ändern und Löschen einer Landing Page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Analytik anzeigen

Um die Effektivität Ihrer Landing Page zu analysieren, gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie dann eine Landing Page aus, die Sie veröffentlicht haben. Hier können Sie die Anzahl der Seitenaufrufe, Seitenklicks, Seitenübermittlungen und die Übermittlungsraten für Ihre Landing Page verfolgen.

![Der Analytics-Bereich für eine Landing Page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Behandlung von Fehlern bei der Formularübermittlung {#handling-form-submission-errors}

Wenn ein Nutzer:innen versucht, ein Formular mit fehlenden oder nicht unterstützten Eingaben abzuschicken, wird eine allgemeine Fehlermeldung angezeigt und das Formular kann nicht abgeschickt werden.

Häufige Ursachen:

- Erforderliche Felder sind leer gelassen
- Sonderzeichen werden in Texteingaben verwendet
- Ein erforderliches Kontrollkästchen ist nicht ausgewählt

Fehlermeldungen, die den Nutzer:innen angezeigt werden, können nicht angepasst werden. Zeigen Sie eine Vorschau Ihrer Landing Page an, um das Verhalten der Felder vor der Veröffentlichung zu bestätigen. 
