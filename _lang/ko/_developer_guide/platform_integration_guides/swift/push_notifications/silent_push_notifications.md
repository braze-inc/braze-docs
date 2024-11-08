---
nav_title: 무음 푸시 알림
article_title: iOS용 무음 푸시 알림
platform: Swift
page_order: 4
description: "이 문서에서는 Swift SDK용 무음 iOS 푸시 알림을 구현하는 방법을 다룹니다."
channel:
  - push

---

# iOS용 무음 푸시 알림

> 푸시 알림을 사용하면 중요한 이벤트가 발생할 때 앱에서 알림을 보낼 수 있습니다. 

사용자에게 중요한 알림이 있을 때 푸시 알림을 보낼 수 있습니다. 푸시 알림은 경고 메시지나 소리 없는 알림을 포함하여 무음 알림일 수 있으며, 앱의 인터페이스를 업데이트하거나 백그라운드 작업을 트리거하는 데만 사용할 수 있습니다. 무음 푸시 알림은 사용자에게 알리지 않고 콘텐츠를 업데이트하거나 특정 작업을 실행하기 위해 앱을 '일시 중단' 또는 '실행 중이 아님' 상태에서 해제할 수 있습니다.

Braze에는 무음 푸시 알림을 사용하는 여러 기능이 있습니다:

|기능|사용자 경험|
|---|---|
|[설치 제거 추적]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | 사용자는 매일 밤 무음 제거 추적 푸시를 수신합니다.|
|[지오펜스]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | 서버에서 기기로 지오펜스를 자동 동기화합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 무음 푸시 알림 설정하기

백그라운드 작업을 트리거하기 위해 무음 푸시 알림을 사용하려면 앱이 백그라운드에 있을 때에도 알림을 받도록 앱을 구성해야 합니다. Xcode에서 **서명 및 기능** 창을 사용하여 백그라운드 모드 기능을 기본 앱 대상에 추가합니다. **원격 알림** 확인란을 선택합니다.

!['기능' 아래에 '원격 알림' 모드 확인란이 표시된 Xcode.]({% image_buster /assets/img_archive/background_mode.png %} "백그라운드 모드 사용")

원격 알림 백그라운드 모드가 활성화되어 있어도 사용자가 애플리케이션을 강제 종료한 경우 시스템은 백그라운드로 앱을 실행하지 않습니다. 사용자가 애플리케이션을 명시적으로 실행하거나 기기를 재부팅해야 시스템에서 백그라운드로 앱을 자동으로 실행할 수 있습니다.

자세한 내용은 [백그라운드 업데이트 푸시하기](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) 및 `application:didReceiveRemoteNotification:fetchCompletionHandler:` [문서를](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) 참조하세요.

## 무음 푸시 알림 보내기

무음 푸시 알림을 보내려면 푸시 알림 페이로드에서 `content-available` 플래그를 `1`로 설정합니다. 

{% alert note %}
Apple에서 원격 알림이라고 부르는 것은 `content-available` 플래그가 설정된 일반 푸시 알림일 뿐입니다.
{% endalert %}

`content-available` 플래그는 Braze 대시보드와 [메시징 API의]({{site.baseurl}}/api/endpoints/messaging/) [Apple 푸시 개체]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) 내에서 설정할 수 있습니다.

{% alert warning %}
제목과 본문에 모두 `content-available=1`을 첨부하는 작업은 정의되지 않은 동작을 유발할 수 있으므로 권장되지 않습니다. 실제로 무음 알림인지 확인하려면 `content-available` 플래그를 `1.`로 설정할 때 제목과 본문을 모두 제외합니다. 자세한 내용은 공식 [백그라운드 업데이트에 대한 Apple 설명서](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)를 참조하세요.
{% endalert %}

![푸시 작성기의 '설정' 탭에 있는 '콘텐츠 사용 가능' 확인란이 표시된 Braze 대시보드.]({% image_buster /assets/img_archive/remote_notification.png %} "콘텐츠 사용 가능")

무음 푸시 알림을 보낼 때 애플리케이션에서 이벤트를 참조할 수 있도록 알림 페이로드에 일부 데이터를 포함할 수도 있습니다. 그러면 몇 개의 네트워킹 요청을 절약하고 앱의 응답성을 높일 수 있습니다.

## iOS 무음 알림 제한 사항

iOS 운영 체제에서는 일부 기능에 대한 알림을 차단할 수 있습니다. 이러한 기능에 문제가 있는 경우 iOS의 무음 알림 게이트가 원인일 수 있습니다.

자세한 내용은 Apple의 [인스턴스 메서드](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) 및 [미수신 알림](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) 문서를 참조하세요.

