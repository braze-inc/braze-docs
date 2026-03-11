{% if include.alert == 'User profile external_id' %}

{% alert warning %}
사용자 프로필에 `external_id` 을 할당하지 말고 고유하게 식별할 수 있도록 하세요. 사용자를 식별한 후에는 익명으로 되돌릴 수 없습니다.
<br><br>
`external_id`은 [`/users/external_ids/rename` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)를 사용하여 업데이트할 수 있습니다. 그러나 사용자의 세션 중에 다른 `external_id`를 설정하려는 모든 시도는 새로운 `external_id`가 연결된 새로운 고객 프로필을 생성합니다. 두 프로필 간에 데이터가 전달되지 않습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
If you intend to create more than one of the same Currents connectors (for example, two message engagement event connectors), they must be in different workspaces. Because the Braze Segment Currents integration cannot isolate events by different apps in a single workspace, failure to do this will lead to unnecessary data deduping and lost data.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
행동 기반 캠페인 또는 캔버스를 오디언스 필터(예: 변경된 속성 또는 커스텀 이벤트 수행)와 동일한 트리거로 구성하지 마세요. 사용자가 트리거 이벤트를 수행할 때 오디언스에 있지 않은 경우 [경합 조건]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)이 발생할 수 있으며, 이는 캠페인을 받지 않거나 캔버스에 들어가지 않음을 의미합니다.
{% endalert %}

{% endif %}
