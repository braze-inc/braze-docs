---
nav_title: 필터
article_title: 액체 필터
page_order: 3
description: "이 참조 페이지에는 정적 또는 동적 콘텐츠의 서식을 다시 지정하는 데 사용할 수 있는 필터가 나열되어 있습니다."

---

# 필터

> 이 참고 문서에서는 Liquid의 필터에 대한 개요와 Braze에서 지원하는 필터에 대해 설명합니다. 이러한 필터를 사용하는 방법에 대한 아이디어를 찾고 계신가요? [Liquid 사용 사례 라이브러리]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/)를 확인하세요.

필터는 Liquid에서 숫자, 문자열, 변수, 오브젝트의 출력을 수정할 수 있는 방법입니다. 필터를 사용하여 문자열을 소문자에서 대문자로 변경하거나 덧셈이나 나눗셈과 같은 수학 연산을 수행하는 등 정적 또는 동적 텍스트의 서식을 변경할 수 있습니다.

{% alert important %}
Braze는 Shopify의 모든 리퀴드 필터를 지원하지 않습니다. 이 페이지에서는 Braze가 테스트한 Liquid 필터를 간략하게 소개하지만, 전체 목록이 아닐 수도 있습니다. 메시지를 보내기 전에 항상 Liquid를 테스트하세요. <br><br>여기에 나열되지 않은 필터에 대해 궁금한 점이 있으면 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 필터 구문

{% raw %}

필터는 출력 태그 `{{ }}` 내에 배치해야 하며 파이프 문자 `|`로 표시해야 합니다.

{% endraw %}

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

이 예에서 `Big Sale` 은 문자열이고 `upcase` 은 적용 중인 필터입니다.

### 다중 필터 구문

하나의 출력에 여러 필터를 사용할 수 있습니다. 왼쪽에서 오른쪽으로 적용됩니다.

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 배열 필터

배열 필터는 배열의 출력을 변경하는 데 사용됩니다.

| 필터               | 정의                                                                                                         | 지원 |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1]          | 매개변수로 전달된 문자를 사용하여 배열의 요소를 조인합니다. 결과는 단일 문자열입니다.          | ✅ 예   |
| [첫 번째][1.2]         | 배열의 첫 번째 요소를 반환합니다. 사용자 지정 속성 배열에서 이것은 가장 오래된 추가 값입니다.                | ✅ 예   |
| [마지막][1.3]          | 배열의 마지막 요소를 반환합니다. 사용자 지정 속성 배열에서 가장 최근에 추가된 값입니다.          | ✅ 예   |
| [컴팩트][1.4]       | 배열에서 `nil` 항목을 제거합니다.                                                                             | ✅ 예   |
| [concat][1.5]        | 배열을 다른 배열과 결합합니다.                                                                              | ✅ 예   |
| [색인][1.6]         | 배열에서 지정된 인덱스 위치에 있는 항목을 반환합니다. 배열의 첫 번째 항목은 `[0]` 로 참조됩니다. | ✅ 예   |
| [지도][1.7]           | 배열 요소의 속성을 매개변수로 받아들이고 각 배열 요소의 값으로 배열을 생성합니다.        | ✅ 예   |
| [역방향][1.8]       | 배열에 있는 항목의 순서를 반대로 바꿉니다.                                                                       | ✅ 예   |
| [크기][1.9]          | 문자열(문자 수) 또는 배열(요소 수)의 크기를 반환합니다.                      | ✅ 예   |
| [정렬][1.10]         | 배열에 있는 요소의 지정된 속성을 기준으로 배열의 요소를 정렬합니다.                                    | ✅ 예   |
| [정렬_자연][1.11] | 배열의 항목을 대소문자를 구분하지 않는 알파벳 순서로 정렬합니다.                                                | ✅ 예   |
| [고유][1.12]         | 배열에 있는 요소의 중복 인스턴스를 제거합니다.                                                           | ✅ 예   |
| [어디][1.13]        | 특정 속성 값을 가진 항목만 포함하도록 배열을 필터링합니다.                                             | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 컬러 필터

Braze에서는 [컬러 필터가][2.1] 지원되지 않습니다.

## 글꼴 필터

Braze에서는 [글꼴 필터가][3.1] 지원되지 않습니다.

## 수학 필터

수학 필터를 사용하면 수학적 연산을 수행할 수 있습니다. 하나의 출력에 여러 필터를 사용하는 경우 왼쪽에서 오른쪽으로 필터가 적용됩니다.

| 필터  | 정의      | 지원 |
| :------ |:----------------| :-------- |
| [절대값][4.1]        | 숫자의 절대값을 반환합니다.     | ✅ 예   |
| [at_most][4.2]    | 숫자를 최대값으로 제한합니다.   | ✅ 예   |
| [at_least][4.3]   | 숫자를 최소값으로 제한합니다.   | ✅ 예   |
| [ceil][4.4]       | 출력을 가장 가까운 정수로 반올림합니다.  | ✅ 예   |
| [divided_by][4.5] | 출력을 숫자로 나눕니다. 출력은 가장 가까운 정수로 반내림됩니다. 반올림을 방지하려면 다음 팁을 확인하세요. | ✅ 예   |
| [floor][4.6]      | 출력을 가장 가까운 정수로 반내림합니다.        | ✅ 예   |
| [마이너스][4.7]      | 출력에서 숫자를 뺍니다.          | ✅ 예   |
| [플러스][4.8]       | 출력에 숫자를 추가합니다.     | ✅ 예   |
| [반올림][4.9]      | 출력을 가장 가까운 정수 또는 지정된 소수점 이하로 반올림합니다.  | ✅ 예   |
| [곱하기][4.10]     | 출력에 숫자를 곱합니다.       | ✅ 예   |
| [모듈][4.11]    | 출력을 숫자로 나누고 나머지를 반환합니다.   | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Liquid에서 정수(정수)를 정수로 나눌 때 답이 부동 소수점(소수점이 있는 숫자)인 경우, Liquid는 자동으로 가장 가까운 정수로 반내림합니다. 그러나 정수를 부동 소수점으로 나누면 항상 부동 소수점이 나옵니다. 즉, 정수를 플로트(1.0, 2.0, 3.0)로 변환하여 플로트를 반환할 수 있습니다.
{% raw %}
<br><br>예를 들어`{{15 | divided_by: 2}}`은 `7`을 출력하고 `{{15 | divided_by: 2.0}}`은 `7.5`을 출력합니다.
{% endraw %}
{% endalert %}

### 사용자 지정 속성을 사용한 수학 연산

두 사용자 지정 속성 간에 수학 연산을 수행할 수 없다는 점에 유의하세요.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

이 예제는 Liquid의 한 줄에서 여러 커스텀 속성을 참조할 수 없기 때문에 작동하지 않습니다. 대신 수학 함수가 수행되기 전에 이러한 값 중 하나 이상에 변수를 할당해야 합니다. 두 개의 커스텀 속성을 함께 추가하려면 두 줄의 Liquid가 필요합니다:

1. 하나는 변수에 커스텀 속성을 할당하는 것입니다,
2. 하나는 추가를 수행합니다.

#### 사용 사례: 현재 잔액 계산

기프트 카드 잔액과 리워드 잔액을 더하여 사용자의 현재 잔액을 계산하고 싶다고 가정해 보겠습니다.

1. `assign` 태그를 사용하여 `current_rewards_balance` 의 사용자 지정 속성을 "balance"라는 용어로 대체합니다. 즉, 이제 조작할 수 있는 `balance`라는 변수가 생겼습니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. `plus` 필터를 사용하여 각 사용자의 기프트 카드 잔액을 `{{balance}}` 개체로 표시되는 보상 잔액과 결합합니다.
{% endraw %}
{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 머니 필터

사용자의 구매, 계정 잔액 또는 돈과 관련된 내용을 업데이트하는 경우에는 머니 필터를 사용해야 합니다. 머니 필터는 소수점이 올바른 위치에 있고 업데이트의 일부가 손실되지 않도록 합니다(예: 마지막에 있는 성가신 `0`).

| 필터         | 정의          | 지원 |
| :--------------- | :--------------- | :-------- |
| [머니][5.1]      | 소수점이 올바른 위치에 있고 숫자 끝에서 0이 빠지지 않도록 숫자 서식을 지정합니다.   | ✅ 예   |
| [money_with_currency][5.2]    | 통화 기호로 숫자 서식을 지정합니다.     | ⛔ 아니요    |
| [money_without_currency][5.4]     | 통화 기호 없이 숫자의 서식을 지정합니다.      | ⛔ 아니요    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
`money` 필터로 숫자 서식을 올바르게 지정하려면 숫자에서 쉼표를 제거하고 `money` 필터 앞에 `plus: 0` 필터를 추가합니다. 예를 들어 다음 Liquid를 참조하세요:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Shopify 머니 필터와 Braze 머니 필터 비교

{% alert warning %}
Shopify `money` 필터의 동작은 Braze에서 사용되는 방식과 다릅니다. 예상되는 동작에 대한 정확한 묘사는 다음 예시를 참조하세요.
{% endalert %}

{% raw %}
사용자 정의 속성(예: `account_balance`)을 입력하는 경우 항상 `money` 필터를 사용하여 소수점을 적절한 위치에 배치하고 숫자 끝에서 0이 빠지는 것을 방지해야 합니다:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| 머니 필터 사용                       | 머니 필터 미사용                    |
| :------------------------------------------ | :------------------------------------------ |
| ![돈 필터 사용][1]                     | ![돈 필터 없음][2]                  |
| 여기서 `account_balance`는 `17.8`에 입력합니다. | 여기서 `account_balance`는 `17.8`에 입력합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze의 `money` 필터는 사전 설정 설정에 따라 소수점이 자동으로 적용되지 않기 때문에 Shopify와 다릅니다. 예를 들어 `rewards_redeemed`에 `145` 값이 포함된 다음 시나리오를 예로 들어 보겠습니다:

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Shopify의 [머니][5.1] 필터에 따르면 `$1.45` 으로 출력되어야 하지만 Braze에서는 `$145.00` 으로 출력됩니다. 해결 방법으로 `divided_by` 필터를 사용하여 숫자를 10진수로 조작한 후 돈 필터를 적용할 수 있습니다:

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 문자열 필터

문자열 필터는 문자열의 출력과 변수를 조작하는 데 사용됩니다. 문자열은 영숫자와 숫자의 조합이며 반드시 큰따옴표로 묶어야 합니다.

{% alert note %}
Liquid에서 직선 따옴표는 곡선 따옴표와 다릅니다. 텍스트 편집기에서 Liquid를 복사하여 Braze에 붙여넣을 때 따옴표로 묶으면 Liquid에 오류가 발생할 수 있으므로 주의하세요. 리퀴드를 Braze에 직접 작성하는 경우, 따옴표가 자동으로 적용됩니다.
{% endalert %}

| 필터          | 설명     | 지원 |
| :--------------- | ------------- | --------- |
| [추가][6.1]     | 문자열에 문자를 추가합니다.           | ✅ 예   |
| [카멜케이스][6.2]     | 문자열을 카멜케이스로 변환합니다.             | ⛔ 아니요    |
| [대문자][6.3]     | 문자열의 첫 단어는 대문자로 표시하고 나머지 문자는 소문자로 표시합니다.         | ✅ 예   |
| [소문자][6.4]      | 문자열을 소문자로 변환합니다.         | ✅ 예   |
| [이스케이프][6.5]    | 문자열을 이스케이프합니다.             | ✅ 예   |
| [핸들/핸들화][6.6]        | 문자열의 형식을 핸들로 지정합니다.        | ⛔ 아니요    |
| [md5][6.7]    | 문자열을 MD5 해시로 변환합니다. 자세한 내용은 [인코딩 필터][3] ]를 참조하세요.   | ✅ 예   |
| [sha1][6.8]    | 문자열을 SHA-1 해시로 변환합니다. 자세한 내용은 [인코딩 필터][3] ]를 참조하세요.  | ✅ 예   |
| HMAC_SHA1_HEX<br>(이전 [hmac_sha_1][6.10]) | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-1 해시로 변환합니다. 메시지의 비밀 키를 필터에 매개변수로 전달합니다. 자세한 내용은 [인코딩 필터][3] ]를 참조하세요. | ✅ 예   |
| [hmac_sha256][6.11]    | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-256 해시로 변환합니다. 메시지의 비밀 키를 필터에 매개변수로 전달합니다.       | ✅ 예   |
| hmac_sha512 | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-512 해시로 변환합니다. 메시지의 비밀 키를 필터에 매개변수로 전달합니다. | ✅ 예  |
| [newline_to_br][6.12]     | 문자열의 각 줄 바꿈 앞에 `<br>` 줄 바꿈 HTML 태그를 삽입합니다.        | ✅ 예   |
| [복수화][6.13]   | 숫자 값에 따라 단수 또는 복수 버전의 영어 문자열을 출력합니다.      | ⛔ 아니요    |
| [prepend][6.14]     | 문자열에 문자를 추가합니다.      | ✅ 예   |
| [제거][6.15]      | 문자열에서 부분 문자열의 모든 항목을 제거합니다.       | ✅ 예   |
| [remove_first][6.16]    | 문자열에서 부분 문자열의 첫 번째 항목만 제거합니다.      | ✅ 예   |
| [대체][6.17]        | 문자열의 모든 항목을 부분 문자열로 바꿉니다.   | ✅ 예   |
| [replace_first][6.18]        | 문자열의 첫 번째 문자열을 부분 문자열로 바꿉니다.      | ✅ 예   |
| [슬라이스][6.19]       | 슬라이스 필터는 지정된 인덱스에서 시작하여 하위 문자열을 반환합니다.       | ✅ 예   |
| [분할][6.20]  | 분할 필터는 하위 문자열을 매개변수로 사용합니다. 하위 문자열은 문자열을 배열로 나누는 구분 기호로 사용됩니다.            | ✅ 예   |
| [스트립][6.21]   | 문자열의 왼쪽과 오른쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.                                                                                                    | ✅ 예   |
| [lstrip][6.22]     | 문자열의 왼쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.    | ⛔ 아니요    |
| [rstrip][6.23]             | 문자열의 오른쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.          | ⛔ 아니요    |
| [strip_html][6.24]         | 문자열에서 모든 HTML 태그를 제거합니다.        | ✅ 예   |
| [스트립_뉴라인][6.25]  | 문자열에서 줄 바꿈/새 줄을 제거합니다.        | ✅ 예   |
| [잘라내기][6.26]    | 첫 번째 매개 변수로 전달된 문자 수만큼 문자열을 잘라냅니다. 잘린 문자열에는 줄임표(...)가 추가되며 문자 수에 포함됩니다.    | ✅ 예   |
| [잘라낸 단어][6.27]   | 첫 번째 매개변수로 전달된 단어 수만큼 문자열을 잘라냅니다. 잘린 문자열에는 줄임표(...)가 추가됩니다.    | ✅ 예   |
| [업케이스][6.28]   | 문자열을 대문자로 변환합니다.      | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 추가 필터

다음 일반 필터는 콘텐츠 서식 지정 또는 변환 등 다양한 용도로 사용됩니다.

| 필터                | 설명                                                                                                                      | 지원 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [날짜][7.1]           | 타임스탬프를 다른 날짜 형식으로 변환합니다. 자세한 내용은 [날짜 필터를](#date-filter) 참조하세요.         | ✅ 예   |
| [기본값][7.2]        | 값이 할당되지 않은 변수의 기본값을 설정합니다. 문자열, 배열 및 해시와 함께 사용할 수 있습니다.      | ✅ 예   |
| [형식_주소][7.3] | 주소의 요소를 로캘에 따라 순서대로 인쇄하도록 주소 형식을 지정합니다.        | ⛔ 아니요    |
| [하이라이트][7.4]      | 제출된 검색어와 일치하는 경우 검색 결과 내의 단어를 HTML `<strong>` 태그와 함께 클래스 하이라이트로 감싸줍니다. | ⛔ 아니요    |
| `time_zone`             | 표준 [시간대 필터를](#time-zone-filter) 참조하세요.     | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

인코딩 및 URL 필터 등 더 많은 지원되는 필터는 [고급 필터]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) 페이지에서 확인할 수 있습니다.

### 날짜 필터 {#date-filter}

`date` 필터를 사용하여 타임스탬프를 다른 날짜 형식으로 변환할 수 있습니다. `date` 필터에 매개변수를 전달하여 타임스탬프 형식을 다시 지정할 수 있습니다. 이러한 매개 변수의 예는 [strfti.me](http://www.strfti.me/)입니다.

예를 들어 `date_attribute`의 값이 타임스탬프 `2021-06-03 17:13:41 UTC`라고 가정해 보겠습니다.

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

`strftime` 서식 지정 옵션 외에도 Braze는 `%s` 날짜 필터를 사용하여 타임스탬프를 unix 시간으로 변환하는 기능도 지원합니다. 예를 들어, unix 시간으로 `date_attribute`를 가져옵니다.

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 시간대 필터 {#time-zone-filter}

{% raw %}
Shopify 문서에 나열된 필터 외에도 Braze는 `time_zone` 필터도 지원합니다.

`time_zone` 필터는 시간, 표준 시간대 및 날짜 형식을 사용하여 해당 표준 시간대의 시간을 지정된 날짜 형식으로 반환합니다. 예를 들어 `{{custom_attribute.$date_attribute}}}`의 값이 `2021-08-04 9:00:00 UTC`라고 가정해 보겠습니다.
{% endraw %}

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

예약 변수 `now`를 사용하여 현재 날짜와 시간에 액세스하여 조작할 수도 있습니다.

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
