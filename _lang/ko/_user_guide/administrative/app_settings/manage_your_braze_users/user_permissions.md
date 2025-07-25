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
{% tab 권한 세트 예시 %}
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
{% tab 역할 예시 %}
| 역할 이름 | 작업 공간 | 권한  
----------- | ----------- | ---------
| 마케터 - 패션 브랜드 | {::nomarkdown}[DEV] 패션 브랜드, [QA] 패션 브랜드, [PROD] 패션 브랜드 {:/} | “캠페인, 캔버스, 카드, 기능 플래그, 세그먼트, 미디어 라이브러리, 및 선호 센터에 액세스"<br>미디어 라이브러리 자산 관리
| 마케터 - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Access Campaigns, Canvases, Cards, 기능 Flags, Segments, 미디어 라이브러리, and Preference Centers” <br>미디어 라이브러리 자산 관리
| 사용자 관리 - 모든 브랜드 | {::nomarkdown}[DEV] 패션 브랜드, [QA] 패션 브랜드, [PROD] 패션 브랜드, [DEV] 스킨케어 브랜드, [QA] 스킨케어 브랜드, [PROD] 스킨케어 브랜드 {:/} | “대시보드 사용자 관리”<br>"팀 관리" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## 권한 집합과 역할은 팀과 어떻게 다른가요?

{% multi_lang_include permissions.md content="Differences" %}

## 사용자 권한 편집

사용자의 현재 [관리자](#admin), [회사](#company) 또는 [작업 공간](#workspace) 권한을 편집하려면 **설정** > **회사 사용자**로 이동한 다음 이름을 선택합니다.

![Braze의 "회사 사용자" 페이지에 결과에 한 명의 사용자가 나열되어 있습니다.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

### 관리자

관리자는 모든 기능에 접근할 수 있으며 회사의 모든 설정을 수정할 수 있는 권한이 있습니다. Braze에서 관리자만 할 수 있는 몇 가지 작업도 있습니다. 

관리자만 할 수 있습니다.

- [승인 설정 ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)변경
- 추가, 편집, 삭제, 일시 중지 또는 다른 [Braze 사용자]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)의 일시 중지 해제
- Braze 사용자를 CSV로 내보내기

관리자 권한을 부여하거나 제거하려면 **이 사용자는 관리자입니다**을 선택한 다음 **사용자 업데이트**를 선택하십시오.

![선택된 사용자의 세부 정보는 관리자 확인란에 초점이 맞춰져 있습니다.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
사용자에게서 관리자 권한을 제거하면, 최소한 하나의 [회사 수준](#company) 또는 [워크스페이스 수준](#workspace) 권한을 부여할 때까지 Braze에 접근할 수 없습니다.
{% endalert %}

### 회사

사용자에 대한 다음 회사 수준 권한을 관리하려면 해당 권한 옆의 상자를 선택하거나 선택 해제하십시오. 완료되면 **사용자 업데이트**를 선택하세요.

|권한 이름|설명|
|----------|-----------|
|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스 생성 및 삭제|사용자가 작업 공간을 생성하고 삭제할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 워크스페이스

Braze에서 사용자가 속한 각 워크스페이스에 대해 다른 권한을 부여할 수 있습니다. 워크스페이스 수준의 권한을 관리하려면 **워크스페이스 및 권한 선택**을 선택한 다음 권한을 수동으로 선택하거나 [이전에 생성한](#creating-a-permission-set) 권한 세트를 할당하세요.

사용자에게 다른 워크스페이스에 대해 다른 권한을 부여해야 하는 경우, 필요한 만큼 이 과정을 반복하세요. 각 권한에 대한 설명은 [권한 목록](#list-of-permissions)을 참조하십시오.

{% tabs local %}
{% tab 수동으로 선택 %}
**작업 공간**에서 드롭다운에서 하나 이상의 작업 공간을 선택합니다. 그런 다음, **권한**에서 드롭다운에서 하나 이상의 권한을 선택합니다. 그들은 선택한 워크스페이스에 대해서만 이러한 권한이 부여됩니다. 선택적으로 **관리자 액세스 활성화**를 선택하여 이 워크스페이스에 대한 전체 권한을 부여할 수 있습니다.

완료되면 **사용자 업데이트**를 선택하세요.

![워크스페이스 수준 권한이 Braze에서 수동으로 선택되고 있습니다.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})
{% endtab %}

{% tab 권한 세트 할당 %}
**작업 공간**에서 드롭다운에서 하나 이상의 작업 공간을 선택합니다. 그런 다음, **권한 세트**에서 하나의 권한 세트를 선택합니다. 그들은 선택한 워크스페이스에 대해서만 이러한 권한이 부여됩니다.

완료되면 **사용자 업데이트**를 선택하세요.

![워크스페이스 수준의 권한이 Braze의 권한 세트를 통해 할당됩니다.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})
{% endtab %}
{% endtabs %}

## 사용자 권한 내보내기

목록을 다운로드하려면 **설정** > **회사 사용자**로 이동한 다음 **사용자 내보내기**를 선택하세요. CSV 파일이 곧 이메일 주소로 전송될 예정입니다.

![Braze의 "회사 사용자" 페이지에서 "사용자 내보내기" 옵션이 선택된 상태입니다.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## 권한 목록

{% alert important %}
2024년 4월부터 프로모션 코드 목록을 생성하거나 업데이트하려면 Braze 사용자는 “캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리 액세스” 권한이 필요합니다.
{% endalert %}

|레벨|이름|정의|
|---|---|---|
|관리자|관리자|사용자가 모든 사용 가능한 기능에 액세스할 수 있습니다. 이것은 모든 신규 사용자에 대한 기본값 설정입니다. 회사 이름 및 시간대를 포함한 회사 설정을 업데이트할 수 있으며, 제한된 사용자는 이를 수행할 수 없습니다.|
|회사|워크스페이스 생성 및 삭제|사용자가 작업 공간을 생성하고 삭제할 수 있습니다.|
|회사|회사 설정 관리|사용자가 회사 설정을 수정할 수 있습니다.|
|워크스페이스|캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터에 액세스|사용자는 대시보드에서 캠페인 및 캔버스 성과 지표를 보고, 캠페인 및 캔버스 초안을 만들고 복제하고, 캠페인 및 캔버스 초안과 템플릿을 편집하고, 뉴스피드, 세그먼트, 템플릿 및 미디어의 초안을 보고, 템플릿을 만들고, 미디어를 업로드하고, 프로모션 코드 목록을 만들거나 업데이트하고, 참여 보고서를 보고, 글로벌 메시지 설정을 볼 수 있습니다. 그러나 이 권한을 가진 사용자는 기존 라이브 콘텐츠를 일시 중지하거나 편집할 수 없습니다.|
|워크스페이스|개발자 콘솔 액세스|다음 설정 및 로그에 대한 전체 액세스를 허용합니다:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API 키</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>내부 그룹</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>메시지 활동 로그</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>이벤트 사용자 로그</a></li><li><a href='/docs/user_guide/data_and_analytics/cloud_ingestion/'>클라우드 데이터 수집 관리</a></li></ul>{:/}|
|워크스페이스|캠페인 승인 및 거부|사용자가 캠페인을 승인하거나 거부할 수 있습니다. 캠페인에 대한 [승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)가 이 권한에 적용되도록 활성화되어야 합니다. 이 설정은 현재 초기 액세스 중입니다. 관심이 있으시면 조기 액세스에 참여하려면 계정 매니저에게 연락하세요.|
|워크스페이스|캔버스 승인 및 거부|사용자가 캔버스를 승인하거나 거부할 수 있습니다. 캔버스에 대한 [승인 워크플로]({{site.baseurl}}/canvas_approval)가 이 권한에 적용되도록 설정되어야 합니다.|
|워크스페이스|커런츠 통합 편집|사용자가 자격 증명을 포함하여 커런츠 연결을 수정할 수 있습니다. 기본값으로, "외부 통합" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|세그먼트 편집|사용자가 세그먼트를 생성하고 편집할 수 있습니다. 이 권한 없이도 기존 세그먼트 및 필터로 캠페인을 계속 생성할 수 있습니다. CSV에 있는 사용자로부터 세그먼트를 생성하거나 CSV에 있는 사용자 그룹을 리타겟하기 위해 이 권한이 필요합니다.|
|워크스페이스|사용자 데이터 내보내기|사용자가 세그먼트, 캠페인 및 캔버스에서 사용자 데이터를 내보낼 수 있습니다. This permission includes sensitive user information like names, email addresses, and other collected personally identifiable information (PII). |
|워크스페이스|사용자 데이터 가져오기 및 업데이트|사용자가 CSV를 가져오고 앱 사용자 파일을 업데이트하며 사용자 가져오기 페이지를 볼 수 있습니다. 이것은 또한 사용자의 구독 상태와 구독 그룹 옵트인/옵트아웃 규칙을 편집할 수 있게 해줍니다.|
|워크스페이스|콘텐츠 블록 실행|사용자가 [콘텐츠 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/)을 시작할 수 있습니다.|
|워크스페이스|환경설정 센터 관리|사용자가 [선호 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)를 시작할 수 있습니다.|
|워크스페이스|앱 관리|사용자가 **앱 설정**을 편집할 수 있습니다.|
|워크스페이스|카탈로그 대시보드 권한 관리|사용자가 카탈로그를 생성하고 관리할 수 있습니다.|
|워크스페이스|대시보드 사용자 관리| Allows non-admins the ability to view, edit, and manage the **Company Users** page, and manage the dashboard users in their workspace by modifying the permissions of any user, including themselves. Users with this permission can’t delete users (only administrators can delete users).|
|워크스페이스|이메일 설정 관리|사용자가 이메일 구성 변경 사항을 저장할 수 있습니다 (**설정** > **이메일 환경설정**).|
|워크스페이스|이벤트, 속성, 구매 관리|사용자가 커스텀 속성을 편집할 수 있도록 허용합니다(이 기능이 없는 사용자는 여전히 커스텀 속성을 볼 수 있음). 커스텀 이벤트의 속성을 편집 및 보기, **데이터 설정**에서 제품의 속성을 편집 및 보기.|
|워크스페이스|외부 통합 관리|**기술 파트너** 아래의 모든 탭에 접근할 수 있으며 Braze를 다른 플랫폼과 동기화할 수 있는 기능을 제공합니다.|
|워크스페이스|피처 플래그 관리|사용자가 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags/)를 생성하거나 편집할 수 있습니다.|
|워크스페이스|미디어 라이브러리 자산 관리|사용자가 미디어 라이브러리 자산을 추가, 편집 및 삭제할 수 있습니다.|
|워크스페이스|구독 그룹 관리|사용자가 구독 그룹을 생성하고 관리할 수 있습니다.|
|워크스페이스|태그 관리|사용자가 태그( **태그 관리** )를 편집하거나 삭제할 수 있습니다. 캠페인이나 세그먼트에 태그를 추가하려면 이 권한이 필요하지 않습니다.|
|워크스페이스|팀 관리|사용자가 **내부 팀**을 관리할 수 있습니다. 이 권한을 선택할 수 있는 능력은 Braze와의 계약에 따라 다릅니다.|
|워크스페이스|변환 관리|사용자가 데이터 변환을 생성하고 관리할 수 있습니다.|
|워크스페이스|카드 게시|이 권한은 뉴스피드가 사용 중지되는 경우에만 계정이 활성화된 경우에만 표시됩니다. 이것은 콘텐츠 카드에 영향을 미치지 않습니다. 사용자가 뉴스피드 카드를 만들고 편집할 수 있습니다. 이 권한 없이도 뉴스피드 카드를 여전히 볼 수 있습니다. 계정이 뉴스피드에 대해 활성화되어 있고 사용자가 기존 콘텐츠 블록을 실행할 수 있어야 하는 경우, "카드 게시" 및 "콘텐츠 블록 실행" 권한이 모두 필요합니다.|
|워크스페이스|캠페인, 캔버스 발송|사용자가 캠페인 및 캔버스를 편집, 보관 및 중지하고 캠페인을 생성하고 캔버스를 시작할 수 있습니다. |
|워크스페이스|청구 상세정보 보기|사용자가 구독 및 청구를 볼 수 있습니다.|
|워크스페이스|커런츠 통합 보기|사용자가 자격 증명을 제외한 Currents 연결에 대한 모든 정보를 볼 수 있도록 합니다. 기본값으로, "캠페인 액세스, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리, 위치, 프로모션 코드 및 환경 설정 센터" 권한이 할당된 사용자에게도 이 권한이 할당됩니다.|
|워크스페이스|PII로 분류된 사용자 지정 속성 보기|Allows non-admin users to view custom attributes that contain sensitive information and are marked as personally identifiable information (PII).|
|워크스페이스|PII 보기|Allows users to view personally identifiable information (PII) fields as defined by your company within the dashboard. 사용자는 메시지 미리 보기의 **사용자로 미리 보기** 탭에서 PII 필드를 볼 수도 있습니다.|
|워크스페이스|사용자 프로필 PII 준수사항 보기|Allows users to view user profiles that contain fields your company has defined as personally identifiable information (PII), but redacts the PII fields. |
|워크스페이스|변환 보기|Allows users to view [Braze Data Transformations]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|워크스페이스|사용 데이터 보기|사용자가 앱 사용량을 볼 수 있도록 하며, 채널 성능 대시보드를 포함합니다.|
|워크스페이스|중복 사용자 병합|사용자가 중복된 사용자 프로필을 병합할 수 있습니다.|
|워크스페이스|중복 사용자 미리보기|사용자가 중복된 사용자 프로필을 미리 볼 수 있습니다.|
|워크스페이스|캔버스 템플릿 생성 및 편집|사용자가 캔버스 템플릿을 만들고 편집할 수 있습니다.|
|워크스페이스|캔버스 템플릿 보기|사용자가 캔버스 템플릿을 볼 수 있도록 허용합니다.|
|워크스페이스|캔버스 템플릿 아카이브|사용자가 캔버스 템플릿을 보관할 수 있습니다.|
|워크스페이스|Manage Custom Event Property Segmentation|Allows users to create segments based on event property recency and frequency.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
