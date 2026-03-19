---
nav_title: "캔버스 컨텍스트 객체"
article_title: API 캔버스 컨텍스트 객체
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "이 문서에서는 Braze 캔버스 컨텍스트 객체에 대해 설명합니다."

---

# 캔버스 컨텍스트 객체

> API를 통해 캔버스를 트리거하거나 예약하는 엔드포인트 중 하나를 사용할 때, `context` 네임스페이스에서 캔버스의 첫 번째 단계에서 전송되는 메시지를 사용자 정의하기 위해 키와 값의 맵을 제공할 수 있습니다.

{% alert note %}
컨텍스트 객체의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 개체 본문

이 객체 본문에는 예제 요청이 포함되어 있습니다.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
예를 들어, API 요청에 `"context": {"product_name" : "shoes", "product_price" : 79.99}`를 포함하고 메시지 템플릿에 ```{{context.${product_name}}}```을 추가하여 "신발"이라는 단어를 참조할 수 있습니다.
{% endraw %}
