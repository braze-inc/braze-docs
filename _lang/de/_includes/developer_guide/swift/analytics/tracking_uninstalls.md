## Einrichten des Uninstall-Trackings

### Schritt 1: Push im Hintergrund aktivieren

Gehen Sie in Ihrem Xcode-Projekt zu **Fähigkeiten** und stellen Sie sicher, dass die **Hintergrundmodi** aktiviert sind. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Schritt 2: Interne Push-Benachrichtigungen ignorieren

Das Swift Braze SDK verwendet Push-Benachrichtigungen im Hintergrund, um Analytics zum Uninstall-Tracking zu sammeln. Um sicherzustellen, dass Ihre App keine unerwünschten Aktionen durchführt, wenn diese gesendet werden, müssen Sie dafür sorgen, dass [interne Push-Benachrichtigungen ignoriert werden]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Schritt 3: Senden Sie einen Push zu Testzwecken (optional)

Als nächstes senden Sie sich selbst eine Push-Benachrichtigung vom Braze-Dashboard aus (keine Sorge - Ihr Nutzerprofil wird dadurch nicht aktualisiert).

1. Gehen Sie zu **Messaging** > **Kampagnen** und erstellen Sie eine Push-Benachrichtigungs-Kampagne über die entsprechende Plattform.
2. Gehen Sie zu **Einstellungen** > **App-Einstellungen** und fügen Sie den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu, und markieren Sie dann **Add Content-Available Flag**.
3. Verwenden Sie die Seite **Vorschau**, um sich selbst einen Test-Push für das Tracking zu senden.
4. Stellen Sie sicher, dass Ihre App keine unerwünschten automatischen Aktionen ausführt, wenn sie eine Push-Benachrichtigung erhält.

{% alert note %}
Mit der Push-Benachrichtigung zum Test wird eine Badge-Nummer verschickt. Bei einem echten Tracking-Push zur Deinstallation werden jedoch keine Badge-Nummern verschickt.
{% endalert %}

### Schritt 3: Uninstall-Tracking aktivieren

Schließlich aktivieren Sie das Uninstall-Tracking in Braze. Eine vollständige Anleitung finden Sie unter [Aktivieren des Uninstall-Trackings]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Das Tracking von Deinstallationen kann ungenau sein. Die Metriken, die Sie auf Braze sehen, können verzögert oder ungenau sein.
{% endalert %}
