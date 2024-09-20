---
nav_title: アプリ内メッセージ配信
article_title: Android と FireOS のアプリ内メッセージ配信
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android と FireOS のアプリ内メッセージ配信について説明し、さまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。"
channel:
  - in-app messages

---

# アプリ内メッセージ配信

> このリファレンス記事では、Android と FireOS のアプリ内メッセージ配信について説明し、さまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。

## トリガーの種類

アプリ内メッセージ製品を使用すると、いくつかの異なるイベントタイプ (`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、`Push Click`) によってアプリ内メッセージの表示をトリガーできます。さらに、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターを含めることができます。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。[カスタムイベントをログに記録する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)方法を確認してください。
{% endalert %}

## 配信セマンティクス

ユーザーが対象となるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます][84]。配信時に、SDK はアセットをプリフェッチしてトリガー時にすぐに利用できるようにし、表示遅延を最小限に抑えます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

アセットがプリフェッチされていないため、配信 (セッション開始、プッシュクリックなど) 時にすぐに表示されるアプリ内メッセージには多少の遅延が発生する可能性があります。

## トリガー間の最小時間間隔

デフォルトでは、アプリ内メッセージのレート制限を30秒ごとに1回に設定して、ユーザーの質の高い体験をサポートしています。

この値をオーバーライドするには、`braze.xml` で `com_braze_trigger_action_minimum_time_interval_seconds` を次のように設定します。

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## サーバー側のイベントトリガー

デフォルトでは、アプリ内メッセージは SDK によって記録されるカスタムイベントによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合にも実現できます。

この機能を有効にするには、デバイスにサイレントプッシュを送信し、カスタムプッシュコールバックで SDK ベースのイベントをログに記録できるようにします。この SDK イベントは、その後、ユーザー向けのアプリ内メッセージをトリガーします。

### ステップ1:サイレントプッシュを受信するプッシュコールバックを作成する

特定のサイレントプッシュ通知をリッスンするには、カスタムプッシュコールバックを登録します。詳細については、\[標準のAndroidプッシュ統合][78]をご参照ください。

配信されるアプリ内メッセージに関して 2 つのイベントが記録されます。1 つはサーバーによって記録され、もう 1 つはカスタムプッシュコールバック内から記録されます。同じイベントが重複しないようにするには、プッシュコールバック内からログに記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの一般的な命名規則に従う必要があります。そうしないと、単一のユーザーアクションについてログに記録される重複イベントによって、セグメンテーションとユーザーデータが影響を受ける可能性があります。

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

### ステップ2:プッシュキャンペーンを作成する

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン][73]を作成します。

![][75]

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンが SDK カスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![キーと値のペアの2つのセット:IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example キャンペーン name".][76]{: style="max-width:70%;" }

前出のプッシュコールバックサンプルコードは、キーと値のペアを認識して、適切な SDK カスタムイベントをログに記録します。

「アプリ内メッセージトリガー」イベントに添付するイベントプロパティを含めるには、プッシュペイロードのキーと値のペアでプロパティを渡します。この例では、後続のアプリ内メッセージのキャンペーン名が含められています。カスタムプッシュコールバックは、カスタムイベントをログに記録するときに、イベントプロパティのパラメーターとして値を渡すことができます。

### ステップ3:アプリ内メッセージキャンペーンを作成する

Braze ダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信が必要であり、カスタムプッシュコールバック内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![アクションベースの配信キャンペーンで、「campaign_name」が「IAM キャンペーン名の例」と等しい場合にアプリ内メッセージがトリガーされます。][77]

アプリがフォアグラウンドにないときにサーバー送信イベントがログに記録されると、イベントはログに記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドになるまでイベントを無視または遅延させる必要があります。

## ローカルのアプリ内メッセージ

アプリ内メッセージはアプリ内で作成し、リアルタイムでローカルに表示できます。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。

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

### アプリ内メッセージ表示を手動でトリガーする

次のメソッドは、アプリ内メッセージを手動で表示します。

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

[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[75]: {% image_buster /assets/img_archive/serverSentPush.png %}
[76]: {% image_buster /assets/img_archive/kvpConfiguration.png %}
[77]: {% image_buster /assets/img_archive/iam_event_trigger.png %}
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[84]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
