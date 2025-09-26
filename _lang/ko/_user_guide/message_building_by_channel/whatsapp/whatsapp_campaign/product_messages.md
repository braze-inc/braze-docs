---
nav_title: 제품 메시지
article_title: 제품 메시지
page_order: 1
description: "이 페이지에서는 WhatsApp 제품 메시지를 사용하여 Meta 카탈로그의 제품을 보여주는 대화형 WhatsApp 메시지를 보내는 방법을 다룹니다."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# 제품 메시지

> 제품 메시지는 Meta 카탈로그에서 직접 제품을 보여주는 대화형 WhatsApp 메시지를 보낼 수 있도록 합니다.

{% alert important %}
WhatsApp 제품 메시지는 현재 초기 액세스 중이며 초기 액세스 기간 동안 지속적인 업데이트가 계획되어 있습니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

사용자에게 WhatsApp 제품 메시지를 보내면 사용자는 다음 고객 여정을 따릅니다:

1. 사용자는 WhatsApp에서 귀하의 제품 또는 카탈로그 메시지를 받습니다.
2. 사용자는 WhatsApp에서 직접 장바구니에 제품을 추가합니다.
3. 사용자는 WhatsApp에서 **주문하기**를 탭합니다.
4. 귀하의 웹사이트나 앱은 Braze로부터 장바구니 데이터를 수신하고 체크아웃 링크를 생성합니다.
5. 사용자는 체크아웃을 완료하기 위해 귀하의 웹사이트나 앱으로 이동합니다.

사용자가 카탈로그 메시지를 통해 장바구니에 항목을 추가하면 Braze는 후속 작업을 위한 웹훅 데이터를 수신합니다.

## 요구 사항

| 요구 사항 | 설명 |
| --- | --- |
| WhatsApp Business 계정 | WhatsApp 제품 메시지를 사용하려면 Braze와 연결된 WhatsApp 비즈니스 계정이 필요합니다. |
| Meta 카탈로그 | Commerce Manager에서 Meta 카탈로그를 설정해야 합니다. |
| 용어 준수 | [Meta 상거래 약관 및 정책](https://www.facebook.com/policies_center/commerce)을 준수하십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 제품 메시지 템플릿

{% tabs %}
{% tab 카탈로그 메시지 %}

카탈로그 메시지는 전체 제품 카탈로그를 인터랙티브 형식으로 표시합니다.

{% alert note %}
브레이즈에서 추가 제품 선택을 할 필요가 없으며, 카탈로그 연결은 메타에 의해 관리되므로 귀하의 제품 카탈로그에 상속됩니다.
{% endalert %}


{% endtab %}
{% tab 다중 제품 메시지 %}

다중 제품 메시지는 카탈로그에서 특정 제품을 강조 표시하며, 메시지당 최대 30개의 강조 항목을 포함할 수 있습니다. 현재 통합 제품 선택기가 없으므로, 제품 SKU를 얻기 위해 메타 카탈로그를 수동으로 참조해야 합니다.

{% alert important %}
메타의 다중 제품 메시지 템플릿에 알려진 헤더 표시 문제가 있습니다. 메타는 이 문제를 인지하고 있으며 수정 작업을 진행 중입니다.
{% endalert %}


{% endtab %}
{% endtabs %}

## 제품 메시지 설정하기

1. [메타 상거래 관리자](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#)에서 [메타의 지침](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1)에 따라 메타 카탈로그를 생성하세요. 브레이즈에 연결된 WhatsApp 비즈니스 계정이 있는 동일한 메타 비즈니스 포트폴리오에 있는지 확인하세요.
2. 메타 비즈니스 관리자에서 "카탈로그 관리" 권한을 할당하여 [메타 카탈로그](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715)을 브레이즈에 연결된 WhatsApp 비즈니스 계정에 연결하기 위해 메타의 지침을 따르세요. 

!["sweeney_catalog"라는 카탈로그의 "파트너 할당" 버튼을 가리키는 화살표가 있는 메타 "카탈로그" 페이지.]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:80%;"}

파트너 비즈니스 ID로 브레이즈 비즈니스 관리자 ID인 `332231937299182`을 사용해야 합니다.

![파트너 비즈니스 ID를 입력하고 "카탈로그 관리" 권한을 할당할 수 있는 필드가 포함된 카탈로그를 파트너와 공유하는 창.]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:60%;"}

{: start="3"}
3\. 메타 카탈로그 설정을 선택하세요. 카탈로그 메시지를 보내려면 **채팅 헤더에 카탈로그 아이콘 표시**를 선택해야 합니다.

!["Catalog_products" 카탈로그에 대한 WhatsApp 관리자 설정 페이지.]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:80%;"}

{: start="4"}
4\. 브레이즈에서 [임베디드 가입]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) 프로세스를 통해 권한을 제공하세요. 이것은 브레이즈 통합 제품 선택기를 잠금 해제합니다.

{% alert tip %}
메타 카탈로그를 생성할 때 따라야 할 모범 사례는 [상거래 관리자에서 고품질 카탈로그 구축을 위한 팁](https://www.facebook.com/business/help/2086567618225367?id=725943027795860)를 참조하세요.
{% endalert %}

## 제품 메시지 작성하기

1. 메타 비즈니스 매니저에서 **메시지 템플릿**으로 이동합니다.
2. 형식으로 **카탈로그**을 선택한 다음, **카탈로그 메시지** (전체 카탈로그 표시)와 **다중 제품 카탈로그 메시지** (특정 항목 강조) 중에서 선택합니다.
3. Braze에서 WhatsApp 캠페인 또는 캔버스 메시지 단계를 만듭니다.
4. 템플릿을 제출한 위치와 일치하는 구독 그룹을 선택합니다.
5. **WhatsApp 템플릿 메시지**을 선택합니다. (제품 및 카탈로그 메시지는 응답 메시지에서 아직 사용할 수 없습니다.)
6. 사용할 템플릿을 선택합니다.
    - 다중 제품 템플릿을 선택하면 강조할 제품의 섹션 제목 및 콘텐츠 ID를 제공해야 합니다.

![섹션 제목 및 콘텐츠 ID를 입력할 필드가 있는 항목 목록입니다.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

{: start="7"}
7\. 메시지 작성을 계속합니다.

## 제품 관리하기

### 상거래 관리자에 접근하기

메타 비즈니스 매니저에서 **상거래 관리자**로 이동하여 조직을 선택합니다. 여기에서 다음과 같은 카탈로그 자산을 관리할 수 있습니다:
- 새 카탈로그 만들기
- 기존 카탈로그에 제품 추가하기
- 제품 정보 업데이트하기
- 단종된 항목 제거하기

{% alert important %}
카탈로그에서 참조된 제품을 제거하면 관련 메시지가 전송되지 않습니다.
{% endalert %}

## 결제: 장바구니 처리 및 웹후크

사용자가 WhatsApp 제품 메시지와 상호작용할 때, 제품을 탐색하고 장바구니에 항목을 추가할 수 있습니다. 그러나 현재 배송 정보나 결제 처리를 위한 내장 결제 기능은 없습니다. 대신, 귀하의 앱이나 웹사이트 내에서 장바구니를 생성하고 사용자에게 사용자 정의 링크를 사용하여 해당 장바구니로 안내할 것을 권장합니다.

### 고려 사항

- **앱 내 결제 없음:** 사용자는 WhatsApp 내에서 직접 구매를 완료할 수 없습니다. 모든 거래는 귀하의 웹사이트나 앱으로 리디렉션되어야 합니다.
- **사용자 정의 링크 필요:** 사용자를 귀하의 플랫폼에서 장바구니로 안내하는 사용자 정의 링크를 생성해야 합니다.
- **수동 설정:** 설정 과정은 귀하의 장바구니 및 메시징 워크플로우의 수동 구성을 요구합니다.

{% alert note %}
현재 WhatsApp 내에서 직접 결제를 지원하지 않으며, 향후 지원은 국가별로 제공될 것입니다(현재 Meta는 인도, 브라질 및 싱가포르에 본사를 두고 사용자와 직접 작업하는 회사에만 제공합니다).
{% endalert %}

### 장바구니 이벤트 트리거 설정

고객이 WhatsApp에서 주문을 할 때, Braze는 자동으로:
1. WhatsApp에서 장바구니 내용을 수신합니다(제품 ID, 수량 및 기타 주문 데이터).
2. 모든 관련 데이터를 포함한 `ecommerce.cart_update` 전자상거래 이벤트를 생성합니다, `source = whats_app`를 포함하여.
3. 응답을 트리거하여 주문에 응답하는 자동화 캠페인을 설정할 수 있습니다.

`ecommerce.cart_update` 전자상거래 이벤트는 이벤트가 전송된 후에만 Braze에 나열되며, 이는 Braze에서 테스트 제품 메시지를 생성하고 장바구니 이벤트를 제출하여 수행할 수 있습니다.
장바구니 이벤트에는 다음이 포함됩니다:

- **장바구니 ID:** 장바구니의 고유 식별자
- **제품:** 제품 ID, 수량 및 가격이 포함된 항목 목록
- **총 가치:** 모든 항목의 합계
- **통화:** 장바구니의 통화
- **소스:** "whats_app"으로 표시됨
- **메타데이터:** 카탈로그 ID 및 메시지 텍스트와 같은 추가 데이터

추가 Braze 장바구니 이벤트 정보를 [추천 전자상거래 이벤트 유형]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events)에서 찾을 수 있습니다.

### 트리거된 응답 설정

1. `ecommerce.cart_updated`에 대한 커스텀 이벤트 트리거 생성.
2. `source = "whats_app"`에 대한 속성 필터 추가.

![의 기본 속성 "source"가 `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})와 같아지는 `ecommerce.cart_updated` 커스텀 이벤트 트리거를 위한 캔버스 단계

{: start="3"}
3\. 장바구니 데이터에 따라 후속 작업 구성.

### 추천 체크아웃 구현 

{% tabs %}
{% tab 간단한 Liquid 기반 장바구니 링크 %}

Liquid를 사용하여 응답 메시지에서 직접 장바구니 URL을 구축하십시오. WhatsApp와 전자상거래 플랫폼 간에 일관된 제품 ID가 있는 경우 가장 좋습니다.

#### 예제 Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### 설정

1. `ecommerce.cart_update` 전자상거래 이벤트의 트리거로 WhatsApp 응답 메시지 캠페인을 만듭니다.
2. 장바구니 URL로 후속 메시지를 만듭니다.
3. Liquid로 장바구니 URL을 구축합니다. Shopify를 사용하는 경우 이전 예제 Liquid로 [장바구니 영구 링크](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks)를 만들 수 있습니다.

![Liquid로 생성된 장바구니의 체크아웃 경험 워크플로우를 보여주는 다이어그램: Meta는 Braze에 주문 수신 메시지를 보내고, 이는 행동 기반 트리거를 발생시킨 후 장바구니 링크가 포함된 메시지를 생성하여 WhatsApp 메시지를 보냅니다.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab 연결된 콘텐츠 %}

개인화된 체크아웃 URL을 생성하기 위해 전자상거래 시스템에 API 호출을 합니다. 동적 장바구니 URL 생성 또는 복잡한 제품 매핑이 필요한 경우 가장 좋습니다.

#### 설정

1. [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) 전자상거래 이벤트에 의해 트리거되는 웹훅 캠페인 또는 캔버스 단계를 생성하여 장바구니 데이터를 전자상거래 시스템으로 보냅니다.
2. 같은 전자상거래 이벤트에 의해 트리거되는 WhatsApp 캠페인 또는 캔버스 메시지 단계를 생성하여 사용자에게 장바구니 URL이 포함된 WhatsApp 응답 메시지를 보냅니다. 후속 응답 메시지의 지침을 따라 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)를 사용합니다.

![연결된 콘텐츠 호출에 대한 체크아웃 경험 워크플로우를 보여주는 다이어그램: Meta는 Braze에 주문 수신 메시지를 보내고, 이는 전자상거래 플랫폼과의 상호 호출을 수행한 후 WhatsApp 메시지를 보냅니다.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab 웹훅 및 커스텀 이벤트 %}

웹훅을 사용하여 장바구니 데이터를 시스템으로 보내고, 커스텀 이벤트를 통해 후속 메시지를 트리거합니다. 복잡한 장바구니 처리 또는 다단계 워크플로우가 필요한 복잡한 통합에 가장 좋습니다.

#### 설정

`ecommerce.cart_update` eCommerce 이벤트에 의해 트리거되는 웹훅 캠페인 또는 캔버스 단계를 생성하여 장바구니 데이터를 귀하의 eCommerce 시스템으로 전송합니다. 귀하의 API는 다음과 같이 진행됩니다:
1. 장바구니 데이터를 수신합니다.
2. 귀하의 시스템에 장바구니를 생성합니다.
3. 체크아웃 URL을 생성합니다.
4. 체크아웃 링크와 함께 WhatsApp 메시지를 전송하도록 Braze에 `checkout_started` 이벤트를 보냅니다.

![웹훅 및 커스텀 이벤트에 대한 체크아웃 경험 워크플로우를 보여주는 다이어그램: Meta는 Braze에 주문 수신 메시지를 보내고, Braze는 eCommerce 플랫폼과 상호 호출을 하며, 이후 장바구니 URL과 함께 WhatsApp 메시지를 보냅니다.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## 테스트 및 검증

### 테스트 메시지 요구 사항

장바구니 기능은 테스트 메시지 간에 유지되지만, 수신 결과의 처리는 유지되지 않습니다.

### 메시지 미리보기

- 제품 이미지 및 세부정보는 귀하의 Meta 카탈로그에서 가져옵니다.
- 통합이 완료될 때까지 대화형 미리보기는 자리 표시자를 표시합니다.

### 오류 코드 

- 제품 ID가 카탈로그에 존재하지 않으면 오류 `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`를 받게 됩니다.
- 카탈로그가 WABA와 연결되지 않으면 오류 `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`를 받게 됩니다.
