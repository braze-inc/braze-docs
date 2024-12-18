---
nav_title: CocoaPods
article_title: iOS용 CocoaPods 통합
platform: Swift
page_order: 2
description: "이 참조 문서에서는 iOS용 CocoaPods를 사용하여 Braze Swift SDK를 통합하는 방법을 설명합니다."

---

# CocoaPods 통합

## 1단계: CocoaPods 설치

[CocoaPods](http://cocoapods.org/)를 통해 iOS SDK를 설치하면 대부분의 설치 과정이 자동으로 수행됩니다. CocoaPods를 설치하려면 CocoaPods [시작 가이드](https://guides.cocoapods.org/using/getting-started.html)를 참조하세요.

시작하려면 다음 명령을 실행하세요:

```bash
$ sudo gem install cocoapods
```

CocoaPods와 관련된 문제가 있는 경우 CocoaPods 문제 [해결 가이드CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "문제 해결 가이드를") 참조하세요.

## 2단계: Podfile 구성

CocoaPods Ruby Gem을 설치했으므로 Xcode 프로젝트 디렉토리에 `Podfile` 파일을 만들어야 합니다.

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이 형식 중 하나를 대신 사용하려면 해당 리포지토리의 설치 지침을 따릅니다.
{% endalert %}

포드파일에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit`에는 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리가 포함되어 있습니다.

포드 업데이트에서 부 버전 업데이트보다 작은 내용을 자동으로 가져올 수 있도록 Braze 버전을 설정하는 것이 좋습니다. `pod 'BrazeKit' ~> Major.Minor.Build`와 유사합니다. 최신 Braze SDK 버전을 자동으로 통합하려면 주요 변경 사항이 있어도 Podfile에서 `pod 'BrazeKit'`를 사용하면 됩니다.

#### 추가 라이브러리

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 잘 제어할 수 있도록 합니다. `BrazeKit` 외에도 다음 라이브러리를 Podfile에 추가할 수 있습니다.

| 라이브러리 | 세부 정보 |
| ------- | ------- |
| `pod 'BrazeLocation'` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리를 제공합니다. |
| `pod 'BrazeUI'` | 앱 내 메시지 및 콘텐츠 카드를 위한 Braze에서 제공하는 사용자 인터페이스 라이브러리입니다. |
{: .ws-td-nw-1}

##### 확장 라이브러리

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이며, 메인 애플리케이션 대상에 직접 추가해서는 안 됩니다. 대신, 이러한 모듈 각각에 대해 별도의 확장 대상을 생성하고 해당 대상으로 Braze 모듈을 가져와야 합니다.

| 라이브러리 | 세부 정보 |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | 풍부한 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `pod 'BrazePushStory'` | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리입니다. |
{: .ws-td-nw-1}

## 3단계: Braze SDK 설치하기

Braze SDK CocoaPod을 설치하려면 터미널에서 Xcode 앱 프로젝트 디렉토리로 이동한 후 다음 명령어를 실행합니다.
```
pod install
```

이때 CocoaPods에서 생성한 새 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용해야 합니다.

![Braze 예제 폴더가 확장되어 새로운 `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

## 다음 단계

[통합을 완료하려면]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/) 지침을 따르세요.

## CocoaPod를 통해 Braze SDK 업데이트하기

CocoaPod를 업데이트하려면 프로젝트 디렉토리에서 다음 명령을 실행하면 됩니다:

```
pod update
```

