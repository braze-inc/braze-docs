---
nav_title: "GET: 제품 ID 내보내기"
article_title: "GET: 제품 ID 내보내기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 제품 ID 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 제품 ID 내보내기
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> 이 엔드포인트를 사용하여 페이지가 지정된 제품 ID 목록을 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `purchases.product_list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
|---|---|---|---|
| `page` | 선택 사항 | 문자열 | 보려는 제품 목록의 페이지입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}
