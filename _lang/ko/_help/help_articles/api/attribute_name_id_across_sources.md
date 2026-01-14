---
nav_title: Braze에서 캠페인과 캔버스 속성의 차이점
article_title: Braze에서 캠페인과 캔버스 속성의 차이점
page_order: 1

page_type: reference
description: "이 도움말 문서에서는 Braze의 여러 소스에서 캠페인과 캔버스 속성 이름 및 ID를 비교합니다."
platform: API
---

# Braze에서 캠페인과 캔버스 속성이 소스 간에 어떻게 다른가요?

캠페인, 캔버스, 및 캔버스 단계 이름과 ID는 모두 Liquid, Braze REST API, 및 커런츠에서 사용할 수 있습니다. 이 속성들은 세 가지 소스 모두에서 동일한 값에 매핑되지만, 이름이 다를 수 있습니다. 이 페이지는 이 세 가지를 연결하는 데 도움을 주기 위한 페이지입니다.

## 사용 사례

### Liquid

캠페인 및 캔버스 속성은 Braze =Liquid 태그 대시보드 {% raw %}(예: `{{campaign.${api_id}}}`){% endraw %}에서 리퀴드 태그로 사용할 수 있습니다. Liquid를 사용하여 이러한 속성을 메시지 자체, 연결된 콘텐츠 호출 또는 키-값 페어로 전달할 수 있습니다. 이는 일반적으로 추적 목적으로 수행됩니다.

### REST API

캠페인 및 캔버스 속성은 [캠페인 세부 정보 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) 또는 [캔버스 세부 정보 내보내기 엔드포인트에서도]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) 사용할 수 있습니다. REST API를 사용하여 매핑, 즉 모든 캔버스 이름과 해당 ID의 목록을 작성할 수 있습니다.

### 커런츠

캠페인 및 캔버스 속성은 커런츠의 [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 연결됩니다. 이는 푸시 전송 또는 이메일 열기가 어떤 캠페인 또는 캔버스 구성 요소와 연결되어 있는지 확인할 수 있도록 하는 중요한 정보입니다.

## 캠페인 속성

| 속성 | Liquid | REST API | 커런츠 |
| --- | --- | --- | --- |
| 캠페인 이름 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| 캠페인 ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A(API 호출 자체의 입력으로 사용됨) | campaign_id |
| 배리언트 이름 | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | 해당 없음(캠페인 세부 정보 내보내기 엔드포인트를 사용하여 이형 상품 이름을 이형 상품 ID에 매핑) |
| 배리언트 상품 ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 캔버스 속성

| 속성 | Liquid | REST API | 커런츠 |
| --- | --- | --- | --- |
| 캔버스 이름 | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| 캔버스 ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A(API 호출 자체의 입력으로 사용됨) | canvas_id |
| 배리언트 이름 | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| 배리언트 상품 ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| 단계 이름 | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| 단계 ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| 메시지 채널 | N/A | `steps.messages.message_variation_id.channel` | 해당 없음(푸시 전송 또는 이메일 열기와 같은 이벤트 유형에서 내재됨) |
| 메시지 ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }