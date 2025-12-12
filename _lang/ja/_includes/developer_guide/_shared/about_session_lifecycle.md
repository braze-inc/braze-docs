## セッションのライフサイクルについて

セッションとは、Braze SDKがアプリ起動後のユーザーアクティビティを追跡する期間を指す。また、[ `changeUser()` メソッドを呼び出す]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id)ことで、強制的に新しいセッションを作ることもできる。

{% tabs %}
{% tab android %}
{% alert note %}
アクティビティライフサイクルコールバック]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) for Android)を設定していれば、Brazeは自動的に [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html)と [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)を自動的に呼び出す。
{% endalert %}

デフォルトでは、`openSession()` が最初に呼ばれたときにセッションが始まる。アプリがバックグラウンドに移動し、その後フォアグラウンドに戻った場合、SDKはセッションが開始してから10秒以上経過しているかどうかをチェックする（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)しない限り）。その場合、新しいセッションが始まる。ユーザーがバックグラウンドでアプリを閉じた場合、アプリを再度開くまでセッションデータがBrazeに送信されない可能性があることに留意すること。

`closeSession()` を呼んでも、すぐにセッションは終了しない。その代わり、ユーザーが別のアクティビティを開始することによって`openSession()` が再度呼び出されなければ、10秒後にセッションを終了する。
{% endtab %}

{% tab swift %}
デフォルトでは、`Braze.init(configuration:)` を呼び出すとセッションが始まる。これは、`UIApplicationWillEnterForegroundNotification` 通知がトリガーされたとき、つまりアプリがフォアグラウンドに入ったときに発生する。

アプリがバックグラウンドになると、`UIApplicationDidEnterBackgroundNotification` 、トリガーがかかる。アプリがフォアグラウンドに戻ったとき、SDKはセッションが開始してから10秒以上経過しているかどうかをチェックする（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)しない限り）。その場合、新しいセッションが始まる。
{% endtab %}

{% tab web %}
デフォルトでは、セッションは`braze.openSession()` を最初にコールしたときに始まる。セッションは、`30` 分間アクティブにならない限り（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout)するか、ユーザーがアプリを閉じない限り）、アクティブのままである。
{% endtab %}
{% endtabs %}