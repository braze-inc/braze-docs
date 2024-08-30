---
nav_title: アンインストール追跡
article_title: Android と FireOS のアンインストール追跡
platform: 
  - Android
  - FireOS
page_order: 7
description: "この記事では、Android または FireOS アプリケーションのアンインストール追跡を構成する方法について説明します。"

---

# アンインストール追跡

> アンインストール追跡は、Firebase Cloud Messagingからのサイレントプッシュを使用して、アンインストールされたデバイスを検出する。Braze はアンインストール追跡通知をインテリジェントに削除し、通常のサイレントプッシュインテントを使用してアプリ内のカスタムプッシュコールバックを起動しません。この記事では、Android または FireOS アプリケーションのアンインストール追跡を構成する方法について説明します。

プッシュ通知が自分自身をアンインストール追跡しているかどうかを検出したい場合は、[`isUninstallTrackingPush()`][3]を使用します。

{% alert important %}
アンインストール追跡サイレントプッシュは Braze プッシュコールバックに転送されないため、このメソッドは、カスタムの [Firebase Messaging Service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-register-braze-firebase-messaging-service) を使用する場合など、プッシュ通知が Braze に渡される前にのみ使用できます。
{% endalert %}

カスタムの[`Application`][1]サブクラスがある場合、サーバーに ping を送る自動ロジックが[`Application.onCreate()`][2]ライフサイクルメソッドにないことを確認してください。 これは、アプリがまだ実行されていない場合に、サイレントプッシュによってアプリが起動され、`Application`コンポーネントがインスタンス化されるためです。

詳細については、ユーザーガイドの[アンインストール追跡][4]を参照してください。

[1]: https://developer.android.com/reference/android/app/Application
[2]: https://developer.android.com/reference/android/app/Application#onCreate()
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/is-uninstall-tracking-push.html
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking
