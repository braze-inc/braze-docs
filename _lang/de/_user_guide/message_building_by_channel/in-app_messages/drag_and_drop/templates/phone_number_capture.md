---
nav_title: SMS- und WhatsApp-Anmeldeformular
article_title: SMS- und WhatsApp-Anmeldeformular
alias: "/phone_number_capture/"
page_order: 1
description: "Auf dieser Seite erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor für In-App-Nachrichten ein Formular für die Registrierung bei SMS und WhatsApp erstellen."
---

# Anmeldeformular für SMS und WhatsApp

> Die Formulare für die SMS- und WhatsApp-Registrierung sind Templates, die im Drag-and-Drop-Editor für In-App-Nachrichten zur Verfügung stehen. Verwenden Sie diese Templates, um die Telefonnummern der Nutzer:innen zu sammeln und Ihre SMS- und WhatsApp-Abo-Gruppen zu vergrößern.

![Drei Beispiele für In-App-Nachrichten, die mit dem Template für das Formular zur Registrierung von Telefonen erstellt wurden.][img7]

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Erstellen eines Anmeldeformulars für Telefonnummern

### Schritt 1: Template wählen

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie für Ihre Template **SMS-Registrierung** oder **WhatsApp-Registrierung** und dann **Nachricht erstellen**. Diese Templates werden sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Modal zum Auswählen der SMS-Registrierung oder WhatsApp-Registrierung als Template beim Erstellen einer In-App-Nachricht.][img2]{: style="max-width:70%"}

### Schritt 2: Nachrichtenstile festlegen

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Arbeitsablauf beim Hochladen und Auswählen einer benutzerdefinierten Schriftart.][img6]

### Schritt 3: Komponente zur Eingabe von Telefonnummern anpassen

Um mit der Erstellung Ihres Anmeldeformulars zu beginnen, wählen Sie im Editor die Komponente zur Eingabe der Telefonnummer.

![Vorschaubereich bei der Erstellung eines Anmeldeformulars mit ausgewählter Eingabekomponente für die Telefonnummer.][img3]{: style="max-width:40%"}

Geben Sie im Seitenmenü an, für welche Abonnementgruppe diese Vorlage Telefonnummern sammeln soll. Um die bewährten Praktiken für die Compliance einzuhalten, können Sie nur die Zustimmung zu einer Abo-Gruppe pro Registrierungsformular für Telefonnummern einholen. Falls gewünscht, können Sie jedoch mehrere Formulare verwenden, um die Zustimmung für andere Abo-Gruppen einzuholen.

![Abonnementgruppen-Dropdown mit einer ausgewählten Abonnementgruppe.][img4]{: style="max-width:40%"}

Standardmäßig sammeln wir Nummern weltweit, aber Sie können die Anzahl der Länder, aus denen Nummern gesammelt werden sollen, einschränken. Dies ist hilfreich, wenn Sie nur Nutzer mit Telefonnummern in bestimmten Ländern benachrichtigen möchten, und kann zur Sauberkeit der Liste beitragen. Deaktivieren Sie dazu die Option **Nummern aus allen Ländern erfassen** und wählen Sie über die Dropdown-Liste bestimmte Länder aus. Ihre Benutzer können nur die Länder auswählen, die Sie ausdrücklich hinzugefügt haben.

![Dropdown-Menü "Länder", um die Länder auszuwählen, aus denen Sie Nummern sammeln möchten.][img5]{: style="max-width:40%"}

#### Ungültige Telefonnummern

Wenn Ihre Benutzer eine Telefonnummer eingeben, die nicht akzeptierte Sonderzeichen enthält, wird eine allgemeine Fehlermeldung angezeigt, die nicht angepasst werden kann, und sie können das Formular nicht abschicken. Sie können das Fehlerverhalten auf der Registerkarte **Vorschau & Test** und auf Ihrem Testgerät sehen. Lesen Sie diesen Artikel, um zu erfahren [, wie Braze Telefonnummern formatiert][2].

### Schritt 4: Haftungsausschluss hinzufügen (für SMS-Formulare zur Registrierung)

Bei SMS-Formularen für die Registrierung ist es wichtig, dass Sie die Art der SMS, die Sie versenden werden, klar angeben. Stellen Sie sicher, dass Ihr Listenwachstum den Vorschriften entspricht, indem Sie die folgenden Informationen in Ihr Formular aufnehmen:

- Beschreibung der Arten von SMS-Nachrichten, die Ihre Kunden erwarten können (Erinnerungen an den Einkaufswagen, Werbeaktionen und Angebote, Terminerinnerungen, usw.). Sie müssen nicht jeden Anwendungsfall auflisten, aber Sie sollten eine Beschreibung der Arten von Nachrichten liefern, die Ihre Marke senden wird.
- Beachten Sie, dass die Zustimmung keine Bedingung für einen Kauf ist (falls zutreffend).
- Häufigkeit der Nachrichten und Hinweis, dass Nachrichten- und Datentarife gelten. Wenn Sie die genaue Häufigkeit der Nachrichten nicht kennen, können Sie sagen, dass die Häufigkeit variieren kann.
- Links zu Ihren Allgemeinen Geschäftsbedingungen und der SMS-Datenschutzrichtlinie.
- Erinnerung an Hilfe- und Opt-out-Schlüsselwörter (HELP für Hilfe; STOP zum Abbrechen).

Wir haben in der Vorlage einen Platzhalter für den Haftungsausschluss bereitgestellt, der lediglich als Beispiel dient. Er stellt keine Rechtsberatung dar und sollte nicht als Grundlage für die Einhaltung von Vorschriften dienen. Es ist wichtig, dass Sie mit Ihrem juristischen Team zusammenarbeiten, um eine Sprache zu entwickeln, die auf Ihre spezielle Marke zugeschnitten ist.

{% alert note %}
Diese Dokumentation ist nicht als Rechtsberatung gedacht und darf auch nicht als solche verstanden werden.
{% endalert %}

Weitere Informationen über die Einhaltung von SMS-Gesetzen finden Sie unter [SMS-Gesetze und -Vorschriften][4].

### Schritt 5: Nachricht gestalten

Passen Sie das Aussehen Ihrer Nachricht mit den [In-App-Nachricht-Komponenten][3] per Drag-and-Drop an.

## Ergebnisse analysieren

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![In-App-Nachricht Performance-Panel mit Klicks für jeden Link in der In-App-Nachricht.][img8]

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}
