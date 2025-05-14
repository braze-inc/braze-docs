---
nav_title: E-Mail erstellen
article_title: Erstellen einer E-Mail per Drag-and-Drop
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "In diesem Artikel erfahren Sie, wie Sie den Drag-and-Drop-Editor für E-Mail-Nachrichten einrichten und richtig verwenden."
tool:
- Campaigns
- Canvas
---

# E-Mail per Drag-and-Drop erstellen

> Mit dem Drag-and-Drop-Editor können Sie vollständig benutzerdefinierte und personalisierte E-Mail-Nachrichten für Kampagnen oder Canvases erstellen, ohne HTML für den Aufbau Ihres E-Mail-Textes zu verwenden.

## Der Editor

Der Drag-and-Drop-Editor verwendet [Inhalt](#content) und [Zeilen](#rows) als die beiden Hauptkomponenten, um Ihren Arbeitsablauf zu vereinfachen, ohne dass Sie zusätzlich HTML verwenden müssen.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Content</th>
        <th style="width: 50%;">Zeilen</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="Der Tab &apos;Zeilen&apos;, der verschiedene Strukturkombinationen für Ihr E-Mail-Layout enthält." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="Der Tab &apos;Inhalt&apos;, der Basisblöcke, Medien und erweiterte Blöcke enthält" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### Content

**Inhalt** enthält Kacheln, die verschiedene Arten von Inhalten darstellen, die Sie in Ihrer Nachricht verwenden können. Diese sind in drei Kategorien unterteilt: Grundlagen, Medien und Fortgeschrittene. 

{% tabs %}
{% tab Basic %}

Die Basisblöcke sind das Fundament Ihrer E-Mail. Mit diesen Blöcken können Sie jedes der folgenden Elemente in den Text Ihrer E-Mail einfügen:

- Titel
- Absatz
- Liste
- Button
- Trennlinie
- Spacer

{% endtab %}
{% tab Media %}

Mit Medienblöcken können Sie verschiedene visuelle Inhalte wie Bilder, Videos, Symbole und Links für soziale Medien und anpassbare Symbole hinzufügen.

{% endtab %}
{% tab Erweitert %}

Obwohl der Drag-and-Drop-Editor Ihren Arbeitsablauf mit diesen Blöcken vereinfacht, können Sie auch vorgebrachte Blöcke verwenden, um HTML einzufügen oder ein Menü in den Text Ihrer E-Mail einzufügen. Beachten Sie, dass die Verwendung Ihres eigenen HTML-Code die Darstellung der Nachricht beeinflussen kann.

{% endtab %}
{% endtabs %}

### Zeilen

**Zeilen** sind Struktureinheiten, die den horizontalen Aufbau eines Abschnitts der Nachricht mit Hilfe von Spalten definieren. Sie können entweder Zeilen oder [Inhaltsblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) leeren. Wenn Sie mehr als eine Spalte verwenden, können Sie verschiedene Inhaltselemente nebeneinander platzieren. Auf diese Weise können Sie alle Strukturelemente, die Sie benötigen, in Ihre Nachricht einfügen – unabhängig von der Vorlage, die Sie zu Beginn ausgewählt haben.

## Verwenden des Drag-and-Drop-Editors

Sie sind sich nicht sicher, ob Ihre E-Mail-Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

Wenn Sie entschieden haben, wo Sie die Nachricht verfassen möchten, können Sie Ihre E-Mail per Drag-and-Drop erstellen.

### Schritt 1: Wählen Sie Ihre Vorlage

Wenn Sie den Drag-and-Drop-Editor als Bearbeitungsmethode ausgewählt haben, haben Sie die Wahl:

- Beginnen Sie mit einer leeren Vorlage.
- Verwenden Sie eine vorgefertigte Braze Drag-and-Drop-E-Mail-Vorlage.
- Verwenden Sie eine gespeicherte Drag-and-Drop-E-Mail-Vorlage.

{% alert note %}
Wenn Sie eine vorhandene benutzerdefinierte HTML-Vorlage oder eine von einem Drittanbieter erstellte Vorlage verwenden möchten, müssen Sie die Vorlage neu erstellen, indem Sie zu **Vorlagen** > **E-Mail-Vorlagen** gehen und den **Drag-and-Drop-Editor** als Bearbeitungsmethode auswählen.
{% endalert %}

Sie können auf alle Vorlagen auch über den Bereich **Vorlagen** zugreifen.

Nachdem Sie Ihre Vorlage ausgewählt haben, sehen Sie unter **E-Mail-Varianten** eine Übersicht über Ihre E-Mail, die die Versandinformationen und den E-Mail-Text enthält. 

Wählen Sie dann **E-Mail-Text bearbeiten**, um mit der Gestaltung der E-Mail-Struktur im Drag-and-Drop-Editor zu beginnen. 

![Der Abschnitt "E-Mail-Varianten" mit einem Beispiel für einen E-Mail-Text.][8]

### Schritt 2: E-Mail erstellen

Die Drag-and-Drop-Bearbeitung ist in drei Bereiche unterteilt: **Sendeeinstellungen**, **Inhalt** und **Vorschau & Test**. Die eigentliche Arbeit an Ihrem E-Mail-Text geschieht im Bereich **Inhalt**. Bevor Sie Ihre E-Mail erstellen, sollten Sie sich über die wichtigsten Komponenten im Klaren sein, die bei der Erstellung Ihrer E-Mail eine Rolle spielen. Näheres finden Sie unter [Der Editor](#about-the-editor).

Wenn Sie fertig sind, können Sie mit den Content-Blöcken per Drag-and-Drop Ihre E-Mail erstellen.

1. Wählen Sie das Panel **Zeilen**. Ziehen Sie die Zeilenkonfigurationen per Drag & Drop in den Haupteditor. Damit wird das Layout Ihres E-Mail-Inhalts abgebildet.
- Beachten Sie, dass neue Konfigurationen an den oberen oder unteren Rand eines bestehenden Abschnitts gezogen werden müssen.
- Wenn Sie eine Zeilenkonfiguration auswählen, werden die Einstellungen für **die Zeileneigenschaften** angezeigt, mit denen Sie weitere Anpassungen für Hintergrundfarben, Bilder und benutzerdefinierte Spaltengrößen vornehmen können.
2. Wählen Sie das Bedienfeld **Inhalt**. Ziehen Sie die gewünschten Inhaltskacheln per Drag-and-Drop auf die Zeilenkomponenten.
- Sie können auch eine der **Inhaltskacheln** in den Haupteditor ziehen. Dadurch wird eine Zeile für die Kachel erstellt.
- Sie können die Kachel weiter verfeinern, indem Sie sie auswählen und die Felder unter **Inhaltseigenschaften** und **Blockoptionen** anpassen. Dazu gehört die Bearbeitung von Buchstabenabständen, Auffüllungen, Zeilenhöhe und mehr.

Unter [Weitere Anpassungen](#other-customizations) finden Sie weitere Möglichkeiten zur Anpassung Ihrer Drag-and-Drop-E-Mail.

Während Sie Ihre E-Mail erstellen, können Sie zwischen einer Desktop- und einer mobilen Ansicht hin- und herschalten, um zu sehen, wie Ihre E-Mail-Nachrichten für Ihre Benutzergruppen aussehen werden. So können Sie überprüfen, ob Ihre Inhalte responsiv sind und können ggf. Anpassungen vornehmen.

{% alert tip %}
Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein und die KI generiert menschenähnliche Marketingtexte für Ihre Werbebotschaften.

![Copywriter-Button im Content-Panel neben den Stileinstellungen im Drag-and-Drop-Editor.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Schritt 3: Sendeinformationen hinzufügen

Sobald Sie Ihre E-Mail-Nachricht entworfen und erstellt haben, können Sie im Bereich **Sendeeinstellungen** Ihre Sendeinformationen hinzufügen.

1. Wählen Sie unter **Sende-Info** eine E-Mail als **Absender-Anzeigename + Adresse**. Sie können dies auch anpassen, indem Sie **Anpassen aus Anzeigename + Adresse** wählen.
2. Wählen Sie eine E-Mail als **Reply-To Adresse**. Sie können sie anpassen, wenn Sie auf **Antwortadresse anpassen** gehen.
3. Wählen Sie dann eine E-Mail als **BCC-Adresse**, damit Ihre E-Mail für diese Adresse sichtbar ist.
4. Fügen Sie eine Betreffzeile zu Ihrer E-Mail hinzu. Optional können Sie auch einen Preheader und ein Leerzeichen nach dem Preheader hinzufügen.

Im rechten Panel wird eine Vorschau mit Ihren Sendeinformationen eingeblendet. Diese Informationen können auch aktualisiert werden, indem Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Sendekonfiguration** navigieren.

#### Personalisierung Ihrer E-Mail-Kopfzeile (fortgeschritten)

Unter **Sendeeinstellungen** können Sie Personalisierungen für E-Mail-Kopfzeilen und E-Mail-Extras hinzufügen, mit denen Sie zusätzliche Daten an andere E-Mail-Dienstanbieter zurücksenden können. Die Personalisierung einer E-Mail-Kopfzeile, wie z.B. die Aufnahme des Namens des Empfängers, kann ebenfalls dazu beitragen, dass Ihre E-Mail mit größerer Wahrscheinlichkeit geöffnet wird.

{% alert note %}
Die erweiterten Funktionen werden im Kampagnen- oder Canvas-Composer angezeigt. In der erweiterten Funktionalität können Sie Ihre Inline-CSS-Einstellung ändern und eine Kopfzeile oder zusätzliche Schlüssel-Wert-Paare eingeben (falls konfiguriert).
{% endalert %}

### Schritt 4: E-Mail ausprobieren

Wenn Sie die Versandinformationen ergänzt haben, ist es an der Zeit, Ihre E-Mail endlich zu testen. 

Gehen Sie zum Bereich **Vorschau und Test**. Hier haben Sie die Möglichkeit, Ihre E-Mail als Nutzer:innen in der Vorschau zu betrachten oder eine Nachricht zum Testen zu versenden. In diesem Bereich finden Sie auch die Funktion [Posteingangssicht]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), mit der Sie überprüfen können, ob Ihre E-Mails in verschiedenen mobilen und Web-Clients korrekt dargestellt werden.

{% alert tip %}
Sie können auch den Schalter für die **Vorschau im dunklen Modus** im Vorschaufenster verwenden, um Ihren E-Mail-Text im dunklen Modus anzuzeigen und Ihre E-Mail nach Bedarf anzupassen.
{% endalert %}

Da Sie drei verschiedene Versionen derselben E-Mail im Editor, in Inbox Vision und als Test-E-Mail anzeigen können, sollten Sie die Details auf allen Plattformen angleichen.

#### Vorschau und Testversand
 
Auf der Registerkarte **Vorschau als Benutzer** können Sie die folgenden Benutzertypen für die Vorschau Ihrer Nachricht auswählen.

- **Zufälliger Benutzer:** Braze wählt nach dem Zufallsprinzip einen Benutzer aus der Datenbank aus und erstellt eine Vorschau der E-Mail auf der Grundlage seiner Attribute oder Ereignisinformationen.
- **Nutzerauswahl:** Sie können einen bestimmten Benutzer anhand seiner E-Mail-Adresse oder seiner externen ID auswählen. Die Vorschau der E-Mail basiert auf Nutzerattributen und Ereignisinformationen.
- **Angepasste Nutzer:innen:** Sie können einen Benutzer individuell anpassen. Braze wird Eingaben für alle verfügbaren Attribute und Ereignisse anbieten. Sie können alle Informationen eingeben, die Sie in der Vorschau-E-Mail sehen möchten.

{% alert note %}
Der zufällige Nutzer:innen kann Teil Ihrer Segmentierungskriterien sein oder auch nicht. Die Segmentierung wird im Nachhinein ausgewählt, so dass Braze Ihre Zielgruppe zu diesem Zeitpunkt noch nicht kennt.
{% endalert %}

#### Verwenden Sie Inbox Vision

Mit Inbox Vision können Sie E-Mail Kampagnen aus der Perspektive von E-Mail Clients und Mobilgeräten betrachten. Um Ihre E-Mail-Nachricht mit Inbox Vision zu testen, wählen Sie **Inbox Vision** im Bereich **Vorschau & Test** und wählen Sie **Inbox Vision ausführen**.

{% alert tip %}
Hintergrundbilder in E-Mail-Nachrichten können manchmal dazu führen, dass weiße Linien oder Unterbrechungen zwischen den Bildern erscheinen. Daher ist es wichtig, die Feinheiten Ihrer E-Mail-Nachricht zu testen und zu überprüfen.
{% endalert %}

Nachdem Sie den Drag-and-Drop-Editor zum Entwerfen und Erstellen Ihrer E-Mail-Nachricht verwendet haben, fahren Sie mit der [Erstellung][12] des restlichen Teils Ihrer Kampagne oder Ihres Canvas fort.

{% details Über die aktualisierte HTML-Engine %}
Die zugrunde liegende Engine, die HTML aus dem Drag-and-Drop-Editor erzeugt, wurde optimiert und aktualisiert, was zu Vorteilen bei der Komprimierung und dem Rendering von HTML-Dateien führt.

Die durchschnittliche Größe unseres exportierten HTML-Daten-Footprints wurde reduziert, was zu schnellerem Laden und Rendering, weniger mobilen Clippern und geringerem Bandbreitenverbrauch führt.

Das HTML-Rendering wurde mit den folgenden Updates verbessert, die die Anzahl der bedingten Kommentare und CSS-Medienabfragen minimieren. Infolgedessen sind HTML-Dateien kleiner und effizienter kodiert.
- Umstellung von einem `<div>` elementgebundenen Design zu einer einheitlichen `<table>`-formatierten Codebasis
- [Editor-Blöcke][7] wurden der Übersichtlichkeit halber neu kodiert
- Der endgültige HTML-Code wird komprimiert, um Leerzeichen zwischen Tags zu entfernen.
- Transparente Trennlinien werden automatisch in Inhaltspolsterung umgewandelt
{% enddetails %}

## Andere Anpassungen

Wenn Sie mit der Erstellung von Drag-and-Drop-E-Mails fortfahren, können Sie jeden E-Mail-Text weiter anpassen, indem Sie eine Kombination dieser kreativen Details verwenden, um die Aufmerksamkeit und das Interesse Ihres Publikums an Ihrer Botschaft zu wecken.

{% alert tip %}
Sie können ein benutzerdefiniertes Design für Ihren Drag&Drop-Editor erstellen, indem Sie [globale Stileinstellungen]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) verwenden.
{% endalert %}

### Automatische Bildbreite

Bilder, die Sie in Ihre E-Mail aufnehmen, werden automatisch auf **automatische Breite** gesetzt. Um diese Einstellung zu ändern, deaktivieren Sie die Option **Automatische Breite** und passen Sie die prozentuale Breite nach Bedarf an.

![Option Automatische Breite auf der Registerkarte Inhalt des Drag&Drop-Editors.][2]

### Farbschichtung

Mit Hilfe von Farbüberlagerungen können Sie die Farbe des E-Mail-Hintergrunds, des Inhaltsbereichs und verschiedener Inhaltskomponenten ändern. Die Reihenfolge der Farben von vorne nach hinten ist: Farbe der Inhaltskomponente, Hintergrundfarbe des Inhaltsbereichs und Hintergrundfarbe.

![Beispiel für die Farbüberlagerung im Drag-and-Drop-Editor.][3]

### Content-Padding

![Blockoptionen für den Drag&Drop-Editor.][4]{: style="float:right;max-width:25%;margin-left:15px;"}

Um die Auffüllung anzupassen, blättern Sie nach unten zu **Blockoptionen** und wählen Sie **Weitere Optionen**. Sie können Ihr Padding fein abstimmen, damit Ihre E-Mail genau richtig aussieht.

### Hintergrund

Sie können ein Hintergrundbild zu Ihrer Zeilenkonfiguration hinzufügen, um mehr Design und visuelle Inhalte in Ihre Kampagnen einzubinden.

### Personalisierung hinzufügen

![Optionen zum Hinzufügen von Personalisierungen für den Drag & Drop-Editor.][5]{: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid wird im Drag-and-Drop-E-Mail-Editor unterstützt. So fügen Sie Ihrer E-Mail eine Personalisierung hinzu:

1. Wählen Sie **Personalisierung** unter dem Abschnitt **Inhalt**. 
2. Wählen Sie die Art der Personalisierung. Dazu gehören Standardattribute, Geräteattribute, angepasste Attribute und mehr. 
3. Suchen Sie nach dem Attribut, das Sie hinzufügen möchten.
4. Kopieren Sie den generierten Liquid-Snippet und fügen Sie ihn in den Text Ihrer E-Mail ein.

Die Flüssigpersonalisierung wird für Bildblöcke und Felder vom Typ Schaltflächenlink nicht unterstützt. 

#### Dynamische Bilder

Sie können dynamische Bilder in Ihr E-Mail-Messaging aufnehmen, indem Sie Liquid in das Bildquellattribut aufnehmen. Anstelle eines statischen Bildes können Sie zum Beispiel {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} als Bild-URL einfügen, um den Vornamen eines Nutzers:innen in das Bild einzubinden. So können Sie Ihre E-Mails für jeden Benutzer personalisieren.

### Textrichtung ändern

Wenn Sie Ihre Nachricht verfassen, können Sie die Textrichtung zwischen links-nach-rechts und rechts-nach-links umschalten, indem Sie den entsprechenden Button **Textrichtung** auswählen. Sie können diese Option verwenden, wenn Sie Nachrichten in Sprachen wie Arabisch oder Hebräisch erstellen.

![E-Mail Drag-and-Drop-Editor Menü mit Button zum Umschalten der Textausrichtung zwischen rechts-nach-links und links-nach-rechts.][1]{: style="max-width:50%;"}

Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie die Diensteanbieter sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

### HTML-Attribute zu Links hinzufügen

![Der Abschnitt "Attribute" mit dem für einen Link deaktivierten Attribut "clicktracking".][6]{: style="float:right;max-width:35%;margin-left:15px;"}

Wenn Sie Links, Schaltflächen, Bilder und Videos im Drag&Drop-Editor verwenden, wählen Sie unter **Attribute** im Abschnitt **Inhalt** die Option **Neues Attribut hinzufügen**, um zusätzliche Informationen an HTML-Tags in E-Mails anzuhängen. Dies kann insbesondere für die Personalisierung, Segmentierung und Aufmachung Ihrer Nachrichten nützlich sein.

Ein gängiger Anwendungsfall ist die Aufnahme eines Attributs in das Anker-Tag, um das Clicktracking beim Versand über Braze zu deaktivieren.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Ein weiterer häufiger Anwendungsfall ist die Kennzeichnung bestimmter Links als universelle Links. Universelle Links sind Links, die zu Ihrer App weiterleiten und Ihren Nutzern ein integriertes Erlebnis bieten.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (ein [benutzerdefinierter Unterpfad](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) muss konfiguriert werden)

Wie Sie universelle Links einrichten, erfahren Sie unter [Universelle Links und App-Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Alternativ können Sie auch einen unserer Attributionspartner wie [Branch]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_deeplinking/) oder [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking) einbinden, um universelle Links zu verwalten.

[1]: {% image_buster /assets/img/dnd/dnd_template1.png %}
[2]: {% image_buster /assets/img/dnd/dnd1.png %}
[3]: {% image_buster /assets/img/dnd/dnd2.png %}
[4]: {% image_buster /assets/img/dnd/dnd3.png %}
[5]: {% image_buster /assets/img/dnd/dnd4.png %}
[6]: {% image_buster /assets/img/dnd_custom_attributes.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/
[8]: {% image_buster /assets/img/dnd/dnd_emailvariant.png %}
[9]: {% image_buster /assets/img/dnd/dnd_content.png %}
[10]: {% image_buster /assets/img/dnd/dnd_rows.png %}
[11]: {% image_buster /assets/img/dnd/dnd_contentsettings.png %}
[12]: {{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/
[14]: {% image_buster /assets/img/rtl_button.png %}
