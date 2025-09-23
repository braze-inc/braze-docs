---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "이 참조 문서에서는 번역을 자동화하여 팀이 뛰어난 고객 경험을 제공하는 데 집중할 수 있도록 지원하는 로컬라이제이션 플랫폼인 Braze와 Transifex의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Transifex

> Transifex를 사용하면 언어에 관계없이 사용자 기반 전반에 걸쳐 강력한 로컬라이제이션이 가능합니다.

_이 통합은 Transifex에서 유지 관리합니다._

## 통합 정보

Braze와 Transifex의 통합을 통해 연결된 콘텐츠를 활용하여 리소스 문자열 모음을 가져오고 언어 기반 조건부 서식 대신 관련 번역을 메시지에 포함할 수 있습니다. 이를 통해 번역을 자동화하고 팀은 뛰어난 고객 경험을 제공하는 데 집중할 수 있습니다.

{% alert important %}
2022년 4월 7일 이후 Transifex는 버전 3을 위해 API 버전 2 및 2.5를 더 이상 지원하지 않습니다. v2 및 v2.5는 더 이상 작동하지 않으며, 관련 요청은 실패합니다. <br><br>다음 통합 지침은 버전 3 업데이트를 반영합니다. 이에 따라 커넥티드 콘텐츠 호출을 업데이트하세요.
{% endalert %}

## 전제 조건

| 요구 사항| 설명|
| ---| ---|
|Transifex 계정 | 이 파트너십을 이용하려면 [Transifex 계정이](https://www.transifex.com/signin/) 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Transifex 통합은 Transifex의 [리소스 번역 API](https://developers.transifex.com/reference/get_resource-translations)를 사용합니다. 다음 cURL을 사용하면 계정에 번역과 관련된 콘텐츠 값이 있는지 확인할 수 있습니다. 

먼저 Transifex 계정에 있는 `<ORGANIZATION_NAME>`, `<PROJECT_NAME>`, `<RESOURCE_NAME>` 을 입력합니다. 다음으로 `<LANGUAGE>` 을 번역을 필터링할 언어 코드로 바꾸고 `<TRANSIFEX_BEARER_TOKEN>` 을 트랜시펙스 [무기명 토큰으로](https://developers.transifex.com/reference/api-authentication) 바꿉니다.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSFIX_BEARER_TOKEN>'
```

예를 들어 Transifex 프로젝트가 `https://www.transifex.com/appboy-3/french2/french_translationspo/` 에 있는 경우 `project_name` 은 "french2"가 되고 `resource_name` 은 "french_translationspo"가 됩니다.

## 커넥티드 콘텐츠 메시지 예시

이 예제 코드 스니펫은 Transifex 리소스 번역 API와 사용자의 `language` 속성을 활용합니다. 그런 다음, 필요에 따라 문자열 오브젝트를 반복하고 다음 Liquid를 사용하여 관련 콘텐츠를 가져올 수 있습니다. `{{strings.data[X].attributes.strings.other}}`

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)
