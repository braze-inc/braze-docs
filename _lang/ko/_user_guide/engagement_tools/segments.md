---
nav_title: 세그먼트
article_title: 세그먼트
page_order: 1
layout: dev_guide
guide_top_header: "세그먼트"
guide_top_text: "오디언스 세분화는 전략적 마케팅의 핵심입니다—이는 타겟팅을 과도하게 하거나, 귀찮게 하거나, 고객과의 잠재적 연결을 놓치는 것을 방지할 수 있습니다. 다음 기사를 확인하여 오디언스를 세그먼트하고 필터링하여 당신과 그들의 최대 이익을 얻는 방법을 알아보세요."
descriptions: "오디언스 세분화는 전략적 마케팅의 핵심입니다—이는 타겟팅을 과도하게 하거나, 귀찮게 하거나, 고객과의 잠재적 연결을 놓치는 것을 방지할 수 있습니다. 이 랜딩 페이지를 확인하여 세그먼트하고 필터링하여 오디언스를 최대한 활용하는 방법을 알아보세요."
search_rank: 4
tool: Segments
page_type: landing
description: "이 랜딩 페이지는 대시보드 캠페인 내 세분화에 대한 기사를 다룹니다. 여기에서 세그먼트, 필터, 퍼널, 인사이트, 확장 프로그램 등을 설정하는 방법에 대한 정보를 찾을 수 있습니다."

guide_featured_title: "인기 기사"
guide_featured_list:
  - name: 세그먼트 만들기
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: 세그먼트 관리
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: 세분화 필터
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: 세그먼트 퍼널
    link: /docs/user_guide/engagement_tools/segments/segment_funnels/
    image: /assets/img/braze_icons/users-right.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: 세그먼트 인사이트
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: 세그먼트 확장
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: SQL 세그먼트
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: 카탈로그 세그먼트
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: 사용자 프로필
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: 위치 타겟팅
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: 정규 표현식
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Suppression Lists
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: 세그먼트 크기 측정
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: 문제 해결
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: 커스텀 속성
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Braze 세그먼트 정보

Braze에서 세그먼트는 사용자가 정의한 특정 기준(사용자 속성, 사용자 행동 및 커스텀 이벤트 등)에 맞는 동적 사용자 그룹입니다. 세그먼트 내에 다른 세그먼트를 중첩하고 추가 기능을 적용하여 기준을 세분화할 수 있으며, 오디언스의 범위를 좁혀 매우 개인화되고 매력적인 콘텐츠를 적절한 사용자에게 보낼 수 있습니다.

사용자를 타겟으로 원하는 만큼 세그먼트를 만들 수 있습니다. 세그먼트 기능과 세분화 필터의 다양한 조합을 탐색하여 사용자 데이터를 활용하는 창의적인 방법을 발견하고, 사용자에게 관련 메시지를 보내고 참여를 증가시키는 새로운 방법을 찾아보세요.

아래 사용 사례를 확인하여 Braze 세그먼트가 사용자를 타겟팅하는 데 어떻게 도움이 되는지 간단히 살펴보세요.

### 사용 사례

- **환영 메시지:** 신규 사용자를 세그먼트하여 온보딩 이메일 또는 인앱 메시지를 보내 앱을 소개할 수 있습니다.
- **로열티 리워드:** 세그먼트 사용자를 구매 빈도, 회원 기념일 또는 기타 마일스톤을 기준으로 세분화하고, 가장 충성도가 높은 사용자에게 독점적인 제안이나 보상을 보내세요.
- **행동 유발 요인:** 사용자의 행동에 따라 세그먼트 사용자를 분류하여 결제 시 장바구니를 포기하는 등의 행동을 트리거로 하여 인앱 메시지 또는 푸시 알림을 보냅니다.
- **항목 추천:** 세그먼트 사용자가 특정 제품을 구매하고 보완 제품 또는 상위 제품에 대한 추천을 보냅니다.
- **A/B 테스트:** 세그먼트 사용자 A/B 테스트 다른 메시지, 제목란 또는 콘텐츠를 테스트하여 특정 연령, 성별 및 기타 속성의 사용자에게 가장 잘 반응하는 것을 결정합니다.

#### 세그먼트 확장 사용 사례

[세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)을 사용하여 고객 프로필의 수명 동안 저장된 커스텀 이벤트 또는 구매 행동을 기반으로 사용자를 타겟팅하여 세그먼트를 더욱 세분화할 수 있습니다.

- **과거 구매:** 세그먼트 사용자가 지난 2년 동안 특정 제품의 특정 색상을 두 번 이상 구매했는지 여부에 따라 세그먼트합니다.
- **이벤트 및 메시지 상호 작용:** 사용자가 지난 30일 동안 구매를 했는지 여부와 특정 인앱 메시지와 상호작용했는지 여부에 따라 세그먼트합니다.
- **쿼리 데이터:** 
  - **쿼리 Snowflake:** 세그먼트 사용자는 Braze 및 CRM 또는 데이터 웨어하우스와 같은 외부 소스에서 결합된 데이터를 사용하여 Snowflake를 쿼리하기 위해 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을(를) 사용할 수 있습니다.
  - **데이터 웨어하우스에서 동기화:** 데이터 웨어하우스 또는 파일 저장 시스템에서 Braze로 직접 동기화된 데이터를 사용하여 [CDI 세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)를 통해 세그먼트 사용자.

