---
nav_title: "SCIM API 객체 및 부록"
article_title: SCIM API 객체 및 부록
page_order: 8
page_type: reference
description: "이 문서는 다양한 SCIM API 객체와 부록을 설명합니다."
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM API 객체 및 부록

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

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | [회사 권한 문자열](#company) 테이블의 회사 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 해당 권한을 가지고 있음을 나타냅니다. |
| `roles` | 선택 사항 | 배열 | [역할 객체의](#role-object) 배열입니다. |
| `appGroup` | 필수 | 배열 | [작업 공간 권한 객체](#workspace-permission-object)의 배열. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 작업 공간 권한 개체 {#workspace-permission-object}

유효한 앱 그룹 권한 객체는 다음 키-값 페어를 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupName`| 선택 사항 | 문자열 | 작업 공간의 이름. 이 객체에 포함된 권한이 적용될 워크스페이스를 지정하는 데 사용됩니다. | 
| `appGroupId` | `appGroupName`이(가) 없으면 필수 | 문자열 | 워크스페이스의 ID로, 워크스페이스를 지정하는 대체 방법으로 사용됩니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 설정 개체](#workspace-permissions-set-object)이 있는 배열. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열](#workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대한 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [팀 권한 객체](#team-permissions-object) 배열. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 작업 공간 권한 설정 객체 {#workspace-permissions-set-object}

유효한 워크스페이스 권한 설정 객체는 다음 키-값 페어를 가진 JSON 객체입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 선택 사항 | 문자열 | 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이(가) 없으면 필수 | 문자열 | 워크스페이스의 ID로, 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 팀 권한 객체

유효한 팀 권한 객체는 다음 키-값 쌍을 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `teamName` | 선택 사항 | 문자열 | 팀의 이름, 이 개체 내의 권한이 어떤 팀을 위한 것인지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이(가) 없으면 필수 | 문자열 | 팀의 ID, 팀을 지정하는 대체 방법으로 사용됩니다. |
| `teamPermissions` | 필수 | 배열 | [teams permission strings](#team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대한 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 역할 개체

유효한 역할 객체는 다음과 같은 키 값 쌍을 가진 JSON 객체입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `roleName` | 선택 사항 | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이(가) 없으면 필수 | 문자열 | 역할을 지정하는 대체 방법으로 사용되는 역할의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 부록

### 회사 권한 문자열 {#company}

| UI에 표시된 대로 | SCIM API 문자열 |
| --- | --- |
| 관리자 | `admin` |
| 회사 설정 관리 가능 | `manage_company_settings` |
| 워크스페이스 추가/제거 가능| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 작업 공간 권한 문자열 {#workspace-strings}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| 관리자 | `admin` |
| 캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리에 액세스 | `basic_access` |
| 캔버스 승인 및 거부 | `approve_deny_campaigns` |
| 캠페인, 캔버스 발송 | `send_campaigns_canvases` |
| 카드 게시 | `publish_cards` |
| 세그먼트 편집 | `edit_segments` |
| 사용자 데이터 내보내기 | `export_user_data` |
| PII 보기 | `view_pii` |
| 사용자 프로필 PII 준수사항 보기 | `view_user_profile` |
| 대시보드 사용자 관리 | `manage_dashboard_users` |
| 미디어 라이브러리 자산 관리 | `manage_media_library` |
| 사용 데이터 보기 | `view_usage_data` |
| 사용자 데이터를 가져오고 업데이트합니다 | `import_update_user_data` |
| 청구 상세정보 보기 | `view_billing_details` |
| 개발자 콘솔 액세스 | `dev_console` |
| 콘텐츠 블록 실행 | `launch_content_blocks` |
| 외부 통합 관리 | `manage_external_integrations` |
| 앱 관리 | `manage_apps` |
| 팀 관리 | `manage_teams` |
| 이벤트, 속성, 구매 관리 | `manage_events_attributes_purchases` |
| 태그 관리 | `manage_tags` |
| 이메일 설정 관리 | `manage_email_settings` |
| 구독 그룹 관리 | `manage_subscription_groups` |
| 승인 설정 관리 | `manage_approval_settings` |
| 카탈로그 대시보드 권한 관리 | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 팀 권한 문자열 {#team}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| 관리자 | `admin` |
| 캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리에 액세스 | `basic_access` |
| 캔버스 승인 및 거부 | `approve_deny_campaigns` |
| 캠페인, 캔버스 발송 | `send_campaigns_canvases` |
| 카드 게시 | `publish_cards` |
| 세그먼트 편집 | `edit_segments` |
| 사용자 데이터 내보내기 | `export_user_data` |
| 사용자 프로필 보기 | `view_user_profile` |
| 대시보드 사용자 관리 | `manage_dashboard_users` |
| 미디어 라이브러리 자산 관리 | `manage_media_library` |
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
