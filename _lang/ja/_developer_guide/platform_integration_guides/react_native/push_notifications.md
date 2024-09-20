---
nav_title: プッシュ通知
article_title: React Native のプッシュ通知
platform: React Native
page_order: 2
toc_headers: h2
description: "この記事では、React Native でのプッシュ通知の実装について説明します。"
channel: push

---

# プッシュ通知の統合

> この参考記事では、React Native のプッシュ通知を設定する方法について説明します。プッシュ通知を統合するには、各ネイティブプラットフォームを個別に設定する必要があります。リストされているそれぞれのガイドに従って、インストールを完了します。

## ステップ 1:初期設定を完了する

{% tabs %}
{% tab 万博 %}
iOS および Android のプッシュをそれぞれ有効にするには、`app.json` ファイルの `enableBrazeIosPush` および `enableFirebaseCloudMessaging` オプションを設定します。詳細については、[こちら]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup)の設定手順を参照してください。

[Expo 通知](https://docs.expo.dev/versions/latest/sdk/notifications/)などの追加のプッシュ通知ライブラリに依存している場合は、ネイティブのセットアップ手順ではなく、これらの設定を使用する必要があることに注意してください。
{% endtab %}

{% tab アンドロイド %}
### ステップ1.1：プッシュ登録

GoogleのFirebase Cloud Messaging (FCM) APIを使ってプッシュに登録する。完全なチュートリアルについては、[ネイティブAndroidプッシュ統合ガイドの]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)以下のステップを参照のこと：

1. [Firebaseをプロジェクトに追加する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project)。
2. [Cloud Messagingを依存関係に追加する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies)。
3. [サービスアカウントを作成する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account)。
4. [JSON認証情報を生成する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials)。
5. [JSON認証情報をBrazeにアップロードする]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze)。

### ステップ1.2：Googleの送信者IDを追加する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>\[**設定**] > \[**プロジェクト設定**] を選択します。

![設定」メニューを開いたFirebaseプロジェクト]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messagingを**選択し、**Firebase Cloud Messaging API (V1)の**下にある**Sender IDを**クリップボードにコピーする。

![Firebaseプロジェクトの "Cloud Messaging "ページ。"Sender ID "がハイライトされている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

次に、プロジェクトの`app.json` ファイルを開き、`firebaseCloudMessagingSenderId` プロパティをクリップボード内の送信者IDに設定する。以下に例を示します。

```
"firebaseCloudMessagingSenderId": "693679403398"
```

### ステップ1.3：Google Services JSONにパスを追加する。

プロジェクトの`app.json` ファイルに、`google-services.json` ファイルへのパスを追加する。このファイルは、お客様の構成で `enableFirebaseCloudMessaging: true` を設定する場合に必要です。

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
### ステップ1.1：APN証明書をアップロードする

Appleプッシュ通知サービス（APNs）証明書を生成し、Brazeダッシュボードにアップロードする。完全なチュートリアルについては、[APNs証明書をアップロードするを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate)参照のこと。

### ステップ1.2：統合方法を選択する

アプリの起動時にプッシュ許可をリクエストする予定がない場合は、AppDelegateの`requestAuthorizationWithOptions:completionHandler:` コールを省略し、[ステップ](#step-2-request-push-notifications-permission)2に進む。そうでない場合は、[iOSネイティブ・インテグレーション・ガイドに]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)従うこと。

終了したら、[ステップ1.](#step-13-migrate-your-push-key)3に進む。

### ステップ1.3：プッシュキーを移行する

以前にプッシュキーの管理に `expo-notifications` を使用していた場合は、アプリケーションのルートフォルダーから `expo fetch:ios:certs` を実行してください。これにより、プッシュキー (a .p8 ファイル) がダウンロードされ、その後 Braze ダッシュボードにアップロードできるようになります。
{% endtab %}
{% endtabs %}

## ステップ2: プッシュ通知の許可をリクエストする

iOS および Android 13以降のユーザーにプッシュ通知の許可を要求するには、`Braze.requestPushPermission()` メソッド (v 1.38.0以降で使用可能) を使用します。Android 12以前の場合、このメソッドは何も実行しません。

このメソッドは、SDK が iOS 上のユーザーにどの権限を要求するかを指定する必須パラメーターを受け取ります。これらのオプションは Android には影響しません。

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

### ステップ 2.1:プッシュ通知をリッスンする (オプション)

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

#### プッシュ通知イベントフィールド

{% alert note %}
iOS のプラットフォーム制限のため、Braze SDK はアプリがフォアグラウンドにあるときにのみプッシュペイロードを処理できます。リスナーは、ユーザーがプッシュを操作した後、iOSで `push_opened` イベントタイプに対してのみトリガーされます。
{% endalert %}

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

| フィールド名         | タイプ      | 説明 |
| ------------------ | --------- | ----------- |
| `payload_type`     | string    | 通知ペイロード・タイプを指定する。Braze React Native SDK から送信される2つの値は `push_opened` と `push_received` です。 iOSでは、`push_opened` イベントのみがサポートされている。 |
| `url`              | string    | 通知によって開かれたURLを指定する。 |
| `use_webview`      | ブール値   | `true` の場合、URLはアプリ内のモーダルウェブビューで開かれる。`false` の場合、URLは端末のブラウザーで開かれる。 |
| `title`            | string    | 通知のタイトルを表す。 |
| `body`             | string    | 通知の本文または内容テキストを表す。 |
| `summary_text`     | string    | 通知の要約テキストを表す。これはiOSの`subtitle` 。 |
| `badge_count`      | 数値   | 通知のバッジカウントを表す。 |
| `timestamp`        | 数値 | ペイロードがアプリケーションによって受信された時刻を表す。 |
| `is_silent`        | ブール値   | `true` の場合、ペイロードは静かに受信される。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications)を参照してください。iOSのサイレント・プッシュ通知の送信については、[iOSのサイレント・プッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)通知を参照のこと。 |
| `is_braze_internal`| ブール値   | ジオフェンス同期、Feature Flag同期、アンインストール追跡など、SDK内部機能のために通知ペイロードが送信された場合、これは`true` 。ペイロードは、ユーザーのために静かに受信される。 |
| `image_url`        | string    | 通知画像に関連するURLを指定する。 |
| `braze_properties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表す。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表す。 |
| `android`          | オブジェクト    | Android固有のフィールドを表す。 |
{: .reset-td-br-1 .reset-td-br-2}

## ステップ 3: ディープリンクを有効にする (オプション)

プッシュ通知がクリックされたときに、BrazeがReactコンポーネント内のディープリンクを処理できるようにするには、追加の手順に従う。

{% tabs %}
{% tab 万博 %}
[BrazeProject サンプル アプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)には、実装されたディープリンクの完全な例が含まれています。ディープリンクの詳細については、[FAQ の記事を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)参照してください。

{% endtab %}
{% tab アンドロイド %}
Android の場合、ディープリンクの設定は [、ネイティブ Android アプリでのディープリンクの設定]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-add-deep-links)と同じです。Braze SDK でプッシュディープリンクを自動的に処理する場合は、`app.json` で `androidHandlePushDeepLinksAutomatically: true` を設定します。

{% endtab %}
{% tab iOS %}
### ステップ 3.1:ディープリンク機能を追加する

iOS の場合は、AppDelegate の `didFinishLaunchingWithOptions` メソッドに `populateInitialUrlFromLaunchOptions` を追加します。以下に例を示します。

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

### ステップ 3.2:ディープリンクの処理を設定する

アプリを開くディープリンクには`Linking.getInitialURL()` 、アプリが起動していないときに開くプッシュ通知内のディープリンクには`Braze.getInitialURL` 。以下に例を示します。

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% alert note %}
アプリ起動時の競合状態が原因で、React Native の Linking API がこのシナリオをサポートしていないため、Braze はこの回避策を提供します。
{% endalert %}
{% endtab %}
{% endtabs %}

## ステップ4: プッシュ通知の表示をテストする

この時点で、デバイスに通知を送信できるはずです。次のステップに従って、プッシュ統合をテストします。

{% alert note %}
macOS 13以降の特定のデバイスでは、Xcode 14以降で実行されている iOS 16以降のシミュレーターで iOS プッシュ通知をテストできます。詳細については、[Xcode 14 リリース ノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. \[**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、\[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。まもなくデバイスに通知が届くはずです。

![Brazeのプッシュキャンペーンでは、自分のユーザーIDをテスト受信者として追加し、プッシュ通知をテストすることができる。][1]

## Androidプッシュを追加FMSに転送する

追加のFirebase Messaging Service (FMS)を使用したい場合は、アプリケーションがBrazeからのものではないプッシュを受信した場合に呼び出すフォールバックFMSを指定できる。以下に例を示します。

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

## Expoでアプリの拡張機能を設定する

### iOSでリッチなプッシュ通知を可能にする

{% alert tip %}
Android では、デフォルトでリッチプッシュ通知を利用できます。
{% endalert %}

Expo を使用して iOS でリッチプッシュ通知を有効にするには、`app.json` の `expo.plugins` オブジェクトで `enableBrazeIosRichPush` プロパティを `true` に構成します。

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

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトのクレデンシャル設定に追加する：`<your-app-bundle-id>.BrazeExpoRichPush`.このプロセスの詳細については、[Expo Application Servicesでアプリ拡張を使用するを](#app-extensions)参照のこと。

### iOSでプッシュストーリーズを有効にする

{% alert tip %}
プッシュ ストーリーは Android でデフォルトで利用可能です。
{% endalert %}

Expoを使ってiOSでプッシュストーリーズを有効にするには、アプリケーションにアプリグループが定義されていることを確認する。詳細については、\[アプリグループの追加][4] を参照のこと。

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

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトのクレデンシャル設定に追加する：`<your-app-bundle-id>.BrazeExpoPushStories`.このプロセスの詳細については、[Expo Application Servicesでアプリ拡張を使用するを](#app-extensions)参照のこと。

{% alert warning %}
Expo Application ServicesでPush Storiesを使用する場合は、`eas build` を実行する際に、必ず`EXPO_NO_CAPABILITY_SYNC=1` フラグを使用すること。コマンドラインに既知の問題があり、拡張機能のプロビジョニングプロファイルからApp Groups機能が削除される。
{% endalert %}

### Expo Application Servicesでアプリ拡張機能を使用する {#app-extensions}

Expo Application Services（EAS）を使用していて、`enableBrazeIosRichPush` または`enableBrazeIosPushStories` を有効にしている場合は、プロジェクト内の各アプリ拡張機能に対応するバンドル識別子を宣言する必要がある。EASでコード署名を管理するためにプロジェクトがどのように構成されているかによって、このステップにアプローチする方法は複数ある。

一つの方法は、Expoの[アプリ拡張ドキュメントに従って](https://docs.expo.dev/build-reference/app-extensions/)、`app.json` ファイルで`appExtensions` 設定を使用することである。あるいは、Expoの[ローカル認証ドキュメンテーションに従って](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)、`credentials.json` ファイルで`multitarget` 設定を行うこともできる。

[1]: {% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test"
[2]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications/
[3]: https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group
