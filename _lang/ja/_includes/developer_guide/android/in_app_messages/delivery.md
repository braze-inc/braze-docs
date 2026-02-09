{% multi_lang_include developer_guide/prerequisites/android.md %}

## メッセージトリガー

### トリガーの種類

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録すると自動的にトリガーされる：`Any Purchase` `Specific Purchase` 、`Session Start` 、`Custom Event` 、`Push Click` 。`Specific Purchase` 、`Custom Event` のトリガーには、ロバストなプロパティフィルターも含まれている。

{% alert note %}
アプリ内メッセージは、API または API イベントによってトリガーすることはできません。SDK によってログに記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

### 配信セマンティクス

対象となるアプリ内メッセージはすべて、セッション開始時にユーザーの端末に配信される。SDKは配信時にアセットをプリフェッチするため、トリガー時にアセットを利用でき、表示レイテンシを最小限に抑えることができる。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。

SDKのセッション開始セマンティクスの詳細については、セッション[ライフサイクルを]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android)参照のこと。

### レート制限

デフォルトでは、アプリ内メッセージのレート制限を30秒ごとに1回に設定して、ユーザーの質の高い体験をサポートしています。

この値をオーバーライドするには、`braze.xml` で `com_braze_trigger_action_minimum_time_interval_seconds` を次のように設定します。

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## キーと値のペア

Braze でキャンペーンを作成する場合は、キーと値のペアを `extras` として設定できます。これは、アプリ内メッセージングオブジェクトがアプリにデータを送信するために使用できます。以下に例を示します。

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) を参照してください。
{% endalert %}

## 自動トリガーを無効にする

アプリ内メッセージが自動的にトリガーされないようにする：

1. 自動統合初期化機能を使用していることを確認してください。この機能は、バージョン `2.2.0` 以降でデフォルトで有効になっています。
2. 次の行を `braze.xml` ファイルに追加することで、アプリ内メッセージ操作のデフォルトを `DISCARD` に設定します。

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## 手動でメッセージをトリガーする

デフォルトでは、アプリ内メッセージは SDK がカスタムイベントを記録したときに自動的にトリガーます。しかし、以下の方法を使えば、手動でメッセージをトリガーすることができる。

### サーバー側のイベントを使用する

サーバー送信イベントを使用してアプリ内メッセージをトリガーするには、サイレントプッシュ通知をデバイスに送信し、カスタムプッシュコールバックがSDKベースのイベントをログに記録できるようにする。このイベントは、その後、ユーザー向けのアプリ内メッセージをトリガーします。

#### ステップ1:サイレントプッシュを受信するプッシュコールバックを作成する

特定のサイレントプッシュ通知をリッスンするために、[カスタムプッシュイーブンコールバックを]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback)登録する。

以下の例では、アプリ内メッセージが配信されるために2つのイベントが記録される。1つはサーバーから、もう1つはカスタムプッシュコールバックからだ。同じイベントが重複しないようにするには、プッシュコールバック内からログに記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの一般的な命名規則に従う必要があります。そうしないと、単一のユーザーアクションについてログに記録される重複イベントによって、セグメンテーションとユーザーデータが影響を受ける可能性があります。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### ステップ 2:プッシュキャンペーンを作成する

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を作成します。

![]({% image_buster /assets/img_archive/serverSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![2組のキーと値のペア：IS_SERVER_EVENT は "true "に設定され、CAMPAIGN_NAME は "example campaign name "に設定されている。]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

前出のプッシュコールバックサンプルコードは、キーと値のペアを認識して、適切な SDK カスタムイベントをログに記録します。

「アプリ内メッセージトリガー」イベントに添付するイベントプロパティを含めるには、プッシュペイロードのキーと値のペアでプロパティを渡します。この例では、後続のアプリ内メッセージのキャンペーン名が含められています。カスタムプッシュコールバックは、カスタムイベントをログに記録するときに、イベントプロパティのパラメーターとして値を渡すことができます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信が必要であり、カスタムプッシュコールバック内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

!["campaign_name" "IAMキャンペーン名の例 "と等しい場合にアプリ内メッセージがトリガーされるアクションベースの配信キャンペーン。]({% image_buster /assets/img_archive/iam_event_trigger.png %})

アプリがフォアグラウンドにないときにサーバー送信イベントがログに記録されると、イベントはログに記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドになるまでイベントを無視または遅延させる必要があります。

### 事前定義されたメッセージを表示する

事前定義したアプリ内メッセージを手動で表示するには、以下の方法を使用します。

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### リアルタイムでメッセージを表示する 

また、ダッシュボードで利用できるのと同じカスタマイズオプションを使って、アプリ内メッセージをリアルタイムで作成・表示することもできる。そのために必要なこと:

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
ソフトキーボードが画面に表示されているときは、レンダリングが定義されていないため、アプリ内メッセージを表示しないでください。
{% endalert %}
