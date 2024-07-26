---
nav_title: プッシュ・コールバック・ブロードキャスト・レシーバー
article_title: Android用カスタム・ブロードキャスト・レシーバー・プッシュ・コールバック
description: "このリファレンス記事では、Androidプッシュ通知用のカスタムBroadcastレシーバーの作成について説明する。"
---

# ブロードキャスト・レシーバーを介したプッシュ受信、開封、却下、キーと値のペアのカスタム・ハンドリング {#android-push-listener-broadcast-receiver}

{% alert important %}
プッシュ通知にカスタム`BroadcastReceiver` を使用することは廃止された。代わりに [` subscribeToPushNotificationEvents()`](/docs/developer_guide/platform_integration_guides/android/push_notifications/android/customization/custom_event_callback/)で代用する。
{% endalert %}

Brazeはまた、プッシュ通知の受信、開封、解除時にカスタムインテントをブロードキャストする。これらのシナリオの特定のユースケース（カスタムキーと値のペアやディープリンクの独自の処理をリッスンする必要性など）がある場合は、カスタム`BroadcastReceiver` を作成することによって、これらのインテントをリッスンする必要がある。

## ステップ 1:BroadcastReceiverを登録する

カスタム`BroadcastReceiver` を登録し、Brazeのプッシュ開封と受信インテントをリッスンする。 [`AndroidManifest.xml`][71]:

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

レシーバーは、Brazeからブロードキャストされたインテントを処理し、アクティビティを起動する：

- をサブクラス化すべきである。 [`BroadcastReceiver`][53]`onReceive()`をオーバーライドする必要がある。
- `onReceive()` メソッドは、Brazeからブロードキャストされるインテントをリッスンする必要がある。
  - プッシュ通知が届くと、`NOTIFICATION_RECEIVED` インテントを受信する。
  - ユーザーがプッシュ通知をクリックすると、`NOTIFICATION_OPENED` インテントを受信する。
  - `NOTIFICATION_DELETED` インテントは、プッシュ通知がユーザーによって却下（スワイプして離す）されたときに受信される。
- これらのケースごとに、あなたのカスタムロジックを実行する必要がある。受信機がディープリンクを開封する場合は、`braze.xml` で`com_braze_handle_push_deep_links_automatically` を`false` に設定し、ディープリンクの自動開封をオフにしておくこと。

詳細なカスタムレシーバーの例については、以下のコードスニペットを参照のこと：

{% tabs %}
{% tab ジャワ %}

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
{% tab コトリン %}

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

ダッシュボードまたはメッセージングAPIを介して送信されたカスタムキーと値のペアは、あなたが選択した任意の目的のために、カスタムブロードキャストレシーバでアクセスできるようになる：

{% tabs %}
{% tab ジャワ %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab コトリン %}

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

[53]: https://developer.android.com/reference/android/content/BroadcastReceiver.html
[71]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml "AndroidManifest.xml"
