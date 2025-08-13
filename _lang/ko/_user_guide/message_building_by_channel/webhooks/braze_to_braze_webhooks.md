---
nav_title: 브레이즈 투 브레이즈 웹훅 만들기
article_title: 브레이즈 투 브레이즈 웹훅 만들기
page_order: 3
channel:
  - webhooks
description: "이 문서에서는 주요 사용 사례에 대한 Braze-to-Braze 웹훅을 만드는 방법에 대해 설명합니다."

---

# Braze-to-Braze 웹훅 만들기

> 웹훅을 사용하여 Braze [REST API와]({{site.baseurl}}/api/basics/) 통신할 수 있으며, 기본적으로 API가 허용하는 모든 작업을 수행할 수 있습니다. Braze는 이를 Braze에서 Braze로 통신하는 웹훅인 Braze 대 Braze 웹훅이라고 부릅니다. 이 페이지의 사용 사례는 사용자가 [웹훅의 작동 방식과]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) Braze에서 [웹훅을 만드는]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 방법에 익숙하다고 가정합니다.

## 필수 조건

Braze-to-Braze 웹훅을 만들려면 연결하려는 엔드포인트에 대한 권한이 있는 [API 키가]({{site.baseurl}}/api/api_key/) 필요합니다.

## Braze-to-Braze 웹훅 설정하기

웹훅 요청의 세부 사항은 사용 사례마다 다르지만, Braze 대 Braze 웹훅을 만드는 일반적인 워크플로는 동일하게 유지됩니다.

1. 캠페인 또는 캔버스 구성 요소로 [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 만듭니다. 
2. **빈 템플릿**을 선택합니다.
3. **작성** 탭에서 사용 사례에 명시된 대로 **웹훅 URL과** **요청 본문을** 지정합니다.
4. **설정** 탭에서 사용 사례에 명시된 대로 **HTTP 메서드** 및 **요청 헤더를** 지정합니다.
5. 필요에 따라 나머지 웹훅을 계속 구축하세요. 일부 사용 사례에는 커스텀 이벤트에서 캠페인 또는 캔버스를 트리거하는 것과 같은 특정 전달 설정이 필요합니다.

## 사용 사례

브레이즈 투 브레이즈 웹훅으로 할 수 있는 일은 많지만, 시작하기 위한 몇 가지 사용 사례는 다음과 같습니다:

- 사용자가 메시지를 수신할 때 카운터에 대한 정수 사용자 지정 속성을 증가시킵니다.
- 초기 캔버스에서 두 번째 캔버스를 트리거합니다.

{% alert tip %}
캔버스에 사용자 [업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)를 추가하여 JSON 작성기에서 사용자의 속성, 이벤트 및 구매를 추적할 수 있습니다. 이렇게 하면 이러한 업데이트가 일괄 처리되므로 Braze는 Braze-Braze 웹훅보다 더 효율적으로 업데이트를 처리할 수 있습니다.
{% endalert %}

### 사용 사례: 카운터의 정수 사용자 지정 속성을 증가시킵니다.

이 사용 사례는 커스텀 속성을 생성하고 Liquid를 사용하여 특정 작업이 발생한 횟수를 계산하는 것입니다. 

예를 들어, 사용자가 활성 인앱 메시지 캠페인을 본 횟수를 계산하여 세 번 본 후에는 다시는 캠페인을 수신하지 못하도록 할 수 있습니다. Braze에서 Liquid 로직으로 수행할 수 있는 작업에 대한 더 많은 아이디어는 [Liquid 사용 사례 라이브러리]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)에서 확인하세요.

Braze 대 Braze 웹훅을 만드는 일반적인 단계를 따르고, 웹훅을 구성할 때 다음을 참조하세요:

- **웹훅 URL:** [REST 엔드포인트 URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) 뒤에 `/users/track` 을 입력합니다. 예를 들어 `US-06` 인스턴스의 경우 URL은 `https://rest.iad-06.braze.com/users/track` 이 됩니다.
- **요청 본문:** 원시 텍스트

#### 요청 헤더 및 방법

Braze는 인증을 위해 API 키가 포함된 HTTP 헤더와 `content-type`을 선언하는 헤더가 필요합니다.

- **요청 헤더:**
  - **권한 부여:** 무기명 {YOUR_API_KEY}
  - **Content-Type:** application/json
- **HTTP 메서드:** POST

`YOUR_API_KEY`를 `users.track` 권한이 있는 Braze API 키로 바꿉니다. Braze 대시보드의 **설정** > **API 키**에서 API 키를 생성할 수 있습니다.

![웹훅의 요청 헤더.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### 요청 본문

요청 본문에 사용자 추적 요청을 추가하고 Liquid에 카운터 변수를 할당합니다. 자세한 내용은 [`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 참조하세요.

다음은 이 엔드포인트에 필요한 Liquid와 요청 본문의 예시이며, 여기서 `your_attribute_count` 은 사용자가 메시지를 본 횟수를 계산하는 데 사용하는 속성입니다:

{% raw %}
```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Each time a custom attribute counter is updated (incremented or decremented) it will consume a [data point]({{site.baseurl}}/user_guide/data/data_points/), which counts toward your overall consumption.
{% endalert %}

### 사용 사례: 초기 캔버스에서 두 번째 캔버스 트리거하기

이 사용 사례에서는 두 개의 캔버스를 만들고 웹훅을 사용하여 첫 번째 캔버스에서 두 번째 캔버스를 트리거합니다. 이는 사용자가 다른 캔버스에서 특정 지점에 도달할 때 항목 트리거처럼 작동합니다.

1. 첫 번째 캔버스에 의해 트리거되어야 하는 두 번째 캔버스를 만드는 것으로 시작하세요. 
2. 캔버스 **입력 일정**의 경우 **API 트리거됨**을 선택합니다.
3. **캔버스 ID**를 기록해 두세요. 나중 단계에서 이 정보가 필요합니다.
4. 두 번째 캔버스의 단계를 계속 구축한 다음 캔버스를 저장합니다.
5. 마지막으로 첫 번째 캔버스를 만듭니다. 두 번째 캔버스를 트리거할 단계를 찾아 웹훅을 사용하여 새 단계를 만듭니다. 

웹훅을 구성할 때 다음을 참조하세요:

- **웹훅 URL:** [REST 엔드포인트 URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) 뒤에 `canvas/trigger/send` 을 입력합니다. 예를 들어 US-06 인스턴스의 경우 URL은 `https://rest.iad-06.braze.com/canvas/trigger/send`입니다.
- **요청 본문:** 원시 텍스트

#### 요청 헤더 및 방법

Braze는 인증을 위해 API 키가 포함된 HTTP 헤더와 `content-type`을 선언하는 헤더가 필요합니다.

- **요청 헤더:**
  - **권한 부여:** Bearer `YOUR_API_KEY`
  - **Content-Type:** application/json
- **HTTP 메서드:** POST

`YOUR_API_KEY`를 `canvas.trigger.send` 권한이 있는 Braze API 키로 바꿉니다. Braze 대시보드의 **설정** > **API 키**에서 API 키를 생성할 수 있습니다.

![웹훅의 요청 헤더.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### 요청 본문

텍스트 필드에 `canvas/trigger/send` 요청을 추가합니다. 자세한 내용은 [API 트리거 배달을 통해 캔버스 메시지 보내기를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 참조하세요. 다음은 이 엔드포인트의 요청 본문 예시이며, `your_canvas_id`는 두 번째 캔버스의 캔버스 ID입니다: 

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

## 알아두어야 할 사항

- Braze 대 Braze 웹훅에는 엔드포인트 [사용량 제한]({{site.baseurl}}/api/api_limits/)이 적용됩니다.
- 고객 프로필을 업데이트하면 추가 [데이터 포인트]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count)가 발생하지만 메시징 엔드포인트를 통해 다른 메시지를 트리거하는 것은 그렇지 않습니다.
- [익명 사용자]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)를 타겟팅하려면 웹훅의 요청 본문에 `external_id` 대신 `braze_id`를 사용하면 됩니다.
- Braze-to-Braze 웹훅을 [템플릿으로]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) 저장하여 다시 사용할 수 있습니다.
- You can check the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) to view and troubleshoot webhook failures.


