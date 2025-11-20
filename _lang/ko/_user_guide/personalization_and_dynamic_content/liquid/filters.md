---
nav_title: 필터
article_title: Liquid 필터
page_order: 3
description: "이 참조 페이지에는 정적 또는 동적 콘텐츠의 형식을 다시 지정하는 데 사용할 수 있는 필터가 나열되어 있습니다."

---

# 필터

> 이 참고 문서에서는 Liquid의 필터에 대한 개요를 제공하고 Braze에서 지원하는 필터에 대해 설명합니다. 이러한 필터를 활용하는 방법에 대한 아이디어를 찾고 계신가요? [Liquid 사용 사례 라이브러리를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/) 확인하세요.

필터는 Liquid에서 숫자, 문자열, 변수 및 객체의 출력을 수정할 수 있는 방법입니다. 필터를 사용하여 문자열을 소문자에서 대문자로 변경하거나 덧셈이나 나눗셈과 같은 수학 연산을 수행하는 등 정적 또는 동적 텍스트의 형식을 변경할 수 있습니다.

{% alert important %}
Braze는 Shopify의 모든 Liquid 필터를 지원하지 않습니다. 이 페이지에서는 Braze가 테스트한 Liquid 필터를 간략하게 소개하지만 전체 목록이 아닐 수도 있습니다. 메시지를 보내기 전에 항상 Liquid를 테스트하세요. <br><br>여기에 나열되지 않은 필터에 대해 궁금한 점이 있으면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필터 구문

{% raw %}

필터는 출력 태그 `{{ }}` 내에 배치해야 하며 파이프 문자 `|` 로 표시해야 합니다.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

이 예에서 `Big Sale` 은 문자열이고 `upcase` 은 적용 중인 필터입니다.

### 여러 필터에 대한 구문

하나의 출력에 여러 필터를 사용할 수 있습니다. 왼쪽에서 오른쪽으로 적용됩니다.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
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
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | 매개변수로 전달된 문자를 사용하여 배열의 요소를 조인합니다. 결과는 하나의 문자열입니다.          | ✅ 예   |
| [먼저](https://shopify.dev/docs/api/liquid/filters/first)         | 배열의 첫 번째 요소를 반환합니다. 커스텀 속성 배열에서 가장 오래된 부가 가치입니다.                | ✅ 예   |
| [마지막](https://shopify.dev/docs/api/liquid/filters/last)          | 배열의 마지막 요소를 반환합니다. 커스텀 속성 배열에서 가장 최근에 추가된 값입니다.          | ✅ 예   |
| [컴팩트](https://shopify.dev/api/liquid/filters/compact)       | 배열에서 `nil` 항목을 제거합니다.                                                                             | ✅ 예   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | 배열을 다른 배열과 결합합니다.                                                                              | ✅ 예   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | 배열에서 지정된 인덱스 위치에 있는 항목을 반환합니다. 배열의 첫 번째 항목은 `[0]` 로 참조됩니다. | ⛔ 아니요   |
| [매핑](https://shopify.dev/api/liquid/filters/map)           | 배열 요소의 속성을 매개변수로 받아 각 배열 요소의 값으로 배열을 생성합니다.        | ✅ 예   |
| [역방향](https://shopify.dev/api/liquid/filters/reverse)       | 배열에 있는 항목의 순서를 반대로 바꿉니다.                                                                       | ✅ 예   |
| [크기](https://shopify.dev/api/liquid/filters/size)          | 문자열(문자 수) 또는 배열(요소 수)의 크기를 반환합니다.                      | ✅ 예   |
| [정렬](https://shopify.dev/api/liquid/filters/sort)         | 배열에 있는 요소의 주어진 속성을 기준으로 배열의 요소를 정렬합니다.                                    | ✅ 예   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | 배열의 항목을 대소문자를 구분하지 않는 알파벳 순서로 정렬합니다.                                                | ✅ 예   |
| [유니크](https://shopify.dev/api/liquid/filters/uniq)         | 배열에 있는 요소의 중복 인스턴스를 제거합니다.                                                           | ✅ 예   |
| [어디](https://shopify.dev/api/liquid/where)        | 특정 속성 값을 가진 항목만 포함하도록 배열을 필터링합니다.                                             | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 컬러 필터

Braze에서는 [컬러 필터가](https://shopify.dev/api/liquid/filters/color-filters) 지원되지 않습니다.

## 글꼴 필터

Braze에서는 [글꼴 필터가](https://shopify.dev/api/liquid/filters/font-filters) 지원되지 않습니다.

## 수학 필터

수학 필터를 사용하면 수학적 연산을 수행할 수 있습니다. 하나의 출력에 여러 필터를 사용하는 경우 왼쪽에서 오른쪽으로 필터가 적용됩니다.

| 필터  | 정의      | 지원 |
| :------ |:----------------| :-------- |
| [복근](https://shopify.dev/api/liquid/filters/abs)        | 숫자의 절대값을 반환합니다.     | ✅ 예   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | 숫자를 최대값으로 제한합니다.   | ✅ 예   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | 숫자를 최소값으로 제한합니다.   | ✅ 예   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | 출력을 가장 가까운 정수로 반올림합니다.  | ✅ 예   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | 출력을 숫자로 나눕니다. 출력은 가장 가까운 정수로 반내림됩니다. 반올림을 방지하려면 다음 팁을 확인하세요. | ✅ 예   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | 출력을 가장 가까운 정수로 반내림합니다.        | ✅ 예   |
| [마이너스](https://shopify.dev/api/liquid/filters/minus)      | 출력에서 숫자를 뺍니다.          | ✅ 예   |
| [플러스](https://shopify.dev/api/liquid/filters/plus)       | 출력에 숫자를 추가합니다.     | ✅ 예   |
| [라운드](https://shopify.dev/api/liquid/filters/round)      | 출력을 가장 가까운 정수 또는 지정된 소수점 이하로 반올림합니다.  | ✅ 예   |
| [횟수](https://shopify.dev/api/liquid/filters/times)     | 출력에 숫자를 곱합니다.       | ✅ 예   |
| [모듈](https://shopify.dev/api/liquid/filters/modulo)    | 출력을 숫자로 나누고 나머지를 반환합니다.   | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Liquid에서 정수(정수)를 정수로 나눌 때 답이 플로트(소수점이 있는 숫자)인 경우, Liquid는 자동으로 가장 가까운 정수로 반내림합니다. 그러나 정수를 플로트로 나누면 항상 플로트를 얻을 수 있습니다. 즉, 정수를 플로트(1.0, 2.0, 3.0)로 변환하여 플로트를 반환할 수 있습니다.
{% raw %}
<br><br>예를 들어`{{15 | divided_by: 2}}` 은 `7` 을 출력하고 `{{15 | divided_by: 2.0}}` 은 `7.5` 을 출력합니다.
{% endraw %}
{% endalert %}

### 커스텀 속성이 있는 수학 연산

두 커스텀 속성 간에는 수학 연산을 수행할 수 없다는 점에 유의하세요.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

이 예제는 Liquid의 한 줄에서 여러 커스텀 속성을 참조할 수 없기 때문에 작동하지 않습니다. 대신 수학 함수가 수행되기 전에 이러한 값 중 하나 이상에 변수를 할당해야 합니다. 두 개의 커스텀 속성을 함께 추가하려면 두 줄의 Liquid가 필요합니다:

1. 변수에 커스텀 속성을 할당하는 데 사용됩니다,
2. 하나는 추가를 수행합니다.

#### 사용 사례: 현재 잔액 계산하기

기프트 카드 잔액과 리워드 잔액을 더하여 사용자의 현재 잔액을 계산하고 싶다고 가정해 보겠습니다.

1. `assign` 태그를 사용하여 `current_rewards_balance` 의 커스텀 속성을 '잔액'이라는 용어로 대체합니다. 즉, 이제 조작할 수 있는 `balance` 이라는 변수가 생겼습니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. `plus` 필터를 사용하여 각 사용자의 기프트 카드 잔액을 `{{balance}}` 개체로 표시되는 리워드 잔액과 결합합니다.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 머니 필터

사용자의 구매, 계정 잔액 또는 돈과 관련된 내용을 업데이트하는 경우에는 돈 필터를 사용해야 합니다. 돈 필터는 소수점이 올바른 위치에 있는지 확인하고 업데이트의 일부가 손실되지 않도록 합니다(예: 마지막에 있는 성가신 `0` ).

| 필터         | 정의          | 지원 |
| :--------------- | :--------------- | :-------- |
| [돈](https://shopify.dev/api/liquid/filters/money)      | 소수점이 올바른 위치에 있고 숫자 끝에서 0이 빠지지 않도록 숫자 서식을 지정합니다.   | ✅ 예   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | 통화 기호로 숫자 서식을 지정합니다.     | ⛔ 아니요    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | 통화 기호 없이 숫자의 서식을 지정합니다.      | ⛔ 아니요    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
`money` 필터로 숫자의 형식을 올바르게 지정하려면 숫자에서 쉼표를 제거하고 `money` 필터 앞에 `plus: 0` 필터를 추가합니다. 예를 들어 다음 Liquid를 참조하세요:<br><br>
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
커스텀 속성(예: `account_balance`)을 입력하는 경우 항상 `money` 필터를 사용하여 소수점을 올바른 위치에 배치하고 숫자 끝에서 0이 빠지지 않도록 해야 합니다:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| 머니 필터 사용                       | 머니 필터 없이                    |
| :------------------------------------------ | :------------------------------------------ |
| \![돈 필터 포함]({% image_buster /assets/img/with_money_filter.png %})                     | \![돈 필터 제외]({% image_buster /assets/img/without_money_filter.png %})                  |
| 여기서 `account_balance` 은 `17.8` 에 입력합니다. | 여기서 `account_balance` 은 `17.8` 에 입력합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze의 `money` 필터는 사전 설정에 따라 소수점이 자동으로 적용되지 않으므로 Shopify와 다릅니다. 예를 들어 `rewards_redeemed` 에 `145` 값이 포함된 다음 시나리오를 예로 들어 보겠습니다:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Shopify의 [머니](https://shopify.dev/api/liquid/filters/money) 필터에 따르면 `$1.45` 의 출력을 가져야 하지만 Braze에서는 `$145.00` 의 출력을 가져옵니다. 해결 방법으로 `divided_by` 필터를 사용하여 숫자를 10진수로 조작한 후 돈 필터를 적용할 수 있습니다:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 문자열 필터

문자열 필터는 문자열의 출력과 변수를 조작하는 데 사용됩니다. 문자열은 영숫자 문자의 조합이며 큰따옴표로 묶어야 합니다.

{% alert note %}
Liquid에서 직선 따옴표는 곡선 따옴표와 다릅니다. 텍스트 편집기에서 따옴표로 묶으면 Liquid에 오류가 발생할 수 있으므로 복사하여 Braze에 붙여넣을 때 주의하세요. Liquid를 Braze에 직접 작성하는 경우, 따옴표는 자동으로 적용됩니다.
{% endalert %}

| 필터          | 설명     | 지원 |
| :--------------- | ------------- | --------- |
| [추가](https://shopify.dev/api/liquid/filters/append)     | 문자열에 문자를 추가합니다.           | ✅ 예   |
| [카멜라이즈](https://shopify.dev/docs/api/liquid/filters/camelize)     | 문자열을 카멜케이스로 변환합니다.             | ⛔ 아니요    |
| [대문자](https://shopify.dev/api/liquid/filters/capitalize)     | 문자열의 첫 번째 단어는 대문자로 표시하고 나머지 문자는 소문자로 표시합니다.         | ✅ 예   |
| [소문자](https://shopify.dev/api/liquid/filters/downcase)      | 문자열을 소문자로 변환합니다.         | ✅ 예   |
| [탈출](https://shopify.dev/api/liquid/filters/escape)    | 문자열을 이스케이프합니다.             | ✅ 예   |
| [핸들사이즈](https://shopify.dev/api/liquid/filters/handleize)        | 문자열을 핸들로 포맷합니다.        | ⛔ 아니요    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | 문자열을 MD5 해시로 변환합니다. 자세한 내용은 [인코딩 필터를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) 참조하세요.   | ✅ 예   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | 문자열을 SHA-1 해시로 변환합니다. 자세한 내용은 [인코딩 필터를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) 참조하세요.  | ✅ 예   |
| hmac_sha1_hex<br>(이전 [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-1 해시로 변환합니다. 메시징의 비밀 키를 필터에 파라미터로 전달합니다. 자세한 내용은 [인코딩 필터를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters) 참조하세요. | ✅ 예   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-256 해시로 변환합니다. 메시징의 비밀 키를 필터에 파라미터로 전달합니다.       | ✅ 예   |
| hmac_sha512 | 해시 메시지 인증 코드(HMAC)를 사용하여 문자열을 SHA-512 해시로 변환합니다. 메시징의 비밀 키를 필터에 파라미터로 전달합니다. | ✅ 예  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | 문자열의 각 줄 바꿈 앞에 `<br>` 줄 바꿈 HTML 태그를 삽입합니다.        | ✅ 예   |
| [복수화](https://shopify.dev/api/liquid/filters/pluralize)   | 숫자 값에 따라 영어 문자열의 단수 또는 복수 버전을 출력합니다.      | ⛔ 아니요    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | 문자열에 문자를 추가합니다.      | ✅ 예   |
| [제거](https://shopify.dev/api/liquid/filters/remove)      | 문자열에서 하위 문자열의 모든 항목을 제거합니다.       | ✅ 예   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | 문자열에서 하위 문자열의 첫 번째 항목만 제거합니다.      | ✅ 예   |
| [대체](https://shopify.dev/api/liquid/filters/replace)        | 문자열의 모든 항목을 하위 문자열로 바꿉니다.   | ✅ 예   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | 문자열의 첫 번째 항목을 하위 문자열로 바꿉니다.      | ✅ 예   |
| [슬라이스](https://shopify.dev/api/liquid/filters/slice)       | 슬라이스 필터는 지정된 인덱스에서 시작하는 하위 문자열을 반환합니다.       | ✅ 예   |
| [분할](https://shopify.dev/api/liquid/filters/split)  | 분할 필터는 하위 문자열을 매개변수로 사용합니다. 하위 문자열은 문자열을 배열로 구분하는 구분 기호로 사용됩니다.            | ✅ 예   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | 문자열의 왼쪽과 오른쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.                                                                                                    | ✅ 예   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | 문자열의 왼쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.    | ⛔ 아니요    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | 문자열의 오른쪽에서 탭, 공백, 줄 바꿈(모두 공백)을 제거합니다.          | ⛔ 아니요    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | 문자열에서 모든 HTML 태그를 제거합니다.        | ✅ 예   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | 문자열에서 줄 바꿈/새 줄을 제거합니다.        | ✅ 예   |
| [잘라내기](https://shopify.dev/api/liquid/filters/truncate)    | 문자열을 첫 번째 매개변수로 전달된 문자 수만큼 잘라냅니다. 잘린 문자열에는 줄임표(...)가 추가되며 문자 수에 포함됩니다.    | ✅ 예   |
| [잘라낸 단어](https://shopify.dev/api/liquid/filters/truncatewords)   | 첫 번째 매개변수로 전달된 단어 수만큼 문자열을 잘라냅니다. 잘린 문자열에는 줄임표(...)가 추가됩니다.    | ✅ 예   |
| [업케이스](https://shopify.dev/api/liquid/filters/upcase)   | 문자열을 대문자로 변환합니다.      | ✅ 예   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 추가 필터

다음의 일반 필터는 콘텐츠 서식 지정 또는 변환 등 다양한 용도로 사용됩니다.

| 필터                | 설명                                                                                                                      | 지원 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [날짜](https://shopify.dev/api/liquid/filters/date)           | 타임스탬프를 다른 날짜 형식으로 변환합니다. 자세한 내용은 [날짜 필터를](#date-filter) 참조하세요.         | ✅ 예   |
| [기본값](https://shopify.dev/api/liquid/filters/default)        | 값이 지정되지 않은 변수에 대한 기본값을 설정합니다. 문자열, 배열 및 해시와 함께 사용할 수 있습니다.      | ✅ 예   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | 주소의 요소를 로캘에 따라 순서대로 인쇄하도록 주소 형식을 지정합니다.        | ⛔ 아니요    |
| [하이라이트](https://shopify.dev/api/liquid/filters/highlight)      | 제출된 검색어와 일치하는 경우 클래스 하이라이트가 포함된 HTML `<strong>` 태그로 검색 결과 내부의 단어를 감싸줍니다. | ⛔ 아니요    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

인코딩 및 URL 필터 등 더 많은 지원되는 필터는 [고급 필터]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) 페이지에서 확인할 수 있습니다.

### 날짜 필터 {#date-filter}

`date` 필터를 사용하여 타임스탬프를 다른 날짜 형식으로 변환할 수 있습니다. `date` 필터에 매개변수를 전달하여 타임스탬프 형식을 다시 지정할 수 있습니다. 이러한 매개 변수의 예는 [strfti.me](http://www.strfti.me/).

예를 들어 `date_attribute` 의 값이 타임스탬프 `2021-06-03 17:13:41 UTC` 라고 가정해 보겠습니다.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

`strftime` 서식 옵션 외에도 Braze는 `%s` 날짜 필터를 사용하여 타임스탬프를 Unix 시간으로 변환하는 기능도 지원합니다. 예를 들어 Unix 시간으로 `date_attribute` 를 가져옵니다:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}