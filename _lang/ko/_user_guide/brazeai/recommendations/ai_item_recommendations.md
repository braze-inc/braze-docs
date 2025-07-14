---
nav_title: AI 항목 추천
article_title: AI 항목 추천
page_order: 15
alias: "/ai_item_recommendations/"
description: "이 참조 기사에서는 카탈로그에 있는 항목에 대한 AI 항목 추천을 생성하는 방법을 다룹니다."
---

# AI 항목 추천

> 카탈로그에 있는 항목에 대한 AI 항목 추천을 만드는 방법을 배우세요.

AI 항목 추천을 사용하여 가장 인기 있는 제품을 계산하거나 특정 [카탈로그][카탈로그]에 대한 개인화된 AI 추천을 생성하세요. 추천을 생성한 후 개인화를 사용하여 해당 제품을 메시지에 삽입할 수 있습니다.

## 필수 조건

시작하기 전에 다음을 완료해야 합니다.

- 하나 이상의 [카탈로그][카탈로그]를 보유해야 아래에 설명된 추천 유형을 사용할 수 있습니다.
- Braze에 저장된 고유 제품 ID에 대한 참조가 포함된 구매 또는 이벤트 데이터(커스텀 이벤트 또는 구매 객체)가 있어야 합니다.

{% alert tip %}
[AI 개인화 추천](#recommendation-types)은 수백 또는 수천 개의 항목과 일반적으로 구매 또는 상호 작용 데이터가 있는 최소 30,000명의 사용자를 대상으로 가장 잘 작동합니다. 이는 대략적인 가이드이며 변동될 수 있습니다. 다른 추천 유형은 더 적은 데이터로 작동할 수 있습니다.
{% endalert %}

## AI 항목 추천 생성

항목 추천 생성하기:

1. **분석** > **AI 항목 추천**으로 이동합니다.
2. **예측 생성** > **AI 항목 추천**을 선택합니다.

개별 카탈로그에서 직접 추천을 생성하도록 선택할 수도 있습니다. **카탈로그** 페이지에서 카탈로그를 선택한 다음, **추천 생성**을 선택합니다.

### 1단계: 추천 세부 정보 추가

추천에 이름과 선택적 설명을 제공하세요.

!["Recommendation details" step with the name and description fields.][1]

### 2단계: 추천 정의 {#recommendation-type}

추천 유형을 선택하세요. 모든 추천 유형은 지난 6개월간의 항목 상호작용(구매 또는 커스텀 이벤트) 데이터를 사용합니다. 아래에 언급된 상호작용은 [3단계](#step-3-select-the-interaction-to-drive-recommendations)에서 선택한 구매 이벤트 또는 커스텀 이벤트를 의미합니다.

- **가장 인기 있음:** 카탈로그에서 워크스페이스의 모든 사용자가 가장 자주 상호작용하는 최대 30개의 항목을 계산합니다. 예를 들어 가장 많이 구매한 제품이 포함됩니다.
- **가장 최근:** 사용자가 가장 최근에 상호작용한 최대 30개의 제품 목록을 생성합니다.
- **AI 개인화:** 트랜스포머라는 새로운 종류의 딥러닝을 사용하여 각 사용자가 다음에 상호작용할 가능성이 가장 높은 항목 세트를 예측합니다. Braze는 가장 가능성이 높은 항목을 가장 가능성이 높은 순서대로 최대 30개까지 계산합니다. 이 유형의 추천은 대형 언어 모델(LLM)을 사용하여 데이터와 다른 Braze 고객의 데이터를 결합하지 않습니다.
- **트렌딩:** 워크스페이스에서 사용자 상호작용 측면에서 가장 최근에 긍정적인 모멘텀을 가졌던 최대 30개의 항목을 계산합니다.

{% alert tip %}
**가장 최근** 또는 **AI 개인화**를 사용할 때, 개별화된 추천을 생성하기에 충분한 데이터가 없는 사용자는 대체로 **가장 인기 있는** 항목을 받게 됩니다. 사용자가 **가장 인기 있는** 대체를 받는 비율은 **분석** 페이지에 표시됩니다.
{% endalert %}

#### 2a 단계: 이전 구매 또는 상호 작용 제외 (선택 사항)

사용자가 이미 구매했거나 상호작용한 항목을 추천하지 않으려면 **사용자가 이전에 상호작용한 항목을 추천하지 않음**을 선택하세요. 이 옵션은 추천 **유형**이 **AI 개인화**로 설정된 경우에만 사용할 수 있습니다.

!["Define your recommendation" step with "Most popular" as the type and the "Do not recommend items users have previously interacted with" option selected.][2-3]

이 설정은 추천이 최근에 업데이트된 경우 사용자가 이미 구매했거나 상호작용한 항목을 메시지가 재사용하지 않도록 방지합니다. 추천 업데이트 사이에 구매하거나 상호작용한 항목은 여전히 나타날 수 있습니다. 항목 추천의 무료 버전에서는 업데이트가 매주 이루어집니다. AI 항목 추천의 프로 버전에서는 업데이트가 24시간마다 이루어집니다.

예를 들어, AI 항목 추천의 프로 버전을 사용할 때 사용자가 무언가를 구매하고 30분 이내에 마케팅 이메일을 받으면 방금 구매한 항목이 이메일에서 제때 제외되지 않을 수 있습니다. 그러나 24시간 후에 보낸 메시지에는 해당 항목이 포함되지 않습니다.

#### 2b 단계: 카탈로그 선택

이미 채워지지 않은 경우, 이 추천이 항목을 가져올 [카탈로그][카탈로그]을 선택하세요.

#### 2c 단계: 선택 항목 추가(선택 사항)

추천에 대한 더 많은 제어를 원하시면, [선택]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)를 선택하여 커스텀 필터를 적용하세요. 선택 항목은 카탈로그의 특정 열, 예를 들어 브랜드, 크기 또는 위치에 따라 추천을 필터링합니다. Liquid이 포함된 선택 항목은 추천에 사용할 수 없습니다.

![An example of the "in-stock" selection selected for the recommendation.][2-2]

{% alert tip %}
선택 항목을 찾을 수 없는 경우 먼저 카탈로그에 설정되어 있는지 확인하세요.
{% endalert %}

### 3단계: 상호작용을 선택하여 추천을 유도하세요

최적화할 이벤트를 선택하세요. 이 이벤트는 일반적으로 구매이지만 항목과의 모든 상호 작용일 수도 있습니다.

다음을 위해 최적화할 수 있습니다.

- [구매 객체]({{site.baseurl}}/api/objects_filters/purchase_object/)가 있는 구매 이벤트
- 커스텀 이벤트는 구매를 나타냅니다
- 제품 조회, 클릭 또는 미디어 재생과 같은 기타 항목 상호작용을 나타내는 커스텀 이벤트

**커스텀 이벤트**을 선택하면 목록에서 이벤트를 선택하세요.

![The "Completed Purchase" custom event selected as how events are currently tracked.][3]

### 4단계: 해당 속성 이름을 선택하세요{#property-name}

추천을 생성하려면 상호작용 이벤트(구매 객체 또는 커스텀 이벤트)의 어느 필드가 카탈로그의 항목 `id` 필드와 일치하는 고유 식별자인지 Braze에 알려야 합니다. 확실하지 않나요? [요구 사항을 보세요](#requirements).

이 필드를 **속성정보 이름**에 대해 선택하세요.

**속성정보 이름** 필드는 SDK를 통해 Braze로 전송된 필드 목록으로 미리 채워집니다. 충분한 데이터가 제공되면 이러한 속성도 올바른 속성정보일 확률에 따라 순위가 매겨집니다. 카탈로그의 `id` 필드에 해당하는 것을 선택하세요.

![The property name "purchase_item" selected that corresponds to the item IDs in the catalog.][4]

#### 요구 사항 {#requirements}

속정정보를 선택하기 위한 몇 가지 요구 사항이 있습니다.

- 선택한 카탈로그의 `id` 필드에 매핑해야 합니다.
- **구매 객체를 선택한 경우:** `product_id` 또는 상호작용 이벤트의 `properties` 필드여야 합니다.
- **커스텀 이벤트를 선택한 경우:** 커스텀 이벤트의 `properties` 필드여야 합니다.
- 중첩 필드는 **속성정보 이름** 드롭다운에 점 표기법으로 `event_property.nested_property` 형식으로 입력해야 합니다. 예를 들어, 이벤트 속성정보 `location` 내의 중첩 속성정보 `district_name`을 선택하는 경우 `location.district_name`을 입력합니다.
- 필드는 제품 배열 안에 있을 수 있거나 ID 배열로 끝날 수 있습니다. 어느 경우든 각 제품 ID는 동일한 타임스탬프를 가진 별도의 순차적 이벤트로 처리됩니다.

#### 예시 매핑

다음 예제 매핑은 모두 이 샘플 카탈로그를 참조합니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">제목</th>
    <th class="tg-0pky">가격</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">아디다스 블랙 사이즈 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">아디다스 레드 사이즈 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">아디다스 화이트 사이즈 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">아디다스 보라색 사이즈 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab 커스텀 이벤트 %}

예를 들어, 고객이 결제하기 전에 유사한 제품을 추천할 수 있도록 `added_to_cart` 커스텀 이벤트를 사용하고 싶다고 가정해 보겠습니다. 이벤트 `added_to_cart`에는 `product_sku`의 이벤트 속성정보가 있습니다.

그런 다음 `product_sku` 속성정보에는 샘플 카탈로그의 `id` 열에서 적어도 하나의 값을 포함해야 합니다. "ADI-BL-7", "ADI-RD-8", "ADI-WH-9", 또는 "ADI-PP-10". 모든 카탈로그 항목에 이벤트가 필요하지는 않지만, 추천 엔진이 작업할 수 있는 충분한 콘텐츠를 갖추기 위해 일부는 필요합니다.

##### 예시 커스텀 이벤트 객체

이 이벤트에는 `"product_sku": "ADI-BL-7"`이 있으며, 이는 샘플 카탈로그의 첫 번째 항목과 일치합니다.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### 예제 커스텀 이벤트 객체와 제품 배열

이벤트 속성에 여러 제품이 배열로 포함되어 있는 경우, 각 제품 ID는 별도의 순차적 이벤트로 처리됩니다. 이 이벤트는 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치시키기 위해 속성을 사용할 수 있습니다.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### 예제 커스텀 이벤트 객체와 제품 ID 배열을 포함하는 중첩 객체

제품 ID가 객체 대신 배열의 값인 경우 동일한 표기법을 사용할 수 있으며 각 제품 ID는 별도의 순차적 이벤트로 처리됩니다. 이것은 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치하도록 속성을 구성하여 다음 이벤트에서 중첩된 객체와 유연하게 결합될 수 있습니다.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab 구매 객체 %}

구매가 이루어지면 구매 객체가 API를 통해 전달됩니다.

매핑의 관점에서, 구매 객체에 대해서도 커스텀 이벤트와 유사한 논리가 적용되지만, 구매 객체의 `product_id`를 사용할지 `properties` 객체의 필드를 사용할지 선택할 수 있습니다.

기억하세요, 모든 카탈로그 항목에 이벤트가 필요하지는 않지만, 추천 엔진이 작업할 수 있는 충분한 콘텐츠를 갖추기 위해 일부는 필요합니다.

##### 제품 ID에 매핑된 구매 예시 객체

이 이벤트에는 `"product_id": "ADI-BL-7`이 있으며, 이는 카탈로그의 첫 번째 항목에 매핑됩니다.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### 속성 필드에 매핑된 예제 구매 객체

이 이벤트는 카탈로그의 두 번째 항목에 매핑되는 `"sku": "ADI-RD-8"` 속성정보를 가지고 있습니다.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### 5단계: 추천 훈련시키기

준비가 되면 **추천 생성**을 선택하세요. 이 과정은 완료하는 데 10분에서 36시간이 걸릴 수 있습니다. 추천이 성공적으로 학습되었거나 생성이 실패한 이유에 대한 설명이 있을 경우, 이메일 업데이트를 받게 됩니다.

**예측** 페이지에서 추천을 찾을 수 있으며, 필요에 따라 편집하거나 보관할 수 있습니다. 추천 사항은 매달 한 번 자동으로 재교육됩니다.

## 분석

추천에 대한 분석을 확인하여 사용자에게 추천된 항목과 추천 모델의 정확성을 확인할 수 있습니다.

1. **분석** > **항목 추천**으로 이동합니다.
2. 목록에서 추천을 선택하세요.

페이지 상단에서 추천에 대한 통계, 예를 들어 정밀도와 범위를 찾을 수 있습니다.

![Recommendation audience metrics showing precision (21.1%), coverage (83.0%), and recommendation types split between personalized and most popular items.][5]

이 측정기준은 다음 표에 정의되어 있습니다. 

| 측정기준              | 설명 |
| ------------------- | ---------- |
| 정밀도           | 모델이 사용자가 다음에 구매한 항목을 올바르게 추측한 시간의 비율입니다. 정확도는 특정 카탈로그의 크기와 구성에 크게 의존하며, 모델이 얼마나 자주 정확한지를 이해하는 가이드로 사용해야 합니다.<br><br>과거 테스트에서 우리는 모델이 6-20% 범위의 정밀도 수치로 잘 수행하는 것을 보았습니다. 이 측정기준은 모델이 다음에 재훈련될 때 업데이트됩니다.  |
| 범위            | 카탈로그에 있는 사용 가능한 항목 중 적어도 한 명의 사용자에게 추천된 항목의 비율은 얼마입니까? 개인화된 항목 추천을 통해 가장 인기 있는 항목보다 더 높은 항목 커버리지를 기대할 수 있습니다. |
| 추천 유형 | 사용자 중 개인화된 또는 최신 추천을 받을 비율과 가장 인기 있는 항목의 대체 비율입니다. 대체는 개인화된 또는 최신 추천을 생성하기에 충분한 데이터가 없는 사용자에게 전송됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다음 섹션은 카탈로그의 항목을 두 개의 가능한 열로 나눈 세부 사항을 보여줍니다.

- **개인화된 항목** 또는 **가장 최근 항목:** 이 열은 사용자에게 가장 자주 추천되는 순서대로 카탈로그의 각 항목을 나열합니다. 이 열은 모델에 의해 각 항목에 할당된 사용자 수를 보여줍니다.
- **가장 인기 있는 항목:** 이 열은 카탈로그의 각 항목을 인기 순으로 내림차순으로 나열합니다. 인기란 전체 워크스페이스에서 사용자가 가장 자주 상호작용하는 카탈로그의 항목을 의미합니다. 가장 인기 있는 것은 개인화된 또는 가장 최근의 것을 개별 사용자에 대해 계산할 수 없을 때 대체로 사용됩니다.

![Side-by-side tables listing items assigned to users, separated by personalized recommendations and most popular recommendations.][6]

**추천 개요**는 추천 구성이 마지막으로 업데이트된 시점을 포함하여 선택한 추천 구성의 요약을 보여줍니다.

![Recommendation overview table displaying type, catalog, event type, custom event name, property name, and last updated date.][7]{: style="max-width:45%" }

## 메시징에서 추천 사용

!["Add Personalization" modal with item recommendation as the personalization type.][10]{: style="max-width:30%;float:right;margin-left:15px;"}

추천이 완료되면 Liquid를 사용하여 해당 카탈로그에서 가장 인기 있는 제품을 삽입하여 메시지를 개인화할 수 있습니다. Liquid은 메시지 작성기에서 찾을 수 있는 개인화 창에 의해 생성될 수 있습니다:

1. 메시지 작성기에서 개인화를 지원하는 경우, 개인화 창을 열려면 <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="개인화 추가"></i>를 선택하세요.
2. **개인화 유형**에서 **항목 추천**을 선택하세요.
3. **항목 추천 이름**에 대해 방금 생성한 추천을 선택하세요.
4. **예측된 항목 수**에 대해 삽입하고 싶은 상위 제품의 수를 입력하세요. 예를 들어, 가장 많이 구매된 상위 세 개의 항목을 표시할 수 있습니다.
5. **표시할 정보**에 대해 카탈로그에서 각 항목에 포함할 필드를 선택하세요. 이 항목에 대한 각 필드의 값은 이 추천과 관련된 카탈로그에서 가져옵니다.
6. **복사** 아이콘을 선택하고 메시지에 Liquid를 붙여넣으세요.

## AI 항목 추천 등급

다음 표는 AI 개인화된, 인기 있는, 트렌딩 추천 유형의 무료 및 프로 버전 간의 차이점을 설명합니다.

| 지역                   | 무료 버전                          | 프로 버전            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| 사용자 업데이트 빈도<sup>1</sup>   | 주별                                | 일별                                    |
| 모델 재훈련 빈도  | 월별                               | 월별                                   |
| 최대 추천 모델 | 타입당 1개 모델 | 100 모델당 2종 |

<sup>1\. 사용자별 항목 추천이 업데이트되는 빈도입니다(모델이 재훈련될 때 업데이트되는 가장 인기 있는 항목 제외). 예를 들어, 사용자가 AI 항목 추천을 기반으로 추천된 항목을 구매하면, 추천된 항목은 이 빈도</sup>에 따라 업데이트됩니다.<br>
<sup>2\. 사용 가능한 추천 유형은 AI 개인화된, 가장 최근, 가장 인기 있는, 그리고 트렌딩입니다.</sup>

## 자주 묻는 질문

### "가장 인기 있음" 항목이 다른 모델의 추천에 섞이는 원인은 무엇입니까?

Braze의 추천 엔진이 목록을 큐레이트할 때, 먼저 선택한 특정 모델에 따라 개인화된 선택을 우선시합니다. 예를 들어 "가장 최근" 또는 "AI 개인화"과 같은 모델입니다. 이 모델이 어떤 이유로든 30개의 추천 목록을 완성할 수 없는 경우, 모든 사용자들 사이에서 가장 인기 있는 항목 중 일부가 추가되어 각 사용자가 항상 완전한 추천 세트를 갖도록 합니다.

이것은 몇 가지 특정 조건에서 발생합니다:

- 모델은 사용자의 기준에 맞는 항목을 30개 미만으로 찾습니다.
- 관련 항목은 더 이상 사용 가능하거나 재고가 없습니다.
- 항목이 현재 선택 기준을 충족하지 않으며, 이는 재고 변경 또는 사용자 선호도 변경 때문일 수 있습니다.

### Do existing recommendations train weekly after upgrading to Item Recommendations Pro?

예, 하지만 다음 예정된 업데이트 이후에만 가능합니다. 기존 추천은 Item Recommendations Pro로 업그레이드할 때 즉시 주간 훈련 및 일일 예측으로 전환되지 않습니다. 그러나 다음 재훈련 주기에서 새로운 일정이 자동으로 적용됩니다. 예를 들어, 추천이 2월 1일에 마지막으로 훈련되었고 30일마다 재훈련되도록 설정된 경우, 3월 2일 다음 업데이트 후 새로운 주간 일정이 적용됩니다.

[1]: {% image_buster /assets/img/item_recs_1.png %}
[2-1]: {% image_buster /assets/img/item_recs_2-1.png %}
[2-2]: {% image_buster /assets/img/item_recs_2-2.png %}
[2-3]: {% image_buster /assets/img/item_recs_2-3.png %}
[3]: {% image_buster /assets/img/item_recs_3.png %}
[4]: {% image_buster /assets/img/item_recs_4.png %}
[5]: {% image_buster /assets/img/item_recs_analytics_1.png %}
[6]: {% image_buster /assets/img/item_recs_analytics_2.png %}
[7]: {% image_buster /assets/img/item_recs_analytics_3.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[카탈로그]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/
