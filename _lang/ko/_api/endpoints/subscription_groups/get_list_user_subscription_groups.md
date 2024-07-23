---
nav_title: "GET: 사용자의 구독 그룹 나열"
article_title: "GET: 사용자의 구독 그룹 나열"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 List 사용자의 구독 그룹 Braze 엔드포인트에 대한 세부 정보를 설명합니다."

---
{% api %}
# 사용자의 구독 그룹 나열
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 사용자의 구독 그룹을 나열하고 가져옵니다.

**이메일 구독 그룹**에 대한 예제를 보거나 이 엔드포인트를 테스트하려면 다음을 수행하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

예를 보거나**SMS 구독 그룹**에 대한 이 끝점을 테스트하려면 다음을 수행하십시오.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

예시를 보거나**WhatsApp 그룹**에 대한 이 엔드포인트를 테스트하려면 다음을 수행하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## 전제조건

이 엔드포인트를 사용하려면 `subscription.groups.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 비율 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `external_id`  | 필수 | 문자열 | 사용자의 `external_id`(최소 1개에서 최대 50개의 `external_ids`를 포함해야 함). |
| `email`| 필수* | 문자열 | 사용자의 이메일 주소는 문자열 배열로 전달될 수 있습니다. 이메일 주소를 하나 이상 포함해야 합니다(최대 50개). |
| `phone`| 필수* |[E.164](https://en.wikipedia.org/wiki/E.164)형식의 문자열 | 사용자의 전화번호입니다. 전화번호를 하나 이상(최대 50개) 포함해야 합니다. |
| `limit`| 선택사항 | 정수 | 반환되는 최대 결과 수에 대한 제한입니다. 기본값(및 최대값) `limit`은 100입니다. |
| `offset`| 선택사항 | 정수 | 검색 기준에 맞는 나머지 템플릿을 반환하기 전에 건너뛸 템플릿 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
동일한 이메일 주소를 공유하는 사용자가 여러 명인 경우(여러 `external_ids`), 모든 사용자는 별도의 사용자로 반환됩니다(동일한 이메일 주소 또는 구독 그룹을 가지고 있는 경우에도 마찬가지임).
{% endalert %}

## 예시 요청 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}
{% endapi %}
