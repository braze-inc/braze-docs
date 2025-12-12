---
nav_title: 연결된 콘텐츠 중단하기
article_title: 연결된 콘텐츠 중단하기
page_order: 2
description: "이 참조 문서에서는 연결된 콘텐츠에 대한 메시지 중단 모범 사례를 다룹니다."
---

# 연결된 콘텐츠 중단하기 {#aborting-connected-content}

> Liquid 템플릿을 사용하면 조건 로직으로 메시지를 중단할 수 있는 옵션이 있습니다. 이 페이지에서는 모범 사례에 대해 설명합니다.

다음 예제에서 `connected.recommendations.size < 5` 및 `connected.foo.bar == nil` 조건문은 메시징이 중단될 수 있는 상황을 지정합니다.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## 중단 사유 지정

중단 사유를 지정할 수도 있으며, 이 사유는 [메시지 활동 로그에]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 저장됩니다. 이 중단 사유는 문자열이어야 하며 Liquid를 포함할 수 없습니다.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
중단된 메시지는 Braze 계정이나 커런츠의 전송 횟수에 포함되지 않습니다.
{% endalert %}
