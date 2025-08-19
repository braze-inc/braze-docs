---
nav_title: プッシュ・コールバック・ブロードキャスト・レシーバー
article_title: Android のカスタムブロードキャストレシーバープッシュコールバック
description: "この参考記事では、Android プッシュ通知用のカスタムブロードキャストレシーバーの作成について説明します。"
---

# ブロードキャストレシーバー {#android-push-listener-broadcast-receiver} を介したプッシュの受信、開封、却下、およびキーと値のペアのカスタム処理

{% alert important %}
プッシュ通知にカスタム`BroadcastReceiver` を使用することは廃止された。代わりに [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events)で代用する。
{% endalert %}

また、Braze は、プッシュ通知が受信、開封、または却下されたときにカスタムインテントをブロードキャストします。これらのシナリオに特定のユースケースがある場合 (カスタムのキーと値のペアをリッスンする必要がある場合や、ディープリンクを独自に処理する必要がある場合など)、カスタム `BroadcastReceiver` を作成してこれらのインテントをリッスンする必要があります。

## ステップ 1:BroadcastReceiverを登録する

カスタム`BroadcastReceiver` を登録して、[`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml) でBrazeプッシュ開封をリッスンし、インテントを受信します。

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## ステップ2:BroadcastReceiverを作成する

レシーバーは、Brazeからブロードキャストされたインテントを処理し、それを使ってアクティビティを起動する：

- これは [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) をサブクラス化し、`onReceive()` をオーバーライドする必要があります。
- `onReceive()` メソッドは、Braze でインテントブロードキャストをリッスンする必要があります。
  - プッシュ通知が届くと、`NOTIFICATION_RECEIVED` インテントを受信する。
  - ユーザーがプッシュ通知をクリックすると、`NOTIFICATION_OPENED` インテントが受信されます。
  - ユーザーがプッシュ通知を却下 （スワイプ） すると、`NOTIFICATION_DELETED` インテントが受信されます。
- これらのケースごとにカスタムロジックを実行する必要があります。受信者がディープリンクを開封する場合は、`braze.xml` で `com_braze_handle_push_deep_links_automatically` を`false` に設定し、自動ディープリンク開封を無効にしてください。

カスタム・レシーバーの詳細な例については、以下のコード・スニペットを参照のこと：

{% tabs %}
{% tab JAVA %}

```java
public class CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class.getName();

  @Override
  public void onReceive(Context context, Intent intent) {
    String pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED;

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
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    val notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    val notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED

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
```

{% endtab %}
{% endtabs %}

{% alert tip %}
通知アクションボタンを使用すると、`opens app` または `deep link` アクションを持つボタンがクリックされると、`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントが起動します。ディープリンクとエクストラの処理は変わりません。`close` アクション付きのボタンは `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントを起動せず、通知を自動的に閉じます。
{% endalert %}

## ステップ 3:カスタムキーと値のペアにアクセスする

ダッシュボード またはメッセージング API を介して送信されたカスタムキーと値のペアは、選択した用途に応じてカスタムブロードキャストレシーバでアクセス可能になります。

{% tabs %}
{% tab JAVA %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// intent is the Braze push intent received by your custom broadcast receiver.
val deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY)

// The extras bundle extracted from the intent contains all custom key-value pairs.
val extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY)

// example of getting specific key-value pair from the extras bundle.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Braze のプッシュデータキーに関するドキュメントは、[Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants) を参照してください。
{% endalert %}

