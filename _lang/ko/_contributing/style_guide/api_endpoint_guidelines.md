---
nav_title: API 엔드포인트 문서 가이드라인
article_title: API 엔드포인트 문서 가이드라인
description: "Braze API 엔드포인트를 문서화하기 위한 가이드라인입니다."
page_order: 3
noindex: true
---

# API 엔드포인트 문서 가이드라인

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> 일반적으로 API 엔드포인트 설명서는 [일반 가이드라인]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines)에 명시된 지침을 따라야 합니다. 그러나 이 문서에 나열된 것처럼 다른 콘텐츠 가이드라인이 필요할 수 있는 특수한 주제가 있습니다.

Braze는 다음 REST API 방법을 지원합니다:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## 새 엔드포인트 문서 생성

새 엔드포인트 문서를 생성할 때는 해당 엔드포인트를 [Braze API 가이드]({{site.baseurl}}/api/home)에도 추가하여 검색할 수 있도록 해야 합니다. **`_docs`** 폴더 **`> _api`** 폴더 **`> home.md`** 파일로 이동하여 엔드포인트의 경로와 한 문장 설명을 추가합니다.

## 엔드포인트 참조

일반적으로 설명서에서 엔드포인트를 참조하는 데 명확한 규칙은 없습니다. Braze 엔드포인트를 참조할 때는 사용 사례에 따라 엔드포인트를 어떻게 참조할지 최선의 판단을 내리세요.

엔드포인트를 경로(예: `/users/track`)로 참조하거나 엔드포인트 이름 뒤에 "endpoint"라는 단어를 붙여(예: the track user endpoint) 참조할 수 있습니다. 경로가 특히 긴 경우에는 엔드포인트 이름으로 참조하세요.

엔드포인트를 이름으로 참조할 때는 문장 스타일을 사용합니다. 엔드포인트를 경로로 참조할 때는 코드 텍스트를 사용합니다.

섹션 이름을 직접 참조하는 경우가 아니라면 "endpoint"라는 단어를 대문자로 쓰지 마세요. 엔드포인트를 직접 참조할 때는 "API"라는 단어를 포함하지 마세요.

엔드포인트를 API로 지칭하는 경우가 있습니다. 예를 들어, Braze 엔드포인트에 대해 일반적으로 이야기할 때 "Braze uses a REST API with many endpoints"는 정확한 표현입니다.

엔드포인트 이름에 따옴표를 넣지 마세요. 경로를 참조할 때 일반 텍스트를 사용하지 마세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">올바른 예</th><th style="width: 50%;">잘못된 예</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Use the Generate preference center URL endpoint to complete the next steps.</td><td style="width: 50%;">Use <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> to complete the next steps.</td></tr>
<tr><td style="width: 50%;">Use the <code>/users/track</code> endpoint.</td><td style="width: 50%;">Use the "Users Track" API endpoint.</td></tr>
</tbody>
</table>
{:/}

### 엔드포인트 문서 링크

엔드포인트 문서를 참조할 때는 문맥 없이도 이해할 수 있는 [의미 있는 링크 텍스트]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links)를 사용해야 합니다. 엔드포인트의 경로를 링크로 사용하는 경우, 경로만으로는 엔드포인트의 기능을 명확하게 전달하지 못할 수 있으므로 주변 텍스트에 세부 정보를 제공해야 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">올바른 예</th><th style="width: 50%;">잘못된 예</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## 제목

엔드포인트 문서의 도입부에는 다음 정보가 포함되어야 합니다:

* 요청 유형 및 엔드포인트 경로 URL  
* "Use this endpoint to…"로 시작하는 엔드포인트에 대한 간략한 설명  
* "See me in Postman" 링크  
* 필수 REST API 키 권한이 포함된 참고 알림

이 체크리스트를 사용하여 각 엔드포인트 문서에 적절한 제목(및 콘텐츠)이 나열된 순서대로 포함되어 있는지 확인하세요. 다양한 유형의 예시 요청과 같이 엔드포인트에 고유한 하위 제목이 있을 수 있습니다.

* 사용량 제한  
* 경로 매개변수  
* 요청 본문  
* 요청 매개변수  
* 예시 요청  
* 응답 매개변수  
* 예시 응답  
* 문제 해결 (해당하는 경우)

서식 가이드라인은 [제목 및 타이틀]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles)을 참조하세요.

### 경로 매개변수

엔드포인트에 경로 매개변수가 있는 경우, 경로 매개변수 제목과 테이블(요청 매개변수 테이블과 유사)을 포함합니다.

엔드포인트에 경로 매개변수가 없는 경우, 경로 매개변수 제목과 다음 안내 문구를 포함합니다: "There are no path parameters for this endpoint."

엔드포인트에 경로 또는 요청 매개변수가 모두 없는 경우, 아래와 같이 동일한 섹션에 안내 문구를 병합합니다.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## 명명 규칙

각 엔드포인트 이름은 방법 뒤에 능동 동사로 시작합니다. 이를 통해 사용자가 엔드포인트의 기능을 즉시 알 수 있습니다.

API 방법을 엔드포인트 이름의 선행 동사로 사용하지 마세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">올바른 예</th><th style="width: 50%;">잘못된 예</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

이 명명 규칙의 예외는 [Export 섹션]({{site.baseurl}}/api/endpoints/export)의 엔드포인트입니다. 섹션 이름 자체가 나열된 정보를 내보낼 수 있음을 나타내는 동사이기 때문입니다.

## API 키 권한

API 키 권한은 특정 API 호출에 대한 접근을 제한하기 위해 사용자 또는 그룹에 할당할 수 있는 권한입니다. 각 엔드포인트 문서에서 Postman 문서 링크 뒤에 다음 안내 문구를 포함하세요:

> 이 엔드포인트를 사용하려면 `permission_name_here` 권한이 있는 API 키를 생성해야 합니다.

API 키 권한의 전체 목록을 확인하려면 Braze 대시보드의 **설정 및 테스트** 아래에서 **설정 > API 키**로 이동하세요. 전체 접근 권한이 있는 API 키를 선택합니다(키 이름에 보통 "full access"라는 문구가 포함됩니다). 각 권한 이름은 일반적으로 엔드포인트 이름과 일치해야 합니다.

SCIM 엔드포인트는 개발자 콘솔 외부에서 발생하는 SCIM 통합에 특화되어 있으므로 나열된 API 키 권한이 없습니다.

## 사용량 제한

일반적으로 사용량 제한에는 요청 수와 할당된 시간을 명시해야 합니다.

총 사용량 제한을 공유하는 엔드포인트에 주의하세요. 예를 들어, 모든 비동기 카탈로그 항목 엔드포인트는 총 사용량 제한을 공유하므로 해당 문서에 이를 명시하는 것이 중요합니다.

### 사용량 제한 파일 업데이트 방법

엔드포인트 문서에서 사용량 제한을 업데이트하거나 새로운 사용량 제한을 나열해야 하는 경우, **_docs > _api > api_limits.md**로 이동하여 사용량 제한을 편집합니다.

## 매개변수

요청 및 응답 매개변수를 두 개의 별도 테이블에 정의합니다. 이 테이블에는 다음 열이 포함되어야 합니다:

* **매개변수**  
* **필수**  
* **데이터 유형**  
* **설명**

엔드포인트의 매개변수를 직접 참조하거나 **매개변수** 열에 값을 나열할 때는 코드 텍스트를 사용합니다. **필수**, **데이터 유형**, **설명** 열에 값을 나열할 때는 첫 글자를 대문자로 씁니다.

### 입력 안내 텍스트

입력 안내 텍스트에는 사용자가 포함해야 할 내용에 대한 간략한 설명과 함께 중괄호를 사용합니다.

API 키 입력 안내에는 `YOUR-REST-API-KEY`가 아닌 `YOUR_REST_API_KEY`를 사용합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">올바른 예</th><th style="width: 50%;">잘못된 예</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

API 키 입력 안내에는 `YOUR_REST_API_KEY`(밑줄 사용)를 사용하고, `YOUR-REST-API-KEY`(하이픈 사용)는 사용하지 마세요.

## 요청 및 응답

API 요청에는 헤더와 요청 매개변수가 포함됩니다. 요청 매개변수는 다음과 같은 형식이어야 합니다:

```bash
parameter": (required/optional, data type) A brief description
```

다음은 [Create new user alias 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)의 요청 본문 예시입니다:

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

예시 요청에서 문자열이나 배열인 매개변수를 식별하려면 큰따옴표(" ")를 사용합니다. 모든 열린 괄호와 소괄호가 닫혀 있는지 확인하세요.

API 응답에는 응답 본문, 헤더, HTTP 상태 코드가 포함됩니다. 항상 예시 응답을 포함하세요. 이 예시에는 매개변수를 설명하는 간단한 텍스트 예시가 포함되어야 합니다. 다음은 [Update user alias 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request)의 예시 응답입니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### 상태 코드 및 오류 코드

상태 코드는 사용자의 특정 요청이 성공적으로 완료되었는지를 나타냅니다. 사용자가 무엇이 성공으로 간주되는지 알 수 있도록 상태 코드를 포함하는 것이 도움이 될 수 있습니다. 예를 들어, 400과 404는 엔드포인트의 오류 응답 지표가 될 수 있습니다.

엔드포인트 문서에서 오류 코드를 나열해야 하는 경우, **_docs** 폴더 **> _api** 폴더 **> errors.md** 파일에 있는 [API 오류 및 응답]({{site.baseurl}}/api/errors/) 문서로 링크하세요.

## 샘플 코드

샘플 요청 및 응답과 같은 샘플 코드는 최소한의 작업으로 복사하여 사용할 수 있어야 합니다. 입력 안내 텍스트(예: 헤더의 API 키)를 제외하고, 예시 요청은 그대로 작동해야 합니다. Postman을 사용하여 요청 형식이 올바른지 확인하세요.

### 정리된 코드 vs 축소된 코드

엔드포인트의 요청에 본문이 포함된 경우, Postman에서 예시를 정리(beautify)합니다. 이렇게 하면 Braze 규칙을 배우는 개발자가 요청의 각 부분을 더 쉽게 이해할 수 있습니다.

엔드포인트의 요청 본문이 매우 짧거나 본문이 없는 경우, 불필요한 공백이 제거되도록 요청을 축소(minify)합니다. [JSON Minifier](https://codebeautify.org/jsonminifier)와 같은 도구를 사용하세요.

### 인라인 주석

예시 코드에서 한 줄 주석을 나타내려면 두 개의 슬래시(//)를 사용합니다.

인라인 주석은 코드의 특정 섹션에 사용자의 주의를 끌거나, 코드 블록의 기능을 설명하거나, 추가 컨텍스트를 제공하는 데 유용한 도구입니다.

인라인 주석을 사용하여 사용자의 로직 레이어가 배치될 위치와 SDK 코드를 참조하는 방법을 빠르게 보여줍니다. 간단하지만 현실적인 예시를 사용하세요. 예를 들어, "example_attribute"보다 "favorite_movie"라는 예시 속성이 더 효과적입니다. 사용자의 비즈니스가 최종 사용자의 좋아하는 영화를 추적하거나 관심을 갖지 않더라도, 이 예시는 이 속성을 통해 추적할 수 있는 *종류*의 사용 사례를 보여줍니다. 일반적인 예시는 같은 직관적 이해를 이끌어내지 못합니다.

사람이 읽을 수 있는 코드나 메서드 이름을 단순히 반복하는 인라인 주석은 피하세요. 대신, 영어가 모국어가 아닌 사용자를 위한 이해를 돕기 위해 Braze 전용 메서드 및 매개변수에 대해 다양한 동의어를 사용하세요.

일반적으로 인라인 주석을 제공할 때는 표준 영어 규칙을 따르세요. 예를 들어, 문장을 대문자로 시작하고, 단어를 완전히 철자하는 등의 규칙을 따릅니다.

## 추가 리소스

- [Google 개발자 설명서 스타일 가이드](https://developers.google.com/style)  
  - [API 참조 코드 및 주석](https://developers.google.com/style/api-reference-comments)