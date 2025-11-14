---
nav_title: WhatsApp 및 외부 시스템
article_title: 외부 시스템과 Braze 및 WhatsApp 통합하기
page_order: 2
description: "이 참조 문서에서는 외부 AI 또는 커뮤니케이션 시스템과 Braze 및 WhatsApp 통합을 위한 단계별 가이드를 제공합니다."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# 외부 AI 또는 커뮤니케이션 시스템과 Braze 및 WhatsApp 통합하기

> WhatsApp 채널에서 AI 챗봇과 실시간 상담원 핸드오프의 강력한 기능을 활용하여 고객 지원 운영을 간소화하세요. 일상적인 문의를 자동화하고 필요 시 상담원에게 원활하게 전환함으로써 응답 시간을 크게 개선하고 전반적인 고객 경험을 향상시킬 수 있습니다.

## 작동 방식

Braze와 외부 AI 또는 커뮤니케이션 시스템 간의 통합은 양방향으로 작동하며, Braze는 커뮤니케이션 채널, 외부 시스템은 메시지를 처리하고 응답을 공식화하는 '인텔리전스'로서 역할을 합니다.

통합 워크플로우는 두 가지 주요 흐름으로 나눌 수 있습니다:
**인바운드 흐름:** 사용자의 메시징이 Braze에 도착하면 처리를 위해 외부 시스템으로 전달됩니다.
**아웃바운드 흐름:** 메시지를 처리한 후 외부 시스템이 Braze에 응답을 보내면 최종 사용자에게 메시지가 전달됩니다.

이러한 커뮤니케이션을 효율적으로 자동화하기 위해 이 통합에서는 [웹훅 캠페인과]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) [API 트리거 캠페인이라는]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 두 가지 주요 Braze 기능을 사용합니다.

!!\![Braze WhatsApp 채널과 외부 시스템 간의 통합 아키텍처.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Braze WhatsApp 채널과 외부 시스템 간의 통합 아키텍처.*</sup>

## 전제 조건

| 전제 조건 | 설명 |
| - | - |
| 외부 시스템 | 챗봇을 구축 및 관리할 수 있는 타사 AI 또는 커뮤니케이션 시스템, API를 사용하는 자동화된 클라이언트 서비스 시스템 또는 둘 다. |
| 브라즈와 왓츠앱 통합 | 브라즈가 관리하는 왓츠앱 번호 | 매니저가 관리하는 왓츠앱 번호
| Braze REST API 키 | `campaigns.trigger.send` 권한이 있는 REST API 키입니다. **설정** > **API 키로** 이동하여 Braze 대시보드에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 통합 구성하기

### 1단계: 인바운드 메시지를 위한 웹훅 캠페인 만들기

먼저, 웹훅 캠페인을 생성하여 Braze에서 수신한 WhatsApp 메시지를 외부 시스템으로 보내는 방법을 설정합니다.

1. Braze에서 웹훅 캠페인을 만듭니다.
2. 웹훅 작성기에서 **웹훅 작성을** 선택합니다.
3. **웹훅 URL** 필드에 메시지를 수신할 외부 시스템의 API 엔드포인트(URL)를 입력합니다.
4. 요청 본문으로 **원시 텍스트를** 선택하고 사용자의 `external_id` 및 전화번호, 메시지 내용, 기타 관련 정보 등이 포함된 개인화된 페이로드를 입력합니다:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5\. 캠페인 작성기의 전달 **예약** 단계에서 전달 유형으로 **실행 기반** 전달을 선택하고 캠페인 트리거로 **WhatsApp 인바운드 메시지 보내기를** 선택합니다.

!!! WhatsApp 인바운드 메시지 전송을 트리거로 하는 실행 기반 전달.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. 캠페인 구성을 완료한 다음 캠페인을 저장하고 실행합니다. 이제 메시지가 수신될 때마다 Braze는 외부 시스템으로 웹훅을 보냅니다.

### 2단계: 아웃바운드 메시징을 위한 API 트리거된 캠페인 만들기 {#step-2}

다음으로, API 트리거 캠페인을 만들어 외부 시스템이 WhatsApp을 통해 사용자에게 메시지를 다시 보낼 수 있는 방법을 설정하세요.

1. Braze에서 WhatsApp 캠페인을 만듭니다. 
2. 메시지 작성기에서 **WhatsApp 템플릿 메시지** 또는 **응답 메시지** 중 하나를 선택한 다음 템플릿 또는 응답 메시지 레이아웃을 선택합니다. 인바운드 메시지가 24시간 WhatsApp 창을 열었으므로 응답 메시지 레이아웃을 선택할 수 있습니다.

메시지 유형과 메시지 레이아웃을 선택할 수 있는 옵션이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. 메시지 본문에 API 트리거 속성을 추가합니다(예: {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}). 이렇게 하면 AI 시스템이 전송할 메시지를 채울 수 있습니다.

트리거 속성이 포함된 메시지 본문이 있는 메시지 작성기입니다.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. 캠페인 작성기의 전달 **예약** 단계에서 전달 유형으로 **실행 기반** 전달을 선택합니다.
5\. 캠페인을 저장한 다음, 이 캠페인을 위해 Braze가 생성하는 고유한 `campaign_id` 을 메모해 두세요. 다음 단계를 진행하려면 ID가 필요합니다.

### 3단계: API 트리거 캠페인에 외부 시스템 연결하기

마지막으로 외부 시스템에서 Braze를 호출하고 응답을 보내도록 구성합니다.

1. 외부 시스템의 코드에서 수신된 메시지를 처리하고 응답을 생성한 후 Braze `/messages/send` 엔드포인트에 POST 요청을 합니다.
2. `/messages/send` 요청 본문에는 [2단계의](#step-2) `campaign_id`, 사용자의 `external_id`, 그리고 외부 시스템의 응답 내용을 포함합니다.
3. [2단계의](#step-2) API 트리거 속성을 사용하여 외부 시스템의 응답을 삽입하고, 이 cURL 예제에서와 같이 인증을 위해 요청 헤더에 API 키를 포함시키는 것을 잊지 마세요:

{% raw %}
```json
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

이제 AI 챗봇 워크플로우 구축을 위한 탄탄한 기반을 갖추었습니다!

### 워크플로우 커스텀하기

통합 로직을 다음과 같이 확장할 수 있습니다:
- 서로 다른 키워드를 사용하여 각기 다른 웹훅 캠페인을 트리거할 수 있습니다.
- 다단계 API 트리거 캠페인을 통해 보다 복잡한 대화 흐름을 만들 수 있습니다.
- Braze에 채팅 정보를 커스텀 속성으로 기록하여 고객 프로필을 보강하고 향후 캠페인을 세분화하세요.
