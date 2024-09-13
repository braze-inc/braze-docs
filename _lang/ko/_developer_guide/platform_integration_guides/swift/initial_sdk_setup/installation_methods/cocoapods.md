---
nav_title: 코코아팟
article_title: iOS용 CocoaPods 통합
platform: Swift
page_order: 2
description: "이 참조 문서는 iOS용 CocoaPods를 사용하여 Braze Swift 소프트웨어 개발 키트를 통합하는 방법을 보여줍니다."

---

# CocoaPods 통합

## 1단계: 코코아팟 설치

iOS 소프트웨어 개발 키트를 [CocoaPods][apple_initial_setup_1]를 통해 설치하면 설치 과정의 대부분이 자동화됩니다. CocoaPods를 설치하려면 CocoaPods [시작 가이드][cocoapods_getting_started]를 참조하세요.

다음 명령어를 실행하여 시작하십시오:

```bash
$ sudo gem install cocoapods
```

CocoaPods에 문제가 있는 경우 CocoaPods \[문제 해결 가이드]\[apple_initial_setup_25]를 참조하십시오.

## 2단계: Podfile 구성하기

이제 CocoaPods Ruby Gem을 설치했으므로 Xcode 프로젝트 디렉토리에 `Podfile`이라는 파일을 만들어야 합니다.

{% alert note %}
버전 7.4.0부터 Braze Swift 소프트웨어 개발 키트는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 대신 이 형식 중 하나를 사용하려면 해당 저장소의 설치 지침을 따르십시오.
{% endalert %}

Podfile에 다음 줄을 추가하십시오:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit`에는 분석 및 푸시 알림을 지원하는 주요 소프트웨어 개발 키트 라이브러리가 포함되어 있습니다.

버전 Braze를 제안하여 포드 업데이트가 사소한 버전 업데이트보다 작은 모든 항목을 자동으로 가져오도록 합니다. 이것은 `pod 'BrazeKit' ~> Major.Minor.Build`처럼 보입니다. 최신 Braze 소프트웨어 개발 키트 버전을 주요 변경 사항과 함께 자동으로 통합하려면 Podfile에서 `pod 'BrazeKit'`을(를) 사용할 수 있습니다.

#### 추가 라이브러리

Braze Swift 소프트웨어 개발 키트는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 잘 제어할 수 있도록 합니다. `BrazeKit` 외에도 다음 라이브러리를 Podfile에 추가할 수 있습니다:

| 라이브러리 | 세부 정보 |
| ------- | ------- |
| `pod 'BrazeLocation'` | 위치 라이브러리 제공 위치 분석 및 지오펜스 모니터링 지원. |
| `pod 'BrazeUI'` | Braze 제공 인앱 메시지 및 콘텐츠 카드용 사용자 인터페이스 라이브러리. |
{: .ws-td-nw-1}

##### 확장 라이브러리

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이며, 메인 애플리케이션 대상에 직접 추가해서는 안 됩니다. 대신, 이러한 모듈 각각에 대해 별도의 확장 타겟을 생성하고 해당 타겟에 Braze 모듈을 가져와야 합니다.

| 라이브러리 | 세부 정보 |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리. |
| `pod 'BrazePushStory'` | 푸시 스토리를 지원하는 알림 콘텐츠 확장 라이브러리. |
{: .ws-td-nw-1}

## 3단계: Braze 소프트웨어 개발 키트 설치

Braze 소프트웨어 개발 키트 CocoaPod을 설치하려면 터미널에서 Xcode 앱 프로젝트 디렉토리로 이동한 후 다음 명령어를 실행하세요:
```
pod install
```

이 시점에서 CocoaPods가 생성한 새로운 Xcode 프로젝트 작업 공간을 열 수 있어야 합니다. 이 Xcode 워크스페이스를 Xcode 프로젝트 대신 사용하십시오.

![Braze 예제 폴더가 확장되어 새 `BrazeExample.workspace`.]\[apple_initial_setup_15]을(를) 표시합니다.

## 다음 단계

지침을 따르십시오 [통합을 완료하는]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## CocoaPods를 통해 Braze 소프트웨어 개발 키트를 업데이트하기

CocoaPod을 업데이트하려면 프로젝트 디렉토리 내에서 다음 명령어를 실행하십시오:

```
pod update
```

[apple_initial_setup_1]: http://cocoapods.org/
[cocoapods_getting_started]: https://guides.cocoapods.org/using/getting-started.html
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "코코아팟 설치 지침"
[apple_initial_setup_5]: https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h
\[apple_initial_setup_15]: {% image_buster /assets/img/braze_example_workspace.png %}
\[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods 문제 해결 Guide"
