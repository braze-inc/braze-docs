---
nav_title: 統合
article_title: iOS 向けのプッシュ統合
platform: iOS
page_order: 0
description: "この参照記事では、iOS アプリケーションにプッシュ通知を統合する方法を説明します。"
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# プッシュ統合

## ステップ1:APN トークンをアップロードする

{% multi_lang_include developer_guide/swift/apns_token.md %}

## ステップ2:プッシュ機能を有効にする

プロジェクト設定で、［**機能**］ タブの ［**プッシュ通知**］ 機能がオンになっていることを確認します。

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

開発用と実稼働用のプッシュ証明書が別々にある場合は、[**全般**] タブの [**署名を自動的に管理する**] チェックボックスをオフにしてください。これにより、Xcode の自動コード署名機能は開発署名のみを行うため、ビルド構成ごとに異なるプロビジョニングプロファイルを選択できるようになります。

![[一般] タブが表示されているXcode プロジェクトの設定。このタブでは、[署名を自動的に管理する] オプションはオフになっています。]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## ステップ3:プッシュ通知に登録する

ユーザーのデバイスを APNs に登録するには、アプリの `application:didFinishLaunchingWithOptions:` デリゲートメソッド内に適切なコードサンプルが含まれている必要があります。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

Braze には、プッシュアクションボタンをサポートするデフォルトのプッシュカテゴリーも用意されており、プッシュ登録コードに手動で追加する必要があります。その他の統合ステップについては、[プッシュアクションボタンを]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons/)参照のこと。

{% alert warning %}
当社の[プッシュ通知のベストプラクティス]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting/)の説明に従ってカスタムプッシュプロンプトを実装している場合は、アプリにプッシュ許可を付与した後、アプリが**実行される**たびに次のコードを呼び出すようにしてください。**[デバイストークンは任意に変更される可能性がある](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html)ため、アプリは APNs に再登録する必要があります。**
{% endalert %}

### UserNotification フレームワークの使用（iOS 10以降）

iOS 10で導入された `UserNotifications` フレームワーク (推奨) を使用している場合は、アプリデリゲートの `application:didFinishLaunchingWithOptions:` メソッドに以下のコードを追加します。

{% alert important %}
次のコードサンプルには、仮のプッシュ許可の統合が含まれています。(5行目と6行目)。アプリで仮許可を使用する予定がない場合は、`requestAuthorization` オプションに `UNAuthorizationOptionProvisional` を追加するコード行を削除できます。<br>プッシュ仮許可の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)をご覧ください。
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
アプリの起動が完了する前に、`center.delegate = self` を使用してデリゲートオブジェクトを同期的に割り当てる必要があります (可能であれば `application:didFinishLaunchingWithOptions:` で) 。そうしないと、アプリがプッシュ通知を受信できなくなる可能性があります。詳細については、Apple の [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) ドキュメントを参照してください。
{% endalert %}

### UserNotifications フレームワークを使用しない場合

`UserNotifications` フレームワークを使用していない場合は、アプリデリゲートの`application:didFinishLaunchingWithOptions:` メソッドに次のコードを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## ステップ 4:Braze にプッシュトークンを登録する

APNs の登録が完了したら、次のメソッドを変更し結果として得られる `deviceToken` を Braze に渡し、ユーザーがプッシュ通知を使用できるようにする必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

`application:didRegisterForRemoteNotificationsWithDeviceToken:` メソッドに次のコードを追加します。

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

アプリの `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` メソッドに次のコードを追加します。

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` デリゲートメソッドは、`[[UIApplication sharedApplication] registerForRemoteNotifications]` の呼び出し後に毎回呼び出されます。他のプッシュサービスから Braze に移行する場合、ユーザーのデバイスがすでに APNs に登録されていれば、このメソッドは次にこのメソッドが呼び出されたときに既存の登録からトークンを収集し、ユーザーはプッシュするために再オプトインする必要はありません。
{% endalert %}

## ステップ5: プッシュ処理を有効にする

以下のコードは受信したプッシュ通知を Braze に渡すコードで、プッシュ分析とリンク処理のログを取るために必要です。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

### iOS 10以降

iOS 10以降に対してビルドする場合は、`UserNotifications` フレームワークを統合し、以下の手順を実行することをお勧めします。

{% tabs %}
{% tab OBJECTIVE-C %}

アプリケーションの `application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに次のコードを追加します。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

次に、アプリの `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドに次のコードを追加します。

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**フォアグラウンドでのプッシュ通知処理**

アプリがフォアグラウンドにある間にプッシュ通知を表示するには、`userNotificationCenter:willPresentNotification:withCompletionHandler:` を実装します。

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` が呼び出され、Braze はプッシュクリックイベントをログに記録します。

{% endtab %}
{% tab swift %}

アプリの `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに次のコードを追加します。

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

次に、アプリの `userNotificationCenter(_:didReceive:withCompletionHandler:)` メソッドに次のコードを追加します。

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**フォアグラウンドでのプッシュ通知処理**

アプリがフォアグラウンドにある間にプッシュ通知を表示するには、`userNotificationCenter(_:willPresent:withCompletionHandler:)` を実装します。

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート `userNotificationCenter(_:didReceive:withCompletionHandler:)` が呼び出され、Braze はプッシュクリックイベントをログに記録します。

{% endtab %}
{% endtabs %}

### iOS 10より前のバージョン

iOS 10では、プッシュがクリックされたときに `application:didReceiveRemoteNotification:fetchCompletionHandler:` を呼び出さないように動作が更新されました。そのため、iOS 10以降に対応するビルドに更新せず、`UserNotifications` フレームワークを使用する場合、古いスタイルのデリゲートの両方から Braze を呼び出す必要があり、以前の統合とは一線を画しています。

iOS 10のSDK（< ）に対してビルドするアプリについては、以下の手順を使用する：

{% tabs %}
{% tab OBJECTIVE-C %}

プッシュ通知でオープントラッキングを有効にするには、アプリの `application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに次のコードを追加します。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

iOS 10でプッシュ分析をサポートするには、アプリの `application:didReceiveRemoteNotification:` デリゲートメソッドに次のコードも追加する必要があります。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

プッシュ通知でオープントラッキングを有効にするには、アプリの `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに次のコードを追加します。

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

iOS 10でプッシュ分析をサポートするには、アプリの `application(_:didReceiveRemoteNotification:)` デリゲートメソッドに次のコードも追加する必要があります。

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## ステップ 6: ディープリンク

プッシュからアプリへのディープリンクは、標準のプッシュ統合ドキュメントを介して自動的に処理されます。アプリ内の特定の場所にディープリンクを追加する方法について詳しくは、[高度なユースケース]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation)を参照してください。

## ステップ 7:単体テスト (オプション)

今行った統合手順のテストカバレッジを追加するには、[[プッシュ単体テスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests/)] を実装します。

