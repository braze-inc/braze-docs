---
nav_title: E-Mail-Anmeldeformular
article_title: E-Mail-Anmeldeformular
alias: "/email_capture/"
page_order: 2
description: "Auf dieser Seite erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor für In-App-Nachrichten ein Formular für die Registrierung per E-Mail erstellen."
---

# E-Mail-Anmeldeformular

> Verwenden Sie die Drag-and-Drop-Vorlage für die E-Mail-Anmeldung in der App, um die E-Mail-Adressen der Nutzer zu sammeln und Ihre Abonnentengruppen zu vergrößern.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Erstellen eines E-Mail-Registrierungsformulars

### Schritt 1: Template wählen

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie **E-Mail-Registrierung** für Ihr Template und dann **Nachricht erstellen** aus. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der In-App-Nachricht-Editor mit dem Template für ein E-Mail-Erfassungsformular.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Schritt 2: Nachrichtenstile festlegen

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Schritt 3: E-Mail-Registrierungskomponente anpassen

Um mit der Erstellung Ihres E-Mail-Registrierungsformulars zu beginnen, wählen Sie im Editor das Element zur E-Mail-Erfassung aus. Standardmäßig weisen alle gesammelten E-Mail-Adressen die globale Abonnementgruppe **Abonniert** auf. Um Nutzer:innen in bestimmte Abo-Gruppen aufzunehmen, referenzieren Sie auf [Update des Status von E-Mail-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des Elements für die E-Mail-Erfassung anpassen.

![Der In-App-Nachricht-Editor mit einem Seitenmenü zum Anpassen des Elements für die E-Mail-Erfassung.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### E-Mail-Validierung

Wenn der oder die Nutzer:in eine E-Mail-Adresse eingibt, die nicht akzeptierte Sonderzeichen enthält, wird eine allgemeine Fehlermeldung angezeigt und das Formular kann nicht gesendet werden. Diese Fehlermeldung ist nicht anpassbar. Sie können das Fehlerverhalten in der **Vorschau & ** Tab **Test** und auf Ihrem Gerät sehen. Erfahren Sie mehr darüber, wie Braze E-Mail-Adressen unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/) formatiert.

### Schritt 4: Sprache für Haftungsausschluss hinzufügen (optional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Schritt 5: Nachricht gestalten

Passen Sie das Aussehen Ihres Registrierungsformulars mit den [In-App-Nachrichten-Komponenten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) per Drag-and-Drop an.

## Analysieren der Ergebnisse

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Bewährte Praktiken

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

