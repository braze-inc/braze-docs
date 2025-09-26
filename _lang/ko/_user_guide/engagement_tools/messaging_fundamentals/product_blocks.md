---
nav_title: 제품 블록
article_title: 드래그 앤 드롭 제품 블록
page_order: 7
description: "이 참조 문서에서는 사용자가 카탈로그 항목의 동적 또는 정적 쇼케이스를 신속하게 추가하고 구성할 수 있는 드래그 앤 드롭 제품 블록을 다룹니다."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# 드래그 앤 드롭 제품 블록 

> 드래그 앤 드롭 편집기를 사용하면 사용자 정의 Liquid 코드를 만들 필요 없이 메시지에 제품 블록을 신속하게 추가하고 구성하여 원활한 제품 쇼케이스를 만들 수 있습니다. 

{% alert important %}
드래그 앤 드롭 제품 블록 기능은 초기 액세스 중이며 현재 이메일에만 제공됩니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## 요구 사항 

| 요구 사항 | 설명 |
| --- | --- |
| eCommerce 추천 이벤트 | [eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events/)는 주문이 이루어지기 전후에 발생하는 주요 행동 이벤트에 대한 표준화된 데이터 스키마를 제공합니다. 이 이벤트는 궁극적으로 레거시 Braze 구매 이벤트를 대체하고 상거래 관련 행동 추적의 표준이 될 것입니다. <br><br> eCommerce 추천 이벤트는 동적 제품 블록에 필요합니다.<br><br> eCommerce 추천 이벤트는 현재 초기 액세스 중입니다. 이 초기 액세스에 참여하고 싶다면 Braze 고객 성공 매니저에게 문의하세요. |
| eCommerce 캔버스 템플릿 | eCommerce 추천 이벤트는 방치된 탐색, 방치된 장바구니 및 주문 확인과 같은 필수 사용 사례를 위해 설계된 eCommerce 캔버스 템플릿을 포함한 미리 구축된 템플릿을 지원합니다. <br><br>[eCommerce 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases/)을 사용하여 이러한 필수 eCommerce 사용 사례 중 하나를 구현할 계획이라면 제공된 캔버스 템플릿을 사용하거나 따라야 합니다. |
| Braze 카탈로그 | 제품 블록 구성에 사용될 다음 필드를 포함하는 Braze 카탈로그를 생성해야 합니다:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## 드래그 앤 드롭 제품 블록의 유형

| 제품 블록 | 목적 | 사용 사례 | 가용성 |
| --- | --- | --- | --- |
| 동적 | 고객 상호작용을 기반으로 한 제품 쇼케이스로 메시징을 개인화하려면 [eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events/) 및 [eCommerce 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases/) 내 카탈로그를 사용하세요. | {::nomarkdown}<ul><li>버려진 탐색</li><li>방치된 장바구니</li><li>중단된 결제</li><li>주문 확인</li></ul>{:/} | 캔버스에서만 사용 가능. |
| 정적 | Braze 카탈로그 또는 [카탈로그 선택]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)에 저장된 데이터만 사용하여 제품을 개인화하세요. | 신제품 출시 또는 카테고리별 제공을 보여주기에 완벽합니다.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## 제품 블록 콘텐츠 구성

각 블록 유형은 서로 다른 콘텐츠 구성을 가지고 있습니다. 

### 제품 필드

**제품 필드** 섹션에서 제품 블록 유형을 선택한 다음 포함할 필드를 토글하세요. 각 필드는 선택한 제품 블록 유형에 따라 서로 다른 소스에서 가져옵니다.

#### 동적 제품 블록

| 제품 필드 | 소스 |
| --- | --- | 
| 변형 이미지 | 카탈로그 | 
| 제품 제목 | 카탈로그 | 
| 제품 URL을 위한 버튼 | 카탈로그 |
| 가격 | eCommerce 추천 이벤트 속성|
| 수량 | eCommerce 추천 이벤트 속성| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![동적 제품 블록을 위한 제품 필드로, 카탈로그 데이터와 이벤트 데이터로 나뉩니다]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### 정적 제품 블록

| 제품 필드 | 소스 |
| --- | --- | --- |
| 변형 이미지 | 카탈로그 |
| 제품 제목 | 카탈로그 |
| 제품 URL을 위한 버튼 | 카탈로그 |
| 가격 | 카탈로그 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![정적 제품 블록을 위한 제품 필드로, 모두 카탈로그 데이터로 분류됩니다.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### 레이아웃 옵션

레이아웃 옵션을 사용하여 제품 블록 내에서 제품 표시 방식을 사용자 정의합니다.

| 옵션 | 설명 |
| --- | --- |
| 제품 방향 | 블록 내에서 이미지 및 제품 필드의 방향을 선택합니다. |
| 정렬 | 블록 내의 텍스트 필드와 버튼의 정렬을 조정합니다. |
| 행당 최대 제품 수 | 정적 제품 블록의 경우 행당 최대 3개의 제품을 표시하고, 총 12개의 제품을 표시하며, 동적 제품 블록의 경우 총 24개의 제품을 표시합니다. |
| 제품 간격 | 제품 간의 간격을 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![제품 방향, 정렬, 행당 최대 제품 수 및 제품 간격에 대한 레이아웃 옵션.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### 전역 이메일 스타일 설정 

[전역 이메일 스타일 설정]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings)을 사용하면 Braze 내에서 이메일에 일관된 스타일을 적용할 수 있습니다. 즉, 모든 이메일에 자동으로 적용될 글꼴, 색상 및 버튼 디자인과 같은 특정 스타일을 정의할 수 있습니다.

#### 전역 이메일 스타일 설정이 제품 블록과 함께 작동하는 방식

단락 및 버튼에 대한 기존 스타일은 제품 블록 내의 텍스트 및 버튼 요소에 자동으로 적용됩니다. 즉, 단락 및 버튼에 대해 설정한 모든 서식이 제품 블록에서 일관되게 사용되어 이메일 전반에 걸쳐 일관된 모양을 유지합니다.

## 제품 블록 설정

### 카탈로그 설정 

{% alert important %}
Braze와 Shopify 통합을 사용하여 [제품 동기화]({{site.baseurl}}/shopify_catalogs/)를 하는 경우, 드래그 앤 드롭 제품 블록을 사용하기 위해 추가 단계를 수행할 필요가 없습니다.<br><br> 제품 변형 정보가 없는 경우, 이벤트 페이로드 및 카탈로그 내의 제품 및 제품 변형 필드에서 최상위 제품 정보를 복제해야 합니다. 즉, 제품 블록이 제대로 작동하도록 하려면 두 식별자에 대해 동일한 제품 세부정보를 제공해야 합니다.
{% endalert %}

드래그 앤 드롭 제품 블록을 사용하려면 특정 필드 값을 포함하는 Braze 카탈로그를 설정해야 합니다. 이 필드는 제품 블록 구성에서 사용됩니다. 카탈로그에 다음 필드가 포함되어 있는지 확인하세요:

| 필드 | 설명 |
| --- | --- |
|`product_title` | 제품의 제목입니다.|
|`product_url` | 고객이 제품을 보고 구매할 수 있는 URL입니다. |
|`variant_image_url` | 변형 이미지의 URL입니다. |

필수 필드를 포함하는 [샘플 제품 카탈로그]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv)를 사용하여 시작하세요. 

![필수 필드 외에 다른 필드가 포함된 샘플 CSV 파일입니다.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## 제품 블록 만들기

이 가이드는 이메일 드래그 앤 드롭 편집기를 사용하여 동적 또는 정적 제품 블록을 생성, 테스트 및 기능을 보장하는 단계를 안내합니다.

### 1단계: 이메일 캠페인 또는 이메일 캔버스 단계를 만드세요.

#### 동적 제품 블록

{% alert note %}
동적 제품 블록은 [전자상거래 추천 이벤트]({{site.baseurl}}/ecommerce_events/)가 필요하며 [캔버스]({{site.baseurl}}/ecommerce_use_cases) 내에서만 사용할 수 있습니다. Braze Shopify 사용자의 경우 이러한 이벤트는 통합의 일부로 자동으로 포함됩니다. 비-Shopify 사용자의 경우 개발자와 협력하여 이러한 이벤트를 Braze로 전달하고 이벤트 내의 기본 제품 식별자가 카탈로그 항목 ID로 추가되도록 해야 합니다.
{% endalert %}

특정 사용 사례에 맞는 Braze 템플릿 중 하나를 사용하는 새 캔버스를 만드세요:
- 버려진 탐색
- 포기된 장바구니
- 포기된 결제
- 주문 확인

전자상거래 캔버스를 만드는 방법에 대한 자세한 지침은 [전자상거래 사용 사례]({{site.baseurl}}/ecommerce_use_cases/)를 참조하세요.

#### 정적 제품 블록

드래그 앤 드롭 이메일 캠페인, 작업 기반 캔버스 또는 드래그 앤 드롭 이메일 메시지 단계를 포함하는 템플릿을 만드세요.

### 2단계: 제품 블록 추가

{% tabs %}
{% tab 동적 제품 블록 %}

메시지 단계 내에서 이메일을 생성하거나 드래그 앤 드롭 이메일 작성기를 사용하여 기존 템플릿을 수정합니다.
이메일 메시지에 제품 블록을 드래그합니다.
동적 블록 유형이 선택되었는지 확인합니다.
개인화를 위해 사용할 제품 카탈로그를 선택합니다. 대상으로 하는 인바운드 이벤트의 제품과 일치하는지 확인합니다.

{% endtab %}
{% tab 정적 제품 블록 %}

이메일 메시지에 제품 블록을 드래그하고 정적 블록 유형을 선택합니다.
제품 블록에 사용할 카탈로그를 선택합니다. 카탈로그에 선택 항목이 있는 경우, 제품 블록에 표시할 제품을 더 좁히기 위해 선택해야 합니다.

{% endtab %}
{% endtabs %}

![편집기 블록이 포함된 "내용" 탭, 예: 제품 블록.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### 3단계: 제품 필드를 구성합니다.

제품 블록에 표시할 [제품 필드](#product-fields)를 선택합니다. 편집기에서 업데이트를 보려면 각 변경 후 **설정 적용**을 선택합니다. 

Liquid 태그 앞의 텍스트를 사용자 정의할 수도 있습니다. 예를 들어, 항목 가격 앞에 달러 기호($)를 추가하거나 수량 용어를 "수량" 또는 다른 선호하는 레이블로 업데이트할 수 있습니다.

![항목 가격 앞에 달러 기호가 추가된 제품 블록.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### 4단계: 레이아웃 설정을 구성합니다.

제품 블록 내에서 제품이 표시되는 방식을 업데이트하려면 [레이아웃 옵션](#layout-options)을 변경하고, 각 변경 후 **설정 적용**을 선택해야 합니다.

### 5단계: 메시지 미리보기 및 테스트

{% tabs %}
{% tab 동적 제품 블록 %}

1. **미리보기 및 테스트** 섹션에서 메시지를 커스텀 사용자로 미리 봅니다.
2. 미리보기에서 렌더링할 항목 수를 지정합니다.
3. 정확한 수의 항목이 나타나고 레이아웃 옵션이 올바르게 적용되었는지 확인합니다. 나타나는 항목은 무작위로 선택됩니다.

!["사용자로 미리보기" 탭에는 4개의 항목을 표시하도록 지정하는 드롭다운 섹션 "동적 제품 블록"이 있습니다.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab 정적 제품 블록 %}

제품 블록에 변경 사항을 적용하면 드래그 앤 드롭 작성기 내에서 미리보기가 생성됩니다. 

![다양한 항목 타일이 있는 생성된 제품 블록을 보여주는 이메일 드래그 앤 드롭 작성기.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

메시지를 작성하고 예상대로 보이는지 확인한 후, 전송할 준비가 되었습니다!