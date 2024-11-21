---
nav_title: 배지
article_title: iOS용 푸시 알림 배지 수
platform: Swift
page_order: 2
description: "이 문서에서는 Swift SDK에 대해 iOS 배지 수를 구현하는 방법을 다룹니다."
channel:
  - push

---

# 배지

> 배지는 사용자의 관심을 끌기에 적합한 작은 아이콘입니다. [**설정**]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/) 탭에서 Braze 대시보드를 사용하여 푸시 알림을 작성할 때 배지 개수를 지정할 수 있습니다. 애플리케이션의 [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) 속성정보 또는 [원격 알림 페이로드](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1)를 통해 배지 수를 수동으로 업데이트할 수도 있습니다. 

Braze는 앱이 포그라운드에 있는 상태에서 Braze 알림을 받으면 배지 수를 자동으로 지웁니다. 배지 수를 0으로 설정하면 알림 센터의 알림도 지워집니다. 

정상적인 앱 작동의 일부로 배지를 지우거나 배지를 지우는 푸시를 전송하여 배지를 지우려는 계획이 없는 경우 앱의 `applicationDidBecomeActive:` 위임 메서드에 다음 코드를 추가하여 앱이 활성화되면 배지를 지워야 합니다.

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab 목표-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

