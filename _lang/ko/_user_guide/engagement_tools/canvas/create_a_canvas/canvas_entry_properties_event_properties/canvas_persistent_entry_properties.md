---
nav_title: 지속적인 항목 속성
article_title: 지속적인 항목 속성
alias: "/persistent_entry/"
page_type: reference
description: "이 참조 문서에서는 캔버스에서 지속적인 항목 속성을 사용하여 더 정제된 메시지를 보내고 매우 정교한 최종 사용자 경험을 만드는 방법을 설명합니다."
tool: Canvas
page_order: 5
---

# 지속적인 항목 속성

> 캔버스가 커스텀 이벤트, 구매 또는 API 호출에 의해 트리거될 때, API 호출, 커스텀 이벤트 또는 구매 이벤트의 메타데이터를 사용하여 캔버스 워크플로의 각 단계에서 개인화를 할 수 있습니다. 

이 기능 이전에는 캔버스의 첫 번째 단계에서만 항목 속성을 사용할 수 있었습니다. 캔버스 여정 전반에 걸쳐 항목 속성을 사용할 수 있는 기능을 통해 고객은 보다 엄선된 메시지를 보내고 매우 정제된 최종 사용자 경험을 만들 수 있습니다.

## 항목 속성 사용

항목 속성은 작업 기반 및 API 트리거 캔버스에서 사용할 수 있습니다. 이 항목 속성은 커스텀 이벤트, 구매 또는 API 호출에 의해 캔버스가 트리거될 때 정의됩니다. 자세한 내용은 다음 기사를 참조하십시오:

- [캔버스 항목 속성 객체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [이벤트 속성 객체]({{site.baseurl}}/api/objects_filters/event_object/)
- [구매 객체]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

이들 객체에서 전달된 속성은 `canvas_entry_properties` Liquid 태그를 사용하여 참조할 수 있습니다. 예를 들어, `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`가 포함된 요청은 Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}를 추가하여 메시지에 "shoes"라는 단어를 추가할 수 있습니다.

캔버스에 `canvas_entry_properties` Liquid 태그가 포함된 메시지가 포함된 경우, 해당 속성에 연결된 값은 사용자가 캔버스를 탐색하는 동안 저장되고 사용자가 캔버스를 종료할 때 삭제됩니다. 캔버스 항목 속성은 Liquid에서 참조용으로만 사용할 수 있습니다. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.

{% alert note %}
캔버스 항목 속성 객체의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 엔트리 속성을 사용하도록 캔버스 업데이트 중

이전에 `canvas_entry_properties`를 사용하지 않은 메시지가 포함되지 않은 활성 캔버스가 `canvas_entry_properties`를 포함하도록 편집된 경우, `canvas_entry_properties`가 캔버스에 추가되기 전에 캔버스에 들어간 사용자에게 해당 속성에 해당하는 값이 제공되지 않습니다. 값은 변경이 이루어진 후 캔버스에 들어가는 사용자에게만 저장됩니다.

예를 들어, 11월 3일에 항목 속성을 사용하지 않는 캔버스를 처음 시작한 후 11월 11일에 새 속성 `product_name`을 캔버스에 추가한 경우, `product_name`에 대한 값은 11월 11일 이후에 캔버스에 들어간 사용자만 저장됩니다.

캔버스 항목 속성이 null이거나 비어 있는 경우 조건문을 사용하여 메시지를 중단할 수 있습니다. 다음 코드 스니펫은 Liquid를 사용하여 메시지를 중단하는 방법의 예입니다.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Liquid 메시지 중단에 대한 자세한 내용을 보려면 [Liquid 설명서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)를 확인하세요.

## 글로벌 캔버스 항목 속성

`canvas_entry_properties`를 사용하면 모든 사용자에게 적용되는 전역 속성이나 지정된 사용자에게만 적용되는 사용자별 속성을 설정할 수 있습니다. 사용자별 속성은 해당 사용자의 전역 속성을 대체합니다.

### 예시 요청

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
 
이 요청에서 "음식 알레르기"의 전역 값은 "없음"입니다. 고객_123의 경우, 값은 "dairy"입니다. 이 캔버스의 메시지에 Liquid 스니펫 {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%}이 포함된 경우 Customer_123에게는 "dairy"로 템플릿되고 다른 모든 사람에게는 "none"으로 템플릿됩니다. 

## 사용 사례

If you have a Canvas that is triggered when a user browses an item in your eCommerce site but does not add it to their cart, the first step of the Canvas might be a push notification asking if they are interested in purchasing the item. {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}을 사용하여 제품 이름을 참조할 수 있습니다

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

두 번째 단계에서는 사용자가 장바구니에 상품을 추가했지만 아직 구매하지 않은 경우 결제를 유도하는 푸시 알림을 보낼 수 있습니다. `product_name` 항목 속성을 {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}을 사용하여 계속 참조할 수 있습니다.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

