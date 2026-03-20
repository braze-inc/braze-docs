---
nav_title: 이메일 메시지 발송
article_title: REST API를 사용하여 이메일 메시지 발송
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Braze REST API와 API 캠페인을 사용하여 이메일 메시지를 발송하는 방법을 안내합니다."
channel:
  - email
---

# REST API를 사용하여 이메일 메시지 발송

> Braze REST API를 사용하여 백엔드에서 실시간으로 트랜잭션 이메일을 발송할 수 있습니다. 이 방식을 사용하면 프로그래밍 방식으로 이메일을 발송하는 서비스를 구축하면서, Braze 대시보드에서 다른 캠페인 및 캔버스와 함께 전달 분석을 추적할 수 있습니다.

이 방식은 콘텐츠가 백엔드 시스템에서 정의되는 트랜잭션 메시징에 특히 유용합니다. 예를 들어, 소비자가 다른 사용자로부터 메시지를 받았을 때 웹사이트를 방문하여 받은편지함을 확인하도록 알림을 보낼 수 있습니다.

이 방식을 사용하면 다음을 수행할 수 있습니다:

- 백엔드에서 실시간으로 이메일을 트리거합니다.
- 열기, 클릭 수, 반송을 포함하여 모든 마케팅 소유 캠페인 및 캔버스와 함께 분석을 추적합니다.
- 메시지 상호작용 데이터를 사용하여 후속 리타겟팅과 같은 후속 메시지를 트리거합니다.
- 메시지 지연 및 A/B 테스트와 같은 추가 Braze 기능으로 사용 사례를 확장합니다.
- 선택적으로 [API 트리거 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)로 전환하여 Braze 대시보드에서 이메일 템플릿을 정의하면서도 백엔드에서 발송을 트리거할 수 있습니다.

REST API를 통해 이메일을 발송하려면 Braze 대시보드에서 API 캠페인을 설정한 다음, [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 엔드포인트를 사용하여 메시지를 발송해야 합니다.

## 필수 조건

이 가이드를 완료하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Braze REST API 키 | `messages.send` 권한이 있는 키입니다. 키를 생성하려면 **설정** > **API 및 식별자** > **API 키**로 이동합니다. |
| Braze 앱 ID | 워크스페이스 내 앱의 식별자입니다. 확인하려면 **설정** > **API 및 식별자**로 이동하여 **앱 식별자** 섹션을 확인합니다. 이 값은 이메일 메시징 오브젝트의 `app_id` 필드에 필요합니다. 자세한 내용은 [앱 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하세요. |
| HTML 이메일 콘텐츠 | 사전에 준비된 이메일 메시지의 HTML 본문입니다. |
| 백엔드 서비스 | Braze REST API에 HTTP POST 요청을 보낼 수 있는 백엔드 서비스 또는 스크립팅 환경입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: API 캠페인 생성

1. Braze 대시보드에서 **메시징** > **캠페인**으로 이동합니다.
2. **캠페인 생성**을 선택한 다음 **API 캠페인**을 선택합니다.
3. 캠페인의 이름과 설명을 입력합니다(예: "이메일 메시지 알림").
4. 식별 및 추적을 위한 관련 태그를 추가합니다.
5. **메시징 채널 추가**를 선택한 다음 **이메일**을 선택합니다.
6. 캠페인 페이지에 표시된 **캠페인 ID**를 기록합니다. API 요청을 구성할 때 이 값이 필요합니다. 선택적으로 **메시지 변형 ID**도 기록해 두세요. 발송 통계를 특정 메시지 변형에 귀속시키려면 요청에 이 값을 포함합니다.

## 2단계: API를 사용하여 이메일 발송

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 엔드포인트에 POST 요청을 구성합니다. 요청 페이로드에 캠페인 ID, 수신자의 외부 사용자 ID, 이메일 콘텐츠를 포함합니다.

{% alert important %}
`external_user_ids`에 참조된 각 수신자는 이미 Braze에 존재해야 합니다. API 전용 발송은 새 고객 프로필을 생성하지 않습니다. 발송의 일부로 사용자를 생성해야 하는 경우 먼저 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)을 사용하거나, [API 트리거 캠페인]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)을 대신 사용하세요.
{% endalert %}

### 요청 예시

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT`를 워크스페이스의 [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints)로 교체합니다.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

플레이스홀더 값을 실제 ID로 교체합니다. `from` 필드는 `"Display Name <email@address.com>"` 형식을 사용해야 합니다. `body` 필드는 유효한 HTML을 허용하며 [Liquid 개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 지원하므로, 각 수신자에 맞게 이메일 콘텐츠를 맞춤 설정할 수 있습니다. 이메일 메시징 오브젝트에서 지원하는 전체 매개변수 목록은 [이메일 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/email_object/)를 참조하세요.

요청을 구성한 후 백엔드 서비스에서 Braze REST API로 POST 요청을 발송합니다.

## 3단계: 통합 확인

설정을 완료한 후 통합을 확인합니다:

1. [2단계](#step-2-send-an-email-using-the-api)에 설명된 대로 자신의 사용자 ID를 수신자로 사용하여 API 요청을 발송합니다.
2. 이메일이 받은편지함에 전달되었는지 확인합니다.
3. Braze 대시보드에서 캠페인 결과 페이지로 이동하여 발송이 기록되었는지 확인합니다.
4. 캠페인을 확장하면서 결과를 면밀히 모니터링합니다.

## 고려 사항

- 필요한 수신 거부 옵션과 개인정보 보호 고지를 포함하여 이메일 캠페인이 GDPR 및 CAN-SPAM과 같은 관련 규정을 준수하는지 확인합니다. 자세한 내용은 [사용자 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) 및 [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)를 참조하세요.
- Braze [개인화 기능]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)을 사용하여 동적 콘텐츠 및 사용자별 데이터를 포함하여 개별 소비자에게 맞춤화된 이메일 콘텐츠를 제공합니다.
- Braze REST API는 메시지 예약, 캠페인 트리거 등을 위한 추가 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/)를 제공합니다.