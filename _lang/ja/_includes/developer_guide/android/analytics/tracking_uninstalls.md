## アンインストール追跡の設定

### ステップ 1: FCMの設定

Android Braze SDKは、Firebase Cloud Messaging (FCM)を使用してサイレントプッシュ通知を送信し、アンインストール追跡分析を収集するために使用される。まだの場合は、プッシュ通知のためにFirebase Cloud Messaging APIを[設定]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications)するか、[移行する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)。

### ステップ 2:手動でアンインストール追跡を検出する（オプション）

デフォルトでは、Android Braze SDKは、アンインストール追跡に関連するサイレントプッシュ通知を自動的に検出し、無視する。しかし、手動でアンインストール追跡を検出するには、以下の方法を選択する。 [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html)メソッドを使う。

{% alert important %}
アンインストール追跡用のサイレント通知は、Brazeのプッシュコールバックには転送されないため、このメソッドを使用できるのは、プッシュ通知をBrazeに渡す前だけである。
{% endalert %}

### ステップ 3:自動サーバーpingを削除する

サイレント・プッシュ通知はアプリを目覚めさせ、アプリがまだ実行中でなければ、`Application` コンポーネントをインスタンス化する。従って、もし顧客に [`Application`](https://developer.android.com/reference/android/app/Application)カスタム・サブクラスがある場合は、ライフサイクル・メソッド中に自動的にサーバーにpingを送るロジックをすべて削除する。 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())ライフサイクル・メソッド中に

### ステップ 4: アンインストール追跡を有効にする

最後に、Brazeでアンインストール追跡を有効にする。完全なチュートリアルについては、[アンインストール追跡を有効にするを]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking)参照のこと。

{% alert important %}
アンインストールの追跡は不正確な場合がある。Brazeに表示される指標は、遅れたり不正確であったりする可能性がある。
{% endalert %}
