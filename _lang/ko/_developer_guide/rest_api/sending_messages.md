---
nav_title: 메시지를 보내다
article_title: REST API를 사용한 메시지 전송
page_order: 1
page_type: reference
description: "이 참조 문서는 Braze REST API를 사용하여 프로그래밍 방식으로 메시지를 전송하는 두 가지 방법을 다룹니다."
---

# REST API를 사용한 메시지 전송

> 두 가지 다른 Braze 엔드포인트를 사용하여 백엔드에서 실시간으로 메시지를 보낼 수 있습니다. 각각 요청 형식이 다릅니다: 하나는 요청에 전체 메시지 내용을 포함해야 하며, 다른 하나는 캠페인 ID를 요구하고 대시보드에서 정의된 내용을 전송합니다.

이 접근 방식은 API가 지원하는 모든 메시징 채널(WhatsApp, 이메일, SMS, 푸시 알림, 콘텐츠 카드, 웹훅 등)에서 작동합니다.

## 보내는 두 가지 방법

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **Campaign ID** | 선택 사항입니다. 대시보드 캠페인 추적 없이 발송하려면 생략하거나, 대시보드에서 추적하려면 각 메시지에 API 캠페인`message_variation_id` ID와 함께  를 제공하십시오. | 필수. |
| **메시지 내용** | 요청에 객체를`messages` 포함해야 합니다(예: `messages.whats_app`, `messages.email`). | 수락되지 않음. 메시지 내용은 Braze 대시보드의 캠페인에서 정의됩니다. |
| **Use case** | API 요청에 완전히 명시된 내용으로 메시지를 전송하십시오. | API를 통해 사전 구축된 캠페인(대시보드 내 콘텐츠)을 특정 수신자에게 트리거합니다. |

전체 요청 및 응답 세부 정보는 [즉시 메시지 보내기(API 전용)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 및 [API 트리거된 전달을 사용한 캠페인 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 엔드포인트 참조 문서를 참조하십시오.

---

## Option 1: 요청에 메시지 내용을 포함하여 전송(`/messages/send`)

API 요청에서 전체 메시지 내용을 지정하려는 경우 이 엔드포인트를 사용하십시오. 반드시 객체(예: `messages.whats_app`, `messages.email``messages`, 또는 `messages.sms`)를 포함해야 **합니다**. 캠페인 추적 없이 발송하려면`campaign_id` 생략하거나, 대시보드에서 발송 내역을 추적하려면 각 메시지에 API `message_variation_id`캠페인 ID와 를 포함하세요(자세한 내용은 [엔드포인트 참조]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 문서 참조).

**필요 사항:** 해당`messages.send`권한을 가진 API 키.

{% alert important %}
수신자 목록에 포함된 각 수신자는 `external_user_ids`Braze에 이미 존재해야 합니다. 사용자를 전송의 일부로 생성하려면 먼저  [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하거나, 대신 [옵션 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend)(API 트리거 캠페인)[를](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) 사용하십시오.
{% endalert %}

### 예시: WhatsApp 템플릿 메시지

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

전체 WhatsApp 객체 사양은 [WhatsApp 객체를]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/) 참조하십시오.

{% alert note %}
이`/messages/send`엔드포인트는 TEXT 또는 IMAGE 헤더가 포함된 WhatsApp 템플릿만 지원합니다. 문서, 동영상 또는 기타 미디어 헤더 유형의 경우 [API 트리거 캠페인 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) 또는 Braze 대시보드를 대신 사용하십시오.
{% endalert %}

### 예시: Email

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

다른 채널에 대해서는 [메시징 객체를]({{site.baseurl}}/api/objects_filters/#messaging-objects) 참조하십시오.

---

## Option 2: 대시보드에서 콘텐츠로 캠페인을 트리거하세요 (`/campaigns/trigger/send`)

Braze 대시보드에서 메시지 콘텐츠가 구축된 경우(API 트리거 캠페인) 이 엔드포인트를 사용하십시오. **필수**`campaign_id`항목과 수신자를 전송합니다; 객체는`messages` 전송하지 않습니다.

**필요 사항:** 해당`campaigns.trigger.send`권한을 가진 API 키.

### 1단계: API로 트리거되는 캠페인 생성

1. Braze 대시보드에서 **메시징** > **캠페인**으로 이동하세요.
2. **캠페인 생성을** 선택한 후, **API 트리거 캠페인**(API 캠페인이 아님)을 선택하십시오.
3. 메시지 채널(WhatsApp, 이메일, SMS 등)을 추가하고 대시보드에서 메시지 내용을 구축하세요.
4. **캠페인 ID**를 기록하십시오(여러 메시지 배리언트를 사용하는 경우 **전송 ID도** 포함). 이것들은 API 요청에서 사용하게 될 것입니다.

API 트리거 캠페인을 구축하는 방법에 대한 자세한 내용은 [API 트리거 전달을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 참조하십시오.

### 2단계: API를 통해 캠페인을 트리거합니다

POST 요청을  로`/campaigns/trigger/send`  와`recipients`  (또는 `broadcast`/`audience`)와`campaign_id`함께 전송하십시오. 객체를`messages` 포함하지 마십시오—콘텐츠는 캠페인에서 제공됩니다.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

전체 요청 본문( , `send_to_existing_only`, `attributes`,`trigger_properties` 등 포함)은 [API 트리거 전달을 사용한 캠페인 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body) 엔드포인트 참조 문서를 참조하십시오.

---

## 통합을 확인하세요

1. 위의 옵션 중 하나를 사용하여 요청을 보내되, 수신자로 본인 ID를 지정하십시오.
2. 메시지가 전달되었는지 확인하십시오.
3. 옵션 2를 사용하는 경우, Braze 대시보드에서 캠페인을 확인하여 발송이 기록되었는지 확인하십시오.

## 고려 사항

- 지원되는 환경에서 Braze [개인화 기능을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) 활용하여 콘텐츠를 맞춤 설정하세요.
- 관련 규정을 준수하고 필수적인 수신 거부 옵션 및 개인정보 처리방침을 포함하도록 메시징을 구성하십시오.
- 추가 엔드포인트(스케줄링, 캔버스 트리거 등)에 대해서는 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/) 참조하십시오.
