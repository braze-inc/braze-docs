---
nav_title: "Trigger Properties 개체"
article_title: API 트리거 속성 개체
page_order: 11
page_type: reference
description: "이 참조 문서에서는 트리거 속성 개체의 다양한 구성 요소에 대해 설명합니다."
tool: Campaigns

---

# 트리거 속성 개체

> API 트리거 전달이 있는 캠페인을 전송하기 위해 엔드포인트 중 하나를 사용하는 경우 키 및 값 맵을 제공하여 메시지를 사용자 지정할 수 있습니다.

`trigger_properties`에 객체가 포함된 API 요청을 만드는 경우 해당 객체의 값을 `api_trigger_properties` 네임스페이스 아래의 메시지 템플릿에서 참조할 수 있습니다. 예를 들어, 다음과 같은 요청은 {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %}를 추가하여 메시지에 `"shoes"` 단어를 추가할 수 있습니다.

{% alert note %}
`trigger_properties` 객체와 {% raw %}`api_trigger_properties.${product_name}`{% endraw %} 구문은 캠페인에서만 지원됩니다. 캔버스에 대한 API 트리거 요청의 키와 값을 사용하여 메시지를 커스텀하려면 [캔버스 항목 속성 객체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)를 사용합니다. `trigger_properties` 개체의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 개체 본문

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


