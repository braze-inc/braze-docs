---
nav_title: 개요
article_title: iOS용 통합 개요
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "통합 개요"
guide_top_text: ""
description: "이 랜딩 페이지에서는 CocoaPods, 스위프트 패키지 매니저, Carthage 등을 위한 Braze SDK 통합 가이드를 다룹니다."

guide_featured_title: "기본 통합 옵션"
guide_featured_list:
- name: CocoaPods
  link: /developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: 스위프트 패키지 매니저(SPM)
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/braze_icons/swift.svg
- name: 카르타고
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/
  image: /assets/img/carthage.png
- name: 매뉴얼
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/
  image: /assets/img/braze_icons/tool-01.svg
- name: "통합 완료"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/flag-05.svg
- name: "기타 선택적 소프트웨어 개발 키트 사용자 정의"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/ios_sdk_integration
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

Braze iOS SDK를 설치하면 기본 분석 기능(세션 처리) 및 기본 인앱 메시지가 제공됩니다. 추가 채널 및 기능을 위해 통합을 추가로 사용자 정의해야 합니다. <br> <br> Braze iOS SDK는 CocoaPods, Carthage, 스위프트 패키지 매니저 또는 수동 통합을 사용하여 설치하거나 업데이트할 수 있습니다. <br> <br> 또한, Braze iOS SDK는 RubyMotion 앱을 완벽하게 지원합니다.

{% alert important %}
iOS SDK는 앱 IPA 파일에 1MB에서 2MB를 추가하고, APP 파일 외에도 프레임워크에 30MB를 추가합니다.
{% endalert %}

나열된 옵션 중 하나를 사용하여 통합을 완료하고 [통합 완료 단계]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/)를 따른 후 다른 SDK 사용자 지정(선택 사항)을 활성화하고 향후 캠페인의 요구 사항에 맞게 추가 채널 및 기능을 통합, 활성화 및 사용자 지정하는 단계를 진행합니다.  

<br>
