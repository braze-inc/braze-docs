---
nav_title: "SMS-, RCS- und WhatsApp-Registrierungsformular"
article_title: "SMS-, RCS- und WhatsApp-Registrierungsformular"
alias: "/phone_number_capture/"
page_order: 1
description: "Auf dieser Seite erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor für In-App-Nachrichten ein Formular für die Registrierung bei SMS, RCS und WhatsApp erstellen."
---

# SMS-, RCS- und WhatsApp-Registrierungsformular

> Die Formulare für die SMS-, RCS- und WhatsApp-Registrierung sind Templates, die im Drag-and-Drop-Editor für In-App-Nachrichten zur Verfügung stehen. Verwenden Sie diese Templates, um die Telefonnummern der Nutzer:innen zu sammeln und Ihre Abo-Gruppen für SMS, MMS, RCS und WhatsApp zu vergrößern.

![Drei Beispiele für In-App-Nachrichten, die mit dem Template des Formulars für die Registrierung auf dem Telefon erstellt wurden.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Erstellen eines Anmeldeformulars für Telefonnummern

### Schritt 1: Wählen Sie Ihr Template

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie die **SMS-Registrierung** (dies gilt auch für die RCS-Registrierung) oder die **WhatsApp-Registrierung** für Ihr Template aus und wählen dann **Nachricht erstellen**. Diese Templates werden sowohl für mobile Apps als auch für Webbrowser unterstützt.

Modal zum Auswählen der SMS-Registrierung oder der WhatsApp-Registrierung als Template beim Erstellen einer In-App-Nachricht.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Schritt 2: Nachrichtenstile festlegen

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Arbeitsablauf beim Hochladen und Auswählen einer angepassten Schriftart.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Schritt 3: Komponente zur Eingabe von Telefonnummern anpassen

Um mit der Erstellung Ihres Anmeldeformulars zu beginnen, wählen Sie im Editor die Komponente zur Eingabe der Telefonnummer.

![Vorschaubereich bei der Erstellung eines Registrierungsformulars mit ausgewählter Komponente für die Eingabe der Telefonnummer.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

Geben Sie im Seitenmenü an, für welche Abonnementgruppe diese Vorlage Telefonnummern sammeln soll. Um die bewährten Praktiken für die Compliance einzuhalten, können Sie nur die Zustimmung zu einer Abo-Gruppe pro Registrierungsformular für Telefonnummern einholen. Falls gewünscht, können Sie jedoch mehrere Formulare verwenden, um die Zustimmung für andere Abo-Gruppen einzuholen.

![Abo-Gruppe Dropdown mit einer ausgewählten Abo-Gruppe.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Standardmäßig sammeln wir Nummern weltweit, aber Sie können die Anzahl der Länder, aus denen Nummern gesammelt werden sollen, einschränken. Dies ist hilfreich, wenn Sie nur Nutzer mit Telefonnummern in bestimmten Ländern benachrichtigen möchten, und kann zur Sauberkeit der Liste beitragen. Deaktivieren Sie dazu die Option **Nummern aus allen Ländern erfassen** und wählen Sie über die Dropdown-Liste bestimmte Länder aus. Ihre Benutzer können nur die Länder auswählen, die Sie ausdrücklich hinzugefügt haben.

![Länder-Dropdown, um die Länder auszuwählen, aus denen Sie Nummern sammeln möchten.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Ungültige Telefonnummern

Wenn Ihre Benutzer eine Telefonnummer eingeben, die nicht akzeptierte Sonderzeichen enthält, wird eine allgemeine Fehlermeldung angezeigt, die nicht angepasst werden kann, und sie können das Formular nicht abschicken. Sie können das Fehlerverhalten in der **Vorschau & ** Tab **Test** und auf Ihrem Gerät sehen. Lesen Sie diesen Artikel, um zu erfahren [, wie Braze Telefonnummern formatiert]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Schritt 4: Haftungsausschluss hinzufügen (für SMS- und RCS-Formulare zur Registrierung)

Bei SMS- und RCS-Registrierungsformularen ist es wichtig, dass Sie die Art der SMS oder RCS, die Sie versenden werden, klar angeben. Stellen Sie sicher, dass Ihr Listenwachstum den Vorschriften entspricht, indem Sie die folgenden Informationen in Ihr Formular aufnehmen:

- Beschreibung der Arten von SMS- und RCS-Nachrichten, die Ihre Kund:innen erwarten können (Warenkorb-Erinnerungen, Aktionen und Angebote, Termin-Erinnerungen usw.). Sie müssen nicht jeden Anwendungsfall auflisten, aber Sie sollten eine Beschreibung der Arten von Nachrichten liefern, die Ihre Marke senden wird.
- Beachten Sie, dass die Zustimmung keine Bedingung für einen Kauf ist (falls zutreffend).
- Häufigkeit der Nachrichten und Hinweis, dass Nachrichten- und Datentarife gelten. Wenn Sie die genaue Häufigkeit der Nachrichten nicht kennen, können Sie sagen, dass die Häufigkeit variieren kann.
- Links zu Ihren Nutzungsbedingungen & Bedingungen und SMS und RCS Datenschutzrichtlinien.
- Erinnerung an Hilfe- und Opt-out-Schlüsselwörter (HELP für Hilfe; STOP zum Abbrechen).

Wir haben in der Vorlage einen Platzhalter für den Haftungsausschluss bereitgestellt, der lediglich als Beispiel dient. Er stellt keine Rechtsberatung dar und sollte nicht als Grundlage für die Einhaltung von Vorschriften dienen. Es ist wichtig, dass Sie mit Ihrem juristischen Team zusammenarbeiten, um eine Sprache zu entwickeln, die auf Ihre spezielle Marke zugeschnitten ist.

{% alert note %}
Diese Dokumentation ist nicht als Rechtsberatung gedacht und darf auch nicht als solche verstanden werden.
{% endalert %}

Weitere Informationen zur Einhaltung von SMS und RCS finden Sie unter [Gesetze und Vorschriften für SMS, MMS und RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Schritt 5: Nachricht gestalten

Passen Sie das Aussehen Ihrer Nachricht mit den [In-App-Nachricht-Komponenten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) per Drag-and-Drop an.

## Analysieren der Ergebnisse

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![In-App-Nachricht Performance-Panel, das die Klicks für jeden Link in der In-App-Nachricht anzeigt.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


