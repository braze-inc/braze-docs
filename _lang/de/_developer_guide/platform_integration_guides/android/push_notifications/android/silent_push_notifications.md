---
nav_title: Stille Push-Benachrichtigungen
article_title: Stille Push-Benachrichtigungen für Android
platform: Android
page_order: 3
description: "Dieser Artikel beschreibt, wie Sie stille Push-Benachrichtigungen in Ihrer Android-Anwendung implementieren."
channel:
  - push

---

# Stille Push-Benachrichtigungen für Android

> Mit stillen Benachrichtigungen können Sie Ihre App im Hintergrund bei wichtigen Events benachrichtigen. Vielleicht haben Sie neue Sofortnachrichten zu versenden, neue Ausgaben eines Magazins zu veröffentlichen, aktuelle Nachrichten zu versenden oder die neueste Folge der Lieblingssendung Ihres Nutzers zum Herunterladen bereitzustellen, damit er sie offline ansehen kann. Stille Benachrichtigungen eignen sich hervorragend für sporadische, aber unmittelbar wichtige Inhalte, bei denen die Verzögerung zwischen den Abrufen im Hintergrund möglicherweise nicht akzeptabel ist.

## Stille Push-Benachrichtigungen einrichten

Stille Benachrichtigungen sind über die Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) verfügbar. Um sie zu nutzen, müssen Sie das Flag `send_to_sync` im [Android-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/android_object/) auf `true` setzen und sicherstellen, dass keine Felder `title` oder `alert` gesetzt sind, da dies zu Fehlern führt, wenn es zusammen mit `send_to_sync`verwendet wird. Sie können jedoch Daten `extras` in das Objekt aufnehmen.

{% alert tip %}
Beim [Verfassen Ihrer Push-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message) können Sie eine stille Android Push-Benachrichtigung senden, indem Sie eine Nachricht mit nur einem einzigen Leerzeichen senden. Beachten Sie jedoch, dass diese Methode zwar **nicht** zum Senden von Push-Benachrichtigungen empfohlen wird, aber in einigen Fällen hilfreich sein kann.
{% endalert %}

