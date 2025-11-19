---
nav_title: 제품 블록
article_title: 드래그 앤 드롭 제품 블록
page_order: 7.5
description: "이 참고 문서에서는 사용자가 카탈로그 품목의 동적 또는 정적 쇼케이스를 빠르게 추가하고 구성할 수 있는 드래그 앤 드롭 제품 블록에 대해 설명합니다."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# 제품 블록 드래그 앤 드롭 

> 드래그 앤 드롭 편집기를 사용하면 커스텀 Liquid 코드를 만들 필요 없이 메시지에 제품 블록을 빠르게 추가하고 구성하여 매끄러운 제품 쇼케이스를 만들 수 있습니다. 

{% alert important %}
드래그 앤 드롭 제품 차단 기능은 현재 얼리 액세스 중이며 이메일에서만 사용할 수 있습니다. 얼리 액세스에 참여하고 싶으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 요구 사항 

| 요구 사항 | 설명 |
| --- | --- |
| 이커머스 추천 이벤트 | [전자상거래 추천 이벤트는]({{site.baseurl}}/ecommerce_events/) 주문 전후에 발생하는 주요 행동 이벤트에 대한 표준화된 데이터 스키마를 제공합니다. 이러한 이벤트는 결국 기존의 Braze 구매 이벤트를 대체할 것이며, 커머스 관련 행동을 추적하는 표준이 될 것입니다. <br><br> 동적 제품 블록에는 전자상거래 추천 이벤트가 필요합니다.<br><br> 전자상거래 추천 이벤트는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 고객 성공 매니저에게 문의하세요. |
| 전자상거래 캔버스 템플릿 | 전자상거래 추천 이벤트는 유기한 탐색, 유기한 장바구니, 주문 확인과 같은 필수 사용 사례를 위해 설계된 전자상거래 캔버스 템플릿을 포함하여 사전 구축된 템플릿을 지원합니다. <br><br>[전자상거래 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases/)을 사용하여 이러한 필수 전자상거래 사용 사례를 구현하려는 경우 제공된 캔버스 템플릿을 사용하거나 따라야 합니다. |
| Braze 카탈로그 | 제품 블록 구성에 사용할 다음 필드가 포함된 Braze 카탈로그를 생성해야 합니다:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| 카탈로그 선택 | 정적 제품 블록의 경우 [카탈로그 선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) 항목을 생성하여 제품 블록에 포함할 제품을 지정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## 드래그 앤 드롭 제품 블록 유형

| 제품 블록 | 목적 | 사용 사례 | 가용성 |
| --- | --- | --- | --- |
| 동적 | [전자상거래 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases/) 내에서 [전자상거래 추천 이벤트]({{site.baseurl}}/ecommerce_events/) 및 카탈로그를 사용하여 고객 상호 작용을 기반으로 한 제품 쇼케이스로 메시징을 개인화하세요. | {::nomarkdown}<ul><li>중단된 탐색</li><li>유기한 장바구니</li><li>중단된 결제</li><li>주문 확인</li></ul>{:/} | 캔버스에서만 사용할 수 있습니다. |
| 정적 | Braze 카탈로그에 저장된 데이터를 사용하여 제품을 개인화하세요. [카탈로그 선택을]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) 사용하여 포함할 제품을 지정해야 합니다. | 신제품 출시 또는 카테고리별 제품을 소개하는 데 적합합니다.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## 제품 블록 콘텐츠 구성

각 블록 유형에는 서로 다른 콘텐츠 구성이 있습니다. 

### 제품 분야

**제품 필드** 섹션에서 제품 블록 유형을 선택한 다음 각 제품에 포함할 필드를 토글합니다. 각 필드는 선택한 제품 블록 유형에 따라 서로 다른 소스에서 가져옵니다.

#### 동적 제품 블록

| 제품 분야 | 출처 |
| --- | --- | 
| 배리언트 이미지 | 카탈로그 | 
| 제품 제목 | 카탈로그 | 
| 제품 URL 버튼 | 카탈로그 |
| 가격 | 전자상거래 추천 이벤트 속성정보|
| 수량 | 전자상거래 추천 이벤트 속성정보| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

!!! 카탈로그 데이터와 이벤트 데이터로 구분되는 동적 제품 블록의 제품 필드]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### 정적 제품 블록

| 제품 분야 | 출처 |
| --- | --- | --- |
| 배리언트 이미지 | 카탈로그 |
| 제품 제목 | 카탈로그 |
| 제품 URL 버튼 | 카탈로그 |
| 가격 | 카탈로그 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

정적 제품 블록의 제품 필드는 모두 카탈로그 데이터로 분류됩니다.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### 레이아웃 옵션

레이아웃 옵션을 사용하여 제품 블록 내에서 제품이 표시되는 방식을 커스텀할 수 있습니다.

| 옵션 | 설명 |
| --- | --- |
| 제품 방향 | 블록 내 이미지 및 제품 필드의 방향을 선택합니다. |
| 정렬 | 블록 내 텍스트 필드와 버튼의 정렬을 조정합니다. |
| 행당 최대 제품 수 | 정적 제품 블록의 경우 행당 최대 3개 제품, 총 12개 제품, 동적 제품 블록의 경우 총 24개 제품을 표시할 수 있습니다. |
| 제품 간격 | 제품 간 간격을 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

제품 방향, 정렬, 행당 최대 제품 수 및 제품 간격에 대한 레이아웃 옵션.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### 글로벌 이메일 스타일 설정 

[글로벌 이메일 스타일 설정을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) 사용하면 Braze 내에서 이메일에 일관된 스타일을 적용할 수 있습니다. 즉, 글꼴, 색상, 버튼 디자인 등 특정 스타일을 정의하여 모든 이메일에 자동으로 적용할 수 있습니다.

#### 글로벌 이메일 스타일 설정이 제품 블록에서 작동하는 방식

단락 및 버튼에 대한 기존 스타일이 제품 블록 내의 텍스트 및 버튼 요소에 자동으로 적용됩니다. 즉, 단락과 버튼에 설정한 서식이 제품 블록에서 일관되게 사용되므로 이메일 전체에서 일관된 모양을 유지할 수 있습니다.

## 제품 블록 설정하기

### 카탈로그 설정 

{% alert important %}
[제품 동기화를]({{site.baseurl}}/shopify_catalogs/) 위해 Braze 및 Shopify 통합을 사용하는 경우 드래그 앤 드롭 제품 블록을 사용하기 위해 추가 단계를 수행할 필요가 없습니다.<br><br> 제품 배리언트 정보가 없는 경우 이벤트 페이로드 및 카탈로그 내의 제품 및 제품 배리언트 필드에 최상위 제품 정보를 모두 복제해야 합니다. 즉, 제품 블록이 제대로 작동하려면 일관성을 유지하려면 두 식별자에 대해 동일한 제품 세부 정보를 제공해야 합니다.
{% endalert %}

드래그 앤 드롭 제품 블록을 사용하려면 특정 필드 값이 포함된 Braze 카탈로그를 설정해야 합니다. 이러한 필드는 제품 블록 구성에 사용됩니다. 카탈로그에 다음 필드가 포함되어 있는지 확인하세요:

| 필드 | 설명 |
| --- | --- |
|`product_title` | 제품 제목입니다.|
|`product_url` | 고객이 제품을 보거나 구매할 수 있는 URL입니다. |
|`variant_image_url` | 배리언트 이미지의 URL입니다. |

필수 필드가 포함된 [샘플 제품 카탈로그를]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv) 작성하여 빠르게 시작할 수 있습니다. 

필수 필드와 기타 필드가 포함된 샘플 CSV 파일입니다.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## 제품 블록 생성

이 가이드에서는 이메일 드래그 앤 드롭 편집기를 사용하여 동적 또는 정적 제품 블록을 생성하고, 테스트하고, 기능을 확인하는 단계를 안내합니다.

### 1단계: 이메일 캠페인 또는 이메일 캔버스 단계 만들기

#### 동적 제품 블록

{% alert note %}
동적 제품 블록에는 [전자상거래 추천 이벤트가]({{site.baseurl}}/ecommerce_events/) 필요하며 [캔버스]({{site.baseurl}}/ecommerce_use_cases) 내에서만 사용할 수 있습니다. Braze Shopify 사용자의 경우 이러한 이벤트는 통합의 일부로 자동으로 포함됩니다. Shopify 이외의 사용자의 경우 개발자와 협력하여 이러한 이벤트를 Braze에 전달하고 이벤트 내의 기본 제품 식별자가 카탈로그 품목 ID로 추가되도록 해야 합니다.
{% endalert %}

특정 사용 사례에 맞게 사용 가능한 Braze 템플릿 중 하나를 사용하는 새 캔버스를 만듭니다:
- 버려진 찾아보기
- 유기한 장바구니
- 중단된 결제
- 주문 확인

전자상거래 캔버스 생성에 대한 자세한 지침은 [전자상거래 사용 사례를]({{site.baseurl}}/ecommerce_use_cases/) 참조하세요.

#### 정적 제품 블록

드래그 앤 드롭 이메일 캠페인, 작업 기반 캔버스 또는 드래그 앤 드롭 이메일 메시지 단계가 있는 템플릿을 만듭니다.

### 2단계: 제품 블록 추가

{% tabs %}
{% tab Dynamic product block %}

메시지 단계 내에서 드래그 앤 드롭 이메일 작성기를 사용하여 이메일을 작성하거나 기존 템플릿을 수정합니다.
제품 블록을 이메일 메시지로 드래그합니다.
동적 블록 유형이 선택되었는지 확인합니다.
개인화에 사용할 제품 카탈로그를 선택합니다. 타겟팅하는 인바운드 이벤트의 제품과 일치하는지 확인하세요.

{% endtab %}
{% tab Static product block %}

제품 블록을 이메일 메시지로 드래그하고 정적 블록 유형을 선택합니다.
제품 블록에 사용할 카탈로그를 선택합니다. 제품 블록에 표시할 제품을 지정하려면 카탈로그 선택 항목을 선택해야 합니다.

{% endtab %}
{% endtabs %}

제품 블록과 같은 편집기 블록이 포함된 '콘텐츠' 탭입니다.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### 3단계: 제품 필드 구성

제품 블록에 표시할 [제품 필드를](#product-fields) 선택합니다. 각 변경 후 **설정 적용을** 선택하여 편집기에서 업데이트를 확인합니다. 

Liquid 태그 앞의 텍스트를 커스텀할 수도 있습니다. 예를 들어 품목 가격에 달러 기호($)를 앞에 붙이거나 수량 용어를 '금액' 또는 다른 선호하는 레이블로 업데이트할 수 있습니다.

!!\![상품 가격에 달러 쪽이 앞에 붙은 제품 블록.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### 4단계: 레이아웃 설정 구성

[레이아웃 옵션을](#layout-options) 변경하여 제품 블록 내에서 제품이 표시되는 방식을 업데이트하고 변경할 때마다 **설정 적용을** 선택해야 합니다.

### 5단계: 메시지 미리보기 및 테스트하기

{% tabs %}
{% tab Dynamic product block %}

1. ** & 테스트 미리보기** 섹션에서 메시지를 커스텀 사용자로 미리 봅니다.
2. 미리 보기에서 렌더링할 항목 수를 지정합니다.
3. 올바른 수의 항목이 표시되고 레이아웃 옵션이 올바르게 적용되었는지 확인합니다. 표시되는 항목은 무작위로 선택된다는 점에 유의하세요.

'사용자로 미리보기' 탭에 4개의 항목을 표시하도록 지정하는 드롭다운 섹션인 '동적 제품 블록'이 있습니다.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

제품 블록에 변경 사항을 적용하면 드래그 앤 드롭 컴포저 내에서 미리보기가 생성됩니다. 

다양한 항목 타일로 제품 블록을 생성하는 이메일 드래그 앤 드롭 작성기를 보여줍니다.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

메시지 작성을 완료하고 메시지가 예상대로 표시되는지 확인하면 전송 준비가 완료된 것입니다!