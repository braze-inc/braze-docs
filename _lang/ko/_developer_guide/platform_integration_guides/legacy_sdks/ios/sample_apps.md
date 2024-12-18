---
nav_title: 샘플 앱
article_title: iOS용 샘플 앱
platform: iOS
page_order: 9
description: "이 참조 문서는 iOS 샘플 앱을 다룹니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 샘플 앱

Braze SDK에는 각각 사용자의 편의를 위해 리포지토리 내 샘플 애플리케이션이 포함되어 있습니다. 이러한 각 앱은 완전히 빌드할 수 있으므로 자체 애플리케이션 내에서 구현하는 동시에 Braze 기능을 테스트할 수 있습니다. 자체 애플리케이션 내 동작과 샘플 애플리케이션 내 예상 동작 및 코드 경로를 비교하여 테스트하는 것은 발생할 수 있는 문제를 디버깅하는 훌륭한 방법입니다.

## 테스트 애플리케이션 빌드
몇 가지 테스트 애플리케이션은 [iOS SDK GitHub 저장소인 앱보이](https://github.com/appboy/appboy-ios-sdk "iOS GitHub 저장")소에서 사용할 수 있습니다. 이 지침을 따라 테스트 애플리케이션을 구축하고 실행하십시오.

1. 새 [워크스페이스]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)를 만들고 앱 식별자 API 키를 기록하십시오.
2. `AppDelegate.m` 파일의 해당 필드에 API 키를 입력합니다.

푸시 알림은 iOS 테스트 애플리케이션에 추가 구성이 필요합니다. 자세한 내용은 [iOS 푸시 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/)을 참조하십시오.

