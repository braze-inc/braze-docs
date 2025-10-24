| 권한 | 목적 | 필수 사항인가요? |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | 테스트 전송을 사용할 때 임시 사용자 프로필을 생성하는 것 외에 고객 프로필의 커스텀 속성도 업데이트합니다. | ✓ |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | 테스트 전송을 사용하는 동안 생성된 임시 고객 프로필을 삭제합니다. | 테스트 전송 전용 |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | 선택한 각 세그먼트의 사용자 목록을 내보내 매일 아침 사용 가능한 오디언스 커뮤니케이션을 업데이트합니다. | ✓ |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | 세그먼트 대신 `external_id`를 사용하여 사용자를 타겟팅할 때 식별자 목록을 검색합니다. Decisioning Studio에서는 개인 식별 정보(PII)가 허용되지 않으므로, `fields_to_export` 매개변수에서 PII가 아닌 필드만 반환되도록 해야 합니다.
 | `external_ids`를 사용하는 경우에만 |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Decisioning Studio의 실험자를 위해 구성된 API 캠페인을 사용하여 권장 시간에 추천 배리언트를 전송합니다. | ✓ |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | 활성 캠페인 목록을 검색하고 실험용으로 사용 가능한 이메일 콘텐츠를 추출합니다. | ✓ |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 집계된 캠페인 데이터를 내보내 Decisioning Studio에서 보고, 검증 및 문제 해결을 활성화함으로써 보고 값을 비교하고 기준 성과를 분석할 수 있도록 합니다.<br><br>이 권한은 필수는 아니지만 권장되는 권한입니다. |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 실험을 위해 기존 캠페인에서 HTML 콘텐츠, 제목란, 이미지 리소스를 검색합니다. | ✓ |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | 활성 캔버스 목록을 검색하여 실험에 사용할 수 있는 이메일 콘텐츠를 추출합니다. | ✓ |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 특히 BAU가 캔버스를 통해 오케스트레이션되는 경우에 보고 및 검증을 위해 집계된 캔버스 데이터를 내보냅니다.<br><br>이 권한은 필수는 아니지만 권장되는 권한입니다. |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | 실험을 위해 기존 캔버스에서 HTML 콘텐츠, 제목란, 이미지 리소스를 검색합니다. | ✓ |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Decisioning Studio 실험자를 위한 잠재적 타겟 오디언스로서 기존의 모든 세그먼트를 검색합니다. | ✓ |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 오디언스 선택 시 Decisioning Studio에 표시되는 세그먼트 크기 정보를 내보냅니다. | ✓ |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | 오디언스 규모 또는 성과의 변화를 이해하는 데 도움이 되는, 진입 및 퇴장 기준과 같은 세그먼트 세부 정보를 검색합니다. |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | 원본을 변경하지 않으면서, [동적 입력 안내]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)(Braze Liquid 태그)를 사용하여 실험을 위해 선택한 기본 HTML 템플릿의 복사본을 생성합니다. | ✓ |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | 클릭 유도와 같은 실험 기준이 변경되면 Studio에서 만든 템플릿 사본에 업데이트를 푸시합니다. | ✓ |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | Decisioning Studio에서 만든 템플릿에 대한 정보를 Braze 인스턴스에서 검색합니다. | ✓ |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 템플릿이 Braze 인스턴스에 성공적으로 복사되었는지 확인합니다. | ✓ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }