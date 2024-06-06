---
nav_title: プッシュ通知
article_title: React Native のプッシュ通知
platform: React Native
page_order: 2
description: "この記事では、React Native でのプッシュ通知の実装について説明します。"
channel: push

---

# プッシュ通知の統合

> この参考記事では、React Native のプッシュ通知を設定する方法について説明します。プッシュ通知を統合するには、各ネイティブプラットフォームを個別に設定する必要があります。リストされているそれぞれのガイドに従って、インストールを完了します。

## プッシュ通知の統合

### 前提条件

どの iOS 統合方法でも、最初に APNs 証明書を生成し、それを Braze ダッシュボードにアップロードしていることを確認してください。Apple からの既存のプッシュキーまたは証明書がない場合、または新しいものを生成したい場合は、[Swift 統合の手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)に従ってください。

### ステップ 1 ネイティブセットアップを完了する

{% tabs %}
{% tab Expo %}

iOS および Android のプッシュをそれぞれ有効にするには、`app.json` ファイルの `enableBrazeIosPush` および `enableFirebaseCloudMessaging` オプションを設定します。詳細については、[こちら]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup)の設定手順を参照してください。

[Expo 通知](https://docs.expo.dev/versions/latest/sdk/notifications/)などの追加のプッシュ通知ライブラリに依存している場合は、ネイティブのセットアップ手順ではなく、これらの設定を使用する必要があることに注意してください。

{% endtab %}
{% tab Android %}

[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)に従ってください。

#### ステップ1.1a
`app.json` で `firebaseCloudMessagingSenderId` 構成プロパティを設定します。送信者 ID の取得については、[Android 統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-set-your-firebase-credentials)を参照してください。

#### ステップ1.2a
`google-services.json` ファイルパスを `app.json` に追加します。このファイルは、お客様の構成で `enableFirebaseCloudMessaging: true` を設定する場合に必要です。

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

{% endtab %}
{% tab iOS %}

[iOS 統合の手順](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications/)に従って Swift に実装するか、Swift または Objective-C で実装する手順については、[プッシュ通知の統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)を参照してください。アプリの起動時にプッシュアクセス許可を要求しない場合は、AppDelegate の `requestAuthorizationWithOptions:completionHandler:` 呼び出しを省略し、次のステップに従います。

#### expo- 通知からプッシュキーを移行する
以前にプッシュキーの管理に `expo-notifications` を使用していた場合は、アプリケーションのルートフォルダーから `expo fetch:ios:certs` を実行してください。これにより、プッシュキー (a .p8 ファイル) がダウンロードされ、その後 Braze ダッシュボードにアップロードできるようになります。

{% endtab %}
{% endtabs %}

### ステップ2: プッシュ通知の許可をリクエストする

iOS および Android 13以降のユーザーにプッシュ通知の許可を要求するには、`Braze.requestPushPermission()` メソッド (v 1.38.0以降で使用可能) を使用します。Android 12以前の場合、このメソッドは何も実行しません。

このメソッドは、SDK が iOS 上のユーザーにどの権限を要求するかを指定する必須パラメーターを受け取ります。これらのオプションは Android には影響しません。

\`\`\`javascript
const permissionOptions = {
alert: true,
sound: true,
badge: true,
provisional: false
};

Braze.requestPushPermission(permissionOptions);
\`\`\`

#### Step 2.1: プッシュ通知をリッスンする (オプション)

さらに、Braze が受信プッシュ通知を検出して処理したイベントをサブスクライブすることもできます。リスナーキー `Braze.Events.PUSH_NOTIFICATION_EVENT` を使用します。

{% alert note %}
Braze プッシュ通知イベントは、Android と iOS の両方で利用できます。プラットフォームが異なるため、iOS はユーザーが通知を操作した場合にのみ Braze プッシュイベントを検出します。
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### プッシュ通知イベントフィールド

{% alert note %}
iOS のプラットフォーム制限のため、Braze SDK はアプリがフォアグラウンドにあるときにのみプッシュペイロードを処理できます。リスナーは、ユーザーがプッシュを操作した後、iOSで `push_opened` イベントタイプに対してのみトリガーされます。
{% endalert %}

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

|フィールド名 |タイプ |説明 |
| ------------------ | --------- | ----------- |
| `payload_type`|文字列 |通知ペイロードのタイプを指定します。Braze React Native SDK から送信される2つの値は `push_opened` と `push_received` です。 iOS では `push_opened` イベントのみがサポートされています。|
| `url`|文字列 |通知によって開かれた URL を指定します。 |
| `use_webview`|ブール値 | `true` の場合,URL はアプリ内でモーダル Web ビューで開きます。もし `false` の場合、URL がデバイスのブラウザーで開きます。 |
| `title`|文字列 |通知のタイトルを表します。 |
| `body`|文字列 |通知の本文またはコンテンツテキストを表します。 |
| `summary_text`|文字列 |通知の概要テキストを表します。これは iOS で `subtitle` からマップされます。|
| `badge_count`| 番号 |通知のバッジ数を表します。 |
| `timestamp`| 番号 |アプリケーションがペイロードを受信した時刻を表します。 |
| `is_silent`|ブール値 | `true` の場合、ペイロードはサイレントに受信されます。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications)を参照してください。iOS のサイレントプッシュ通知の送信の詳細については、[iOS のサイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)を参照してください。 |
| `is_braze_internal`|ブール値 | ジオフェンス同期、機能フラグ同期、またはアンインストールトラッキングなどの内部 SDK 機能に対して通知ペイロードが送信された場合、これは `true` になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `image_url`| 文字列 |通知画像に関連付けられた URL を指定します。 |
| `braze_properties` | オブジェクト |キャンペーンに関連付けられた Braze プロパティを表します (キーと値のペア)。 |
| `ios`| オブジェクト | iOS 固有のフィールドを表します。 |
| `android`| オブジェクト | Android 固有のフィールドを表します。 |
{: .reset-td-br-1 .reset-td-br-2}

### ステップ 3: ディープリンクを有効にする (オプション)

プッシュ通知がクリックされたときに Braze が React コンポーネント内のディープリンクを処理できるようにするには、追加の手順に従います。

{% tabs %}
{% tab Expo %}

[BrazeProject サンプル アプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)には、実装されたディープリンクの完全な例が含まれています。ディープリンクの詳細については、[FAQ の記事を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)参照してください。

{% endtab %}
{% tab Android %}

#### ステップ 3.1a: ディープリンクを自動的に処理する

Android の場合、ディープリンクの設定は [、ネイティブ Android アプリでのディープリンクの設定]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links)と同じです。Braze SDK でプッシュディープリンクを自動的に処理する場合は、`app.json` で `androidHandlePushDeepLinksAutomatically: true` を設定します。

{% endtab %}
{% tab iOS %}

#### ステップ3.1b: `populateInitialUrlFromLaunchOptions` を追加する

iOS の場合は、AppDelegate の `didFinishLaunchingWithOptions` メソッドに `populateInitialUrlFromLaunchOptions` を追加します。 

例えば:

\`\`\`objc
\- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration \*configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze \*braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
\`\`\`

#### ステップ 3.2b: `getInitialURL()` を追加する

ディープリンクがアプリを開いたときに処理する `Linking.getInitialURL()` メソッドを追加します。

また、アプリが実行されていないときに iOS プッシュ通知のクリックからディープリンクを処理するには、`Braze.getInitialURL` メソッドを呼び出す必要があります。アプリ起動時の競合状態が原因で、React Native の Linking API がこのシナリオをサポートしていないため、Braze はこの回避策を提供します。

例えば:

\`\`\`javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// iOS アプリがプッシュクリックによってハードクローズされた状態から起動されるときに、ディープリンクを処理します。
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
\`\`\`

{% endtab %}
{% endtabs %}

### ステップ4: プッシュ通知の表示をテストする

この時点で、デバイスに通知を送信できるはずです。次のステップに従って、プッシュ統合をテストします。

{% alert note %}
macOS 13以降の特定のデバイスでは、Xcode 14以降で実行されている iOS 16以降のシミュレーターで iOS プッシュ通知をテストできます。詳細については、[Xcode 14 リリース ノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。まもなくデバイスに通知が届くはずです。

![プッシュ通知をテストするために、テスト受信者として独自のユーザー ID を追加できることを示す Braze プッシュ キャンペーン。][1]

## リッチプッシュ通知を有効にする (iOS)

Android では、デフォルトでリッチプッシュ通知を利用できます。Expo を使用して iOS でリッチプッシュ通知を有効にするには、`app.json` の `expo.plugins` オブジェクトで `enableBrazeIosRichPush` プロパティを `true` に構成します。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

## プッシュストーリーを有効にする (iOS)

プッシュ ストーリーは Android でデフォルトで利用可能です。Expo を使用して iOS でプッシュ ストーリーを有効にするには、アプリケーションにアプリグループが定義されていることを確認してください。詳細については、[アプリグループの追加][4] を参照してください。

次に、`enableBrazeIosPushStories` プロパティを `true` に構成し、`app.json` の `expo.plugins` オブジェクトの `iosPushStoryAppGroup` にアプリグループ ID を割り当てます。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

## Android プッシュ通知を別の FirebaseMessagingService に転送する

使用したい別の Firebase メッセージングサービスがある場合は、アプリケーションが Braze からではないプッシュを受信した場合に呼び出すフォールバック Firebase メッセージングサービスを指定することもできます。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

[1]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"
[2]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications/
[3]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group
