[Braze SDK를 통합한]({{site.baseurl}}/developer_guide/sdk_integration/) 후 앱을 처음 실행하는 사용자는 `changeUser` 메서드를 호출하여 `external_id` 을 할당할 때까지 "익명" 사용자로 간주됩니다. 일단 할당되면 다시 익명으로 설정할 수 없습니다. 그러나 앱을 삭제했다가 다시 설치하면 `changeUser` 을 호출할 때까지 다시 익명으로 전환됩니다.

이전에 식별된 사용자가 새 기기에서 세션을 시작하는 경우, 해당 기기에서 `external_id` 을 사용하여 `changeUser` 으로 호출하면 모든 익명 활동이 기존 프로필에 자동으로 동기화됩니다. 여기에는 새 기기에서 세션 중에 수집된 모든 속성, 이벤트 또는 기록이 포함됩니다.

{% if include.section == "user_guide" %}
{% alert tip %}
전체 안내는 [사용자 ID 설정하기를]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/) 참조하세요.
{% endalert %}
{% endif %}