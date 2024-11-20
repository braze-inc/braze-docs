---
nav_title: 단위 테스트 (선택 사항)
article_title: iOS용 푸시 알림 단위 테스트
platform: iOS
page_order: 29.5
description: "이 참조 문서에서는 iOS 푸시 구현에 대한 선택적 단위 테스트를 구현하는 방법을 설명합니다."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 단위 테스트 {#unit-tests}

이 선택적 가이드는 앱 대리자가 [푸시 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)에 설명된 단계를 올바르게 따르는지 확인하는 몇 가지 단위 테스트를 구현하는 방법을 설명합니다. 

모든 테스트가 통과되면 일반적으로 코드 기반 푸시 설정 부분이 작동한다는 의미입니다. 테스트가 실패하면 단계를 잘못 따랐거나 유효한 사용자 지정이 기본 지침과 정확히 일치하지 않기 때문일 수 있습니다.

어느 쪽이든 통합 단계를 따랐는지 확인하고 회귀를 모니터링하는 데 도움이 되는 유용한 접근 방식이 될 수 있습니다.

## 1단계: 단위 테스트 대상 생성

Xcode의 앱 프로젝트에 단위 테스트 번들이 이미 포함되어 있는 경우 이 단계를 건너뜁니다.

앱 프로젝트에서 메뉴 **파일 > 새로 만들기 > 대상**으로 이동하여 새로운 '단위 테스트 번들'을 추가합니다. 이 번들은 Objective-C 또는 Swift를 사용할 수 있으며 어떤 이름도 지정할 수 있습니다. '테스트할 대상'을 기본 앱 대상으로 설정합니다.

## 2단계: 단위 테스트에 Braze 소프트웨어 개발 키트를 추가하십시오

처음에 [Braze SDK를 설치]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/)하는 데 사용한 동일한 방법을 사용하여 동일한 SDK 설치가 단위 테스트 대상으로 사용 가능한지 확인합니다. 예를 들어, CocoaPods를 사용하는 경우:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## 3단계: 단위 테스트에 OCMock 추가

CocoaPods, Carthage 또는 정적 라이브러리를 통해 [OCMock](https://ocmock.org/)을 테스트 대상에 추가하십시오. 예를 들어, CocoaPods를 사용하는 경우:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## 4단계: 추가된 라이브러리 설치 완료

Braze SDK 및 OCMock 설치를 완료합니다. 예를 들어 CocoaPods를 통해 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동하여 다음 명령을 실행합니다.

```
pod install
```

이 시점에서 CocoaPods가 생성한 Xcode 프로젝트 작업 공간을 열 수 있어야 합니다.

## 5단계: 푸시 테스트 추가

단위 테스트 대상에 새 Objective-C 파일을 만드십시오. 

단위 테스트 대상이 Swift에 있는 경우 Xcode에서 'Objective-C 브리징 헤더를 구성하시겠어요?'라고 물을 수 있습니다. 브리징 헤더는 선택 사항이므로 **생성하지 않음**을 클릭하고 여전히 이러한 단위 테스트를 성공적으로 실행할 수 있습니다.

새 파일에 HelloSwift 샘플 앱의 [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) 내용을 추가합니다.

## 6단계: 테스트 스위트 실행

앱의 유닛 테스트를 실행하세요. 일회성 검증 단계일 수 있습니다. 또는 테스트 스위트에 무기한으로 이를 포함시켜 회귀를 포착할 수 있습니다.

