---
nav_title: Zendesk
article_title: Zendesk 채팅
description: "Zendesk Chat과 Braze를 연동하고 양방향 SMS 대화를 설정하는 방법에 대해 알아보세요."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk 채팅

> [Zendesk Chat은](https://www.zendesk.com/service/messaging/) 각 플랫폼의 웹훅을 사용하여 양방향 SMS 대화를 설정합니다. 사용자가 지원을 요청하면 Zendesk에 티켓이 만들어집니다. 상담원 응답은 API 트리거 SMS 캠페인을 통해 Braze로 전달되고, 사용자 답장은 다시 Zendesk로 전송됩니다.

## 필수 조건


| 전제 조건 | 설명 |
|---|---|
| Zendesk 계정 | 이 파트너십을 이용하려면 Zendesk 계정이 필요합니다.|
| Zendesk 기본 인증 토큰 | Zendesk 기본 인증 토큰은 Braze에서 Zendesk로 아웃바운드 웹훅 요청을 하는 데 사용됩니다.|
| Braze REST API 키  | `campaigns.trigger.send` 권한이 있는 Braze REST API 키. 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다.|

## 사용 사례

Braze SMS 기능과 Zendesk 실시간 상담원 응답을 결합하여 사용자 문의를 인적 지원으로 신속하게 처리함으로써 고객 지원의 효율성을 향상하세요.

## Zendesk Chat 통합하기

### 1단계: Zendesk에서 웹훅 만들기

1. Zendesk 개발자 콘솔에서 웹훅으로 이동합니다: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. **웹훅 만들기에서** **트리거 또는 자동화를** 선택합니다.
3. **엔드포인트 URL의** 경우 **/campaign/trigger/send** 엔드포인트를 추가합니다.
4. **인증에서** 무기명 **토큰을** 선택하고 `campaigns.trigger.send` 권한이 있는 Braze REST API 키를 추가합니다.

![Zendesk 웹훅 예제입니다.][1]{: style="max-width:70%;"}

### 2단계: 아웃바운드 SMS 캠페인 만들기

다음으로 Zendesk의 웹훅을 수신하여 고객에게 사용자 지정 SMS 응답을 보내는 SMS 캠페인을 만들 수 있습니다.

#### 2.1 단계: 메시지 작성

Zendesk가 API를 통해 메시지 콘텐츠를 보낼 때 다음과 같은 형식으로 제공됩니다:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

따라서 이 문자열에서 원하는 세부 정보를 추출하여 메시지에 표시해야 하며, 그렇지 않으면 사용자에게 모든 세부 정보가 표시됩니다.

![서식을 지정하지 않은 SMS 예시입니다.][2]{: style="max-width:40%;"}

**메시지** 텍스트 상자에 다음 Liquid 코드와 옵트아웃 언어 또는 기타 정적 콘텐츠를 추가합니다:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![서식이 포함된 SMS 예시입니다.][3]{: style="max-width:70%;"}

#### 2.2 단계: 배송 예약하기

배달 유형으로 **API 트리거 배달을** 선택한 다음 다음 단계에서 사용할 캠페인 ID를 복사합니다.

![API 트리거 배달][4]{: style="max-width:70%;"}

마지막으로 **배달 관리에서** 다시 자격을 설정합니다.

!["배송 관리"에서 재자격이 활성화됩니다.][5]

### 3단계: Zendesk에서 트리거를 만들어 상담원 답장을 Braze로 전달하기

**개체 및 규칙** > **비즈니스 규칙** > **트리거로** 이동합니다.

1. 새 **카테고리를** 만듭니다(예: **메시지 트리거**).
2. 새 **트리거를** 만듭니다(예: **SMS Braze를 통해 응답하기**).
3. **조건에서** 선택합니다:
- 티켓 **> 댓글이** **있음 및 요청자가 댓글을 볼 수** 있도록 티켓 업데이트에 새 공개 댓글이 포함될 때마다 메시지가 트리거되도록 설정합니다.
- **티켓>업데이트는** **웹 서비스(API)** *가 아니므로* 사용자가 Braze에서 메시지를 보내면 휴대폰으로 다시 전달되지 않습니다. Zendesk에서 오는 메시지만 전달됩니다.

![SMS Braze를 통해 응답하세요.][6]{: style="max-width:70%;"}

**작업에서** **웹훅으로 알림을** 선택하고 1단계에서 만든 엔드포인트를 선택합니다. 다음으로 API 호출의 본문을 지정합니다. [2.2단계의](#step-22-schedule-the-delivery) `campaign_id` 을 요청 본문에 입력합니다.

![SMS Braze JSON 본문을 통해 응답합니다.][7]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### 4단계: 티켓이 종료되면 사용자를 업데이트하도록 Zendesk에서 트리거 만들기

사용자에게 티켓이 종료되었음을 알리려면 Braze에서 템플릿 응답 본문으로 새 캠페인을 만드세요.

![티켓이 종료되면 사용자를 업데이트합니다.][8]{: style="max-width:70%;"}

**API 트리거 전송을** 선택하고 캠페인 ID를 복사합니다.

다음으로 티켓이 마감되면 Braze에 알려주는 트리거를 설정합니다:
- 카테고리: **메시지 트리거**
- 조건에서 **티켓>티켓 상태를** 선택하고 **해결됨으로** 변경합니다.

![Zendesk에서 해결된 티켓을 설정합니다.][9]{: style="max-width:70%;"}

**작업에서** **웹훅으로 알림을** 선택하고 방금 만든 두 번째 엔드포인트를 선택합니다. 거기에서 API 호출의 본문을 지정해야 합니다:

![해결된 티켓 JSON 본문.][10]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### 5단계: Zendesk에서 사용자 지정 사용자 필드 추가하기

관리 센터의 사이드바에서 **사람을** 선택한 다음 **구성** > **사용자 필드를** 선택합니다. 사용자 지정 사용자 필드 추가 `braze_external_id`.

### 6단계: 인바운드-SMS 전달 설정

다음으로 Braze에서 두 개의 새 웹훅 캠페인을 만들어 고객의 인바운드 SMS를 Zendesk 받은 편지함으로 전달할 수 있도록 합니다.

| 캠페인           | 목적                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| 웹훅 캠페인 1 | Zendesk에서 새 티켓을 만듭니다.                                                     |
| 웹훅 캠페인 2 | 고객으로부터 인바운드로 전송된 모든 대화형 SMS 응답을 Zendesk로 전달합니다. |
{: .reset-td-br-1 .reset-td-br-2 }

#### 6.1단계: SMS 키워드 카테고리 만들기

Braze 대시보드에서 **오디언스**로 이동하고 **SMS 구독 그룹**을 선택한 다음, **커스텀 키워드 추가**를 선택합니다. 다음 필드를 작성하여 Zendesk의 전용 SMS 키워드 카테고리를 만드세요.

| 필드            | 설명                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| 키워드 카테고리 | 키워드 카테고리의 이름(예: `ZendeskSMS1`).                                                                 |
| 키워드         | 사용자 지정 키워드(예: `SUPPORT`.                                                                                  |
| 회신 메시지    | 키워드가 감지되면 "고객 서비스 담당자가 곧 연락을 드릴 것입니다."와 같은 메시지가 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 }

![Braze의 SMS 키워드 카테고리 예시.][11]{: style="max-width:70%;"}

#### 6.2단계: 첫 번째 웹훅 캠페인 만들기

Braze 대시보드에서 첫 번째 웹훅 캠페인을 생성합니다. 이 메시지는 지원이 요청되고 있음을 Zendesk에 알립니다.

웹훅 작성기에서 다음 필드를 입력합니다:
- 웹훅 URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP 메서드: POST
- 요청 헤더:
- 콘텐츠 유형: 애플리케이션/json
- 권한 부여:  기본 {{Token}}
- 요청 본문: 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![두 개의 필수 헤더가 포함된 요청 예시입니다.][12]{: style="max-width:70%;"}


#### 6.3단계: 첫 번째 배송 예약하기

**예약 전달**의 경우 **실행 기반 전달**을 선택한 다음, 트리거 유형으로 **SMS 인바운드 메시지 전송**을 선택합니다. 또한 이전에 설정한 SMS 수신 그룹 및 키워드 카테고리를 추가합니다.

![첫 번째 웹훅 캠페인의 '전송 예약' 페이지입니다.][13]

**배달 관리에서** 다시 자격을 설정합니다.

![첫 번째 웹훅 캠페인의 '전달 제어'에서 재자격이 선택되었습니다.][14]

#### 6.4단계: 두 번째 웹훅 캠페인 만들기

웹훅 캠페인을 설정하여 사용자의 남은 SMS 메시지를 Zendesk로 전달합니다:

Zendesk는 티켓 ID를 문자열로 보내므로 콘텐츠 블록을 만들어 문자열을 정수로 변환하여 Zendesk의 웹훅에서 사용할 수 있도록 합니다.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

웹훅 컴포저에서
- 웹훅 URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- 요청: PUT
- KVP:
    - 콘텐츠 유형:application/JSON
    - 권한 부여: 기본 {{Token}}

샘플 본문: 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### 6.5단계: 두 번째 웹훅 캠페인 설정 완료
- '기타' 카테고리에서 인바운드 메시지를 보내는 사용자에 대한 작업 기반 트리거를 설정합니다.
- 재자격 기준을 설정합니다.
- 적용 가능한 대상을 추가합니다(이 경우 사용자 지정 속성 **zendesk_ticket_open이** **참입니다**).

[1]: {% image_buster /assets/img/zendesk/instant_chat/chat1.png %}
[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
[3]: {% image_buster /assets/img/zendesk/instant_chat/chat3.png %}
[4]: {% image_buster /assets/img/zendesk/instant_chat/chat4.png %}
[5]: {% image_buster /assets/img/zendesk/instant_chat/chat5.png %}
[6]: {% image_buster /assets/img/zendesk/instant_chat/chat6.png %}
[7]: {% image_buster /assets/img/zendesk/instant_chat/chat7.png %}
[8]: {% image_buster /assets/img/zendesk/instant_chat/chat8.png %}
[9]: {% image_buster /assets/img/zendesk/instant_chat/chat9.png %}
[10]: {% image_buster /assets/img/zendesk/instant_chat/chat10.png %}
[11]: {% image_buster /assets/img/zendesk/instant_chat/chat11.png %}
[12]: {% image_buster /assets/img/zendesk/instant_chat/chat12.png %}
[13]: {% image_buster /assets/img/zendesk/instant_chat/chat13.png %}
[14]: {% image_buster /assets/img/zendesk/instant_chat/chat14.png %}
