--- 
nav_title: SessionM
article_title: SessionM
description: "이 참고 문서에서는 고객 참여 및 로열티 플랫폼인 Braze와 세션엠의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# 세션엠 로열티 플랫폼

> [세션엠은](https://www.mastercardservices.com/en/capabilities/sessionm) 마케터가 타겟팅된 홍보를 통해 참여도와 수익성을 높일 수 있도록 캠페인 관리 기능과 로열티 관리 솔루션을 제공하는 고객 참여 및 충성도 플랫폼입니다.

## Prerequisites

| 소스 | 요구 사항 | 설명 |
| --- | --- | --- |
| Braze | Braze REST API 키 | `trigger_send` 권한이 있는 Braze REST API 키. 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze | Braze REST 엔드포인트 | 귀하의 REST 엔드포인트 URL. 엔드포인트는 [인스턴스의]({{site.baseurl}}/api/basics/#endpoints) Braze URL에 따라 달라집니다. |
| 브레이즈 및 세션M | 일치하는 식별자 | 통합 기능을 사용하려면 SessionM과 Braze 모두 각 플랫폼에서 사용하는 식별자에 대한 기록이 있어야 합니다. `user_id` 에 대한 참조는 SessionM에서 프로필 생성 시 생성된 SessionM의 사용자 식별자에 해당합니다. |
| SessionM | SessionM 계정 | 이 파트너십을 이용하려면 SessionM 계정이 필요합니다. |
| SessionM | SessionM 핵심 REST 엔드포인트 | 엔드포인트는 인스턴스의 SessionM URL에 따라 달라집니다. 이는 **디지털 자산의** SessionM 대시보드에서 만들 수 있습니다. |
| SessionM | SessionM 코어 REST API 키 | 인스턴스 및 Braze 통합과 연결된 SessionM API 키입니다. 이 키는 태그를 포함한 모든 코어 기반 호출에 사용할 수 있습니다. 이는 **디지털 자산의** SessionM 대시보드에서 만들 수 있습니다. |
| SessionM | SessionM 핵심 REST API 비밀 | 인스턴스 및 Braze 통합과 관련된 SessionM API 비밀입니다. 이 키는 태그를 포함한 모든 코어 기반 호출에 사용할 수 있습니다. 이는 **디지털 자산의** SessionM 대시보드에서 만들 수 있습니다. |
| SessionM | SessionM Connect REST 엔드포인트 | 엔드포인트는 인스턴스의 SessionM URL에 따라 달라집니다. 세션엠 기술 계정 관리자 또는 제공 팀에 문의해 주세요. |
| SessionM | SessionM 연결 REST 권한 부여 문자열 | 인스턴스와 연결된 SessionM Connect 기본 권한 부여 문자열입니다. 이 인증 문자열은 get_user_offers를 포함한 모든 연결 기반 호출에 사용할 수 있습니다. 세션엠 기술 계정 관리자 또는 제공 팀에 문의해 주세요. |
| SessionM | SessionM Connect REST 소매업체 ID | 인스턴스와 연결된 특정 고객에 대한 고유한 가이드 식별입니다. 세션엠 기술 계정 관리자 또는 제공 팀에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[이전 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 생성할 수 있습니다.
{% endalert %} 

## 사용 사례

다음 사용 사례는 SessionM과 Braze 통합을 활용하는 몇 가지 방법을 보여줍니다.

- 모든 로열티, 고객 관리 및 메시징 플랫폼에 걸쳐 데이터를 통합하는 세분화를 생성합니다.
- 강력한 세분화를 사용하여 오퍼 및 프로모션으로 특정 사용자 세트를 타겟팅하세요.
- 메시지를 보낼 때 가장 최신의 사용자, 오퍼, 로열티 정보를 활용하세요.
- 고객에게 프로모션 및 로열티 활동의 진행 상황과 완료에 대한 자세한 알림을 제공합니다.
- 새 혜택이 부여되면 고객에게 알림을 보내고 혜택 세부 정보를 제공합니다.

## 세션M과 Braze 통합

### 1단계: Braze에서 세그먼트 만들기

Braze에서 세션엠 프로모션 및 오퍼로 타겟팅할 사용자 세그먼트를 생성합니다. 

!['사용자 지정 속성' 필터가 선택된 세그먼트 빌더]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### 2단계: 브레이즈 세그먼트를 세션M으로 가져오기

#### 옵션 1: SessionM 태그 엔드포인트로 내보내기(권장)

먼저 Braze에서 웹훅 캠페인을 생성하고 웹훅 URL을 {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %} 으로 설정합니다. Liquid를 사용하여 URL 내에 `user_id` 을 정의합니다. 

원시 텍스트 **요청 본문을** 사용하여 세션M의 사용자 프로필에 추가할 태그와 원하는 라이브 시간을 포함하도록 웹훅 본문을 작성합니다. 예를 들면 다음과 같습니다:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

**설정** 탭에서 각 요청 헤더 필드에 키-값 쌍을 추가합니다:
    \- 해당 값으로 `Content-Type` 키를 만듭니다. `application/json`
    \- 해당 값 `Basic YOUR-ENCODED-STRING-KEY` 을 사용하여 `Authorization` 키를 생성합니다. 엔드포인트에 대한 인코딩된 문자열 키는 SessionM 팀에 문의하세요. 

![웹훅 설정.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

전송 일정을 예약하고 [이전에 생성한](#step-1-create-a-segment-in-braze) 세그먼트를 **타겟팅하도록 타겟 오디언스를** 설정한 다음 캠페인을 시작합니다.

{% alert important %}
이 프로세스는 고객, 태그 이름, 통화 내 각 사용자(통화당 단일 사용자)에 대한 라이브 시간을 지정하여 [SessionM 태그 엔드포인트에](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) 직접 요청함으로써 Postman과 같은 API 클라이언트를 통해 수행할 수도 있습니다.
<br><br>
다음 예제 요청은 cURL을 사용합니다. 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### 옵션 2: CSV 가져오기

브레이즈 세그머를 사용하여 브레이즈 세그먼트를 내보내고 태그할 고객, 태그 이름, 파일에 있는 각 사용자에 대한 라이브 시간이 포함된 CSV 파일을 SessionM에 제공합니다.

## Braze로 실시간 오퍼 지갑 검색하기

세션엠과 브레이즈를 통합하면 커넥티드 콘텐츠를 사용하여 메시지 전송 시 세션엠 사용자 데이터를 실시간으로 가져올 수 있어 오래되었거나 만료되었거나 이미 사용한 로열티 오퍼를 고객에게 전달할 위험을 없앨 수 있습니다. 

다음 예는 연결된 콘텐츠를 사용하여 오퍼 지갑 데이터를 메시지로 템플릿화하는 방법을 보여줍니다. 그러나 커넥티드 콘텐츠는 세션엠의 모든 커넥트 엔드포인트와 함께 사용할 수 있습니다. 

### 1단계: 세션M에서 오퍼 발행

세션엠은 구성할 수 있는 여러 가지 내부 레버를 통해 고객에게 오퍼를 발행합니다. 오퍼가 발행된 후, 오퍼는 세션엠이 "오퍼 지갑"이라고 부르는 상태로 이동합니다.

고객은 필요한 조치를 완료하거나 타겟팅을 충족해야 하며, 세션M 내에서 오퍼를 발급받습니다.

그런 다음 세션엠은 발행된 상태로 고객의 지갑에 오퍼를 추가합니다.

### 2단계: 세션엠 오퍼 월렛 API 호출

캠페인 또는 캔버스 단계에서 SessionM 오퍼를 사용하는 경우, [커넥티드 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) 사용하여 [SessionM `get_user_offers` 엔드포인트에](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/) API 호출을 수행합니다.

연결된 콘텐츠 요청에서 사용자의 세션M `user_id` 및 귀하의 `retailer_id` 을 지정하여 고객이 지갑에 가지고 있는 활성 오퍼의 전체 목록을 검색합니다. 이 엔드포인트에 대한 각 요청에는 단일 사용자가 포함될 수 있습니다. 커넥티드 콘텐츠 호출의 기본 인증 헤더에 대한 인코딩된 문자열 키는 SessionM 팀에 문의하세요.

요청 본문에서 `culture` 는 기본값이 `en-US` 이지만 Liquid를 사용하여 다국어 SessionM 오퍼에 대한 사용자 언어를 템플릿으로 만들 수 있습니다(예: {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### 3단계: 브레이즈 메시징에 오퍼 지갑 채우기

엔드포인트에 요청이 이루어지면 SessionM은 발행된 상태의 전체 오퍼 목록과 각 오퍼에 대한 전체 세부 정보를 반환합니다. 반환된 응답의 예입니다:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

리퀴드 도트 표기법을 사용하여 메시지에 입력할 수 있습니다. 예를 들어, 결과 `offer_id` 로 메시지를 개인화하려면 `100` 를 반환하는 {% raw %}`{{wallet.payload.available_points}`{% endraw %} 을 사용하여 반환 페이로드를 활용할 수 있습니다.

{% alert note %}
이것은 개별 API입니다. 500명 이상의 사용자를 일괄 전송하려는 경우 SessionM 계정 팀에 문의하여 통합에 일괄 데이터를 통합하는 방법에 대해 문의하세요.
{% endalert %}

## 트리거된 메시징 설정하기

세션엠과 브레이즈 간의 통합으로 사용자 프로필 데이터, 오퍼 세부 정보, 포인트 잔액을 메시징에 동적으로 입력할 수 있으며, 행동 시점에 고객에게 실시간으로 전송할 수 있습니다.

### 1단계: 세션엠 딜리버리 팀이 템플릿을 구성합니다.

세션엠 전달 팀과 협업하여 트리거된 메시징에 사용할 템플릿을 개발하세요. 세션엠은 사용자 프로필 데이터, 오퍼 세부 정보, 포인트 잔액을 메시징에 삽입하고 실시간 고객 메시징을 위해 Braze에서 트리거합니다.

SessionM의 모든 템플릿에 있는 표준 필드에는 다음이 포함됩니다:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
`broadcast flag` 을 `true` 으로 설정하면 캠페인 또는 캔버스가 Braze에서 타겟팅하는 전체 세그먼트에 메시지가 전송됩니다.
{% endalert %}

특정 요구 사항에 따라 추가 필드를 구성할 수 있습니다:

- **데이터 제공** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **포인트 적립 데이터:** `point award amount`, `point account name`
- **이벤트 트리거 데이터:** 트리거/전송 웹훅 결과를 활용하는 트리거 이벤트의 모든 데이터
- **캠페인별 데이터:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

메시지를 개인화하기 위해 추가 필드는 `trigger_properties` 으로 Braze에 전송됩니다. 

### 2단계: Braze 캠페인 또는 캔버스 만들기

세션M에서 트리거할 API 트리거 캠페인 또는 캔버스를 Braze에서 생성합니다. `offer_id` 또는 `offer title` 과 같이 추가 필드를 구성한 경우 Liquid(예: {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %})를 사용하여 개인화된 필드를 메시지에 추가합니다.

![API 트리거 속성]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

**전송 예약** 탭에서 캠페인 또는 캔버스 ID를 기록해 두면 SessionM 캠페인 **고급 설정에** 추가됩니다.

![API 트리거 캠페인]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

캠페인 또는 캔버스 세부 정보를 마무리하고 **시작을** 선택합니다. 

### 3단계: SessionM 프로모션 또는 메시징 캠페인 만들기

다음으로, SessionM에서 캠페인을 생성합니다.

![세션엠 캠페인 생성.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

`braze_campaign_id` 또는 `braze_canvas_id` 을 포함하는 다음 JSON 페이로드를 포함하도록 SessionM 캠페인의 고급 설정을 업데이트합니다.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

원하는 일정 또는 동작에 대한 메시지 트리거를 만듭니다. 그런 다음 **외부 메시지** 메뉴에서 **Braze 메시징** 변형을 **메시징 변형으로** 선택하여 템플릿을 사용합니다.

![SessionM 외부 메시지]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

이 템플릿은 관련 정적 및 동적 속성을 가져와서 Braze 엔드포인트로 호출합니다.

![세션엠 브레이즈 템플릿]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
