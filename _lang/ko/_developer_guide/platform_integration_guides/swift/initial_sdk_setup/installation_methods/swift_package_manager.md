---
nav_title: 스위프트 패키지 매니저
article_title: iOS용 Swift 패키지 관리자 통합
platform: Swift
page_order: 1
description: "이 튜토리얼에서는 iOS용 스위프트 패키지 매니저를 사용하여 Braze Swift SDK를 설치하는 방법을 다룹니다."

---

# 스위프트 패키지 매니저 통합

> [스위프트 패키지 매니저](https://swift.org/package-manager/)(SPM)를 통해 Swift SDK를 설치하면 설치 과정의 대부분이 자동화됩니다. 이 프로세스를 시작하기 전에 [버전 정보를](https://github.com/braze-inc/braze-swift-sdk#version-information) 확인하여 사용 중인 환경이 Braze에서 지원되는지 확인하세요.

## 프로젝트에 종속성 추가하기

### SDK 버전 가져오기

프로젝트를 열고 프로젝트 설정으로 이동합니다. **Swift 패키지** 탭을 선택하고 패키지 목록 아래에 있는 <i class="fas fa-plus"></i> 추가 버튼을 클릭합니다.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이 형식 중 하나를 대신 사용하려면 해당 리포지토리의 설치 지침을 따릅니다.
{% endalert %}

텍스트 필드에 iOS Swift SDK 리포지토리 URL(`https://github.com/braze-inc/braze-swift-sdk`)을 입력합니다. **종속성 규칙** 섹션에서 SDK 버전을 선택합니다. 마지막으로 **패키지 추가를** 클릭합니다.

![]({% image_buster /assets/img/importsdk_example.png %})

### 패키지 선택

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 잘 제어할 수 있도록 합니다.

| 패키지 | 세부 정보 |
| ------- | ------- |
| `BrazeKit` | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다. |
| `BrazeLocation` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리를 제공합니다. |
| `BrazeUI` | 앱 내 메시지 및 콘텐츠 카드를 위한 Braze에서 제공하는 사용자 인터페이스 라이브러리입니다. |
{: .ws-td-nw-1}

#### 확장 라이브러리

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이므로 기본 애플리케이션 대상에 직접 추가해서는 안 됩니다. 대신 링크된 가이드에 따라 각각의 대상 확장에 개별적으로 통합합니다.
{% endalert %}

| 패키지 | 세부 정보 |
| ------- | ------- |
| `BrazeNotificationService` | 풍부한 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `BrazePushStory` | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다. |
{: .ws-td-nw-1}

 필요에 가장 적합한 패키지를 선택하고 **패키지 추가를** 클릭합니다. 최소한 `BrazeKit`를 선택해야 합니다.

![]({% image_buster /assets/img/add_package.png %})

## 다음 단계

[통합을 완료하려면]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/) 지침을 따르세요.

