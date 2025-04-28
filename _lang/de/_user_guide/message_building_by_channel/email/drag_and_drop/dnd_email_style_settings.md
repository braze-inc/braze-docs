---
nav_title: Globale Stileinstellungen für E-Mails
article_title: Globale Stileinstellungen für E-Mails
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie im Drag-and-Drop-Editor globale E-Mail-Stil-Einstellungen für Ihre Kampagnen und Canvases festlegen."
tool: 
  - Campaigns
  - Canvas
---

# Globale E-Mail-Stil-Einstellungen

> Mit den globalen Stil-Einstellungen können Sie das Aussehen Ihrer E-Mail-Kampagnen und Canvases individuell gestalten. Sie können ein Standardthema für Ihren Drag-and-Drop-Editor hinzufügen und anpassen. Dazu gehört die Bearbeitung Ihrer Stile für E-Mail-Titel, Text, Buttons und vieles mehr. Mit einer Kombination dieser Einstellungen können Sie ein einheitliches Erscheinungsbild für Ihre E-Mail-Nachrichten schaffen.

Um Ihre globalen Stileinstellungen zu bearbeiten, gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen** > **Drag-and-Drop-E-Mail-Voreinstellungen**. Nachdem Sie die Stile im Drag-and-Drop-E-Mail-Editor bearbeitet haben, klicken Sie auf **Speichern**. Um Ihre E-Mail-Kampagnen und Canvase weiter anzupassen, sehen Sie sich an, wie Sie [Drag-and-Drop-Editor-Blöcke][8] einbinden können.

![][1]

{% alert note %}
Aktualisierungen der globalen Stileinstellungen werden für alle zukünftigen E-Mail-Kampagnen und Canvases übernommen.
{% endalert %} 

## Standard-Stil 

Für **Basic Styling** können Sie Ihre Standardfarben für den Hintergrund von E-Mails und Inhalten für Ihre E-Mail-Kampagnen und Canvases festlegen. Sie können auch eine Standardschriftart auswählen, eine benutzerdefinierte Schriftart hinzufügen und Linkfarben bearbeiten.

![Standard-Stil-Optionen, die Optionen zur Bearbeitung der Hintergrundfarben für E-Mails und Inhalte, des Standard-Schriftnamens und der Standard-Linkfarbe umfassen.][2] 

## Eigene Schriftart

Mit benutzerdefinierten Schriftarten können Sie manuell eine Web-Schriftart hinzufügen, um ein einheitliches Branding auf verschiedenen E-Mail-Plattformen zu gewährleisten. Sie können eine benutzerdefinierte Schriftart pro Abschnitt hinzufügen. 

Bevor Sie eine angepasste Schriftart hinzufügen, überprüfen Sie, ob die angepasste Schriftartdatei die folgenden Anforderungen erfüllt:

- CORS muss auf dem Server, der die benutzerdefinierte Schriftartdatei bereitstellt, aktiviert sein. Dies wird normalerweise von Ihrem IT-Team verwaltet. 
  - Die benutzerdefinierte Schriftartdatei muss die Kopfzeile enthalten: `Access-Control-Allow-Origin: *`
- Die Datei-URL muss auf eine CSS-Datei verweisen (nicht WOFF, OTF usw.)
- Der Name der benutzerdefinierten Schrift muss mit dem Namen der Schriftart in der CSS-Datei übereinstimmen

Um eine benutzerdefinierte Schriftart hinzuzufügen:

1. Klicken Sie auf **Benutzerdefinierte Schriftart hinzufügen** unter dem **Namen der Standardschriftart** im Bereich Styling.
2. Geben Sie in das Feld **Schriftname** denselben Schriftnamen ein, der in der Quelldatei Ihrer benutzerdefinierten Schrift erscheint. Achten Sie darauf, dass der Name in Großbuchstaben und mit korrekten Abständen geschrieben wird. 
3. Geben Sie die entsprechende URL in das Feld **Schrift-URL** ein.
4. Vergewissern Sie sich vor dem Speichern, dass die Vorschau Ihre benutzerdefinierte Schrift anzeigt. 
5. Klicken Sie auf **Speichern**, um die benutzerdefinierte Schriftart als Standard-E-Mail-Schriftart zu verwenden. 

{% alert important %}
Google Mail unterstützt keine angepassten Schriftarten, sodass Ihre angepasste Schriftart möglicherweise als Standard-Systemschriftart angezeigt wird. Prüfen Sie bei anderen E-Mail-Plattformen, ob Ihre benutzerdefinierte Schriftart korrekt angezeigt wird, bevor Sie Ihre E-Mail-Nachrichten versenden.
{% endalert %}

Bitte beachten Sie, dass der Anbieter der benutzerdefinierten Schriftart persönliche Daten von Ihren Empfängern erfassen kann. Sie sollten die Richtlinien Ihres Schriftartenanbieters vor der Verwendung überprüfen.

Um alternative benutzerdefinierte Schriftarten in Ihren E-Mail-Kampagnen zu verwenden, haben Sie die Möglichkeit, eine [E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) oder [Inhaltsblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) zu erstellen. Vergewissern Sie sich, dass die von Ihnen gewählte Schriftart noch websicher ist und von Ihren E-Mail-Plattformen unterstützt wird. 

### Fallback-Schriftart

Fallback-Schriften werden für den Titel, die Kopfzeile und den Textkörper verwendet, wenn Ihre Standardschriftart vom Posteingangsanbieter oder dem Betriebssystem nicht unterstützt wird. Standardmäßig stellt Braze automatisch Arial als Ausweichschriftart ein, wenn die globalen Stileinstellungen gespeichert werden. Sie haben auch die Möglichkeit, Serif oder Sans Serif als Optionen für Ihre Standardschriftart-Familie hinzuzufügen.

![][11]

Sie können bis zu 17 Fallback-Schriften hinzufügen. Die zuerst gewählte Ausweichschriftart wird als erste ausprobiert. Die Fallback-Schriftart wird nur für neu erstellte Vorlagen, E-Mail-Kampagnen und Canvas-Komponenten verwendet. Die Ersatzschriftart wird nicht automatisch für Nachrichten gesetzt, die erstellt wurden, bevor die Ersatzschriftart festgelegt wurde. Wir empfehlen Ihnen dringend, Fallback-Schriftarten zu wählen, die Ihrem E-Mail-Messaging ähneln, um die Konsistenz Ihres Markenauftritts zu gewährleisten.

## Titel Styling

Hier können Sie den Stil Ihrer E-Mail-Titel anpassen, indem Sie die Schriftgröße, die Schriftfarbe und die Textausrichtung bearbeiten. Dies gilt für die Hauptkopfzeile und die Nebenkopfzeile. 

![][9]

Optional können Sie den Standardstil Ihres Drag-and-Drop-Editor-Designs überschreiben. Klicken Sie auf **Standardstil überschreiben**, um das von Ihnen gewählte Titeldesign anzuwenden. Dazu kann die Einstellung einer anderen Schriftart und Linkfarbe gehören.

## Absatz-Styling

Um einen Standard-Absatzstil festzulegen, gehen Sie zur **Absatzgestaltung**, geben Sie den **Schriftgrad** ein und wählen Sie **Schriftfarbe**, um eine Schriftfarbe auszuwählen. Sie können auch das Blockstyling für den Textkörper anpassen, indem Sie die Werte **Auffüllen oben**, **Auffüllen rechts**, **Auffüllen unten** und **Auffüllen links** bearbeiten. Dies gilt für die Abstände in allen vier Bereichen, die den Absatzblock umgeben.

![][7]

## Listen-Stil

Wenn Sie Listen zu Ihren Nachrichten hinzufügen, sorgt der Abschnitt **Listengestaltung** für eine einheitliche Gestaltung Ihrer Listen. Dazu gehören Details wie: 

- Schriftgröße
- Schriftfarbe
- Schriftschnitt
- Zeilenhöhe
- Ausrichtung
- Textrichtung
- Buchstabenabstand
- Abstand zwischen den Listenelementen
- Einzug für Listenelemente
- Listentyp
- Listenstil-Typ

Sie können den **Listentyp** entweder als nummeriert oder als Aufzählungszeichen festlegen. Der **Listenstiltyp** bietet zusätzliche Anpassungsmöglichkeiten für den Stil Ihrer Listen. Sie können z.B. festlegen, dass die Aufzählungstypen immer mit Aufzählungszeichen versehen sind und dass jedes Aufzählungszeichen ein Quadrat ist.  

![][10]

## Button-Stil

Im Bereich **Gestaltung der Schaltfläche** können Sie die folgenden Standardstile für die Schaltfläche bearbeiten:
- Hintergrundfarbe
- Schriftgröße
- Schriftfarbe
- Rahmenradius
- Rahmenfarbe
- Rahmenstärke
- Padding-Button

![][12]

Wie bei allen anderen Styling-Abschnitten können Sie das Block-Styling anpassen, indem Sie die Werte **Padding Top**, **Padding Right**, **Padding Bottom** und **Padding Left** bearbeiten.

## Breite der E-Mail-Vorlage

Mit der Breite der E-Mail-Vorlage können Sie eine Breite für die Konsistenz Ihrer E-Mail-Kampagnen festlegen und anpassen. 

![][13]

## Content-Block-Breite

Sie können die Breite des Inhaltsblocks auch im Drag-and-Drop-Editor für E-Mails festlegen. Wir empfehlen, die Breite des Content-Blocks an die Breite der E-Mail-Template anzupassen.

![][14]


[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[13]: {% image_buster /assets/img_archive/dnd_email_template_width.png %}
[14]: {% image_buster /assets/img_archive/dnd_content_block_width.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks
