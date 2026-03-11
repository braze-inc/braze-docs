---
nav_title: WhatsApp 및 외부 시스템
article_title: Braze 및 WhatsApp을 외부 시스템과 통합합니다
page_order: 2
description: "이 참조 문서는 Braze 및 WhatsApp 통합을 외부 AI 또는 커뮤니케이션 시스템과 통합하는 단계별 가이드를 제공합니다."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# 외부 AI 또는 커뮤니케이션 시스템과 Braze 및 WhatsApp을 통합하세요

> WhatsApp 채널에서 AI 챗봇과 실시간 상담원 연결 기능을 활용하여 고객 지원 운영을 효율화하세요. 일상적인 문의 사항을 자동화하고 필요 시 원활하게 상담원으로 전환함으로써 응답 시간을 크게 단축하고 전반적인 고객 경험을 향상시킬 수 있습니다.

## 작동 방식

Braze와 외부 AI 또는 커뮤니케이션 시스템 간의 통합은 양방향으로 작동합니다. 여기서 Braze는 커뮤니케이션 채널 역할을 하고, 외부 시스템은 메시지를 처리하고 응답을 구성하는 '지능' 역할을 합니다.

통합 워크플로는 두 가지 주요 흐름으로 나눌 수 있습니다:
**인바운드 흐름:** 사용자의 메시지가 Braze에 도착한 후, 처리하기 위해 귀사의 외부 시스템으로 전달됩니다.
**아웃바운드 흐름:** 메시지 처리 후, 외부 시스템이 Braze에 응답을 전송하면 Braze가 해당 메시지를 최종 사용자에게 전달합니다.

이 통신을 효율적으로 자동화하기 위해, 이 통합은 두 가지 핵심 Braze 기능을 사용합니다: [웹훅 캠페]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)인과 [API 트리거 캠페인입니다]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Braze WhatsApp 채널과 외부 시스템 간 통합 아키텍처]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Braze WhatsApp 채널과 외부 시스템 간 통합 아키텍처*</sup>

## 필수 조건

| Prerequisite | 설명 |
| - | - |
| 외부 시스템 | API를 활용하여 챗봇 및 자동화된 고객 서비스 시스템을 구축하고 관리할 수 있는, 또는 둘 다 가능한 제3자 AI 또는 커뮤니케이션 시스템. |
| Braze와 WhatsApp 통합 | Braze에서 관리하는 WhatsApp 번호 |
| Braze REST API 키 | 권한이 `campaigns.trigger.send`부여된 REST API 키. Braze 대시보드에서 **설정** > **API **키로 이동하여 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## 통합 구성하기

### 1단계: 수신 메시지를 위한 웹훅 캠페인 생성

먼저, Braze에서 수신한 WhatsApp 메시지를 외부 시스템으로 전송할 수 있는 방법을 설정하기 위해 웹훅 캠페인을 생성하십시오.

1. Braze에서 웹훅 캠페인을 생성하세요.
2. 웹훅 작성기에서 **'웹훅 작성'을** 선택하세요.
3. **웹훅 URL** 필드에 메시지를 수신할 외부 시스템의 API 엔드포인트(URL)를 입력하십시오.
4. 요청 본문에 **'원시 텍스트'를** 선택하고, 사용자의`external_id`이름과 전화번호, 메시지 내용 및 기타 관련 정보(예: 개인화된 메시지)를 포함합니다.

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
5\. 캠페인 컴포저의 **'배달 일정** 설정' 단계에서 배달 유형으로 **'실행 기반** 전달'을 선택하고 캠페인 트리거로 **'WhatsApp 인바운드 메시지 전송'을 선택하세요**.

![WhatsApp 수신 메시지 전송을 트리거로 하는 실행 기반 전달]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. 캠페인 작성을 완료한 후 저장하고 캠페인을 시작하세요. 캠페인을 시작한 후, 메시지가 수신될 때마다 Braze는 외부 시스템으로 웹훅을 전송합니다.

### 2단계: API 트리거형 아웃바운드 메시지 캠페인을 생성합니다 {#step-2}

다음으로, 외부 시스템이 WhatsApp을 통해 사용자에게 메시지를 다시 전송할 수 있는 방법을 마련하기 위해 API 트리거 캠페인을 생성하십시오.

1. Braze에서 WhatsApp 캠페인을 생성하세요. 
2. 메시지 작성기에서 **WhatsApp 템플릿 메시지** 또는 **응답 메시지를** 선택한 후, 템플릿 또는 응답 메시지 레이아웃을 선택하세요. 수신 메시지가 24시간 WhatsApp 창을 열었기 때문에 어떤 응답 메시지 레이아웃이든 선택할 수 있습니다.

![메시지 유형 및 메시지 레이아웃을 선택할 수 있는 옵션이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. 메시지 본문에 API 트리거 속성을 추가합니다. 예를 들어 {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. 이를 통해 AI 시스템이 전송될 메시지를 채울 수 있습니다.

![메시지 본문에 트리거 속성이 포함된 메시지 작성기.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. 캠페인 작성기의 **'전달 일정** 설정' 단계에서 전달 유형으로 **'실행 기반** 전달'을 선택하세요.
5\. 캠페인을 저장한 후, Braze가 이 캠페인에`campaign_id` 대해 생성한 고유 ID를 기록해 두십시오. 다음 단계를 진행하려면 ID가 필요합니다.

### 3단계: 외부 시스템을 API 트리거 캠페인에 연결하십시오

마지막으로, 외부 시스템을 구성하여 Braze를 호출하고 응답을 전송하도록 설정하십시오.

1. 외부 시스템의 코드에서 수신된 메시지를 처리하고 응답을 생성한 후, Braze`/messages/send`엔드포인트로 POST 요청을 수행하십시오.
2. 요청 `/messages/send`본문에 [2단계에서 ](#step-2)`campaign_id`생성된 인증 토큰, 사용자의 ID`external_id`, 그리고 외부 시스템의 응답 내용을 포함하십시오.
3. [2](#step-2)단계의 API 트리거 속성을 사용하여 외부 시스템의 응답을 삽입하고, 인증을 위해 요청 헤더에 API 키를 포함하는 것을 잊지 마십시오. 예를 들어 다음과 같은 cURL 예시와 같이:

{% raw %}
```bash
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

이제 AI 챗봇 워크플로를 구축할 수 있는 탄탄한 기반을 마련하셨습니다!

### 커스텀 워크플로우 맞춤 설정

통합 로직을 다음과 같이 확장할 수 있습니다:
- 서로 다른 키워드를 사용하여 별개의 웹훅 캠페인을 트리거하세요.
- 다단계 API 트리거 캠페인을 통해 더 복잡한 전환 흐름을 생성하세요.
- Braze에서 채팅 정보를 커스텀 속성으로 기록하여 고객 프로필을 풍부하게 하고 향후 캠페인을 세그먼트하세요.
