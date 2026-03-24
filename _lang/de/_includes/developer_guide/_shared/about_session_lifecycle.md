## Über den Lebenszyklus einer Sitzung

Eine Sitzung referenziert den Zeitraum, in dem das Braze SDK die Aktivitäten der Nutzer:in Ihrer App nach deren Start verfolgt. Sie können auch eine neue Sitzung erzwingen, indem [Sie die Methode `changeUser()` aufrufen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab web %}
Standardmäßig beginnt eine Sitzung, wenn Sie `braze.openSession()` zum ersten Mal aufrufen. Die Sitzung bleibt bis zu `30` Minuten der Inaktivität aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) oder der Nutzer:innen schließt die App.
{% endtab %}

{% tab android %}
{% alert note %}
Wenn Sie den [Aktivitätslebenszyklus-Callback]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) für Android eingerichtet haben, ruft Braze automatisch[`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html)  und[`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)  für jede Aktivität in Ihrer App auf.
{% endalert %}

Standardmäßig wird eine Sitzung gestartet, wenn `openSession()` zum ersten Mal aufgerufen wird. Wenn Ihre App in den Hintergrund wechselt und anschließend wieder in den Vordergrund zurückkehrt, überprüft das SDK, ob seit Beginn der Sitzung mehr als 10 Sekunden vergangen sind (es sei denn, Sie [ändern die Standard-Sitzungszeitüberschreitung]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). In diesem Fall wird eine neue Sitzung beginnen. Wenn der Nutzer:innen Ihre App schließt, während sie im Hintergrund läuft, werden die Daten der Sitzung möglicherweise erst dann an Braze gesendet, wenn er die App erneut öffnet.

Wenn Sie `closeSession()` aufrufen, wird die Sitzung nicht sofort beendet. Stattdessen wird die Sitzung nach 10 Sekunden beendet, wenn `openSession()` nicht erneut vom Nutzer:innen aufgerufen wird, der eine andere Aktivität startet.
{% endtab %}

{% tab swift %}
Standardmäßig beginnt eine Sitzung, wenn Sie `Braze.init(configuration:)` aufrufen. Dies geschieht, wenn die Benachrichtigung `UIApplicationWillEnterForegroundNotification` getriggert wird, was bedeutet, dass die App in den Vordergrund getreten ist.

Wenn Ihre App in den Hintergrund wechselt,`UIApplicationDidEnterBackgroundNotification`wird getriggert. Die App bleibt im Hintergrund nicht in einer aktiven Sitzung. Wenn Ihre App wieder in den Vordergrund rückt, vergleicht das SDK die seit Beginn der Sitzung verstrichene Zeit mit dem Zeitlimit für die Sitzung (es sei denn, Sie [ändern das Standard-Zeitlimit für die Sitzung]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Wenn die seit Beginn der Sitzung verstrichene Zeit die Zeitüberschreitung überschreitet, wird eine neue Sitzung gestartet.
{% endtab %}
{% endtabs %}