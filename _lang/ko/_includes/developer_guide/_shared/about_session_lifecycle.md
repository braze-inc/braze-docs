## 세션 수명 주기 정보

세션은 앱이 실행된 후 Braze 소프트웨어 개발 키트에서 사용자 활동을 추적하는 기간을 말합니다. [ `changeUser()` 메서드를 호출하여]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id) 새 세션을 강제로 생성할 수도 있습니다.

{% tabs %}
{% tab android %}
{% alert note %}
활동 라이프사이클 콜백]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) (Android의 경우)]을 설정한 경우, Braze가 자동으로 호출하여 [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) 및 [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) 를 호출합니다.
{% endalert %}

기본값으로 세션은 `openSession()` 을 처음 호출할 때 시작됩니다. 앱이 백그라운드로 이동했다가 다시 포그라운드로 돌아오면 소프트웨어 개발 키트에서 세션이 시작된 후 10초 이상 경과했는지 확인합니다( [기본값 세션 시간 제한을 변경하지]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout) 않은 경우). 그렇다면 새 세션이 시작됩니다. 사용자가 백그라운드에서 앱을 닫으면 앱을 다시 열 때까지 세션 데이터가 Braze로 전송되지 않을 수 있다는 점에 유의하세요.

`closeSession()` 으로 전화해도 세션이 즉시 종료되지는 않습니다. 대신 사용자가 다른 활동을 시작하여 `openSession()` 을 다시 호출하지 않으면 10초 후에 세션이 종료됩니다.
{% endtab %}

{% tab swift %}
기본적으로 세션은 `Braze.init(configuration:)` 을 호출하면 시작됩니다. 이는 `UIApplicationWillEnterForegroundNotification` 알림이 트리거될 때 발생하며, 이는 앱이 포그라운드에 진입했음을 의미합니다.

앱이 백그라운드로 이동하면 `UIApplicationDidEnterBackgroundNotification` 이 트리거됩니다. 앱이 포그라운드로 돌아오면 소프트웨어 개발 키트에서 세션이 시작된 후 10초 이상 경과했는지 확인합니다( [기본값 세션 시간 제한을 변경하지]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout) 않는 한). 그렇다면 새 세션이 시작됩니다.
{% endtab %}

{% tab 웹 %}
기본값으로 세션은 `braze.openSession()` 을 처음 호출할 때 시작됩니다. 세션은 [기본값인 세션 시간 제한을 변경하거나]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) 사용자가 앱을 닫지 않는 한 최대 `30` 분 동안 활성 상태로 유지됩니다.
{% endtab %}
{% endtabs %}