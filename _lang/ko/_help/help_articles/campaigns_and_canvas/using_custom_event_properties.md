---
nav_title: 커스텀 이벤트 속성 로깅
article_title: 커스텀 이벤트 속성 로깅
page_order: 3
page_type: solution
description: "이 도움말 문서는 커스텀 이벤트가 예상대로 기록되도록 보장하기 위한 세 가지 중요한 점검을 안내합니다."
tool: 
- Campaigns
- Canvas
---

# 커스텀 이벤트 속성 로깅

세 가지 중요한 확인 사항이 있습니다. 커스텀 이벤트가 예상대로 기록되고 있는지 확인하세요.

* [어떤 이벤트가 기록되는지 확인](#verify-events)
* [로그 확인](#verify-log)
* [값 확인](#verify-values)

## 커스텀 이벤트 속성 확인

[커스텀 이벤트 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)은 커스텀 이벤트를 설명하는 메타데이터입니다. 커스텀 이벤트가 기록될 때마다 여러 속성이 기록될 수 있습니다.

### 이벤트 확인

개발자에게 어떤 이벤트 속성정보가 추적되고 있는지 확인하세요. 모든 이벤트 속성은 대소문자를 구분한다는 점을 명심하세요. 커스텀 이벤트 추적에 대한 추가 정보는 플랫폼에 따라 다음 기사를 확인하세요.

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### 로그 확인

이벤트 속성이 성공적으로 추적되었는지 확인하려면 **커스텀 이벤트** 페이지에서 모든 이벤트 속성을 볼 수 있습니다.

1. **데이터 설정** > **커스텀 이벤트**로 이동합니다.
2. 목록에서 커스텀 이벤트를 찾으세요.
3. 이벤트를 위해 **속성 관리**를 클릭하십시오. 이것은 이벤트와 관련된 속성의 이름을 보여줍니다.

### 값 확인

사용자를 테스트 사용자로 추가한 후, 값을 확인하려면 다음 단계를 따르세요. 

1. 앱 내에서 커스텀 이벤트를 수행합니다.
2. 데이터가 플러시될 때까지 약 10초 정도 기다리세요.
3. [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab)를 새로고침하여 커스텀 이벤트 및 함께 전달된 이벤트 속성정보 값을 확인하세요.

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 날짜: 2023년 4월 10일_

