---
nav_title: "푸시 프라이머"
article_title: iOS용 푸시 프라이머
page_order: 6
page_type: reference
description: "이 참조 문서에서는 iOS 푸시 프라이머를 통합하는 방법에 대해 설명합니다."
platform: iOS
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 푸시 프라이머 통합

푸시 프라이머 캠페인은 사용자가 기기에서 앱에 대한 푸시를 활성화할 것을 권장합니다. 사용자로부터 사용자의 기기로 직접 메시지를 보낼 수 있는 권한을 부여받는 작업은 복잡할 수 있지만, 본 가이드가 도움이 될 수 있습니다! 이 가이드에서는 개발자가 푸시 프라이밍을 통합하기 위해 수행해야 하는 단계를 보여줍니다.

## 1단계: AppDelegate.m 파일에 스니펫 추가

표준 통합 대신 `AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

{% tabs %}
{% tab 목표-C %}

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

## 2단계: AppDelegate.m 파일에 사용자 지정 이벤트 검사기 추가

다음 코드 스니펫은 사용자 지정 이벤트가 실행되어야 하는지 여부를 확인합니다. `AppDelegate.m` 에 다음 코드 줄을 추가합니다.

{% tabs %}
{% tab 목표-C %}
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

## 3단계: 딥링크 핸들러 설정

딥링크 처리 코드 안에 다음 코드 스니펫을 배치하세요. 푸시 프라이머 인앱 메시지에 대해서만 이 딥링킹 코드를 실행해야 합니다.

딥링크에 대한 자세한 내용은 [링크 처리 사용자 지정을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-handling-customization) 참조하세요.

{% tabs %}
{% tab 목표-C %}
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
