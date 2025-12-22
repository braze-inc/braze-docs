---
nav_title: "プッシュプライマー"
article_title: iOS 用プッシュプライマー
page_order: 6
page_type: reference
description: "この参考記事では、iOS のプッシュプライマーの統合方法について説明します。"
platform: iOS
channel:
  - push
noindex: true
alias: /push_primer/
---

{% multi_lang_include deprecations/objective-c.md %}

# プッシュプライマーの統合

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュを有効にするようにユーザーに促します。ユーザーのデバイスに直接メッセージを送信する許可をユーザーから取得するのは難しい場合がありますが、当社のガイドが役立ちます。このガイドでは、開発者がプッシュプライミングを統合するために行う必要のある手順を示します。

## ステップ1:AppDelegate.m ファイルにスニペットを追加する

標準統合の代わりに、次のコード行を `AppDelegate.m` ファイルに追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
...
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus != UNAuthorizationStatusNotDetermined) {
        // authorization has already been requested, need to follow usual steps
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
        }];
        center.delegate = self;
        [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
      }
    }];
  } else {
    UIApplication *sharedApplication = [UIApplication sharedApplication];
    UIUserNotificationSettings *notificationSettings = [sharedApplication currentUserNotificationSettings];
    if (notificationSettings.types) {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
    }
  }
```
{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus != .notDetermined {
      // authorization has already been requested, need to follow usual steps
      center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
      }
      center.delegate = self as? UNUserNotificationCenterDelegate
      center.setNotificationCategories(ABKPushUtils.getAppboyUNNotificationCategorySet())
      UIApplication.shared.registerForRemoteNotifications()
    }
  })
} else {
  let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
}
```
{% endtab %}
{% endtabs %}

## ステップ2:カスタム・イベント・チェッカーをAppDelegate.m ファイルに追加する。

次のコードスニペットは、カスタムイベントを起動する必要があるかどうかをチェックします。`AppDelegate.m` に次のコード行を追加します。

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus == UNAuthorizationStatusNotDetermined) {
        // ...
        // fire custom event
        // ...
      }
    }];
  } else {
    UIUserNotificationSettings *notificationSettings = [[UIApplication sharedApplication] currentUserNotificationSettings];
    if (!notificationSettings.types) {
        // …
        // fire custom event
        // ...
    }
  }
```
{% endtab %}
{% tab swift %}
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
      // ...
      // fire custom event
      // ...
    }
  })
} else {
let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    // ...
    // fire custom event
    // ...
  }
}
```
{% endtab %}
{% endtabs %}

## ステップ3: ディープリンクハンドラーの設定

以下のコードスニペットをディープリンク処理コードの中に入れてください。このディープリンクコードは、プッシュプライマーアプリ内メッセージに対してのみ実行してください。

ディープリンクについて詳しくは、[リンク処理のカスタマイズ]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-handling-customization)を参照してください。

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
      [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
    }];
    center.delegate = self;
    [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
    [[UIApplication sharedApplication] registerForRemoteNotifications];
  } else {
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      UIApplication *sharedApplication = [UIApplication sharedApplication];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
  }
```
{% endtab %}
{% tab swift %}

```swift
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if #available(iOS 10, *) {
    let center = UNUserNotificationCenter.current()
    center.delegate = self as? UNUserNotificationCenterDelegate
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
  } else {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
```
{% endtab %}
{% endtabs %}
