{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## プッシュ通知の設定 {#setting-up-push-notifications}

### ステップ 1: 初期設定を完了する

{% tabs local %}
{% tab Expo %}
#### 前提条件

Expoでプッシュ通知を使う前に、[Braze Expoプラグインを設定]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo)する必要があります。

#### ステップ1.1：`app.json` ファイルを更新する

次に、AndroidとiOS用の `app.json` ファイルを更新します：

- **Android：**`enableFirebaseCloudMessaging` オプションを追加します。
- **iOS：**`enableBrazeIosPush` オプションを追加します。

#### ステップ1.2：Google の送信者 ID を追加する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>&nbsp;**設定** > **プロジェクト設定** を選択します。

![「設定」メニューが開いているFirebaseプロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messaging** を選択し、**Firebase Cloud Messaging API (V1)** の下にある **送信者 ID** をクリップボードにコピーします。

![Firebaseプロジェクトの「Cloud Messaging」ページで「送信者ID」が強調表示されている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

次に、プロジェクトの `app.json` ファイルを開き、`firebaseCloudMessagingSenderId` プロパティをクリップボード内の送信者IDに設定します。以下に例を示します。

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### ステップ1.3：Google Services JSONへのパスを追加する

プロジェクトの `app.json` ファイルに、`google-services.json` ファイルへのパスを追加します。このファイルは、設定で `enableFirebaseCloudMessaging: true` を指定する場合に必要です。

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

[Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) などの追加のプッシュ通知ライブラリーに依存している場合は、ネイティブのセットアップ手順ではなく、これらの設定を使用する必要があることに注意してください。
{% endtab %}

{% tab Android Native %}
Braze Expoプラグインを使用していない場合、またはこれらの設定をネイティブで構成したい場合は、[ネイティブAndroidプッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)を参照してプッシュ通知を登録してください。
{% endtab %}

{% tab iOS Native %}
Braze Expoプラグインを使用していない場合、またはこれらの設定をネイティブで構成したい場合は、[ネイティブiOSプッシュ統合ガイド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)の以下のステップを参照してプッシュ登録を行ってください：

#### ステップ1.1：プッシュ通知の権限をリクエストする

アプリ起動時にプッシュ通知の権限をリクエストする予定がない場合は、AppDelegate内の `requestAuthorizationWithOptions:completionHandler:` 呼び出しを省略してください。その後、[ステップ2](#reactnative_step-2-request-push-notifications-permission)に進んでください。それ以外の場合は、[iOSネイティブ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)に従ってください。

#### ステップ1.2（オプション）：プッシュキーを移行する

以前にプッシュキーの管理に `expo-notifications` を使用していた場合は、アプリケーションのルートフォルダーから `expo fetch:ios:certs` を実行してください。これにより、プッシュキー（.p8 ファイル）がダウンロードされ、その後 Braze ダッシュボードにアップロードできるようになります。
{% endtab %}
{% endtabs %}

### ステップ 2：プッシュ通知の許可をリクエストする

iOS および Android 13以降のユーザーにプッシュ通知の許可をリクエストするには、`Braze.requestPushPermission()` メソッド（v1.38.0以降で使用可能）を使用します。Android 12以前の場合、このメソッドは何も実行しません。

このメソッドは、SDK が iOS 上のユーザーにどの権限をリクエストするかを指定する必須パラメーターを受け取ります。これらのオプションは Android には影響しません。

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### ステップ 2.1：プッシュ通知をリッスンする（オプション）

さらに、Braze が受信プッシュ通知を検出して処理したイベントをサブスクライブすることもできます。リスナーキー `Braze.Events.PUSH_NOTIFICATION_EVENT` を使用します。

{% alert important %}
iOS プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされます。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされません。
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
| `url`              | 文字列    | 通知によって開かれたURLを指定します。 |
| `use_webview`      | ブール値   | `true` の場合、URLはアプリ内のモーダルウェブビューで開かれます。`false` の場合、URLはデバイスのブラウザーで開かれます。 |
| `title`            | 文字列    | 通知のタイトルを表します。 |
| `body`             | 文字列    | 通知の本文またはコンテンツテキストを表します。 |
| `summary_text`     | 文字列    | 通知の要約テキストを表します。これは iOS では `subtitle` からマッピングされます。 |
| `badge_count`      | 数値   | 通知のバッジカウントを表します。 |
| `timestamp`        | 数値 | ペイロードがアプリケーションによって受信された時刻を表します。 |
| `is_silent`        | ブール値   | `true` の場合、ペイロードはサイレントに受信されます。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。iOS のサイレントプッシュ通知の送信の詳細については、[iOS でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を参照してください。 |
| `is_braze_internal`| ブール値   | ジオフェンス同期、フィーチャーフラグ同期、またはアンインストール追跡などの内部 SDK 機能に対して通知ペイロードが送信された場合、これは `true` になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `image_url`        | 文字列    | 通知画像に関連するURLを指定します。 |
| `braze_properties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表します。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表します。 |
| `android`          | オブジェクト    | Android固有のフィールドを表します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ3：ディープリンクを有効にする（オプション）

Reactコンポーネント内でプッシュ通知がクリックされた際にBrazeがディープリンクを処理できるようにするには、まず[React Native Linking](https://reactnative.dev/docs/linking)ライブラリーで説明されているステップを実装するか、任意のソリューションで実装してください。次に、以下の追加ステップに従ってください。

ディープリンクの詳細については、[FAQの記事]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)を参照してください。

{% tabs local %}
{% tab Android Native %}
[Braze Expoプラグイン]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option)を使用している場合、`app.json` で `androidHandlePushDeepLinksAutomatically` を `true` に設定することで、プッシュ通知のディープリンクを自動的に処理できます。

代わりにディープリンクを手動で処理するには、ネイティブAndroidのドキュメントを参照してください：[ディープリンクを追加する]({{site.baseurl}}/developer_guide/push_notifications/deep_linking)。

#### ステップ 3.1：アプリ起動時にプッシュ通知のペイロードを保存する

{% alert note %}
これはReact Native SDK 19.1.0以降でサポートされています。
{% endalert %}

メインアクティビティの `onCreate()` メソッドに `populateInitialPushPayloadFromIntent` を追加します。React Nativeが初期化される前にこれを呼び出して、初期のIntentデータをキャプチャする必要があります。以下に例を示します。

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
  super.onCreate(savedInstanceState)
}
```

#### ステップ 3.2：閉じている状態からのディープリンクを処理する

[React Native Linking](https://reactnative.dev/docs/linking)が扱う基本シナリオに加えて、`Braze.getInitialPushPayload` メソッドを実装し、`url` の値を取得します。これにより、アプリが起動していない状態でプッシュ通知からアプリを開くディープリンクに対応できます。以下に例を示します。

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
このメソッドでは、ステップ3.1でプラットフォーム向けのネイティブ設定が必要です。Braze Expoプラグインを使用している場合、これは自動的に処理される可能性があります。
{% endalert %}

{% endtab %}
{% tab iOS Native %}

{% alert important %}
iOSでプッシュ通知からのディープリンクを処理するには、ネイティブiOSレイヤーでリンク処理も設定する必要があります。
{% endalert %}

これには、カスタムURLスキームの登録と `AppDelegate` でのURLハンドラーの実装が含まれます。完全なセットアップ手順については、ネイティブiOSドキュメントの[ディープリンクの処理]({{site.baseurl}}/developer_guide/platforms/swift/in_app_messages/deep_linking/?tab=objective-c)を参照してください。
#### ステップ 3.1：アプリ起動時にプッシュ通知のペイロードを保存する
{% alert note %}
Braze Expoプラグインを使用している場合は、ステップ3.1をスキップしてください。この機能は自動的に処理されます。
{% endalert %}

iOS の場合は、AppDelegate の `didFinishLaunchingWithOptions` メソッドに `populateInitialPayloadFromLaunchOptions` を追加します。以下に例を示します。

{% subtabs local %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // ... Perform regular React Native setup

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
{% endsubtab %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
) -> Bool {
  // ... Perform regular React Native setup

  let configuration = Braze.Configuration(apiKey: apiKey, endpoint: endpoint)
  configuration.triggerMinimumTimeInterval = 1
  configuration.logger.level = .info
  let braze = BrazeReactBridge.initBraze(configuration)
  AppDelegate.braze = braze
  registerForPushNotifications()
  BrazeReactUtils.shared().populateInitialPayload(fromLaunchOptions: launchOptions)

  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```
{% endsubtab %}
{% endsubtabs %}

#### ステップ 3.2：閉じている状態からのディープリンクを処理する

[React Native Linking](https://reactnative.dev/docs/linking)が扱う基本シナリオに加えて、`Braze.getInitialPushPayload` メソッドを実装し、`url` の値を取得します。これにより、アプリが起動していない状態でプッシュ通知からアプリを開くディープリンクに対応できます。以下に例を示します。

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
このメソッドでは、ステップ3.1でプラットフォーム向けのネイティブ設定が必要です。Braze Expoプラグインを使用している場合、これは自動的に処理される可能性があります。
{% endalert %}

#### ステップ3.3：ユニバーサルリンクを有効にする（オプション）

[ユニバーサルリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links)のサポートを有効にするには、指定されたURLを開くかどうかを判断するBrazeデリゲートを実装し、それをBrazeインスタンスに登録します。

{% subtabs local %}
{% subtab Swift %}
`iOS` ディレクトリ内に `BrazeReactDelegate.swift` ファイルを作成し、以下を追加します。`YOUR_DOMAIN_HOST` を実際のドメインに置き換えてください。

```swift
import Foundation
import BrazeKit
import UIKit

class BrazeReactDelegate: NSObject, BrazeDelegate {

  /// This delegate method determines whether to open a given URL.
  /// Reference the context to get additional details about the URL payload.
  func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
    if let host = context.url.host,
       host.caseInsensitiveCompare("YOUR_DOMAIN_HOST") == .orderedSame {
      // Sample custom handling of universal links
      let application = UIApplication.shared
      let userActivity = NSUserActivity(activityType: NSUserActivityTypeBrowsingWeb)
      userActivity.webpageURL = context.url
      // Routes to the `continueUserActivity` method, which should be handled in your AppDelegate.
      application.delegate?.application?(
        application,
        continue: userActivity,
        restorationHandler: { _ in }
      )
      return false
    }
    // Let Braze handle links otherwise
    return true
  }
}
```

次に、プロジェクトの `AppDelegate.swift` ファイルの `didFinishLaunchingWithOptions` 内で `BrazeReactDelegate` を作成し登録します。

```swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  
  static var braze: Braze?
  
  // Keep a strong reference to the BrazeDelegate so it is not deallocated.
  private var brazeDelegate: BrazeReactDelegate?
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Other setup code (e.g., Braze initialization)
    
    brazeDelegate = BrazeReactDelegate()
    AppDelegate.braze?.delegate = brazeDelegate
    return true
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
`iOS` ディレクトリ内に `BrazeReactDelegate.h` ファイルを作成し、以下のコードスニペットを追加します。

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

次に、`BrazeReactDelegate.m` ファイルを作成し、以下のコードスニペットを追加します。`YOUR_DOMAIN_HOST` を実際のドメインに置き換えてください。

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

次に、プロジェクトの `AppDelegate.m` ファイルの `didFinishLaunchingWithOptions` 内で `BrazeReactDelegate` を作成し登録します。

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
{% endsubtab %}
{% endsubtabs %}

統合の例については、[こちら](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm)のサンプルアプリを参照してください。
{% endtab %}
{% endtabs %}

### ステップ 4：フォアグラウンド通知を処理する

フォアグラウンド通知の処理は、プラットフォームや設定によって異なります。統合方法に合わせてアプローチを選択してください。

{% tabs local %}
{% tab iOS %}
iOSでは、フォアグラウンド通知の処理はネイティブのSwift統合と同じです。`UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)` の実装内で `handleForegroundNotification(notification:)` を呼び出します。

詳細な情報とコード例については、Swiftプッシュ通知のドキュメントにある[フォアグラウンド通知の処理]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#handling-foreground-notifications)を参照してください。
{% endtab %}

{% tab Android %}
Androidの場合、フォアグラウンド通知の処理はネイティブのAndroid統合と同じです。`FirebaseMessagingService.onMessageReceived` メソッド内で `BrazeFirebaseMessagingService.handleBrazeRemoteMessage` を呼び出します。

詳細な情報とコード例については、Androidプッシュ通知のドキュメントにある[フォアグラウンド通知の処理]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications)を参照してください。
{% endtab %}

{% tab Expo %}
Expo管理ワークフローでは、ネイティブ通知ハンドラーを直接呼び出しません。代わりに、Expo Notifications API を使ってフォアグラウンド表示をコントロールし、Braze Expoプラグインがネイティブ処理を自動的に行います。

```javascript
import * as Notifications from 'expo-notifications';
import Braze from '@braze/react-native-sdk';

// Control foreground presentation in Expo
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,    // Show alert while in foreground
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// React to Braze push events
const subscription = Braze.addListener('pushNotificationEvent', (event) => {
  console.log('Braze push event', {
    type: event.payload_type,   // "push_received" | "push_opened"
    title: event.title,
    url: event.url,
    is_silent: event.is_silent,
  });
  // Handle deep links, custom behavior, etc.
});

// Handle initial payload when app launches via push
Braze.getInitialPushPayload((payload) => {
  if (payload) {
    console.log('Initial push payload', payload);
  }
});
```

{% alert note %}
Expo管理ワークフローでは、Braze Expoプラグインがネイティブプッシュ処理を自動的に行います。上記のExpo Notificationsプレゼンテーションオプションで、フォアグラウンドUIをコントロールします。
{% endalert %}

ベアワークフロー統合については、代わりにネイティブのiOSおよびAndroidのアプローチに従ってください。
{% endtab %}
{% endtabs %}

### ステップ 5：テストのプッシュ通知を送信する

この時点で、デバイスに通知を送信できるはずです。次のステップに従って、プッシュ統合をテストしてください。

{% alert note %}
macOS 13以降の特定のデバイスでは、Xcode 14以降で実行されているiOS 16以降のシミュレーターでiOSプッシュ通知をテストできます。詳細については、[Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

1. React Nativeアプリケーションで `Braze.changeUserId('your-user-id')` メソッドを呼び出して、アクティブユーザーを設定します。
2. **キャンペーン**に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、**テスト**タブに移動します。テストユーザーと同じ `user-id` を追加し、**テストを送信**をクリックします。まもなくデバイスに通知が届くはずです。

![Brazeのプッシュキャンペーンでは、自分のユーザーIDをテスト受信者として追加し、プッシュ通知をテストすることができます。]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Expoプラグインを使う

[Expoでプッシュ通知を設定](#reactnative_setting-up-push-notifications)した後、ネイティブのAndroidやiOSレイヤーでコードを書く必要なく、以下のプッシュ通知の動作を処理できます。

### Androidプッシュを追加FMSに転送する

追加の Firebase Messaging Service（FMS）を使用する場合は、アプリケーションがBraze以外からプッシュを受信した場合に呼び出すフォールバックFMSを指定できます。以下に例を示します。

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

### Expo Application Servicesでアプリ拡張機能を使用する {#app-extensions}

Expo Application Services（EAS）を使用していて、`enableBrazeIosRichPush` または `enableBrazeIosPushStories` を有効にしている場合は、プロジェクト内の各アプリ拡張機能に対応するバンドル識別子を宣言する必要があります。EASでコード署名を管理するためにプロジェクトがどのように構成されているかによって、このステップにアプローチする方法は複数あります。

一つの方法は、Expoの[アプリ拡張ドキュメント](https://docs.expo.dev/build-reference/app-extensions/)に従って、`app.json` ファイルで `appExtensions` 設定を使用することです。あるいは、Expoの[ローカル認証情報ドキュメント](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project)に従って、`credentials.json` ファイルで `multitarget` 設定を行うこともできます。

### トラブルシューティング

以下は、Braze React Native SDKおよびExpoプラグインとのプッシュ通知統合における一般的なトラブルシューティングステップです。

#### プッシュ通知が機能しなくなった {#troubleshooting-stopped-working}

Expoプラグイン経由のプッシュ通知が機能しなくなった場合：

1. Braze SDKがまだセッションの追跡を行っているか確認してください。
2. SDKが明示的または暗黙的な `wipeData` 呼び出しによって無効化されていないことを確認してください。
3. Expoや関連ライブラリーの最近のアップグレードを確認してください。Brazeの設定と競合する可能性があります。
4. 最近追加されたプロジェクトの依存関係を確認し、それらが既存のプッシュ通知デリゲートメソッドを手動で上書きしていないかチェックしてください。

{% alert tip %}
iOS統合については、プロジェクトの依存関係との潜在的な競合を識別するのに役立つ、[プッシュ通知設定チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications)も参照できます。
{% endalert %}

#### デバイストークンがBrazeに登録されない {#troubleshooting-token-registration}

デバイストークンがBrazeに登録されない場合、まず[プッシュ通知が機能しなくなった](#troubleshooting-stopped-working)を確認してください。

問題が解決しない場合、別の依存関係がBrazeのプッシュ通知設定に干渉している可能性があります。それを削除するか、代わりに手動で `Braze.registerPushToken` を呼び出すことを試してください。