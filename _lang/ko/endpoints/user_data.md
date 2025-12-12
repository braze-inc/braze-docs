---
nav_title: 사용자 데이터
article_title: 사용자 데이터 엔드포인트
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "이 랜딩 페이지에는 Braze 사용자 데이터 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "사용자 데이터 엔드포인트"
guide_top_text: "Braze 사용자 데이터 엔드포인트를 사용하면 모바일 앱 외부에서 오는 사용자에 대한 데이터를 기록하여 사용자에 대한 정보를 추적할 수 있습니다. 이 API를 사용하여 테스트 또는 기타 목적으로 사용자를 삭제할 수도 있습니다. <br> <br> 모든 API 엔드포인트의 데이터 페이로드 제한은 4MB입니다. 4MB를 초과하는 데이터를 게시하려고 시도하면 HTTP 413 요청 엔티티가 너무 커서 실패합니다. <br> <br> 이 섹션의 예시에는 https://rest.iad-01.braze.com URL이 포함되어 있지만 다른 엔드포인트 URL을 사용해야 할 수도 있습니다(예: Braze EU 데이터 센터에서 호스팅되거나 전용 Braze를 설치한 경우). Braze 고객 성공 관리자가 다른 엔드포인트 URL을 사용해야 하는지 알려줄 것입니다."

guide_featured_title: "사용자 데이터 엔드포인트"
guide_featured_list:
  - name: "POST: 새 사용자 별칭 만들기"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 사용자 별칭 업데이트"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: 사용자 데이터 삭제"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: 사용자 식별"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: 사용자 추적"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: 사용자 추적(동기식)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: 사용자 병합"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: 외부 ID 이름 바꾸기"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 더 이상 사용되지 않는 외부 ID 제거"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
