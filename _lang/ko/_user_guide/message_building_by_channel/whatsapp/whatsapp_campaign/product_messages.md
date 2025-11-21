---
nav_title: 제품 메시지
article_title: 제품 메시지
page_order: 2
description: "이 페이지에서는 WhatsApp 제품 메시지를 사용하여 메타 카탈로그의 제품을 소개하는 대화형 WhatsApp 메시지를 보내는 방법에 대해 설명합니다."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# 제품 메시지

> 제품 메시지를 사용하면 메타 카탈로그에서 바로 제품을 소개하는 대화형 WhatsApp 메시지를 보낼 수 있습니다.

사용자에게 WhatsApp 제품 메시지를 보내면 사용자는 다음과 같은 고객 여정을 진행하게 됩니다:

1. 사용자는 WhatsApp에서 제품 또는 카탈로그 메시지를 수신합니다.
2. 사용자가 WhatsApp에서 직접 장바구니에 제품을 추가합니다.
3. 사용자가 WhatsApp에서 **주문하기를** 탭합니다.
4. 웹사이트나 앱은 Braze로부터 카트 데이터를 수신하고 결제 링크를 생성합니다.
5. 사용자는 결제를 완료하기 위해 웹사이트 또는 앱으로 이동합니다.

사용자가 카탈로그 메시지를 통해 장바구니에 상품을 추가하면 Braze는 후속 조치를 위해 웹훅 데이터를 수신합니다.

## 요구 사항

| 요구 사항 | 설명 |
| --- | --- |
| WhatsApp 비즈니스 계정 | WhatsApp 제품 메시지를 사용하려면 Braze와 연결된 WhatsApp 비즈니스 계정이 있어야 합니다. |
| 메타 카탈로그 | 커머스 매니저에서 메타 카탈로그를 설정해야 합니다. |
| 기간 준수 | [메타 커머스 약관 및 정책을](https://www.facebook.com/policies_center/commerce) 준수합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 제품 메시지 유형

{% alert note %}
[제품 메시지 설정](#setting-up-product-messages) 4단계에서 액세스할 수 있는 통합 제품 선택기를 사용하여 제품 메시지 경험을 향상하세요.
{% endalert %}

{% tabs local %}
{% tab Catalog messages %}

카탈로그 메시지는 전체 제품 카탈로그를 대화형 형식으로 표시합니다. [템플릿 및 응답 메시지로](#building-a-product-message) 사용할 수 있습니다.

[설정](#setting-up-product-messages) 중에 Braze에 카탈로그 권한을 인에이블먼트한 경우 사용자에게 표시할 썸네일을 선택할 수 있습니다. 

{% alert note %}
카탈로그 연결은 Meta에서 관리하므로 제품 카탈로그에 상속되므로 Braze에서 추가로 제품을 선택할 필요가 없습니다.
{% endalert %}


{% endtab %}
{% tab Multi-product messages %}

다중 제품 메시지는 카탈로그의 특정 제품을 강조 표시하며 메시지당 최대 30개까지 강조 표시할 수 있습니다. [템플릿 및 응답 메시지로](#building-a-product-message) 사용할 수 있습니다.

ID를 사용하여 제품을 수동으로 선택하거나 [설정](#setting-up-product-messages) 중에 카탈로그 권한을 인에이블먼트한 경우 드롭다운 제품 선택기를 사용할 수 있습니다.

{% alert important %}
메타에서 여러 제품 메시지 템플릿의 헤더 표시 문제가 알려져 있습니다. 메타에서 이 문제를 인지하고 수정 작업을 진행 중입니다.
{% endalert %}

{% endtab %}
{% tab Single product %}

단일 제품 메시지는 제품 카탈로그에서 특정 제품 하나를 강조 표시합니다. [응답 메시지로](#building-a-product-message) 사용할 수 있습니다.

ID를 사용하여 제품을 수동으로 선택하거나 [설정](#setting-up-product-messages) 중에 카탈로그 권한을 인에이블먼트한 경우 드롭다운 제품 선택기를 사용할 수 있습니다.

{% endtab %}
{% endtabs %}

## 제품 메시지 설정하기

1. [메타 커머스 매니저에서](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#) [메타의 지침에](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) 따라 메타 카탈로그를 생성합니다. Braze에 연결된 WhatsApp 비즈니스 계정과 동일한 메타 비즈니스 포트폴리오에 있는지 확인하세요.
2. 메타 비즈니스 매니저에서 "카탈로그 관리" 권한을 할당하여 [메타 카탈로그를](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) Braze에 연결된 WhatsApp 비즈니스 계정에 [연결하려면](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) 메타의 지침을 따르세요. 

메타 "카탈로그" 페이지에 "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}라는 카탈로그의 "파트너 할당" 버튼을 가리키는 화살표가 표시됨){: style="max-width:90%;"}

파트너 비즈니스 ID로 Braze 비즈니스 매니저 ID( `332231937299182`)를 사용해야 합니다.

파트너 비즈니스 ID를 입력하고 '카탈로그 관리' 권한을 할당할 수 있는 필드가 포함된 카탈로그를 파트너와 공유하는 창입니다.]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3\. 메타 카탈로그 설정을 선택합니다. 카탈로그 메시지를 보내려면 **채팅 헤더에 카탈로그 아이콘 표시를** 선택해야 합니다.

"Catalog_products" 카탈로그의 WhatsApp 매니저 설정 페이지로 이동합니다.]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Braze에서 [임베드된 가입]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) 절차를 거쳐 권한을 제공합니다. 권한을 제공하려는 **모든** 카탈로그를 선택해야 합니다. 그러면 Braze 통합 제품 선택기가 잠금 해제됩니다.

5개의 카탈로그가 선택된 창에서 권한을 제공합니다.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
메타 카탈로그를 생성할 때 따라야 할 모범 사례는 [커머스 매니저에서 고품질 카탈로그 구축을 위한 팁을](https://www.facebook.com/business/help/2086567618225367?id=725943027795860) 참조하세요.
{% endalert %}

## 제품 메시지 구축하기

WhatsApp 템플릿 메시지 또는 응답 메시지를 사용하여 제품 메시지를 구축할 수 있습니다.

{% tabs local %}
{% tab WhatsApp message template %}

1. 메타 비즈니스 매니저에서 **메시지 템플릿으로** 이동합니다.
2. **카탈로그를** 형식으로 선택한 다음 **카탈로그 메시지** (전체 카탈로그 표시)와 **다중 제품 카탈로그 메시지** (특정 항목 강조 표시) 중에서 선택합니다.
3. Braze에서 WhatsApp 캠페인 또는 캔버스 메시지 단계를 만듭니다.
4. 템플릿을 제출한 위치와 일치하는 구독 그룹을 선택합니다.
5. **WhatsApp 템플릿 메시지를** 선택합니다.
6. 사용하려는 템플릿을 선택합니다.
    - 여러 제품 템플릿을 선택하는 경우 강조 표시할 제품의 섹션 제목과 콘텐츠 ID를 입력합니다. 메타 커머스 매니저에서 직접 콘텐츠 ID를 복사하거나 통합 제품 선택기에 대한 권한을 인에이블먼트한 경우 항목을 선택할 수 있습니다.

섹션 제목과 콘텐츠 ID를 입력할 수 있는 필드가 있는 항목 목록입니다.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

선택할 수 있는 항목 드롭다운이 있는 항목 목록입니다.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7\. 메시징을 계속 구축하세요.

{% endtab %}
{% tab Response message %}

1. Braze에서 WhatsApp 캠페인 또는 캔버스 메시지 단계를 만듭니다.
2. 구독 그룹을 선택합니다.
3. **응답 메시지를** 선택합니다.
4. **메타 제품 메시지를** 선택합니다.

"응답 메시지" 및 "메타 제품 메시지"가 강조 표시된 메시지 유형 및 응답 메시지 레이아웃을 선택하는 옵션입니다.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5\. 사용하려는 [메시지 유형을](#product-message-types) 선택합니다.

!"멀티 제품"의 메사지 레이아웃 선택.]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6\. 메시징을 계속 구축하세요.

제품에 대한 정보가 입력된 메타 제품 메시지 예시.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## 제품 관리하기

### 커머스 매니저 액세스하기

메타 비즈니스 매니저에서 **커머스 매니저로** 이동하여 조직을 선택합니다. 여기에서 다음과 같은 카탈로그 자산을 관리할 수 있습니다:
- 새 카탈로그 만들기
- 기존 카탈로그에 제품 추가하기
- 제품 정보 업데이트
- 단종된 품목 제거

{% alert important %}
카탈로그에서 참조된 제품을 제거하면 관련 메시지를 전송하지 못합니다.
{% endalert %}

## 인바운드 제품 문의 받기 

사용자는 제품 또는 카탈로그 메시지에 제품 관련 질문으로 응답할 수 있습니다. 이러한 메시지는 인바운드 메시지로 도착하며, [행동 경로를]({{site.baseurl}}/action_paths/) 사용하여 정렬할 수 있습니다. 

또한 Braze는 이러한 질문에서 제품 ID와 카탈로그 ID를 추출하므로 응답을 자동화하거나 다른 팀(예: 고객 지원팀)에 질문을 보내려는 경우 이러한 세부 정보를 포함할 수 있습니다. 예를 들어 `inbound_product_id` 또는 `inbound_catalog_id` 의 WhatsApp 속성을 사용하여 응답을 개인화할 수 있습니다.

개인화 유형이 "WhatsApp 속성"이고 강조 표시된 속성이 "inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}인 "개인화 추가" 창이 나타납니다.{: style="max-width:60%;"}

## 결제: 카트 처리 및 웹훅

사용자가 WhatsApp 제품 메시지와 상호 작용할 때 제품을 탐색하고 장바구니에 항목을 추가할 수 있습니다. 그러나 현재 배송 정보나 결제 처리를 위한 결제 기능이 구축되어 있지 않습니다. 대신 자체 앱이나 웹사이트 내에 카트를 생성하고 커스텀 링크를 사용하여 사용자를 해당 카트로 안내하는 것이 좋습니다.

### 고려 사항

- **앱 내 결제가 없습니다:** 사용자는 WhatsApp 내에서 직접 구매를 완료할 수 없습니다. 모든 트랜잭션은 웹사이트 또는 앱으로 리디렉션되어야 합니다.
- **커스텀 링크가 필요합니다:** 사용자를 플랫폼의 카트로 안내하는 커스텀 링크를 만들어야 합니다.
- **수동 설정:** 설정 프로세스에서는 카트 및 메시징 워크플로우를 수동으로 구성해야 합니다.

{% alert note %}
현재 WhatsApp에서 직접 발생하는 결제는 지원하지 않으며, 향후에는 국가별로 지원될 예정입니다(현재 메타는 인도, 브라질, 싱가포르에 기반을 두고 사용자와 직접 협력하는 기업에게만 해당 기능을 제공하고 있습니다).
{% endalert %}

### 카트 이벤트 트리거 설정하기

고객이 WhatsApp에서 주문을 하면 자동으로 Braze가 실행됩니다:
1. WhatsApp에서 카트 내용(제품 ID, 수량 및 기타 주문 데이터)을 수신합니다.
2. `source = whats_app` 을 포함한 모든 관련 데이터가 포함된 `ecommerce.cart_update` 이커머스 이벤트를 생성합니다.
3. 응답을 트리거하여 주문에 응답하도록 자동화된 캠페인을 설정할 수 있습니다.

`ecommerce.cart_update` 이커머스 이벤트는 이벤트가 전송된 후에만 Braze에 표시되며, 이는 Braze에서 테스트 제품 메시지를 생성하고 장바구니 이벤트를 제출하여 수행할 수 있습니다.
장바구니 이벤트에는 다음이 포함됩니다:

- **카트 ID:** 카트의 고유 식별자
- **제품:** 제품 ID, 수량 및 가격이 포함된 품목 목록
- **총 가치:** 모든 항목의 합계
- **통화:** 카트의 통화
- **출처:** 로 표시 "whats_app"
- **메타데이터:** 카탈로그 ID 및 메시지 텍스트와 같은 추가 데이터

[이커머스 추천 이벤트 유형에서]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events) 추가 Braze 카트 이벤트 정보를 확인할 수 있습니다.

### 트리거된 응답 설정하기

1. `ecommerce.cart_updated` 에 대한 커스텀 이벤트 트리거를 생성합니다.
2. `source = "whats_app"` 에 대한 속성 필터를 추가합니다.

\![기본 속성이 `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %}와 동일한 "source"인 `ecommerce.cart_updated` 커스텀 이벤트 트리거의 캔버스 단계)

{: start="3"}
3\. 카트 데이터를 기반으로 후속 조치를 구성합니다.

### 권장 결제 구현 

{% tabs local %}
{% tab Simple Liquid-based cart links %}

Liquid를 사용하여 응답 메시징에 바로 카트 URL을 구축하세요. WhatsApp과 전자상거래 플랫폼 간에 일관된 제품 ID를 사용하는 것이 가장 좋습니다.

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

1. `ecommerce.cart_update` 이커머스 이벤트를 트리거로 WhatsApp 응답 메시지 캠페인을 만듭니다.
2. 카트 URL로 후속 메시지를 생성합니다.
3. Liquid로 카트 URL을 구축하세요. Shopify를 사용하는 경우 이전 예제 Liquid를 사용하여 [카트 퍼머링크를 생성할](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) 수 있습니다.

Liquid 생성 카트에 대한 결제 환경 워크플로우를 보여주는 다이어그램: Meta는 주문 수신 메시지를 Braze에 전송하고, 이 메시지는 액션 기반 트리거를 트리거한 다음 장바구니 링크가 포함된 메시지를 생성하여 WhatsApp 메시지를 전송합니다.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

이커머스 시스템에 API를 호출하여 개인화된 결제 URL을 생성합니다. 동적 카트 URL 생성이나 복잡한 제품 매핑이 필요한 경우에 가장 적합합니다.

#### 설정

1. 웹훅 캠페인이나 캔버스 단계가 트리거되는 웹훅 캠페인을 생성하여 [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) 이벤트에 의해 트리거되는 웹훅 캠페인 또는 캔버스 단계를 생성하여 카트 데이터를 전자상거래 시스템으로 전송합니다.
2. 동일한 전자상거래 이벤트에 의해 트리거된 WhatsApp 캠페인 또는 캔버스 메시지 단계를 생성하여 사용자에게 장바구니 URL이 포함된 WhatsApp 응답 메시지를 전송합니다. 이후 응답 메시지의 안내에 따라 [연결된 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 사용합니다.

연결된 콘텐츠 호출에 대한 결제 환경 워크플로우를 보여주는 다이어그램입니다: Meta는 주문 수신 메시지를 이커머스 플랫폼과 주고받는 통화 기능이 있는 Braze에 보낸 다음 WhatsApp 메시지를 보냅니다.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook and custom events %}

웹훅을 사용하여 카트 데이터를 시스템으로 전송한 다음 커스텀 이벤트를 통해 후속 메시지를 트리거할 수 있습니다. 광범위한 카트 처리 또는 다단계 워크플로우가 필요한 복잡한 통합에 가장 적합합니다.

#### 설정

`ecommerce.cart_update` 전자상거래 이벤트에 의해 트리거되는 웹훅 캠페인 또는 캔버스 단계를 생성하여 카트 데이터를 전자상거래 시스템으로 전송합니다. 그러면 API가 작동합니다:
1. 장바구니 데이터 수신
2. 시스템에서 카트 만들기
3. 결제 URL 생성
4. Braze에 `checkout_started` 이벤트를 전송하여 결제 링크가 포함된 WhatsApp 메시지를 트리거합니다.

웹훅 및 커스텀 이벤트에 대한 결제 경험 워크플로우를 보여주는 다이어그램: Meta는 이커머스 플랫폼과 주고받는 통화가 있는 Braze에 주문 수신 메시지를 전송한 다음 장바구니 URL이 포함된 WhatsApp 메시지를 보냅니다.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## 테스트 및 유효성 검사

### 테스트 메시지 요구 사항

카트 기능은 테스트 메시지 간에 이월되지만 인바운드 결과 처리는 이월되지 않습니다.

### 메시지 미리 보기

- 메타 카탈로그에서 제품 이미지와 세부 정보를 가져옵니다.
- 통합이 완료될 때까지 대화형 미리 보기에 입력 안내가 표시됩니다.

### 오류 코드 

- 카탈로그에 제품 ID가 없는 경우 `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359` 라는 오류가 표시됩니다.
- 카탈로그가 WABA에서 연결이 끊어지면 `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings` 이라는 오류가 표시됩니다.
