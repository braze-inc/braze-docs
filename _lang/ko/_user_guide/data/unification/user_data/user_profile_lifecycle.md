---
nav_title: 고객 프로필 수명주기
article_title: 고객 프로필 수명주기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze 고객 프로필 수명주기와 고객 프로필을 식별하고 참조할 수 있는 다양한 방법에 대해 설명합니다."

---

# 고객 프로필 수명주기

> 이 문서에서는 Braze 고객 프로필 수명주기와 고객 프로필을 식별하고 참조하는 다양한 방법에 대해 설명합니다. 고객 생애주기를 더 잘 이해하고 싶다면 [사용자 라이프사이클 매핑에](https://learning.braze.com/mapping-customer-lifecycles) 대한 Braze 학습 과정을 확인해 보세요.

사용자와 관련된 모든 영구 데이터는 사용자 프로필에 저장됩니다. API를 통해 또는 소프트웨어 개발 키트에서 사용자를 인식하여 고객 프로필을 생성한 후에는 해당 프로필에 여러 매개변수를 할당하여 해당 사용자를 식별하고 참조할 수 있습니다. 

이러한 매개 변수에는 다음이 포함됩니다:

* `braze_id` (Braze에서 지정)
* `external_id`
* `email`
* `phone`
* 설정한 사용자 별칭 지정 수 제한 없음

## 익명 사용자 프로필

지정된 `external_id` 주소가 없는 모든 사용자를 [익명 사용자라고]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) 합니다. 예를 들어 웹사이트를 방문했지만 가입하지 않은 사용자나 모바일 앱을 다운로드했지만 프로필을 만들지 않은 사용자 등이 이에 해당할 수 있습니다.

처음에 소프트웨어 개발 키트에서 사용자를 인식하면 관련 `braze_id`: Braze에 의해 자동으로 할당되고 편집할 수 없으며 기기별로 고유한 식별자를 가진 익명 사용자 프로필이 생성됩니다. 이 식별자는 [API를]({{site.baseurl}}/api/endpoints/user_data/) 통해 고객 프로필을 업데이트하는 데 사용할 수 있습니다.

## 식별된 고객 프로필

앱에서 사용자를 인식할 수 있게 되면(사용자 ID 또는 이메일 주소를 제공함으로써) `changeUser` 방법을 사용하여 해당 사용자의 프로필에 `external_id` 을 할당하는 것이 좋습니다[(웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). `external_id` 을 사용하면 여러 기기에서 동일한 고객 프로필을 식별할 수 있습니다.

`external_id` 사용의 추가 혜택은 다음과 같습니다: 

- 여러 기기와 플랫폼에서 일관된 사용자 경험을 제공하세요(예: iPhone 앱의 충성도가 높은 사용자에게는 Android 태블릿에 휴면 사용자 알림을 보내지 않음).
- 사용자가 앱을 삭제했다가 다시 설치하거나 다른 기기에 앱을 설치할 때마다 새로운 고객 프로필을 생성하지 않는지 확인하여 분석의 정확성을 향상하세요.
- [사용자 데이터 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/) 사용하여 앱 외부의 소스에서 사용자 데이터 가져오기를 인에이블먼트하고 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/) 사용하여 트랜잭션 메시지로 사용자를 타겟팅하세요.
- 세그먼트 내의 "테스트" [필터를]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) 사용하여 개별 사용자를 검색하고, 세그먼트 내에서 [**사용자 검색**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) 페이지에서 검색합니다.

### 외부 ID에 대한 고려 사항

{% alert warning %}
고객 프로필에 `external_id` 을 할당하지 마세요. 고객 프로필을 고유하게 식별할 수 있어야 합니다. 사용자를 식별한 후에는 익명으로 되돌릴 수 없습니다.
<br><br>
[`/users/external_ids/rename` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) 사용하여 `external_id` 을 업데이트할 수 있습니다. 그러나 사용자 세션 중에 다른 `external_id` 을 설정하려고 시도하면 새로운 `external_id` 이 연결된 새 고객 프로필이 생성됩니다. 두 프로필 간에 데이터가 전달되지 않습니다.
{% endalert %} 

#### 이메일 또는 해시된 이메일을 외부 ID로 사용할 위험성

이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있지만, 사용자 개인정보 및 데이터 보안에 대한 잠재적 위험을 고려하는 것이 중요합니다.

- **추측 가능한 정보:** 이메일 주소는 쉽게 추측할 수 있어 공격에 취약합니다.
- **악용 위험:** 악의적인 사용자가 웹 브라우저를 변경하여 다른 사람의 이메일 주소를 외부 ID로 보내는 경우, 민감한 메시지나 계정 정보에 액세스할 수 있습니다.

### 익명 사용자를 식별하면 어떻게 되나요?

익명 사용자를 식별할 때는 두 가지 시나리오 중 하나가 발생할 수 있습니다:

1) **익명 사용자가 새로운 식별자 사용자가 됩니다:** <br>`external_id` 이 아직 Braze에 존재하지 않는 경우 익명 사용자는 새로 식별된 사용자가 되며 익명 사용자의 모든 속성과 기록을 그대로 유지합니다. 

2) **익명 사용자는 이미 존재하는 사용자로 식별됩니다:** <br>`external_id` 이 이미 Braze에 존재하는 경우 이 사용자는 이전에 다른 기기(예: 태블릿)나 가져온 사용자 데이터 등 다른 방식으로 시스템에서 사용자로 식별된 것입니다. 

즉, 이 사용자에 대한 고객 프로필이 이미 있습니다. 이 인스턴스에서 Braze는 다음을 수행합니다:
1. 익명 사용자 고아 만들기
2. 익명 프로필에서 식별된 사용자 프로필에 아직 존재하지 않는 [특정 사용자 프로필 필드를]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) 병합합니다.
3. 사용자 기반에서 익명 사용자 프로필을 제거하여 사용자 수가 부풀려지지 않도록 하세요.

익명 사용자와 알려진 사용자 모두 이름이 있는 경우 알려진 사용자의 이름이 유지됩니다. 알려진 사용자에 null 값이 있고 익명 사용자에게 값이 있는 경우 익명 사용자의 값이 이러한 [특정 사용자 프로필 필드에]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) 해당하는 경우 익명 사용자의 값이 알려진 사용자의 프로필에 병합됩니다.

고객 프로필에 대해 `external_id` 을 설정하는 방법에 대한 자세한 내용은 설명서를 참조하세요[(iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [웹]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## 사용자 별칭 지정

Braze 이외의 식별자로 사용자를 참조하려면 `external_id`, 사용자 프로필에 대해 사용자 별칭을 지정합니다. 사용자 프로필에 대해 설정된 별칭은 사용자의 `braze_id` 또는 `external_id` 을 대체하는 것이 아니라 추가로 작동합니다. 사용자 프로필에 대해 설정할 수 있는 별칭 지정 수에는 제한이 없습니다.

각 별칭은 별칭의 키를 정의하는 `alias_label` 과 값을 정의하는 `alias_name` 의 두 부분으로 구성된 키-값 페어로 작동합니다. 단일 레이블에 대한 `alias_name` 은 `external_id` 과 마찬가지로 사용자 기반 전체에서 고유해야 합니다. 기존 레이블과 이름 조합으로 두 번째 고객 프로필을 업데이트하려고 하면 사용자 프로필이 업데이트되지 않습니다.

### 사용자 별칭 지정 업데이트하기

별칭은 [사용자 데이터 엔드포인트를]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) 사용하거나 SDK를 통해 새 이름을 전달하여 설정한 후 해당 라벨의 새 이름으로 업데이트할 수 있습니다. 그러면 해당 사용자 데이터를 내보낼 때 사용자 별칭 지정이 표시됩니다.

\![사용자 별칭 라벨은 같지만 별칭 이름이 다른 별도의 사용자에 대한 두 개의 다른 고객 프로필 만들기]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### 익명 사용자 태그 지정하기

또한 사용자 별칭 지정을 통해 익명 사용자에게 식별자를 태그할 수 있습니다. 예를 들어 사용자가 전자상거래 사이트에 이메일 주소를 제공했지만 아직 가입하지 않은 경우 해당 이메일 주소를 해당 익명 사용자의 별칭으로 사용할 수 있습니다. 그런 다음 이러한 사용자는 사용자 별칭 지정을 사용하여 내보내거나 API에서 참조할 수 있습니다.

### 익명 사용자 프로필의 사용자 별칭 지정 동작

별칭이 있는 익명 사용자 프로필이 나중에 `external_id` 으로 인식되면 정상적으로 식별된 사용자 프로필로 취급되지만 기존 별칭은 그대로 유지되며 해당 별칭으로 계속 참조할 수 있습니다.

### 알려진 사용자 프로필에 사용자 별칭 지정하기

알려진 사용자 프로필에 사용자 별칭을 설정하여 외부에 알려진 다른 ID로 알려진 사용자를 참조할 수도 있습니다. 예를 들어, 사용자가 Braze 내에서 참조하고자 하는 비즈니스 인텔리전스 도구 ID(예: Amplitude ID)를 가지고 있을 수 있습니다.

사용자 별칭 지정 방법에 대한 자세한 내용은 각 플랫폼[(iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users))에 대한 설명서를 참조하세요.

Braze에서 고객 프로필 수명주기의 흐름도. 익명 사용자에 대해 changeUser()가 호출되면 해당 사용자는 식별된 사용자가 되고 데이터는 식별된 사용자 프로필로 마이그레이션됩니다. 식별된 사용자에게는 Braze ID와 외부 ID가 있습니다. 이 때 두 번째 익명 사용자가 changeUser()를 호출하면 식별된 사용자에 아직 존재하지 않는 사용자 데이터 필드가 병합됩니다. 식별된 사용자가 기존 사용자 프로필에 별칭을 추가한 경우 데이터는 영향을 받지 않지만 별칭이 있는 식별된 사용자가 됩니다. 식별된 사용자와 별칭 라벨은 같지만 별칭 이름이 다른 세 번째 익명 사용자가 changeUser()를 호출하면 식별된 사용자에 존재하지 않는 모든 필드가 병합되고 식별된 사용자 프로필의 별칭 라벨이 유지됩니다.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
고객 프로필 수명주기가 어떻게 될지 상상하기 어렵나요? 사용자 데이터 수집 모범 사례를 보려면 [모범]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) 사례를 방문하세요.
{% endalert %}

## 고급 사용 사례

SDK와 [사용자 데이터 엔드포인트를]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint) 사용하는 API를 통해 기존에 식별된 사용자 프로필에 대해 새로운 사용자 별칭을 설정할 수 있습니다. 그러나 알 수 없는 기존 고객 프로필에 대해서는 API를 통해 사용자 별칭을 지정할 수 없습니다.

이 과정에서 사용자 별칭 지정도 병합됩니다. 단, 고아 처리할 사용자와 대상 사용자 모두 동일한 레이블의 별칭을 가지고 있는 경우 대상 사용자의 별칭만 유지됩니다.

앱을 삭제했다가 다시 설치하면 해당 사용자에 대해 새로운 익명 사용자 아이디( `braze_id` )가 생성됩니다.

### 사용자 ID로 문제 해결하기

모든 사용자 ID는 대시보드 내에서 테스트 사용자를 찾고 식별하는 데 사용할 수 있습니다. Braze 대시보드에서 사용자를 찾으려면 [테스트 사용자 추가하기를]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) 참조하세요.

{% alert important %}
Braze는 세션 수가 5,000,000개가 넘는 사용자("더미 사용자")를 금지 또는 차단하며, 이러한 사용자는 일반적으로 잘못된 통합의 결과이므로 더 이상 해당 사용자의 소프트웨어 개발 키트 이벤트를 수집하지 않습니다. 합법적인 사용자에게 이런 일이 발생한 것을 발견하면 Braze 계정 매니저에게 문의하세요.
{% endalert %}