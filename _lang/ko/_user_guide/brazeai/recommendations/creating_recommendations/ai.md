---
nav_title: AI 추천
article_title: AI 아이템 추천 만들기
description: "이 참고 문서에서는 카탈로그의 품목에 대한 AI 품목 추천을 생성하는 방법에 대해 설명합니다."
page_order: 1
---

# AI 항목 추천 만들기

> 카탈로그의 항목으로 AI 추천 엔진을 만드는 방법을 알아보세요.

## AI 아이템 추천 정보

AI 제품 추천을 사용하여 가장 인기 있는 제품을 계산하거나 특정 [카탈로그에]({{site.baseurl}}/user_guide/data/activation/catalogs/) 대한 개인화된 AI 추천을 생성하세요. 추천을 생성한 후 개인화를 사용하여 해당 제품을 메시징에 삽입할 수 있습니다.

{% alert tip %}
[AI 개인화된 추천은](#recommendation-types) 수백 또는 수천 개의 아이템과 일반적으로 구매 또는 상호작용 데이터를 보유한 최소 30,000명의 사용자에서 가장 잘 작동합니다. 이는 대략적인 가이드일 뿐이며 달라질 수 있습니다. 다른 추천 유형은 더 적은 데이터로 작동할 수 있습니다.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## AI 아이템 추천 생성하기

### 전제 조건

시작하기 전에 다음을 완료해야 합니다:

- 아래에 설명된 권장 사항 유형을 사용하려면 [카탈로그가]({{site.baseurl}}/user_guide/data/activation/catalogs/) 하나 이상 있어야 합니다.
- 카탈로그에 저장된 고유 제품 ID에 대한 참조가 포함된 구매 또는 이벤트 데이터(커스텀 이벤트 또는 구매 오브젝트)가 Braze에 있어야 합니다.

### 1단계: 새 추천 만들기

대시보드의 어느 위치에서나 AI 아이템 추천을 생성할 수 있습니다:

{% tabs local %}
{% tab From the navigation menu %}
1. **분석** > **AI 항목 추천으로** 이동합니다.
2. **예측 생성** > **AI 항목 추천을** 선택합니다.
{% endtab %}

{% tab From a catalog %}
개별 카탈로그에서 직접 추천을 생성하도록 선택할 수도 있습니다. **카탈로그** 페이지에서 카탈로그를 선택한 다음 **권장 사항 만들기를** 선택합니다.
{% endtab %}
{% endtabs %}

### 2단계: 추천 세부 정보 추가

추천의 이름과 설명(선택 사항)을 입력합니다.

이름 및 설명 필드가 있는 '추천 세부 정보' 단계를 클릭합니다.]({% image_buster /assets/img/item_recs_1.png %})

### 3단계: 추천 정의 {#recommendation-type}

추천 유형을 선택합니다. 각 유형은 구매 또는 커스텀 이벤트 데이터와 같은 지난 6개월간의 아이템 상호 작용 데이터를 사용합니다. 각 [유형에]({{site.baseurl}}/user_guide/brazeai/recommendations/) 대한 자세한 정보와 사용 사례는 [유형 및 사용 사례를]({{site.baseurl}}/user_guide/brazeai/recommendations/) 참조하세요.

{% alert tip %}
**가장 최근** 또는 **AI 개인화를** 사용할 때 개인화된 추천을 생성하기에 데이터가 부족한 사용자에게는 **가장 인기 있는** 항목이 대체로 제공됩니다. **가장 인기 있는** 대체 서비스를 받는 사용자의 비율은 **분석** 페이지에 표시됩니다.
{% endalert %}

#### 3.1단계: 이전 구매 또는 상호 작용 제외(선택 사항)

사용자가 이미 구매했거나 상호 작용한 아이템을 추천하지 않으려면 **사용자가 이전에 상호 작용한 아이템을 추천하지 않음을** 선택합니다. 이 옵션은 추천 **유형이** **AI 개인화로** 설정된 경우에만 사용할 수 있습니다.

"추천 정의" 단계에서 "AI 개인화"를 유형으로 선택하고 "사용자가 이전에 상호작용한 항목은 추천하지 않음" 옵션을 선택합니다.]({% image_buster /assets/img/item_recs_2-3.png %})

이 설정은 추천이 최근에 업데이트된 경우 사용자가 이미 구매하거나 상호 작용한 항목을 메시징에서 재사용하지 못하도록 합니다. 추천 업데이트 사이에 구매하거나 상호작용한 항목이 계속 표시될 수 있습니다. 무료 버전의 항목 추천의 경우 매주 업데이트가 이루어집니다. AI 아이템 추천 프로 버전의 경우 24시간마다 업데이트가 이루어집니다.

예를 들어, AI 아이템 추천 프로 버전을 사용할 때 사용자가 상품을 구매한 후 30분 이내에 마케팅 이메일을 받으면 방금 구매한 아이템이 제때 이메일에서 제외되지 않을 수 있습니다. 그러나 24시간 이후에 전송된 모든 메시지에는 해당 항목이 포함되지 않습니다.

#### 3.2단계: 카탈로그 선택

아직 채워져 있지 않은 경우 이 권장 사항에서 항목을 가져올 [카탈로그를]({{site.baseurl}}/user_guide/data/activation/catalogs/) 선택합니다.

#### 3.3단계: 선택 항목 추가(선택 사항)

추천을 보다 세밀하게 제어하고 싶다면 커스텀 필터를 적용하는 [옵션을]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) 선택하세요. 선택 항목은 브랜드, 크기, 위치 등 카탈로그의 특정 열을 기준으로 권장 사항을 필터링합니다. Liquid가 포함된 선택 항목은 추천에 사용할 수 없습니다.

추천을 위해 선택된 '재고 있음' 선택의 예입니다.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
선택한 항목을 찾을 수 없는 경우 먼저 카탈로그에 설정되어 있는지 확인하세요.
{% endalert %}

### 4단계: 추천을 유도할 상호 작용을 선택합니다.

이 권장 사항을 최적화할 이벤트를 선택합니다. 이 이벤트는 일반적으로 구매이지만 아이템과의 모든 상호작용일 수도 있습니다.

최적화할 수 있습니다:

- [구매 개체를]({{site.baseurl}}/api/objects_filters/purchase_object/) 사용한 구매 이벤트
- 구매 담당자를 위한 커스텀 이벤트
- 기타 항목 상호 작용(예: 제품 보기, 클릭 또는 미디어 재생)을 담당하는 커스텀 이벤트

**커스텀 이벤트를** 선택한 경우 목록에서 이벤트를 선택합니다.

현재 이벤트 추적 방법으로 '구매 완료' 커스텀 이벤트를 선택했습니다.]({% image_buster /assets/img/item_recs_3.png %})

### 5단계: 해당 속성 이름을 선택합니다. {#property-name}

추천을 생성하려면 카탈로그에서 항목의 `id` 필드와 일치하는 고유 식별자가 있는 인터랙션 이벤트(구매 오브젝트 또는 커스텀 이벤트)의 필드를 Braze에 알려야 합니다. 잘 모르시겠어요? [요구 사항 보기](#requirements).

**속성 이름에** 이 필드를 선택합니다.

**속성 이름** 필드에는 소프트웨어 개발 키트를 통해 Braze로 전송된 필드 목록이 미리 채워집니다. 충분한 데이터가 제공되면 이러한 속성은 올바른 속성일 가능성이 높은 순서대로 순위가 매겨집니다. 카탈로그의 `id` 필드에 해당하는 것을 선택합니다.

카탈로그의 항목 ID에 해당하는 속성 이름 "purchase_item" 을 선택했습니다.]({% image_buster /assets/img/item_recs_4.png %})

#### 요구 사항 {#requirements}

숙소를 선택하기 위한 몇 가지 요구 사항이 있습니다:

- 선택한 카탈로그의 `id` 필드에 매핑해야 합니다.
- **객체 구매를 선택한 경우** `product_id` 또는 인터랙션 이벤트의 `properties` 필드여야 합니다.
- **커스텀 이벤트를 선택한 경우:** 커스텀 이벤트의 필드여야 합니다 `properties`.
- 중첩된 필드는 **속성 이름** 드롭다운에 `event_property.nested_property` 형식의 점 표기법으로 입력해야 합니다. 예를 들어, 이벤트 속성정보 `location` 내에서 중첩된 이벤트 속성정보 `district_name` 를 선택하는 경우 `location.district_name` 를 입력합니다.
- 필드는 여러 제품 배열 안에 있거나 여러 ID 배열로 끝날 수 있습니다. 두 경우 모두 각 제품 ID는 동일한 타임스탬프를 가진 별도의 순차적 이벤트로 처리됩니다.

#### 매핑 예시

다음 예제 매핑은 모두 이 샘플 카탈로그를 참조합니다:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">title</th>
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
    <td class="tg-0pky">아디다스 퍼플 사이즈 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Custom event %}

고객이 결제하기 전에 비슷한 제품을 추천할 수 있도록 커스텀 이벤트( `added_to_cart` )를 사용한다고 가정해 보겠습니다. 이벤트 `added_to_cart` 의 이벤트 속성정보는 `product_sku` 입니다.

그런 다음 `product_sku` 속성에는 샘플 카탈로그의 `id` 열에 있는 값 중 하나 이상이 포함되어야 합니다: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" 또는 "ADI-PP-10". 모든 카탈로그 항목에 이벤트가 필요한 것은 아니지만 추천 엔진이 작업할 수 있는 충분한 콘텐츠를 확보하기 위해 몇 가지 이벤트가 필요합니다.

##### 커스텀 이벤트 오브젝트 예시

이 이벤트에는 샘플 카탈로그의 첫 번째 항목과 일치하는 `"product_sku": "ADI-BL-7"` 이 있습니다.

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

##### 제품 배열이 있는 커스텀 이벤트 오브젝트 예시

이벤트 속성정보에 여러 제품이 배열로 포함된 경우 각 제품 ID는 별도의 순차적 이벤트로 처리됩니다. 이 이벤트는 `products.sku` 속성을 사용하여 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치시킬 수 있습니다.

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

##### 제품 ID 배열을 포함하는 중첩된 오브젝트가 있는 커스텀 이벤트 오브젝트 예시

제품 ID가 객체가 아닌 배열의 값인 경우 동일한 표기법을 사용할 수 있으며 각 제품 ID는 별도의 순차적 이벤트로 취급됩니다. 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치하도록 속성을 `purchase.product_skus` 으로 구성하여 다음 이벤트에서 중첩된 개체와 유연하게 결합할 수 있습니다.

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
{% tab Purchase object %}

구매가 이루어지면 구매 개체가 API를 통해 전달됩니다.

매핑 측면에서 구매 오브젝트에도 커스텀 이벤트와 유사한 로직이 적용되지만, 구매 오브젝트의 `product_id` 또는 `properties` 오브젝트의 필드 중 하나를 선택할 수 있다는 점이 다릅니다.

모든 카탈로그 항목에 이벤트가 필요한 것은 아니지만, 추천 엔진이 충분한 콘텐츠를 확보할 수 있도록 일부 이벤트는 필요합니다.

##### 제품 ID에 매핑된 구매 개체 예시

이 이벤트에는 카탈로그의 첫 번째 항목에 매핑되는 `"product_id": "ADI-BL-7` 이 있습니다.

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

##### 속성 필드에 매핑된 구매 개체 예시

이 이벤트의 속성은 `"sku": "ADI-RD-8"` 이며, 카탈로그의 두 번째 항목에 매핑됩니다.

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

### 6단계: 추천 훈련

준비가 완료되면 **추천 생성을** 선택합니다. 이 과정을 완료하는 데 10분에서 36시간까지 걸릴 수 있습니다. 추천이 성공적으로 학습되면 이메일 업데이트를 받거나 생성에 실패한 이유에 대한 설명을 받게 됩니다.

**예측** 페이지에서 추천을 찾은 다음 필요에 따라 편집하거나 보관할 수 있습니다. 추천은 매주(유료) 또는 매월(무료) 한 번씩 자동으로 재교육됩니다.