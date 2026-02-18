{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
콘텐츠 카드에는 최대 게재빈도 설정이 적용되지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
"12-1-2021" 또는 "12/1/2021"과 같은 날짜 문자열은 날짜/시간 개체로 변환되어 [시간 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time)으로 처리됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
모든 고객 프로필 데이터(커스텀 이벤트, 커스텀 속성, 커스텀 데이터)는 해당 프로필이 활성 상태인 동안 저장됩니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze는 사용자가 앱을 처음 사용할 때까지 프로필을 생성하지 않으므로 아직 앱을 열지 않은 사용자를 타겟팅할 수 없습니다.
{% endalert %}

{% endif %}
