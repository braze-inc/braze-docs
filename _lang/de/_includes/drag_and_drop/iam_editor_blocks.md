## In-App-Nachricht Editor-Blöcke verwenden

Editor-Blöcke befinden sich unter dem Abschnitt **Build** für In-App-Nachrichten. Um sie zu verwenden, ziehen Sie einen Editor-Block in eine Spalte. Es passt sich automatisch an die Spaltenbreite an. Jeder Editor-Block hat eigene Einstellungen etwa zu Padding. Das rechte Bedienfeld wechselt automatisch in ein Eigenschaftsfenster für das ausgewählte Inhaltselement.

## Typen

Die folgende Tabelle zeigt, wie Sie die einzelnen Editor-Blöcke verwenden können.

| Name | Beschreibung |
| --- | --- |
| Titel | Gibt einen Titeltext in die Nachricht ein. |
| Absatz | Gibt einen Absatztext in die Nachricht ein. |
| Button | Fügt eine Standard-Schaltfläche hinzu. Die Eigenschaften erlauben Bearbeitung, Link-Einrichtung und Analytics. |
| Radio-Button | Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen können. Bei der Übermittlung protokolliert das Nutzerprofil das zugehörige angepasste Attribut. |
| Bild | Fügt ein Bild aus der [Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) ein. |
| Link | Fügt einen Hyperlink ein, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in einen Text eingebettet oder eigenständig sein. |
| Spacer | Fügt Leerraum oder Füllmaterial zwischen anderen Blöcken hinzu. |
| Angepasster Code | Fügt angepasstes HTML, CSS oder JavaScript ein und führt es aus, um Fortschritte bei der Anpassung zu erzielen.  |
| Erfassung von Telefonnummern | Fügt ein Formularfeld für Telefonnummern ein. Nach dem Absenden ist der Nutzer:in der [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) oder [WhatsApp Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups/) angemeldet. |
| E-Mail-Erfassung | Fügt ein Formularfeld für E-Mail-Adressen ein. Nach der Übermittlung wird die E-Mail Adresse dem Profil des Nutzers:in in Braze hinzugefügt. |
| Dropdown      | Fügt ein Dropdown-Menü mit einer vordefinierten Liste von Artikeln ein, aus der Nutzer:innen einen auswählen können. Sie können der Liste beliebige angepasste Attribute Strings hinzufügen. |
| Kontrollkästchen      | Fügt ein Kontrollkästchen ein. Wenn der Nutzer:innen das Kästchen markiert, wird das Attribut des Blocks auf `true` gesetzt. Wenn es nicht markiert ist, wird sein Attribut auf `false` gesetzt. |
| Kontrollkästchen-Gruppe| Nutzer:innen können aus mehreren angebotenen Möglichkeiten auswählen. Die Werte werden entweder festgelegt oder zu einem definierten Array angepasster Attribute hinzugefügt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Eigenschaften

Einzelheiten zu den Eigenschaften der einzelnen Editorblöcke finden Sie in den folgenden Tabellen.

### Titel und Absatz

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Dicke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Zeilenhöhe | Ändert den Abstand zwischen den Textzeilen |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textausrichtung | Verschiebt den Text, um ihn links, mittig, rechts oder im Blocksatz auszurichten. |
| Textfarbe | Ändert die Farbe des Textes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Button

| Eigenschaft | Beschreibung |
| --- | --- |
| Button-Breite | Ändert die Breite des Buttons auf automatisch oder manuell |
| Schriftfamilie | Dies ist der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Dicke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Button-Ausrichtung | Verschiebt den Button so, dass er links, mittig oder rechts ausgerichtet ist. |
| Button-Textfarbe | Ändert die Farbe des Textes auf dem Button |
| Hintergrundfarbe | Ändert die Farbe des Hintergrunds des Buttons |
| Rahmenstil | Legt den Stil der Umrandung des Buttons fest | 
| Rahmenradius | Bestimmt, wie rund Sie die Ecken haben möchten |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bild

| Eigenschaft | Beschreibung |
| --- | --- |
| URL | Die gehostete Adresse für das Bild |
| Ausrichtung | Verschiebt das Bild so, dass es links, mittig oder rechts ausgerichtet ist. |
| Hintergrundfarbe | Ändert die Farbe des Hintergrunds des Bildes |
| Rahmenstil | Bestimmt den Stil der Umrandung des Bildes | 
| Rahmenradius | Bestimmt, wie rund Sie die Ecken des Bildes haben möchten |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Dies ist der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Dicke des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textfarbe | Ändert die Farbe des Textes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

| Eigenschaft | Beschreibung |
| --- | --- |
| Hintergrundfarbe | Ändert die Hintergrundfarbe des Abstandshalters |
| Höhe | Ändert die Höhe des Abstandshalters. Diese können Sie auch mit den Griffen am Abstandshalter ändern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Angepasster Code

| Eigenschaft | Beschreibung |
| --- | --- |
| Angepasster Code | Ermöglicht es Ihnen, HTML, CSS und JavaScript für eine In-App-Nachricht hinzuzufügen, zu bearbeiten oder zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Telefonerfassung

| Eigenschaft | Beschreibung |
| --- | --- |
| Abo-Gruppe | Die [SMS-]({{site.baseurl}}/sms_rcs_subscription_groups/) oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups/), für die der Nutzer:in durch die Erfassung seiner Telefonnummer abonniert wird, mit der Option, Nummern aus allen Ländern zu erfassen |
| Textausrichtung | Verschiebt den Text, um ihn links, mittig, rechts oder im Blocksatz auszurichten. |
| Platzhaltertext | Eine Platzhalter-Telefonnummer für die Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### E-Mail-Erfassung

| Eigenschaft | Beschreibung |
| --- | --- |
| Schriftfamilie | Der Schriftstil für den Text |
| Schriftschnitt | Bestimmt die Dicke des Textes |
| Schriftgröße | Bestimmt die Größe des Textes |
| Zeilenhöhe | Ändert den Abstand zwischen den Textzeilen |
| Textfarbe | Ändert die Farbe des Textes |
| Buchstabenabstand | Ändert den Abstand zwischen den einzelnen Zeichen |
| Textausrichtung | Verschiebt den Text, um ihn links, mittig, rechts oder im Blocksatz auszurichten. |
| Platzhaltertext | Ein Platzhalter für eine E-Mail Adresse zur Anzeige |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aktionen

Sie können eine Aktion zuweisen, die ausgeführt wird, wenn ein Nutzer:innen auf einen Button, einen Link oder ein Bild in der Nachricht tippt. Sie können [Liquid]({{site.baseurl}}/liquid/) auch verwenden, um die Aktionen zu personalisieren. Einzelheiten zu den Aktionen der einzelnen Editor-Blöcke finden Sie in den folgenden Tabellen.

### Button

| Aktion | Beschreibung |
| --- | --- |
| Formular absenden, wenn auf den Button geklickt wird | Sendet das Formular ab und führt das ausgewählte Klickverhalten aus. Deaktivieren Sie diese Option, um nur das Verhalten beim Klicken auszuführen. |
| Separate Verhaltensweisen für jede Plattform festlegen | Passt das Verhalten des Buttons für jede Plattform separat an. |
| On-Click-Verhalten | Legt die Aktion fest, die ausgeführt werden soll, wenn der Nutzer:innen auf den Button klickt, z.B. die Nachricht schließen, die Web-URL öffnen, einen Deeplink zu einer bestimmten Seite der App herstellen, zu einer anderen Seite gehen oder [eine Push-Erlaubnis anfordern]({{site.baseurl}}/push_primer/). |
| Angepasste Attribute oder Events protokollieren | Legt fest, ob ein Klick auf den Button das Profil des Nutzers mit angepassten Daten aktualisiert. Sie können auch den Bezeichner für die Berichterstattung auswählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bild

Die Spezifikationen für Bilder finden Sie in unseren [Spezifikationen für In-App-Nachricht-Bilder]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Aktion | Beschreibung |
| --- | --- |
| Alt-Text | Die schriftliche Kopie, die anstelle eines Bildes erscheint, wenn das Bild nicht geladen werden kann. Screenreader melden Alt-Text, um Bilder zu erklären. Verwenden Sie also Klartext, um wichtige Informationen über ein Bild bereitzustellen. |
| Formular bei Klick auf Bild senden | Sendet das Formular ab und führt das ausgewählte Klickverhalten aus. Deaktivieren Sie diese Option, um nur das Verhalten beim Klicken auszuführen. |
| Separate Verhaltensweisen für jede Plattform festlegen | Passt das Verhalten des Bildes für jede Plattform separat an. |
| On-Click-Verhalten | Bestimmt die Aktion, wenn der Nutzer:in auf das Bild klickt, z.B. Schließen der Nachricht, Öffnen der Web-URL, Deeplinking auf eine bestimmte Seite der App, Wechsel zu einer anderen Seite oder [Anfrage nach Push-Erlaubnis]({{site.baseurl}}/push_primer/). |
| Angepasste Attribute oder Events protokollieren | Legt fest, ob ein Klick auf das Bild das Profil des Nutzers mit angepassten Daten aktualisiert. Sie können auch den Bezeichner für die Berichterstattung auswählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Aktion | Beschreibung |
| --- | --- |
| URL | Der Hyperlink zum Navigieren zu |
| Bezeichner für Berichterstellung | Legt fest, welcher Bezeichner für die Berichterstattung verwendet wird |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

