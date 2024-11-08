---
nav_title: 샘플 앱
article_title: iOS용 샘플 앱
platform: Swift
page_order: 9
search_rank: 2
description: "이 문서에서는 iOS Swift SDK 샘플 앱을 다룹니다."

---

# 샘플 앱

> Braze SDK에는 각각 사용자의 편의를 위해 리포지토리 내 샘플 애플리케이션이 포함되어 있습니다. 이러한 각 앱은 완전히 빌드할 수 있으므로 자체 애플리케이션 내에서 구현하는 동시에 Braze 기능을 테스트할 수 있습니다. 

자체 애플리케이션 내 동작과 샘플 애플리케이션 내 예상 동작 및 코드 경로를 비교하여 테스트하는 것은 발생할 수 있는 문제를 디버깅하는 훌륭한 방법입니다.

## 예제 탐색

[Swift SDK GitHub 리포지토리](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)의 `Examples` 폴더에서 여러 테스트 애플리케이션을 사용할 수 있습니다. README에서는 다음과 같은 샘플 통합의 모든 다양한 순열에 대해 설명합니다.

1. 통합 유형(스위프트 패키지 매니저, CocoaPods, 수동)
2. 코딩 언어(Swift 및 Objective-C)
3. 플랫폼(iOS, tvOS, Mac Catalyst 등)
4. 기능(인앱 메시지, 콘텐츠 카드, 위치, 리치 푸시, 푸시 스토리 등)
5. 사용자 지정 유형(기본 UI, 완전 사용자 지정 UI)

## 테스트 애플리케이션 빌드

다음 지침에 따라 테스트 애플리케이션을 빌드하고 실행하세요.

1. 새 [워크스페이스]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)를 생성하고 앱 식별자 API 키와 엔드포인트를 기록합니다.
2. 통합 방법(스위프트 패키지 매니저, CocoaPods, 수동)에 따라 적절한 `xcodeproj` 파일을 선택하여 엽니다.
3. `Credentials` 파일의 해당 필드에 API 키와 엔드포인트를 입력합니다.

