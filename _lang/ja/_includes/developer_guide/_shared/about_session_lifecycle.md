## セッションのライフサイクルについて

セッションとは、Braze SDKがアプリ起動後にユーザーの活動をトラッキングする期間を指す。また、[メソッド`changeUser()`を呼び]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id)出すことで新しいセッションを強制的に開始できる。

{% tabs %}
{% tab web %}
デフォルトでは、セッションは最初に呼び出された時点で開始`braze.openSession()`される。セッションは、最大`30`  分間操作がない状態が続くと終了する（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout)しない限り、またはユーザーがアプリを閉じる場合を除く）。
{% endtab %}

{% tab android %}
{% alert note %}
Android用のアクティビティライフサイクルコールバックを設定した場合、]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)Brazeはアプリ内の各アクティビティに対して[`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)自動的に`onStart`と`onStop`[`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html)を呼び出す。
{% endalert %}

デフォルトでは、セッションはが最初に呼び出された`openSession()`時に開始される。アプリがバックグラウンドに移行した後、再びフォアグラウンドに戻った場合、SDKはセッション開始から10秒以上経過しているかどうかを確認する（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)しない限り）。そうであれば、新しいセッションが始まる。ユーザーがバックグラウンドでアプリを閉じた場合、セッションデータはアプリを再起動するまでBrazeに送信されない可能性があることに留意せよ。

呼び出しはセッションを`closeSession()`直ちに終了させない。代わりに、ユーザーが別のアクティビティを開始して再度呼び出さない`openSession()`場合、10秒後にセッションを終了する。
{% endtab %}

{% tab swift %}
デフォルトでは、セッションは を呼び出した時に開始`Braze.init(configuration:)`される。これは通知`UIApplicationWillEnterForegroundNotification`がトリガーされた時に発生する。つまりアプリがフォアグラウンドに入ったことを意味する。

アプリがバックグラウンドに移行すると、トリガー`UIApplicationDidEnterBackgroundNotification`される。アプリはバックグラウンドではアクティブなセッションを維持しない。アプリがフォアグラウンドに戻った時、SDKはセッション開始からの経過時間をセッションタイムアウトと比較する（[デフォルトのセッションタイムアウトを変更]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)しない限り）。セッション開始からの時間がタイムアウト期間を超えた場合、新しいセッションが始まる。
{% endtab %}
{% endtabs %}