---
nav_title: 사용자 프로필 데이터 가져오기
article_title: 연결된 콘텐츠 호출에서 사용자 프로필 데이터 가져오기
page_order: 5
description: "이 문서에서는 사용자 프로필을 커넥티드 콘텐츠 호출로 가져오는 방법과 Liquid 템플릿과 관련된 모범 사례에 대해 설명합니다."

---

# 사용자 프로필 데이터 가져오기

> 연결된 콘텐츠 응답에 고객 프로필 필드가 포함된 경우(Liquid 개인화 태그 내), 이러한 값은 Liquid 패스백을 올바르게 렌더링하려면 연결된 콘텐츠 호출 전에 메시지 앞부분에서 Liquid를 통해 정의해야 합니다. 

마찬가지로 `:rerender` 플래그도 요청에 포함되어야 합니다. `:rerender` 플래그는 한 단계 깊이에 불과하므로 중첩된 연결된 콘텐츠 태그에는 적용되지 않습니다.

개인화를 위해 Braze는 사용자 프로필 필드를 가져온 다음 해당 필드를 Liquid에 전달하므로, 커넥티드 콘텐츠의 응답에 사용자 프로필 필드가 있는 경우 미리 정의해야 합니다. 

예를 들어 연결된 콘텐츠 호출인 경우입니다.
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
그리고 연결된 콘텐츠 응답은 {% raw %}`Your language is ${language}`{% endraw %}이며, 이 시나리오에서 표시되는 콘텐츠는 `Hi Jon, your language is`입니다. 언어 자체는 템플릿화되지 않습니다. 이는 Braze가 연결된 콘텐츠 호출을 수행하기 전에 사용자로부터 어떤 필드를 검색할지 알아야 하기 때문입니다.

Liquid 패스백을 제대로 렌더링하려면 다음 코드 스니펫에 표시된 것처럼 요청의 아무 곳에나 {% raw %}`${language}`{%endraw%} 태그를 넣어야 합니다. Liquid 전처리기는 사용자로부터 "언어" 속성을 가져와 응답 템플릿을 준비할 수 있도록 합니다.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
`:rerender` 플래그 옵션은 한 단계만 깊다는 점을 기억하세요. 연결된 콘텐츠 응답 자체에 더 많은 연결된 콘텐츠 태그가 있는 경우, Braze는 이러한 추가 태그를 다시 렌더링하지 않습니다.
{% endalert %}
