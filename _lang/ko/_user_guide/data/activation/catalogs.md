---
nav_title: 카탈로그
article_title: 카탈로그
page_order: 6
layout: dev_guide

guide_top_header: "카탈로그"
guide_top_text: "카탈로그는 가져온 CSV 파일 및 API 엔드포인트의 데이터에 액세스하여 메시지를 보강하며, 이는 Liquid를 통해 커스텀 속성 또는 커스텀 이벤트 속성에 액세스하는 방식과 유사합니다."

description: "이 랜딩 페이지에는 카탈로그가 있습니다. 카탈로그와 필터링된 세트를 사용하여 Braze 캠페인에서 비사용자 데이터를 활용하여 개인화된 메시지를 보낼 수 있습니다."

guide_featured_title: "섹션 기사"
guide_featured_list:
- name: 카탈로그 만들기
  link: /docs/user_guide/data/activation/catalogs/create/
  image: /assets/img/braze_icons/users-01.svg
- name: 카탈로그 사용
  link: /docs/user_guide/data/activation/catalogs/use/
  image: /assets/img/braze_icons/users-01.svg
- name: 재고 부족 알림
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 가격 인하 알림
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 선택 항목
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: 카탈로그 API 엔드포인트
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: 드래그 앤 드롭 제품 블록
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## 카탈로그 사용 사례

모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. 일반적으로 데이터는 제품, 할인, 프로모션, 이벤트 등과 같은 오퍼링에 대한 메타데이터입니다. 이 데이터를 사용하여 관련성이 높은 메시징으로 사용자를 타겟팅하는 방법에 대한 몇 가지 예는 아래 사용 사례를 참조하세요.

### 소매 및 이커머스

- **시즌별 프로모션:** 시즌별 제품 컬렉션을 가져오고 최신 트렌드를 반영하여 메시지를 개인화하세요.
- **현지화된 메시지:** 실제 위치 주소, 시간, 서비스를 가져온 다음 사용자 위치를 기반으로 알림을 개인화하세요.
- **품절 알림:** 재고 수량이 포함된 제품 정보를 가져온 다음, [품절 알림과]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) Braze 커스텀 이벤트를 사용하여 사용자에게 제품이 입고되었다는 알림을 보내는 캠페인이나 캔버스를 트리거하세요.
- **가격 인하 알림:** 제품 가격이 포함된 제품 정보를 가져온 다음 [가격 인하 알림과]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) Braze 커스텀 이벤트를 사용하여 사용자에게 제품 가격이 인하되었다는 알림을 보내는 캔버스를 트리거할 수 있습니다.

### 엔터테인먼트

- **구독 요금제:** 사용 패턴과 가장 자주 소비하는 콘텐츠 유형에 따라 구독 요금제를 가져와 사용자에게 부가 기능을 홍보하세요.
- **예정된 이벤트:** 예정된 이벤트 목록과 해당 위치, 오디언스 연령을 가져온 다음 해당 지역과 타겟 연령대의 사용자에게 개인화된 알림을 보내세요.
- **미디어 환경설정:** 영화와 프로그램에 대한 정보를 가져온 다음, 사용자가 좋아하는 타이틀과 가장 많이 시청한 장르를 기반으로 사용자에게 콘텐츠를 추천하세요.

### 여행 및 접객업

- **대상:** 여행 대상지와 가장 인기 있는 명소, 레스토랑, 액티비티를 가져온 다음, 이전 여행을 기반으로 사용자에게 추천을 개인화할 수 있습니다.
- **숙박 시설:** 호텔 숙소와 편의시설, 객실 유형, 가격을 가져온 다음 선택한 기본 설정에 따라 사용자에게 프로모션을 전송하세요.
- **여행 방법**: 여행 모드(항공편, 기차, 렌터카 등)에 대한 특가 및 프로모션을 가져온 다음, 최근 사용자 검색 기록을 기반으로 사용자에게 전송할 수 있습니다.
- **식사 환경설정:** 식사 제공에 대한 정보를 가져오고 [선택 항목을]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) 사용하여 가장 최근에 본 음식 카테고리를 기반으로 특정 식사 선호도를 가진 사용자에게 개인화된 메시지를 보낼 수 있습니다.

## 카탈로그와 Liquid가 함께 작동하는 방식

카탈로그는 데이터 저장 기능입니다. 여기에는 개인화를 위해 메시징에서 참조할 수 있는 대규모 데이터 세트가 포함되어 있습니다. 실제로 데이터를 참조하려면 템플릿 언어로 [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하게 됩니다. 즉, 카탈로그는 데이터가 저장된 스토리지이고 Liquid는 스토리지에서 관련 데이터를 가져오는 언어입니다.

Liquid를 사용하여 카탈로그 정보를 가져오는 방법에 대한 예는 [카탈로그 만들기의]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/) 추가 사용 사례를 참조하세요.

#### 데이터 저장 용량 제한

카탈로그의 데이터 저장 용량은 카탈로그 항목의 크기에 따라 제한되며, 업로드된 CSV 파일의 크기와 다를 수 있습니다.

무료 버전의 카탈로그의 경우 허용되는 저장 용량은 최대 100MB입니다. 저장 공간이 100MB를 초과하지 않는 한 무제한으로 항목을 보유할 수 있습니다.

카탈로그 프로의 경우 저장소 크기 옵션은 다음과 같습니다: 5GB, 10GB, 15GB 또는 50GB. 각 요금제에는 무료 버전의 저장 용량(100MB)이 포함되어 있습니다.
