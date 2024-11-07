---
nav_title: Shopify 컬렉션 동기화
article_title: Shopify 컬렉션 동기화
permalink: "/shopify_collections_sync/"
description: "이 참고 문서에서는 고객이 카테고리별로 제품을 찾을 수 있도록 제품을 컬렉션으로 그룹화할 수 있는 Shopify 컬렉션 동기화를 설정하는 방법에 대해 설명합니다."
hidden: true
---

# Shopify 컬렉션 동기화 베타

> Shopify 컬렉션 동기화를 사용하면 제품을 컬렉션으로 그룹화하여 고객이 카테고리별로 제품을 찾을 수 있습니다. 보다 원활한 쇼핑객 경험을 위해 상점의 컬렉션 내 아이템을 Braze 메시지에 통합할 수 있습니다.

{% alert important %}
Shopify 컬렉션 동기화는 현재 베타 버전입니다. 베타에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## Shopify 컬렉션 동기화 설정

Shopify 스토어에서 Braze로 제품을 동기화하려면 [Shopify 통합의]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze) **제품 동기화** 단계에서 **Shopify 컬렉션 동기화** 확인란을 선택합니다.<br><br>!['Shopify 컬렉션 동기화' 확인란을 선택한 상태에서 Shopify 제품 동기화 4단계를 수행합니다.][1]

제품 동기화가 완료되면 Shopify 카탈로그에서 컬렉션과 연결된 제품을 확인할 수 있습니다. <br><br>!['베스트셀러' 및 '첫 페이지' 컬렉션에 있는 제품을 보여주는 카탈로그 테이블 행입니다.][2]

Shopify 카탈로그의 **선택** 탭에서 Shopify 컬렉션을 볼 수 있습니다. <br><br>![선택 탭에는 "베스트셀러"와 "첫 페이지"의 두 가지 컬렉션 목록이 표시됩니다.][3]

### 베타 기능

- Braze는 최대 30개의 컬렉션을 지원합니다.
- 현재 컬렉션의 정렬 순서는 유지 관리되거나 지원되지 않습니다. 현재로서는 다음을 기준으로 정렬 순서를 지정합니다:
    - 컬렉션에 가장 최근에 추가된 항목입니다.
    - 연속 동기화 중에 항목이 업데이트되는 순서입니다.
    - Shopify 컬렉션의 선택 탭에서 선택한 순서입니다.

## Shopify 컬렉션 사용

Shopify 컬렉션을 사용하여 캠페인의 각 사용자에 대한 메시지를 개인화하려면 [Braze 선택]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) 항목을 사용하는 방법과 유사합니다.

{% alert warning %}
베타 버전에서는 다음 동작에 유의하세요: <br><br>Shopify 컬렉션 설명 또는 필터 설정을 업데이트하면 Shopify 컬렉션 동기화가 중단됩니다. 결과적으로 Shopify 컬렉션이 예상대로 작동하지 않습니다.
{% endalert %}

### 1단계: Shopify 컬렉션의 정렬 순서 구성

1. Shopify 컬렉션의 선택 탭에서 **정렬 순서를** 선택하여 Shopify 컬렉션 결과가 반환되는 순서를 지정합니다. 여기에는 정렬 순서를 무작위로 지정하는 옵션이 포함되어 있습니다.
2. **제한 수**에 최대 결과 수(최대 50개)를 입력합니다.
3. **선택 항목 업데이트**를 선택합니다.

![필터 설정, 정렬 유형 및 결과 제한을 선택할 수 있는 선택 항목 편집 페이지입니다.][4]

### 2단계: 캠페인에서 컬렉션 사용

1. 캠페인을 만든 다음 메시지 작성기에서 **\+ 개인화 설정을** 선택합니다.
2. 다음을 선택합니다:<br>- **개인화 유형**으로 **카탈로그 항목** <br>\- 카탈로그 이름<br>\- 항목 선택 방법<br>\- 선택 이름(Shopify 컬렉션 이름) <br>\- 메시지에 표시할 정보

{: start="3"}
3\. 메시지에서 정보를 표시할 위치에 Liquid 스니펫을 복사하여 붙여넣습니다.

![카탈로그, 항목 선택 방법, 표시할 정보를 선택할 수 있는 필드가 있는 "개인화 추가" 섹션입니다.][5]{: style="max-width:30%;"}

#### 선택 결과의 Liquid

커스텀 속성 및 커스텀 이벤트와 같은 카탈로그의 결과를 사용하면 선택 항목의 사용자마다 다른 결과가 반환될 수 있습니다.

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
