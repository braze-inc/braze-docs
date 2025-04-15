## About the session lifecycle

A session refers to the period of time the Braze SDK tracks user activity in your app after it's launched. You can also force a new session by [calling the `changeUser()` method]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab android %}
{% alert note %}
If you've set up the [activity lifecycle callback]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) for Android, Braze will automatically call `openSession()` and `closeSession()` for each activity in your app.
{% endalert %}

By default, a session starts when `openSession()` is first called. If your app goes to the background, the session will remain active for `10` seconds (unless you [change the default session timeout]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout) or the user closes your app. Keep in mind, if the user closes your app while it's in the background, session data may not be sent to Braze until they reopen the app.

Calling `closeSession()` will not immediately end the session. Instead, it will end the session after 10 seconds if `openSession()` isn't called again by the user starting another activity.
{% endtab %}

{% tab swift %}
By default, a session starts when you call `Braze.init(configuration:)`. This occurs when the `UIApplicationWillEnterForegroundNotification` notification is triggered, meaning the app has entered the foreground.

If your app goes to the background, `UIApplicationDidEnterBackgroundNotification` will be triggered. The session will remain active for `10` seconds (unless you [change the default session timeout]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout) or the user closes your app.
{% endtab %}

{% tab web %}
By default, a session starts when you first call `braze.openSession()`. The session will remain active for up to `30` minutes of inactivity (unless you [change the default session timeout]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) or the user closes the app.
{% endtab %}
{% endtabs %}