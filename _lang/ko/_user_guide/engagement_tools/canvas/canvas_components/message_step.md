---
nav_title: 메시지 
article_title: 메시지 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "이 참고 문서에서는 메시지 단계를 사용하여 독립형 메시지를 만드는 방법에 대해 설명합니다."
tool: Canvas

---

# 메시지 

> 메시지 단계를 사용하면 캔버스 흐름에서 원하는 위치에 독립형 메시지를 추가할 수 있습니다.

![A Message step named "Lunch promo" using the push channel.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Creating a message

메시지 컴포넌트를 만들려면 먼저 캔버스에 스텝을 추가합니다. Drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Message**. 

### Step 1: Select your messaging channel

You can select from the following messaging channels: 
- Content Cards
- Email
- LINE
- Push notifications
- SMS/MMS/RCS
- In-app messages 
- Webhook
- WhatsApp

![A list of available messaging channels to select for the Message step.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Step 2: 배달 설정 편집

Next, you can edit settings for Intelligent Delivery, Quiet Hours overrides, and delivery validation.

#### Intelligent Timing

사용자 프로필에 최적의 시간을 계산할 수 있는 데이터가 충분하지 않은 경우 대체 옵션으로 [지능형 타이밍을]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) 사용 설정할 수 있습니다. Intelligent Timing 및 [사용량 제한조치]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/)를 사용 설정하여 사용자가 메시지 단계에 진입한 후 실제 메시지 전송까지 지연되는지 추가로 확인하는 것이 좋습니다.

**전달 설정** 탭에서 **Intelligent Timing 사용**을 선택합니다. 여기에서 가장 인기 있는 시간 또는 특정 대체 시간을 선택할 수 있습니다. 방해금지 시간을 사용 설정한 경우 메시지 단계에서도 이 설정을 재정의할 수 있습니다.

#### Delivery validations

배달 유효성 검사는 메시지 전송 시 대상 그룹이 배달 기준을 충족하는지 확인하기 위한 추가 확인 기능을 제공합니다. 이 설정은 방해금지 시간, Intelligent Timing 또는 사용량 제한이 활성화된 경우에 권장됩니다. 세그먼트 또는 추가 필터를 추가하여 메시지 전송 시 유효성을 검사할 수 있습니다. 사용자가 메시지 단계에 대해 설정된 전달 유효성 검사를 충족하지 못하면 해당 단계에서 캔버스를 종료합니다.

![메시지 구성 요소 설정을 위한 전달 설정 탭입니다. 방해금지 시간을 사용하도록 설정하고 Intelligent Timing 사용 확인란을 선택하면 최적의 시간에 메시지를 전달할 수 있습니다. Delivery Validations are enabled to validate the audience at message send.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## How users advance

메시지 단계에 진입한 모든 사용자는 다음 조건 중 하나라도 충족되면 다음 단계로 진행합니다.

- 모든 메시지가 전송됩니다.
- 메시지의 빈도가 제한되어 전송되지 않습니다.
- 메시지가 중단되었습니다.
- 채널로 사용자에게 연결할 수 없으므로 메시지가 전송되지 않습니다.

{% raw %}
작업 기반 캔버스가 인바운드 SMS 메시지에 의해 트리거되는 경우, 첫 번째 단계(메시지 단계) 또는 행동 경로 단계 아래에 중첩된 메시지 단계에서 SMS 속성을 참조할 수 있습니다. 예를 들어 메시지 단계에서는 `{{sms.${inbound_message_body}}}` 또는 `{{sms.${inbound_media_urls}}}`을 사용할 수 있습니다.
{% endraw %}

## Referencing Canvas entry properties

Canvas entry properties are configured in the **Entry Schedule** step of creating a Canvas and will indicate the trigger that enters a user into a Canvas. 이러한 속성은 API 트리거 캔버스에 있는 항목 페이로드의 속성에도 액세스할 수 있습니다. Note that the `canvas_entry_properties` object has a maximum size limit of 50 KB. 

Entry properties can be used in Liquid in any Message step. Use the following Liquid when referencing these entry properties: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. 이 방법으로 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas.
{% endalert %}

Use the following Liquid when referencing these entry properties: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. 이 방법을 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어 다음 요청을 고려해 보세요: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Liquid `{{canvas_entry_properties.${product_name}}}`를 사용하여 메시지에 "신발"이라는 단어를 추가할 수 있습니다.
{% endraw %}

You can also leverage [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) in any Message step to guide your users through personalized steps throughout your Canvas workflow.

### 이벤트 등록정보

Event properties refer to the properties that you set for custom events and purchase events. These event properties can be used in campaigns with action-based delivery as well as Canvases. 

In Canvas, custom event and purchase event properties can be used in Liquid in any Message step that follows an [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) step. For example, when referencing `event_properties`, use this Liquid snippet: {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` can't be used independently of Action Paths steps.
{% endalert %}

행동 경로 다음의 첫 번째 메시지 단계에서 해당 작업 경로에 참조된 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 작업 경로 또는 메시지 단계가 아닌)를 배치할 수 있습니다. 메시지 단계가 행동 경로 단계에서 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties`에 액세스할 수 있습니다.

{% alert important %}
You can't use `event_properties` in the lead Message step. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 앞에 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.
{% endalert %}

{% details Expand for original Canvas editor %}

As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This section is available for reference only.

- `event_properties` can't be used in scheduled full steps. However, you can use `event_properties` in the first full step of an action-based Canvas, even if the full step is scheduled.
- `canvas_entry_properties` can be referenced only in the first full step of a Canvas.
- For in-app message channels specifically, `canvas_entry_properties` can be referenced in the original Canvas editor if you have persistent entry properties enabled as part of the previous early access.

{% enddetails %}

## 분석

메시지 구성 요소 메트릭의 정의는 다음 표를 참조하세요: 

| 측정기준 | 설명 |
| --- | --- |
| _Entries_ | 단계를 입력한 횟수입니다. 캔버스에 재자격이 있는 사용자가 메시지 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| _Proceeded to Next Step_ | 캔버스에서 다음 단계로 진행된 항목 수입니다. |
| _Sends_ | 해당 단계가 보낸 총 메시지 수입니다. 캔버스 자격이 다시 부여되고 사용자가 메시지 단계를 두 번 입력하면 두 개의 항목이 기록됩니다. |
| _Unique Recipients_ | 이 단계에서 메시지를 받은 사용자 수입니다. |
| _Primary Conversion Event_ | Braze 캠페인에서 수신한 메시지와 상호작용하거나 메시지를 본 후 정의된 이벤트가 발생한 횟수입니다. 캠페인을 구축할 때 이 이벤트를 정의합니다. |
| _Revenue_ | 설정된 주요 전환 기간 내에 캠페인 수신자로부터 발생한 총 매출(달러)입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


