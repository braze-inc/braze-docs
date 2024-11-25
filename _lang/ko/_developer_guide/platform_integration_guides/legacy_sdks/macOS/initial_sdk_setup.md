---
nav_title: 초기 SDK 설정
article_title: MacOS용 초기 SDK 설정
platform: MacOS
page_order: 0
page_type: reference
description: "이 참조 문서에서는 macOS에서 Braze SDK의 초기 통합을 위한 리소스를 제공합니다."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 초기 SDK 설정

> 이 참조 문서에서는 MacOS용 Braze SDK를 설치하는 방법을 설명합니다. 

버전 [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0)부터 Braze SDK는 스위프트 패키지 매니저를 통해 통합할 때 [Mac Catalyst](https://developer.apple.com/mac-catalyst/)를 사용하여 앱의 macOS를 지원합니다. 현재 SDK는 CocoaPods 또는 Carthage를 사용할 때 Mac Catalyst를 지원하지 않습니다.

{% alert note %}
Mac Catalyst로 앱을 빌드하려면 <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple 설명서</a>를 참조하세요.
{% endalert %}

앱이 Catalyst를 지원하면 [다음 지침에 따라 스위프트 패키지 매니저를 사용]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)하여 Braze SDK를 앱으로 가져옵니다.

## 지원되는 기능

Braze는 Mac Catalyst에서 실행할 때 [푸시 알림]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), [콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/#content-cards-data-model), [인앱 메시지]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/), [자동 위치 수집]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)을 지원합니다.

푸시 스토리, 리치 푸시 및 지오펜스는 macOS에서 지원되지 않습니다.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
