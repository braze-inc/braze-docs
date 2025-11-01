---
nav_title: CSV 사용
article_title: "CSV 가져오기"
description: "CSV 가져오기를 사용하여 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아보세요."
page_order: 1.2
---

# CSV 가져오기

> CSV 가져오기를 사용하여 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트하는 방법을 알아보세요.

## CSV 가져오기 정보

CSV 가져오기를 사용하여 다음 사용자 속성 및 커스텀 이벤트를 기록하고 업데이트할 수 있습니다.

|유형|정의|예|최대 파일 크기|
|---|---|---|---|
|기본 속성|Braze에서 인식한 예약 사용자 속성.|`first_name`, `email`|500MB|
|커스텀 속성|비즈니스에 고유한 사용자 속성.|`last_destination_searched`|500MB|
|커스텀 이벤트|사용자 행동을 담당하는 비즈니스 고유의 이벤트.|`trip_booked`|50MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## CSV 가져오기 사용

### 1단계: CSV 템플릿 다운로드

CSV 가져오기를 열려면 **오디언스** > **사용자 가져오기로** 이동합니다. 여기에는 업로드 날짜, 업로더 이름, 파일 이름, 타겟팅 사용 가능성, 가져온 행 수, 가져오기 상태 등 가장 최근 가져오기에 대한 세부 정보가 나열된 표가 있습니다.

CSV를 시작하려면 속성 또는 이벤트에 대한 템플릿을 다운로드하세요.

Braze 대시보드의 '사용자 가져오기' 페이지.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### 2단계: 식별자 선택 {#choose-an-identifier}

가져오는 CSV에는 전용 식별자가 필요합니다. 다음 중에서 선택할 수 있습니다:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
고객 데이터를 가져올 때 `external_id` 을 각 고객의 고유 식별자로 사용할 수 있습니다. 사용자 가져오기에 `external_id` 을 입력하면 Braze는 기존 사용자를 동일한 `external_id` 으로 업데이트하거나, 사용자를 찾을 수 없는 경우 `external_id` 을 설정하여 새로 식별된 사용자를 생성합니다.

- 다운로드: [CSV 속성 가져오기 템플릿: 외부 ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- 다운로드: [CSV 이벤트 가져오기 템플릿: 외부 ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
`external_id` 주소가 있는 사용자와 없는 사용자를 혼합하여 업로드하는 경우 각 가져오기마다 하나의 CSV를 만들어야 합니다. 하나의 CSV에는 `external_ids` 및 사용자 별칭 지정이 모두 포함될 수 없습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
`external_id` 이 없는 사용자를 타겟팅하려면 사용자 별칭 지정이 있는 사용자 목록을 가져오기하면 됩니다. 별칭은 대체 고유 사용자 식별자 역할을 하며, 앱에 가입하거나 계정을 만들지 않은 익명 사용자를 대상으로 마케팅하려는 경우 유용하게 사용할 수 있습니다.

사용자 별칭 지정만 있는 고객 프로필을 업로드하거나 업데이트하는 경우 CSV에 다음 두 개의 열이 있어야 합니다:

- `user_alias_name`: 고유한 사용자 식별자, 즉 `external_id`  
- `user_alias_label`: 사용자 별칭을 그룹화하기 위한 공통 라벨

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

사용자 가져오기에 `user_alias_name` 와 `user_alias_label` 을 모두 제공하면 Braze는 기존 사용자를 동일한 `user_alias_name` 와 `user_alias_label` 로 업데이트합니다. 사용자를 찾을 수 없는 경우 Braze는 해당 `user_alias_name` 설정으로 새로 식별된 사용자를 생성합니다.

{% alert important %}
기존 사용자가 이미 `external_id` 을 가지고 있는 경우 CSV 가져오기를 사용하여 기존 사용자를 `user_alias_name` 으로 업데이트할 수 없습니다. 대신 `user_alias_name` 으로 연결된 새 고객 프로필이 생성됩니다. 별칭 전용 사용자를 `external_id` 에 연결하려면 [사용자 식별자 지정 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) 사용합니다.
{% endalert %}

다운로드: [CSV 속성 가져오기 템플릿: 사용자 별칭 지정]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
`external_id` 또는 `user_alias_name`, `user_alias_label` 값 대신 내부 Braze ID 값을 사용하여 기존 고객 프로필을 업데이트하려면 열 헤더로 `braze_id` 을 지정하세요.

이 기능은 세분화 내에서 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보내고 기존 사용자에게 새로운 커스텀 속성을 추가하려는 경우에 유용할 수 있습니다.

{% alert important %}
`braze_id` 을 사용하여 새 사용자를 만드는 데는 CSV 가져오기를 사용할 수 없습니다. 이 방법은 Braze 플랫폼 내에서 기존 사용자를 업데이트하는 데만 사용할 수 있습니다.  
{% endalert %}

{% alert tip %}
Braze 대시보드의 CSV 내보내기에서 `braze_id` 값은 `Appboy ID` 으로 레이블이 지정될 수 있습니다. 이 ID는 사용자의 `braze_id` 와 동일하므로 CSV를 다시 가져오기 할 때 이 열의 이름을 `braze_id` 로 변경할 수 있습니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
외부 ID 또는 사용자 별칭 지정을 생략하고 이메일 주소나 전화번호를 사용하여 사용자 가져오기를 할 수 있습니다. 이메일 주소나 전화번호가 포함된 CSV 파일을 가져오기 전에 다음 사항을 확인하세요:

- CSV 파일에 이러한 프로필에 대한 외부 ID 또는 사용자 별칭 지정이 없는지 확인합니다. 이 경우 Braze는 이메일 주소보다 외부 ID 또는 사용자 별칭을 우선적으로 사용하여 프로필을 식별합니다.  
- CSV 파일의 형식이 올바르게 지정되었는지 확인합니다.  

{% alert note %}
CSV 파일에 이메일 주소와 전화번호를 모두 포함하면 프로필을 조회할 때 전화번호보다 이메일 주소가 우선시됩니다.
{% endalert %}

기존 프로필에 해당 이메일 주소 또는 휴대폰 번호가 있는 경우 해당 프로필이 업데이트되며 Braze는 새 프로필을 만들지 않습니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우 Braze는 [`/users/track` 엔드포인트와]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 동일한 로직을 사용하여 가장 최근에 업데이트된 프로필을 업데이트합니다.

해당 이메일 주소 또는 휴대폰 번호가 포함된 프로필이 없는 경우 Braze는 해당 식별자를 사용하여 새 프로필을 생성합니다. 나중에 [`/users/identify` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) 사용하여 이 프로필을 식별할 수 있습니다. 고객 프로필을 삭제하려면 다음을 사용할 수도 있습니다. [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) 엔드포인트를 사용할 수도 있습니다.
{% endtab %}
{% endtabs %}

### 3단계: CSV 파일 구축하기

다음 데이터 유형 중 하나를 단일 CSV 파일로 업로드할 수 있습니다. 두 개 이상의 데이터 유형을 업로드하려면 여러 개의 CSV 파일을 업로드하세요.

- **사용자 속성:** 여기에는 기본 및 커스텀 사용자 속성이 모두 포함됩니다. 기본 사용자 속성은 Braze에 예약된 키(예: `first_name` 또는 `email`)이며 커스텀 속성은 비즈니스에 고유한 사용자 속성(예: `last_destination_searched`)입니다.  
- **커스텀 이벤트:** 이는 비즈니스에 고유하며 사용자가 수행한 작업(예: 여행 예약 앱의 경우 `trip_booked` )을 반영합니다.

CSV 파일 구축을 시작할 준비가 되면 다음 정보를 참조하세요:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### 필수 식별자 {#required-identifiers-attributes}

`external_id` 은 필수는 아니지만 다음 식별자 중 **하나를** CSV 파일의 헤더로 **포함해야** 합니다. 각 항목에 대한 자세한 내용은 [식별자 선택을](#choose-an-identifier) 검토하세요.

- `external_id`
- `braze_id`
- `user_alias_name` **그리고** `user_alias_label`
- `email`
- `phone`

#### 커스텀 속성

다음 데이터 유형을 CSV 가져오기에 대한 커스텀 속성으로 사용할 수 있습니다. [기본 속성과](#default-attributes) 정확히 일치하지 않는 열 헤더에는 Braze에서 커스텀 속성이 부여됩니다.

| 데이터 유형 | 설명 |
|---|---|
| 날짜 시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장해야 합니다. |
| 부울 | 수락 `true` 또는 `false`. |
| 번호 | 공백이나 쉼표가 없는 정수 또는 플로트여야 합니다. 플로트는 소수점 구분 기호로 마침표(`.`)를 사용해야 합니다. |
| 문자열 | 값을 큰따옴표(`""`)로 묶은 경우 쉼표를 포함할 수 있습니다. |
| 공백 | 빈 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 기존의 모든 사용자 속성을 포함할 필요는 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
배열, 푸시 토큰 및 커스텀 이벤트 데이터 유형은 사용자 가져오기에서 지원되지 않습니다. CSV 파일의 쉼표는 열 구분 기호로 해석되어 파일을 구문 분석하는 동안 오류가 발생할 수 있기 때문입니다.<br><br>이러한 종류의 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [클라우드 데이터 수집을]({{site.baseurl}}/user_guide/data/cloud_ingestion/) 대신 사용하세요.
{% endalert %} 

#### 기본 속성

{% alert important %}
기본 속성을 가져오기 할 때 사용하는 열 헤더는 기본 사용자 속성의 철자 및 대문자와 정확히 일치해야 합니다. 그렇지 않으면 Braze는 이를 [커스텀 속성으로](#custom-attributes) 대신 감지합니다.
{% endalert %}

| 고객 프로필 필드 | 데이터 유형 | 설명 | 필수 사항인가요? |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 고객을 위한 고유한 사용자 식별자입니다. | 조건부. [필수 식별자를](#required-identifiers-attributes) 참조하세요. |
| `user_alias_name` | 문자열 | `external_id` 대신 사용할 수 있는 익명 사용자를 위한 고유한 사용자 식별자입니다. `user_alias_label` 와 함께 사용해야 합니다. | 조건부. [필수 식별자를](#required-identifiers-attributes) 참조하세요. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화할 수 있는 공통 라벨입니다. `user_alias_name` 와 함께 사용해야 합니다. | 조건부. [필수 식별자를](#required-identifiers-attributes) 참조하세요. |
| `first_name` | 문자열 | 사용자가 지정한 사용자의 이름(예: `Jane`)입니다. | 아니요 |
| `last_name` | 문자열 | 사용자가 지정한 사용자의 성(예: `Doe`)입니다. | 아니요 |
| `email` | 문자열 | 사용자가 지정한 사용자의 이메일(예: `jane.doe@braze.com`). | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 알파-2 표준(예: `GB`)에 따라 Braze에 전달해야 합니다. | 아니요 |
| `dob` | 문자열 | "YYYY-MM-DD" 형식(예: `1980-12-21`)으로 전달해야 합니다. 이렇게 하면 사용자의 생년월일을 가져와서 생일이 '오늘'인 사용자를 타겟팅할 수 있습니다. | 아니요 |
| `gender` | 문자열 | "M", "F", "O"(기타), "N"(해당 없음), "P"(말하지 않음) 또는 없음(알 수 없음)입니다. | 아니요 |
| `home_city` | 문자열 | 사용자가 지정한 사용자의 고향 도시(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준(예: `en`)에 따라 Braze에 전달되어야 합니다. [허용되는 언어 목록을]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/) 참조하세요. | 아니요 |
| `phone` | 문자열 | 사용자가 지정한 전화번호, `E.164` 형식(예: `+442071838750`)입니다. 서식 지정 지침은 [사용자 전화번호를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) 참조하세요. | 아니요 |
| `email_open_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다. 이 사용자에게 향후 전송되는 모든 이메일에 열린 상태 추적 픽셀이 추가되지 않도록 하려면 true로 설정합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다. | 아니요 |
| `email_click_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다. 이 사용자에게 전송되는 향후 이메일 내의 모든 링크에 대한 클릭 추적을 사용하지 않으려면 true로 설정합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값은 `opted_in` (명시적으로 이메일 메시지 수신 등록), `unsubscribed` (명시적으로 이메일 메시지 수신 거부), `subscribed` (옵트인/옵트아웃 모두 없음)입니다. | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값은 `opted_in` (푸시 메시지를 수신하도록 명시적으로 등록됨), `unsubscribed` (푸시 메시지를 명시적으로 수신 거부함), `subscribed` (옵트인하지도 옵트아웃하지도 않음)입니다. | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스와 동일한 형식(예: `America/New_York` 또는 `Eastern Time (US & Canada)`)으로 Braze에 전달해야 합니다. | 아니요 |
| `date_of_first_session`  `date_of_last_session` | 문자열 | 다음 ISO 8601 형식 중 하나로 전달할 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`. 이 식별자는 대시보드의 구독 그룹 페이지에서 찾을 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id` 에서 지정한 구독 그룹에 대한 구독 상태입니다. 허용되는 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 속함)입니다. | 아니요, 하지만 `subscription_group_id` 을 사용하는 경우 강력히 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### 구독 그룹 상태 업데이트하기(선택 사항)

또한 사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 사용자가 SMS 채널을 통해 메시지를 받으려면 SMS 구독 그룹에 등록되어 있어야 하므로 이는 특히 SMS에 유용합니다. 자세한 내용은 [SMS 구독 그룹을](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) 참조하세요.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 개의 열이 있어야 합니다:

- `subscription_group_id`: [구독 그룹의](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) `id`.  
- `subscription_state`: 사용 가능한 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 속함)입니다.

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | 콜비 | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | 가입한 가입자 |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | 가입한 가입자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
사용자 가져오기의 행당 `subscription_group_id` 하나만 설정할 수 있습니다. 행마다 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 구독 그룹에 등록해야 하는 경우에는 여러 번 사용자 가져오기를 수행해야 합니다.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### 필수 식별자 {#required-identifiers-custom-events}

`external_id` 은 필수는 아니지만 다음 식별자 중 **하나를** CSV 파일의 헤더로 **포함해야** 합니다. 각 항목에 대한 자세한 내용은 [식별자 선택을](#choose-an-identifier) 검토하세요.

- `external_id`
- `braze_id`
- `user_alias_name` **그리고** `user_alias_label`
- `email`
- `phone`

#### 커스텀 이벤트 필드

CSV에는 다음 외에도 이벤트 속성정보에 대한 추가 열 헤더가 포함될 수 있습니다. 이러한 속성의 열 헤더는 `<event_name>.properties.<property name>.`

예를 들어, 커스텀 이벤트 `trip_booked` 에는 `destination` 및 `duration` 속성이 있을 수 있습니다. 열 헤더를 `trip_booked.properties.destination` 및 `trip_booked.properties.duration` 로 지정하여 가져올 수 있습니다.

| 고객 프로필 필드 | 데이터 유형 | 정보 | 필수 사항인가요? |
| :---- | :---- | :---- | :---- |
| `external_id` | 문자열 | 사용자의 고유한 사용자 식별자입니다. | 조건부. [필수 식별자를](#required-identifiers-custom-events) 참조하세요. |
| `braze_id` | 문자열 | 사용자에 대해 Braze가 지정한 식별자입니다. | 조건부. [필수 식별자를](#required-identifiers-custom-events) 참조하세요. |
| `user_alias_name` | 문자열 | `external_id` 대신 사용할 수 있는 익명 사용자를 위한 고유한 사용자 식별자 입니다. `user_alias_label` 와 함께 사용해야 합니다. | 조건부. [필수 식별자를](#required-identifiers-custom-events) 참조하세요. |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화할 수 있는 공통 라벨입니다. `user_alias_name` 와 함께 사용해야 합니다. | 조건부. [필수 식별자를](#required-identifiers-custom-events) 참조하세요. |
| `email` | 문자열 | 사용자가 지정한 사용자의 이메일(예: `jane.doe@braze.com`). | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조하세요. |
| `phone` | 문자열 | 사용자가 지정한 전화번호, `E.164` 형식(예: `+442071838750`)입니다. 서식 지정 지침은 [사용자 전화번호를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) 참조하세요. | 아니요, 다른 식별자가 없는 경우에만 사용할 수 있습니다. 다음 참고 사항을 참조하세요. |
| `name` | 문자열 | 사용자의 커스텀 이벤트. | 예 |
| `time` | 문자열 | 이벤트 시간입니다. 다음 ISO-8601 형식 중 하나로 전달할 수 있습니다: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) | 예 |
| `<event name>.properties.<property name>` | 여러 | 커스텀 이벤트와 관련된 이벤트 속성정보입니다. 예를 들면 다음과 같습니다. `trip_booked.properties.destination` | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### 4단계: 데이터 업로드 및 미리 보기

Braze가 CSV를 처리하기 전에 처음 몇 행의 미리 보기를 생성하여 문제가 있는지 확인할 수 있습니다. 미리보기를 생성하려면 **속성** 또는 **이벤트를** 선택한 다음 **파일 찾아보기를** 선택하고 CSV 파일을 업로드합니다. 

<!-- old image -->
\![단일 열에 데이터 유형이 혼합된 오류와 함께 CSV 업로드가 완료됨]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
사용자 가져오기 미리보기는 입력 파일의 모든 행을 검사하지 않습니다. 상위 몇 행 이후의 오류는 잡히지 않을 수 있으므로 CSV 파일 전체를 검토해 보세요.
{% endalert %}

### 5단계: 타겟팅 기본 설정 선택하기

다음 타겟팅 기본 설정 중에서 선택할 수도 있습니다. 가져오기에서 새 타겟팅 필터 또는 세그먼트를 만들 필요가 없는 경우 **이 목록을 타겟팅 필터로 사용할 수 없도록 설정하지 않음을** 선택합니다.

| 옵션 | 설명 |
|---|---|
| 타겟팅 필터 | 사용자 세그먼트를 구축할 때 CSV 파일을 리타겟팅 옵션으로 변환하려면 **CSV에서 업데이트/가져오기** 드롭다운에서 파일을 선택한 다음 **타겟팅 필터 생성을** 선택합니다. |
| 새로운 세그먼트 세분화 | 또한 새 타겟팅 필터에서 새 세그먼트를 만들려면 **타겟팅 필터 만들기 및 새 세그먼트에 추가** 를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

"할로윈 시즌 재미"라는 제목의 CSV 파일이 포함된 "업데이트/가져온 CSV" 필터 그룹이 있습니다.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### 6단계: CSV 가져오기 시작

준비가 완료되면 **가져오기 시작을** 선택합니다. 5초마다 자동으로 새로고침되는 **사용자 가져오기** 페이지에서 현재 진행 상황을 추적할 수 있습니다.

문제가 없으면 상태가 **완료로** 업데이트되고 처리된 행 수가 표시됩니다. 처리된 행의 모든 데이터는 기존 프로필이나 새로 만든 프로필에 추가됩니다.

{% alert note %}
동시에 두 개 이상의 CSV를 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 직렬로 보장되지 않습니다. CSV 가져오기를 차례로 실행해야 하는 경우, CSV 가져오기가 완료될 때까지 기다렸다가 두 번째 가져오기를 업로드하세요.
{% endalert %}

## 데이터 포인트 고려 사항

CSV 파일에서 가져온 각 고객 데이터는 외부 ID와 공백 값을 제외하고 고객 프로필의 기존 값을 덮어쓰고 데이터 포인트를 기록합니다. Braze 데이터 포인트의 미묘한 차이에 대해 궁금한 점이 있으면 Braze 계정 매니저가 답변해 드립니다.

| 고려 사항 | 세부 정보 |
|---|---|
| 외부 ID | `external_id` 으로만 CSV를 업로드하면 데이터 포인트가 기록되지 않습니다. 이를 통해 데이터 제한에 영향을 주지 않고 기존 Braze 사용자를 세분화할 수 있습니다. 그러나 `email` 또는 `phone` 같은 필드를 포함하면 기존 사용자 데이터를 덮어쓰고 데이터 포인트를 **기록하게** 됩니다. <br><br>세분화를 위해서만 사용되는 CSV 가져오기는 `external_id`, `braze_id` 또는 `user_alias_name` 와 같은 데이터 포인트를 기록하지 않습니다. |
| 빈 값 | CSV의 빈 값은 기존 사용자 프로필 데이터를 덮어쓰지 않습니다. 가져올 때 모든 사용자 속성이나 커스텀 이벤트를 포함할 필요는 없습니다. |
| 구독 상태 | `email_subscribe`, `push_subscribe`, `subscription_group_id`, 또는 `subscription_state` 업데이트는 데이터 포인트 사용량에 **포함되지 않습니다**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자에 대해 `language` 또는 `country` 을 설정하면 Braze가 소프트웨어 개발 키트를 통해 이 정보를 자동으로 캡처하지 못합니다.
{% endalert %}

## 문제 해결

CSV 가져오기에 문제가 있는 경우 다음과 같은 일반적인 문제를 검토하세요. 아직도 도움이 필요하신가요? [지원팀에 문의@braze.com](mailto:support@braze.com).

### 파일 서식 문제

#### 잘못된 행

업로드가 오류와 함께 완료된 경우 CSV 파일에 잘못된 행이 있을 수 있습니다. 

데이터를 올바르게 가져오려면 헤더 행이 있어야 합니다. 각 행에는 머리글 행과 동일한 수의 셀이 있어야 합니다. 길이가 헤더 행보다 크거나 작은 값의 행은 가져오기에서 제외됩니다. 값의 쉼표는 구분 기호로 해석되어 이 오류가 발생할 수 있습니다. 또한 모든 데이터는 UTF-8로 인코딩되어야 합니다.

CSV 파일에 빈 행이 있고 가져오는 행 수가 CSV 파일의 총 행 수보다 적은 경우, 빈 행은 가져올 필요가 없으므로 가져오기에 문제가 없는 것으로 간주할 수 있습니다. 올바르게 가져온 회선 수를 확인하고 가져오기하려는 사용자 수와 일치하는지 확인합니다.

#### 누락된 행

가져온 사용자 수가 CSV 파일의 총 행 수와 일치하지 않을 수 있는 몇 가지 이유가 있습니다:

| 이슈 | 해상도 |
|---|---|
| 중복된 외부 ID, 사용자 별칭, Braze ID, 이메일 주소 또는 전화번호 | 외부 ID 열이 중복되면 행의 형식이 올바르게 지정되어 있어도 행이 잘못되거나 가져오지 못할 수 있습니다. 경우에 따라 특정 오류를 보고하지 않을 수도 있습니다. 다시 업로드하기 전에 중복 항목을 확인하고 제거합니다. |
| 악센트 문자 | CSV에는 악센트가 있는 이름이나 속성이 포함될 수 있습니다. 가져오기 문제를 방지하기 위해 파일이 UTF-8로 인코딩되었는지 확인하세요. |
| 고아 사용자에 속하는 Braze ID | 사용자가 다른 사용자와 병합되어 Braze가 남은 프로필에 해당 ID를 연결할 수 없는 경우 해당 행은 가져오기되지 않습니다. |
| 빈 행 | CSV에 빈 행이 있으면 잘못된 데이터 오류가 발생할 수 있습니다. Excel이나 스프레드시트가 아닌 일반 텍스트 편집기를 사용하여 확인합니다. |
| 큰따옴표 포함 (`"` ) | 이 문자는 유효하지 않으며 잘못된 행을 생성합니다. 대신 작은따옴표(`'`)를 사용합니다. |
| 일관성 없는 줄 바꿈 | 줄 바꿈(e.g., `\n` 및 `\r\n`)이 혼합되어 있으면 데이터의 첫 번째 행이 헤더의 일부로 처리될 수 있습니다. 육각 또는 고급 텍스트 편집기를 사용하여 검사하고 수정합니다. |
| 잘못 인코딩된 파일 | 악센트가 허용되더라도 파일은 UTF-8로 인코딩되어야 합니다. 다른 인코딩은 부분적으로 작동할 수 있지만 완전히 지원되지는 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 문자열 따옴표

작은따옴표(`''`) 또는 큰따옴표(`""`)로 묶인 값은 가져오기 시 문자열 값으로 읽힙니다.

#### 잘못된 형식의 날짜

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아닌 날짜는 가져오기 시 `datetimes` 로 읽히지 않습니다.

### 데이터 구조 문제

#### 잘못된 이메일 주소

업로드가 오류와 함께 완료된 경우 하나 이상의 잘못된 암호화된 이메일 주소가 있을 수 있습니다. 이메일 주소를 Braze로 가져오기 전에 모든 이메일 주소가 제대로 암호화되었는지 확인하세요.

- Braze에서 ** [이메일 주소를 업데이트하거나 가져올]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users) 때** 이메일이 포함될 때마다 해시된 이메일 값을 사용하세요. 이러한 해시 이메일 값은 내부 팀에서 제공합니다. 
- **새 사용자를 만들 때** 사용자의 암호화된 이메일 값과 함께 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 생성되지 않습니다. 마찬가지로 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 업데이트되지 않습니다.

#### 커스텀 속성으로 가져온 데이터

기본 사용자 데이터(예: `email` 또는 `first_name`)를 커스텀 속성으로 가져온 경우 CSV 파일의 대소문자와 간격을 확인하세요. 예를 들어 `First_name` 을 커스텀 속성으로 가져오는 반면, `first_name` 은 사용자 프로필의 '이름' 필드에 올바르게 가져올 수 있습니다.

#### 여러 데이터 유형

Braze는 열의 각 값이 동일한 데이터 유형일 것으로 예상합니다. 속성의 데이터 유형과 일치하지 않는 값은 세그먼트화에 오류를 일으킵니다.

또한 숫자 속성을 0으로 시작하면 0으로 시작하는 숫자는 문자열로 간주되므로 문제가 발생할 수 있습니다. Braze가 해당 문자열 값을 변환할 때 0에서 7까지의 숫자를 사용하는 8진수 값처럼 취급될 수 있으며, 이는 해당 10진수 값으로 변환된다는 의미입니다. 예를 들어 CSV 파일의 값이 0130이면 Braze 프로필에 88이 표시됩니다. 이 문제를 방지하려면 문자열 데이터 유형이 있는 속성을 사용하세요. 그러나 이 데이터 유형은 세분화 번호 비교에서는 사용할 수 없습니다.

#### 기본 속성 유형

일부 기본 속성은 사용자 업데이트에 대해 특정 값만 유효한 것으로 허용할 수 있습니다. 지침은 [CSV 구성을]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv) 참조하세요.

후행 공백과 대소문자 차이로 인해 값이 유효하지 않은 것으로 해석될 수 있습니다. 예를 들어, 다음 CSV 파일에서 허용된 값이 `unsubscribed`, `subscribed`, `opted_in` 이므로 첫 번째 행(`brazetest1`)에 있는 사용자만 이메일 및 푸시 상태가 성공적으로 업데이트됩니다. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "CSV 파일 선택"이 작동하지 않습니다.

**CSV 파일 선택** 버튼이 작동하지 않는 데에는 몇 가지 이유가 있습니다:

| 이슈 | 해상도 |
|---|---|
| 팝업 차단기 | 이로 인해 페이지가 표시되지 않을 수 있습니다. 브라우저에서 Braze 대시보드 웹사이트에서 팝업을 허용하는지 확인합니다. |
| 오래된 브라우저 | 브라우저가 최신 버전인지 확인하고, 최신 버전이 아닌 경우 최신 버전으로 업데이트하세요. |
| 백그라운드 프로세스 | 모든 브라우저 인스턴스를 닫은 다음 컴퓨터를 다시 시작합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
