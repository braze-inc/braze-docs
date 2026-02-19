익명 사용자에게는 `external_ids` 이 없지만 대신 [사용자 별칭을]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) 지정할 수 있습니다. 사용자에게 다른 식별자를 추가하고 싶지만 `external_id` 주소가 무엇인지 모르는 경우(예: 로그인하지 않은 경우) 사용자 별칭을 지정해야 합니다. 사용자 별칭 지정도 가능합니다:

- Braze API를 사용하여 익명 사용자와 관련된 이벤트 및 속성을 로그에 기록하세요.
- [외부 사용자 ID가 비어 있음]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) 세분화 필터를 사용하여 메시징에서 익명 사용자를 타겟팅하세요.

{% if include.section == "user_guide" %}
{% alert tip %}
전체 안내는 [Braze 소프트웨어 개발 키트를 참조하세요: 사용자 별칭 지정]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}