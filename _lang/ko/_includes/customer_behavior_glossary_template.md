---
nav_title: 고객 행동 및 사용자 이벤트
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 Braze가 커런트를 사용하여 추적하고 선택한 데이터 웨어하우스로 전송할 수 있는 다양한 고객 행동 및 사용자 이벤트가 나열되어 있습니다."
tool: Currents
search_rank: 7
---

추가 이벤트 자격에 대한 액세스가 필요한 경우 Braze 담당자에게 문의하거나 [지원 티켓을]({{site.baseurl}}/braze_support/) 개설하세요. 이 페이지에서 필요한 정보를 찾을 수 없다면 [메시지 참여 이벤트 라이브러리]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 또는 [커런츠 샘플 데이터 예시를](https://github.com/Appboy/currents-examples/tree/master/sample-data) 확인하세요.

{% details 고객 행동 및 사용자 이벤트 구조와 플랫폼 가치에 대한 설명 %}

### 이벤트 구조

이 고객 행동 및 사용자 이벤트 분석은 일반적으로 고객 행동 또는 사용자 이벤트에 어떤 유형의 정보가 포함되는지 보여줍니다. 구성 요소에 대한 확실한 이해를 바탕으로 개발자와 비즈니스 인텔리전스 전략 팀은 수신되는 Currents 이벤트 데이터를 사용하여 데이터 기반 보고서와 차트를 만들고 다른 유용한 데이터 메트릭을 활용할 수 있습니다.

![사용자별 속성, 행동별 속성, 기기별 속성별로 그룹화된 구매 이벤트를 보여주는 사용자 이벤트 분석]({% image_buster /assets/img/customer_engagement_event.png %})

고객 행동 및 사용자 이벤트는 **사용자별** 속성, **행동별** 속성, **기기별** 속성으로 구성됩니다.

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
저장 스키마는 우리가 데이터 웨어하우스 저장 파트너(예: Google Cloud Storage, Amazon S3 및 Microsoft Azure Blob Storage)로 보내는 평면 파일 이벤트 데이터에 적용됩니다. 여기에 나열된 일부 이벤트와 목적지 조합은 아직 일반적으로 사용할 수 없습니다. 다양한 파트너가 지원하는 이벤트에 대한 자세한 내용은 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하여 각 페이지를 확인하세요.<br><br>또한, 커런츠는 페이로드가 900KB를 초과하는 지나치게 큰 이벤트는 삭제한다는 점에 유의하세요.
{% endalert %}