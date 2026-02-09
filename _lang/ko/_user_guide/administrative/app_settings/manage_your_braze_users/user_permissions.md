---
nav_title: 권한
article_title: Braze 권한
page_order: 2
page_type: reference
description: "이 참조 문서는 Braze에서 사용자 권한이 작동하는 방식을 다룹니다. 여기에서 편집하고 사용자 권한을 설정하는 방법을 배우고, 대시보드에서 누가 앱에 접근할 수 있는지 선택할 수 있습니다."
tool: Dashboard

---

# Braze 권한

> 사용자 권한을 편집하고, 사용자 권한을 내보내는 방법을 배우고, 권한 세트를 생성하고, 역할을 생성하여 사용자가 가장 필요로 하는 워크스페이스와와 기능에만 액세스할 수 있도록 할 수 있습니다.

## 권한 세트 생성

권한 세트를 사용하여 특정 주제 영역 또는 작업과 관련된 권한을 번들로 묶습니다. 그들은 다른 워크스페이스에서 동일한 액세스가 필요한 대시보드 사용자에게 적용될 수 있습니다. 권한 세트를 만들려면 **설정** > **권한 설정**으로 이동한 다음 **권한 세트 만들기**을 선택합니다. 각 권한에 대한 설명은 [권한 목록](#list-of-permissions)을 참조하십시오.

{% tabs local %}
{% tab example permission sets %}
|이름|권한|
\|-----------|----------------|
|개발자|“개발자 콘솔에 액세스”|
|마케터|“캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경 설정 센터에 액세스” <br> 미디어 라이브러리 자산 관리
|사용자 관리|“대시보드 사용자 관리” <br> "팀 관리"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## 역할 만들기

역할은 개별 커스텀 권한을 워크스페이스 액세스 제어와 함께 묶어 더 많은 구조를 허용합니다. 이는 하나의 대시보드에 여러 브랜드나 로컬 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 올바른 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 각 권한에 대한 설명은 [권한 목록](#list-of-permissions)을 참조하십시오.

{% tabs local %}
{% tab example roles %}
| 역할 이름 | 작업 공간 | 권한  
----------- | ----------- | ---------
| 마케터 - 패션 브랜드 | {::nomarkdown}[DEV] 패션 브랜드, [QA] 패션 브랜드, [PROD] 패션 브랜드 {:/} | "캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경 설정 센터에 액세스"<br>미디어 라이브러리 자산 관리
| 마케터 - 스킨케어 브랜드 | {::nomarkdown}[DEV] 스킨케어 브랜드, [QA] 스킨케어 브랜드, [PROD] 스킨케어 브랜드 {:/} | "캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리 및 선호도 센터에 액세스" <br>미디어 라이브러리 자산 관리
| 사용자 관리 - 모든 브랜드 | {::nomarkdown}[개발] 패션 브랜드, [품질] 패션 브랜드, [홍보] 패션 브랜드, [개발] 스킨케어 브랜드, [품질] 스킨케어 브랜드, [홍보] 스킨케어 브랜드 {:/} | "대시보드 사용자 관리"<br>"팀 관리" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## How do permission sets and roles differ from Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Teams에 사용자 권한을 추가할 때 고려할 사항

특히 워크스페이스에서 사용자를 추가 또는 제거하거나 팀에 추가할 때, Braze 대시보드에 권한을 저장하려고 할 때 어려움을 겪을 수 있습니다. 사용자에 대한 권한이 워크스페이스 수준에서 이미 가지고 있는 권한과 동일한 경우 사용자 **저장/업데이트** 버튼이 회색으로 표시될 수 있습니다. 이 제한은 모든 사용자가 전체 작업 영역과 동일한 권한을 가지고 있는 경우 Teams를 사용하는 이점이 없기 때문에 존재합니다.

동일한 권한을 유지하면서 사용자를 Teams에 성공적으로 추가하려면 작업 영역 수준에서 권한을 할당하지 마세요. 대신 팀 수준에서만 권한을 할당하세요.

## 제한된 사용자

제한된 사용자는 회사 관리자 및 워크스페이스 관리자에 비해 제한이 있지만, 특정 권한을 통해 Braze 대시보드의 특정 측면을 관리할 수 있습니다.

| 권한 > 권한 > 제한된 사용자는 '대시보드 사용자 관리' 권한이 체크되어 있는 경우 다른 제한된 사용자의 권한을 편집할 수 있습니다. 또한 제한된 사용자를 새로 만들고 권한 집합을 수정할 수도 있습니다. 그러나 회사 관리자 계정을 만들거나 관리할 수는 없습니다. |
| 역할 제한 | 제한된 사용자에게 '앱 그룹 관리자'를 제외한 모든 권한이 있는 경우에도 일반적으로 워크스페이스 관리자에게 부여되는 다른 모든 권한에 액세스할 수 있습니다. |
| 권한 가시성 | 제한된 사용자가 한 앱 그룹(예: 개발)에 대해서는 '대시보드 사용자 관리'를 선택했지만 다른 앱 그룹(예: 프로덕션)에 대해서는 선택하지 않은 경우 '사용자 관리' 프로필에 프로덕션 앱 그룹 권한이 표시되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 사용자 비교

| 제한된 사용자 유형 | 설명 |
| --- | --- |
| 앱 그룹 관리자 | 앱 그룹 관리자는 앱 그룹 관리와 관련된 권한을 갖지만 회사 관리자와 동일한 권한은 갖지 않습니다. 제한된 사용자는 필요한 권한을 체크한 경우 앱 그룹 관리자와 유사한 권한을 상속받을 수 있습니다. |
| 회사 관리자 | 회사 관리자는 대시보드 사용자를 삭제할 수 있는 기능을 포함하여 더 광범위한 권한을 가집니다. 그러나 자신의 계정을 삭제할 수는 없으며 해당 작업은 다른 회사 관리자에게 문의해야 합니다. |
| 기본 읽기 전용 권한 | 기술 파트너 페이지와 같은 대시보드의 특정 부분에 액세스하려면 사용자에게 기본 읽기 전용 권한이 있어야 합니다. 여기에는 캠페인, 캔버스, 카드, 세그먼트 및 미디어 라이브러리에 대한 액세스 권한과 함께 '외부 통합 관리'를 인에이블하는 것이 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 액세스 오류

사용자에게 '제한된 액세스'와 같은 메시징이 표시될 수 있습니다. 이 페이지에 액세스할 수 있는 권한이 없습니다." 이러한 경우 계정 관리자는 사용자의 권한을 비활성화했다가 다시 인에이블하여 문제를 해결할 수 있는지 확인해야 합니다.

{% alert note %}
대시보드 사용자 간에 사용자 권한을 병합하거나 다른 대시보드 사용자로 가져오기는 불가능합니다.
{% endalert %}

## 사용자 권한 편집

사용자의 현재 관리자, 회사 또는 워크스페이스 권한을 편집하려면 **설정** > **회사 사용자로** 이동한 다음 이름을 선택합니다.

![결과에 한 명의 사용자가 나열된 Braze의 '회사 사용자' 페이지입니다.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### 관리자

관리자는 모든 기능에 접근할 수 있으며 회사의 모든 설정을 수정할 수 있는 권한이 있습니다. They can:

- [승인 설정 ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)변경
- 추가, 편집, 삭제, 일시 중지 또는 다른 [Braze 사용자]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)의 일시 중지 해제
- Braze 사용자를 CSV로 내보내기

관리자 권한을 부여하거나 제거하려면 **이 사용자는 관리자입니다**을 선택한 다음 **사용자 업데이트**를 선택하십시오.

![관리자 확인란에 초점이 맞춰진 선택된 사용자의 세부 정보입니다.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
사용자에게서 관리자 권한을 제거하면, 최소한 하나의 [회사 수준](#company) 또는 [워크스페이스 수준](#workspace) 권한을 부여할 때까지 Braze에 접근할 수 없습니다.
{% endalert %}

{% endtab %}
{% tab Company %}

### 회사

사용자에 대한 다음 회사 수준 권한을 관리하려면 해당 권한 옆의 상자를 선택하거나 선택 해제하십시오. 완료되면 **사용자 업데이트**를 선택하세요.

|권한 이름|설명|
|----------|-----------|
|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스 생성 및 삭제|사용자가 작업 공간을 생성하고 삭제할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### 워크스페이스

Braze에서 사용자가 속한 각 워크스페이스에 대해 다른 권한을 부여할 수 있습니다. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually to select or assign a permission set [you previously created](#creating-a-permission-set).

사용자에게 다른 워크스페이스에 대해 다른 권한을 부여해야 하는 경우, 필요한 만큼 이 과정을 반복하세요. 각 권한에 대한 설명은 [권한 목록](#list-of-permissions)을 참조하십시오.

{% subtabs %}
{% subtab Select manually %}

**작업 공간**에서 드롭다운에서 하나 이상의 작업 공간을 선택합니다. Then, under **Permissions**, choose one or more permissions from the dropdown. Braze는 사용자가 선택한 워크스페이스에 대해서만 이러한 권한을 할당합니다. 선택적으로 **관리자 액세스 활성화**를 선택하여 이 워크스페이스에 대한 전체 권한을 부여할 수 있습니다.

완료되면 **사용자 업데이트**를 선택하세요.

![Braze에서 수동으로 선택한 워크스페이스 수준 권한.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

**작업 공간**에서 드롭다운에서 하나 이상의 작업 공간을 선택합니다. 그런 다음, **권한 세트**에서 하나의 권한 세트를 선택합니다. Braze는 사용자가 선택한 워크스페이스에 대해서만 이러한 권한을 할당합니다.

완료되면 **사용자 업데이트**를 선택하세요.

![Braze에서 설정된 권한을 통해 워크스페이스 수준 권한이 할당됩니다.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 사용자 권한 내보내기

To download a list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. CSV 파일이 곧 이메일 주소로 전송될 예정입니다.

!['사용자 내보내기' 옵션이 초점이 맞춰진 Braze의 '회사 사용자' 페이지입니다.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## 권한 목록

{% alert important %}
2024년 4월부터 프로모션 코드 목록을 생성하거나 업데이트하려면 Braze 사용자는 “캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리 액세스” 권한이 필요합니다.
{% endalert %}

|레벨|이름|정의|
|---|---|---|
|관리자|관리자|사용자가 모든 사용 가능한 기능에 액세스할 수 있습니다. 이것은 모든 신규 사용자에 대한 기본값 설정입니다. 회사 이름 및 시간대를 포함한 회사 설정을 업데이트할 수 있으며, 제한된 사용자는 이를 수행할 수 없습니다.|
|회사|워크스페이스 생성 및 삭제|사용자가 작업 공간을 생성하고 삭제할 수 있습니다.|
|회사|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스|캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터에 액세스|Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of segments, templates and media, create templates, upload media, create or update promotion code lists, view engagement reports, and view global message settings in the dashboard. 그러나 이 권한을 가진 사용자는 기존 라이브 콘텐츠를 일시 중지하거나 편집할 수 없습니다.|
|워크스페이스|개발자 콘솔 액세스|다음 설정 및 로그에 대한 전체 액세스를 허용합니다:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API 키</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>내부 그룹</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>메시지 활동 로그</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>이벤트 사용자 로그</a></li></ul>{:/}|
|워크스페이스|캠페인 승인 및 거부|사용자가 캠페인을 승인하거나 거부할 수 있습니다. 캠페인에 대한 [승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)가 이 권한에 적용되도록 활성화되어야 합니다. 이 설정은 현재 초기 액세스 중입니다. 관심이 있으시면 조기 액세스에 참여하려면 계정 매니저에게 연락하세요.|
|워크스페이스|캔버스 승인 및 거부|사용자가 캔버스를 승인하거나 거부할 수 있습니다. The [approval workflow for Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply.|
|워크스페이스|커런츠 통합 편집|사용자가 자격 증명을 포함하여 커런츠 연결을 수정할 수 있습니다. 기본값으로, "외부 통합" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|세그먼트 편집|사용자가 세그먼트를 생성하고 편집할 수 있습니다. 이 권한 없이도 기존 세그먼트 및 필터로 캠페인을 계속 생성할 수 있습니다. CSV에 있는 사용자로부터 세그먼트를 생성하거나 CSV에 있는 사용자 그룹을 리타겟하기 위해 이 권한이 필요합니다.|
|워크스페이스|사용자 데이터 내보내기|사용자가 세그먼트, 캠페인 및 캔버스에서 사용자 데이터를 내보낼 수 있습니다. This permission includes sensitive user information like names, email addresses, and other collected personally identifiable information (PII). 대시보드에서 CSV를 내보내려면 이 권한과 'PII 보기' 권한이 있어야 합니다.|
|워크스페이스|사용자 데이터 가져오기 및 업데이트|사용자가 CSV를 가져오고 앱 사용자 파일을 업데이트하며 사용자 가져오기 페이지를 볼 수 있습니다. 이것은 또한 사용자의 구독 상태와 구독 그룹 옵트인/옵트아웃 규칙을 편집할 수 있게 해줍니다.|
|워크스페이스|콘텐츠 블록 실행 및 관리|사용자가 [콘텐츠 블록을]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) 시작하고 관리할 수 있습니다.|
|워크스페이스|환경설정 센터 관리|사용자가 [선호 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)를 시작할 수 있습니다.|
|워크스페이스|앱 관리|사용자가 **앱 설정**을 편집할 수 있습니다.|
|워크스페이스|카탈로그 대시보드 권한 관리|사용자가 카탈로그를 생성하고 관리할 수 있습니다.|
|워크스페이스|대시보드 사용자 관리| Allows non-admins the ability to view, edit, and manage the **Company Users** page, and manage the dashboard users in their workspace by modifying the permissions of any user, including themselves. Users with this permission can’t delete users (only administrators can delete users).<br><br>이는 레거시 권한 `MANAGE_DEVELOPERS_AND_PERMISSIONS` 에 해당합니다.|
|워크스페이스|이메일 설정 관리|사용자가 이메일 구성 변경 사항을 저장할 수 있습니다 (**설정** > **이메일 환경설정**).|
|워크스페이스|이벤트, 속성, 구매 관리|사용자가 커스텀 속성을 편집할 수 있도록 허용합니다(이 기능이 없는 사용자는 여전히 커스텀 속성을 볼 수 있음). 커스텀 이벤트의 속성을 편집 및 보기, **데이터 설정**에서 제품의 속성을 편집 및 보기.|
|워크스페이스|외부 통합 관리|Allows access to all tabs under **Technology Partners**, ability to sync Braze with other platforms, and access to manage [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|워크스페이스|피처 플래그 관리|사용자가 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags/)를 생성하거나 편집할 수 있습니다.|
|워크스페이스|미디어 라이브러리 자산 관리|사용자가 미디어 라이브러리 자산을 추가, 편집 및 삭제할 수 있습니다.|
|워크스페이스|구독 그룹 관리|사용자가 구독 그룹을 생성하고 관리할 수 있습니다.|
|워크스페이스|태그 관리|사용자가 태그( **태그 관리** )를 편집하거나 삭제할 수 있습니다. 캠페인이나 세그먼트에 태그를 추가하려면 이 권한이 필요하지 않습니다.|
|워크스페이스|팀 관리|사용자가 **내부 팀**을 관리할 수 있습니다. 이 권한을 선택할 수 있는 능력은 Braze와의 계약에 따라 다릅니다.<br><br>이는 레거시 권한 `MANAGE_TERRITORIES` 에 해당합니다.|
|워크스페이스|변환 관리|사용자가 데이터 변환을 생성하고 관리할 수 있습니다.|
|워크스페이스|캠페인, 캔버스 발송|사용자가 캠페인 및 캔버스를 편집, 보관 및 중지하고 캠페인을 생성하고 캔버스를 시작할 수 있습니다. |
|워크스페이스|청구 상세정보 보기|사용자가 구독 및 청구를 볼 수 있습니다.|
|워크스페이스|커런츠 통합 보기|사용자가 자격 증명을 제외한 Currents 연결에 대한 모든 정보를 볼 수 있도록 합니다. 기본값으로, "캠페인 액세스, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|PII로 분류된 사용자 지정 속성 보기|Allows non-admin users to view custom attributes that contain sensitive information and are marked as personally identifiable information (PII).|
|워크스페이스|PII 보기|Allows users to view personally identifiable information (PII) fields as defined by your company within the dashboard. 사용자는 메시지 미리 보기의 **사용자로 미리 보기** 탭에서 PII 필드를 볼 수도 있습니다.<br><br>You need this permission to use [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), because it allows direct access to some customer data. 대시보드에서 CSV를 내보내려면 사용자에게 이 권한과 '사용자 데이터 내보내기' 권한이 모두 필요합니다.|
|워크스페이스|사용자 프로필 PII 준수사항 보기|Allows users to view user profiles that contain fields your company has defined as personally identifiable information (PII), but redacts the PII fields.<br><br>You need this permission to use the user search tool. |
|워크스페이스|변환 보기|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|워크스페이스|사용 데이터 보기|사용자가 앱 사용량을 볼 수 있도록 하며, 채널 성능 대시보드를 포함합니다.|
|워크스페이스|중복 사용자 병합|사용자가 중복된 사용자 프로필을 병합할 수 있습니다.|
|워크스페이스|중복 사용자 미리보기|사용자가 중복된 사용자 프로필을 미리 볼 수 있습니다.|
|워크스페이스|캔버스 템플릿 생성 및 편집|사용자가 캔버스 템플릿을 만들고 편집할 수 있습니다.|
|워크스페이스|캔버스 템플릿 보기|사용자가 캔버스 템플릿을 볼 수 있습니다.|
|워크스페이스|캔버스 템플릿 아카이브|사용자가 캔버스 템플릿을 보관할 수 있습니다.|
|워크스페이스|Manage Custom Event Property Segmentation|Allows users to create segments based on event property recency and frequency.|
|워크스페이스|Publish Landing Pages|Allows users to publish [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|워크스페이스|Create Landing Page Drafts|Allows users to create and save landing page drafts.|
|워크스페이스|Access Landing Pages|Allows users to access the **Landing Pages** page.|
|워크스페이스|Create and Edit Landing Page Templates|Allows users to create and edit landing page templates.|
|워크스페이스|View Landing Page Templates|Allows users to view landing page templates.|
|워크스페이스|Archive Landing Page Templates|Allows users to archive landing page templates.|
|워크스페이스|커스텀 AI 에이전트 보기|사용자가 [커스텀 AI 상담원을]({{site.baseurl}}/user_guide/brazeai/agents/) 볼 수 있습니다. This feature is currently in beta.|
|워크스페이스|커스텀 AI 에이전트 생성|사용자가 커스텀 AI 상담원을 만들 수 있습니다. This feature is currently in beta.|
|워크스페이스|커스텀 AI 에이전트 편집|사용자가 커스텀 AI 상담원을 편집할 수 있습니다. This feature is currently in beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
