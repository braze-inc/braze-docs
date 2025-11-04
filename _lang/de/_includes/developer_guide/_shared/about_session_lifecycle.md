## Über den Lebenszyklus einer Sitzung

Eine Sitzung referenziert den Zeitraum, in dem das Braze SDK die Aktivitäten der Nutzer:in Ihrer App nach deren Start verfolgt. Sie können auch eine neue Sitzung erzwingen, indem [Sie die Methode `changeUser()` aufrufen]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab android %}
{% alert note %}
Wenn Sie den [activity lifecycle callback]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) für Android eingerichtet haben, ruft Braze automatisch [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) und [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) für jede Aktivität in Ihrer App auf.
{% endalert %}

Standardmäßig wird eine Sitzung gestartet, wenn `openSession()` zum ersten Mal aufgerufen wird. Wenn Ihre App in den Hintergrund geht, bleibt die Sitzung 10 Sekunden lang aktiv (es sei denn, Sie [ändern den Standard-Sitzungs-Timeout]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout) oder der Nutzer:innen schließt Ihre App. Wenn der Nutzer:innen Ihre App schließt, während sie im Hintergrund läuft, werden die Daten der Sitzung möglicherweise erst dann an Braze gesendet, wenn er die App erneut öffnet.

Wenn Sie `closeSession()` aufrufen, wird die Sitzung nicht sofort beendet. Stattdessen wird die Sitzung nach 10 Sekunden beendet, wenn `openSession()` nicht erneut vom Nutzer:innen aufgerufen wird, der eine andere Aktivität startet.
{% endtab %}

{% tab schnell %}
Standardmäßig beginnt eine Sitzung, wenn Sie `Braze.init(configuration:)` aufrufen. Dies geschieht, wenn die Benachrichtigung `UIApplicationWillEnterForegroundNotification` getriggert wird, was bedeutet, dass die App in den Vordergrund getreten ist.

Wenn Ihre App in den Hintergrund geht, wird `UIApplicationDidEnterBackgroundNotification` getriggert. Die Sitzung bleibt für `10` Sekunden aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout) oder der Nutzer:innen schließt Ihre App.
{% endtab %}

{% tab Internet %}
Standardmäßig beginnt eine Sitzung, wenn Sie `braze.openSession()` zum ersten Mal aufrufen. Die Sitzung bleibt bis zu `30` Minuten der Inaktivität aktiv (es sei denn, Sie [ändern den Standard-Timeout für die Sitzung]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) oder der Nutzer:innen schließt die App.
{% endtab %}
{% endtabs %}