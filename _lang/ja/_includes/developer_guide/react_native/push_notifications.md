{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## プッシュ通知の設定 {#setting-up-push-notifications}

### ステップ 1: 初期設定を完了する

{% tabs local %}
{% tab Expo %}
#### 前提条件

Expoをプッシュ通知に使用する前に、[Braze Expoプラグインを設定する]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo)必要がある。

#### ステップ1.1：`app.json` ファイルを更新する。

次にAndroidとiOS用の`app.json` ファイルを更新する：

- **Android :**`enableFirebaseCloudMessaging` オプションを追加する。
- **iOS:**`enableBrazeIosPush` オプションを追加する。

#### ステップ1.2：Google の送信者 ID を追加する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![設定」メニューが開封されたFirebaseプロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] 選択し、[**Firebase Cloud Messaging API (V1)**] の下にある [**送信者 ID**] をクリップボードにコピーします。

![Firebaseプロジェクトの "Cloud Messaging "ページで、"Sender ID "がハイライトされている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

次に、プロジェクトの`app.json` ファイルを開き、`firebaseCloudMessagingSenderId` プロパティをクリップボード内の送信者IDに設定する。以下に例を示します。

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### ステップ1.3：Google Services JSONにパスを追加する。

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

[Expo 通知](https://docs.expo.dev/versions/latest/sdk/notifications/)などの追加のプッシュ通知ライブラリに依存している場合は、ネイティブのセットアップ手順ではなく、これらの設定を使用する必要があることに注意してください。
{% endtab %}

{% tab Android Native %}
Braze Expoプラグインを使用していない場合、またはこれらの設定をネイティブで行いたい場合は、[Androidネイティブプッシュ統合ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)参照してプッシュ登録を行う。
{% endtab %}

{% tab iOS Native %}
Braze Expoプラグインを使用していない場合、またはこれらの設定をネイティブで行いたい場合は、[ネイティブiOSプッシュ統合ガイドの]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)以下のステップを参照してプッシュ登録を行う：

#### ステップ1.1：プッシュ権限のリクエスト

アプリの起動時にプッシュ権限を要求する予定がない場合は、AppDelegateの`requestAuthorizationWithOptions:completionHandler:` コールを省略する。そして[ステップ](#reactnative_step-2-request-push-notifications-permission)2に進む。そうでない場合は、[iOSネイティブ・インテグレーション・ガイドに]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)従うこと。

#### ステップ1.2（オプション）：プッシュキーを移行する

以前にプッシュキーの管理に `expo-notifications` を使用していた場合は、アプリケーションのルートフォルダーから `expo fetch:ios:certs` を実行してください。これにより、プッシュキー (a .p8 ファイル) がダウンロードされ、その後 Braze ダッシュボードにアップロードできるようになります。
{% endtab %}
{% endtabs %}

### ステップ 2:プッシュ通知の許可をリクエストする

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

#### ステップ 2.1:プッシュ通知をリッスンする (オプション)

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

##### プッシュ通知イベントフィールド

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
| `is_silent`        | ブール値   | `true` の場合、ペイロードはサイレントに受信されます。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。iOS のサイレントプッシュ通知の送信の詳細については、[iOS のサイレントプッシュ通知を参照してください]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)。 |
| `is_braze_internal`| ブール値   | ジオフェンス同期、機能フラグ同期、またはアンインストールトラッキングなどの内部 SDK 機能に対して通知ペイロードが送信された場合、これは `true` になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `image_url`        | 文字列    | 通知画像に関連するURLを指定する。 |
| `braze_properties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表す。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表す。 |
| `android`          | オブジェクト    | Android固有のフィールドを表す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ3: ディープリンクを有効にする (オプション)

プッシュ通知がクリックされたときに、BrazeがReactコンポーネント内のディープリンクを処理できるようにするには、まず、[React Native Linking](https://reactnative.dev/docs/linking)libraryで説明されているステップを実装するか、選択したソリューションで実装する。その後、以下の追加ステップに従う。

ディープリンクの詳細については、[FAQ の記事を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)参照してください。

{% tabs local %}
{% tab Android Native %}
[Braze Expoプラグインを]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option)使用している場合、`app.json` で`androidHandlePushDeepLinksAutomatically` を`true` に設定することで、プッシュ通知のディープリンクを自動的に処理することができる。

ディープリンクを手動で処理するには、Androidネイティブのドキュメントを参照すること：[ディープリンクを追加する]({{site.baseurl}}/developer_guide/push_notifications/deep_linking)。

{% endtab %}
{% tab iOS Native %}
#### ステップ 3.1:アプリ起動時にプッシュ通知のペイロードを保存する
{% alert note %}
Braze Expoプラグインを使用している場合は、この機能は自動的に処理されるので、ステップ3.1をスキップする。
{% endalert %}

iOS の場合は、AppDelegate の `didFinishLaunchingWithOptions` メソッドに `populateInitialPayloadFromLaunchOptions` を追加します。以下に例を示します。

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
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

#### ステップ 3.2:閉じた状態からのディープリンクを扱う

[React Native Linkingが](https://reactnative.dev/docs/linking)扱う基本シナリオに加えて、`Braze.getInitialPushPayload` メソッドを実装し、`url` 値を取得することで、アプリが実行されていないときに開封されるプッシュ通知からのディープリンクを考慮する。以下に例を示します。

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
アプリ起動時の競合状態が原因で、React Native の Linking API がこのシナリオをサポートしていないため、Braze はこの回避策を提供します。
{% endalert %}

#### ステップ3.3 ユニバーサルリンクを有効にする（オプション）

[ユニバーサル・リンク・]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links)サポートを有効にするには、`iOS` ディレクトリに`BrazeReactDelegate.h` ファイルを作成し、以下のコード・スニペットを追加する。

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

次に、`BrazeReactDelegate.m` ファイルを作成し、以下のコード・スニペットを追加する。`YOUR_DOMAIN_HOST` を実際のドメインに置き換える。

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

次に、プロジェクトの`AppDelegate.m` ファイルの`didFinishLaunchingWithOptions` に、`BrazeReactDelegate` を作成し登録する。

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```

統合の例については、[こちらの](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm)サンプルアプリを参照されたい。
{% endtab %}
{% endtabs %}

### ステップ 4: テストプッシュ通知を送信する

この時点で、デバイスに通知を送信できるはずです。次のステップに従って、プッシュ統合をテストします。

{% alert note %}
macOS 13以降の特定のデバイスでは、Xcode 14以降で実行されている iOS 16以降のシミュレーターで iOS プッシュ通知をテストできます。詳細については、[Xcode 14 リリース ノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

1. `Braze.changeUserId('your-user-id')` メソッドを呼び出して、React Native アプリケーションにアクティブユーザーを設定する。
2. [**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。まもなくデバイスに通知が届くはずです。

![Brazeのプッシュキャンペーンでは、自分のユーザーIDをテスト受信者として追加し、プッシュ通知をテストすることができる。]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Expoプラグインを使う

[Expoのプッシュ通知を設定](#reactnative_setting-up-push-notifications)すると、AndroidやiOSのネイティブレイヤーにコードを記述することなく、[Expoを使って](#reactnative_setting-up-push-notifications)以下のプッシュ通知の動作を処理することができる。

### Androidプッシュを追加FMSに転送する

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

### Expo Application Services でアプリ拡張機能を使用する {#app-extensions}

Expo Application Services（EAS）を使用していて、`enableBrazeIosRichPush` または`enableBrazeIosPushStories` を有効にしている場合は、プロジェクト内の各アプリ拡張機能に対応するバンドル識別子を宣言する必要がある。EAS でコード署名を管理するためにプロジェクトがどのように構成されているかによって、このステップにアプローチする方法は複数あります。

一つの方法は、Expo の[アプリ拡張ドキュメント](https://docs.expo.dev/build-reference/app-extensions/)に従って、`app.json` ファイルで `appExtensions` 設定を使用することです。あるいは、Expo の[ローカル認証情報ドキュメント](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)に従って、`credentials.json` ファイルで `multitarget` 設定を行うこともできます。

### トラブルシューティング

これらは、Braze React Native SDKとExpoプラグインを使用したプッシュ通知の統合に関する一般的なトラブルシューティングのステップである。

#### プッシュ通知が機能しなくなった {#troubleshooting-stopped-working}

Expoプラグインによるプッシュ通知が機能しなくなった場合：

1. Braze SDKがまだセッションをトラッキング, 追跡していることを確認する。
2. SDK が`wipeData` への明示的または暗黙的なコールによって無効化されていないことを確認する。
3. お使いのBrazeの設定と競合する可能性があるため、Expoまたはその関連ライブラリーの最近のアップグレードを確認する。
4. 最近追加されたプロジェクトの依存関係を確認し、既存のプッシュ通知デリゲートメソッドを手動でオーバーライドしていないかチェックする。

{% alert tip %}
iOSとの統合については、[プッシュ通知のセットアップチュートリアルを](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications)参照し、プロジェクトの依存関係との潜在的な競合を特定するのに役立てることができる。
{% endalert %}

#### トークンがBrazeに登録されない。 {#troubleshooting-token-registration}

デバイストークンがBrazeに登録されない場合は、まず[プッシュ通知が機能しなくなった](#troubleshooting-stopped-working)ことを確認する。

問題が解決しない場合は、別の依存関係がBrazeのプッシュ通知設定に干渉している可能性がある。削除してみるか、代わりに手動で`Braze.registerPushToken` 。
