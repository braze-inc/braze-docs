{% multi_lang_include developer_guide/prerequisites/android.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)を設定する必要があります。

## プッシュイベントにコールバックを使用する {#push-callback}

Braze には、プッシュ通知が受信されたとき、開かれたとき、または却下されたときのための [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) コールバックが用意されています。アプリケーションが実行されていないときに発生するイベントを見逃さないように、このコールバックを `Application.onCreate()` に配置することをお勧めします。

{% alert note %}
以前にアプリケーションでこの機能にカスタムブロードキャストレシーバーを使用していた場合は、この統合オプションを優先して、レシーバーを削除しても問題ありません。
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
通知アクションボタンを使用すると、`opens app` または `deep link` アクションを持つボタンがクリックされると、`BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントが起動します。ディープリンクとエクストラの処理は変わりません。`close` アクション付きのボタンは `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` インテントを起動せず、通知を自動的に閉じます。
{% endalert %}

{% alert important %}
`Application.onCreate` でプッシュ通知リスナーを作成し、アプリが終了状態にある間にエンドユーザーが通知をタップした後にリスナーがトリガーされるようにします。
{% endalert %}

## 通知の表示のカスタマイズ

### ステップ 1: カスタム通知ファクトリーを作成する

サーバー側では面倒な方法や利用できない方法でプッシュ通知をカスタマイズしたい場合があります。通知表示を完全に制御できるよう追加された機能により、独自の [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) を定義して Braze で表示する通知オブジェクトを作成できるようになりました。

カスタムの `IBrazeNotificationFactory` が設定されている場合、ユーザーに通知が表示される前に、プッシュ受信時に Braze がファクトリーの `createNotification()` メソッドを呼び出します。Braze は、Braze プッシュデータを含む `Bundle` と、ダッシュボードまたはメッセージング API 経由で送信されたカスタムのキーと値のペアを含む別の `Bundle` を渡します。

Braze は、Braze プッシュ通知からのデータを含む[`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) を渡します。

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

カスタムの `createNotification()` メソッドから `null` を返して通知をまったく表示しないことも、`BrazeNotificationFactory.getInstance().createNotification()` を使用してそのデータのデフォルトの `notification` オブジェクトを取得し、表示前に変更することも、完全に別個の `notification` オブジェクトを生成して表示することもできます。

{% alert note %}
Braze のプッシュデータキーに関するドキュメントは、[Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html) を参照してください。
{% endalert %}

### ステップ 2:カスタム通知ファクトリーを設定する

Braze にカスタム通知ファクトリーを使用するように指示するには、`setCustomBrazeNotificationFactory` メソッドを使用して [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) を設定します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

カスタム `IBrazeNotificationFactory` を設定する場所として推奨されるのは、`Application.onCreate()` アプリケーションのライフサイクルメソッド (アクティビティではない) です。これにより、アプリプロセスがアクティブなときはいつでも通知ファクトリーを正しく設定できるようになります。

{% alert important %}
ゼロから独自の通知を作成するのは高度なユースケースです。十分なテストを行い、Braze のプッシュ機能を深く理解した上で行うようにしてください。たとえば、通知がプッシュ通知の開封数を正しくログに記録することを確認する必要があります。
{% endalert %}

カスタム [ の設定を解除し、プッシュのデフォルトの Braze 処理に戻すには、`IBrazeNotificationFactory` をカスタム通知ファクトリー設定機能に渡します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## マルチカラーテキストのレンダリング

Braze SDK 3.1.1 では、プッシュ通知 s でマルチカラーテキストをレンダリングするためにHTMLを装置に送信できます。

![文字に複数の異なる色、斜体、背景色が指定された、Android プッシュ通知メッセージ「マルチカラープッシュテストメッセージ」。]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

この例は、以下の HTML でレンダリングされます。

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

プッシュ通知sで有効なHTML要素とタグsをAndroid制限することに注意してください。たとえば、`marquee` は使用できません。

{% alert important %}
マルチカラーテキストレンダリングはデバイス固有であり、Androidのデバイスまたはバージョンに基づいて表示されない場合があります。
{% endalert %}

プッシュ通知でマルチカラーテキストをレンダリングするには、`braze.xml` または`BrazeConfig` を更新します。

{% tabs local %}
{% tab braze.xml %}
`braze.xml` に以下を追加します。

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
[`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration) に以下を追加します。

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 対応HTML タグ

現在、Google はAndroid でサポートされているHTML タグをドキュメントに直接的に一覧表示しません。この情報は、[Git リポジトリの`Html.java` file](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) にのみ表示されます。この情報はこのファイルから取得され、サポートされているHTML タグs は変更される可能性があるため、次のテーブルを参照するときはこの点に注意してください。

<table>
  <thead>
    <tr>
      <th>カテゴリー</th>
      <th>HTMLタグ</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">基本的なテキストスタイル</td>
      <td><code></td>
      <td>太字のテキスト</td>
    </tr>
    <tr>
      <td><code></td>
      <td>斜体テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;u></code></td>
      <td>テキストの下線</td>
    </tr>
    <tr>
      <td><code></td>
      <td>テキストを取り消す</td>
    </tr>
    <tr>
      <td><code>&lt;sup></code></td>
      <td>上付き文字</td>
    </tr>
    <tr>
      <td><code>&lt;sub></code></td>
      <td>添え字テキスト</td>
    </tr>
    <tr>
      <td><code>&lt;tt></code></td>
      <td>モノスペーステキスト</td>
    </tr>
    <tr>
      <td rowspan="3">サイズ/フォント</td>
      <td><code></td>
      <td>相対テキストサイズの変更</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."></code></td>
      <td>前景色を設定する</td>
    </tr>
    <tr>
      <td><code>&lt;span></code> (インラインCSS付き)</td>
      <td>インラインスタイル(e.g.カラー、バックグラウンド)</td>
    </tr>
    <tr>
      <td rowspan="4">段落&amp;アンプ;ブロック</td>
      <td><code></td>
      <td>ブロックレベルのセクション</td>
    </tr>
    <tr>
      <td><code>&lt;br></code></td>
      <td>改行</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote></code></td>
      <td>引用ブロック</td>
    </tr>
    <tr>
      <td><code></td>
      <td>行頭記号付きの順序なしリスト</td>
    </tr>
    <tr>
      <td>表題</td>
      <td><code></td>
      <td>見出し(各種サイズ)</td>
    </tr>
    <tr>
      <td rowspan="2">リンク&amp;アンプ;画像</td>
      <td><code>&lt;a href="..."></code></td>
      <td>クリック可能なリンク</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."></code></td>
      <td>インライン画像</td>
    </tr>
    <tr>
      <td>その他インライン</td>
      <td><code></td>
      <td>斜体または太字の同義語</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## インライン"画像のレンダリング

### 仕組み

インライン"画像プッシュを使用して、Android プッシュ通知内の大きな"画像を表示できます。この設計により、ユーザーは画像を拡大するために手動でプッシュを拡大する必要がなくなります。通常の Android プッシュ通知とは異なり、インライン画像プッシュ画像の縦横比は 3:2 です。

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### 互換性

インライン"画像s を任意のデバイスに送信できますが、最低限のバージョンを満たしていないデバイスやSDKでは、代わりに通常の"画像が表示されます。インライン"画像s を正しく表示するには、Android Braze SDK v10.0.0+ とAndroid M+ を実行する機器の両方が必要です。"画像をレンダリングするには、SDKも有効にする必要があります。

{% alert note %}
Android 12 を実行しているデバイスでは、カスタムプッシュ通知スタイルの変更によりレンダリングが異なります。
{% endalert %}

### インライン"画像プッシュの送信

Android プッシュメッセージを作成する場合、この機能は [**通知タイプ**] ドロップダウンで使用できます。

![「通知タイプ」ドロップダウン (標準のプッシュプレビューの上) の場所を示すプッシュキャンペーンエディター。]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})()

## 設定

Braze ダッシュボードを介して送信されるAndroid プッシュ通知には、多くの高度な設定が利用可能です。この記事では、これらの機能とそれらを効果的に使用する方法について説明します。

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### 通知 ID {#notification-id}

**通知 ID** は、選択したメッセージカテゴリの一意の識別子です。その ID からの最新のメッセージのみを尊重するようメッセージングサービスに通知する役割を果たします。通知 ID を設定すると、古くて無関係なメッセージのスタックではなく、最新で関連性の高いメッセージだけを送信できます。

### Firebase メッセージング配信の優先度 {#fcm-priority}

[Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) フィールドでは、「通常」または「高」のどちらの優先度でプッシュを Firebase Cloud Messaging に送信するかを制御できます。

### 有効時間 (TTL) {#ttl}

**有効期間** (TTL) フィールドを使用すると、プッシュメッセージングサービスでメッセージを保存する期間をカスタム設定できます。有効期間のデフォルト値は、FCM の場合は 4 週間、ADM の場合は 31 日です。

### 要約テキスト {#summary-text}

要約テキストを使用すると、拡張通知ビューに追加のテキストを設定できます。画像付きの通知のキャプションとしても機能します。

![タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」の Android メッセージ。]({% image_buster /assets/img/android/push/collapsed-android-notification.png %})({: style="max-width:65%;"})

要約テキストは、展開されたビューのメッセージ本文の下に表示されます。 

![タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」の Android メッセージ。]({% image_buster /assets/img/android/push/expanded-android-notification.png %})({: style="max-width:65%;"})

画像を含むプッシュ通知の場合、折りたたまれたビューにはメッセージテキストが表示され、通知が展開されると、要約テキストが画像のキャプションとして表示されます。 

### カスタム URI {#custom-uri}

**カスタム URI** 機能を使用すると、通知がクリックされたときの誘導先 Web URL または Android リソースを指定できます。カスタム URI が指定されていない場合、通知をクリックするとユーザーはアプリに誘導されます。カスタム URI を使用してアプリ内でディープリンクし、アプリ外部のリソースにユーザーを誘導することができます。この設定は、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュ作成画面の「**詳細設定**」から行うことができる：

![Braze プッシュコンポーザーのディープリンクの高度な設定。]({% image_buster /assets/img_archive/deep_link.png %})

### 通知の表示優先度 {#notification-priority}

{% alert important %}
通知の表示優先度設定は、Android O 以降を実行しているデバイスでは使用されなくなりました。新しいデバイスの場合は、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance)を使用して優先度を設定します。
{% endalert %}

プッシュ通知の優先度レベルは、通知トレイ内で他の通知と比較して通知がどのように表示されるかに影響します。また、通常のメッセージや優先度の低いメッセージは、バッテリー寿命を延ばすために遅延がわずかに長くなったり、バッチ処理で送信されたりするのに対し、優先度の高いメッセージは常に即座に送信されるため、配信の速度と方法にも影響する可能性があります。

Android O では、通知の優先度が通知チャネルのプロパティになりました。開発者と協力して設定中にチャネルの優先度を定義し、ダッシュボードを使用して通知音を送信するときに適切なチャネルを選択する必要があります。Android がO より前のバージョンで動作している機器では、Android 通知 s のプライオリティレベルをBraze ダッシュボード およびメッセージング API で指定できます。 

特定の優先度でユーザーベース全体にメッセージを送信するには、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance) (ターゲットO+ デバイスへ) で間接的に優先度を指定し、ダッシュボード(ターゲット<O デバイスへ) から個々の優先度を送信することをお勧めします。

Android または Fire OS プッシュ通知で設定できる優先度レベルは次のとおりです。

| 優先順位 | 説明／使用目的 | `priority` 値 (API メッセージ用) |
|----------|--------------------------|-------------------------------------|
| マックス      | 緊急または一刻を争うメッセージ | `2` |
| 高     | 友人からの新着メッセージなど、重要なコミュニケーション | `1` |
| デフォルト  | ほとんどの通知 - メッセージが他の優先度タイプのいずれにも明示的に該当しない場合に使用します | `0` |
| 低      | ユーザーに知ってもらいたいが、すぐに行動を起こす必要のない情報 | `-1` |
| 最小      | コンテキストまたは背景情報 | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細については、グーグルの[Android 通知](http://developer.android.com/design/patterns/notifications.html)ドキュメントを参照してください。

### サウンド {#sounds}

Android O では、通知音は通知チャネルのプロパティになりました。開発者と協力して設定時にチャネルのサウンドを定義し、通知を送信するときにダッシュボードを使用して適切なチャネルを選択する必要があります。

Android O より前のバージョンを実行しているデバイスの場合、Braze を使用すると、ダッシュボードコンポーザーを通じて個々のプッシュメッセージのサウンドを設定できます。これを行うには、デバイスのローカルサウンドリソースを指定します (例: `android.resource://com.mycompany.myapp/raw/mysound`)。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュ作成画面の「**詳細設定**」で指定できる。

![Braze プッシュコンポーザーのサウンドの高度な設定。]({% image_buster /assets/img_archive/sound_android.png %})

完全なサウンドリソース URI (例: `android.resource://com.mycompany.myapp/raw/mysound`) をダッシュ​​ボードプロンプトに入力します。

特定のサウンドでフルユーザーベースにメッセージを送るには、[通知チャネル設定](https://developer.android.com/training/notify-user/channels)(ターゲットO+ デバイスへ)でサウンドを間接的に指定し、ダッシュボードから個別のサウンド(ターゲット<O デバイスへ)を送ることをお勧めします。
