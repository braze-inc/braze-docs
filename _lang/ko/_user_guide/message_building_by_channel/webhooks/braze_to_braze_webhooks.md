---
nav_title: Braze-to-Braze 웹훅 만들기
article_title: Braze-to-Braze 웹훅 만들기
page_order: 3
channel:
  - webhooks
description: "이 참조 문서에서는 사용자 업데이트와 Braze-to-Braze 웹훅을 사용할 때와 Braze-to-Braze 웹훅을 만드는 방법을 다룹니다."

---

# Braze-to-Braze 웹훅 만들기

> Braze-to-Braze 웹훅을 사용하면 Braze 내에서 [Braze REST API]({{site.baseurl}}/api/basics/)를 호출할 수 있습니다. [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 사용하여 [캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) 또는 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/)에서 호출할 수 있습니다. API 트리거 캔버스와 같은 오케스트레이션 작업에 사용하세요. 캔버스에서 [사용자 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 또는 [구매]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)를 업데이트하려면 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 사용하세요. 사용자 프로필 변경을 위해 설계되었으며 업데이트를 더 효율적으로 처리합니다.

이 문서에서 최대한 많은 정보를 얻으려면 [웹훅 작동 방식]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)과 Braze에서 [웹훅 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)에 익숙해야 합니다.

## 사용자 데이터 변경을 위해 사용자 업데이트를 사용하세요.

캔버스 내에서 사용자 프로필을 업데이트하려면, [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 수정, [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 기록 또는 [구매]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) 기록을 포함하여 Braze-to-Braze 웹훅 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 사용하세요. 

사용자 업데이트는 여러 변경 사항을 그룹화하여 배치로 전송하므로 웹훅보다 빠릅니다. 웹훅보다 설정이 더 쉽고 [고급 JSON 작성기]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer)를 통해 복잡한 업데이트를 지원합니다. 예를 들어 사용자가 메시지를 본 횟수를 세려면 Braze-to-Braze 웹훅 대신 사용자 업데이트의 [증가 및 감소 기능]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values)를 사용하세요.

{% alert tip %}
캔버스에 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 추가하여 JSON 작성기를 사용하여 사용자의 속성, 이벤트 및 구매를 업데이트하세요.
{% endalert %}

## Braze-to-Braze 웹훅을 사용할 때

사용자 업데이트는 사용자 프로필을 업데이트하기 위해 Braze-to-Braze 웹훅과 거의 동일한 작업을 처리할 수 있습니다. 단순한 커스텀 속성을 넘어 복잡한 업데이트를 위해 [고급 JSON 작성기]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer)를 사용할 수 있습니다.

Braze 내에서 Braze의 [REST API]({{site.baseurl}}/api/basics/)를 호출해야 할 때 Braze-to-Braze 웹훅을 사용할 수 있습니다. 이는 캔버스 단계에서 직접 사용자 업데이트 외의 시나리오에 해당합니다. 일반적인 예는 다음과 같습니다:

- 다른 캔버스에서 [API 트리거 캔버스]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 트리거하기
- Braze에서 하나의 워크플로우가 전용 캔버스 구성 요소가 없는 API를 호출해야 하는 오케스트레이션 패턴을 위해 다른 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/)을 호출합니다.

캔버스 내 사용자 업데이트의 경우, 권장 방법은 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 사용하는 것입니다.

## 필수 조건

Braze-to-Braze 웹훅을 생성하려면 도달하려는 엔드포인트에 대한 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다. 예를 들어, API 트리거 캔버스를 트리거하려면 `canvas.trigger.send` 권한이 있는 API 키가 필요합니다.

## Braze-to-Braze 웹훅 설정하기

Braze-to-Braze 웹훅을 생성하는 일반적인 워크플로우는 다음 단계를 따릅니다:

1. 캠페인 또는 캔버스 구성 요소로 [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 만듭니다. 
2. **빈 템플릿**을 선택합니다.
3. **작성** 탭에서 API 사용 사례에 대한 **웹훅 URL** 및 **요청 본문**을 지정합니다.
4. **설정** 탭에서 엔드포인트에서 요구하는 대로 **HTTP 메서드** 및 **요청 헤더**를 지정합니다.
5. 추가 전달 설정(예: 사용자 정의 이벤트에서 트리거하기)을 구성하고 나머지 캠페인 또는 캔버스를 구축합니다.

## 초기 캔버스에서 두 번째 캔버스 트리거하기

이 사용 사례에서는 두 개의 캔버스를 생성하고 Braze-to-Braze 웹훅을 사용하여 첫 번째 캔버스에서 두 번째 캔버스를 트리거합니다. 이는 사용자가 다른 캔버스에서 특정 지점에 도달할 때 항목 트리거처럼 작동합니다.

1. 첫 번째 캔버스에 의해 트리거되어야 하는 두 번째 캔버스를 만드는 것으로 시작하세요.
2. 캔버스 **입력 일정**의 경우 **API 트리거됨**을 선택합니다.
3. **캔버스 ID**를 기록해 두세요. 이것은 나중 단계에서 필요합니다.
4. 두 번째 캔버스의 단계를 계속 구축한 다음 캔버스를 저장합니다.
5. 마지막으로 첫 번째 캔버스를 만듭니다. 두 번째 캔버스를 트리거할 단계를 찾아 웹훅을 사용하여 새 단계를 만듭니다.

웹훅을 구성할 때 다음을 참조하세요:

- **웹훅 URL:** [REST 엔드포인트 URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) 뒤에 `/canvas/trigger/send` 을 입력합니다. 예를 들어, `US-06` 인스턴스의 경우 URL은 `https://rest.iad-06.braze.com/canvas/trigger/send`가 됩니다.
- **요청 본문:** 원시 텍스트

#### Request headers and method

Braze는 API 키와 콘텐츠 유형을 선언하는 다른 HTTP 헤더를 포함하는 권한 부여를 위한 HTTP 헤더가 필요합니다.

- **Request Headers:**
  - **권한:** `Bearer YOUR_API_KEY`
  - **콘텐츠 유형:** `application/json`
- **HTTP 메서드:** `POST`

`YOUR_API_KEY`을 `canvas.trigger.send` 권한이 있는 Braze API 키로 교체합니다. Braze 대시보드에서 **설정** > **API 키**로 이동하여 API 키를 생성할 수 있습니다.

![웹훅에 대한 요청 헤더는 Braze 대시보드에서 권한 및 콘텐츠 유형 필드를 보여줍니다.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

텍스트 필드에 `/canvas/trigger/send` 요청을 추가합니다. 자세한 내용은 [API 트리거 전달을 통한 캔버스 메시지 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 참조하세요. 다음은 이 엔드포인트의 요청 본문 예시이며, `your_canvas_id`는 두 번째 캔버스의 캔버스 ID입니다:

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

사용자가 첫 번째 캔버스의 이 웹훅 단계에 도달하면, Braze는 API를 통해 해당 사용자에 대한 두 번째 캔버스를 트리거합니다.

## 고려 사항

- **사용자 업데이트:** 캔버스에서 사용자 프로필(속성, 이벤트, 구매)을 업데이트하려면, 더 나은 효율성과 비용 효과를 위해 Braze-to-Braze 웹훅 대신 [사용자 업데이트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 사용하세요.
- Braze-to-Braze 웹훅은 엔드포인트 [요금 제한]({{site.baseurl}}/api/api_limits/)의 적용을 받습니다.
- 사용자 프로필에 대한 업데이트는 전체 소비량에 포함되는 [데이터 포인트]({{site.baseurl}}/user_guide/data/data_points/)을 발생시키며, 메시징 엔드포인트를 통해 다른 메시지를 트리거하는 것은 그렇지 않습니다.
- [익명 사용자]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)를 타겟팅하려면, 웹훅의 요청 본문에서 `braze_id` 대신 `external_id`을 사용하세요.
- Braze-to-Braze 웹훅을 재사용을 위해 [웹훅 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/)으로 저장할 수 있습니다.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) to view and troubleshoot webhook failures.


