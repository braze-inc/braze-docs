---
nav_title: 고급 설정
article_title: 고급 푸시 설정
platform: iOS
page_order: 5
description: "이 참조 문서에서는 알림 옵션, 소리, 만료 등과 같은 고급 iOS 푸시 알림 설정을 다룹니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 고급 설정

푸시 캠페인을 생성할 때 작성 단계에서 **설정**을 선택하여 사용 가능한 고급 설정을 확인합니다.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## 푸시 키-값 쌍에서 데이터 추출하기

Braze에서는 커스텀 정의 문자열 키-값 페어(`extras`)를 푸시 알림과 함께 애플리케이션에 전송할 수 있습니다. 추가 항목은 대시보드 또는 API를 통해 정의할 수 있으며, 푸시 위임 구현에 전달되는 `notification` 사전 내에서 키-값 페어로 사용할 수 있습니다.

## 경고 옵션

**경고 옵션** 확인란을 선택하여 알림이 기기에 표시되는 방식을 조정할 수 있는 키-값 드롭다운을 확인합니다.

## 콘텐츠 가용 플래그 추가

**콘텐츠 가용 플래그 추가** 확인란을 선택하여 기기가 백그라운드에서 새 콘텐츠를 다운로드하도록 지시합니다. 가장 일반적으로 [무음 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/) 보내고 싶은 경우 이 옵션을 선택할 수 있습니다.

## 변경 가능한 콘텐츠 플래그 추가

iOS 10 이상 기기에서 고급 수신기 사용자 지정을 활성화하려면 **변경 가능한 콘텐츠 플래그 추가** 확인란을 선택합니다. 이 플래그는 이 확인란의 값에 관계없이 [리치 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/rich_notifications/) 작성할 때 자동으로 전송됩니다.

## 앱 배지 수 업데이트

배치 수를 업데이트하려는 숫자를 입력하거나 Liquid 구문을 활용하여 사용자 지정 조건을 설정하세요. 애플리케이션의 `applicationIconBadgeNumber` 속성정보 또는 푸시 알림 페이로드를 통해 배지 수를 수동으로 업데이트할 수도 있습니다. 자세한 내용은 [배지 수]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/badges/) 관련 문서를 참조하세요.

## 소리

여기에서 앱 번들에 있는 사운드 파일의 경로를 입력하여 푸시 메시지를 수신할 때 재생할 사운드를 지정할 수 있습니다. 지정한 사운드 파일이 존재하지 않거나 'default' 키워드가 입력된 경우 Braze는 기기의 기본 알림 사운드를 사용합니다. 사용자 지정에 대한 자세한 내용은 [사용자 지정 사운드]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/custom_sounds/) 전용 문서를 참조하세요.

## 접기 ID

축소 ID를 지정하여 유사한 알림을 결합합니다. 동일한 축소 ID로 여러 알림을 발송한 경우, 기기에는 가장 최근 수신된 알림만 표시됩니다. [통합 알림에](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) 대한 Apple의 문서를 참조하세요.

## 만료 

**만료** 확인란을 선택하면 메시지의 만료 시간을 설정할 수 있습니다. 사용자 기기와 연결이 끊어지면 Braze는 지정된 시간까지 계속해서 메시지 발송을 시도합니다. 이 옵션을 설정하지 않으면 플랫폼은 기본적으로 30일 만료로 설정됩니다. 배달 전에 만료되는 푸시 알림은 실패로 간주되지 않으며 반송으로 기록되지 않습니다.

