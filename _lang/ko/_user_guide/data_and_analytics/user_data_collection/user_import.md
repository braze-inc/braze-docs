---
nav_title: 사용자 가져오기
article_title: 사용자 가져오기
page_order: 4
page_type: reference
description: "이 참조 문서에서는 REST API, 클라우드 데이터 수집, CSV 및 가져오기 모범 사례를 사용하여 Braze 대시보드에 사용자를 가져오는 방법을 다룹니다."

---
# 사용자 가져오기

> Braze는 사용자 데이터를 플랫폼에 가져오는 다양한 방법을 제공합니다: SDK, API, 클라우드 데이터 수집, 기술 파트너 통합 및 CSV.

{% multi_lang_include email-via-sms-warning.md %}

진행하기 전에 Braze가 가져오기 중에 HTML 데이터를 소독(검증 또는 적절한 형식화)하지 않는다는 점을 유의하십시오. 이는 웹 개인화를 위한 모든 가져오기 데이터에 대해 스크립트 태그를 제거해야 함을 의미합니다.

데이터를 웹 브라우저에서 개인화 용도로 사용하기 위해 Braze에 가져올 때는 웹 브라우저에서 렌더링될 때 악의적으로 활용될 수 있는 HTML, JavaScript 또는 기타 스크립트 태그가 제거되었는지 확인하십시오.  

또는 HTML의 경우 Braze Liquid 필터(`strip_html`)를 사용하여 렌더링된 텍스트를 HTML로 이스케이프할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs 지역 %}
{% tab 입력 %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## REST API

사용자는 \[`/users/track` 엔드포인트][12]를 사용하여 커스텀 이벤트, 사용자 속성 및 구매를 기록할 수 있습니다.

## 클라우드 데이터 수집

Braze \[Cloud Data Ingestion][14]을 사용하여 사용자 속성을 가져오고 유지할 수 있습니다. 

## CSV 가져오기

CSV 파일을 통해 **오디언스** > **사용자 가져오기**에서 사용자 프로필을 업로드하고 업데이트할 수 있습니다.

이 기능은 사용자 속성(예: 이름 및 이메일)을 기록하고 업데이트하는 것을 지원하며, 신발 크기와 같은 커스텀 속성도 지원합니다. CSV를 가져오려면 두 개의 고유 사용자 식별자 중 하나를 지정할 수 있습니다: `external_id` 또는 사용자 별칭.

{% alert note %}
사용자와 `external_id` 없는 사용자를 혼합하여 업로드하는 경우 각 가져오기에 대해 하나의 CSV를 만들어야 합니다. 하나의 CSV에는 `external_ids` 및 사용자 별칭을 모두 포함할 수 없습니다.
{% endalert %}

### 외부 ID로 가져오기

고객 데이터를 가져올 때 각 고객의 고유 식별자, 즉 `external_id`을(를) 지정해야 합니다. CSV 가져오기를 시작하기 전에 엔지니어링 팀에게 사용자가 Braze에서 어떻게 식별될지 이해하는 것이 중요합니다. 일반적으로, 이것은 내부 데이터베이스 ID입니다. 이것은 모바일 및 웹에서 Braze 소프트웨어 개발 키트에 의해 사용자가 식별되는 방식과 일치해야 하며, 각 고객이 자신의 기기에서 Braze 내에서 단일 고객 프로필을 갖도록 설계되었습니다. Braze \[고객 프로필 수명주기][13]에 대해 자세히 알아보기.

귀하의 가져오기에 `external_id`을(를) 제공하면 Braze는 동일한 `external_id`을(를) 가진 기존 사용자를 업데이트하거나 해당 `external_id` 세트가 없는 경우 새로 식별된 사용자를 생성합니다.

**다운로드:** \[CSV 가져오기 템플릿]\[템플릿]

### 사용자 별칭으로 가져오는 중

`}사용자가 없는 사용자를 대상으로 하려면 사용자 별칭이 있는 사용자 목록을 가져올 수 있습니다.`external_id` 별칭은 대체 고유 사용자 식별자로 사용될 수 있으며, 회원 가입이나 앱 계정을 만들지 않은 익명의 사용자에게 마케팅하려는 경우에 유용할 수 있습니다.

사용자 프로필을 별칭만으로 업로드하거나 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `user_alias_name`: 고유 사용자 식별자; `external_id`의 대안
- `user_alias_label`: 사용자 별칭을 그룹화하는 일반적인 레이블

| 사용자_별명_이름 | 사용자_별명_레이블 | 성 | 이메일 | 샘플_속성 |
| --- | --- | --- | --- | --- |
| 182736485 | 내_대체_식별자 | Smith | smith@user.com | 진실 |
| 182736486 | 내_대체_식별자 | 응우옌 | nguyen@user.com | 거짓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

둘 다 `user_alias_name` 및 `user_alias_label`를 제공하면 Braze는 동일한 `user_alias_name` 및 `user_alias_label`를 가진 기존 사용자를 업데이트합니다. 사용자를 찾을 수 없는 경우 Braze는 해당 `user_alias_name` 세트로 새로 식별된 사용자를 생성합니다.

{% alert important %}
CSV 가져오기를 사용하여 `user_alias_name`이(가) 있는 기존 사용자를 업데이트할 수 없습니다. 이미 `external_id`이(가) 있는 경우. 대신, 이것은 관련된 `user_alias_name`와 함께 새로운 고객 프로필을 생성할 것입니다. 별칭 전용 사용자를 `external_id`와(과) 연결하려면 [사용자 식별 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)를 사용하십시오.
{% endalert %}

**다운로드:** \[CSV 별칭 가져오기 템플릿]\[template_alias]

### Braze ID로 가져오기

내부 Braze ID 값을 사용하여 Braze에서 기존 사용자 프로필을 업데이트하려면 `external_id` 또는 `user_alias_name` / `user_alias_label` 값을 대신하여 `braze_id`를 열 머리글로 지정하십시오.

세분화 내에서 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보낸 후 기존 사용자에게 새 커스텀 속성을 추가하려는 경우 유용할 수 있습니다.

{% alert important %}
CSV 가져오기를 사용하여 `braze_id`을(를) 사용하여 새 사용자를 만들 수 없습니다. 이 방법은 Braze 플랫폼 내에서 기존 사용자만 업데이트하는 데 사용할 수 있습니다.
{% endalert %}

{% alert tip %}
Braze 대시보드에서 CSV 내보내기 시 `braze_id` 값이 `Appboy ID`(으)로 표시될 수 있습니다. 이 ID는 사용자의 `braze_id`와 동일하므로 CSV를 다시 가져올 때 이 열의 이름을 `braze_id`(으)로 바꿀 수 있습니다.
{% endalert %}

### CSV를 구성하는 중

Braze에는 여러 데이터 유형이 있습니다. CSV 파일을 사용하여 사용자 프로필을 가져오거나 업데이트할 때 기본값 사용자 속성 또는 커스텀 속성을 생성하거나 업데이트할 수 있습니다.

- 기본값 user attributes are 예약 keys in Braze. 예를 들어, `first_name` 또는 `email`.
- 커스텀 속성은 귀하의 비즈니스에 커스텀입니다. 예를 들어, 여행 예약 앱에는 `last_destination_searched`이라는 커스텀 속성이 있을 수 있습니다.

{% alert important %}
고객 데이터를 가져올 때 사용하는 열 머리글은 기본 사용자 속성의 철자 및 대소문자와 정확히 일치해야 합니다. 그렇지 않으면 Braze는 해당 사용자의 프로필에 커스텀 속성을 자동으로 생성합니다.
{% endalert %}

Braze는 최대 500MB 크기의 파일에서 표준 CSV 형식의 사용자 데이터를 수락합니다. 다운로드 가능한 CSV 템플릿에 대한 가져오기 섹션을 참조하십시오.

#### 데이터 포인트 고려사항

CSV 파일에서 가져온 각 고객 데이터는 외부 ID 및 빈 값을 제외하고 사용자 프로필의 기존 값을 덮어쓰며 데이터 포인트로 계산됩니다. 

- CSV 파일에서 업로드된 외부 ID는 데이터 포인트를 소모하지 않습니다. 외부 ID만 업로드하여 기존 Braze 사용자를 세그먼트로 나누기 위해 CSV를 업로드하는 경우, 데이터 포인트를 소모하지 않고도 이를 수행할 수 있습니다. 만약 사용자 이메일이나 전화번호와 같은 추가 데이터를 가져오기에 추가한다면, 기존 사용자 데이터를 덮어쓰게 되어 데이터 포인트를 소모하게 됩니다.
  - 세분화 목적을 위한 CSV 가져오기(`external_id`, `braze_id`, 또는 `user_alias_name`만 필드로 사용하여 가져온 경우)는 데이터 포인트를 소모하지 않습니다.
- 빈 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 고객 속성을 포함할 필요는 없습니다.
- `email_subscribe`, `push_subscribe`, `subscription_group_id`, `subscription_state`을(를) 업데이트해도 데이터 포인트 소비에 포함되지 않습니다.

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자에게 `language` 또는 `country`을(를) 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 수집하지 않도록 합니다.
{% endalert %}

#### 기본값 사용자 데이터 열 머리글

| 고객 프로필 필드 | 데이터 TYPE | 정보 | 필수 |
|---|---|---|---|
| `external_id` | 문자열 | 고객을 위한 고유 사용자 식별자. | 네, 다음 메모를 참조하세요 |
| `user_alias_name` | 문자열 | 익명의 사용자를 위한 고유한 사용자 식별자. `external_id`에 대한 대안. | 아니요, 다음 메모를 참조하세요 |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 일반적인 레이블. | 예, `user_alias_name`이 사용되는 경우 |
| `first_name` | 문자열 | 사용자가 표시한 이름(예: `Jane`) | 아니요 |
| `last_name` | 문자열 | 사용자가 표시한 성(예: `Doe`). | 아니요 |
| `email` | 문자열 | 사용자가 표시한 이메일(예: `jane.doe@braze.com`)입니다. | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 alpha-2 표준(예: `GB`)으로 Braze에 전달되어야 합니다. | 아니요 |
| `dob` | 문자열 | 반드시 "YYYY-MM-DD" 형식으로 전달되어야 합니다 (예: `1980-12-21`). 이것은 사용자의 생년월일을 가져오고 생일이 '오늘'인 사용자를 타겟팅할 수 있게 해줍니다. | 아니요 |
| `gender` | 문자열 | "M", "F", "O" (기타), "N" (해당 없음), "P" (말하지 않음 선호), 또는 nil (알 수 없음). | 아니요 |
| `home_city` | 문자열 | 사용자가 표시한 대로 사용자의 고향 도시(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준(예: `en`)으로 Braze에 전달되어야 합니다. <br>허용된 언어 목록을 참조하십시오. | 아니요 |
| `phone` | 문자열 | 사용자가 지정한 전화번호는 `E.164` 형식입니다 (예: `+442071838750`). <br> 형식 지침은 [사용자 전화번호][2]를 참조하십시오. | 아니요 |
| `email_open_tracking_disabled` | 부울 | 참 또는 거짓 수락됨.  이 사용자가 받는 모든 향후 이메일에 오픈 추적 픽셀이 추가되지 않도록 설정합니다.   | 아니요 |
| `email_click_tracking_disabled` | 부울 | 참 또는 거짓 수락됨.  이 사용자가 수신하는 향후 이메일 내 모든 링크에 대한 클릭 추적을 비활성화하려면 true로 설정하십시오. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값은 `opted_in` (이메일 메시지를 받도록 명시적으로 등록됨), `unsubscribed` (이메일 메시지를 받지 않도록 명시적으로 선택됨), 및 `subscribed` (선택되지 않음)입니다. | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값은 `opted_in` (푸시 메시지를 수신하도록 명시적으로 등록됨), `unsubscribed` (푸시 메시지를 수신하지 않도록 명시적으로 선택됨), 및 `subscribed` (선택되지 않음)입니다. | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스(예: `America/New_York` 또는 `Eastern Time (US & Canada)`)와 동일한 형식으로 Braze에 전달되어야 합니다.  | 아니요 |
| `date_of_first_session` <br><br> `date_of_last_session`| 문자열 | 다음 ISO 8601 형식 중 하나로 전달될 수 있습니다: {::nomarkdown} <ul> <li> YYYY-MM-DD </li> <li> YYYY-MM-DDTHH:MM:SS+00:00 </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) </li> </ul> {:/} | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`. 이 식별자는 대시보드의 구독 그룹 페이지에서 찾을 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id`에 의해 지정된 구독 그룹의 구독 상태. 허용된 값은 `unsubscribed` (구독 그룹에 포함되지 않음) 또는 `subscribed` (구독 그룹에 포함됨)입니다. | 아니요, 그러나 `subscription_group_id`이(가) 사용되는 경우 강력히 권장됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
비록 `external_id` 자체는 필수가 아니지만, **반드시** 이 필드 중 하나를 포함해야 합니다:
- `external_id`: 고객을 위한 고유 사용자 식별자 <br> \- 또는 -
- `braze_id`: 기존 Braze 사용자에 대해 가져온 고유 사용자 식별자 <br> \- 또는 -
- `user_alias_name`: 익명 사용자를 위한 고유한 사용자 식별자
{% endalert %}

### 커스텀 데이터 가져오기

기본값 사용자 데이터와 정확히 일치하지 않는 모든 헤더는 Braze 내에서 커스텀 속성을 생성합니다.

다음 데이터 유형은 사용자 가져오기에 허용됩니다:
- 날짜 및 시간 (반드시 [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장되어야 함)
- 부울 (참/거짓)
- 숫자 (정수 또는 공백이나 쉼표가 없는 플로트, 소수점 구분자로 마침표(.)를 사용해야 함)
- 문자열 (Can contain commas as long as there are double quotation marks surrounding the column value)
- 공백 (공백 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 고객 속성을 포함할 필요는 없습니다.)

{% alert important %}
배열, 푸시 토큰 및 커스텀 이벤트 데이터 유형은 사용자 가져오기를 지원하지 않습니다.
특히 배열의 경우 CSV 파일의 쉼표는 열 구분 기호로 해석되므로 값에 쉼표가 있으면 파일을 구문 분석하는 동안 오류가 발생합니다.

이러한 종류의 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/)을 사용하십시오.
{% endalert %}

### 구독 그룹 상태 업데이트 중

사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 이것은 SMS에 특히 유용합니다. 사용자가 SMS 채널로 메시지를 받으려면 SMS 구독 그룹에 등록되어야 하기 때문입니다. 자세한 내용은 [SMS 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)을 참조하십시오.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `subscription_group_id`: `id`의 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: 사용 가능한 값은 `unsubscribed` (구독 그룹에 포함되지 않음) 또는 `subscribed` (구독 그룹에 포함됨)입니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">외부 ID</th>
    <th class="tg-0pky">이름</th>
    <th class="tg-0pky">구독_그룹_ID</th>
    <th class="tg-0pky">구독 상태</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">콜비</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">구독됨</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">톰</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">구독됨</td>
  </tr>
</tbody>
</table>

{% alert important %}
사용자 가져오기에서 행당 하나의 `subscription_group_id`만 설정할 수 있습니다. 다른 행은 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 구독 그룹에 등록해야 하는 경우 여러 번 가져와야 합니다.
{% endalert %}

### CSV 가져오기

CSV 파일을 가져오려면 **사용자 가져오기** 페이지로 이동하여 **Audiences** 섹션 아래로 이동하십시오. 여기에서 가장 최근의 가져오기를 나열한 표를 찾을 수 있으며, 업로드 날짜, 업로더의 이름, 파일 이름, 타겟팅 가능 여부, 가져온 행 수 및 각 가져오기 상태와 같은 세부 정보가 포함됩니다.

![][3]

**파일 찾아보기** 및 파일을 선택하십시오. Braze는 파일을 업로드하고 열 헤더와 각 열의 데이터 유형을 확인합니다.

CSV 템플릿을 다운로드하려면 이 페이지의 [외부 ID로 가져오기](#importing-with-external-id) 또는 [사용자 별칭으로 가져오기](#importing-with-user-alias) 섹션을 참조하세요.

{% alert important %}
CSV 가져오기는 대소문자를 구분합니다. 이는 CSV 가져오기에서 대문자가 표준 속성 대신 커스텀 속성으로 필드를 작성함을 의미합니다. 예를 들어, "이메일"은 맞지만, "이메일"은 커스텀 속성으로 작성됩니다.
{% endalert %}

업로드가 완료되면 파일 내용의 미리보기가 포함된 모달이 표시됩니다. 이 표의 모든 정보는 CSV 파일의 상위 몇 개 행의 값을 기반으로 합니다. 열 머리글의 경우 표준 속성은 일반 텍스트로 작성되고 커스텀 속성은 이탤릭체로 작성되며 괄호 안에 유형이 표시됩니다. 팝업 상단에는 파일 요약도 있습니다.

한 번에 여러 개의 CSV를 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 순차적일 것이라고 보장할 수 없습니다. CSV 가져오기가 연달아 실행되도록 하려면, 첫 번째 CSV 가져오기가 완료된 후 두 번째 CSV를 업로드하십시오.

Braze가 업로드 중 파일에서 잘못된 점을 발견하면 이러한 오류가 요약과 함께 표시됩니다. 예를 들어, 파일에 잘못된 행이 포함된 경우 파일을 가져올 때 미리보기에서 해당 오류가 표시됩니다. 따라서 파일은 오류가 있는 상태로 가져올 수 있지만, 가져오기가 시작된 후에는 취소하거나 롤백할 수 없습니다. 미리보기를 검토하고 오류가 있으면 가져오기를 취소하고 파일을 수정하십시오. 

{% alert important %}
업로드 전에 전체 CSV 파일을 검사하십시오. Braze는 미리보기를 위해 입력 파일의 모든 행을 스캔하지 않습니다. 이는 Braze가 이 미리보기를 생성하는 동안 잡지 못하는 오류가 존재할 수 있음을 의미합니다.
{% endalert %}

외부 ID가 없거나 잘못된 행은 가져오지 않습니다. 다른 모든 오류는 가져올 수 있지만 세그먼트를 만들 때 필터링에 방해가 될 수 있습니다. 자세한 내용은 [문제 해결](#troubleshooting) 섹션으로 건너뛰십시오.

![CSV 업로드가 단일 열에서 혼합된 데이터 유형과 관련된 오류로 완료되었습니다][4]{: style="max-width:70%"}

{% alert warning %}
오류는 데이터 유형 및 파일 구조에만 기반합니다. 예를 들어, 형식이 잘못된 이메일 주소는 여전히 문자열로 구문 분석될 수 있으므로 여전히 가져올 수 있습니다.
{% endalert %}

업로드에 만족하면 가져오기를 시작하십시오. 팝업이 닫히고 백그라운드에서 가져오기가 시작됩니다. **사용자 가져오기** 페이지에서 진행 상황을 추적할 수 있으며, 5초마다 새로고침되거나 **최근 가져오기** 상자에서 새로고침 버튼을 누르면 새로고침됩니다.

줄 처리 아래는 가져오기 진행 상황입니다. 완료되면 상태가 완료로 변경됩니다. 가져오는 동안 Braze 대시보드의 REST를 계속 사용할 수 있으며, 가져오기가 시작되고 끝날 때 알림을 받게 됩니다.

가져오기 프로세스에서 오류가 발생하면 파일의 총 줄 수 옆에 노란색 경고 아이콘이 표시됩니다. 아이콘 위에 마우스를 올리면 특정 줄이 실패한 이유에 대한 세부 정보를 볼 수 있습니다. 가져오기가 완료되면 모든 데이터가 기존 프로필에 추가되거나 새 프로필이 생성됩니다.

### 람다 사용자 CSV 가져오기

서버리스 S3 Lambda CSV 가져오기 스크립트를 사용하여 사용자 속성을 플랫폼에 업로드할 수 있습니다. 이 솔루션은 CSV 업로더로 작동하여 CSV를 S3 버킷에 드롭하면 스크립트가 API를 통해 업로드합니다.

백만 개의 행이 있는 파일의 예상 실행 시간은 약 5분입니다. 자세한 내용은 [사용자 속성 CSV를 Braze로 가져오기]({{site.baseurl}}/user_csv_lambda/)를 참조하십시오.

## 세그먼트화

사용자 가져오기는 사용자 프로필을 생성 및 업데이트하며, 세그먼트를 생성하는 데에도 사용할 수 있습니다. 세그먼트를 만들려면 가져오기를 시작하기 전에 **이 CSV에서 가져온 사용자로부터 세그먼트를 자동으로 생성**을 선택하십시오.

세그먼트의 이름을 설정하거나 기본값을 수락할 수 있습니다. 기본값은 파일의 이름입니다. 세그먼트를 생성하는 데 사용된 파일은 가져오기가 완료된 후 세그먼트를 볼 수 있는 링크가 있습니다.

세그먼트를 생성하는 데 사용된 필터는 선택한 가져오기에서 생성되거나 업데이트된 사용자를 선택하며 편집 세그먼트 페이지의 다른 모든 필터와 함께 사용할 수 있습니다.

## 문제 해결 {#troubleshooting}

### 누락된 행

CSV 파일에 있는 총 행 수와 가져온 사용자 수가 일치하지 않을 수 있는 몇 가지 이유가 있습니다:

- **중복된 외부 ID:** 외부 ID 열이 중복되면 행이 올바르게 형식화되었더라도 잘못된 형식이거나 가져오지 않은 행이 발생할 수 있습니다. 일부 경우에는 특정 오류를 보고하지 않을 수 있습니다. CSV에 중복된 외부 ID가 있는지 확인하십시오. 그렇다면 중복을 제거하고 다시 업로드해 보세요.
- **강세 문자:** 귀하의 CSV에는 악센트가 포함된 이름이나 속성이 있을 수 있습니다. 문제를 방지하려면 파일을 항상 UTF-8로 인코딩하세요.

### 잘못된 행

데이터를 올바르게 가져오려면 헤더 행이 있어야 합니다. 각 행은 헤더 행과 동일한 수의 셀이 있어야 합니다. 헤더 행보다 길거나 짧은 값을 가진 행은 가져오기에 제외됩니다. 값의 쉼표는 구분 기호로 해석되어 이 오류가 발생할 수 있습니다. 또한, 모든 데이터는 UTF-8로 인코딩되어야 합니다.

CSV 파일에 빈 행이 있고 CSV 파일의 총 줄 수보다 적은 행이 가져와진 경우, 빈 행은 가져올 필요가 없기 때문에 가져오기 문제를 나타내지 않을 수 있습니다. 가져온 줄 수가 올바른지 확인하고 가져오려는 사용자 수와 일치하는지 확인하십시오.

### 여러 데이터 유형

Braze는 열의 각 값이 동일한 데이터 유형이어야 합니다. 속성의 데이터 유형과 일치하지 않는 값은 세분화하는 데 오류를 일으킬 것입니다.

### 잘못된 형식의 날짜

날짜가 [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아니면 가져올 때 날짜 및 시간으로 읽히지 않습니다.

### 문자열 인용

단일 ('') 또는 이중 ('') 인용 부호로 묶인 값은 가져올 때 문자열로 읽힙니다.

### 데이터 가져오기 커스텀 속성으로

기본 사용자 데이터(예: `email` 또는 `first_name`)가 커스텀 속성으로 가져온 경우, CSV 파일의 대소문자 및 공백을 확인하십시오. 예를 들어, `First_name`은(는) 커스텀 속성으로 가져오고, `first_name`는(는) 사용자의 프로필의 "이름" 필드에 올바르게 가져옵니다.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
\[errors]:#common-errors
\[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
\[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
