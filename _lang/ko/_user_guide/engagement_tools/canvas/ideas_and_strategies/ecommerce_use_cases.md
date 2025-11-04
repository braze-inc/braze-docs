---
nav_title: 전자상거래 사용 사례
article_title: 전자상거래 사용 사례
alias: /ecommerce_use_cases/
page_order: 4
description: "이 참고 문서에서는 이커머스 마케터를 위해 특별히 맞춤화된 몇 가지 사전 구축된 Braze 템플릿을 통해 필수 전략을 쉽게 구현할 수 있습니다."
toc_headers: h2
---

# 전자상거래 사용 사례

> Braze Canvas는 이커머스 마케터를 위해 특별히 맞춤화된 여러 가지 사전 구축 템플릿을 제공하므로 필수 전략을 쉽게 구현할 수 있습니다. 이 페이지에서는 고객 여정을 개선하는 데 사용할 수 있는 몇 가지 주요 템플릿을 제공합니다.

{% alert important %}
[전자상거래 추천 이벤트는]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 고객 성공 관리자에게 문의하세요. <br><br>새로운 Shopify 커넥터를 사용하는 경우 통합을 통해 전자상거래 추천 이벤트를 자동으로 사용할 수 있습니다.
{% endalert %}

## 캔버스 템플릿 사용

캔버스 템플릿을 사용하려면
1. **메시징** > **캔버스로** 이동합니다.
2. **캔버스 만들기** > **캔버스 템플릿 사용을** 선택합니다.
3. **Braze 템플릿** 탭에서 사용하려는 템플릿을 찾아봅니다. 템플릿의 이름을 선택하여 미리 볼 수 있습니다.
4. 사용하려는 템플릿에 대해 **템플릿 적용을** 선택합니다.<br><br>!['캔버스 템플릿' 페이지가 'Braze 템플릿' 탭으로 열리고 최근에 사용한 템플릿과 선택 가능한 Braze 템플릿 목록이 표시됩니다.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## 전자상거래 템플릿

- [중단된 탐색](#abandoned-browse)
- [방치된 장바구니](#abandoned-cart)
- [중단된 결제](#abandoned-checkout)
- [주문 확인 및 피드백 설문조사](#order-confirmation--feedback-survey)

## 중단된 탐색

제품을 탐색했지만 장바구니에 추가하거나 주문하지 않은 사용자의 참여를 유도하려면 **포기한 탐색** 템플릿을 사용하세요.

!['항목 규칙'이 확장된 '포기된 찾아보기' 캔버스 템플릿이 적용된 경우]({% image_buster /assets/img_archive/abandoned_browse.png %})

### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **버려진 찾아보기** 템플릿을 적용합니다. 

#### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항 
    - 캔버스 이름: **중단된 탐색**
    - 전환 이벤트: `ecommerce.order placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 `ecommerce.product_viewed` 이벤트를 수행할 때 액션 기반
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스의 '액션 기반 옵션']({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- 타겟 오디언스 
    - 항목 오디언스 
        - 이메일이 **비어 있지 않습니다.**
        - 비즈니스 요구 사항에 맞게 참가 대상 기준을 수정할 수도 있습니다.
    - 항목 제어
        - 사용자는 캔버스의 전체 기간이 완료된 후 이 캔버스에 다시 입장할 수 있습니다.
    - 종료 기준 
        - 수행 `ecommerce.cart_updated`, `ecommerce.checkout_started`, 또는 `ecommerce.order_placed`<br><br>![캔버스에 대한 항목 제어 및 종료 기준]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
    - 1시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

### 이메일에 대한 중단된 제품 개인화 찾아보기 

다음은 중단된 찾아보기 이메일에 HTML 제품 블록을 추가하는 방법의 예입니다. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### 제품 URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## 방치된 장바구니

**중단된 카트** 템플릿을 사용하여 장바구니에 제품을 추가했지만 결제나 주문을 계속하지 않은 고객의 잠재적인 매출 손실에 대응하세요. 

![확장된 '항목 규칙'이 적용된 '버려진 카트' 캔버스 템플릿.]({% image_buster /assets/img_archive/abandoned_cart.png %})

### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **버려진 카트** 템플릿을 적용합니다. 

#### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항 
    - 캔버스 이름: **방치된 장바구니**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 **카트 업데이트 이벤트 수행** (드롭다운에 위치)을 트리거할 때 액션 기반 트리거를 트리거합니다.
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스의 '액션 기반 옵션']({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- 타겟 오디언스 
    - 항목 오디언스 
        - 이 앱을 **0회 이상** 사용한 적이 있습니다. 
        - 이메일이 **비어 있지 않습니다.**
    - 항목 제어
        - 사용자는 즉시 캔버스 참가 자격이 다시 부여됩니다.
    - 종료 기준 
        - 수행 `ecommerce.cart_updated`, `ecommerce.checkout_started`, 또는 `ecommerce.order_placed`<br><br>![캔버스에 대한 항목 제어 및 종료 기준]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
     - 4시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

### 이메일용 버려진 장바구니 제품 개인화 {#abandoned-cart-checkout}

이탈한 카트 사용자 여정에는 제품 개인화를 위한 특별한 `shopping_cart` 리퀴드 태그가 필요합니다. 

다음은 `shopping_cart` Liquid 태그가 포함된 HTML 블록을 추가하여 이메일에 제품을 추가하는 방법의 예시입니다. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Shopify를 사용하는 경우 카탈로그 이름을 추가하여 이형 상품 이미지 URL을 가져옵니다.
{% endalert %}

#### HTML 카트 URL

사용자를 카트로 다시 안내하려면 다음과 같이 중첩된 이벤트 속성을 메데이터 객체 아래에 추가하면 됩니다:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopify를 사용하는 경우 이 Liquid 템플릿을 사용하여 카트 URL을 생성합니다:

{% raw %}
```liquid
{{context.source}}/checkouts/cn/{{context.cart_id}}
```
{% endraw %}

## 중단된 결제

**중단된 결제** 템플릿을 사용하여 결제 프로세스를 시작했지만 주문하기 전에 이탈한 고객을 타겟팅할 수 있습니다. 

![확장된 '입력 규칙'이 적용된 '중단된 결제' 캔버스 템플릿.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **중단된 결제** 템플릿을 적용합니다. 

#### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항 
    - 캔버스 이름: **중단된 결제**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 `ecommerce.checkout_started` 이벤트를 수행할 때 동작 기반 트리거
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스의 '액션 기반 옵션']({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- 타겟 오디언스 
    - 항목 오디언스 
        - 이 앱을 **0회 이상** 사용한 적이 있습니다. 
        - 이메일이 **비어 있지 않습니다.**
    - 항목 제어
        - 사용자는 즉시 캔버스 참가 자격이 다시 부여됩니다.
        - 종료 기준 
            - `ecommerce.order_placed` 이벤트 수행<br><br>![캔버스에 대한 항목 제어 및 종료 기준]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
    - 4시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

### 이메일에 대한 중단된 결제 개인 설정

결제를 포기한 사용자 여정에는 제품 개인화를 위한 특별한 `shopping_cart` 리퀴드 태그가 필요합니다. 

다음은 `shopping_cart` Liquid 태그가 포함된 HTML 블록을 추가하여 이메일에 제품을 추가하는 방법의 예시입니다. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### 결제 URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## 주문 확인 및 피드백 설문조사

**주문 확인 및 피드백 설문조사** 템플릿을 사용하여 성공적인 주문을 확인하고 고객 만족도를 높일 수 있습니다.

![확장된 '입력 규칙'이 적용된 '주문 확인' 캔버스 템플릿.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **주문 확인 및 피드백 설문조사** 템플릿을 적용합니다. 

#### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항 
    - 캔버스 이름: **피드백 설문조사를 통한 주문 확인**
    - 전환 이벤트: `ecommerce.session_start`
        - 전환 마감일: 10일 
- 진입 스케줄 
    - 사용자가 `ecommerce.cart_updated` 이벤트를 수행할 때 동작 기반 트리거
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스의 '액션 기반 옵션']({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- 타겟 오디언스 
    - 항목 오디언스 
        - 이 앱을 **0회 이상** 사용한 적이 있습니다. 
        - 이메일이 **비어 있지 않습니다.**
    - 항목 제어
        - 사용자는 즉시 캔버스 참가 자격이 다시 부여됩니다.
    - 종료 기준 
        - 해당 없음<br><br>![캔버스에 대한 추가 필터 및 항목 컨트롤.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

### 이메일 주문 확인 개인화

다음은 주문이 접수된 후 주문 확인에 HTML 제품 블록을 추가하는 방법의 예시입니다.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### 주문 상태 URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## 메시지 개인화

[Liquid는]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 고객을 위한 역동적이고 개인화된 콘텐츠를 제작할 수 있는 강력한 템플릿 언어로, Braze에서 사용합니다. Liquid 태그를 사용하면 고객 데이터, 제품 정보 및 기타 변수를 기반으로 메시지를 사용자 지정하여 쇼핑 경험을 개선하고 참여를 유도할 수 있습니다.

### Liquid의 주요 기능

- **동적 콘텐츠:** 이름, 주문 세부 정보, 기본 설정 등 고객별 정보를 메시지에 삽입하세요.
- **조건부 논리:** 특정 조건(예: 고객 위치 및 구매 내역)에 따라 다른 콘텐츠를 표시하려면 if/else 문을 사용합니다.
- **루프:** 제품 또는 고객 데이터 컬렉션을 반복하여 항목의 목록 또는 그리드를 표시합니다.

### Liquid 시작하기

Liquid 태그를 사용하여 메시지를 맞춤 설정하려면 다음 리소스를 참조하세요:

- 사전 정의된 리퀴드 태그가 포함된 [Shopify 데이터]({{site.baseurl}}/shopify_features/#shopify-data) 참조
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## 세분화

Braze 세그먼트를 사용하여 특정 속성 및 행동을 기반으로 타겟 고객 세그먼트를 생성하고 개인화된 메시지와 캠페인을 전달할 수 있습니다. 이 강력한 기능을 사용하면 적시에 적절한 메시지를 적절한 대상에게 전달하여 고객의 참여를 효과적으로 유도할 수 있습니다.

세그먼트 시작하기에 대한 자세한 내용은 [브레이즈 세그먼트 소개를]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments) 참조하세요.

### 추천 이벤트

이커머스 이벤트는 [추천 이벤트를]({{site.baseurl}}/recommended_events/) 기반으로 합니다.
추천 이벤트는 사용자 지정 이벤트이므로 [사용자 지정 이벤트 필터를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters) 선택하여 추천 이커머스 이벤트 이름을 검색할 수 있습니다.

### 전자상거래 필터

세분화 도구 내의 **전자상거래** 섹션으로 이동하여 **전자상거래 소스** 및 **총 수익과** 같은 전자상거래 필터를 사용하여 사용자를 세분화합니다.

!['전자상거래' 필터가 있는 세그먼트 필터 드롭다운]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
구매 이벤트는 결국 더 이상 사용되지 않으며 [전자상거래 추천 이벤트로]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/) 대체될 예정입니다. 이 경우 세그먼트 필터는 더 이상 구매 행동 아래에 채워지지 않습니다. 구매 이벤트의 전체 목록은 [구매 이벤트 로깅하기를]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events) 참조하세요.
{% endalert %}

## 중첩된 이벤트 속성

중첩된 이벤트 속성을 기준으로 [세그먼트하려면 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) 활용하면 됩니다. 예를 들어 세그먼트 확장을 사용하여 지난 90일 동안 'SKU-123' 제품을 구매한 사람을 찾을 수 있습니다.

## 분석

{% alert note %}
현재 Shopify 통합은 Braze [구매 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) 채우기를 지원하지 않습니다. 따라서 구매 필터, Liquid 태그, 액션 기반 트리거, 애널리틱스에서는 ecommerce.order_placed 이벤트를 사용해야 합니다.
{% endalert %}

통합을 통해 지원되는 이벤트를 수행한 사람을 기준으로 [사용자 지정 이벤트 보고서를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) 만들려면 특정 [이벤트 이름을]({{site.baseurl}}/shopify_data_features/) 지정하면 됩니다.

론칭한 캔버스에서 발생한 주문과 관련된 트렌드에 대한 인사이트를 얻으려면 [전환 대시보드를]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) 설정하고 캔버스를 지정해야 합니다.

고급 보고 사용 사례의 경우, Braze [쿼리 빌더를]({{site.baseurl}}/user_guide/analytics/query_builder/) 사용하여 사용자 지정 보고서를 생성할 수 있습니다. 

