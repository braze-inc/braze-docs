캔버스 사용자 여정에서 캔버스 항목 속성정보와 이벤트 속성정보를 사용할 수 있습니다.

{% tabs local %}
{% tab Canvas Entry Properties %}

[캔버스 진입 속성]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)은 실행 기반 또는 API로 트리거되는 캔버스에 매핑하는 속성입니다. `canvas_entry_properties` 객체의 최대 크기 제한은 50KB입니다.

{% alert note %}
For in-app message channels specifically, `canvas_entry_properties` can only be referenced in Canvas.
{% endalert %}

이 Liquid 형식의 메시지 단계에서 `canvas_entry_properties` 을 참조할 수 있습니다: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. 이 방법을 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

#### 사용 사례

{% raw %}
소매점인 RetailApp에 다음과 같은 요청이 있다고 가정해 보겠습니다: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp은 제품 이름(신발)을 이 Liquid를 사용하여 메시지로 가져올 수 있습니다: `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

또한 RetailApp은 구매 이벤트를 트리거한 사용자를 대상으로 하는 캔버스의 다양한 `product_name` 속성에 대해 특정 메시지를 전송하도록 트리거할 수 있습니다. 예를 들어, 신발을 구매한 사용자와 다른 제품을 구매한 사용자에게 각각 다른 메시지를 보낼 수 있도록 다음 Liquid를 메시지 단계에 추가할 수 있습니다.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

You can no longer create or duplicate Canvases using the original editor. This section is available for reference only. 원래 편집기로 구축된 캔버스의 경우 캔버스 항목 속성은 캔버스의 첫 번째 전체 단계에서만 참조할 수 있습니다.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

이벤트 속성은 사용자 지정 이벤트 및 구매에 대해 설정한 속성을 나타냅니다. 이러한 `event_properties`는 실행 기반 전달 및 캔버스가 있는 캠페인에서 사용할 수 있습니다.

{% alert important %}
캔버스의 첫 번째 메시지 단계에서는 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.
{% endalert %}

캔버스에서 커스텀 이벤트 및 구매 이벤트 속성정보는 행동 경로 단계를 따르는 모든 메시지 단계에서 Liquid에서 사용할 수 있습니다. 이러한 이벤트 속성정보를 참조하는 경우 {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} 을 사용해야 합니다. 이러한 이벤트는 메시지 구성 요소에서 이러한 방식으로 사용하려면 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

행동 경로 다음의 첫 번째 메시지 단계에서는 해당 행동 경로에서 참조된 이벤트와 관련된 이벤트 속성정보를 사용할 수 있습니다. 그러나 이러한 이벤트 속성정보는 사용자가 실제로 작업을 수행한 경우에만 사용할 수 있습니다(다른 모든 사용자 그룹으로 분류되지 않은 경우). 이 작업 경로와 메시지 단계 사이에 다른 작업 경로 또는 메시지 단계가 아닌 다른 단계를 가질 수 있습니다.

{% details Expand for original Canvas editor %}

You can no longer create or duplicate Canvases using the original editor. This section is available for reference only. 기존 캔버스 에디터의 경우 예약된 전체 단계에서는 이벤트 속성정보를 사용할 수 없습니다. 그러나 전체 단계가 예약되어 있더라도 액션 기반 캔버스의 첫 번째 전체 단계에서는 이벤트 속성정보를 사용할 수 있습니다.

{% enddetails %}

{% endtab %}
{% endtabs %}

자세한 정보와 예시는 [캔버스 항목 속성 및 이벤트 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) 참조하세요.