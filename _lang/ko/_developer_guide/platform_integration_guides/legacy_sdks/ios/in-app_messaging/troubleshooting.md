---
nav_title: 문제 해결
article_title: iOS용 인앱 메시징 문제 해결
platform: iOS
page_order: 7
description: "이 참조 문서에서는 잠재적인 iOS 인앱 메시지 문제 해결 주제를 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 인앱 메시지 문제 해결하기

## 노출 횟수

#### 노출 또는 클릭 분석이 기록되지 않습니다.

메시지 표시 또는 클릭 동작을 수동으로 처리하도록 인앱 메시지 위임을 설정한 경우, 인앱 메시지에서 클릭 및 노출 횟수를 수동으로 기록해야 합니다.

#### 예상보다 적은 노출 횟수

트리거는 세션 시작 시 기기와 동기화하는 데 시간이 걸리므로 사용자가 세션 시작 직후 구매 또는 이벤트를 기록하면 경합 조건이 발생할 수 있습니다. 한 가지 가능한 해결 방법은 세션 시작 시 트리거하도록 캠페인을 변경한 다음, 의도한 이벤트 또는 구매를 세분화하는 것입니다. 이렇게 하면 이벤트가 발생한 후 다음 세션이 시작될 때 인앱 메시지가 전달됩니다.

## 예상 인앱 메시지가 표시되지 않았습니다.

대부분의 인앱 메시지 문제는 전달과 표시라는 두 가지 주요 카테고리로 분류할 수 있습니다. 예상 인앱 메시지가 디바이스에 표시되지 않는 문제를 해결하려면 먼저 [인앱 메시지가 디바이스에 전달되었는지](#troubleshooting-in-app-message-delivery) 확인한 다음 [메시지 표시 문제를](#troubleshooting-in-app-message-display) 해결해야 합니다.

### 인앱 메시지 전달 {#troubleshooting-in-app-message-delivery}

SDK는 세션 시작 시 Braze 서버에 인앱 메시지를 요청합니다. 인앱 메시지가 기기에 전달되고 있는지 확인하려면 인앱 메시지가 SDK에 의해 요청되고 Braze 서버에 의해 반환되는지 확인해야 합니다.

#### 메시지 요청 및 반환 여부 확인

1. 테스트 사용자]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) 대시보드에서)로 자신을 추가합니다.
2. 사용자를 대상으로 인앱 메시지 캠페인을 설정합니다.
3. 애플리케이션에서 새 세션이 발생하는지 확인합니다.
4. 이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) )를 사용하여 세션 시작 시 디바이스에서 인앱 메시지를 요청하는지 확인하세요. 테스트 사용자의 세션 시작 이벤트와 연결된 SDK 요청을 찾습니다.
  - 앱에서 트리거된 인앱 메시지를 요청하는 경우 **응답 데이터** 아래 **요청된 응답** 필드에 `trigger`가 표시되어야 합니다.
  - 앱에서 원본 인앱 메시지를 요청하는 경우 **응답 데이터** 아래 **요청된 응답** 필드에 `in_app`이 표시되어야 합니다.
5. 이벤트 사용자 로그]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) )를 사용하여 응답 데이터에서 올바른 인앱 메시지가 반환되는지 확인하세요.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### 요청되지 않는 메시지 문제 해결

인앱 메시지가 요청되지 않는 경우 앱이 세션을 올바르게 추적하지 않을 수 있습니다. 인앱 메시지는 세션 시작 시 새로 고쳐지기 때문입니다. 또한 앱의 세션 제한 시간 의미에 따라 앱이 실제로 세션을 시작했는지 확인해야 합니다.

![성공적인 세션 시작 이벤트를 표시하는 이벤트 사용자 로그에서 발견된 SDK 요청.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### 반환되지 않는 메시지 문제 해결

인앱 메시지가 반환되지 않는다면 캠페인 타겟팅에 문제가 있는 것일 수 있습니다:

- 세그먼트에 사용자가 포함되어 있지 않습니다.
  - 사용자의 [\*\*참여**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) 탭에서 **세그먼트** 아래에 올바른 세그먼트가 표시되는지 확인하세요.
- 사용자가 이전에 인앱 메시지를 받은 적이 있으며 다시 받을 자격이 없습니다.
  - **캠페인 컴포저의** **전달** 단계 아래 [캠페인 재자격 설정]({{ site.baseurl }}/user_guide/참여_tools/campaigns/building_campaigns/delivery_types/reeligibility/) )을 확인하고 재자격 설정이 테스트 설정과 일치하는지 확인합니다.
- 사용자가 캠페인의 빈도 한도에 도달했습니다.
  - 캠페인 [빈도 제한 설정]({{ site.baseurl }}/user_guide/참여_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) )을 확인하여 테스트 설정과 일치하는지 확인하세요.
- 캠페인에 대조 그룹이 있는 경우 사용자가 대조 그룹에 속했을 수 있습니다.
  - 캠페인 이형 상품이 **컨트롤로** 설정된 수신된 캠페인 이형 상품 필터로 세그먼트를 생성하고 사용자가 해당 세그먼트에 속하는지 확인하여 이 문제가 발생했는지 확인할 수 있습니다.
  - 통합 테스트 목적으로 캠페인을 생성할 때는 대조군 추가를 옵트아웃해야 합니다.

### 인앱 메시지 표시 {#troubleshooting-in-app-message-display}

앱에서 인앱 메시지를 성공적으로 요청 및 수신하고 있지만 표시되지 않는 경우 일부 기기 측 로직으로 인해 표시되지 않는 것일 수 있습니다.

- 트리거된 인앱 메시지는 트리거 사이의 [최소 시간 간격]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers)을 기준으로 속도 제한이 적용되며, 기본값은 30초입니다.
- 인앱 메시지 처리를 사용자 지정하기 위해 위임을 설정한 경우, 위임이 인앱 메시지 표시를 방해하지 않는지 확인합니다.
- 이미지 다운로드에 실패하면 이미지가 포함된 인앱 메시지가 표시되지 않습니다. `SDWebImage` 프레임워크가 제대로 통합되지 않은 경우 이미지 다운로드는 항상 실패합니다. 기기 로그를 확인하여 이미지 다운로드가 실패하지 않았는지 확인하십시오.
- 기기 방향이 인앱 메시지에 지정된 방향과 일치하지 않으면 인앱 메시지가 표시되지 않습니다. 디바이스의 방향이 올바른지 확인하세요.


