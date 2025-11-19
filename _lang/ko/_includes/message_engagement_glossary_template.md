---
nav_title: 메시지 인게이지먼트 이벤트
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 커런트를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 메시지 참여 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 6
---

스토리지 스키마는 데이터 웨어하우스 스토리지 파트너(Google Cloud Storage, Amazon S3, Microsoft Azure Blob Storage)로 전송하는 플랫 파일 이벤트 데이터에 적용됩니다. 다른 파트너에 적용되는 스키마는 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하여 해당 페이지를 확인하세요.

Contact your account manager or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. 이 문서에서 필요한 내용을 찾을 수 없는 경우 [고객 행동 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 또는 [커런츠 샘플 데이터 예시](https://github.com/Appboy/currents-examples/tree/master/sample-data)를 확인하세요.

{% details 메시지 참여 이벤트 구조 및 플랫폼 가치에 대한 설명 %}

### 이벤트 구조

이 이벤트 분석은 일반적으로 메시지 인게이지먼트 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성 요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 Currents 이벤트 데이터를 사용하여 데이터 기반 보고서와 차트를 만들고 다른 유용한 데이터 메트릭을 활용할 수 있습니다.

![사용자별 속성, 캠페인 또는 캔버스 추적 속성, 이벤트별 속성별로 그룹화된 이메일 수신 거부 이벤트를 보여주는 메시지 인게이지먼트 이벤트의 분석]({% image_buster /assets/img/message_engagement_event.png %})

메시지 참여 이벤트는 **사용자별** 속성, **캠페인/캔버스 추적** 속성, **이벤트별** 속성으로 구성됩니다.

### User ID schema

사용자 ID의 이름 지정 규칙에 유의하세요.

| Braze schema | 전류 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | The unique identifier that is automatically assigned by Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | The unique identifier of a user's profile that is set by the customer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 플랫폼 가치

특정 이벤트는 사용자 기기의 플랫폼을 지정하는 `platform` 값을 반환합니다.
<br>다음 표에서는 반환 가능한 값을 자세히 설명합니다:

| 사용자 디바이스 | 플랫폼 가치 |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| 웹 | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
현재 페이로드가 900KB를 초과하는 지나치게 큰 이벤트는 삭제됩니다.
{% endalert %}

{% alert note %}
캔버스 흐름과 관련된 개체에는 그룹화에 사용할 수 있는 ID가 있으며 [캔버스 세부 정보 내보내기 엔드포인트를]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) 통해 사람이 읽을 수 있는 이름으로 변환할 수 있습니다.
{% endalert %}

{% alert note %}
특정 필드는 캠페인이나 캔버스가 업데이트된 후 가장 최근 상태를 표시하는 데 시간이 더 걸릴 수 있습니다. 이러한 필드는 다음과 같습니다:
<ul>
  <li>"캠페인_이름"</li>
  <li>"캔버스_이름"</li>
  <li>"캔버스_스텝_이름"</li>
  <li>"전환_행동"</li>
  <li>"캔버스_변형_이름"</li>
  <li>"실험_분할_이름"</li>
  <li>"메시지_변형_이름"</li>
</ul>
완전한 일관성이 필요한 경우 이러한 필드에 대한 마지막 업데이트 후 한 시간 정도 기다렸다가 사용자에게 메시지를 보내는 것이 좋습니다.
{% endalert %}