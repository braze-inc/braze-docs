---
nav_title: 푸시 설정
article_title: iOS용 푸시 설정
platform: Swift
page_order: 7
description: "이 참조 문서에서는 Swift SDK의 알림 옵션, 소리, 만료 등과 같은 고급 iOS 푸시 알림 설정에 대해 설명합니다."
channel:
  - push

---

# 푸시 설정

> 대시보드를 통해 푸시 캠페인을 만들 때 **작성** 단계의 **설정** 탭을 클릭하면 사용 가능한 고급 설정을 볼 수 있습니다.

![][1]

## 키-값 쌍

Braze를 사용하면 사용자 정의 문자열 키-값 쌍( `extras`)을 푸시 알림과 함께 애플리케이션에 전송할 수 있습니다. 추가 정보는 대시보드 또는 API를 통해 정의할 수 있으며, 푸시 델리게이트 구현에 전달되는 `notification` 사전 내에서 키-값 쌍으로 사용할 수 있습니다.

## 경고 옵션

알림 **옵션** 확인란을 선택하면 알림이 디바이스에 표시되는 방식을 조정할 수 있는 키 값 드롭다운을 볼 수 있습니다.

## 콘텐츠 사용 가능 플래그 추가

**콘텐츠 사용 가능 플래그 추가 확인란을** 선택하면 디바이스가 백그라운드에서 새 콘텐츠를 다운로드하도록 지시할 수 있습니다. 가장 일반적으로는 \[무음 알림] 전송에 관심이 있는 경우][2] 에서 확인할 수 있습니다.

## 변경 가능한 콘텐츠 플래그 추가

고급 수신기 사용자 지정을 사용하려면 **변경 가능한 콘텐츠 플래그 추가** 확인란을 선택합니다. 이 플래그는 이 확인란의 값에 관계없이 \[리치 알림][3]]을 작성할 때 자동으로 전송됩니다.

## 앱 배지 수 업데이트

배지 수를 업데이트할 숫자를 입력하거나 Liquid 구문을 사용하여 사용자 지정 조건을 설정합니다. 프로그래밍 방식으로 메시지 배지 수를 업데이트할 수도 있습니다. [배지 수]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/) 전용 문서를 참조하세요.

## 소리

푸시 알림을 받을 때 사용자 지정 사운드와 함께 수신되도록 하려면 **사운드** 필드를 사용하여 사운드 파일의 프로토콜 URL을 지정하세요. 사용자 지정에 대한 자세한 내용은 [사용자 지정 사운드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/) 문서를 참조하세요.

## 접기 ID

유사한 알림을 통합하려면 축소 ID를 지정하세요. 동일한 축소 ID로 여러 개의 알림을 보내면 디바이스에는 가장 최근에 받은 알림만 표시됩니다. 통합 알림]에 대한 Apple 문서를 참조하세요][4].

## 만료 

**만료** 확인란을 선택하면 메시지의 만료 시간을 설정할 수 있습니다. 사용자 디바이스의 연결이 끊어지면 Braze는 지정된 시간까지 계속해서 메시지 전송을 시도합니다. 이 옵션을 설정하지 않으면 플랫폼은 기본적으로 30일 만료로 설정됩니다. 배달 전에 만료되는 푸시 알림은 실패로 간주되지 않으며 반송으로 기록되지 않습니다.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/
[4]:https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
