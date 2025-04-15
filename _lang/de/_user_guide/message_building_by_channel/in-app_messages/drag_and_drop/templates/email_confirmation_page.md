---
nav_title: E-Mail Registrierung mit Bestätigung
article_title: E-Mail Registrierung mit Bestätigungsseite
alias: "/email_confirmation_page/"
page_order: 6
description: "Auf dieser Seite erfahren Sie, wie Sie den In-App-Nachricht Drag-and-Drop-Editor verwenden, um eine E-Mail-Registrierung mit einer Bestätigungsseite zu erstellen."
---

# E-Mail-Registrierung mit Bestätigungsseite

> Verwenden Sie den In-App-Nachricht Drag-and-Drop-Editor, um eine E-Mail-Registrierung mit einer Bestätigungsseite zu erstellen.

{% multi_lang_include drag_and_drop/templates.md section='SDK-Anforderungen' %}

## Erstellen eines Formulars für die Registrierung per E-Mail mit einer Bestätigungsseite

### Schritt 1: Wählen Sie Ihr Template

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie **E-Mail-Registrierung mit Bestätigungsseite** für Ihr Template und dann **Nachricht erstellen**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der Editor für In-App-Nachrichten mit dem Template für ein E-Mail-Formular zur Registrierung mit Bestätigungsseite.][img1]

### Schritt 2: Nachrichtenstile festlegen

{% multi_lang_include drag_and_drop/templates.md section='Nachrichtenstil' %}

### Schritt 3: E-Mail-Registrierungskomponente anpassen

Um mit der Erstellung Ihres E-Mail-Registrierungsformulars zu beginnen, wählen Sie im Editor das Element zur E-Mail-Erfassung aus. Standardmäßig weisen alle gesammelten E-Mail-Adressen die globale Abonnementgruppe **Abonniert** auf. Um Nutzer:innen in bestimmte Abo-Gruppen aufzunehmen, referenzieren Sie auf [Update des Status von E-Mail-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des Elements für die E-Mail-Erfassung anpassen.

![Der In-App-Nachricht-Editor mit einem Seitenmenü zum Anpassen des Elements für die E-Mail-Erfassung.][img2]

#### E-Mail-Validierung

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Schritt 4: Sprache für Haftungsausschluss hinzufügen (optional)

{% multi_lang_include drag_and_drop/templates.md section='E-Mail-Haftungsausschluss' %}

### Schritt 5: Nachricht gestalten

Passen Sie das Aussehen Ihrer E-Mail-Registrierungsformulare und Bestätigungsseiten mit den [In-App-Nachrichten-Komponenten][3] per Drag-and-Drop an.

## Analysieren der Ergebnisse

{% multi_lang_include drag_and_drop/templates.md section='Berichterstattung' %}

## Bewährte Praktiken

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
