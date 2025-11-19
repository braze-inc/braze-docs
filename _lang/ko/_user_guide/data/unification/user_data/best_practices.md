---
nav_title: 수집 모범 사례
article_title: 컬렉션 모범 사례
page_order: 3.1
page_type: reference
description: "다음 문서에서는 신규 및 기존 사용자 데이터를 수집하는 다양한 방법과 모범 사례를 명확히 설명합니다."

---

# 수집 모범 사례

> 고객의 고객 프로필 수명주기를 구상할 때 알려진 사용자와 알려지지 않은 사용자의 사용자 데이터를 언제, 어떻게 수집해야 하는지 파악하는 것은 어려울 수 있습니다. 이 도움말에서는 사용 사례를 통해 신규 및 기존 사용자 데이터를 수집하는 다양한 방법과 모범 사례를 명확히 설명합니다.

다음 예는 이메일 수집 사용 사례이지만 이 로직은 다양한 데이터 수집 시나리오에 적용됩니다. 이 예에서는 이미 가입 양식이나 사용자 정보를 수집하는 방법을 통합했다고 가정합니다. 

사용자가 기록할 정보를 제공한 후에는 해당 데이터가 데이터베이스에 이미 존재하는지 확인하고 필요한 경우 사용자 별칭 프로필을 만들거나 기존 사용자 프로필을 업데이트하는 것이 좋습니다.

알 수 없는 사용자가 사이트를 방문한 후 나중에 계정을 만들거나 이메일 가입을 통해 자신을 식별하는 경우 프로필 병합을 신중하게 처리해야 합니다. 병합하는 방법에 따라 사용자 별칭 지정 사용자 정보 또는 익명 데이터를 덮어쓸 수 있습니다.

## 웹 양식을 통해 사용자 데이터 캡처하기

### 1단계: 사용자 존재 여부 확인

사용자가 웹 양식을 통해 콘텐츠를 입력하는 경우 해당 이메일을 가진 사용자가 데이터베이스에 이미 존재하는지 확인하세요. 이 작업은 두 가지 방법 중 하나로 수행할 수 있습니다:

- **내부 데이터베이스 확인(권장):** 제공된 사용자 정보가 포함된 외부 기록이나 데이터베이스가 Braze 외부에 존재하는 경우 이메일 제출 또는 계정 생성 시 이를 참조하여 정보가 이미 캡처되지 않았는지 확인하세요.
- **[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/):** `email` 을 식별자로 사용하면 이메일 주소가 아직 없는 경우 새 고객 프로필이 생성됩니다.

### 2단계: 사용자 로그 또는 업데이트

- **사용자가 존재하는 경우:**
  - 새 프로필을 만들지 마세요.
  - 사용자 프로필에 커스텀 속성(예: `newsletter_subscribed: true`)을 기록하여 사용자가 뉴스레터 구독을 통해 이메일을 제출했음을 표시합니다. 동일한 이메일 주소로 여러 개의 Braze 고객 프로필이 존재하는 경우 모든 프로필이 내보내집니다.<br><br>
- **사용자가 존재하지 않는 경우:**
  - [`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 통해 별칭 전용 프로필을 만듭니다. 이 엔드포인트는 `update_existing_only` 이 `false` 로 설정된 경우 [`user_alias` 개체를]({{site.baseurl}}/api/objects_filters/user_alias_object/) 수락하고 별칭 전용 프로필을 생성합니다. 사용자의 이메일을 사용자 별칭 지정으로 설정하여 향후 해당 사용자를 참조할 수 있도록 합니다(사용자에게 `external_id`)가 없으므로).

\![별칭 전용 사용자 프로필을 업데이트하는 프로세스를 보여주는 다이어그램. 사용자가 마케팅 랜딩 페이지에서 이메일 주소와 커스텀 속성인 우편 번호를 제출합니다. 랜딩 페이지 컬렉션에서 별칭 전용 사용자 프로필을 가리키는 화살표는 사용자 별칭 이름, 별칭 라벨, 이메일, 우편 번호가 포함된 요청 본문과 함께 사용자 추적 엔드포인트에 대한 Braze API 요청을 표시합니다. 프로필에는 새로 생성된 프로필에 반영되는 데이터를 표시하기 위해 요청 본문의 속성과 함께 "사용자 별칭만 Braze에서 생성된 사용자"라는 라벨이 표시됩니다.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## 이메일 캡처 양식을 통해 사용자 이메일 캡처하기

이메일 캡처 양식을 사용하여 사용자에게 이메일 주소를 제출하라는 메시지를 표시하면 고객 프로필에 추가됩니다. 이 양식을 설정하는 방법에 대한 자세한 내용은 [이메일 캡처 양식을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) 참조하세요.
 
## 별칭 전용 사용자 식별자 지정하기

계정 생성 시 사용자를 식별할 때 별칭 전용 사용자를 식별하고 [`/users/identify` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 통해 별칭 전용 사용자와 알려진 프로필을 병합하여 외부 ID를 할당할 수 있습니다. 

사용자 별칭 지정 전용인지 확인하려면 [해당 사용자가](#step-1-check-if-user-exists) 데이터베이스 내에 [존재하는지 확인하세요](#step-1-check-if-user-exists). 
- 외부 레코드가 있는 경우 `/users/identify/` 엔드포인트를 호출할 수 있습니다. 
- [`/users/export/id` 엔드포인트가]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) `external_id` 을 반환하면 `/users/identify/` 엔드포인트를 호출할 수 있습니다.
- 엔드포인트가 아무것도 반환하지 않으면 `/users/identify/` 호출을 하지 않아야 합니다.

## 별칭 전용 사용자 정보가 이미 있는 경우 사용자 데이터 캡처하기

사용자가 계정을 만들거나 이메일 가입을 통해 자신을 식별하는 경우 프로필을 병합할 수 있습니다. 병합할 수 있는 필드 목록은 [업데이트 동작 병합을]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) 참조하세요.

### 중복된 고객 프로필 병합하기

사용자 데이터가 증가함에 따라 중복된 사용자 프로필을 Braze 대시보드에서 병합할 수 있습니다. 이러한 중복 프로필은 동일한 검색어를 사용하여 찾아야 합니다. 고객 프로필을 복제하는 방법에 대한 자세한 내용은 [프로필 병합하기를]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles) 참조하세요.

[사용자 병합 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 사용하여 한 고객 프로필을 다른 고객 프로필에 병합할 수도 있습니다. 

{% alert note %}
고객 프로필이 병합된 후에는 이 작업을 취소할 수 없습니다.
{% endalert %}

## 추가 리소스
- 자세한 내용은 Braze [고객 프로필 수명주기에]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) 대한 글을 참조하세요.<br>
- [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention) 및 [웹용]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) 사용자 ID 설정 및 `changeUser()` 메서드 호출에 대한 설명서를 참조하세요.

