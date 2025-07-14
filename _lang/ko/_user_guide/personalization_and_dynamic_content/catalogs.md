---
nav_title: 카탈로그
article_title: 카탈로그
page_order: 6
layout: dev_guide

guide_top_header: "카탈로그"
guide_top_text: "카탈로그는 Liquid를 통해 커스텀 속성이나 커스텀 이벤트 속성정보에 액세스하는 방법과 유사하게 가져온 CSV 파일 및 API 엔드포인트에서 데이터에 액세스하여 메시지를 보강합니다."

description: "이 랜딩 페이지에는 카탈로그가 있습니다. 카탈로그와 필터링된 세트를 사용하여 Braze 캠페인에서 비사용자 데이터를 활용하여 개인화된 메시지를 보낼 수 있습니다."

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: 카탈로그 만들기
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: 카탈로그 사용
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: 재고 부족 알림
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 가격 인하 알림
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 선택
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: 카탈로그 API 엔드포인트
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
---
<br><br>

## 카탈로그 사용 사례

모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. 일반적으로 데이터는 제품, 할인, 프로모션, 이벤트 등과 같은 오퍼링에 대한 메타데이터입니다. 이 데이터를 사용하여 관련성이 높은 메시지로 사용자를 타겟팅하는 방법에 대한 몇 가지 예는 아래 사용 사례를 참조하세요.

### Retail and eCommerce

- **시즌별 프로모션:** 시즌별 제품 컬렉션을 가져오고 최신 트렌드를 반영하여 메시지를 개인화하세요.
- **현지화된 메시지:** 실제 위치 주소, 시간, 서비스를 가져온 다음 사용자 위치를 기반으로 알림을 개인화하세요.
- **품절 알림:** Import product information that includes inventory quantity, then use [back-in-stock notifications]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/) and Braze custom events to trigger a campaign or Canvas that sends users a notification that a product is now stocked.
- **가격 인하 알림:** Import product information that includes product prices, then use [price drop notifications]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) and Braze custom events to trigger a Canvas that sends users a notification that a product's price dropped.

### 엔터테인먼트

- **구독 요금제:** 사용 패턴과 가장 자주 소비하는 콘텐츠 유형에 따라 구독 요금제를 가져와 사용자에게 추가 기능을 홍보하세요.
- **예정된 이벤트:** 예정된 이벤트 목록과 해당 위치 및 오디언스 연령을 가져온 다음 해당 지역 및 대상 연령대의 사용자에게 맞춤 알림을 보냅니다.
- **미디어 환경설정:** 영화와 프로그램에 대한 정보를 가져온 다음, 사용자가 좋아하는 타이틀과 가장 많이 시청한 장르를 기반으로 콘텐츠를 추천하세요.

### 여행 및 접객업

- **목적지:** 여행 목적지와 가장 인기 있는 명소, 레스토랑, 액티비티를 가져온 다음, 이전 여행을 기반으로 사용자에게 맞춤 추천을 제공하세요.
- **숙박 시설:** 호텔 숙소와 편의시설, 객실 유형 및 가격을 가져온 다음, 선택한 기본 설정에 따라 사용자에게 프로모션을 전송하세요.
- **여행 방법**: 항공편, 기차, 렌터카 등 여행 모드에 대한 특가 및 프로모션을 가져온 다음 최근 검색 기록을 기반으로 사용자에게 전송합니다.
- **식사 선호도:** 식사 제공에 대한 정보를 가져오고 [선택 항목]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)을 사용하여 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도를 가진 사용자에게 개인화된 메시지를 보낼 수 있습니다.

## 카탈로그와 Liquid가 함께 작동하는 방식

카탈로그는 데이터 저장 기능입니다. 여기에는 개인화를 위해 메시지에서 참조할 수 있는 대규모 데이터 세트가 포함되어 있습니다. 실제로 데이터를 참조하기 위해서는 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 템플릿 언어로 사용하게 됩니다. 즉, 카탈로그는 데이터가 저장된 저장소이고 Liquid는 저장소에서 관련 데이터를 가져오는 언어입니다.

Liquid를 사용하여 카탈로그 정보를 가져오는 방법에 대한 예는 [카탈로그 만들기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases/)의 추가 사용 사례를 참조하세요.

#### Data storage limitations

Data storage for catalogs is limited based on the size of the catalog items and selections, which may be different from the sizes of uploaded CSV files.

For the free version of catalogs, the amount of storage allowed is up to 100 MB. You can have unlimited items as long as the storage space does not exceed 100 MB. Selections will contribute to your storage. The more complex a selection is, the more storage it will take up.

For Catalogs Pro, The storage size options are: 5 GB, 10 GB, 15 GB or 50 GB. Note that the free version's storage (100 MB) is included in each of these plans.
