---
nav_title: 고급 필터
article_title: 고급 액체 필터
page_order: 4
description: "이 참고 문서에는 고급 필터, 예제 및 캠페인에서 필터를 사용하는 방법이 나와 있습니다."

---

# 고급 필터

> 이 참고 문서에서는 Liquid의 고급 필터에 대한 개요와 사용 방법을 설명합니다.

## 인코딩 필터

{% raw %}
| 필터 이름 | 필터 설명 | 예제 입력 | 예제 출력 | 예제 출력
\|---|---|---|---|
`md5` | md5로 인코딩된 문자열 반환 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | sha1 인코딩된 문자열 반환 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | sha2(256비트, SHA-256이라고도 함) 인코딩된 문자열 반환 | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204|
`base64` base64로 인코딩된 문자열 반환 | `{{'blah' | base64_encode}}` | YmxhaA== | |
`hmac_sha1_hex` (이전 `hmac_sha1`) | 16진수 문자열로 인코딩된 hmac-sha1 서명을 반환합니다 | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |.
`hmac_sha1_base64` | 베이스64 문자열로 인코딩된 hmac-sha1 서명을 반환합니다 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | 헥스 문자열로 인코딩된 hmac-sha256 서명을 반환합니다 | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e|
`hmac_sha256_base64` 베이스64 문자열로 인코딩된 hmac-sha256 서명을 반환 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## URL 필터

| 필터 이름 | 필터 설명 | 입력 예시 | 출력 예시 |
|---|---|---|---|
| `url_escape` | URLS에서 허용되지 않는 문자열의 모든 문자를 식별하고 해당 문자를 이스케이프된 변형으로 바꿉니다. | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | URL에서 허용되지 않는 문자열의 모든 문자를 앰퍼샌드(&)를 포함한 이스케이프된 변형으로 바꿉니다. | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | URL 친화적인 문자열을 인코딩합니다. | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
`assign` 태그를 HTML과 결합하면 여러 개의 하이퍼링크를 만들 때 시간과 노력을 절약할 수 있습니다.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## 속성정보 접근자 필터

| 필터 이름 | 필터 설명 |
|---|---|---|---|
| `property_accessor` | 해시 및 해시 키를 가져와 해당 키에서 해당 해시에 있는 값을 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**해시 예시:** `{"a" => 42, "b" => 0}`
**입력 예시:** `{{hash | property_accessor: 'a'}}`
**출력 예시:** `42`

또한 속성 접근자 필터를 사용하면 사용자 지정 속성을 해시 키로 템플릿화하여 특정 해시 값에 액세스할 수 있습니다.

{% endraw %}

{% alert note %}
Braze 내에서는 Liquid에서 해시를 변수(예: 표현식)로 인스턴스화할 수 있는 방법이 없습니다.
{% endalert %}

{% raw %}

## 숫자 서식 필터

| 필터 이름 | 필터 설명 | 입력 예시 | 출력 예시 |
|---|---|---|---|
| `number_with_delimiter` | 쉼표로 숫자 서식 지정 | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## JSON 이스케이프 / 문자열 이스케이프 필터

| 필터 이름 | 필터 설명 |
|---|---|---|---|
| `json_escape` | 문자열에 있는 모든 특수 문자(예: 큰따옴표 `""` 및 백슬래시 '')를 이스케이프 처리합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 필터는 JSON 사전에서 문자열을 개인화할 때 항상 사용해야 하며 특히 웹훅에 유용합니다.
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#null 속성 값에 대한 회계 처리
