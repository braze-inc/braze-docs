# アンインストール追跡

> アンインストール追跡では、Firebase Cloud Messaging からのサイレントプッシュを利用して、アンインストールされたデバイスを検出します。Braze はアンインストール追跡通知をインテリジェントに削除し、通常のサイレントプッシュインテントを使用してアプリ内のカスタムプッシュコールバックを起動しません。この記事では、Android または FireOS アプリケーションのアンインストール追跡を構成する方法について説明します。

プッシュ通知が自分自身をアンインストール追跡しているかどうかを検出したい場合は、[`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html)を使用します。

{% alert important %}
アンインストール追跡サイレントプッシュは Braze プッシュコールバックに転送されないため、このメソッドは、カスタムの [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) を使用する場合など、プッシュ通知が Braze に渡される前にのみ使用できます。
{% endalert %}

カスタムの[`Application`](https://developer.android.com/reference/android/app/Application)サブクラスがある場合、サーバーに ping を送る自動ロジックが[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())ライフサイクルメソッドにないことを確認してください。 これは、アプリがまだ実行されていない場合に、サイレントプッシュによってアプリが起動され、`Application`コンポーネントがインスタンス化されるためです。

詳細については、ユーザーガイドの[アンインストール追跡]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking)を参照してください。

