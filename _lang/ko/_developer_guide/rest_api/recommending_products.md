---
nav_title: 사용자에게 제품 추천
article_title: 사용자에게 제품 추천하기
page_order: 4
page_type: reference
description: "이 참조 문서에서는 Braze REST API, 카탈로그, 연결된 콘텐츠를 사용하여 메시징 채널 전반에서 사용자에게 제품을 추천하는 방법을 안내합니다."
---

# 사용자에게 제품 추천하기

> Braze REST API를 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/create/) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)와 함께 사용하여 메시지에 개인화된 제품 추천을 표시할 수 있습니다. 이 접근 방식을 사용하면 자체 추천 엔진을 Braze 메시징 생태계에 연결할 수 있으므로, 비기술 사용자도 각 추천과 관련된 콘텐츠와 메시징을 직접 관리할 수 있습니다.

이 접근 방식을 사용하면 다음을 수행할 수 있습니다:

- REST API를 사용하여 백엔드에서 고객 프로필에 제품 추천을 저장합니다.
- 카탈로그 또는 연결된 콘텐츠를 사용하여 발송 시점에 제품 메타데이터를 검색합니다.
- 이메일, 푸시, 인앱 메시지 등 모든 메시징 채널에서 개인화된 추천을 표시합니다.

## 필수 조건

이 가이드를 완료하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Braze REST API 키 | `users.track` 권한이 있는 키이며, API를 통해 카탈로그를 관리하는 경우 관련 카탈로그 권한도 필요합니다. 생성하려면 **설정** > **API 키**로 이동하세요. |
| Braze 카탈로그 | 제품 메타데이터(이름, 카테고리, 가격, 이미지 URL 등)가 포함된 카탈로그입니다. 생성하려면 [카탈로그 생성]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)을 참조하세요. |
| Liquid 지식 | 개인화된 변수를 템플릿화하고 연결된 콘텐츠를 사용하기 위한 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)에 대한 중급 수준의 이해가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: 고객 프로필에 추천 저장

먼저, 추천 엔진에서 생성한 제품 추천을 Braze 고객 프로필에 커스텀 속성으로 저장합니다. 이렇게 하면 메시지 발송 시점에 각 사용자의 추천 제품을 참조할 수 있습니다.

1. 제품 ID나 선호 카테고리 등 저장할 추천 데이터를 결정합니다.
2. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 사용하여 고객 프로필에 커스텀 속성으로 추천을 기록합니다.

### 요청 예시

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT`를 워크스페이스의 [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints)로 바꾸세요.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

나중에 Liquid 템플릿에서 쉽게 참조할 수 있도록 의미 있는 속성 이름(예: `recommended_product_id`)을 사용하세요. 추천 엔진이 새로운 결과를 생성할 때마다 정기적으로 업데이트하여 추천의 정확성을 유지하세요.

## 2단계: 제품 메타데이터 검색

각 고객 프로필에 추천 식별자를 저장한 후, 메시지에 포함할 전체 제품 메타데이터(이름, 가격, 이미지 등)를 검색해야 합니다. 두 가지 옵션이 있습니다:

- **옵션 A:** [Braze 카탈로그](#option-a-braze-catalogs) — 빠른 내장 조회를 위해 제품 정보를 Braze에 직접 저장합니다.
- **옵션 B:** [연결된 콘텐츠](#option-b-connected-content) — 발송 시점에 외부 API에서 제품 정보를 가져옵니다.

### 옵션 A: Braze 카탈로그

제품 인벤토리로 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)를 생성한 경우, Liquid를 사용하여 메시지에서 직접 항목을 조회할 수 있습니다. 전체 안내는 [카탈로그 사용]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)을 참조하세요.

#### 특정 카탈로그 항목 추천

{% raw %}
ID로 특정 제품을 참조하려면 `catalog_items` Liquid 태그를 사용합니다. 예를 들어, `retail_products`라는 카탈로그에서 제품 `1001`을 추천하려면:

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### 여러 카탈로그 항목 추천

{% raw %}
하나의 태그에서 여러 항목을 참조할 수도 있습니다. 예를 들어, 세 가지 제품을 소개하려면:

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### 사용자의 추천을 사용하여 항목 템플릿화

{% raw %}
[1단계](#step-1-store-recommendations-on-user-profiles)의 커스텀 속성과 카탈로그 조회를 결합하여 각 사용자에게 맞는 추천을 개인화합니다:

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### 옵션 B: 연결된 콘텐츠

제품 메타데이터가 Braze 카탈로그가 아닌 외부 서비스에 있는 경우, [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)를 사용하여 발송 시점에 가져올 수 있습니다.

{% raw %}
예를 들어, 내부 API가 ID로 제품 세부 정보를 반환하는 경우:

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

메시지에서 API 호출을 수행하는 방법에 대한 자세한 내용은 [API 호출하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)를 참조하세요.

{% alert warning %}
연결된 콘텐츠를 사용하여 대량의 제품 목록을 가져온 다음 발송 시점에 Liquid에서 해당 목록을 반복 처리하는 것은 피하세요. 대용량 응답 페이로드는 발송 지연 시간을 증가시키고, 대규모 발송 시 메시지 시간 초과 또는 전달 실패를 유발할 수 있습니다. 대신, 사용자에게 필요한 특정 제품 ID만 프로필에 저장하고([1단계](#step-1-store-recommendations-on-user-profiles) 참조), 해당 개별 항목의 메타데이터를 가져오거나 빠른 조회에 최적화된 [카탈로그](#option-a-braze-catalogs)를 사용하세요.
{% endalert %}

## 3단계: 통합 확인

설정을 완료한 후 통합을 확인합니다:

1. [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 엔드포인트를 사용하여 자신의 고객 프로필에 테스트 추천을 기록합니다.
2. 카탈로그 또는 연결된 콘텐츠를 사용하여 추천 제품을 참조하는 테스트 메시지를 발송합니다.
3. 전달된 메시지에서 제품 세부 정보가 올바르게 렌더링되는지 확인합니다.
4. Braze 대시보드에서 캠페인 또는 캔버스 결과 페이지로 이동하여 발송이 기록되었는지 확인합니다.

## 고려 사항

- 추천 엔진이 새로운 결과를 생성할 때마다 커스텀 속성을 정기적으로 업데이트하여 추천 데이터의 정확성을 유지하세요.
- Braze [개인화 기능]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)을 사용하여 제품 세부 정보와 함께 사용자별 데이터를 포함하는 등 메시지를 더욱 맞춤화하세요.
- Braze 대시보드에서 정의한 템플릿을 사용하여 백엔드에서 메시지를 트리거하려면 [API 트리거 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 사용을 고려하세요.