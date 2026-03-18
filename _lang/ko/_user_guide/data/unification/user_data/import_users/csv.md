---
nav_title: CSV import
article_title: "CSV import"
description: "CSV 가져오기를 사용하여 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아보세요."
page_order: 1.2
---

# CSV import

> CSV 가져오기를 사용하여 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아보세요.

## CSV 가져오기에 관하여

You can use CSV import to record and update the following user attributes and custom events.

|유형|Definition|Example|Maximum file size|
|---|---|---|---|
|Default Attributes|Reserved user attributes recognized by Braze.|`first_name`, `email`|500 MB|
|Custom Attributes|User attributes unique to your business.|`last_destination_searched`|500 MB|
|Custom Events|Events unique to your business that represent user actions.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSV 가져오기 사용

### 1단계: CSV 템플릿 다운로드

CSV 가져오기를 열려면, **오디언스** > **사용자 가져오기로** 이동하세요. 여기에는 최근 가져온 항목에 대한 세부 정보가 나열된 테이블이 있습니다. 여기에는 업로드 날짜, 업로더 이름, 파일 이름, 타겟팅 가능 여부, 가져온 행 수, 가져오기 상태 등이 포함됩니다.

CSV 작업을 시작하려면 속성 또는 이벤트용 템플릿을 다운로드하세요.

![Braze 대시보드의 '사용자 가져오기' 페이지입니다.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### 2단계: 식별자를 선택하십시오 {#choose-an-identifier}

가져오는 CSV에는 고유 식별자가 필요합니다. 다음 중에서 선택할 수 있습니다:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
고객 데이터를 가져올 때, 각 고객의 고유 식별자로`external_id`사용할 수 있습니다. 가져오기 `external_id`시  를 제공하면, Braze는 동일한  를 가진 기존`external_id` 사용자를 업데이트하거나, 해당`external_id`  가 설정된 새로 생성된 식별자를 가진 사용자를 생성합니다(해당 사용자가 존재하지 않을 경우).

- 다운로드: [CSV 속성 가져오기 템플릿: 외부 ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- 다운로드: [CSV 이벤트 가져오기 템플릿: 외부 ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
사용자 정보가 포함된`external_id`CSV와 포함되지 않은 CSV를 혼합하여 업로드하는 경우, 각 사용자 가져오기 작업마다 하나의 CSV 파일을 생성해야 합니다. 하나의 CSV 파일에는 사용자 별칭과 사용자`external_ids` ID를 동시에 포함할 수 없습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
사용자 별칭이 있는 사용자 목록을 가져와서 별칭이 없는 사용자를 `external_id`타겟팅할 수 있습니다. 별칭은 대체 고유 사용자 식별자 역할을 하며, 앱에 가입하거나 계정을 생성하지 않은 익명 사용자에게 마케팅을 시도할 때 유용할 수 있습니다.

사용자 프로필을 별칭만으로 업로드하거나 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `user_alias_name`: 고유 사용자 식별자; `external_id`의 대안  
- `user_alias_label`: 사용자 별칭을 그룹화하는 일반적인 레이블

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | 진실 |
| 182736486 | my_alt_identifier | 응우옌 | nguyen@user.com | 거짓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

가져오기 시  `user_alias_label`와  `user_alias_name`를 모두 제공하면, Braze는 동일한`user_alias_name`  와  를 가진 기존 `user_alias_label`사용자를 업데이트합니다. 사용자가 발견되지 않으면, Braze는 해당`user_alias_name`식별자로 새로 식별된 사용자를 생성합니다.

{% alert important %}
기존 사용자에게 이미 비밀번호가 설정된 경우 CSV 가져오기를`user_alias_name` 통해`external_id` 비밀번호를 업데이트할 수 없습니다. 대신, 이는 연관된 `user_alias_name`.과 함께 새로운 고객 프로필을 생성합니다. 별칭 전용 사용자를 `external_id`와(과) 연결하려면 [사용자 식별 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)를 사용하십시오.
{% endalert %}

다운로드: [CSV 속성 가져오기 템플릿: 사용자 별칭]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
`external_id` 또는 `user_alias_name`, `user_alias_label` 값 대신 내부 Braze ID 값을 사용하여 기존 고객 프로필을 업데이트하려면 열 헤더로 `braze_id`를 지정하세요.

이는 세분화 내의 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보낸 후 기존 사용자에게 새로운 사용자 지정 속성을 추가하려는 경우에 유용할 수 있습니다.

{% alert important %}
CSV 가져오기를 사용하여 새 사용자를 `braze_id`생성할 수 없습니다. 이 방법은 Braze 플랫폼 내에서 기존 사용자만 업데이트하는 데 사용할 수 있습니다.  
{% endalert %}

{% alert tip %}
Braze 대시보드의 CSV 내보내기에서 `braze_id` 값은 `Appboy ID`로 레이블이 지정될 수 있습니다. 이 ID는 사용자의 `braze_id`와 동일하므로 CSV를 다시 가져올 때 이 열의 이름을 `braze_id`로 변경할 수 있습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
외부 ID 또는 사용자 별칭을 생략하고 이메일 주소 또는 전화번호를 사용하여 사용자를 가져올 수 있습니다. 이메일 주소나 전화번호가 포함된 CSV 파일을 가져오기 전에 다음 사항을 확인하세요:

- CSV 파일에 이러한 프로필에 대한 외부 ID나 사용자 별칭이 없는지 확인합니다. 이 경우 Braze는 이메일 주소보다 외부 ID 또는 사용자 별칭을 우선적으로 사용하여 프로필을 식별합니다.  
- CSV 파일이 올바르게 형식화되었는지 확인하십시오.  

{% alert note %}
CSV 파일에 이메일 주소와 전화번호를 모두 포함하면, 프로필을 조회할 때 이메일 주소가 전화번호보다 우선시됩니다.
{% endalert %}

기존 프로필에 해당 이메일 주소나 전화번호가 있는 경우, 해당 프로필이 업데이트되며 Braze는 새 프로필을 생성하지 않습니다. 해당 이메일 주소와 동일한 여러 프로필이 있는 경우, Braze는 가장 최근에 업데이트된 프로필이 업데이트되는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)와 동일한 논리를 사용할 것입니다.

해당 이메일 주소나 전화번호를 가진 프로필이 존재하지 않으면, Braze는 해당 식별자로 새 프로필을 생성합니다. 당신은 나중에 이 [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)을 사용하여 이 프로필을 식별할 수 있습니다. 사용자 프로필을 삭제하려면 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 엔드포인트를 사용할 수도 있습니다.
{% endtab %}
{% endtabs %}

### 3단계: CSV 파일을 구축하세요

다음 데이터 유형 중 하나를 단일 CSV 파일로 업로드할 수 있습니다. 여러 데이터 유형을 업로드하려면 여러 CSV 파일을 업로드하십시오.

- **사용자 속성:** 이는 기본 및 커스텀 사용자 속성을 모두 포함합니다. 기본 사용자 속성은 Braze에서 예약된 키(예:`first_name`  또는 `email`)이며, 커스텀 속성은 귀사의 비즈니스에 고유한 사용자 속성(예: `last_destination_searched`)입니다.  
- **커스텀 이벤트:** 이러한 항목은 귀사의 비즈니스에 고유하며, 사용자가 취한 행동을 반영합니다. 예를 들어 여행 `trip_booked`예약 앱의 경우 다음과 같습니다.

CSV 파일 구축을 시작할 준비가 되면 다음 정보를 참조하십시오:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### 필수 식별자 {#required-identifiers-attributes}

CSV 파일에는 헤더로 다음 식별자 중 **하나를** 반드시 포함해야`external_id` 합니다. 각 항목에 대한 자세한 내용은 ['식별자 선택'을](#choose-an-identifier) 참조하십시오.

- `external_id`
- `braze_id`
- `user_alias_name` **그리고** `user_alias_label`
- `email`
- `phone`

#### Custom attributes

다음 데이터 유형은 CSV 가져오기 시 커스텀 속성으로 사용할 수 있습니다. [기본 속성과](#default-attributes) 정확히 일치하지 않는 열 헤더는 Braze에서 커스텀 속성으로 가져옵니다.

| Data Type | 설명 |
|---|---|
| Datetime | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장해야 합니다. |
| 부울 | `true` 또는 `false`를 수락합니다. |
| 숫자 | 공백이나 쉼표 없이 정수 또는 플로트여야 합니다. 플로트는 소수점 구분자로 점(`.`.)을 사용해야 합니다. |
| 문자열 | 값이 큰따옴표(`""`)로 묶여 있을 경우 쉼표를 포함할 수 있습니다. |
| Blank | 빈 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 기존 사용자 속성을 모두 포함할 필요는 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
사용자 가져오기에서는 배열, 푸시 토큰 및 커스텀 이벤트 데이터 유형을 지원하지 않습니다. CSV 파일 내 쉼표가 열 구분자로 해석되어 파일 구문 분석 시 오류를 발생시키기 때문입니다.<br><br>이러한 유형의 값을 업로드하려면 [엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [Cloud Data]({{site.baseurl}}/user_guide/data/cloud_ingestion/)[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)[ Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/)을 사용하십시오.
{% endalert %} 

#### 기본 속성

{% alert important %}
기본 속성을 가져올 때 사용하는 열 헤더는 기본 사용자 속성의 철자와 대소문자를 정확히 일치시켜야 합니다. 그렇지 않으면 Braze는 이를 [커스텀 ](#custom-attributes)속성으로 감지합니다.
{% endalert %}

사용자 가져오기에 사용할 수 있는 기본 속성은 다음과 같습니다.

| 사용자 프로필 필드 | Data Type | 설명 | 필수 사항인가요? |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 고객을 위한 고유 사용자 식별자. | 조건부로. [필수 식별자를](#required-identifiers-attributes) 참조하십시오. |
| `user_alias_name` | 문자열 | 익명 사용자를 위한 고유한 식별자로, `external_id`의 대안입니다. 반드시 함께 사용해야`user_alias_label` 합니다. | 조건부로. [필수 식별자를](#required-identifiers-attributes) 참조하십시오. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 일반적인 레이블. 반드시 함께 사용해야`user_alias_name` 합니다. | 조건부로. [필수 식별자를](#required-identifiers-attributes) 참조하십시오. |
| `first_name` | 문자열 | 사용자가 지정한 사용자의 이름(예: `Jane`)입니다. | 아니요 |
| `last_name` | 문자열 | 사용자가 지정한 사용자의 성(예: `Doe`)입니다. | 아니요 |
| `email` | 문자열 | 사용자가 표시한 사용자의 이메일(예: `jane.doe@braze.com`)입니다. | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 alpha-2 표준(예: `GB`)으로 Braze에 전달되어야 합니다. | 아니요 |
| `dob` | 문자열 | "YYYY-MM-DD" 형식으로 전달되어야 합니다(예: `1980-12-21`). 이 기능은 사용자의 생년월일을 가져와 생일이 "오늘"인 사용자를 타겟팅할 수 있게 합니다. | 아니요 |
| `gender` | 문자열 | “M”, “F”, “O”(기타), “N”(해당 없음), “P”(말하고 싶지 않음), 또는 nil(알 수 없음). | 아니요 |
| `home_city` | 문자열 | 사용자가 지정한 사용자의 고향 도시(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준(예: `en`)으로 Braze에 전달되어야 합니다. [허용된 언어 목록]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/)을 참조하십시오. | 아니요 |
| `phone` | 문자열 | 사용자가 지정한 전화번호, `E.164` 형식(예: `+442071838750`)입니다. 형식 지침은 [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)를 참조하십시오. | 아니요 |
| `email_open_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다. 이 사용자에게 향후 전송되는 모든 이메일에 열린 추적 픽셀이 추가되지 않도록 하려면 true로 설정합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다. | 아니요 |
| `email_click_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다. 이 사용자가 수신하는 향후 이메일 내 모든 링크에 대한 클릭 추적을 비활성화하려면 true로 설정하십시오. SparkPost 및 SendGrid에서만 사용할 수 있습니다. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(이메일 메시지를 수신하도록 명시적으로 등록됨), `unsubscribed`(이메일 메시지를 수신 거부함), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(푸시 메시지 수신을 명시적으로 등록), `unsubscribed`(푸시 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스와 동일한 형식(예: `America/New_York` 또는 `Eastern Time (US & Canada)`)으로 Braze에 전달해야 합니다. | 아니요 |
| `date_of_first_session`  `date_of_last_session` | 문자열 | 다음 ISO 8601 형식 중 하나로 전달될 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`. 이 식별자는 대시보드의 구독 그룹 페이지에서 찾을 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id`에 의해 지정된 구독 그룹의 구독 상태. 허용되는 값은 `unsubscribed`(구독 그룹에 속하지 않음) 또는 `subscribed`(구독 그룹에 속함)입니다. | 아니요, 그러나 `subscription_group_id`이(가) 사용되는 경우 강력히 권장됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### 구독 그룹 상태 업데이트 (선택 사항)

또한 사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 이는 SMS 채널로 메시지를 보내려면 사용자가 SMS 구독 그룹에 등록되어 있어야 하므로 SMS에 특히 유용합니다. 자세한 내용은 [SMS 구독 그룹](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)을 참조하십시오.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 개의 열이 있어야 합니다:

- `subscription_group_id`: `id`의 [구독 그룹](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: 사용 가능한 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 속함)입니다.

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | 구독됨 |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | 구독됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
사용자 가져오기에서 행당 하나의 `subscription_group_id`만 설정할 수 있습니다. 다른 행은 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 구독 그룹에 등록해야 하는 경우, 여러 번의 가져오기 작업을 수행해야 합니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### 필수 식별자 {#required-identifiers-custom-events}

CSV 파일에는 헤더로 다음 식별자 중 **하나를** 반드시 포함해야`external_id` 합니다. 각 항목에 대한 자세한 내용은 ['식별자 선택'을](#choose-an-identifier) 참조하십시오.

- `external_id`
- `braze_id`
- `user_alias_name` **그리고** `user_alias_label`
- `email`
- `phone`

#### 커스텀 이벤트 필드

다음 외에도 CSV 파일에는 이벤트 속성정보에 대한 추가 열 헤더가 포함될 수 있습니다. 이러한 속성에는 열 헤더가 있어야 합니다. `<event_name>.properties.<property name>.`

예를 들어, 커스텀 이벤트에는  및  `destination`속성이`trip_booked` 있을`duration` 수 있습니다. 이들은 열 헤더`trip_booked.properties.destination`  와  를 사용하여 `trip_booked.properties.duration`가져올 수 있습니다.

| 사용자 프로필 필드 | Data Type | 정보 | 필수 사항인가요? |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 사용자의 고유한 사용자 식별자입니다. | 조건부로. [필수 식별자를](#required-identifiers-custom-events) 참조하십시오. |
| `braze_id` | 문자열 | 사용자에 대해 Braze에서 할당된 식별자입니다. | 조건부로. [필수 식별자를](#required-identifiers-custom-events) 참조하십시오. |
| `user_alias_name` | 문자열 | 익명 사용자를 위한 고유한 사용자 식별자, 즉 .`external_id`의 대안입니다. 반드시 함께 사용해야`user_alias_label` 합니다. | 조건부로. [필수 식별자를](#required-identifiers-custom-events) 참조하십시오. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 일반적인 레이블. 반드시 함께 사용해야`user_alias_name` 합니다. | 조건부로. [필수 식별자를](#required-identifiers-custom-events) 참조하십시오. |
| `email` | 문자열 | 사용자가 표시한 사용자의 이메일(예: `jane.doe@braze.com`)입니다. | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조하십시오. |
| `phone` | 문자열 | 사용자가 지정한 전화번호, `E.164` 형식(예: `+442071838750`)입니다. 형식 지침은 [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)를 참조하십시오. | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조하십시오. |
| `name` | 문자열 | 사용자의 사용자 지정 이벤트. | 예 |
| `time` | 문자열 | 이벤트 시간입니다. 다음 ISO-8601 형식 중 하나로 전달될 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) | 예 |
| `<event name>.properties.<property name>` | 다중 | 사용자 지정 이벤트와 연결된 이벤트 속성입니다. 예는`trip_booked.properties.destination`입니다. | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### 4단계: 파일을 업로드하세요

파일을 업로드하려면 **속성** 또는 **이벤트를** 선택하고, **파일 찾아보기를** 클릭한 후 CSV 파일을 업로드하십시오. Braze는 처음 몇 행의 미리보기와 감지된 필드에 대한 요약을 표시합니다.

![업로드 완료 모달에는 파일 미리보기, 가져오기 이름 필드, 타겟팅 설정, 파일 유효성 검사 체크박스가 표시됩니다.]({% image_buster /assets/img/csv_import/upload_completed.png %})

**가져오기 이름** 필드에서 가져오기 항목의 이름을 변경할 수 있습니다. 기본값으로 파일 이름이 사용됩니다.

{% alert note %}
파일 미리보기에는 파일의 처음 몇 행만 표시됩니다. 가져오기 전에 모든 행을 확인하려면 [파일 유효성 검사를](#file-validation) 사용하십시오.
{% endalert %}

### 5단계: 파일 유효성 검사 (선택 사항) {#file-validation}

가져오기를 시작하기 전에 파일 유효성 검사를 실행하여 모든 행의 오류 및 경고를 확인할 수 있습니다. 파일을 검증하려면 **가져오기 전에 '파일 검증'을** 선택한 후 **'가져오기 시작'을** 클릭하십시오.

최대 허용 크기의 파일은 검증이 최대 2분까지 소요될 수 있습니다. 검증 실행 중에는 **'검증 건너뛰기'를** 선택하여 검증을 건너뛰고 즉시 진행할 수 있습니다.

#### 검증 결과

검증이 완료되면 다음 결과 중 하나가 표시됩니다.

| 결과 | 의미 | 다음 단계 |
|---|---|---|
| **검증 완료** | 문제가 발견되지 않았습니다. | **데이터 가져오기를** 선택하십시오. |
| **발견된 문제점** | 일부 행에 오류나 경고가 있습니다. | 오류 보고서를 다운로드하여 검토한 후, 계속 진행하려면 **'어쨌든 가져오기'를** 선택하거나 파일을 먼저 수정하려면 **'취소'를** 선택하십시오. |
| **검증 시간 초과** | 검증 시간이 초과되었습니다. 확인된 행에는 문제가 없었습니다. | **데이터 가져오기를** 선택하십시오. 전체 보고서는 몇 분 안에 제공될 예정입니다. |
| **검증 시간 초과 및 문제 발생** | 검증 시간이 초과되었으며, 확인한 일부 행에서 오류를 발견했습니다. | 부분 보고서를 다운로드하여 발견된 내용을 검토한 후, **'어쨌든 가져오기'** 또는 **'취소'를** 선택하십시오. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

![발견된 문제 대화 상자에는 오류 및 경고가 포함된 행 수가 표시되며, 취소, 오류 보고서 다운로드 또는 그대로 가져오기 옵션이 제공됩니다.]({% image_buster /assets/img/csv_import/validation_issues.png %})

#### 오류 보고서 이해하기

오류 보고서는 표시된 모든 행과 해당 원본 데이터, 문제 설명을 포함하는 CSV 파일입니다.

| 이슈 유형 | 설명 |
|---|---|
| **Error** | 해당 행은 가져오기 과정에서 완전히 건너뜁니다. |
| **경고** | 행은 가져오지만 일부 값은 생략됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

보고서를 검토한 후 원본 파일의 문제를 수정하여 재업로드하거나, 부분적인 결과를 수락하고 가져오기를 진행할 수 있습니다.

### Step 6: 타겟팅 설정 선택

다음과 같은 타겟팅 설정 중에서 선택할 수도 있습니다. 가져온 데이터로 새로운 타겟팅 필터나 세그먼트를 생성할 필요가 없다면, **'이 목록을 타겟팅 필터로 사용 가능하게 하지 않음'을** 선택하세요.

| 옵션 | 설명 |
|---|---|
| 타겟팅 필터 | 사용자 세그먼트를 구축할 때 CSV 파일을 리타겟팅 옵션으로 변환하려면, **'업데이트됨/CSV에서** **가져옴'** 드롭다운에서 파일을 선택한 후 **'타겟팅 필터 생성'을** 선택하세요. |
| 새로운 세그먼트 | 새 타겟팅 필터로 새 세그먼트를 생성하려면 **'타겟팅 필터 생성'을** 선택하고 **새 세그먼트에 추가하세요**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

!["업데이트됨/CSV에서 가져옴" 필터를 포함하는 필터 그룹으로, "할로윈 시즌 재미"라는 제목의 CSV 파일을 포함합니다.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### 7단계: CSV 가져오기를 시작하세요

준비가 되면 **'가져오기 시작'을** 클릭하세요. **사용자** **가져오기** 페이지에서 현재 진행 상황을 확인할 수 있으며, 해당 페이지는 5초마다 자동으로 새로고침됩니다.

{% alert note %}
한 번에 여러 개의 CSV를 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 순차적일 것이라고 보장할 수 없습니다. CSV 가져오기가 연달아 실행되도록 하려면, 첫 번째 CSV 가져오기가 완료된 후 두 번째 CSV를 업로드하세요.
{% endalert %}

#### 수입 상태

사용자 가져오기를 시작한 후에는 **'사용자** **가져오기'** 페이지에서 상태를 확인할 수 있습니다.

| 상태 | 설명 |
|---|---|
| **완료** | 모든 행이 성공적으로 가져왔습니다. |
| **부분적 성공** | 일부 행이 실패했습니다. 가져오기 옆에 있는 점 세 개 메뉴를 선택하여 오류 보고서 또는 원본 업로드된 CSV 파일을 다운로드하세요. |
| **진행 중** | 현재 가져오기가 실행 중입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![사용자 가져오기 페이지에 부분 성공 상태가 표시되고 컨텍스트 메뉴가 열려 있으며, '오류 보고서 다운로드' 및 '업로드된 CSV 다운로드' 옵션이 표시됩니다.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

수입 후 오류 보고서에는 Braze에 사용자가 존재하지 않는 경우처럼 유효성 검사에서 다루지 않는 사유로 실패한 행이 포함됩니다.

## 데이터 포인트 고려사항

CSV 파일에서 가져온 각 고객 데이터는 외부 ID 및 빈 값을 제외하고 고객 프로필의 기존 값을 덮어쓰고 데이터 포인트를 기록합니다. Braze 데이터 포인트의 세부 사항에 대해 궁금한 점이 있으시면, 담당 Braze 계정 매니저에게 문의하시면 답변을 받으실 수 있습니다.

| Consideration | 세부 정보 |
|---|---|
| 외부 ID | CSV 파일에  만 포함된 경우 데이터 `external_id`포인트가 기록되지 않습니다. 이를 통해 기존 Braze 사용자를 세그먼트할 수 있으며, 데이터 한도에 영향을 미치지 않습니다. 그러나  또는  `email`같은 필드를 포함하면 `phone`기존 사용자 데이터를 덮어쓰고 로그 데이터 포인트를 **기록합니다**. <br><br>세분화 목적으로만 사용되는 CSV 가져오기는 ,`braze_id` , 또는 만`external_id` 포함된 데이터 포인트와 같은`user_alias_name` 항목을 기록하지 않습니다. |
| 빈 값 | CSV 파일의 빈 값은 기존 고객 프로필 데이터를 덮어쓰지 않습니다. 가져올 때 모든 사용자 속성이나 커스텀 이벤트를 포함할 필요는 없습니다. |
| 구독 상태 | 업데이트`email_subscribe`, `push_subscribe`, `subscription_group_id`, 또는`subscription_state`  는 데이터 포인트 사용량에 포함되지 **않습니다**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자에게  또는`country`  을`language` 설정하면 Braze가 소프트웨어 개발 키트를 통해 이 정보를 자동으로 수집하지 못합니다.
{% endalert %}

## 문제 해결

[파일 검증을](#file-validation) 사용한 경우, 오류 보고서부터 확인하세요. 해당 보고서에는 표시된 각 행의 구체적인 문제점과 해결 방법이 설명되어 있습니다. 검증 단계가 아닌 가져오기 과정에서 실패한 행에 대해서는 **'사용자** **가져오기'** 페이지의 점 세 개 메뉴에서 오류 보고서를 다운로드하십시오.

CSV 가져오기에 문제가 발생하면 아래의 일반적인 문제점을 확인해 보세요. 아직도 도움이 필요하신가요? [support@로](mailto:support@braze.com) 문의하십시오[braze.com](mailto:support@braze.com).

### 파일 서식 문제

#### 잘못된 행

업로드가 오류와 함께 완료된 경우, CSV 파일에 잘못된 형식의 행이 있을 수 있습니다. 

데이터를 올바르게 가져오려면 헤더 행이 있어야 합니다. 각 행은 헤더 행과 동일한 수의 셀이 있어야 합니다. 길이가 헤더 행보다 크거나 작은 값의 행은 가져오기에서 제외됩니다. 값의 쉼표는 구분 기호로 해석되어 이 오류가 발생할 수 있습니다. 또한, 모든 데이터는 UTF-8로 인코딩되어야 합니다.

CSV 파일에 빈 행이 포함되어 있고, 가져온 행 수가 CSV 파일의 총 행 수보다 적더라도 이는 가져오기 문제로 간주되지 않을 수 있습니다. 빈 행은 가져올 필요가 없기 때문입니다. 올바르게 가져온 회선 수를 확인하고 가져오려는 사용자 수와 일치하는지 확인하세요.

#### 누락된 행

CSV 파일에 있는 총 행 수와 가져온 사용자 수가 일치하지 않을 수 있는 몇 가지 이유가 있습니다:

| Issue | 해상도 |
|---|---|
| 중복된 외부 ID, 사용자 별칭, Braze ID, 이메일 주소 또는 전화번호 | 외부 ID 열이 중복된 경우 행의 형식이 올바르게 지정되어 있어도 잘못된 형식이거나 가져오지 않은 행이 발생할 수 있습니다. 경우에 따라서는 특정 오류를 보고하지 않을 수 있습니다. 중복 파일을 확인하고 재업로드 전에 제거하십시오. |
| 악센트 부호가 있는 문자 | CSV 파일에는 악센트가 포함된 이름이나 속성이 포함될 수 있습니다. 파일의 UTF-8 인코딩을 확인하여 가져오기 문제를 방지하십시오. |
| Braze ID는 고아 상태의 사용자에게 속합니다 | 사용자가 다른 사용자와 병합되었고 Braze가 Braze ID를 남은 프로필과 연결할 수 없는 경우, 해당 행은 가져오지 않습니다. |
| 빈 행 | CSV 파일의 빈 행은 데이터 형식 오류가 발생할 수 있습니다. 엑셀이나 스프레드시트가 아닌 일반 텍스트 편집기로 확인하세요. |
| 이탈되지 않거나 불균형한 큰따옴표 (`"`) | 따옴표는 쉼표가 포함된 문자열 값을 감쌉니다. 값 자체에 큰따옴표(`""`")가 포함되어 있다면, 이를 이중으로 표시하여 이스케이프 처리합니다. 이스케이프되지 않았거나 불균형한 큰따옴표는 잘못된 형식의 행을 유발합니다. |
| 일관되지 않은 줄바꿈 | 혼합된 줄바꿈(e.g.,`\n`  및 `\r\n`)은 데이터의 첫 번째 행이 헤더의 일부로 처리될 수 있습니다. 16진수 또는 고급 텍스트 편집기를 사용하여 검사하고 수정하십시오. |
| 잘못 인코딩된 파일 | 악센트가 허용되더라도 파일은 반드시 UTF-8로 인코딩되어야 합니다. 다른 인코딩은 부분적으로 작동할 수 있으나 완전히 지원되지는 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 문자열 따옴표

작은따옴표(`''`) 또는 큰따옴표(`""`)로 묶은 값은 가져오기 시 문자열로 읽힙니다.

#### 잘못된 형식의 날짜

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아닌 날짜는 가져오기 시 `datetimes` 로 읽히지 않습니다.

### 데이터 구조 문제

#### 잘못된 이메일 주소

업로드가 오류와 함께 완료된 경우, 하나 이상의 유효하지 않은 암호화된 이메일 주소가 있을 수 있습니다. Braze로 이메일 주소를 가져오기 전에 모든 이메일 주소가 올바르게 암호화되었는지 확인하십시오.

- Braze에서 **[이메일 주소를 업데이트하거나 가져올]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users) 때**, 이메일이 포함된 모든 위치에서 해시 처리된 이메일 값을 사용하십시오. 이러한 해시 이메일 값은 귀사의 내부 팀에서 제공합니다. 
- **새 사용자를 생성할 때**, 사용자의 암호화된 이메일 값으로  를`email_encrypted` 추가해야 합니다. 그렇지 않으면 Braze는 사용자를 생성하지 않습니다. 마찬가지로, 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 반드시 .`email_encrypted`을 추가해야 합니다. 그렇지 않으면 Braze는 사용자를 업데이트하지 않습니다.

#### 커스텀 속성으로 가져온 데이터

기본 사용자 데이터(예: `email` 또는 `first_name`)를 사용자 지정 속성으로 가져온 경우 CSV 파일의 대소문자와 띄어쓰기를 확인하세요. 예를 들어,`First_name`  는 커스텀 속성으로 가져오지만,`first_name`  는 고객 프로필의 "이름" 필드에 올바르게 가져옵니다.

#### 여러 데이터 유형

Braze는 열의 각 값이 동일한 데이터 유형이어야 합니다. 속성의 데이터 유형과 일치하지 않는 값은 세분화 과정에서 오류를 발생시킵니다.

또한 숫자 속성을 0으로 시작하면 문제가 발생합니다. 0으로 시작하는 숫자는 문자열로 간주되기 때문입니다. Braze가 해당 문자열을 변환할 때, 해당 문자열은 8진수 값(0부터 7까지의 숫자를 사용)으로 처리될 수 있습니다. 즉, 해당 값은 대응하는 10진수 값으로 변환됩니다. 예를 들어, CSV 파일의 값이 0130인 경우 Braze 프로필에는 88이 표시됩니다. 이 문제를 방지하려면 문자열 데이터 유형의 속성을 사용하십시오. 그러나 이 데이터 유형은 세분화 번호 비교에서는 사용할 수 없습니다.

#### 기본 속성 유형

일부 기본 속성은 사용자 업데이트 시 특정 값만 유효한 값으로 허용할 수 있습니다. 가이드라인은 [CSV 생성 방법을]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv) 참조하십시오.

뒤에 붙은 공백과 대소문자 차이가 값을 유효하지 않은 것으로 해석되게 할 수 있습니다. 예를 들어, 다음 CSV 파일에서 첫 번째 행의 사용자(`brazetest1`)만 이메일 및 푸시 상태가 성공적으로 업데이트되었습니다. 허용되는 `opted_in`값은 , `subscribed`, `unsubscribed`및 이기 때문입니다. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "CSV 파일 선택"이 작동하지 않습니다

**CSV 파일 선택** 버튼이 작동하지 않을 수 있는 몇 가지 이유가 있습니다:

| Issue | 해상도 |
|---|---|
| 팝업 차단기 | 이로 인해 페이지가 표시되지 않을 수 있습니다. 브라우저에서 Braze 대시보드 웹사이트의 팝업 창을 허용하도록 설정되어 있는지 확인하십시오. |
| 구형 브라우저 | 브라우저가 최신 버전인지 확인하십시오. 그렇지 않다면 최신 버전으로 업데이트하십시오. |
| 백그라운드 프로세스 | 모든 브라우저 인스턴스를 닫은 후 컴퓨터를 재시작하십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
