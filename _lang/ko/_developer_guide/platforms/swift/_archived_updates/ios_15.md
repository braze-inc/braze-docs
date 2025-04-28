---
nav_title: iOS 15 업그레이드 가이드
article_title: iOS 15 SDK 업그레이드 가이드
page_order: 7
platform: iOS
description: "이 참조 문서에서는 새로운 iOS 15 OS 업데이트, 필수 SDK 업데이트 및 새로운 기능을 다룹니다."
hidden: true
noindex: true
---

# iOS 15 SDK 업그레이드 가이드

> 이 가이드에서는 iOS 15(WWDC21)에 도입된 변경 사항과 Braze iOS SDK 통합에 필요한 업그레이드 단계를 간략하게 설명합니다. 새로운 iOS 15 업데이트의 전체 목록은 Apple의 [iOS 15 릴리스 정보](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes)를 참조하세요.


## UI 탐색의 투명성 변경 사항

매년 iOS 베타를 테스트하는 과정에서 특정 UI 탐색 막대가 불투명하지 않고 투명하게 표시되는 Apple의 변경 사항을 확인했습니다. 이것은 Braze 기본 UI를 사용하여 콘텐츠 카드를 사용할 때 또는 웹 딥 링크가 별도의 브라우저 앱이 아닌 앱 내에서 열릴 때 iOS 15에서 표시됩니다.

iOS 15에서 이러한 시각적 변경 사항을 방지하려면 휴대폰을 새로운 iOS 15 운영 체제로 업그레이드하기 전에 가능한 한 빨리 [Braze iOS SDK v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2)로 업그레이드할 것을 적극 권장합니다.

## 새로운 알림 설정 {#notification-settings}

iOS 15에는 사용자가 하루 종일 집중하고 자주 방해받지 않도록 도와주는 새로운 알림 기능이 도입되었습니다. 이러한 새로운 기능에 대한 지원을 제공하게 되어 기쁩니다. 이러한 기능은 추가적인 SDK 업그레이드가 필요하지 않으며 iOS 15 기기를 사용하는 사용자에게만 적용됩니다.

### 초점 모드 {#focus-mode}

이제 iOS 15 사용자는 커스텀 프로필인 '포커스 모드'를 생성하여 어떤 알림을 집중해서 눈에 띄게 표시할지 결정할 수 있습니다.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### 방해 수준 {#interruption-levels}

iOS 15에서는 푸시 알림을 네 가지 방해 수준 중 하나로 보낼 수 있습니다.

* **수동**(신규) - 소리, 진동, 절전 화면 해제, 초점 해제 설정이 없습니다.
* **활성**(기본값) - 소리, 진동, 절전 화면 해제, 초점 해제 설정을 지원합니다.
* **시간 기반**(신규) - 소리, 진동, 절전 화면 해제를 지원하며, 허용하는 경우 시스템 제어를 통해 해제할 수 있습니다.
* **중요** \- 소리, 진동, 절전 화면 해제를 허용하며, 시스템 제어를 통해 해제할 수 있고, 벨소리 스위치를 우회할 수 있습니다.

iOS 푸시에서 이 옵션을 설정하는 방법에 대해 자세히 알아보려면 [iOS 알림 옵션]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level)을 참조하세요.

### 알림 요약 {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15에서는 사용자가 선택적으로 하루 중 특정 시간을 선택하여 알림 요약을 받을 수 있습니다. 즉각적인 주의가 필요하지 않은 알림(예: '수동'으로 전송되거나 사용자가 초점 모드에 있을 때 전송되는 알림 등)은 하루 종일 계속 방해받지 않도록 그룹화됩니다.

보내는 각 알림에 대해 곧 '관련성 점수'를 지정하여 요약 상단에 표시할 알림을 제어할 수 있습니다.

알림의 '관련성 점수'를 설정하는 방법에 대해 자세히 알아보려면 [iOS 알림 옵션]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score)을 참조하세요.

## 위치 버튼 {#location-buttons}

iOS 15에서는 사용자가 앱 내에서 일시적으로 위치 액세스 권한을 부여할 수 있는 편리한 새로운 방법이 도입되었습니다. 

새로운 위치 버튼은 동일한 세션에서 여러 번 클릭하는 사용자에게 반복적으로 메시지를 표시하지 않고 기존의 '한 번만 허용' 권한을 기반으로 합니다.

자세한 내용은 올해 세계 개발자 컨퍼런스(WWDC)에서 Apple의 [위치 버튼 만나기](https://developer.apple.com/videos/play/wwdc2021/10102/) 동영상을 시청하세요.

{% alert tip %}
이 기능을 사용하면 사용자에게 권한을 요청할 수 있는 추가 기회를 얻을 수 있습니다! iOS 15 이전에 위치 권한을 거부한 적이 있는 사용자가 위치 버튼을 클릭하면 마지막으로 거부된 상태에서 권한을 재설정할 수 있는 프롬프트가 표시됩니다.
{% endalert %}

### Braze에서 위치 버튼 사용하기

Braze에서 위치 버튼을 사용할 때는 추가 통합이 필요하지 않습니다. 사용자가 권한을 부여한 경우 앱은 평소와 같이 사용자 위치를 계속 전달해야 합니다.

Apple에 따르면, 이미 백그라운드 위치 액세스를 공유한 사용자의 경우 '앱 사용 중' 옵션은 iOS 15로 업그레이드한 후에도 해당 수준의 권한을 계속 부여합니다.

## Apple 메일 {#mail}

올해 Apple은 이메일 추적 및 개인정보 보호에 대한 많은 업데이트를 발표했습니다. 자세한 내용은 [블로그 게시물을](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature) 참조하세요.

## Safari IP 주소 위치

iOS 15에서는 사용자가 자신의 IP 주소에서 확인된 위치를 익명화하거나 일반화하도록 Safari를 구성할 수 있습니다. 위치 기반 타겟팅 또는 세분화를 사용할 때는 이 점을 염두에 두세요.

