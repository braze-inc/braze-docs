---
nav_title: 문제 해결
article_title: 웹용 인앱 메시지 문제 해결
platform: Web
page_order: 5
channel: in-app messages
description: "이 페이지에는 인앱 메시징 전달 또는 표시와 관련된 일반적인 문제에 대해 취할 수 있는 문제 해결 단계가 포함되어 있습니다."

---

# 문제 해결

> 이 문서에서는 몇 가지 웹 SDK 문제 해결 시나리오를 제공합니다.

## 노출 수가 예상보다 낮습니다.

트리거는 세션 시작 시 디바이스와 동기화하는 데 시간이 걸리므로 사용자가 세션 시작 직후 이벤트를 기록하거나 구매하면 경쟁 조건이 발생할 수 있습니다. 한 가지 잠재적인 해결 방법은 세션 시작 시 트리거되도록 캠페인을 변경한 다음 의도한 이벤트 또는 구매를 세분화하는 것입니다. 이렇게 하면 이벤트가 발생한 후 다음 세션이 시작될 때 인앱 메시지가 전달된다는 점에 유의하세요.

## 예상 인앱 메시지가 표시되지 않았습니다.

대부분의 인앱 메시지 문제는 전달과 표시라는 두 가지 주요 카테고리로 분류할 수 있습니다. 예상 인앱 메시지가 디바이스에 표시되지 않는 이유를 해결하려면 먼저 \[인앱 메시지가 디바이스에 전달되었는지 확인해야 합니다]\[troubleshooting_iams_11], \[메시지 표시 문제 해결]\[troubleshooting_iams_12].

## 인앱 메시지 전달 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. 인앱 메시지가 디바이스에 전달되고 있는지 확인하려면, 인앱 메시지가 SDK에 의해 요청되고 Braze 서버에서 반환되는지 확인해야 합니다.

### 메시지 요청 및 반환 여부 확인

1. 대시보드에서 \[테스트 사용자]\[troubleshooting_iams_1] ]로 자신을 추가합니다.
2. 사용자를 대상으로 인앱 메시지 캠페인을 설정합니다.
3. 애플리케이션에서 새 세션이 발생하는지 확인합니다.
4. 이벤트 사용자 로그]\[troubleshooting_iams_3] ]를 사용하여 세션 시작 시 기기에서 인앱 메시지를 요청하는지 확인하세요. 테스트 사용자의 세션 시작 이벤트와 연결된 SDK 요청을 찾습니다.
  - 앱에서 트리거된 인앱 메시지를 요청하는 경우 **응답 데이터** 아래의 **요청된 응답** 필드에 `trigger` 이 표시되어야 합니다.
  - 앱에서 원본 인앱 메시지를 요청하는 경우 **응답 데이터** 아래의 **요청된 응답** 필드에 `in_app` 이 표시되어야 합니다.
5. 이벤트 사용자 로그]\[troubleshooting_iams_3] ]를 사용하여 응답 데이터에서 올바른 인앱 메시지가 반환되는지 확인하세요.<br>![]\[트러블슈팅_iams_5]

### 요청되지 않는 메시지 문제 해결

인앱 메시지가 요청되지 않는 경우, 세션 시작 시 인앱 메시지가 새로고침되므로 앱이 세션을 올바르게 추적하지 못할 수 있습니다. 또한 앱의 세션 시간 초과 의미에 따라 앱이 실제로 세션을 시작하고 있는지 확인하세요:

![성공적인 세션 시작 이벤트를 표시하는 이벤트 사용자 로그에서 발견된 SDK 요청]\[troubleshooting_iams_10]

### 반환되지 않는 메시지 문제 해결

인앱 메시지가 반환되지 않는다면 캠페인 타겟팅에 문제가 있는 것일 수 있습니다:

- 세그먼트에 사용자가 포함되어 있지 않습니다.
  - 사용자의 \[\*\*참여**]\[troubleshooting_iams_6] ] 탭에서 **세그먼트** 아래에 올바른 세그먼트가 표시되는지 확인합니다.
- 사용자가 이전에 인앱 메시지를 받은 적이 있으며 다시 받을 수 있는 자격이 없습니다.
  - **캠페인 컴포저의** **전달** 단계 아래 \[캠페인 재자격 설정]\[문제 해결_iams_7] ]을 확인하고 재자격 설정이 테스트 설정과 일치하는지 확인합니다.
- 사용자가 캠페인의 빈도 한도에 도달했습니다.
  - 캠페인 \[주파수 제한 설정]\[troubleshooting_iams_8] ]을 확인하여 테스트 설정과 일치하는지 확인하세요.
- 캠페인에 대조 그룹이 있는 경우 사용자가 대조 그룹에 속했을 수 있습니다.
  - 캠페인 이형 상품이 **컨트롤로** 설정된 수신된 캠페인 이형 상품 필터로 세그먼트를 생성하고 사용자가 해당 세그먼트에 속하는지 확인하여 이 문제가 발생했는지 확인할 수 있습니다.
  - 통합 테스트 목적으로 캠페인을 생성할 때는 대조군 추가를 선택 해제해야 합니다.

## 인앱 메시지 표시 {#troubleshooting-in-app-message-display}

앱에서 인앱 메시지를 성공적으로 요청하고 수신하고 있지만 표시되지 않는 경우 일부 디바이스 측 로직으로 인해 표시되지 않는 것일 수 있습니다:

- 트리거된 인앱 메시지는 \[트리거 간 최소 시간 간격]\[troubleshooting_iams_9], 기본값은 30초]에 따라 속도가 제한됩니다.
- `braze.subscribeToInAppMessage` 또는 `appboy.subscribeToNewInAppMessages` 을 통해 사용자 지정 인앱 메시지 처리를 사용하는 경우 해당 구독을 확인하여 인앱 메시지 표시에 영향을 미치지 않도록 하세요.

\[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
\[troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[troubleshooting_iams_4]: #세션-추적
\[troubleshooting_iams_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
\[troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
\[troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
\[troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
\[troubleshooting_iams_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
\[troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
\[troubleshooting_iams_11]: #문제해결-인앱-메시지-배달
\[troubleshooting_iams_12]: #문제해결-인앱-메시지-디스플레이
