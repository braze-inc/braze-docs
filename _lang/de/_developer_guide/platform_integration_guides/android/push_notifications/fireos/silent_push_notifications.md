---
nav_title: Stille Push-Benachrichtigungen
article_title: Stille Push-Benachrichtigungen für FireOS
platform: FireOS
page_order: 3

page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie stille FireOS-Push-Benachrichtigungen versenden können, und beschreibt mögliche Anwendungsfälle, in denen stille Push-Benachrichtigungen vorteilhaft sein können."
channel: push

---

# Stille Push-Benachrichtigungen

> Mit stillen Benachrichtigungen können Sie Ihre App im Hintergrund bei wichtigen Events benachrichtigen. Vielleicht haben Sie neue Sofortnachrichten zu versenden, neue Ausgaben eines Magazins zu veröffentlichen, aktuelle Nachrichten zu versenden oder die neueste Folge der Lieblingssendung Ihres Nutzers zum Herunterladen bereitzustellen, damit er sie offline ansehen kann. Stille Benachrichtigungen eignen sich hervorragend für sporadische, aber unmittelbar wichtige Inhalte, bei denen die Verzögerung zwischen den Abrufen im Hintergrund möglicherweise nicht akzeptabel ist.

Stille Benachrichtigungen sind über die Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) verfügbar. Um sie zu nutzen, müssen Sie das Flag `send_to_sync` im [Android-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/android_object/) auf `true` setzen und sicherstellen, dass keine Felder `title` oder `alert` gesetzt sind, da dies zu Fehlern führt, wenn es zusammen mit `send_to_sync` verwendet wird. Sie können jedoch Daten als `extras` in das Objekt aufnehmen.

Stille Benachrichtigungen sind auch im Dashboard verfügbar. Um eine stille Benachrichtigung zu senden, stellen Sie sicher, dass das Titel- und Textfeld der Benachrichtigung leer sind (siehe Abbildung):

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Beispiel für stille Push-Benachrichtigungen -- Android")

