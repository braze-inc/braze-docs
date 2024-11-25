---
nav_title: 설치 제거 추적
article_title: iOS용 추적 제거
platform: Swift
page_order: 7
description: "이 문서에서는 Swift SDK를 위한 제거 추적을 구성하는 방법을 다룹니다."

---

# 제거 추적

> iOS 앱의 앱 제거 추적을 설정하는 방법을 알아두면 앱이 Braze 앱 제거 추적 푸시를 받을 때 원치 않는 자동 조치를 취하지 않도록 할 수 있습니다. 제거 추적은 페이로드에 Braze 플래그가 포함된 백그라운드 푸시 알림을 활용합니다. 일반적인 정보는 [제거 추적 제거][6] 를 참조하세요.

{% alert important %}
제거 추적은 정확하지 않을 수 있다는 점에 유의하세요. Braze에 표시되는 지표는 지연되거나 부정확할 수 있습니다.
{% endalert %}

## 1단계: 백그라운드 푸시 사용

Xcode 프로젝트에서 **기능으로** 이동하여 **백그라운드 모드가** 활성화되어 있는지 확인합니다. 자세한 내용은 [무음 푸시 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) 참조하세요.

## 2단계: Braze 백그라운드 푸시 확인

Braze는 백그라운드 푸시 알림을 사용하여 제거 추적 분석을 수집합니다. 제거 추적 알림을 받은 애플리케이션이 [원치 않는 동작]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/)을 취하지 않는지 확인하세요.

## 3단계: Braze 대시보드에서 테스트

그런 다음, Braze 대시보드에서 테스트 푸시를 보내세요. 이 테스트 푸시는 사용자 프로필을 업데이트하지 않는다는 점에 유의하세요.

1. **캠페인** 페이지에서 푸시 알림 캠페인을 생성하고 **iOS 푸시**를 플랫폼으로 선택합니다.
2. **설정** 페이지에서 `appboy_uninstall_tracking` 키를 해당 값 `true`와 함께 추가하고 **콘텐츠 사용 가능 플래그 추가**를 선택합니다
3. **미리보기** 페이지를 사용하여 테스트 제거 추적 푸시를 직접 전송합니다.
4. 앱이 푸시 수신 시 원치 않는 자동 동작을 수행하지 않는지 확인합니다.

{% alert important %}
이 테스트 단계는 Braze에서 제거 추적 푸시를 보내기 위한 프록시입니다. 배지 수를 활성화한 경우 테스트 푸시와 함께 배지 번호가 전송되지만, Braze의 제거 추적 푸시는 애플리케이션에 배지 번호를 설정하지 않습니다.
{% endalert %}

## 4단계: 제거 추적 활성화

[제거 추적 활성화]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) 지침을 따릅니다.

