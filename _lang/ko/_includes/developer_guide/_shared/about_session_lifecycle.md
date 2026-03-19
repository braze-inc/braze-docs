## 세션 생명주기에 대하여

세션은 Braze SDK가 앱이 시작된 후 사용자 활동을 추적하는 기간을 의미합니다. 새로운 세션을 강제로 시작할 수도 있습니다 [메서드 `changeUser()` 호출]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab web %}
기본적으로 세션은 `braze.openSession()`을 처음 호출할 때 시작됩니다. 세션은 비활동 상태가 `30`분 이상 지속될 경우 활성 상태를 유지합니다(기본 세션 타임아웃을 [변경하지 않거나]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) 사용자가 앱을 닫지 않는 한).
{% endtab %}

{% tab android %}
{% alert note %}
Android용 [활동 생명주기 콜백]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)을 설정한 경우, Braze는 앱의 각 활동에 대해 [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) 및 [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)을 자동으로 호출합니다.
{% endalert %}

기본적으로 세션은 `openSession()`이 처음 호출될 때 시작됩니다. 앱이 백그라운드로 전환된 후 다시 포그라운드로 돌아오면, SDK는 세션이 시작된 이후 10초 이상 경과했는지 확인합니다(기본 세션 타임아웃을 [변경하지 않는 한]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). 그렇다면 새로운 세션이 시작됩니다. 사용자가 앱을 백그라운드에서 닫으면, 세션 데이터는 사용자가 앱을 다시 열 때까지 Braze에 전송되지 않을 수 있습니다.

`closeSession()`을 호출한다고 해서 세션이 즉시 종료되지는 않습니다. 대신, 사용자가 다른 활동을 시작하여 `openSession()`을 다시 호출하지 않으면 10초 후에 세션이 종료됩니다.
{% endtab %}

{% tab swift %}
기본적으로 세션은 `Braze.init(configuration:)`을 호출할 때 시작됩니다. 이것은 `UIApplicationWillEnterForegroundNotification` 알림이 트리거될 때 발생하며, 이는 앱이 포그라운드로 들어갔음을 의미합니다.

앱이 백그라운드로 전환되면 `UIApplicationDidEnterBackgroundNotification`이 트리거됩니다. 앱은 백그라운드에 있는 동안 활성 세션을 유지하지 않습니다. 앱이 포그라운드로 돌아오면, SDK는 세션이 시작된 이후 경과된 시간을 세션 타임아웃과 비교합니다(기본 세션 타임아웃을 [변경하지 않는 한]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). 세션이 시작된 이후 시간이 타임아웃 기간을 초과하면 새로운 세션이 시작됩니다.
{% endtab %}
{% endtabs %}