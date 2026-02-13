{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
**발신자 표시 이름 + 주소** 및 **회신 주소** 필드에 [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하여 커스텀 속성에 따라 동적으로 템플릿을 만들 수 있습니다. 이를 통해 단일 이메일 캠페인 또는 캔버스 단계를 사용하여 여러 브랜드, 지역 또는 부서에서 전송할 수 있습니다.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
[오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 또는 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 트리거 이벤트의 속성정보를 참조하기 위해 컨텍스트 단계가 필요하지 않습니다. **컨텍스트 변수** 필터를 사용하여 필터 그룹에서 직접 속성을 참조할 수 있습니다. 올바른 데이터 유형을 선택했는지 확인하세요.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
카탈로그 트리거 항목에 대한 이미지를 가져오려면 카탈로그에 `image_url` 이라는 필드가 포함되어 있어야 합니다. 그런 다음 {%raw%}``{{ items[0].image_url }}``{%endraw%} 을 사용하여 참조할 수 있습니다.
{% endalert %}

{% endif %}