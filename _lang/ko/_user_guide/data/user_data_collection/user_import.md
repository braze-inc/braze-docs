---
nav_title: 사용자 가져오기
article_title: 사용자 가져오기
page_order: 4
page_type: reference
description: "이 참조 문서에서는 REST API, 클라우드 데이터 수집, CSV 및 가져오기 모범 사례를 사용하여 Braze 대시보드에 사용자를 가져오는 방법을 다룹니다."

---
# 사용자 가져오기

> Braze는 사용자 데이터를 플랫폼에 가져오는 다양한 방법을 제공합니다. SDK, API, 클라우드 데이터 수집, 기술 파트너 통합 및 CSV 파일.

계속 진행하기 전에, Braze는 가져오는 동안 HTML 데이터를 정리(유효성 검사 또는 적절한 형식 지정)하지 않는다는 점에 유의하세요. 이는 웹 개인화를 위한 모든 가져오기 데이터에 대해 스크립트 태그를 제거해야 함을 의미합니다.

데이터를 웹 브라우저에서 개인화 용도로 사용하기 위해 Braze에 가져올 때는 웹 브라우저에서 렌더링될 때 악의적으로 활용될 수 있는 HTML, JavaScript 또는 기타 스크립트 태그가 제거되었는지 확인하세요.  

또는 HTML의 경우 Braze Liquid 필터(`strip_html`)를 사용하여 렌더링된 텍스트를 HTML로 이스케이프할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs local %}
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

`/users/track` 엔드포인트][12] ]를 사용하여 사용자 지정 이벤트, 사용자 속성 및 사용자에 대한 구매를 기록합니다.

## 클라우드 데이터 수집

Braze [클라우드 데이터 수집][14] ]을 사용하여 사용자 속성을 가져오고 유지 관리합니다. 

## CSV 가져오기

**오디언스** > **사용자 가져오기**에서 CSV 파일을 통해 고객 프로필을 업로드하고 업데이트할 수 있습니다.

CSV 가져오기는 신발 사이즈와 같은 사용자 지정 속성 외에도 이름, 이메일과 같은 사용자 속성을 기록하고 업데이트하는 기능을 지원합니다. `external_id` 또는 사용자 별칭의 두 가지 고유 사용자 식별자 중 하나를 지정하여 CSV를 가져올 수 있습니다.

{% alert note %}
`external_id` 주소가 있는 사용자와 없는 사용자를 혼합하여 업로드하는 경우 각 가져오기마다 하나의 CSV를 만들어야 합니다. 하나의 CSV에는 `external_ids` 및 사용자 별칭을 모두 포함할 수 없습니다.
{% endalert %}

### CSV 구성하기

Braze에는 여러 데이터 유형이 있습니다. CSV 파일을 사용하여 사용자 프로필을 가져오거나 업데이트할 때 기본값 사용자 속성 또는 커스텀 속성을 생성하거나 업데이트할 수 있습니다.

- 기본값 사용자 속성은 Braze에서 예약된 키입니다. 예를 들어, `first_name` 또는 `email`.
- 커스텀 속성은 사용자 비즈니스에 커스텀입니다. 예를 들어, 여행 예약 앱에는 `last_destination_searched`이라는 커스텀 속성이 있을 수 있습니다.

{% alert important %}
고객 데이터를 가져올 때 사용하는 열 헤더는 기본 사용자 속성의 철자 및 대소문자와 정확히 일치해야 합니다. 그렇지 않으면 Braze는 해당 사용자의 프로필에 커스텀 속성을 자동으로 생성합니다.
{% endalert %}

Braze는 최대 500MB 크기의 파일에서 표준 CSV 형식의 사용자 데이터를 허용합니다. 다운로드 가능한 CSV 템플릿에 대한 가져오기 섹션을 참조하세요.

#### 데이터 포인트 고려사항

CSV 파일에서 가져온 각 고객 데이터는 외부 ID 및 빈 값을 제외하고 고객 프로필의 기존 값을 덮어쓰며 데이터 포인트로 계산됩니다. 

- CSV 파일에서 업로드된 외부 ID는 데이터 포인트를 소모하지 않습니다. 외부 ID만 업로드하여 기존 Braze 사용자를 세그먼트로 나누기 위해 CSV를 업로드하는 경우, 데이터 포인트를 소모하지 않고도 이를 수행할 수 있습니다. 만약 사용자 이메일이나 전화번호와 같은 추가 데이터를 가져오기에 추가한다면, 기존 사용자 데이터를 덮어쓰게 되어 데이터 포인트를 소모하게 됩니다.
  - 세분화 목적의 CSV 가져오기(`external_id`, `braze_id`, 또는 `user_alias_name`을 유일한 필드로 사용하여 가져오기)는 데이터 포인트를 소비하지 않습니다.
- 빈 값은 고객 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 모든 기존 고객 속성을 포함할 필요는 없습니다.
- `email_subscribe`, `push_subscribe`, `subscription_group_id` 또는 `subscription_state`를 업데이트하는 것은 데이터 포인트 소비에 포함되지 않습니다.

{% alert important %}
CSV 가져오기 또는 API를 통해 사용자에게 `language` 또는 `country`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 수집하지 않도록 합니다.
{% endalert %}

#### 기본값 사용자 데이터 열 머리글

| 고객 프로필 필드 | DATA TYPE | 정보 | 필수 |
|---|---|---|---|
| `external_id` | 문자열 | 고객을 위한 고유 사용자 식별자. | 네, 다음 메모를 참조하세요 |
| `user_alias_name` | 문자열 | 익명의 사용자를 위한 고유한 사용자 식별자. `external_id`에 대한 대안. | 아니요, 다음 메모를 참조하세요 |
| `user_alias_label` | 문자열 | 사용자 별칭을 그룹화하는 일반적인 레이블. | 예, `user_alias_name`이 사용되는 경우 |
| `first_name` | 문자열 | 사용자가 지정한 사용자의 이름(예: `Jane`)입니다. | 아니요 |
| `last_name` | 문자열 | 사용자가 지정한 사용자의 성(예: `Doe`)입니다. | 아니요 |
| `email` | 문자열 | 사용자가 표시한 사용자의 이메일(예: `jane.doe@braze.com`)입니다. | 아니요 |
| `country` | 문자열 | 국가 코드는 ISO-3166-1 alpha-2 표준(예: `GB`)으로 Braze에 전달되어야 합니다. | 아니요 |
| `dob` | 문자열 | 반드시 "YYYY-MM-DD" 형식으로 전달되어야 합니다 (예: `1980-12-21`). 이렇게 하면 사용자의 생년월일을 가져와서 생일이 "오늘"인 사용자를 타겟팅할 수 있습니다. | 아니요 |
| `gender` | 문자열 | "M", "F", "O"(기타), "N"(해당 없음), "P"(말하지 않음) 또는 nil(알 수 없음)입니다. | 아니요 |
| `home_city` | 문자열 | 사용자가 지정한 사용자의 고향 도시(예: `London`). | 아니요 |
| `language` | 문자열 | 언어는 ISO-639-1 표준(예: `en`)으로 Braze에 전달되어야 합니다. <br>[허용된 언어 목록][1]을 참조하십시오. | 아니요 |
| `phone` | 문자열 | 사용자가 지정한 전화번호, `E.164` 형식(예: `+442071838750`)입니다. <br> 형식 지침은 [사용자 전화번호][2]를 참조하십시오. | 아니요 |
| `email_open_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다.  이 사용자에게 향후 전송되는 모든 이메일에 열린 추적 픽셀이 추가되지 않도록 하려면 true로 설정합니다.   | 아니요 |
| `email_click_tracking_disabled` | 부울 | 참 또는 거짓이 허용됩니다.  이 사용자가 수신하는 향후 이메일 내 모든 링크에 대한 클릭 추적을 비활성화하려면 true로 설정하십시오. | 아니요 |
| `email_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(이메일 메시지를 수신하도록 명시적으로 등록됨), `unsubscribed`(이메일 메시지를 수신 거부함), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `push_subscribe` | 문자열 | 사용 가능한 값은 `opted_in`(푸시 메시지 수신을 명시적으로 등록), `unsubscribed`(푸시 메시지 수신을 명시적으로 거부), `subscribed`(수신 동의도 거부도 하지 않음)입니다. | 아니요 |
| `time_zone` | 문자열 | 시간대는 IANA 시간대 데이터베이스와 동일한 형식(예: `America/New_York` 또는 `Eastern Time (US & Canada)`)으로 Braze에 전달해야 합니다.  | 아니요 |
| `date_of_first_session` <br><br> `date_of_last_session`| 문자열 | 다음 ISO 8601 형식 중 하나로 전달될 수 있습니다: {::nomarkdown} <ul> <li> YYYY-MM-DD </li> <li> YYYY-MM-DDTHH:MM:SS+00:00 </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (예: 2019-11-20T18:38:57) </li> </ul> {:/} | 아니요 |
| `subscription_group_id` | 문자열 | 구독 그룹의 `id`. 이 식별자는 대시보드의 구독 그룹 페이지에서 찾을 수 있습니다. | 아니요 |
| `subscription_state` | 문자열 | `subscription_group_id`에 의해 지정된 구독 그룹의 구독 상태. 허용되는 값은 `unsubscribed`(구독 그룹에 속하지 않음) 또는 `subscribed`(구독 그룹에 속함)입니다. | 아니요, 그러나 `subscription_group_id`이(가) 사용되는 경우 강력히 권장됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
비록 `external_id` 자체는 필수가 아니지만, **반드시** 이 필드 중 하나를 포함해야 합니다.
- `external_id`: 고객을 위한 고유 사용자 식별자 <br> \- 또는 -
- `braze_id`: 기존 Braze 사용자에 대해 가져온 고유 사용자 식별자 <br> \- 또는 -
- `user_alias_name`: 익명 사용자를 위한 고유한 사용자 식별자
{% endalert %}

### CSV 가져오기

CSV 파일을 가져오려면 **Audiences** > **사용자 가져오기**로 이동하세요. 여기에서 가장 최근의 가져오기를 나열한 테이블을 찾을 수 있으며, 업로드 날짜, 업로더 이름, 파일 이름, 타겟팅 가능 여부, 가져온 행 수 및 각 가져오기 상태와 같은 세부 정보가 포함됩니다.

![Braze 대시보드의 '사용자 가져오기' 페이지입니다.][3]

**파일 찾아보기** 및 파일을 선택하십시오. Braze는 파일을 업로드하고 열 헤더와 각 열의 데이터 유형을 확인합니다.

CSV 템플릿을 다운로드하려면 이 페이지의 [외부 ID로 가져오기](#importing-with-external-id) 또는 [사용자 별칭으로 가져오기](#importing-with-user-alias) 섹션을 참조하세요.

{% alert important %}
CSV 가져오기는 대소문자를 구분합니다. 즉, CSV 가져오기에서 대문자는 표준 속성이 아닌 커스텀 속성으로 필드를 작성합니다. 예를 들어 "이메일"이 맞지만 "이메일"은 커스텀 속성으로 작성됩니다.
{% endalert %}

업로드가 완료되면 파일 내용의 미리보기가 포함된 모달이 표시됩니다. 이 테이블의 모든 정보는 CSV 파일의 상위 몇 개 행의 값을 기반으로 합니다. 열 머리글의 경우 표준 속성은 일반 텍스트로 작성되고 커스텀 속성은 이탤릭체로 작성되며 괄호 안에 유형이 표시됩니다. 팝업 상단에는 파일 요약도 있습니다.

한 번에 여러 개의 CSV를 가져올 수 있습니다. CSV 가져오기는 동시에 실행되므로 업데이트 순서가 순차적일 것이라고 보장할 수 없습니다. CSV 가져오기가 연달아 실행되도록 하려면, 첫 번째 CSV 가져오기가 완료된 후 두 번째 CSV를 업로드하세요.

Braze가 업로드 중 파일에서 잘못된 점을 발견하면 이러한 오류가 요약과 함께 표시됩니다. 예를 들어, 파일에 잘못된 행이 포함된 경우 파일을 가져올 때 미리보기에서 해당 오류가 표시됩니다. 따라서 파일은 오류가 있는 상태로 가져올 수 있지만, 가져오기가 시작된 후에는 취소하거나 롤백할 수 없습니다. 미리보기를 검토하고 오류가 있으면 가져오기를 취소하고 파일을 수정하십시오. 

{% alert important %}
Braze는 미리보기를 위해 입력 파일의 모든 행을 스캔하지 않으니 업로드하기 전에 전체 CSV 파일을 검토하세요. 이는 Braze가 이 미리보기를 생성하는 동안 놓친 오류가 존재할 수 있음을 의미합니다.
{% endalert %}

외부 ID가 없거나 잘못된 행은 가져오지 않습니다. 다른 모든 오류는 가져올 수 있지만 세그먼트를 만들 때 필터링에 방해가 될 수 있습니다. 자세한 내용은 [문제 해결](#troubleshooting) 섹션으로 건너뛰십시오.

![CSV 업로드가 단일 열에서 혼합된 데이터 유형과 관련된 오류와 함께 완료되었습니다][4]{: style="max-width:70%"}

{% alert warning %}
오류는 데이터 유형 및 파일 구조에만 기반합니다. 예를 들어, 형식이 잘못된 이메일 주소는 여전히 문자열로 구문 분석될 수 있으므로 여전히 가져올 수 있습니다.
{% endalert %}

업로드에 만족하면 가져오기를 시작하십시오. 팝업이 닫히고 백그라운드에서 가져오기가 시작됩니다. **사용자 가져오기** 페이지에서 진행 상황을 추적할 수 있으며, 5초마다 새로고침되거나 **최근 가져오기** 상자에서 새로고침 버튼을 누르면 새로고침됩니다.

**처리한 줄** 아래는 가져오기 진행 상황입니다. 완료되면 상태가줄 **완료**로 변경됩니다. 가져오기 중에도 나머지 Braze 대시보드는 계속 사용할 수 있으며, 가져오기가 시작되고 종료되면 알림을 받게 됩니다.

가져오기 프로세스에서 오류가 발생하면 파일의 총 줄 수 옆에 노란색 경고 아이콘이 표시됩니다. 아이콘 위에 마우스를 올리면 특정 줄이 실패한 이유에 대한 세부 정보를 볼 수 있습니다. 가져오기가 완료되면 모든 데이터가 기존 프로필에 추가되거나 새 프로필이 만들어집니다.

### 외부 ID로 가져오기

고객 데이터를 가져올 때는 각 고객의 고유 식별자(`external_id`)를 지정해야 합니다. CSV 가져오기를 시작하기 전에 엔지니어링 팀으로부터 Braze에서 사용자를 식별하는 방법을 이해하는 것이 중요합니다. 일반적으로, 이것은 내부 데이터베이스 ID입니다. 이는 모바일과 웹에서 Braze SDK가 사용자를 식별하는 방식과 일치해야 하며 각 고객이 여러 기기에서 Braze 내에서 단일 고객 프로필을 가질 수 있도록 설계되었습니다. Braze [고객 프로필 수명주기][13]에 대해 자세히 알아보세요.

가져오기에 `external_id`를 제공하면 Braze는 동일한 `external_id`를 가진 기존 사용자를 업데이트하거나 해당 `external_id` 세트가 없는 경우 새로 식별된 사용자를 생성합니다.

**다운로드:** [CSV 가져오기 템플릿][템플릿]

### 사용자 별칭으로 가져오는 중

`external_id`가 없는 사용자를 타겟팅하려면 사용자 별칭이 있는 사용자 목록을 가져올 수 있습니다. 별칭은 대체 고유 사용자 식별자로 사용될 수 있으며, 회원 가입이나 앱 계정을 만들지 않은 익명의 사용자에게 마케팅하려는 경우에 유용할 수 있습니다.

사용자 프로필을 별칭만으로 업로드하거나 업데이트하는 경우 CSV에 다음 두 열이 있어야 합니다:

- `user_alias_name`: 고유 사용자 식별자; `external_id`의 대안
- `user_alias_label`: 사용자 별칭을 그룹화하는 일반적인 레이블

| user_alias_name | user_alias_label | last_name | 이메일 | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | 진실 |
| 182736486 | my_alt_identifier | 응우옌 | nguyen@user.com | 거짓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

가져오기에 `user_alias_name` 및 `user_alias_label` 모두 제공하면 Braze는 기존 사용자를 동일한 `user_alias_name` 및 `user_alias_label`로 업데이트합니다. 사용자를 찾을 수 없는 경우 Braze는 해당 `user_alias_name` 세트로 새로 식별된 사용자를 생성합니다.

{% alert important %}
기존 사용자에게 이미 `external_id`가 있는 경우 CSV 가져오기를 사용하여 `user_alias_name`가 있는 사용자를 업데이트할 수 없습니다. 대신 `user_alias_name`에 연결된 새 고객 프로필이 생성됩니다. 별칭 전용 사용자를 `external_id`와(과) 연결하려면 [사용자 식별 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)를 사용하십시오.
{% endalert %}

**다운로드:** [CSV 별칭 가져오기 템플릿][template_alias]

### Braze ID로 가져오기

`external_id` 또는 `user_alias_name`, `user_alias_label` 값 대신 내부 Braze ID 값을 사용하여 기존 고객 프로필을 업데이트하려면 열 헤더로 `braze_id`를 지정하세요.

이는 세분화 내의 CSV 내보내기 옵션을 통해 Braze에서 사용자 데이터를 내보낸 후 기존 사용자에게 새로운 사용자 지정 속성을 추가하려는 경우에 유용할 수 있습니다.

{% alert important %}
`braze_id`를 사용하여 새 사용자를 만드는 데는 CSV 가져오기를 사용할 수 없습니다. 이 방법은 Braze 플랫폼 내에서 기존 사용자만 업데이트하는 데 사용할 수 있습니다.
{% endalert %}

{% alert tip %}
Braze 대시보드의 CSV 내보내기에서 `braze_id` 값은 `Appboy ID`로 레이블이 지정될 수 있습니다. 이 ID는 사용자의 `braze_id`와 동일하므로 CSV를 다시 가져올 때 이 열의 이름을 `braze_id`로 변경할 수 있습니다.
{% endalert %}

### 이메일 주소와 전화번호로 가져오기

외부 ID 또는 사용자 별칭을 생략하고 이메일 주소 또는 전화번호를 사용하여 사용자를 가져올 수 있습니다. 이메일 주소나 전화번호가 포함된 CSV 파일을 가져오기 전에 다음 사항을 확인하세요:

- CSV 파일에 이러한 프로필에 대한 외부 ID나 사용자 별칭이 없는지 확인합니다. 이 경우 Braze는 이메일 주소보다 외부 ID 또는 사용자 별칭을 우선적으로 사용하여 프로필을 식별합니다.
- CSV 파일이 올바르게 형식화되었는지 확인하십시오.

{% alert note %}
CSV 파일에 이메일 주소와 전화번호를 모두 포함하면, 프로필을 조회할 때 이메일 주소가 전화번호보다 우선시됩니다.
{% endalert %}

기존 프로필에 해당 이메일 주소나 전화번호가 있는 경우, 해당 프로필이 업데이트되며, Braze는 새 프로필을 생성하지 않습니다. 해당 이메일 주소와 동일한 여러 프로필이 있는 경우, Braze는 가장 최근에 업데이트된 프로필이 업데이트되는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)와 동일한 논리를 사용할 것입니다.

해당 이메일 주소나 전화번호로 프로필이 존재하지 않으면, Braze는 해당 식별자로 새 프로필을 생성합니다. 당신은 나중에 이 [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)을 사용하여 이 프로필을 식별할 수 있습니다. 사용자 프로필을 삭제하려면 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) 엔드포인트를 사용할 수도 있습니다.

### 커스텀 데이터 가져오기

기본 사용자 데이터와 정확히 일치하지 않는 헤더는 Braze 내에서 사용자 지정 속성을 생성합니다.

다음 데이터 유형은 사용자 가져오기에 허용됩니다:
- **날짜:** [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식으로 저장해야 합니다.
- **부울:** `true` 또는 `false`
- **번호:** 공백이나 쉼표가 없는 정수 또는 부동 소수점, 부동 소수점은 마침표(`.`)를 소수점 구분 기호로 사용해야 합니다.
- **문자열:** 열 값 주위에 큰따옴표(`""`)가 있는 경우 쉼표를 포함할 수 있습니다.
- **공백:** 빈 값은 사용자 프로필의 기존 값을 덮어쓰지 않으며, CSV 파일에 기존의 모든 사용자 속성을 포함할 필요는 없습니다.

{% alert important %}
배열, 푸시 토큰 및 사용자 지정 이벤트 데이터 유형은 사용자 가져오기에서 지원되지 않습니다.
특히 배열의 경우 CSV 파일의 쉼표는 열 구분 기호로 해석되므로 값에 쉼표가 있으면 파일 구문 분석에 오류가 발생합니다.<br><br>이러한 종류의 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/)을 사용하십시오.
{% endalert %}

### 람다 사용자 CSV 가져오기

서버리스 S3 Lambda CSV 가져오기 스크립트를 사용하여 사용자 속성을 플랫폼에 업로드할 수 있습니다. 이 솔루션은 CSV 업로더로 작동하며, CSV를 S3 버킷에 넣으면 스크립트가 API를 통해 업로드합니다.

1,000,000개의 행이 있는 파일의 예상 실행 시간은 5분 정도입니다. 자세한 내용은 [사용자 속성 CSV를 Braze로 가져오기]({{site.baseurl}}/user_guide/data/cloud_ingestion/)를 참조하십시오.

### 구독 그룹 상태 업데이트 중

사용자 가져오기를 통해 이메일 또는 SMS 구독 그룹에 사용자를 추가할 수 있습니다. 이는 SMS 채널로 메시지를 보내려면 사용자가 SMS 구독 그룹에 등록되어 있어야 하므로 SMS에 특히 유용합니다. 자세한 내용은 [SMS 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)을 참조하십시오.

구독 그룹 상태를 업데이트하는 경우 CSV에 다음 두 개의 열이 있어야 합니다:

- `subscription_group_id`: `id`의 [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: 사용 가능한 값은 `unsubscribed` (구독 그룹에 속하지 않음) 또는 `subscribed` (구독 그룹에 속함)입니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">구독됨</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">구독됨</td>
  </tr>
</tbody>
</table>

{% alert important %}
사용자 가져오기에서 행당 하나의 `subscription_group_id`만 설정할 수 있습니다. 다른 행은 다른 `subscription_group_id` 값을 가질 수 있습니다. 그러나 동일한 사용자를 여러 개의 구독 그룹에 등록해야 하는 경우에는 여러 번 가져오기를 수행해야 합니다.
{% endalert %}

## 사용자 가져오기에서 리타겟팅 필터 만들기

사용자 가져오기를 사용하면 **이 CSV에서 사용자 가져오기를 선택하여 CSV 파일을 리타겟팅 필터로 전환하고 이 특정 사용자 배치를 그룹**으로 리타겟팅할 수 있습니다. 세그먼트의 파일 또는 필터링 옵션이 있는 모든 파일을 기준으로 필터링하려면 **업데이트됨/CSV에서 가져오기** 필터를 선택한 다음 파일의 정확한 이름을 검색합니다.

!["할로윈 시즌 재미"라는 제목의 CSV 파일이 포함된 "업데이트됨/CSV에서 가져온" 필터 그룹이 있습니다.][5]

## 사용자 가져오기에서 세그먼트 만들기

사용자 가져오기를 사용하여 **이 CSV에서 사용자 가져오기를 선택하고 이 특정 사용자 배치를 그룹으로 리타겟팅하고** 가져오기를 시작하기 전에 **이 CSV에서 가져온 사용자로부터 자동으로 세그먼트 생성에** 체크하여 세그먼트를 생성할 수도 있습니다.

세그먼트의 이름을 설정하거나 기본값을 수락할 수 있습니다. 기본값은 파일의 이름입니다. 세그먼트를 만드는 데 사용된 파일에는 가져오기가 완료된 후 세그먼트를 볼 수 있는 링크가 표시됩니다.

세그먼트를 생성하는 데 사용된 필터는 선택한 가져오기에서 생성되거나 업데이트된 사용자를 선택하며 편집 세그먼트 페이지의 다른 모든 필터와 함께 사용할 수 있습니다.

## 고려 사항

{% multi_lang_include email-via-sms-warning.md %}

## 문제 해결

###  오류로 업로드 완료

#### 잘못된 행

데이터를 제대로 가져오려면 헤더 행이 있어야 합니다. 각 행은 헤더 행과 동일한 수의 셀이 있어야 합니다. 길이가 헤더 행보다 크거나 작은 값의 행은 가져오기에서 제외됩니다. 값의 쉼표는 구분 기호로 해석되어 이 오류가 발생할 수 있습니다. 또한, 모든 데이터는 UTF-8로 인코딩되어야 합니다.

CSV 파일에 빈 행이 있고 가져오는 행 수가 CSV 파일의 전체 행 수보다 적은 경우 빈 행은 가져올 필요가 없으므로 가져오기에 문제가 없는 것으로 간주할 수 있습니다. 올바르게 가져온 회선 수를 확인하고 가져오려는 사용자 수와 일치하는지 확인하세요.

#### 잘못된 이메일 주소

Braze에서 잘못된 암호화된 이메일 주소를 감지했습니다. 이메일 주소를 Braze로 가져오기 전에 모든 이메일 주소가 제대로 암호화되었는지 확인하세요.

- Braze에서 ** [이메일 주소를 업데이트하거나 가져올]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users) 때** 이메일이 포함될 때마다 해시된 이메일 값을 사용하세요. 이러한 해시 이메일 값은 내부 팀에서 제공합니다. 
- **새 사용자를 만들 때는** 사용자의 암호화된 이메일 값과 함께 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 생성되지 않습니다. 마찬가지로 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 `email_encrypted` 을 추가해야 합니다. 그렇지 않으면 사용자가 업데이트되지 않습니다.

### 누락된 행

CSV 파일에 있는 총 행 수와 가져온 사용자 수가 일치하지 않을 수 있는 몇 가지 이유가 있습니다:

- **중복된 외부 아이디, 사용자 별칭, Braze 아이디, 이메일 주소 또는 전화번호:** 외부 ID 열이 중복된 경우 행의 형식이 올바르게 지정되어 있어도 잘못된 형식이거나 가져오지 않은 행이 발생할 수 있습니다. 경우에 따라 특정 오류를 보고하지 않을 수도 있습니다. CSV에 중복된 외부 ID가 있는지 확인하십시오. 그렇다면 중복을 제거하고 다시 업로드해 보세요.
- **강세 문자:** 귀하의 CSV에는 악센트가 포함된 이름이나 속성이 있을 수 있습니다. 문제를 방지하려면 파일을 항상 UTF-8로 인코딩하세요.
- **Braze ID는 고아 사용자의 소유입니다:** 사용자가 고아가 된 경우, 고아가 병합된 나머지 사용자는 고아가 된 사용자의 Braze ID를 프로필에 연결할 수 없습니다. 이 경우 Braze는 업데이트할 사용자를 찾지 못하므로 해당 행은 가져온 것으로 간주되지 않습니다.
- **빈 행입니다:** CSV 파일에 빈 행이 있습니다. 텍스트 편집기 프로그램에서 CSV를 열면 확인할 수 있습니다(Excel이나 스프레드시트 사용 금지). 빈 행이 있는 CSV를 업로드하면 잘못된 데이터가 있는 행이 있다는 오류 메시지가 표시됩니다.
- **큰따옴표 포함 (`"`):** 이 문자는 유효하지 않으며 행이 잘못 표시됩니다. 대신 작은따옴표(`'`)를 사용합니다.
- **줄 바꿈이 일관되지 않습니다:** 예를 들어 CSV 파일에서 첫 번째 줄에 `\n`, 이후 각 줄에 `\r\n` 을 사용하는 경우 데이터의 첫 번째 행은 헤더의 일부로 처리되며 해당 데이터는 예상대로 가져오지 않습니다. 공백 문자를 구분하는 특수 텍스트 편집기나 헥스 에디터에서 확인할 수 있습니다.
- **잘못 인코딩된 파일입니다:** CSV 파일에는 악센트가 있는 이름이나 속성이 포함될 수 있지만, 이를 제대로 가져오려면 파일을 UTF-8로 인코딩해야 합니다. 다른 문자로 된 인코딩도 경우에 따라 작동할 수는 있지만, UTF-8만 완벽하게 호환됩니다.

### 잘못된 형식의 날짜

[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 형식이 아닌 날짜는 가져오기 시 `datetimes` 로 읽히지 않습니다.

### 문자열 따옴표

작은따옴표(`''`) 또는 큰따옴표(`""`)로 묶은 값은 가져오기 시 문자열로 읽힙니다.

### 커스텀 속성으로 가져온 데이터

기본 사용자 데이터(예: `email` 또는 `first_name`)를 사용자 지정 속성으로 가져온 경우 CSV 파일의 대소문자와 띄어쓰기를 확인하세요. 예를 들어 `First_name`은 커스텀 속성으로 가져오지만 `first_name`은 고객 프로필의 '이름' 필드에 올바르게 가져옵니다.

### 여러 데이터 유형

Braze는 열의 각 값이 동일한 데이터 유형이어야 합니다. 속성의 데이터 유형과 일치하지 않는 값은 세그먼테이션에 오류를 일으킵니다.

또한 숫자 속성을 0으로 시작하면 0으로 시작하는 숫자는 문자열로 간주되므로 문제가 발생할 수 있습니다. Braze가 해당 문자열을 변환할 때 0에서 7까지의 숫자를 사용하는 8진수 값처럼 취급될 수 있으며, 이는 해당 10진수 값으로 변환된다는 의미입니다. 예를 들어 CSV 파일의 값이 0130이면 Braze 프로필에 88이 표시됩니다. 이 문제를 방지하려면 문자열 데이터 유형이 있는 속성을 사용하세요. 그러나 이 데이터 유형은 세분화 번호 비교에서는 사용할 수 없습니다.

### 기본 속성 유형

일부 기본 속성은 특정 값만 사용자 업데이트에 유효한 것으로 허용할 수 있습니다. 지침은 [CSV 구성을]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv) 참조하세요.

후행 공백과 대소문자 차이로 인해 값이 유효하지 않은 것으로 해석될 수 있습니다. 예를 들어, 다음 CSV 파일에서 허용된 값이 `unsubscribed`, `subscribed`, `opted_in` 이므로 첫 번째 행(`brazetest1`)에 있는 사용자만 이메일 및 푸시 상태가 성공적으로 업데이트됩니다. 

```
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### 'CSV 파일 선택' 버튼이 작동하지 않습니다.

**CSV 파일 선택** 버튼이 작동하지 않는 데에는 몇 가지 이유가 있습니다:

- **팝업 차단기:** 이로 인해 페이지가 표시되지 않을 수 있습니다. 브라우저에서 Braze 대시보드 웹사이트에서 팝업을 허용하는지 확인합니다. 
- **오래된 브라우저:** 브라우저가 최신 버전인지 확인하고, 최신 버전이 아닌 경우 최신 버전으로 업데이트하세요.
- **백그라운드 프로세스:** 모든 브라우저 인스턴스를 닫은 다음 컴퓨터를 다시 시작합니다.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/csvfilter.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
