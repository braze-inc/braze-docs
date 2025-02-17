---
nav_title: E-Mail Registrierung mit Angebot
article_title: E-Mail Registrierung mit Sonderangebot
alias: "/email_offer/"
page_order: 5
description: "Auf dieser Seite erfahren Sie, wie Sie den In-App-Nachricht per Drag-and-Drop-Editor nutzen können, um Ihre E-Mail-Liste aufzubauen, indem Sie bei der Registrierung einen Sonderrabatt erhalten."
---

# E-Mail-Registrierung mit Sonderangebot

> Nutzen Sie den In-App-Nachricht per Drag-and-Drop-Editor, um Ihre E-Mail-Liste aufzubauen und bieten Sie einen Sonderrabatt bei der Registrierung an.

{% multi_lang_include drag_and_drop/templates.md section='SDK-Anforderungen' %}

## Erstellen eines Formulars für die Registrierung per E-Mail mit einem Sonderangebot

### Schritt 1: Wählen Sie Ihr Template

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie für Ihr Template **E-Mail-Registrierung mit Sonderangebot** und anschließend **Nachricht erstellen**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der Editor für In-App-Nachrichten mit dem Template für eine E-Mail-Registrierung mit einem Sonderangebot.][img1]

### Schritt 2: Nachrichtenstile festlegen

{% multi_lang_include drag_and_drop/templates.md section='Nachrichtenstil' %}

### Schritt 3: E-Mail-Registrierungskomponente anpassen

Um mit der Erstellung Ihres Formulars für die Registrierung per E-Mail zu beginnen, wählen Sie die Seite für **die Registrierung per E-Mail** und dann das Element für die Erfassung von E-Mails im Editor aus. Standardmäßig weisen alle gesammelten E-Mail-Adressen die globale Abonnementgruppe **Abonniert** auf. Um Nutzer:innen in bestimmte Abo-Gruppen aufzunehmen, referenzieren Sie auf [Update des Status von E-Mail-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des Elements für die E-Mail-Erfassung anpassen.

![Der In-App-Nachricht-Editor mit einem Seitenmenü zum Anpassen des Elements für die E-Mail-Erfassung.][img2]

#### E-Mail-Validierung

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Schritt 4: Sprache für Haftungsausschluss hinzufügen (optional)

{% multi_lang_include drag_and_drop/templates.md section='E-Mail-Haftungsausschluss' %}

### Schritt 5: Nachricht gestalten

Passen Sie das Aussehen Ihres Sonderangebots mit den [In-App-Nachrichten-Komponenten][3] per Drag-and-Drop an.

## Analysieren der Ergebnisse

{% multi_lang_include drag_and_drop/templates.md section='Berichterstattung' %}

## Bewährte Praktiken

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_offer.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_offer.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components