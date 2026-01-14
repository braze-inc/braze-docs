---
nav_title: 지속성 항목 속성정보
article_title: 지속성 항목 속성정보
alias: "/persistent_entry/"
page_type: reference
description: "이 참조 문서에서는 캔버스에서 지속성 항목 속성정보를 사용하여 보다 선별된 메시지를 보내고 고도로 정제된 최종 사용자 경험을 만드는 방법에 대해 설명합니다."
tool: Canvas
page_order: 5
---

# 지속성 항목 속성정보

> 캔버스가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거되면 API 호출, 커스텀 이벤트 또는 구매 이벤트의 메타데이터를 사용하여 캔버스 워크플로우의 각 단계에서 개인화할 수 있습니다. 이러한 속성을 사용하여 더욱 선별된 메시지를 보낼 수 있습니다.

{% alert important %}
지속성 항목 속성정보는 원래 캔버스 에디터의 아티팩트로, 과거 참조용으로 남아 있는 용어에 대한 참조가 더 이상 사용되지 않습니다. 현재 업데이트된 캔버스 편집기에 대해서는 [캔버스 항목 속성 및 이벤트 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) 참조하세요.
{% endalert %}

## 항목 속성 사용

항목 속성은 액션 기반 및 API 트리거 캔버스에서 사용할 수 있습니다. 이러한 항목 속성은 캔버스가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거될 때 정의됩니다. 자세한 내용은 다음 도움말을 참조하세요:

- [캔버스 항목 속성 개체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [이벤트 속성정보 개체]({{site.baseurl}}/api/objects_filters/event_object/)
- [구매 개체]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

이러한 객체에서 전달된 프로퍼티는 `canvas_entry_properties` Liquid 태그를 사용하여 참조할 수 있습니다. 예를 들어, `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` 라는 요청에 Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} 를 추가하여 메시징에 "신발"이라는 단어를 추가할 수 있습니다.

캔버스에 `canvas_entry_properties` Liquid 태그가 있는 메시징이 포함된 경우, 해당 속성과 관련된 값은 사용자가 캔버스에 머무는 동안 저장되고 사용자가 캔버스를 나가면 삭제됩니다. 캔버스 항목 속성은 Liquid에서만 참조할 수 있습니다. 캔버스 내의 속성을 필터링하려면 [이벤트 속성 세분화를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) 대신 사용하세요.

{% alert note %}
캔버스 항목 속성 개체의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 항목 속성을 사용하도록 캔버스 업데이트하기

이전에 `canvas_entry_properties` 을 사용하는 메시징을 포함하지 않았던 활성 캔버스가 `canvas_entry_properties` 을 포함하도록 편집된 경우 `canvas_entry_properties` 이 캔버스에 추가되기 전에 캔버스를 입력한 사용자는 해당 속성에 해당하는 값을 사용할 수 없게 됩니다. 변경이 이루어진 후 캔버스에 들어오는 사용자에 대해서만 값이 저장됩니다.

예를 들어 11월 3일에 입력 속성을 사용하지 않은 캔버스를 처음 시작한 후 11월 11일에 새 속성 `product_name` 을 캔버스에 추가한 경우 11월 11일 이후에 캔버스에 입력한 사용자에 대해서만 `product_name` 의 값이 저장됩니다.

캔버스 항목 속성이 null이거나 비어 있는 경우 조건문을 사용하여 메시지를 중단할 수 있습니다. 다음 코드 스니펫은 Liquid를 사용하여 메시지를 중단하는 방법의 예시입니다.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Liquid로 메시지를 중단하는 방법에 대해 자세히 알아보려면 [Liquid 설명서를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) 참조하세요.

## 글로벌 캔버스 항목 속성

`canvas_entry_properties` 을 사용하여 모든 사용자에게 적용되는 전역 속성 또는 지정된 사용자에게만 적용되는 사용자별 속성을 설정할 수 있습니다. 사용자별 속성이 해당 사용자의 전역 속성을 대체합니다.

### 요청 예시

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
이 요청에서 '음식 알레르기'의 글로벌 값은 '없음'입니다. Customer_123, 의 경우 값은 "유제품"입니다. Liquid 스니펫 {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} 이 포함된 캔버스의 메시지는 Customer_123 에 대해서는 "유제품"으로, 그 외에는 "없음"으로 템플릿이 지정됩니다. 

## 사용 사례

사용자가 전자상거래 사이트에서 품목을 탐색했지만 장바구니에 추가하지 않을 때 트리거되는 캔버스가 있는 경우, 캔버스의 첫 번째 단계는 품목 구매에 관심이 있는지 묻는 푸시 알림이 될 수 있습니다. 다음을 사용하여 제품 이름을 참조할 수 있습니다. {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

\![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

두 번째 단계에서는 사용자가 장바구니에 상품을 추가했지만 아직 구매하지 않은 경우 결제를 요청하는 또 다른 푸시 알림을 보낼 수 있습니다. {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} 을 사용하여 `product_name` 항목 속성을 계속 참조할 수 있습니다.

\![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

