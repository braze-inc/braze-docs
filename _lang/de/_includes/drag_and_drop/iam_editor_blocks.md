## Verwendung von In-App-Nachrichten-Editor-Blöcken

Die Editor-Blöcke befinden sich im Abschnitt **Erstellen** für In-App-Nachrichten. Um sie zu verwenden, ziehen Sie einen Editor-Block in eine Spalte. Er passt sich automatisch an die Spaltenbreite an. Jeder Editor-Block hat eigene Einstellungen, wie z. B. eine granulare Steuerung des Paddings. Das rechte Panel wechselt automatisch in ein Eigenschafts-Panel für das ausgewählte Inhaltselement.

## Typen

Die folgende Tabelle zeigt, wie Sie die einzelnen Editor-Block-Typen verwenden können.

| Name | Beschreibung |
| --- | --- |
| Titel | Fügt einen Titeltext in die Nachricht ein. |
| Absatz | Fügt einen Absatztext in die Nachricht ein. |
| Button | Fügt einen Standard-Button hinzu. Die Eigenschaften dieses Blocks ermöglichen das Bearbeiten, Einrichten von Links und das Protokollieren von Analytics. |
| Radio-Button | Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen können. Bei der Übermittlung protokolliert das Nutzerprofil das zugehörige angepasste Attribut, das ein String sein muss, um gespeichert zu werden. Angepasste Attribute mit anderen Datentypen werden nicht im Nutzerprofil gespeichert. |
| Bild | Fügt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) ein. |
| Link | Fügt einen Hyperlink ein, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig verwendet werden. |
| Spacer | Fügt Leerraum oder Padding zwischen anderen Blöcken hinzu. |
| Angepasster Code | Fügt angepasstes HTML, CSS oder JavaScript für erweiterte Anpassungen ein und führt es aus. |
| Telefonerfassung | Fügt ein Formularfeld für Telefonnummern ein. Nach der Übermittlung wird der/die Nutzer:in in die [SMS-]({{site.baseurl}}/sms_rcs_subscription_groups/) oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups/) aufgenommen. |
| E-Mail-Erfassung | Fügt ein Formularfeld für E-Mail-Adressen ein. Nach der Übermittlung wird die E-Mail-Adresse dem Nutzerprofil in Braze hinzugefügt. |
| Kurztext    | Fügt ein Formularfeld ein, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt. |
| Dropdown      | Fügt ein Dropdown-Menü mit einer vordefinierten Liste von Artikeln ein, aus der Nutzer:innen einen auswählen können. Sie können der Liste beliebige angepasste Attribut-Strings hinzufügen. |
| Kontrollkästchen      | Fügt ein Kontrollkästchen ein. Wenn der/die Nutzer:in das Kästchen markiert, wird das Attribut des Blocks auf `true` gesetzt. Wenn es nicht markiert ist, wird sein Attribut auf `false` gesetzt. |
| Kontrollkästchen-Gruppe| Nutzer:innen können aus mehreren vorgegebenen Optionen auswählen. Die Werte werden entweder festgelegt oder zu einem definierten angepassten Array-Attribut hinzugefügt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Eigenschaften

Einzelheiten zu den Eigenschaften der einzelnen Editor-Blöcke finden Sie in den folgenden Tabellen.

### Titel und Absatz

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Stärke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Zeilenhöhe | Ändert den Abstand zwischen den Textzeilen |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textausrichtung | Richtet den Text linksbündig, zentriert, rechtsbündig oder im Blocksatz aus |
| Textfarbe | Ändert die Farbe des Textes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Button

| Eigenschaft | Beschreibung |
| --- | --- |
| Button-Breite | Ändert die Breite des Buttons auf automatisch oder manuell |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Stärke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Button-Ausrichtung | Richtet den Button linksbündig, zentriert oder rechtsbündig aus |
| Button-Textfarbe | Ändert die Farbe des Textes auf dem Button |
| Hintergrundfarbe | Ändert die Farbe des Button-Hintergrunds |
| Rahmenstil | Legt den Stil des Button-Rahmens fest | 
| Rahmenradius | Bestimmt, wie rund die Ecken sein sollen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bild

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Eigenschaft | Beschreibung |
| --- | --- |
| URL | Die gehostete Adresse für das Bild |
| Ausrichtung | Richtet das Bild linksbündig, zentriert oder rechtsbündig aus |
| Hintergrundfarbe | Ändert die Farbe des Bild-Hintergrunds |
| Rahmenstil | Legt den Stil des Bild-Rahmens fest | 
| Rahmenradius | Bestimmt, wie rund die Ecken des Bildes sein sollen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Stärke des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textfarbe | Ändert die Farbe des Textes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

| Eigenschaft | Beschreibung |
| --- | --- |
| Hintergrundfarbe | Ändert die Hintergrundfarbe des Spacers |
| Höhe | Ändert die Höhe des Spacers. Sie können dies auch über die Ziehpunkte am Spacer ändern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Angepasster Code

| Eigenschaft | Beschreibung |
| --- | --- |
| Angepasster Code | Ermöglicht es Ihnen, HTML, CSS und JavaScript für eine In-App-Nachricht hinzuzufügen, zu bearbeiten oder zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Telefonerfassung

| Eigenschaft | Beschreibung |
| --- | --- |
| Abo-Gruppe | Die [SMS-]({{site.baseurl}}/sms_rcs_subscription_groups/) oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups/), die Nutzer:innen durch Angabe ihrer Telefonnummer abonnieren, mit der Option, Nummern aus allen Ländern zu erfassen |
| Textausrichtung | Richtet den Text linksbündig, zentriert, rechtsbündig oder im Blocksatz aus |
| Platzhaltertext | Eine Platzhalter-Telefonnummer zur Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### E-Mail-Erfassung

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Stärke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Zeilenhöhe | Ändert den Abstand zwischen den Textzeilen |
| Textfarbe | Ändert die Farbe des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textausrichtung | Richtet den Text linksbündig, zentriert, rechtsbündig oder im Blocksatz aus |
| Platzhaltertext | Eine Platzhalter-E-Mail-Adresse zur Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aktionen

Sie können eine Aktion zuweisen, die ausgeführt wird, wenn Nutzer:innen auf einen Button, einen Link oder ein Bild in der Nachricht tippen. Sie können auch [Liquid]({{site.baseurl}}/liquid/) verwenden, um die Aktionen zu personalisieren. Einzelheiten zu den Aktionen der einzelnen Editor-Blöcke finden Sie in den folgenden Tabellen.

### Button

| Aktion | Beschreibung |
| --- | --- |
| Formular absenden, wenn auf den Button geklickt wird | Sendet das Formular ab und führt das ausgewählte Klickverhalten aus. Deaktivieren Sie diese Option, um nur das Klickverhalten auszuführen. |
| Separate Verhaltensweisen für jede Plattform festlegen | Passt das Verhalten des Buttons für jede Plattform separat an. |
| On-Click-Verhalten | Legt die Aktion fest, die ausgeführt wird, wenn Nutzer:innen auf den Button klicken, z. B. das Schließen der Nachricht, das Öffnen der Web-URL, das Deeplinking zu einer bestimmten Seite der App, das Wechseln zu einer anderen Seite oder [die Anfrage einer Push-Berechtigung]({{site.baseurl}}/push_primer/). |
| Angepasste Attribute oder Events protokollieren | Legt fest, ob ein Klick auf den Button das Nutzerprofil mit angepassten Daten aktualisiert. Sie können auch den Bezeichner für die Berichterstattung auswählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bild

Informationen zu Bildspezifikationen finden Sie in unseren [Bildspezifikationen für In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Aktion | Beschreibung |
| --- | --- |
| Alt-Text | Der Text, der anstelle eines Bildes erscheint, wenn das Bild nicht geladen werden kann. Screenreader lesen den Alt-Text vor, um Bilder zu erklären. Verwenden Sie daher einfache Sprache, um wichtige Informationen über ein Bild bereitzustellen. |
| Formular bei Klick auf Bild absenden | Sendet das Formular ab und führt das ausgewählte Klickverhalten aus. Deaktivieren Sie diese Option, um nur das Klickverhalten auszuführen. |
| Separate Verhaltensweisen für jede Plattform festlegen | Passt das Verhalten des Bildes für jede Plattform separat an. |
| On-Click-Verhalten | Legt die Aktion fest, die ausgeführt wird, wenn Nutzer:innen auf das Bild klicken, z. B. das Schließen der Nachricht, das Öffnen der Web-URL, das Deeplinking zu einer bestimmten Seite der App, das Wechseln zu einer anderen Seite oder [die Anfrage einer Push-Berechtigung]({{site.baseurl}}/push_primer/). |
| Angepasste Attribute oder Events protokollieren | Legt fest, ob ein Klick auf das Bild das Nutzerprofil mit angepassten Daten aktualisiert. Sie können auch den Bezeichner für die Berichterstattung auswählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Aktion | Beschreibung |
| --- | --- |
| URL | Der Hyperlink, zu dem navigiert wird |
| Bezeichner für Berichterstattung | Legt fest, welcher Bezeichner für die Berichterstattung verwendet wird |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }