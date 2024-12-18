---
nav_title: "고급 푸시 캠페인 설정"
article_title: 고급 푸시 캠페인 설정
page_type: reference
page_order: 6
description: "이 참고 문서에서는 알림 옵션, 플래그, 사운드, 만료 등 몇 가지 고급 푸시 캠페인 설정에 대해 설명합니다."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# 고급 푸시 캠페인 설정

> 이 참고 문서에서는 알림 옵션, 플래그, 사운드, 만료 등 몇 가지 고급 푸시 캠페인 설정에 대해 설명합니다.

푸시 참여를 만들 때 **작성** 단계에서 <i class="fas fa-cog"></i> 톱니바퀴 아이콘을 선택하여 메시지에 대한 고급 설정을 볼 수 있습니다.

![][1]

## 경고 옵션

여기에서 확인란을 선택하면 알림이 기기에 표시되는 방식을 조정할 수 있는 키 값의 드롭다운 메뉴가 표시됩니다.

## 콘텐츠 사용 가능 플래그 추가

`content-available` 플래그는 기기가 백그라운드에서 새 콘텐츠를 다운로드하도록 지시합니다. 가장 일반적으로는 [무음 알림 전송][2]에 관심이 있는 경우 확인할 수 있습니다.

## 변경 가능한 콘텐츠 플래그 추가

`mutable-content` 플래그를 사용하면 iOS 10 이상 기기에서 고급 수신기 사용자 지정이 가능합니다. 이 플래그는 이 확인란의 값에 관계없이 [리치 알림][3]을 작성할 때 자동으로 전송됩니다.

## 소리

여기에서 앱 번들에 있는 사운드 파일의 경로를 입력하여 푸시 메시지를 수신할 때 재생할 사운드를 지정할 수 있습니다. 지정한 사운드 파일이 존재하지 않거나 "default" 키워드를 입력하면 Braze는 기본 기기 알림음을 사용합니다.

## 접기 ID
Collapse ID(접기 ID)를 지정하여 유사한 알림을 합칠 수 있습니다. 동일한 접기 ID로 여러 알림을 발송한 경우, 기기에는 가장 최근 수신된 알림만 표시됩니다. 자세한 내용은 Apple의 [문서][4]]를 참조하세요.

## 만료 

**만료를** 선택하면 메시지의 만료 시간을 설정할 수 있는 옵션이 제공됩니다. 사용자의 디바이스가 연결이 끊어지면 Braze는 지정된 시간까지 계속해서 메시지를 보내려고 시도합니다. 이 옵션을 설정하지 않으면 플랫폼은 기본적으로 30일 만료로 설정됩니다. 배달 전에 만료되는 푸시 알림은 실패한 것으로 간주되지 않으며 반송으로 기록되지 않습니다.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[4]:https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
