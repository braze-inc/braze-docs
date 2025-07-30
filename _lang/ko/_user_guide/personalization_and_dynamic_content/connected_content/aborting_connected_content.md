---
nav_title: 연결된 콘텐츠 중단하기
article_title: 연결된 콘텐츠 중단하기
page_order: 2
description: "이 참조 문서에서는 연결된 콘텐츠의 메시지 중단 모범 사례에 대해 설명합니다."
---

# 연결된 콘텐츠 중단하기 {#aborting-connected-content}

> When you use Liquid templating, you have the option to abort messages with conditional logic. This page covers best practices when doing so.

다음 예제에서 `connected.recommendations.size < 5` 및 `connected.foo.bar == nil` 조건문은 메시지가 중단될 수 있는 상황을 지정합니다.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Specify an abort reason

중단 사유를 지정할 수도 있으며, 이 사유는 [메시지 활동 로그]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)에 저장됩니다. 이 중단 사유는 문자열이어야 하며 리퀴드를 포함할 수 없습니다.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze doesn't count aborted messages toward the send count in your Braze account or in Currents.
{% endalert %}
