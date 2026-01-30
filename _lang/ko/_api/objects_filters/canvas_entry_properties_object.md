---
nav_title: "캔버스 항목 속성 객체"
article_title: API 캔버스 엔트리 속성 객체
page_order: 2
page_type: reference
tool:
  - Canvas
description: "이 문서에서는 Braze 캔버스 항목 속성 개체에 대해 설명합니다."

---

# 캔버스 항목 속성 객체

> API를 통해 캔버스를 트리거하거나 예약하는 엔드포인트 중 하나를 사용할 때, `canvas_entry_properties` 네임스페이스에서 캔버스의 첫 번째 단계에서 전송되는 메시지를 사용자 정의하기 위해 키와 값의 맵을 제공할 수 있습니다.

{% alert note %}
캔버스 항목 속성 객체의 최대 크기 제한은 50KB입니다.
{% endalert %}

## 개체 본문

이 객체 본문에는 예제 요청이 포함되어 있습니다.

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
예를 들어 `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` 요청에 ```{{canvas_entry_properties.${product_name}}}``` 을 추가하여 메시지에 '신발'이라는 단어를 추가할 수 있습니다.
{% endraw %}
