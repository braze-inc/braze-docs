---
nav_title: E-Mail Registrierung mit Bild
article_title: E-Mail Registrierung mit Hintergrundbild
alias: "/email_image/"
page_order: 4
description: "Auf dieser Seite erfahren Sie, wie Sie den In-App-Nachricht Drag-and-Drop-Editor verwenden, um Ihren Markenstil mit einer einfachen Nachricht zu zeigen und Ihre E-Mail-Liste aufzubauen."
---

# E-Mail-Registrierung mit Hintergrundbild

> Nutzen Sie den In-App-Nachricht Drag-and-Drop-Editor, um Ihren Markenstil mit einer einfachen Nachricht zu zeigen und Ihre E-Mail-Liste aufzubauen.

{% multi_lang_include drag_and_drop/templates.md section='SDK-Anforderungen' %}

## Erstellen eines Formulars für die Registrierung per E-Mail mit einem Hintergrundbild

### Schritt 1: Wählen Sie Ihr Template

Wenn Sie eine In-App-Nachricht per Drag-and-Drop erstellen, wählen Sie **E-Mail-Registrierung mit Hintergrundbild** für Ihr Template und dann **Nachricht erstellen**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der In-App-Nachricht-Editor mit dem Template für eine E-Mail-Registrierung mit einem Hintergrundbild.][img1]

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

Passen Sie das Aussehen Ihres Registrierungsformulars mit den [In-App-Nachrichten-Komponenten][3] per Drag-and-Drop an. Fügen Sie Ihr eigenes Hintergrundbild hinzu, indem Sie die Standard-URL des Hintergrundbildes im Menü **des Nachrichten-Containers** ersetzen, oder entfernen Sie die URL und wählen Sie Ihr Bild aus der [Bibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/).

## Analysieren der Ergebnisse

{% multi_lang_include drag_and_drop/templates.md section='Berichterstattung' %}

## Bewährte Praktiken

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %} 


[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components