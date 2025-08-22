---
nav_title: 웹훅 소개
article_title: 웹훅 소개
page_order: 0
channel:
  - webhooks
description: "이 참조 문서에서는 웹훅의 기본 사항, 일반적인 사용 사례, 웹훅의 구조 및 Braze에서 사용하는 방법을 다룹니다."

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}웹훅에 대하여

> 이 참고 문서는 웹훅의 기초를 다루어 여러분이 직접 만들 수 있는 기본 요소를 제공합니다. Braze에서 웹훅을 생성하는 방법에 대한 단계를 찾고 계십니까? [웹훅 생성]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 참조하십시오.

웹훅은 애플리케이션이 실시간으로 데이터를 공유하기 위해 통신하는 일반적인 방법입니다. 오늘날 우리는 모든 것을 할 수 있는 독립형 애플리케이션을 거의 사용하지 않습니다. 대부분의 경우, 특정 작업을 수행하도록 특화된 여러 다른 앱이나 시스템에서 작업하고 있으며, 이러한 앱들은 모두 서로 통신할 수 있어야 합니다. 그게 바로 웹훅이 등장하는 곳입니다.

웹훅은 특정 기준이 충족된 후 한 시스템에서 다른 시스템으로 보내는 자동화된 메시지입니다. Braze에서 이 기준은 보통 커스텀 이벤트의 트리거링입니다.

핵심적으로, 웹훅은 실시간으로 전송된 데이터에 따라 두 개의 별도 시스템이 효과적인 조치를 취할 수 있도록 하는 이벤트 기반 방법입니다. 그 메시지에는 특정 작업을 수행할 시기와 방법을 수신 시스템에 지시하는 지침이 포함되어 있습니다. 이로 인해 웹훅은 데이터 및 프로그래밍 기능에 보다 동적이고 유연한 접근을 제공하며, 프로세스를 간소화하는 고객 여정을 설정할 수 있도록 합니다.

## 사용 사례

웹훅은 시스템을 연결하는 훌륭한 방법입니다. 결국 웹훅은 앱이 소통하는 방식입니다. 다음은 웹훅이 특히 유용할 수 있는 몇 가지 일반적인 시나리오입니다:

- Braze로 데이터를 보내고 받기
- Braze에서 직접 지원하지 않는 채널을 통해 고객에게 메시지를 보내기
- Braze API에 게시

보다 구체적인 사용 사례는 다음과 같습니다:

- 사용자가 이메일에서 구독을 취소하면 웹훅이 동일한 정보를 사용하여 분석 데이터베이스 또는 CRM을 업데이트하여 해당 사용자의 행동에 대한 전체적인 관점을 보장할 수 있습니다.
- Facebook 메신저 또는 라인 내에서 [거래 메시지]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/)를 사용자에게 전송하세요.
- 웹훅을 사용하여 [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)와 같은 타사 서비스와 통신함으로써 고객의 인앱 및 웹 활동에 응답하여 다이렉트 메일을 보냅니다.
- 게이머가 특정 레벨에 도달하거나 특정 포인트를 획득하면 웹훅과 기존 API 설정을 사용하여 캐릭터 업그레이드 또는 코인을 직접 계정으로 보냅니다. 멀티 채널 메시징 캠페인의 일부로 웹훅을 보내는 경우, 푸시 또는 다른 메시지를 보내어 게이머에게 보상에 대해 동시에 알릴 수 있습니다.
- 항공사인 경우 웹훅과 기존 API 설정을 사용하여 고객이 일정 횟수의 항공편을 예약한 후 고객의 계정에 할인을 적립할 수 있습니다.
- 끝없는 "If This Then That"([IFTTT](https://ifttt.com/about)) 레시피. 예를 들어, 고객이 이메일을 통해 앱에 로그인하면 해당 주소가 자동으로 Salesforce에 구성될 수 있습니다.

## 웹훅의 해부학

웹훅은 다음과 같은 부분으로 구성됩니다.

| 웹훅의 일부 | 설명 |
| --- | --- |
| [HTTP 메서드](#methods) | API와 마찬가지로 웹훅도 요청 메서드가 필요합니다. 이들은 웹훅이 타격하는 URL에 제공되며, 엔드포인트에 제공된 정보를 어떻게 처리할지 알려줍니다. 지정할 수 있는 네 가지 HTTP 메서드가 있습니다: 바로 POST, GET, PUT, 그리고 DELETE입니다. |
| HTTP URL | 웹훅 엔드포인트의 URL 주소. 엔드포인트는 웹훅에서 캡처한 정보를 보내는 장소입니다. |
| 요청 본문 | 웹훅의 이 부분에는 엔드포인트에 전달하는 정보가 포함되어 있습니다. 요청 본문은 JSON 키-값 페어 또는 원시 텍스트일 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![HTTP 메서드, HTTP URL, 요청 본문이 포함된 웹훅 예시]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### HTTP 메서드 {#methods}

다음 표는 웹훅에서 지정할 수 있는 네 가지 다른 HTTP 메서드를 설명합니다.

| HTTP 메서드 | 설명 |
| ----------- | ----------- |
| 게시물 | 이 메서드는 수신 서버에 새 정보를 씁니다. 실제 응용 프로그램에서 POST 메서드의 일반적인 예는 웹사이트의 [연락처 양식](https://www.braze.com/company/contact)입니다. 양식에 입력한 모든 정보는 요청 본문의 일부가 되어 수신자에게 전송됩니다. 이것은 데이터를 보낼 때 가장 일반적으로 사용되는 방법입니다.
| GET | 이 방법은 새로운 정보를 작성하는 것과 반대로 기존 정보를 검색합니다. 정의상 GET 요청은 요청 본문을 지원하지 않습니다. 이것은 서버에서 데이터를 요청할 때 가장 일반적으로 사용되는 방법입니다. 예를 들어, [`/segments/list` 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)를 고려하십시오. GET 요청을 하면 세그먼트 목록이 반환됩니다.
| PUT | 이 메서드는 요청 본문에 있는 정보로 기존 정보를 대체하여 엔드포인트의 정보를 업데이트합니다. 
| 삭제 | 이 메서드는 HTTP URL의 리소스를 삭제합니다. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze의 웹훅

Braze에서 웹훅을 웹훅 캠페인, API 캠페인 또는 캔버스 구성 요소로 만들 수 있습니다.

{% tabs %}
{% tab 웹훅 캠페인 %}

1. Braze 대시보드에서 **캠페인**으로 이동하세요.
2. **캠페인 생성**을 클릭하고 **웹훅**을 선택합니다.

[웹훅 생성]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 참조하십시오.

{% endtab %}
{% tab API 캠페인 %}

1. Braze 대시보드에서 **캠페인**으로 이동하세요.
2. **캠페인 생성**을 클릭하고 **API 캠페인**을 선택합니다.
3. **메시지 추가**를 클릭하고 **웹훅**을 선택합니다.
4. API 호출을 [웹훅 객체]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/)로 포함하도록 포맷하십시오.

[웹훅 생성]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 참조하십시오.

{% endtab %}
{% tab 캔버스 구성요소 %}

1. 귀하의 캔버스에서 새 구성 요소를 만드십시오.
2. 구성 요소의 **메시지** 섹션에서 **웹훅**을 선택합니다.

[웹훅 생성]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 참조하십시오.

{% endtab %}
{% endtabs %}

## 웹훅 오류 처리 및 속도 제한

Braze가 웹훅 호출에서 오류 응답을 수신하면 이러한 응답 헤더를 기반으로 해당 웹훅의 전송 동작을 자동으로 조정합니다:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

이러한 헤더는 속도 제한을 해석하고 그에 따라 전송 속도를 조정하여 추가 오류를 방지하는 데 도움이 됩니다. 또한 재시도에 대한 기하급수적 백오프 전략을 구현하여 시간이 지남에 따라 재시도 시도를 분산함으로써 서버에 과부하가 걸릴 위험을 줄입니다.

특정 호스트에 대한 대부분의 웹훅 요청이 실패하는 것으로 감지되면 해당 호스트에 대한 모든 전송 시도를 일시적으로 연기합니다. 그런 다음 지정된 쿨다운 시간이 지나면 전송을 재개하여 시스템이 복구될 수 있도록 합니다.


