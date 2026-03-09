## 세분화된 권한 마이그레이션

{% alert important %}
세분화된 권한은 초기 액세스 중입니다. 귀사의 마이그레이션이 계획될 때, 귀하의 Braze 관리자에게 [세분화된 권한 마이그레이션]({{site.baseurl}}/granular_permissions_migration/)에 대한 이메일과 대시보드 배너가 전송됩니다.
{% endalert %}

기존 SCIM 통합 및 [레거시 SCIM API 객체]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api)는 4월 말 세분화된 권한 마이그레이션 후에도 계속 작동합니다. 

즉각적인 조치를 취할 필요는 없습니다. 그러나 세분화될 권한에 대해 통합을 검토할 것을 권장합니다. 예를 들어, 현재 API에서 `basic_access`을(를) 전송하고 있다면, 세분화 후 특정 권한(예: `"appGroupPermissions":["view_campaigns","edit_campaigns"]`)을 포함하도록 통합을 업데이트할 것을 제안합니다. Braze는 세분화된 권한 마이그레이션 후에도 기존 통합이 중단되지 않도록 `basic_access`과 같은 레거시 문자열을 계속 수용합니다.

## 권한 객체

권한 객체는 SCIM ID 권한을 통해 사용자 리소스와 상호 작용할 때 일부 요청 및 응답에서 발견되는 필드입니다.

{% alert note %}
앱 그룹은 Braze에서 워크스페이스로 이름이 변경되었지만, 이 페이지의 키는 여전히 이전 용어를 참조합니다(예: `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

유효한 권한 객체는 다음 키-값 쌍을 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | Description |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | 사용자가 해당 권한을 가지고 있는지에 따라 문자열의 존재가 일치하는 [회사 수준 권한 문자열]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company)의 배열입니다. |
| `roles` | 선택 사항 | 배열 | [역할 객체의]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object) 배열입니다. |
| `appGroup` | 필수 | 배열 | [작업 공간 권한 객체]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object)의 배열. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 작업 공간 권한 객체

유효한 앱 그룹 권한 객체는 다음 키-값 페어를 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | Description |
| --- | --- | --- | --- |
| `appGroupName`| Optional | 문자열 | 작업 공간의 이름. 이 객체에 포함된 권한이 적용될 워크스페이스를 지정하는 데 사용됩니다. | 
| `appGroupId` | `appGroupName`이(가) 없으면 필수 | 문자열 | 워크스페이스의 ID로, 워크스페이스를 지정하는 대체 방법으로 사용됩니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 설정 개체]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object)이 있는 배열. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대한 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [팀 권한 객체]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object) 배열. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 작업 공간 권한 설정 객체 {#workspace-permissions-set-object}

유효한 워크스페이스 권한 설정 객체는 다음 키-값 페어를 가진 JSON 객체입니다.

| 키 | 필수 | 데이터 유형 | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | 문자열 | 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이(가) 없으면 필수 | 문자열 | 워크스페이스의 ID로, 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 팀 권한 객체

유효한 팀 권한 객체는 다음 키-값 쌍을 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | Description |
| --- | --- | --- | --- |
| `teamName` | Optional | 문자열 | 팀의 이름, 이 개체 내의 권한이 어떤 팀을 위한 것인지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이(가) 없으면 필수 | 문자열 | 팀의 ID, 팀을 지정하는 대체 방법으로 사용됩니다. |
| `teamPermissions` | 필수 | 배열 | [teams permission strings]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대한 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 역할 개체

유효한 역할 객체는 다음과 같은 키 값 쌍을 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | Description |
| --- | --- | --- | --- |
| `roleName` | Optional | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이(가) 없으면 필수 | 문자열 | 역할을 지정하는 대체 방법으로 사용되는 역할의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 부록

### 회사 권한 문자열 {#company}

| UI에 표시된 대로 | SCIM API 문자열 |
| --- | --- |
| 관리자 | `admin` |
| 회사 설정 관리 | `manage_company_settings` |
| 워크스페이스 생성 및 삭제| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 작업 공간 권한 문자열 {#workspace-strings}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| 캠페인 보기 | `view_campaigns` |
| 캠페인 편집 | `edit_campaigns` |
| 캠페인 보관 | `archive_campaigns` |
| 캔버스 보기 | `view_canvases` |
| 캔버스 편집 | `edit_canvases` |
| 캔버스 보관 | `archive_canvases` |
| 최대 게재빈도 설정 규칙 보기 | `view_frequency_caps` |
| 최대 게재빈도 설정 규칙 편집 | `edit_frequency_caps` |
| 메시지 우선순위 보기 | `view_message_prioritization` |
| 메시지 우선순위 편집 | `edit_message_prioritization` |
| 콘텐츠 블록 보기 | `view_content_blocks` |
| 콘텐츠 블록 편집 | `edit_content_blocks` |
| 콘텐츠 블록 보관 | `archive_content_blocks` |
| 기능 플래그 보기 | `view_feature_flags` |
| 기능 플래그 편집 | `edit_feature_flags` |
| 기능 플래그 보관 | `archive_feature_flags` |
| 세그먼트 보기 | `view_segments` |
| 세그먼트 편집 | `edit_segments` |
| 세그먼트 보관 | `archive_segments` |
| 글로벌 컨트롤 그룹 보기 | `view_global_control_group` |
| 글로벌 컨트롤 그룹 편집 | `edit_global_control_group` |
| IAM 템플릿 보기 | `view_iam_templates` |
| IAM 템플릿 편집 | `edit_iam_templates` |
| IAM 템플릿 보관 | `archive_iam_templates` |
| 이메일 템플릿 보기 | `view_email_templates` |
| 이메일 템플릿 편집 | `edit_email_templates` |
| 이메일 템플릿 보관 | `archive_email_templates` |
| 웹훅 템플릿 보기 | `view_webhook_templates` |
| 웹훅 템플릿 편집 | `edit_webhook_templates` |
| 웹훅 템플릿 보관 | `archive_webhook_templates` |
| 링크 템플릿 보기 | `view_link_templates` |
| 링크 템플릿 편집 | `edit_link_templates` |
| 미디어 라이브러리 자산 보기 | `view_media_library_assets` |
| 위치 보기 | `view_locations` |
| 위치 편집 | `edit_locations` |
| 위치 보관 | `archive_locations` |
| 프로모션 코드 보기 | `view_promotion_codes` |
| 프로모션 코드 편집 | `edit_promotion_codes` |
| 프로모션 코드 내보내기 | `export_promotion_codes` |
| 선호 센터 보기 | `view_preference_centers` |
| 선호 센터 편집 | `edit_preference_centers` |
| 보고서 편집 | `edit_reports` |
| 배치 보기 | `view_placements` |
| 배치 편집 | `edit_placements` |
| 배치 보관 | `archive_placements` |
| 배너 템플릿 보기 | `view_banner_templates` |
| 다국어 설정 보기 | `view_multi_language_settings` |
| 운영자 사용 | `use_operator` |
| 결정 스튜디오 에이전트 보기 | `view_decisioning_studio_agents` |
| 결정 스튜디오 오디언스 보기 |`view_decisioning_studio_audience` |
| 결정 스튜디오 전환 이벤트 보기 | `view_decisioning_studio_conversion_event` |
| 결정 스튜디오 가드레일 보기 | `view_decisioning_studio_guardrails` |
| 캠페인 시작 | `launch_campaigns` |
| 캔버스 시작 | `launch_canvases` |
| 대시보드 사용자 편집 | `edit_dashboard_users` |
| 미디어 라이브러리 자산 편집 | `edit_media_library_assets` |
| 미디어 라이브러리 자산 삭제 | `delete_media_library_assets` |
| 가져오기 사용자 보기 | `view_import_users` |
| 사용자 가져오기	| `import_users` |
| 사용자 데이터 편집 | `edit_user_data` |
| 사용자 병합 기록 보기 | `view_user_merge_records` |
| 중복 사용자 병합 | `merge_duplicate_users` |
| API 키 보기 | `view_api_keys` |
| API 키 편집 | `edit_api_keys` |
| 내부 그룹 보기 | `view_internal_user_groups` |
| 내부 그룹 편집 | `edit_internal_user_groups` |
| 내부 그룹 삭제 | `delete_internal_user_groups` |
| 메시지 활동 로그 보기 | `view_message_activity_log` |
| 이벤트 사용자 로그 보기 | `view_event_user_log` |
| API 식별자 보기 | `view_api_identifiers` |
| API 사용 대시보드 보기 | `view_api_usage_dashboard` |
| API 한도 보기 | `view_api_limits` |
| API 사용 경고 보기 | `view_api_usage_alerts` |
| API 사용 경고 편집 | `edit_api_usage_alerts` |
| SDK 디버거 보기 | `view_sdk_debugger` |
| SDK 디버거 편집 | `edit_sdk_debugger` |
| 콘텐츠 블록 실행 | `launch_content_blocks` |
| 클라우드 데이터 수집 편집 | `edit_cloud_data_ingestion` |
| 앱 설정 보기 | `view_app_settings` |
| 앱 설정 편집 | `edit_app_settings` |
| 푸시 설정 보기 | `view_push_settings` |
| 푸시 설정 편집 | `edit_push_settings` |
| 팀 보기 | `view_teams` |
| 팀 편집 | `edit_teams` |
| 팀 보관 | `archive_teams` |
| 커스텀 속성 보기 | `view_custom_attributes` |
| 커스텀 속성 편집 | `edit_custom_attributes` |
| 커스텀 속성 블록리스트 | `blocklist_custom_attributes` |
| 커스텀 속성 삭제 | `delete_custom_attributes` |
| 사용자 지정 속성 내보내기 | `export_custom_attributes` |
| 커스텀 이벤트 보기	 | `view_custom_events` |
| 커스텀 이벤트 편집 | `edit_custom_events` |
| 커스텀 이벤트 블록리스트 | `blocklist_custom_events` |
| 커스텀 이벤트 삭제 | `delete_custom_events` |
| 사용자 지정 이벤트 내보내기 | `export_custom_events` |
| 커스텀 이벤트 속성 세분화 편집 | `edit_custom_event_property_segmentation` |
| 제품 보기 | `view_products` |
| 제품 편집	 | `edit_products` |
| 차단 목록 제품 | `blocklist_products` |
| 구매 속성 세분화 편집 | `edit_purchase_property_segmentation` |
| 태그 보기 | `view_tags` |
| 태그 편집 | `edit_tags` |
| 태그 삭제 | `delete_tags` |
| 이메일 설정 보기	| `view_email_settings` |
| 이메일 설정 편집 | `edit_email_settings` |
| 카탈로그 보기 | `view_catalogs` |
| 카탈로그 편집	 | `edit_catalogs` |
| 카탈로그 내보내기 | `export_catalogs` |
| 카탈로그 삭제 | `delete_catalogs` |
| 왓츠앱 설정 보기 | `view_whatsapp_settings` |
| 기술 파트너 편집 | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 팀 권한 문자열 {#team}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| 캠페인 보기 | `view_campaigns` |
| 캠페인 편집 | `edit_campaigns` |
| 캠페인 보관 | `archive_campaigns` |
| 캔버스 보기 | `view_canvases` |
| 캔버스 편집 | `edit_canvases` |
| 캔버스 보관 | `archive_canvases` |
| 최대 게재빈도 설정 규칙 보기 | `view_frequency_caps` |
| 최대 게재빈도 설정 규칙 편집 | `edit_frequency_caps` |
| 메시지 우선순위 보기 | `view_message_prioritization` |
| 메시지 우선순위 편집 | `edit_message_prioritization` |
| 콘텐츠 블록 보기 | `view_content_blocks` |
| 기능 플래그 보기 | `view_feature_flags` |
| 기능 플래그 편집 | `edit_feature_flags` |
| 기능 플래그 보관 | `archive_feature_flags` |
| 세그먼트 보기 | `view_segments` |
| 세그먼트 편집 | `edit_segments` |
| 글로벌 컨트롤 그룹 편집 | `edit_global_control_group` |
| IAM 템플릿 보기 | `view_iam_templates` |
| IAM 템플릿 편집 | `edit_iam_templates` |
| IAM 템플릿 보관 | `archive_iam_templates` |
| 이메일 템플릿 보기 | `view_email_templates` |
| 이메일 템플릿 편집 | `edit_email_templates` |
| 이메일 템플릿 보관 | `archive_email_templates` |
| 웹훅 템플릿 보기 | `view_webhook_templates` |
| 웹훅 템플릿 편집 | `edit_webhook_templates` |
| 웹훅 템플릿 보관 | `archive_webhook_templates` |
| 링크 템플릿 보기 | `view_link_templates` |
| 링크 템플릿 편집 | `edit_link_templates` |
| 미디어 라이브러리 자산 보기 | `view_media_library_assets` |
| 위치 보기 | `view_locations` |
| 위치 편집 | `edit_locations` |
| 위치 보관 | `archive_locations` |
| 프로모션 코드 보기 | `view_promotion_codes` |
| 프로모션 코드 편집 | `edit_promotion_codes` |
| 프로모션 코드 내보내기 | `export_promotion_codes` |
| 선호 센터 보기 | `view_preference_centers` |
| 선호 센터 편집 | `edit_preference_centers` |
| 보고서 보기 | `view_reports` |
| 보고서 생성 | `create_reports` |
| 보고서 편집 | `edit_reports` |
| 배너 템플릿 보기 | `view_banner_templates` |
| 다국어 설정 보기 | `view_multi_language_settings` |
| 운영자 사용 | `use_operator` |
| 결정 스튜디오 에이전트 보기 | `view_decisioning_studio_agents` |
| 결정 스튜디오 전환 이벤트 보기 | `view_decisioning_studio_conversion_event` |
| 캠페인 시작 | `launch_campaigns` |
| 캔버스 시작 | `launch_canvases` |
| 대시보드 사용자 편집 | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 부서 문자열

| UI에 표시된 대로 | SCIM API 문자열 |
| --- | --- |
| 대행사/타사 | `agency` |
| BI/분석 | `bi` |
| 임원급 관리자 | `c_suite` |
| 엔지니어링 | `engineering` |
| 재무 | `finance` |
| 마케팅/편집 | `marketing` |
| 제품 관리 | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }