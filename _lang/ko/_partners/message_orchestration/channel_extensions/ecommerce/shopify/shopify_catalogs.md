---
nav_title: Shopify 제품 동기화
article_title: Shopify 제품 동기화
alias: /shopify_catalogs/
page_order: 4
description: "이 참조 문서에서는 Shopify에서 Braze 카탈로그로 제품을 가져오는 방법을 다룹니다."
---

# Shopify 제품 동기화 

> Shopify 스토어의 모든 제품을 Braze [카탈로그에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) 동기화하여 보다 심층적인 메시징 개인화를 수행할 수 있습니다. 

Shopify 스토어에서 제품을 편집하고 변경하면 Shopify 카탈로그가 거의 실시간으로 업데이트됩니다. 유기한 장바구니, 주문 확인 등을 최신 제품 세부 정보 및 정보로 보강할 수 있습니다.

## Shopify 제품 동기화 설정 {#setting-up}

이미 Shopify 스토어를 설치한 경우에도 아래 지침에 따라 제품을 동기화할 수 있습니다. 

### 1단계: 동기화 켜기

Shopify 설치 플로우 또는 Shopify 파트너 페이지를 통해 제품을 Braze 카탈로그에 동기화할 수 있습니다. 

!['Shopify 배리언트 ID'가 '카탈로그 제품 식별자'인 설정 프로세스의 3단계.][1]{: style="max-width:70%;"}

Braze 카탈로그에 동기화된 제품은 [카탈로그 한도에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) 영향을 미칩니다.

### 2단계: 제품 식별자 선택

카탈로그 ID로 사용할 제품 식별자를 선택합니다:
- Shopify 배리언트 ID
- SKU

선택한 제품 식별자의 ID 및 헤더 값에는 문자, 숫자, 하이픈, 밑줄만 포함할 수 있습니다. 제품 식별자가 이 형식을 따르지 않는 경우 Braze는 카탈로그 동기화에서 해당 제품 식별자를 필터링합니다.

이것은 Braze 카탈로그 정보를 참조하는 데 사용하는 기본 식별자입니다. 

{% alert note %}
SKU를 카탈로그 ID로 선택하는 경우 스토어의 모든 제품 및 이형 상품에 SKU가 설정되어 있고 고유한지 확인합니다. 
- 품목에 누락된 SKU가 있는 경우 Braze는 해당 제품을 카탈로그에 동기화할 수 없습니다. 
- 동일한 SKU를 가진 제품이 두 개 이상 있는 경우 예기치 않은 동작이 발생하거나 중복된 SKU로 인해 제품 정보가 의도치 않게 재정의될 수 있습니다.
{% endalert %}

### 3단계: 동기화 진행 중

대시보드 알림을 받게 되며, 상태가 '진행 중'으로 표시되어 초기 동기화가 시작되었음을 알 수 있습니다. 동기화가 완료되는 데 걸리는 시간은 Shopify에서 동기화해야 하는 제품 및 배리언트 수에 따라 달라집니다. 이 시간 동안 이 페이지를 떠나 완료 시점을 알리는 대시보드 알림 또는 이메일을 기다릴 수 있습니다.

초기 동기화가 [카탈로그 한도를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) 초과하면 Braze는 더 이상 제품 동기화를 중지합니다. 시간이 경과하며 추가된 새로운 제품 때문에 동기화에 성공한 후 제한을 초과하면 동기화가 더 이상 활성화되지 않습니다. 이 두 가지 경우 Shopify의 제품 업데이트는 더 이상 Braze에 반영되지 않습니다. 계정 관리자에게 문의하여 티어 업그레이드를 고려하세요. 

### 4단계: 동기화 완료

동기화에 성공하면 대시보드 알림과 이메일을 받게 됩니다. Shopify 파트너 페이지의 Shopify 카탈로그 아래 상태도 "동기화 중"으로 업데이트됩니다. Shopify 파트너 페이지에서 카탈로그 이름을 클릭하여 제품을 확인할 수 있습니다.

카탈로그 데이터를 활용하여 메시지를 개인화하는 방법에 대해 자세히 알아보려면 [카탈로그 추가 사용 사례]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)를 참조하세요.

#### 지원되는 Shopify 카탈로그 데이터

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `body_html`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
어떤 식으로든 Shopify 카탈로그를 수정하면 의도치 않게 실시간 제품 동기화를 방해할 수 있습니다. Shopify 카탈로그는 Shopify에서 재정의할 수 있으므로 편집하지 마십시오. 대신 Shopify 인스턴스에서 필요한 제품 업데이트를 수행합니다.<br><br>Shopify 카탈로그를 삭제하려면 Shopify 페이지로 이동하여 동기화를 비활성화합니다. 카탈로그 페이지에서 직접 Shopify 카탈로그를 삭제하지 마십시오.
{% endalert %}

##### `product_handle` 또는 `product_url`

`product_handle` 및 `product_url` 에 액세스하여 사용하려면 다음을 수행하여 Shopify 카탈로그 연결을 끊었다가 다시 연결합니다.

1. Shopify 통합 페이지로 이동하여 **구성 편집을** 선택합니다.

![Shopify 통합 페이지]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\. **카탈로그 동기화** 단계에서 카탈로그를 끄고 설정을 업데이트합니다.
3\. 카탈로그를 켜고 설정을 업데이트합니다.

![Shopify "카탈로그 동기화" 단계와 카탈로그 토글.]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## 재고 소진 및 가격 인하 사용 사례

품절 알림을 설정하려면 [여기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications) 단계를 따르세요.

가격 인하 알림을 설정하려면 [여기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) 단계를 따르세요.

Shopify 통합을 사용하려면 각 사용 사례에 대해 카탈로그에서 사용자의 가입 상태를 캡처하는 사용자 지정 이벤트를 생성해야 합니다. 사용자 지정 이벤트에는 Shopify 제품 동기화의 일부로 선택한 [SKU 또는 Shopify 이형 상품 ID에]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) 매핑되는 이벤트 속성이 필요합니다. 

## 카탈로그 ID 변경

Shopify 카탈로그의 제품 식별자를 변경하려면 동기화를 비활성화해야 합니다. 먼저 이 Shopify 카탈로그 데이터를 사용하여 메시지 전송을 중지했는지 확인합니다. Shopify 카탈로그 초기 동기화를 다시 실행하고 [제품 동기화](#setting-up) 단계에 따라 원하는 제품 식별자를 선택합니다.

## 제품 동기화 비활성화 {#deactivate}

Shopify 제품 동기화 기능을 비활성화하면 전체 카탈로그와 제품이 삭제됩니다. 이 카탈로그의 제품 데이터를 적극적으로 사용할 수 있는 모든 전송에도 영향을 미칠 수 있습니다. 비활성화하기 전에 이러한 캠페인 또는 캔버스를 업데이트하거나 일시 중지했는지 확인하세요. 제품 세부 정보가 없는 메시지가 전송될 수 있습니다. 카탈로그 페이지에서 직접 Shopify 카탈로그를 삭제하지 마십시오.

## 문제 해결
Shopify 제품 동기화에서 오류가 발생하는 경우 다음과 같은 오류가 발생할 수 있습니다. 문제를 수정하고 동기화를 해결하는 방법에 대한 지침을 따르세요:

| 오류 | 이유 | 솔루션 |
| --- | --- | --- |
| 서버 오류 | 이는 제품 동기화를 시도할 때 Shopify 측에 서버 오류가 있는 경우 발생합니다. | [동기화를 비활성화하고](#deactivate) 전체 제품 인벤토리를 다시 동기화합니다. |
| 중복 SKU | 이는 SKU를 카탈로그 품목 ID로 사용하고 동일한 SKU를 가진 제품이 있는 경우에 발생합니다. 카탈로그 품목 ID는 고유해야 하므로 모든 제품에는 고유한 SKU가 있어야 합니다. | Shopify에서 제품 및 배리언트의 전체 목록을 감사하여 중복되는 SKU가 없는지 확인합니다. 중복 SKU가 있는 경우 Shopify 스토어 계정에서만 고유한 SKU로 업데이트하십시오. 이 문제가 해결되면 [동기화를 비활성화](#deactivate)하고 전체 제품 인벤토리를 다시 동기화합니다. |
| 카탈로그 한도 초과 | 이는 카탈로그 한도를 초과하는 경우에 발생합니다. 더 이상 가용 스토리지가 없어서 Braze가 동기화를 완료하거나 동기화를 활성 상태로 유지할 수 없습니다. | 이 문제에 대한 두 가지 해결책이 있습니다:<br><br>1\. 계정 관리자에게 문의하여 티어를 업그레이드하여 카탈로그 한도를 늘리세요. <br><br>2\. 다음 중 하나를 삭제하여 저장 공간을 확보하세요:<br>\- 다른 카탈로그의 카탈로그 항목<br>\- 기타 카탈로그<br>\- 선택 항목 생성<br><br> 두 솔루션 중 하나를 사용한 후에는 동기화를 비활성화한 다음, 다시 동기화해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}