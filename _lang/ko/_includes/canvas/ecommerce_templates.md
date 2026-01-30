{% tabs %}
{% tab Abandoned browse %}

### 버려진 탐색

제품을 탐색했지만 장바구니에 추가하거나 주문하지 않은 사용자의 참여를 유도하려면 **포기한 탐색** 템플릿을 사용하세요.

!['항목 규칙'이 확장된 '포기된 찾아보기' 캔버스 템플릿이 적용되었습니다.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **버려진 찾아보기** 템플릿을 적용합니다. 

##### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항 
    - 캔버스 이름: **중단된 탐색**
    - 전환 이벤트: `ecommerce.order placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 `ecommerce.product_viewed` 이벤트를 수행할 때 액션 기반
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스에 대한 '액션 기반 옵션'.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- 타겟 오디언스 
    - 항목 오디언스 
        - 이메일이 **비어 있지 않습니다.**
        - 비즈니스 요구 사항에 맞게 참가 대상 기준을 수정할 수도 있습니다.
    - 항목 제어
        - 사용자는 캔버스의 전체 기간이 완료된 후 이 캔버스에 다시 입장할 수 있습니다.
    - 종료 기준 
        - 수행 `ecommerce.cart_updated`, `ecommerce.checkout_started`, 또는 `ecommerce.order_placed`<br><br>![캔버스에 대한 항목 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
    - 1시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

#### 이메일에 대한 중단된 제품 개인화 찾아보기 

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

##### 제품 URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### 방치된 장바구니

**중단된 카트** 템플릿을 사용하여 장바구니에 제품을 추가했지만 결제나 주문을 계속하지 않은 고객의 잠재적인 매출 손실에 대응하세요. 

!["항목 규칙"이 확장된 "유기한 장바구니" 캔버스 템플릿이 적용됩니다.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **버려진 카트** 템플릿을 적용합니다. 

##### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:
- 기본 사항 
    - 캔버스 이름: **방치된 장바구니**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 **카트 업데이트 이벤트 수행** (드롭다운에 위치)을 트리거할 때 액션 기반 트리거를 트리거합니다.
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스에 대한 '액션 기반 옵션'.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- 타겟 오디언스 
    - 항목 오디언스 
        - 이 앱을 **0회 이상** 사용한 적이 있습니다. 
        - 이메일이 **비어 있지 않습니다.**
    - 항목 제어
        - 사용자는 즉시 캔버스 참가 자격이 다시 부여됩니다.
    - 종료 기준 
        - 수행 `ecommerce.cart_updated`, `ecommerce.checkout_started`, 또는 `ecommerce.order_placed`<br><br>![캔버스에 대한 항목 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
     - 4시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

#### 유기한 장바구니 재입장 로직의 작동 방식

사용자가 결제 프로세스를 시작하면 장바구니가 `checkout_started` 로 표시됩니다. 그 시점부터 동일한 장바구니 ID로 장바구니를 추가로 업데이트해도 사용자는 유기한 장바구니 사용자 여정에 다시 참여할 수 없습니다.

1. 사용자가 장바구니에 아이템을 추가하면 캔버스에 들어갑니다.
2. 아이템을 추가하거나 업데이트할 때마다 캔버스에 다시 들어가면 카트 데이터와 메시징이 최신 상태로 유지됩니다.
3. 사용자가 결제 프로세스를 시작하면 카트에 `checkout_started` 라는 태그가 지정되고 캔버스를 종료합니다.
4. 이 카트는 이미 결제 단계로 이동했기 때문에 향후 동일한 카트 ID를 사용하여 카트를 업데이트해도 재입장 트리거가 발생하지 않습니다.

사용자가 결제 사용자 여정으로 이동하면 구매 여정에서 더 높은 단계에 있는 사용자를 위해 설계된 [결제 포기 캔버스를](#abandoned-checkout) 통해 타겟팅됩니다.

#### 이메일용 버려진 장바구니 제품 개인화 {#abandoned-cart-checkout}

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

##### HTML 카트 URL

사용자를 카트로 다시 안내하려면 메타데이터 객체 아래에 다음과 같이 중첩된 이벤트 속성정보를 추가하면 됩니다:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopify를 사용하는 경우 이 Liquid 템플릿을 사용하여 카트 URL을 생성합니다:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### 중단된 결제

**중단된 결제** 템플릿을 사용하여 결제 프로세스를 시작했지만 주문하기 전에 이탈한 고객을 타겟팅할 수 있습니다. 

![확장된 "입력 규칙"이 적용된 "중단된 결제" 캔버스 템플릿.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택한 다음 **중단된 결제** 템플릿을 적용합니다. 

##### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항 
    - 캔버스 이름: **중단된 결제**
    - 전환 이벤트: `ecommerce.order_placed`
        - 전환 마감일: 3일 
- 진입 스케줄 
    - 사용자가 `ecommerce.checkout_started` 이벤트를 수행할 때 동작 기반 트리거
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스에 대한 '액션 기반 옵션'.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- 타겟 오디언스 
    - 항목 오디언스 
        - 이 앱을 **0회 이상** 사용한 적이 있습니다. 
        - 이메일이 **비어 있지 않습니다.**
    - 항목 제어
        - 사용자는 즉시 캔버스 참가 자격이 다시 부여됩니다.
        - 종료 기준 
            - `ecommerce.order_placed` 이벤트 수행<br><br>![캔버스에 대한 항목 제어 및 종료 기준.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 보내기 설정 
    - 구독 또는 옵트인한 사용자 
- 지연 단계
    - 4시간 지연
- 메시지 단계 
    - 이메일 템플릿과 HTML 블록을 Liquid 템플릿 예시와 함께 검토하여 미리 작성된 템플릿에서 메시지에 제품을 추가하세요. 자체 이메일 템플릿을 사용하는 경우 다음 섹션에서 설명하는 것처럼 [Liquid 변수를](#message-personalization) 참조할 수도 있습니다.

#### 이메일에 대한 중단된 결제 개인 설정

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

##### 결제 URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### 주문 확인 및 피드백 설문조사

**주문 확인 & 피드백 설문조사** 템플릿을 사용하여 성공적인 주문을 확인하고 고객 만족도를 높일 수 있습니다.

!['입력 규칙'이 확장된 '주문 확인' 캔버스 템플릿이 적용됩니다.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### 설정

캔버스 페이지에서 **캔버스 템플릿 사용** > **Braze 템플릿을** 선택한 다음 **주문 확인 & 피드백 설문조사** 템플릿을 적용합니다. 

##### 기본 설정

캔버스에는 다음 설정이 미리 구성되어 있습니다:

- 기본 사항 
    - 캔버스 이름: **피드백 설문조사를 통한 주문 확인**
    - 전환 이벤트: `ecommerce.session_start`
        - 전환 마감일: 10일 
- 진입 스케줄 
    - 사용자가 `ecommerce.cart_updated` 이벤트를 수행할 때 동작 기반 트리거
    - 시작 시간은 캔버스 템플릿을 생성할 때입니다.<br><br>!["캔버스에 대한 '액션 기반 옵션'.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
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

#### 이메일 주문 확인 개인화

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

##### 주문 상태 URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}