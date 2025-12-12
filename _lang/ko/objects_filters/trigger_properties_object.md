---
nav_title: "트리거 속성 개체"
article_title: API 트리거 속성 개체
page_order: 11
page_type: reference
description: "이 참조 문서에서는 트리거 속성 개체의 다양한 구성 요소에 대해 설명합니다."
tool: Campaigns

---

# 트리거 속성 개체

> API 트리거 전송으로 캠페인을 전송하기 위해 엔드포인트 중 하나를 사용하는 경우 메시지를 사용자 지정하기 위해 키와 값의 맵을 제공할 수 있습니다.

`trigger_properties` 에 객체가 포함된 API 요청을 하면 해당 객체의 값을 `api_trigger_properties` 네임스페이스에서 메시지 템플릿에서 참조할 수 있습니다. 예를 들어 다음과 같은 요청은 {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} 을 추가하여 메시지에 `"shoes"` 이라는 단어를 추가할 수 있습니다. 

트리거 속성을 메시지로 템플릿화할 수는 있지만 기본적으로 사용자 프로필에 자동으로 저장되지는 않습니다.

{% alert note %}
`trigger_properties` 개체 및 {% raw %}`api_trigger_properties.${product_name}`{% endraw %} 구문은 캠페인에서만 지원됩니다. 캔버스에 대한 API 트리거 요청의 키와 값으로 메시지를 사용자 지정하려면 캔버스 [항목 속성 개체를]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 사용하세요. `trigger_properties` 객체의 최대 크기 제한은 50KB입니다.
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


