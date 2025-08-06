{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Stille Push-Benachrichtigungen einrichten

Stille Benachrichtigungen sind über die Braze [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) verfügbar. Um sie zu nutzen, müssen Sie das Flag `send_to_sync` im [Android-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/android_object/) auf `true` setzen und sicherstellen, dass keine Felder `title` oder `alert` gesetzt sind, da dies zu Fehlern führt, wenn es zusammen mit `send_to_sync` verwendet wird. Sie können jedoch Daten als `extras` in das Objekt aufnehmen.

Stille Benachrichtigungen sind auch im Dashboard verfügbar. Um eine stille Benachrichtigung zu senden, stellen Sie sicher, dass das Titel- und Textfeld der Benachrichtigung leer sind (siehe Abbildung):

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Beispiel für stille Push-Benachrichtigungen -- Android")
