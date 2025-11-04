# Tracken von Sitzungen

> Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Benutzerengagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Benutzer wichtig sind. Das SDK generiert Datenpunkte für "start session" und "close session", die die Sitzungsdauer und die Anzahl der Sitzungen berücksichtigen und im Braze-Dashboard auf der Grundlage der folgenden Sitzungssemantik angezeigt werden. Dieser Referenzartikel beschreibt, wie Sie Sitzungsupdates für Ihre Android- oder FireOS-Anwendung abonnieren können.

## Lebenszyklus einer Sitzung

Wenn Sie Braze mit der von uns empfohlenen [activity lifecycle callback integration] integriert haben ({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), werden `openSession()` und `closeSession()` automatisch für jede Aktivität in Ihrer App aufgerufen. Standardmäßig werden Sitzungen unter Android beim ersten Aufruf von `openSession()` geöffnet und geschlossen, nachdem eine App länger als 10 Sekunden nicht mehr im Vordergrund war. Beachten Sie, dass der Aufruf von `closeSession()` eine Sitzung nicht sofort beendet. Vielmehr schließt die Sitzung nach 10 Sekunden, wenn der oder die Nutzer:in in der Zwischenzeit nicht `openSession()` aufruft (z. B. durch Navigieren zu einer anderen Aktivität).

Eine Android-Sitzung wird nach 10 Sekunden beendet, ohne dass eine Kommunikation mit der Host-Anwendung stattgefunden hat. Das heißt, wenn der oder die Nutzer:in die App verlässt und 9 Sekunden später zurückkehrt, wird die gleiche Sitzung fortgesetzt. Beachten Sie, dass, wenn eine Sitzung geschlossen wird, während der Nutzer:innen die App im Hintergrund hat, diese Daten möglicherweise erst dann auf den Server übertragen werden, wenn die App erneut geöffnet wird.

{% alert note %}
Wenn Sie eine neue Sitzung erzwingen müssen, können Sie dies tun, indem Sie den Nutzer wechseln.
{% endalert %}

## Anpassen des Sitzungs-Timeouts
Um das Sitzungs-Timeout anzupassen, fügen Sie `com_braze_session_timeout` zu Ihrer Datei [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml) hinzu. Der Mindestwert für `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` ist 1 Sekunde.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Testen des Sitzungs-Trackings

Um Sitzungen über Ihren Benutzer zu erkennen, suchen Sie Ihren Benutzer im Dashboard und navigieren Sie im Benutzerprofil zu **App-Nutzung**. Sie können sich vergewissern, dass das Sitzungs-Tracking funktioniert, indem Sie überprüfen, ob die Metrik für die Sitzung ansteigt, wenn Sie es erwarten würden.

![Eine Komponente des Nutzerprofils, die anzeigt, wie viele Sitzungen stattgefunden haben, wann die App zum ersten Mal benutzt wurde und wann sie zuletzt benutzt wurde.]({% image_buster /assets/img_archive/test_session.png %})

## Updates für Sitzungen abonnieren

Das Braze SDK bietet den Abonnemebtdienst [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html), der auf Updates von Sitzungen prüft:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

