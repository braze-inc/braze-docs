---
nav_title: 추적 세션
article_title: Windows Universal용 세션 추적
platform: Windows Universal
page_order: 0
description: "이 참조 문서는 Windows Universal 플랫폼에서 세션을 추적하는 방법을 다룹니다."
hidden: true
---

# 분석
{% multi_lang_include archive/windows_deprecation.md %}

## 세션 추적

Braze SDK는 Braze 대시보드에서 사용자 인게이지먼트 및 기타 분석을 계산하는 데 사용되는 세션 데이터를 보고합니다. 다음 세션 의미론을 기반으로, Braze SDK는 세션 길이 및 Braze 대시보드 내에서 볼 수 있는 세션 수를 설명하는 "세션 시작" 및 "세션 종료" 데이터 포인트를 생성합니다.

### 세션 수명 주기

Braze Windows 통합은 앱이 실행될 때 세션 열림을 기록하고 애플리케이션이 닫힐 때 세션 닫힘을 기록합니다. `sessionTimeoutInSeconds`의 최소값은 1초입니다. 새 세션을 강제로 시작해야 하는 경우 사용자를 변경하여 수행할 수 있습니다.

### 테스트 세션 추적

세션을 고객을 통해 감지하려면 대시보드에서 고객을 찾아 고객 프로필의 "앱 사용"으로 이동하세요. "세션" 메트릭이 예상대로 증가하는지 확인하여 세션 추적 기술이 작동하는지 확인할 수 있습니다.

![앱 사용이 25회 세션으로 표시되었으며 마지막 사용은 두 시간 전, 첫 사용은 20일 전인 고객 프로필][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

