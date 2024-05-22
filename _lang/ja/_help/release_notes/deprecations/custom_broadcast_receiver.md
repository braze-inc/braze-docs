---
nav_title: プッシュコールバックブロードキャストレシーバ
article_title: Android 用カスタムブロードキャストレシーバープッシュコールバック
description: "この参考記事では、Android プッシュ通知用のカスタムブロードキャストレシーバーの作成について説明しています。"
---

# Broadcast Receiverによるプッシュ受信、オープン、却下、およびキーと値のペアのカスタム処理 {#android-push-listener-broadcast-receiver}

{% alert important %}
`BroadcastReceiver`プッシュ通知にカスタムを使用することは廃止されました。[` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/)代わりに使用してください。
{% endalert %}

また、Braze はプッシュ通知の受信、開封、または却下時にカスタムインテントをブロードキャストします。これらのシナリオで特定のユースケース（カスタムのキーと値のペアを監視する必要がある場合や、ディープリンクの独自の処理が必要な場合など）がある場合は、カスタムを作成してこれらの意図に耳を傾ける必要があります。`BroadcastReceiver`

## ステップ 1:放送受信機を登録する

カスタムを登録すると`BroadcastReceiver`、以下の画面で Braze のプッシュが開いて受信したインテントを聞くことができます。[`AndroidManifest.xml`][71]

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## ステップ 2:ブロードキャストレシーバーを作成

受信者は Braze によってブロードキャストされたインテントを処理し、その受信者でアクティビティを開始する必要があります。

- [`BroadcastReceiver`][53]`onReceive()`サブクラス化してオーバーライドする必要があります。
- `onReceive()`このメソッドは Braze によってブロードキャストされたインテントをリッスンする必要があります。
  - プッシュ通知が到着すると、`NOTIFICATION_RECEIVED`インテントが受信されます。
  - ユーザーがプッシュ通知をクリックすると、`NOTIFICATION_OPENED`インテントが受信されます。
  - ユーザーがプッシュ通知を閉じる (スワイプする) と、`NOTIFICATION_DELETED`インテントが受信されます。
- それぞれのケースでカスタムロジックを実行する必要があります。受信者がディープリンクを開く場合は、`com_braze_handle_push_deep_links_automatically``false`でに設定してディープリンクの自動開封を必ずオフにしてください`braze.xml`。

詳細なカスタムレシーバーの例については、次のコードスニペットを参照してください。

{% tabs %}
{% tab JAVA %}

\`\`\`ジャワ
パブリッククラスのカスタムブロードキャストレシーバはブロードキャストレシーバを拡張します {
  プライベート・スタティック・ファイナル・ストリング・タグ = customBroadcastReceiver.class.getName ();

  @Override
  パブリックボイドonReceive（コンテキストコンテキスト、インテントインテント）{
    String PushReceivedAction = Constants.Braze\_push\_intent\_notification\_Received;
    String notificationOpenedAction = Constants.Braze\_push\_intent\_notification\_open;
    String notificationDeletedAction = Constants.Braze\_push\_intent\_notification\_Deleted;

    String action = intent.getAction();
    Log.d(TAG, String.format("Received intent with action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log.d(TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent.");
    } else {
      Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action));
    }
  }
}
\`\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`コトリン
クラスカスタム放送受信機：ブロードキャストレシーバー () {
  onReceive でオーバーライドする (コンテキスト:コンテキスト、意図:意図) {
    val Push\_ReceivedAction = Constant.Braze\_Push\_Intent\_Notification\_Received
    val NotificationOpenedAction = Constants.Braze\_push\_intent\_notification\_open
    val notificationDeletedAction = Constants.Braze\_push\_intent\_notification\_Deleted

    val action = intent.action
    Log.d(TAG, String.format("Received intent with action %s", action))

    when (action) {
      pushReceivedAction -> {
        Log.d(TAG, "Received push notification.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action))
      }
    }
  }

  companion object {
private val TAG = CustomBroadcastReceiver::class.java.name
}
    }
  \`\`\`

{% endtab %}
{% endtabs %}

{% alert tip %}
通知アクションボタンでは、`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED``opens app``deep link`またはアクションの付いたボタンがクリックされたときにインテントが起動します。ディープリンクとエクストラの処理は変わりません。`close``BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`アクション付きのボタンはインテントを起動せず、通知を自動的に閉じます。
{% endalert %}

## ステップ 3:カスタムのキーと値のペアへのアクセス

ダッシュボードまたはメッセージAPIを介して送信されたカスタムキーと値のペアは、任意の目的でカスタムブロードキャストレシーバーからアクセスできます。

{% tabs %}
{% tab JAVA %}

\`\`\`ジャワ
//インテントは、カスタムブロードキャストレシーバーが受信する Braze プッシュインテントです。
String DeepLink = intent.getStringExtra (Constants.Braze\_push\_deep\_link\_key);

//インテントから抽出されたエクストラバンドルには、カスタムのキーと値のペアがすべて含まれています。
バンドルエクストラ = intent.getBundleExtra (Constants.Braze\_push\_Extras\_key);

//Extras バンドルから特定のキーと値のペアを取得する例。
String MyExtra = Extras.GetString (「my\_key」);
\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`コトリン
//インテントは、カスタムブロードキャストレシーバーが受信する Braze プッシュインテントです。
val DeepLink = intent.GetStringExtra (Constants.Braze\_push\_deep\_link\_key)

//インテントから抽出されたエクストラバンドルには、カスタムのキーと値のペアがすべて含まれています。
val extras = intent.getBundleExtra (Constants.Braze\_push\_Extras\_key)

//Extras バンドルから特定のキーと値のペアを取得する例。
val MyExtra = Extras.GetString (「my\_key」)
\`\`

{% endtab %}
{% endtabs %}

{% alert note %}
Braze プッシュデータキーに関するドキュメントについては、[Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants) を参照してください。
{% endalert %}

[53]: https://developer.android.com/reference/android/content/BroadcastReceiver.html
[71]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml "AndroidManifest.xml"
