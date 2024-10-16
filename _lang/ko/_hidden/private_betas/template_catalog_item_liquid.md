---
nav_title: 액체를 포함한 카탈로그 항목 템플릿
article_title: 액체를 포함한 카탈로그 항목 템플릿
permalink: "/templating_catalog_items_liquid/"
description: "Liquid가 포함된 카탈로그 항목을 템플릿으로 만드는 방법을 알아보세요."
page_type: reference
hidden: true
---

# Liquid를 포함한 카탈로그 항목 템플릿

 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)와 마찬가지로 Liquid 콘텐츠를 렌더링하려면 Liquid 태그에 `:rerender` 플래그가 포함되어야 합니다. `:rerender` 플래그는 한 단계 깊이에 불과하므로 중첩된 Liquid 태그 호출에는 적용되지 않는다는 점에 유의하세요.

 {% alert important %}
 Liquid를 포함하는 카탈로그 항목 템플릿은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
 {% endalert %}

카탈로그 항목에 고객 프로필 필드가 포함된 경우(Liquid 개인화 태그 내), 이러한 값은 템플릿을 생성하기 전에 Liquid를 통해 메시지 앞부분에서 정의해야 Liquid를 올바르게 렌더링할 수 있습니다. `:rerender` 플래그가 제공되지 않으면 원시 Liquid 콘텐츠를 렌더링합니다.

예를 들어 "메시지"라는 이름의 카탈로그에 이 Liquid가 있는 항목이 있는 경우입니다.

![][15]{: style="max-width:80%;"}<br>

다음과 같은 리퀴드 콘텐츠를 렌더링합니다:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

다음과 같이 표시됩니다:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
카탈로그 리퀴드 태그는 카탈로그 내에서 재귀적으로 사용할 수 없습니다.
{% endalert %}

[15]: {% image_buster /assets/img_archive/catalog_liquid_templating.png %}
