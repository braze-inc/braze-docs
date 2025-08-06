## Einrichten des Uninstall-Trackings

### Schritt 1: FCM einrichten

Das Android Braze SDK verwendet Firebase Cloud Messaging (FCM), um stille Push-Benachrichtigungen zu versenden, die zum Sammeln von Analytics für das Uninstall-Tracking verwendet werden. Falls Sie dies noch nicht getan haben, richten Sie [die]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) Firebase Cloud Messaging API für Push-Benachrichtigungen ein oder [migrieren Sie zu dieser]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

### Schritt 2: Manuelles Uninstall-Tracking erkennen (optional)

Standardmäßig erkennt und ignoriert das Android Braze SDK automatisch stille Push-Benachrichtigungen im Zusammenhang mit dem Uninstall-Tracking. Sie können das Tracking jedoch auch manuell mit der [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) Methode.

{% alert important %}
Da stille Benachrichtigungen für das Uninstall-Tracking nicht an Push-Callbacks von Braze weitergeleitet werden, können Sie diese Methode nur verwenden, bevor Sie eine Push-Benachrichtigung an Braze übergeben.
{% endalert %}

### Schritt 3: Automatische Server-Pings entfernen

Eine stille Push-Benachrichtigung weckt Ihre App auf und instanziiert die Komponente `Application`, wenn die App nicht bereits läuft. Wenn Sie also eine angepasste [`Application`](https://developer.android.com/reference/android/app/Application) Unterklasse haben, entfernen Sie jede Logik, die Ihre Server automatisch während Ihrer [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) Lebenszyklus-Methode.

### Schritt 4: Uninstall-Tracking aktivieren

Schließlich aktivieren Sie das Uninstall-Tracking in Braze. Eine vollständige Anleitung finden Sie unter [Aktivieren des Uninstall-Trackings]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Das Tracking von Deinstallationen kann ungenau sein. Die Metriken, die Sie auf Braze sehen, können verzögert oder ungenau sein.
{% endalert %}
