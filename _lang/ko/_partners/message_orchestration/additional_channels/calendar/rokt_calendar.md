---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar
description: "이 참고 문서에서는 브랜드가 캘린더 이벤트 및 알림의 형태로 1:1 이벤트와 프로모션 커뮤니케이션을 푸시할 수 있는 동적 캘린더 마케팅 기술인 Braze와 Rokt Calendar의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

layout: redirect
redirect_to: /docs/partners/home
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/)는 동적 캘린더 마케팅 기술입니다. 이를 통해 브랜드는 이벤트와 홍보성 커뮤니케이션을 캘린더 이벤트와 알림 형태로 보낼 수 있습니다.

_This integration is maintained by Rokt Calendar._

## 통합 정보

Braze와 Rokt 캘린더 통합을 통해 Rokt 캘린더 구독자 및 해당 데이터를 Braze 웹훅을 통해 Braze로 푸시할 수 있습니다. 그런 다음, Braze 캔버스에서 다음 커스텀 [Rokt Calendar 속성](#audience-segmentation)을 사용하여 타겟팅 및 오디언스 세분화 여정에 이 데이터를 사용할 수 있습니다. 

## 필수 조건

| 요구 사항  | 설명 |
| ------------ | ----------- |
| Rokt 캘린더 계정 | 이 파트너십을 이용하려면 고객별 Rokt 캘린더 계정이 필요합니다. 계정 관리자와 상담하려면 [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) 에 문의하세요.  |
| Rokt 캘린더 설정 | Rokt 캘린더 계정 관리자가 고객님과 협력하여 다음과 같은 설정을 포함하여 고객의 필요에 가장 적합한 캘린더를 설정해 드립니다:<br>\- 플래그 병합<br>\- 구독자ID 폴백 플래그<br>\- 필요한 경우 이메일 캡처 |
| Rokt 캘린더 OAuth 자격 증명 | Rokt 캘린더 계정 관리자가 제공한 이 키를 사용하면 Braze와 Rokt 캘린더 계정을 연결할 수 있습니다.<br><br>Braze 대시보드의 **설정** > **연결된 콘텐츠**에서 생성할 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. 이 키를 Rokt 캘린더 계정 관리자에게 제공해야 합니다.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| [Braze REST 엔드포인트]({{site.baseurl}}/api/basics/#endpoints) | REST 엔드포인트 URL. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| 외부 구독자 ID | Rokt 캘린더 구독 프로세스에서 캘린더 구독자와 Braze 사용자를 일치시키기 위해 사용하는 식별자입니다. 이 정보는 Rokt 캘린더에 전달합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 오디언스 세분화 {#audience-segmentation}

Rokt Calendar가 새 사용자를 생성하거나 기존 가입자를 Braze 사용자와 매칭하면, Rokt Calendar는 Braze 내에서 필터링할 수 있는 다음 커스텀 가입 속성을 전송합니다.

| 커스텀 속성  | 정의       | 예시          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Rokt 캘린더 계정의 코드 | `brazetest/f5733866ade2` 및 `brazetest/ff10919f1078` |
| `rokt:account_id` |Rokt 캘린더 계정의 ID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Rokt 캘린더 계정 이름 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Rokt Calendar 캘린더 코드 | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | Rokt Calendar 캘린더 ID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Rokt Calendar 캘린더 제목 | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 생성된 구독과 관련된 국가 코드 | `AU/f5733866ade2` |
| `rokt:device_name` | 생성된 구독과 관련된 디바이스 유형 | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 생성된 가입과 관련된 출생 국가 | `Australia/f5733866ade2` |
| `rokt:optIn1` | 사용자가 생성된 구독과 관련된 두 가지 옵트인 중 첫 번째 옵트인에 동의한 경우 | `True/f5733866ade2` |
| `rokt:optIn2` | 사용자가 생성한 구독과 관련된 2개의 옵트인 중 두 번째 옵트인에 동의한 경우 | `True/f5733866ade2` |
| `rokt:source` | 생성된 구독의 소스 | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | 구독 과정에서 사용자가 입력한 이메일 주소 | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 생성된 가입과 관련된 고유 식별자 역할을 하는 가입 ID | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 생성된 가입과 관련된 가입 방법(webcal/Google). | `WebCal/f5733866ade2` |
| `rokt:tags` | 생성된 구독과 관련하여 사용된 캘린더 태그입니다. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

또한 사용자가 Rokt Calendar에 가입하는 즉시 `subscribe` 커스텀 이벤트가 트리거됩니다. 이 이벤트는 Braze 세분화에서 사용하거나 캠페인 또는 캔버스 구성요소의 트리거로 사용할 수 있습니다.

## 통합

### 1단계: 캘린더 구독자 대상 구축

캔버스에서 캘린더 이벤트를 보내려면 먼저 사용자가 이미 가입한 Rokt Calendar가 설정되어 있어야 합니다. 이렇게 하려면 사용자에게 캘린더를 구독할 수 있는 위치와 방법을 알려야 합니다. Rokt Calendar에서는 다음을 권장합니다.

#### 구독 통합 포인트 제공
캘린더 가입자 오디언스를 구축하려면 사용자가 탐색하여 가입할 수 있는 대상을 제공해야 합니다. 몇 가지 구독 통합 포인트의 예는 다음과 같습니다:
  - 웹사이트에 캘린더 버튼 추가
  - 이메일 또는 SMS에 캘린더 링크 추가하기 
  - 앱에 캘린더 버튼 추가
  - 소셜 미디어에 캘린더 링크 추가

#### 캘린더 홍보
가입자 오디언스를 구축하려면 가입자가 가입 방법을 알 수 있도록 오디언스에게 캘린더를 홍보해야 합니다. 캘린더 프로모션의 예는 다음과 같습니다:
  - 소셜 미디어의 개시물
  - 이메일 뉴스레터 및 업데이트
  - 블로그 게시물
  - 인앱 알림

### 2단계: Braze에서 Rokt 캘린더 웹훅 만들기

Braze 내에서 웹훅 캠페인 또는 캔버스 내 웹훅을 설정하여 다음을 수행할 수 있습니다.

- 새로운 개인화된 이벤트를 전송합니다. 구독자의 캘린더 세그먼트에 새 이벤트를 추가할 수 있도록 허용합니다.
- 개인화된 이벤트를 업데이트합니다: 구독자의 캘린더에 있는 기존 이벤트를 업데이트할 수 있도록 허용합니다.

향후 캠페인이나 캔버스에서 사용할 Rokt 캘린더 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하세요. 

일회성 로크트 캘린더 웹훅 캠페인을 만들거나 기존 템플릿을 사용하려면 새 캠페인을 만들 때 Braze에서 **웹훅을** 선택하세요.

{% tabs %}
{% tab 새 이벤트 보내기 %}
Rokt 캘린더 웹훅 템플릿을 선택하면 다음과 같은 내용이 표시됩니다:
- **웹훅 URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **요청 본문**: 원시 텍스트
{% endtab %}
{% tab 기존 이벤트 업데이트 %}
Rokt 캘린더 웹훅 템플릿을 선택하면 다음과 같은 내용이 표시됩니다:
- **웹훅 URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **요청 본문**: 원시 텍스트
{% endtab %}
{% endtabs %}

#### 요청 헤더 및 메서드

Rokt Calendar에서는 권한 부여를 위해 `HTTP Header`에 Rokt Calendar 연결된 콘텐츠 자격 증명 이름이 포함되어야 합니다. 다음은 이미 템플릿에 키-값 쌍으로 포함되어 있지만 **설정** 탭에서 `<Rokt-Calendar-API>` 을 `Manage Settings > Connected Content > Credential` 에 있는 자격 증명 이름으로 바꿔야 합니다.

{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

{% tabs local %}
{% tab 새 이벤트 보내기 %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab 기존 이벤트 업데이트 %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab 이벤트 세부 정보 %}
다음 필드에는 이벤트 수준에서 사용자 지정할 수 있는 정보가 포함되어 있습니다.

| 필드             | 정의       | 예시          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>**\*필수** | 추가하거나 업데이트할 이벤트의 고유 식별자 | `Event_00001`
| `eventTitle` <br>**\*필수** | 캘린더에 표시되는 이벤트의 제목입니다. | 2019 여름 세일
| `eventDescr` | 캘린더에 표시되는 이벤트에 대한 설명 | 세일은 3일간 진행되며, 이 링크( `www.mybusiness.com/sale` )를 클릭하여 혜택을 확인하세요. |
| `eventLocation` | 캘린더에 표시되는 이벤트의 위치. eventTitle을 보완하는 두 번째 클릭 유도 문안으로 종종 사용됩니다. | 이벤트를 열고 50% 할인 받기 |
| `eventStart` <br>**\*필수**  | 캘린더에 표시되는 이벤트의 시작 날짜 및 시간 | `2019-02-21T15:00:00` |
| `eventEnd` <br>**\*필수**  | 캘린더에 표시되는 이벤트의 시작 날짜 및 시간 | `2019-02-21T16:00:00` |
| `eventTz` <br>**\*필수**  | 캘린더에 표시되는 이벤트의 시간대. 해당 시간대 목록은 [여기](https://roktcalendar-api.readme.io/docs/timezones)에서 확인할 수 있습니다. | `Eastern Standard Time` |
| `notifyBefore` <br>**\*필수**  | 캘린더에 표시되는 이벤트의 알림 시간(분 단위) | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
유효한 표준 시간대 목록은 [https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezones를 참조하세요.
{% endalert %}

### 3단계: 요청 미리보기

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 사용자 지정하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

