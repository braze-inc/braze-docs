---
nav_title: 사용자 데이터
article_title: Braze의 사용자 데이터
page_order: 3.5
layout: dev_guide
guide_top_header: "Braze의 사용자 데이터"
guide_top_text: "Braze 구현을 완료하기 전에 마케팅 팀과 개발 팀 간에 마케팅 목표에 대해 충분히 논의하세요. 이러한 목표를 고려하고 목표에서 역으로 추적할 데이터와 Braze로 해당 데이터를 추적하는 방법을 결정하는 것이 좋습니다."

page_type: landing
description: "이 랜딩 페이지는 사용자 데이터 수집에 관한 문서를 모아둔 곳입니다. 여기에서 아카이브 정의, 사용자 가져오기, 고객 프로필 수명주기, 활용 사례, 모범 사례 등에 대한 자료를 찾을 수 있습니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: SDK 데이터 수집
    link: /docs/user_guide/data/unification/user_data/sdk_data_collection/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: 고객 프로필 수명주기
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/
    image: /assets/img/braze_icons/refresh-ccw-05.svg
  - name: 데이터 수집 모범 사례
    link: /docs/user_guide/data/unification/user_data/best_practices/
    image: /assets/img/braze_icons/thumbs-up.svg
  - name: 데이터 수집 활용 사례 예시
    link: /docs/user_guide/data/unification/user_data/collection_use_case/
    image: /assets/img/braze_icons/data.svg
  - name: 사용자 가져오기
    link: /docs/user_guide/data/unification/user_data/import_users/
    image: /assets/img/braze_icons/users-01.svg
  - name: 사용자 삭제
    link: /docs/user_guide/data/unification/user_data/delete_users/
    image: /assets/img/braze_icons/edit-05.svg
  - name: 익명 사용자
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/
    image: /assets/img/braze_icons/user-circle.svg
  - name: 사용자 언어 코드
    link: /docs/user_guide/data/unification/user_data/language_codes/
    image: /assets/img/braze_icons/globe-04.svg
---

<br>

{% alert important %}
Braze는 세션이 500만 회를 초과하는 사용자("더미 사용자")를 차단하거나 금지하며, 해당 사용자의 SDK 이벤트를 더 이상 수집하지 않습니다. 이는 일반적으로 잘못된 통합으로 인해 발생하기 때문입니다. 정상적인 사용자에게 이런 일이 발생한 것을 발견하면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

<br>