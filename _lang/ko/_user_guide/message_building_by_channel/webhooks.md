---
nav_title: 웹훅
article_title: 웹훅
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "웹훅"
guide_top_text: "웹훅은 애플리케이션이 통신하는 일반적인 방법으로, 실시간으로 데이터를 공유합니다. 오늘날에는 모든 것을 할 수 있는 독립형 애플리케이션이 거의 없습니다. 대부분의 경우 특정 작업을 수행하기 위해 특화된 다양한 앱이나 시스템에서 작업하고 있으며, 이러한 앱은 모두 서로 통신할 수 있어야 합니다. 이것이 바로 웹훅이 필요한 이유입니다. <br><br> 웹훅은 특정 기준이 충족된 후 한 시스템에서 다른 시스템으로 자동화된 메시지입니다. Braze에서 이 기준은 일반적으로 커스텀 이벤트의 트리거가 됩니다. <br><br>웹훅의 핵심은 두 개의 개별 시스템이 실시간으로 전송되는 데이터를 기반으로 효과적인 조치를 취할 수 있는 이벤트 기반 방식입니다. 이 메시지에는 수신 시스템에 특정 작업을 언제, 어떻게 수행해야 하는지 알려주는 지침이 포함되어 있습니다. 따라서 웹훅을 사용하면 데이터 및 프로그래밍 기능에 보다 역동적이고 유연하게 액세스할 수 있으며, 프로세스를 간소화하는 고객 여정을 설정할 수 있습니다. <br><br>**웹훅 사용 가능 여부는 사용 중인 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요**."
description: "이 랜딩 페이지에는 웹훅이 있습니다. 여기에서 웹훅 만들기, 웹훅 템플릿 만들기, Braze 간 웹훅에 대한 글을 찾을 수 있습니다."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "섹션 기사"
guide_featured_list:
- name: 웹훅 만들기
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: 웹훅 템플릿 만들기
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Braze 간 웹훅
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: 보고
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: 웹훅 요청 문제 해결하기 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"} 사용 사례

웹훅은 시스템을 서로 연결하는 훌륭한 방법이며, 결국 웹훅은 앱이 통신하는 방식입니다. 다음은 웹훅이 특히 유용할 수 있는 몇 가지 일반적인 시나리오입니다:

- Braze와 데이터 주고받기
- Braze에서 직접 지원하지 않는 채널을 통해 고객에게 메시지 보내기
- Braze API에 게시하기

좀 더 구체적인 사용 사례는 다음과 같습니다:

- 사용자가 이메일을 탈퇴하면 웹훅을 통해 동일한 정보로 분석 데이터베이스 또는 CRM을 업데이트하여 해당 사용자의 행동에 대한 전체적인 관점을 확보할 수 있습니다.
- Facebook 메신저 또는 Line 내에서 사용자에게 [트랜잭션 메시지를]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) 보냅니다.
- 웹훅을 사용하여 다음과 같은 타사 서비스와 통신하여 고객의 인앱 및 웹 활동에 대한 응답으로 고객에게 다이렉트 메일을 보내세요. [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- 게이머가 특정 레벨에 도달하거나 특정 포인트를 획득하면 웹훅과 기존 API 설정을 사용하여 캐릭터 업그레이드 또는 코인을 계정으로 직접 전송할 수 있습니다. 멀티 채널 메시징 캠페인의 일부로 웹훅을 전송하는 경우 푸시 또는 기타 메시지를 전송하여 게이머에게 보상에 대해 동시에 알릴 수 있습니다.
- 항공사의 경우 웹훅과 기존 API 설정을 사용하여 고객이 특정 항공편을 예약한 후 고객의 계정에 할인을 적립할 수 있습니다.
- 예를 들어 고객이 이메일을 통해 앱 인스턴스에 로그인하면 해당 주소가 자동으로 Salesforce에 구성될 수 있는 무한한 "[IFTTT(](https://ifttt.com/about)If This Then That[)](https://ifttt.com/about)" 레시피가 있습니다.

## 웹훅의 해부학

웹훅은 다음과 같은 부분으로 구성됩니다.

| 웹훅의 일부 | 설명 |
| --- | --- |
| [HTTP 메서드](#methods) | API와 마찬가지로 웹훅에도 요청 메서드가 필요합니다. 이는 웹훅이 도달한 URL에 주어지며, 엔드포인트에 주어진 정보로 수행할 작업을 알려줍니다. 지정할 수 있는 HTTP 메서드는 네 가지가 있습니다: 게시, 가져오기, 넣기, 삭제. |
| HTTP URL | 웹훅 엔드포인트의 URL 주소입니다. 엔드포인트는 웹훅에서 캡처하는 정보를 전송하는 곳입니다. |
| 요청 본문 | 웹훅의 이 부분에는 엔드포인트에 전달하는 정보가 포함되어 있습니다. 요청 본문은 JSON 키-값 페어 또는 원시 텍스트일 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

예제 웹훅은 HTTP 메서드, HTTP URL, 요청 본문으로 구성됩니다.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### HTTP 메서드 {#methods}

다음 표에서는 웹훅에 지정할 수 있는 네 가지 HTTP 메서드에 대해 설명합니다.

| HTTP 메서드 | 설명 |
| ----------- | ----------- |
| POST | 이 메서드는 수신 서버에 새 정보를 기록합니다. 실제 애플리케이션에서 POST 방법을 사용하는 일반적인 예는 웹사이트의 [문의 양식입니다](https://www.braze.com/company/contact). 양식에 입력하는 모든 정보는 요청 본문의 일부가 되어 수신자에게 전송됩니다. 데이터를 전송할 때 가장 일반적으로 사용되는 방법입니다.
| GET | 이 방법은 새로운 정보를 작성하는 것이 아니라 기존 정보를 검색합니다. 정의상 GET 요청은 요청 본문을 지원하지 않습니다. 서버에 데이터를 요청할 때 가장 일반적으로 사용되는 방법입니다. 예를 들어 [`/segments/list` 엔드포인트를]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) 생각해 보세요. GET 요청을 하면 세그먼트 목록을 반환합니다.
| PUT | 이 메서드는 엔드포인트의 정보를 업데이트하여 기존 정보를 요청 본문에 있는 정보로 대체합니다. 
| 삭제 | 이 메서드는 HTTP URL에서 리소스를 삭제합니다. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze 간 웹훅

Braze에서는 웹훅을 웹훅 캠페인, API 캠페인 또는 캔버스 컴포넌트로 만들 수 있습니다.

{% tabs %}
{% tab Webhook Campaign %}

1. Braze 대시보드에서 **캠페인으로** 이동합니다.
2. **캠페인 생성을** 클릭하고 **웹훅을** 선택합니다.

자세한 내용은 [웹훅 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 참조하세요.

{% endtab %}
{% tab API Campaign %}

1. Braze 대시보드에서 **캠페인으로** 이동합니다.
2. **캠페인 생성을** 클릭하고 **API 캠페인을** 선택합니다.
3. **메시지 추가를** 클릭하고 **웹훅을** 선택합니다.
4. [웹훅 객체를]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/) 포함하도록 API 호출 형식을 지정합니다.

자세한 내용은 [웹훅 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 참조하세요.

{% endtab %}
{% tab Canvas Component %}

1. 캔버스에서 새 컴포넌트를 만듭니다.
2. 컴포넌트의 **메시지** 섹션에서 **웹훅을** 선택합니다.

자세한 내용은 [웹훅 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 참조하세요.

{% endtab %}
{% endtabs %}

## 웹훅 오류 처리 및 속도 제한

Braze가 웹훅 호출에서 오류 응답을 받으면 이러한 응답 헤더를 기반으로 해당 웹훅의 전송 동작을 자동으로 조정합니다:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

이러한 헤더는 속도 제한을 해석하고 그에 따라 전송 속도를 조정하여 추가 오류를 방지하는 데 도움이 됩니다. 또한 재시도에 대한 지수 백오프 전략을 구현하여 시간이 지남에 따라 재시도 시도를 분산함으로써 서버에 과부하가 걸릴 위험을 줄입니다.

특정 호스트에 대한 대부분의 웹훅 요청이 실패하는 것을 감지하면 해당 호스트에 대한 모든 전송 시도를 일시적으로 연기합니다. 그런 다음 지정된 쿨다운 시간이 지나면 전송을 재개하여 시스템이 복구될 수 있도록 합니다.


