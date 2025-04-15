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

## ステップ1:初期設定を完了する

{% tabs %}
{% tab Expo %}
iOS および Android のプッシュをそれぞれ有効にするには、`app.json` ファイルの `enableBrazeIosPush` および `enableFirebaseCloudMessaging` オプションを設定します。詳細については、[こちら]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/#step-2-complete-native-setup)の設定手順を参照してください。

[Expo 通知](https://docs.expo.dev/versions/latest/sdk/notifications/)などの追加のプッシュ通知ライブラリに依存している場合は、ネイティブのセットアップ手順ではなく、これらの設定を使用する必要があることに注意してください。
{% endtab %}

{% tab Android %}
### ステップ1.1：プッシュ登録

Google の Firebase Cloud Messaging (FCM) API を使用してプッシュに登録します。詳しい手順については、「[ネイティブ Android プッシュ通知統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)」で以下の手順を参照してください。

1. [Firebase をプロジェクトに追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project)。
2. [Cloud Messaging を依存関係に追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies)。
3. [サービスアカウントを作成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account)。
4. [JSON 認証情報を生成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials)。
5. [JSON認証情報をBrazeにアップロードする]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze)。

### ステップ1.2：Google の送信者 ID を追加する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![[設定] メニューが開いた状態の Firebase プロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] 選択し、[**Firebase Cloud Messaging API (V1)**] の下にある [**送信者 ID**] をクリップボードにコピーします。

![[送信者 ID] が強調表示されている Firebase プロジェクトの「Cloud Messaging」ページ。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

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

Appleプッシュ通知サービス（APNs）証明書を生成し、Brazeダッシュボードにアップロードする。詳細な手順については、[APN 証明書のアップロード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate)を参照してください。

### ステップ1.2：統合方法を選択する

アプリの起動時にプッシュ許可をリクエストする予定がない場合は、AppDelegate の `requestAuthorizationWithOptions:completionHandler:` 呼び出しを省略し、[ステップ 2](#step-2-request-push-notifications-permission) に進みます。そうでない場合は、[iOSネイティブ・インテグレーション・ガイドに]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)従うこと。

終了したら、[ステップ 1.3](#step-13-migrate-your-push-key) に進みます。

### ステップ1.3：プッシュキーを移行する

以前にプッシュキーの管理に `expo-notifications` を使用していた場合は、アプリケーションのルートフォルダーから `expo fetch:ios:certs` を実行してください。これにより、プッシュキー (a .p8 ファイル) がダウンロードされ、その後 Braze ダッシュボードにアップロードできるようになります。
{% endtab %}
{% endtabs %}

## ステップ 2:プッシュ通知の許可をリクエストする

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

{% alert important %}
iOS プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされます。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされない。
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

#### プッシュ通知イベントフィールド

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

| フィールド名         | タイプ      | 説明 |
| ------------------ | --------- | ----------- |
| `payload_type`     | 文字列    | 通知ペイロードのタイプを指定します。Braze React Native SDK から送信される2つの値は `push_opened` と `push_received` です。 |
| `url`              | 文字列    | 通知によって開かれたURLを指定する。 |
| `use_webview`      | ブール値   | `true` の場合、URLはアプリ内のモーダルウェブビューで開かれる。`false` の場合、URLは端末のブラウザーで開かれる。 |
| `title`            | 文字列    | 通知のタイトルを表す。 |
| `body`             | 文字列    | 通知の本文または内容テキストを表す。 |
| `summary_text`     | 文字列    | 通知の要約テキストを表す。これは iOS で `subtitle` からマップされます。 |
| `badge_count`      | 数値   | 通知のバッジカウントを表す。 |
| `timestamp`        | 数値 | ペイロードがアプリケーションによって受信された時刻を表す。 |
| `is_silent`        | ブール値   | `true` の場合、ペイロードはサイレントに受信されます。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications)を参照してください。iOS のサイレントプッシュ通知の送信の詳細については、[iOS のサイレントプッシュ通知を参照してください]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)。 |
| `is_braze_internal`| ブール値   | ジオフェンス同期、機能フラグ同期、またはアンインストールトラッキングなどの内部 SDK 機能に対して通知ペイロードが送信された場合、これは `true` になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `image_url`        | 文字列    | 通知画像に関連するURLを指定する。 |
| `braze_properties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表す。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表す。 |
| `android`          | オブジェクト    | Android固有のフィールドを表す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ3: ディープリンクを有効にする (オプション)

プッシュ通知がクリックされたときに Braze が React コンポーネント内のディープリンクを処理できるようにするには、追加の手順に従います。

{% tabs %}
{% tab Expo %}
[BrazeProject サンプル アプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)には、実装されたディープリンクの完全な例が含まれています。ディープリンクの詳細については、[FAQ の記事を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)参照してください。

{% endtab %}
{% tab Android %}
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

アプリを開くディープリンクには `Linking.getInitialURL()` メソッドを使用し、アプリが実行されていないときにアプリを開くプッシュ通知内のディープリンクには `Braze.getInitialURL` メソッドを使用します。以下に例を示します。

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

## ステップ 4:プッシュ通知の表示をテストする

この時点で、デバイスに通知を送信できるはずです。次のステップに従って、プッシュ統合をテストします。

{% alert note %}
macOS 13以降の特定のデバイスでは、Xcode 14以降で実行されている iOS 16以降のシミュレーターで iOS プッシュ通知をテストできます。詳細については、[Xcode 14 リリース ノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React アプリケーションにアクティブユーザーを設定します。
2. [**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。まもなくデバイスに通知が届くはずです。

![テスト受信者として独自のユーザID を追加して、プッシュ通知をテストできることを示す Braze プッシュキャンペーン。]({% image_buster /assets/img/react-native/push-notification-test.png %}"Push Campaign Test")

## Androidプッシュを追加FMSに転送する

追加の Firebase Messaging Service (FMS) を使用する場合は、アプリケーションが Braze 以外からプッシュを受信した場合に呼び出すフォールバック FMS を指定できます。以下に例を示します。

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

### iOS のリッチプッシュ通知を有効にする

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

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトの認証情報設定に追加します：`<your-app-bundle-id>.BrazeExpoRichPush`.このプロセスの詳細については、[Expo Application Services でアプリ拡張機能を使用する](#app-extensions)を参照してください。

### iOSでプッシュストーリーズを有効にする

{% alert tip %}
プッシュ ストーリーは Android でデフォルトで利用可能です。
{% endalert %}

Expoを使ってiOSでプッシュストーリーズを有効にするには、アプリケーションにアプリグループが定義されていることを確認する。詳細については、[アプリグループの追加]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group)を参照してください。

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

最後に、このアプリ拡張機能のバンドル識別子を、プロジェクトの認証情報設定に追加します：`<your-app-bundle-id>.BrazeExpoPushStories`.このプロセスの詳細については、[Expo Application Services でアプリ拡張機能を使用する](#app-extensions)を参照してください。

{% alert warning %}
Expo Application Services で Push Stories を使用する場合は、`eas build` を実行する際に、必ず `EXPO_NO_CAPABILITY_SYNC=1` フラグを使用してください。コマンドラインに既知の問題があり、拡張機能のプロビジョニングプロファイルからApp Groups機能が削除される。
{% endalert %}

### Expo Application Services でアプリ拡張機能を使用する {#app-extensions}

Expo Application Services（EAS）を使用していて、`enableBrazeIosRichPush` または`enableBrazeIosPushStories` を有効にしている場合は、プロジェクト内の各アプリ拡張機能に対応するバンドル識別子を宣言する必要がある。EAS でコード署名を管理するためにプロジェクトがどのように構成されているかによって、このステップにアプローチする方法は複数あります。

一つの方法は、Expo の[アプリ拡張ドキュメント](https://docs.expo.dev/build-reference/app-extensions/)に従って、`app.json` ファイルで `appExtensions` 設定を使用することです。あるいは、Expo の[ローカル認証情報ドキュメント](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)に従って、`credentials.json` ファイルで `multitarget` 設定を行うこともできます。

