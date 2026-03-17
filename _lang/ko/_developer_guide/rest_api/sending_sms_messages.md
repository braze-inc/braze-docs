---
nav_title: SMS 메시지 전송
article_title: REST API를 사용하여 SMS 메시지 전송
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze REST API와 API 캠페인을 사용하여 SMS 메시지를 전송하는 방법을 설명합니다."
channel:
  - SMS
---

# REST API를 사용하여 SMS 메시지 전송

> Braze REST API를 사용하여 백엔드에서 실시간으로 트랜잭션 SMS 메시지를 전송합니다. 이 접근 방식은 SMS 메시지를 프로그래밍 방식으로 전송하면서 Braze 대시보드의 다른 캠페인 및 캔버스와 함께 전달 분석을 추적할 수 있는 서비스를 구축할 수 있게 해줍니다.

특히 백엔드 시스템에서 정의된 콘텐츠가 있는 대량의 트랜잭션 메시징에 유용할 수 있습니다. 예를 들어, 다른 사용자로부터 메시지를 받을 때 소비자에게 알림을 보내고 웹사이트를 방문하여 받은편지함을 확인하도록 초대할 수 있습니다.

이 접근 방식을 사용하면 다음을 수행할 수 있습니다:

- 백엔드에서 실시간으로 SMS 메시지를 트리거합니다.
- 모든 마케팅 소유 캠페인 및 캔버스와 함께 분석을 추적합니다.
- 메시지 지연, 후속 리타겟팅 및 A/B 테스트와 같은 추가 Braze 기능으로 사용 사례를 확장합니다.
- 선택적으로, [API 트리거된 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)로 전환하여 Braze 대시보드에서 메시지 템플릿을 정의하면서 여전히 백엔드에서 전송을 트리거할 수 있습니다.

REST API를 통해 SMS 메시지를 전송하려면 Braze 대시보드에서 API 캠페인을 설정한 다음 [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 엔드포인트를 사용하여 메시지를 전송해야 합니다.

## 필수 조건

이 가이드를 완료하려면 다음이 필요합니다:

| Requirement | Description |
| --- | --- |
| Braze REST API key | `messages.send` 권한이 있는 키. 하나를 만들려면 **설정** > **API 및 식별자** > **API 키**로 이동합니다. |
| SMS 구독 그룹 | Braze 작업 공간에 구성된 SMS 구독 그룹. |
| 백엔드 서비스 | Braze REST API에 HTTP POST 요청을 할 수 있는 백엔드 서비스 또는 스크립팅 환경. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: Create an API campaign

1. Braze 대시보드에서 **메시징** > **캠페인**으로 이동합니다.
2. **캠페인 만들기**을 선택한 다음 **API 캠페인**을 선택합니다.
3. "SMS 메시지 알림"과 같은 캠페인 이름과 설명을 입력합니다.
4. 식별 및 추적을 위한 관련 태그를 추가합니다.
5. **메시징 채널 추가**을 선택한 다음 **SMS**을 선택합니다.
6. 캠페인 페이지에 표시된 **캠페인 ID**와 **메시지 변형 ID**를 기록해 두십시오. API 요청을 구성할 때 두 값이 모두 필요합니다.

## 2단계: API를 사용하여 SMS 메시지를 보냅니다.

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 엔드포인트에 POST 요청을 구성합니다. 요청 페이로드에 캠페인 ID, 수신자의 외부 사용자 ID 및 SMS 내용을 포함합니다.

{% alert important %}
`external_user_ids`에 참조된 각 수신자는 Braze에 이미 존재해야 합니다. API 전용 전송은 새로운 사용자 프로필을 생성하지 않습니다. 전송의 일환으로 사용자를 생성해야 하는 경우, 먼저 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)을 사용하거나 대신 [API 트리거 캠페인]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)을 사용하십시오.
{% endalert %}

### 예시 요청

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT`을 귀하의 작업 공간에 대한 [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints)로 교체하십시오.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

자리 표시자 값을 실제 ID로 교체하십시오. `body` 필드는 [Liquid 개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 지원하므로 각 수신자에게 맞춤화된 메시지 내용을 작성할 수 있습니다. SMS 메시징 객체에서 지원하는 매개변수의 전체 목록은 [SMS 객체]({{site.baseurl}}/api/objects_filters/messaging/sms_object/)를 참조하십시오.

요청을 구성한 후, 백엔드 서비스에서 Braze REST API로 POST 요청을 보냅니다.

## 3단계: 통합을 확인하십시오.

설정을 완료한 후, 통합을 확인하십시오:

1. [2단계](#step-2-send-an-sms-message-using-the-api)에 설명된 대로 API 요청을 보내고, 수신자로 자신의 사용자 ID를 사용하세요.
2. SMS 메시지가 귀하의 전화로 전달되었는지 확인하세요.
3. Braze 대시보드에서 캠페인 결과 페이지로 이동하여 전송이 기록되었는지 확인하세요.
4. 캠페인을 확장할 때 결과를 면밀히 모니터링하세요.

## 고려 사항

- SMS 캠페인이 관련 규정 및 통신사 요구 사항을 준수하는지 확인하세요. 모든 메시지에 옵트아웃 지침(예: "옵트아웃하려면 STOP을 문자로 보내세요")을 포함하세요. 자세한 내용은 [SMS 법률 및 규정]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) 및 [옵트인 및 옵트아웃 키워드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)를 참조하세요.
- Braze [개인화 기능]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)을 사용하여 동적 콘텐츠 및 사용자 특정 데이터를 포함하여 SMS 콘텐츠를 개별 소비자에 맞게 조정하세요.
- Braze REST API는 메시지 예약, 캠페인 트리거 및 기타 작업을 위한 추가 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/)을 제공합니다.
