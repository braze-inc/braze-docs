---
nav_title: Custom attributes
article_title: 커스텀 속성
page_order: 10
page_type: reference
description: "이 페이지에서는 커스텀 속성에 대해 설명하고 다양한 커스텀 속성 데이터 유형에 대해 설명합니다."
search_rank: 1
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 속성

> 이 페이지에서는 사용자 고유 특성의 모음인 커스텀 속성에 대해 설명합니다. 커스텀 속성은 사용자에 대한 속성이나 애플리케이션 내에서 가치가 낮은 동작에 대한 정보를 저장하는 데 가장 적합합니다. 

Braze에 저장된 커스텀 속성을 사용하여 오디언스 세그먼트를 구축하고 Liquid를 사용하여 메시지를 개인화할 수 있습니다. 커스텀 속성에 대해서는 시계열 정보를 저장하지 않으므로 커스텀 이벤트에서와 같이 해당 속성을 기반으로 한 그래프를 얻을 수 없다는 점에 유의하세요.

## 커스텀 속성 관리

대시보드에서 커스텀 속성을 만들고 관리하려면 **데이터 설정** > **커스텀 속성**으로 이동합니다. 

![네 개의 부울 커스텀 속성.]({% image_buster /assets/img/export_custom_attributes.png %})

**마지막 업데이트** 열에는 커스텀 속성을 마지막으로 편집한 시간(예: 차단 목록 또는 활성으로 마지막으로 설정한 시간)이 나열됩니다.

{% alert important %}
적절한 메시지 타겟팅을 위해서는 커스텀 속성 데이터 유형이 실제 커스텀 속성과 일치하는지 확인하세요. <br><br>예를 들어, `newsletter_subscribed`가 문자열로 정의되면 Liquid 구문은 {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}```{% endraw %}와 같아야 합니다. `newsletter_subscribed`가 부울로 정의되면 Liquid 구문에는 작은따옴표가 없어야 합니다: {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == true %}```{% endraw %}.
{% endalert %}

이 페이지에서 기존 커스텀 속성을 확인, 관리, 생성 또는 차단 목록에 추가할 수 있습니다. 다음 동작을 수행하려면 커스텀 속성 옆의 메뉴를 선택합니다:

### 차단 목록에 추가

커스텀 속성은 동작 메뉴에서 개별적으로 차단 목록에 추가하거나, 최대 100개의 속성을 선택하여 일괄적으로 차단 목록에 추가할 수 있습니다. 커스텀 속성을 차단하면 해당 속성과 관련된 데이터가 수집되지 않으며, 다시 활성화하지 않는 한 기존 데이터를 사용할 수 없고, 차단된 속성은 필터나 그래프에 표시되지 않습니다. 또한 해당 속성이 현재 Braze 대시보드의 다른 영역에 있는 필터나 트리거에서 참조되고 있는 경우, 해당 속성을 참조하는 필터나 트리거의 모든 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

### 개인 식별 정보(PII)로 표시하기

관리자는 이 페이지에서 커스텀 속성을 생성하고 이를 PII로 표시할 수도 있습니다. 이러한 속성은 'PII로 표시된 커스텀 속성 보기' 권한이 있는 관리자와 대시보드 사용자만 볼 수 있습니다.

### 설명 추가하기

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성을 만든 후 설명을 추가할 수 있습니다. 커스텀 속성을 편집하고 팀에 대한 메모 등 원하는 내용을 입력하세요.

### 태그 추가하기

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성이 생성된 후 태그를 추가할 수 있습니다. 그런 다음 태그를 사용하여 속성 목록을 필터링할 수 있습니다. 

### 커스텀 속성 제거하기

고객 프로필에서 커스텀 속성을 제거하는 방법에는 두 가지가 있습니다:

* [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes)에서 제거할 커스텀 속성 이름을 선택합니다.
* API 요청에서 `null` 값을 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track)로 설정합니다.

### 데이터 내보내기

커스텀 속성 목록을 CSV 파일로 내보내려면 페이지 상단에서 **모두 내보내기**를 선택합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

## 사용량 보고서 보기

사용량 보고서에는 특정 커스텀 속성을 사용하는 모든 캔버스, 캠페인 및 세그먼트가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다. 

해당 커스텀 속성 옆의 체크박스를 선택한 다음 **사용량 보고서 보기**를 선택하면 한 번에 최대 100개의 사용량 보고서를 볼 수 있습니다.

### 값 탭

사용량 보고서를 볼 때, 선택한 커스텀 속성의 상위 값을 보려면 **값** 탭을 선택하세요. 이 값은 약 250,000명의 사용자 샘플을 기반으로 합니다. 결과가 사용자 하위 집합에서 샘플링되기 때문에 샘플에는 모든 기존 값이 포함되지 않을 수 있습니다. 따라서 **값** 탭은 문제 해결이나 모든 사용자의 데이터를 통합해야 하는 활용 사례에는 사용하지 않는 것이 좋습니다.

![선택한 커스텀 속성에 대한 사용량 보고서로, "값" 탭이 열려 있으며, "US" 및 "PR"과 같은 국가 속성 값의 원형 차트를 보여줍니다.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## 커스텀 속성 설정

다음은 커스텀 속성을 설정하는 데 사용되는 다양한 플랫폼의 메서드 목록입니다.

{% details 플랫폼별 설명서 펼치기 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (구 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## 커스텀 속성 저장소

커스텀 속성 데이터를 포함하여 **고객 프로필**에 저장된 모든 데이터는 각 프로필이 [활성]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) 상태인 한 무기한 보관됩니다.

## 커스텀 속성 데이터 유형

커스텀 속성은 뛰어난 타겟팅을 가능하게 하는 매우 유연한 도구입니다.

커스텀 속성으로 저장할 수 있는 데이터 유형은 다음과 같습니다:

- [부울](#booleans)
- [숫자](#numbers)
- [문자열](#strings)
- [배열](#arrays)
- [시간](#time)
- [오브젝트]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [오브젝트 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### 부울(참/거짓) {#booleans}

부울 속성은 구독 상태와 같은 사용자에 대한 간단한 이진 데이터를 저장하는 데 유용합니다. 변수가 명시적으로 참 또는 거짓 값으로 설정된 사용자와 해당 속성에 대한 기록이 아직 없는 사용자를 찾을 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 부울 값이 참, 거짓, 참이거나 설정되지 않음, 또는 거짓이거나 설정되지 않음 중 하나**인지** 확인합니다 | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, 또는 **FALSE OR NOT SET** | 이 필터가 `coffee_drinker`를 지정하는 경우 사용자는 다음과 같은 상황에서 이 필터와 일치합니다: <br> {::nomarkdown}<ul><li>이 필터가 <code>true</code>이고 사용자가 <code>coffee_drinker</code> 값을 가지고 있는 경우</li><li>이 필터가 <code>false</code>이고 사용자가 <code>coffee_drinker</code> 값을 가지고 있지 않은 경우</li><li>이 필터가 <code>true or not set</code>이고 사용자가 <code>coffee_drinker</code> 값을 가지고 있거나 값이 없는 경우</li><li>이 필터가 <code>false or not set</code>이고 사용자가 <code>coffee_drinker</code> 또는 아무 값도 가지고 있지 않은 경우</li></ul>{:/} |
| 고객 프로필에 부울 값이 **존재하고** null이 아닌지 확인합니다 | **IS NOT BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성에 대한 값이 있는 경우 해당 사용자는 이 필터와 일치합니다. | 
| 부울 값이 고객 프로필에 **존재하지 않거나** null인지 확인합니다 | **IS BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성이 없거나 `coffee_drinker` 값이 null인 경우, 해당 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 숫자 {#numbers}

숫자 속성에는 [정수](https://en.wikipedia.org/wiki/Integer)와 [플로트](https://en.wikipedia.org/wiki/Floating-point_arithmetic)가 포함되며 다양한 활용 사례가 있습니다. 증분 숫자 커스텀 속성은 데이터 한도에 포함되지 않으면서 특정 동작이나 이벤트가 발생한 횟수를 저장하는 데 유용합니다. 표준 숫자는 다음과 같은 다양한 용도로 사용됩니다:

- 신발 사이즈
- 허리 사이즈
- 사용자가 특정 제품 기능 또는 카테고리를 조회한 횟수

{% alert tip %}
이 방법으로 지출 금액을 기록해서는 안 됩니다. 대신 [구매 방법](#purchase-revenue-tracking)을 통해 기록해야 합니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 숫자 속성이 **정확히** **숫자**인지 확인합니다| **EXACTLY** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 있는 경우 해당 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자와** **같지 않은지** 확인합니다| **DOES NOT EQUAL** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 없는 경우 해당 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자보다** **큰지** 확인합니다| **MORE THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필의 값이 `10`보다 큰 경우 해당 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자보다** **작은지** 확인합니다| **LESS THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필의 값이 `10`보다 작은 경우 해당 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 고객 프로필에 **존재하고** null이 아닌지 확인합니다 | **IS NOT BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있으면 값에 관계없이 사용자가 이 필터와 일치합니다. |
| 숫자 속성이 고객 프로필에 **존재하지 않거나** null인지 확인합니다 | **IS BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있지 않거나 속성 값이 null인 경우 해당 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 숫자 속성 세부 정보

- "정확히 0" 및 "미만" 필터에는 NULL 필드가 있는 사용자가 포함됩니다
  - 커스텀 속성에 대한 값이 없는 사용자를 제외하려면 **is not blank** 필터를 포함해야 합니다.

### 문자열(영숫자) {#strings}

문자열 속성은 즐겨 찾는 브랜드, 전화번호 또는 애플리케이션 내에서 마지막으로 검색한 문자열과 같은 사용자 입력을 저장하는 데 유용합니다. 문자열 속성은 최대 255자까지 입력할 수 있습니다.

단어 사이, 앞, 뒤에 공백이 있는 값을 입력하면 Braze에서도 동일한 공백이 있는지 확인합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하는지** 확인합니다 | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** <br>대소문자 구분 없음, 최대 32,764자 | 
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하지 않는지** 확인합니다 | **DOES NOT MATCH REGEX** * | **STRING** **OR** **REGULAR EXPRESSION**<br>대소문자 구분 없음, 최대 32,764자 |
| 문자열 속성이 고객 프로필에 **존재하고** 빈 문자열이 아닌지 확인합니다 | **IS NOT BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 있는 경우 사용자는 속성 값에 관계없이 이 필터와 일치합니다. 예를 들어 사용자는 `sci-fi`, `romance` 또는 다른 값을 가질 수 있습니다.|
| 문자열 속성이 고객 프로필에 **존재하지 않는지** 확인합니다 | **BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 없는 경우 해당 사용자는 이 필터와 일치합니다.|
| 문자열이 입력된 문자열 중 **하나와** 정확히 일치하는지 확인합니다 | **IS ANY OF** | **STRING**<br>대소문자 구분, 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 이러한 문자열 중 하나 이상이 있는 경우 사용자는 이 필터와 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 정확히 일치하지 않는지** 확인합니다 | **IS NONE OF** |**STRING**<br>대소문자 구분, 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 이러한 문자열이 포함되어 있지 않은 경우 사용자는 필터와 일치합니다.|
| 문자열 속성이 입력된 문자열 중 **하나와 부분적으로 일치하는지** 확인합니다 | **CONTAINS ANY OF** | **STRING**<br>대소문자 구분, 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 `gold_tier` 또는 `former_gold_tier`와 같은 문자열에 `gold`가 포함된 경우 해당 사용자는 필터와 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 부분적으로 일치하지 않는지** 확인합니다 | **DOESN'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분, 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 어떤 문자열에도 `gold`가 포함되지 않은 경우, 해당 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
**DOES NOT MATCH REGEX** 필터를 사용하여 세분화할 때는 해당 고객 프로필에 값이 할당된 커스텀 속성이 이미 있어야 합니다. Braze는 커스텀 속성이 비어 있는지 확인하여 사용자가 제대로 타겟팅되고 있는지 확인하기 위해 "OR" 논리를 사용할 것을 권장합니다.
{% endalert %}

### 배열 {#arrays}

배열 속성은 사용자에 대한 관련 정보 목록을 저장하는 데 유용합니다. 예를 들어, 사용자가 마지막으로 시청한 100개의 콘텐츠를 배열에 저장하면 특정 관심사를 기준으로 세분화할 수 있습니다.

배열의 최대 크기는 100&nbsp;KB입니다. 속성의 기본 길이는 최대 500개 항목입니다. 예를 들어, "시청한 영화"와 같은 속성을 전송하고 500으로 설정된 경우, 사용자가 501번째 영화를 시청하면 첫 번째 영화가 배열에서 제거되고 가장 최근 영화가 추가됩니다. 

단어 사이, 앞, 뒤에 공백이 있는 값을 입력하면 Braze에서도 동일한 공백이 있는지 확인합니다.

{% alert note %}
속성이 데이터 유형을 자동으로 감지하도록 설정된 경우 최대 길이를 늘리는 옵션은 사용할 수 없으며, 데이터 유형을 배열로 설정해야 합니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 배열 속성에 입력한 값과 **정확히 일치하는 값이 포함되어** 있는지 확인합니다| **INCLUDES VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 있는 경우 해당 사용자는 이 필터와 일치합니다.|
| 배열 속성에 입력한 값과 **정확히 일치하는 값이 포함되어 있지 않은지** 확인합니다| **DOESN'T INCLUDE VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 없는 경우 해당 사용자는 이 필터와 일치합니다.|
| 배열 속성에 입력된 값 **또는** 정규표현식과 **부분적으로 일치하는 값이 포함되어** 있는지 확인합니다 | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION**<br>최대 32,764자 | |
| 배열 속성에 **값이 있거나** 비어 있지 않은지 확인합니다 | **HAS A VALUE** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 `favorite_genres`가 어떤 값이든 포함된 경우 해당 사용자는 이 필터와 일치합니다. |
| 배열 속성이 **비어 있거나** 존재하지 않는지 확인합니다 | **IS EMPTY** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 `favorite_genres`가 포함되어 있지 않거나 `favorite_genres`가 포함되어 있지만 값이 없는 경우, 해당 사용자는 이 필터와 일치합니다.|
| 배열 속성에 입력한 값 중 **하나와 정확히 일치하는 값이 포함되어** 있는지 확인합니다 | **INCLUDES ANY OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy`, 또는 `romance` 중 하나만 포함된 경우(예: `sci-fi`만 포함)에도 일치합니다. 사용자는 `sci-fi`, `fantasy`, `romance` 중 하나라도 있는 경우 문자열에 `horror` 또는 다른 값을 가질 수 있습니다.|
| 배열 속성에 입력한 값 중 **어느 것과도 정확히 일치하는 값이 포함되어 있지 않은지** 확인합니다 | **INCLUDES NONE OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy` 또는 `romance`의 조합이 없는 경우 해당 사용자는 이 필터와 일치합니다. 사용자는 `sci-fi`, `fantasy`, `romance` 중 하나라도 없는 경우 `horror` 또는 다른 값을 가질 수 있습니다.|
| 배열 속성에 입력된 값 중 **하나와 부분적으로 일치하는 값이 포함되어** 있는지 확인합니다 | **VALUES CONTAIN ANY OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 하나 이상의 문자열에 `gold`가 포함된 경우 사용자는 이 필터와 일치합니다. 여기에는 `gold_tier`, `former_gold_tier` 등과 같은 문자열 값이 포함됩니다.|
| 배열 속성에 입력한 값 중 **어느 것과도 부분적으로 일치하는 값이 포함되어 있지 않은지** 확인합니다 | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 어떤 문자열에도 `gold`가 포함되지 않은 경우 해당 사용자는 이 필터와 일치합니다. 즉, `gold_tier` 및 `former_gold_tier` 같은 문자열 값을 가진 사용자는 이 필터와 일치하지 않습니다.|
| 배열 속성에 입력된 **모든 값이 포함되어** 있는지 확인합니다 | **IS ALL OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 해당 값이 모두 있는 경우 해당 사용자는 이 필터와 일치합니다. 사용자는 `horror` 또는 다른 값을 가지고 있어도 이 필터와 일치할 수 있습니다.|
| 배열 속성에 입력된 값이 **모두 포함되지 않았는지** 확인합니다 | **ISN'T ALL OF** | **STRING**<br>대소문자 구분, 여러 값 허용(최대 256개)|  이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 이러한 값이 모두 없는 경우 해당 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
정규식(regex) 사용 방법에 대한 자세한 내용은 다음 리소스를 참조하세요:
- [Perl 호환 정규식(PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze를 사용한 정규식]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [정규식 디버거 및 테스터](https://www.regex101.com/)
- [정규식 튜토리얼](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### 시간 {#time}

시간 속성은 특정 동작이 마지막으로 수행된 시간을 저장하는 데 유용하므로 사용자에게 콘텐츠별 재참여 메시지를 제공할 수 있습니다.

상대 날짜(예: 1일 이상 전, 2일 미만 전)를 사용하는 시간 필터는 하루를 24시간으로 계산합니다. 이 필터를 사용하여 실행하는 모든 캠페인에는 24시간 단위로 모든 사용자가 포함됩니다. 예를 들어 `last used app more than 1 day ago`는 캠페인이 실행되는 정확한 시간부터 "24시간 이상 전에 앱을 마지막으로 사용한" 모든 사용자를 캡처합니다. 더 긴 날짜 범위로 설정된 캠페인도 마찬가지입니다. 활성화 후 5일은 이전 120시간을 의미합니다.

예를 들어, 향후 24시간에서 48시간 사이의 시간 속성을 가진 사용자를 타겟팅하는 세그먼트를 구축하려면 `in more than 1 day in the future` 및 `in less than 2 days in the future` 필터를 적용합니다.

{% alert warning %}
커스텀 이벤트 또는 구매 이벤트가 발생한 마지막 날짜는 자동으로 기록되며 커스텀 시간 속성을 통해 다시 기록해서는 안 됩니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 시간 속성이 **선택한 날짜** **이전인지** 확인합니다| **BEFORE** | **CALENDAR DATE SELECTOR** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필의 날짜가 `2024-1-31` 이전인 경우 해당 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **선택한 날짜** **이후인지** 확인합니다| **AFTER** | **CALENDAR DATE SELECTOR** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필의 날짜가 `2024-1-31` 이후인 경우 해당 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **X일** **이상** 전인지 확인합니다 | **MORE THAN** | **NUMBER OF DAYS AGO** | 이 필터가 `7`을 지정하고 고객 프로필에 7일 이상 전의 날짜가 있는 경우 해당 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **X일** **미만** 전인지 확인합니다| **LESS THAN** | **NUMBER OF DAYS AGO** | 이 필터가 `7`을 지정하고 고객 프로필의 날짜가 7일 미만 전인 경우 해당 사용자는 이 필터와 일치합니다.|
| 시간 속성이 **향후 X일** **이상** 남았는지 확인합니다 | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | 이 필터가 `7`을 지정하고 고객 프로필의 날짜가 7일 이상 미래인 경우 해당 사용자는 이 필터와 일치합니다.|
| 시간 속성이 **향후 X일** **미만**인지 확인합니다 | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | 이 필터가 `7`을 지정하고 고객 프로필의 날짜가 미래 7일 미만인 경우 해당 사용자는 이 필터와 일치합니다.|
| 시간 속성이 고객 프로필에 **존재하고** null이 아닌지 확인합니다 | **IS NOT BLANK** | **N/A** | 이 필터가 고객 프로필에 있는 시간 속성을 지정하면 사용자는 이 필터와 일치합니다.|
| 시간 속성이 고객 프로필에 **존재하지 않거나** null인지 확인합니다 | **IS BLANK** | **N/A** | 이 필터가 고객 프로필에 없는 시간 속성을 지정하면 사용자는 이 필터와 일치합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 시간 속성 세부 정보

- 반복 이벤트의 날짜
  - "반복 이벤트의 날짜" 필터를 사용하는 경우 "반복 이벤트의 캘린더 날짜"를 선택하라는 메시지가 표시되면 `IS LESS THAN` 또는 `IS MORE THAN`을 선택하면 해당 세분화 필터에 현재 날짜가 포함됩니다.
  - 예를 들어 2020년 3월 10일에 속성의 날짜를 `LESS THAN ... March 10, 2020`으로 선택한 경우 속성은 2020년 3월 10일까지의 날짜(포함)로 간주됩니다. 
- X일 전 미만: "X일 전 미만" 필터에는 X일 전과 현재 날짜/시간 사이의 날짜가 포함됩니다.
- 향후 X일 미만: 현재 날짜/시간과 미래 X일 사이의 날짜를 포함합니다.

### 오브젝트

중첩 커스텀 속성을 사용하여 오브젝트를 커스텀 속성의 데이터 유형으로 보낼 수 있습니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)을 참조하세요.

### 오브젝트 배열

오브젝트 배열을 사용하여 관련 속성을 그룹화합니다. 자세한 내용은 [오브젝트 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) 문서를 참조하세요.

### 통합 연산자

속성 필터, 커스텀 속성 필터, 중첩 커스텀 속성 필터에 사용할 수 있는 연산자 목록이 통합되었습니다. 이러한 연산자를 사용하는 기존 필터가 있는 경우 새 연산자를 사용하도록 자동으로 업데이트됩니다.

| 데이터 유형 | 이전 연산자 | 새 연산자 | 값 |
| --- | --- | --- | --- |
| 문자열 | equals | is any of | 1개 이상의 값 |
| 문자열 | does not equal | is none of | 1개 이상의 값 |
| 배열 | includes value | includes any of | 1개 이상의 값 |
| 배열 | doesn't include value | includes none of | 1개 이상의 값 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 구매 및 매출 추적 {#purchase-revenue-tracking}

구매 방법을 사용하여 인앱 구매를 기록하면 각 개별 고객 프로필에 대한 생애주기 가치(LTV)가 설정됩니다. 이 데이터는 매출 페이지에서 시계열로 볼 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 총 지출 금액이 **숫자보다** **큰지** 확인합니다| **GREATER THAN** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필의 값이 `500`보다 큰 경우 해당 사용자는 이 필터와 일치합니다. |
| 총 지출 금액이 **숫자보다** **작은지** 확인합니다| **LESS THAN** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필의 값이 `500`보다 작은 경우 해당 사용자는 이 필터와 일치합니다.|
| 총 지출 금액이 **정확히** **숫자**인지 확인합니다| **EXACTLY** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필에 `500` 값이 있는 경우 해당 사용자는 이 필터와 일치합니다. |
| **X 날짜 이후에** 마지막으로 구매가 발생했는지 확인합니다 | **AFTER** | **TIME** | 이 필터가 `2024/31/1`을 지정하고 사용자의 마지막 구매가 `2024/31/1` 이후인 경우 해당 사용자는 이 필터와 일치합니다.|
| **X 날짜 이전에** 마지막으로 구매가 발생했는지 확인합니다 | **BEFORE** | **TIME** | 이 필터가 `2024/31/1`을 지정하고 사용자의 마지막 구매가 `2024/31/1` 이전인 경우 해당 사용자는 이 필터와 일치합니다.|
| 마지막 구매가 **X일 이상** 전에 발생했는지 확인합니다 | **MORE THAN** | **TIME** | 이 필터가 `7`로 지정되어 있고 사용자의 마지막 구매가 오늘로부터 7일 이상 전인 경우, 해당 사용자는 이 필터와 일치합니다.|
| 마지막 구매가 **X일 미만** 전에 발생했는지 확인합니다 | **LESS THAN** | **TIME** |  이 필터가 `7`로 지정되어 있고 사용자의 마지막 구매가 오늘로부터 7일 미만 전인 경우, 해당 사용자는 이 필터와 일치합니다.|
| 구매가 **X(최대 = 50)회 이상** 발생했는지 확인합니다 | **MORE THAN** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |  이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 7회 이상 구매를 한 경우 이 필터와 일치합니다.|
| 구매가 **X(최대 = 50)회 미만으로** 발생했는지 확인합니다 | **LESS THAN** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** | 이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 구매한 횟수가 7회 미만인 경우 해당 사용자는 이 필터와 일치합니다.|
| 구매가 **정확히 X(최대 = 50)회** 발생했는지 확인합니다 | **EXACTLY** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** | 이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 7번의 구매를 한 경우 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
특정 구매가 발생한 횟수를 기준으로 세분화하려면 해당 구매를 [증분 커스텀 속성]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes)으로 개별적으로 기록해야 합니다.
{% endalert %}

커스텀 속성의 데이터 유형을 변경할 수 있지만 [데이터 유형을 변경하면]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) 어떤 영향이 있는지 알고 있어야 합니다.