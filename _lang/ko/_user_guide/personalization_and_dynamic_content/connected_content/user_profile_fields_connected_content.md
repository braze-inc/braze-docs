---
nav_title: 사용자 프로필 데이터 가져오기
article_title: 연결된 콘텐츠 호출에서 사용자 프로필 데이터 가져오기
page_order: 3
description: "이 문서에서는 연결된 콘텐츠 호출에 고객 프로필을 가져오는 방법과 Liquid 템플릿과 관련된 모범 사례에 대해 설명합니다."
toc_headers: h2
---

# 사용자 프로필 데이터 가져오기

> 이 페이지에서는 연결된 콘텐츠 호출에 고객 프로필을 가져오는 방법과 Liquid 템플릿과 관련된 모범 사례를 다룹니다. 

## 전제 조건

연결된 콘텐츠 응답에 고객 프로필 필드가 포함된 경우(Liquid 개인화 태그 내), 이러한 값은 연결된 콘텐츠 호출 전에 연결된 콘텐츠 메시지 앞부분에서 정의해야 Liquid 패스백을 올바르게 렌더링할 수 있습니다. 마찬가지로 `:rerender` 플래그도 요청에 포함되어야 합니다. `:rerender` 플래그는 한 단계 깊이에 불과하므로 중첩된 연결된 콘텐츠 태그에는 적용되지 않습니다.

## 연결된 콘텐츠 호출의 Liquid 템플릿 지정

개인화를 위해 Braze는 해당 필드를 Liquid에 전달하기 전에 고객 프로필 필드를 가져오므로 연결된 콘텐츠의 응답에 사용자 프로필 필드가 있는 경우 이를 미리 정의해야 합니다. 

예를 들어 연결된 콘텐츠 호출인 경우입니다:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

연결된 콘텐츠 응답은 {% raw %}`Your language is ${language}`{% endraw %} 입니다. 이 예제에서 표시되는 콘텐츠는 `Hi Jon, your language is` 입니다. 

언어 자체는 템플릿화되지 않습니다. 이는 연결된 콘텐츠 호출을 하기 전에 사용자로부터 어떤 필드를 검색할지 Braze가 알아야 하기 때문입니다.

Liquid 패스백을 올바르게 렌더링하려면 다음 코드 스니펫에 표시된 것처럼 요청의 아무 곳에나 {% raw %}`${language}`{% endraw %} 태그를 포함해야 합니다. Liquid 전처리기는 사용자로부터 "언어" 속성을 가져와 응답 템플릿을 준비할 수 있습니다.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
`:rerender` 플래그 옵션은 한 단계만 깊다는 점을 기억하세요. 연결된 콘텐츠 응답 자체에 연결된 콘텐츠 태그나 카탈로그 태그가 더 있는 경우 Braze는 이러한 추가 태그를 다시 렌더링하지 않습니다.
{% endalert %}

## 모범 사례

### JSON 형식을 깨뜨릴 수 있는 Liquid 태그와 함께 `json_escape` 사용

`:rerender` 를 사용하는 경우 잠재적으로 JSON 형식을 깨뜨릴 수 있는 모든 Liquid 태그에 `json_escape` 필터를 추가하세요. Liquid 태그에 JSON 형식을 깨는 문자가 포함되어 있으면 전체 연결된 콘텐츠 응답이 텍스트로 해석되어 메시징에 템플릿화되며 변수는 저장되지 않습니다.

예를 들어 아래 예시의 `message` 이벤트 속성정보에 JSON 형식을 깨뜨릴 수 있는 문자가 포함되어 있는 경우 이 예시와 같이 `json_escape` 필터를 추가합니다:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}