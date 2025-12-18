---
nav_title: 사용자 삭제하기
article_title: 사용자 삭제하기
page_order: 4.2
toc_headers: h2
description: "개별 사용자 또는 사용자 세그먼트를 삭제하는 방법을 Braze 대시보드에서 직접 알아보세요." 
---

# 사용자 삭제하기

> 개별 사용자 또는 사용자 세그먼트를 삭제하는 방법을 Braze 대시보드에서 직접 알아보세요.

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 참여에 관심이 있는 경우 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 전제 조건

사용자를 삭제하려면 관리자이거나 **사용자 삭제** 권한이 있어야 합니다.

## 사용자 삭제 정보

사용자 삭제를 사용하면 더 이상 필요하지 않거나, 실수로 생성되었거나, 규정 준수(예: GDPR 또는 CCPA)를 위해 삭제해야 하는 고객 프로필을 제거하여 데이터베이스를 관리할 수 있습니다.

| 고려 사항 | 세부 정보 |
|---------------|---------|
| 최대 크기 | 세그먼트를 삭제할 때 최대 1억 개의 고객 프로필을 삭제할 수 있습니다. |
| 대기 기간 | 모든 세그먼트 삭제에는 7일의 대기 기간과 삭제 처리 시간이 필요합니다. |
| 작업 제한 | 7일의 대기 기간을 포함하여 한 번에 하나의 세그먼트만 삭제할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 사용자 삭제하기

[개별 사용자](#delete-individual) 또는 [사용자 세그먼트를](#delete-segment) 삭제하려면 Braze 대시보드를 통해 삭제할 수 있습니다:

### 개인 삭제하기 {#delete-individual}

Braze에서 개별 사용자를 삭제하려면 **오디언스** > **사용자 검색으로** 이동한 다음 사용자를 검색하여 선택합니다. 중복된 고객 프로필을 삭제하는 경우 올바른 프로필을 선택했는지 확인하세요.

Braze의 '사용자 검색' 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
단일 사용자 삭제는 영구적이며, 프로필은 삭제된 후에는 복구할 수 없습니다.  
{% endalert %}

고객 프로필 페이지에서 <i class="fa-solid fa-ellipsis-vertical"></i> **옵션 표시** > **사용자 삭제를** 선택합니다. Braze에서 사용자가 완전히 삭제되려면 몇 분 정도 걸릴 수 있습니다.

세로줄임표 메뉴가 열려 있고 사용자 삭제 옵션이 표시된 Braze의 사용자.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### 세그먼트 삭제하기 {#delete-segment}

아직 [만들지]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) 않았다면 삭제하려는 고객 프로필이 포함된 [세그먼트를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). 중복된 사용자를 삭제하는 경우 모든 고객 프로필을 포함해야 합니다.

Braze에서 **오디언스** > **오디언스 관리로** 이동한 다음 **사용자 삭제** 탭을 선택합니다.

Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭을 클릭합니다.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**사용자 삭제를** 선택하고 삭제하려는 세그먼트를 선택한 후 **다음을** 선택합니다.

삭제를 위해 선택한 세그먼트가 있는 팝업 창이 나타납니다.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

**삭제를** 입력하여 요청을 확인한 다음 **사용자 삭제를** 선택합니다.

확인 상자에 '삭제'가 입력된 확인 페이지가 표시됩니다.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

이 세그먼트의 사용자는 즉시 삭제되지 않습니다. 대신 향후 7일 동안 삭제 보류 중으로 표시됩니다. 이 시간이 지나면 해당 게시물은 삭제되며 이를 알려드리기 위해 이메일을 보내드립니다.

{% alert tip %}
세그먼트 변경에 관계없이 이러한 정확한 사용자가 삭제되도록 하기 위해 **보류 중인 삭제라는** 세그먼트 필터가 자동으로 생성됩니다. [이 필터를 사용하여]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) 보류 중인 삭제 상태를 확인할 수 있습니다.
{% endalert %}

## 세그먼트 삭제 취소하기 {#cancel}

보류 중인 세그먼트 삭제는 7일 이내에 취소할 수 있습니다. 취소하려면 **오디언스** > **오디언스 관리로** 이동한 다음 **사용자 삭제** 탭을 선택합니다.

Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭을 클릭합니다.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

보류 중인 세그먼트 삭제 옆의 <i class="fa-solid fa-eye"></i> 을 선택하여 삭제 레코드 세부 정보를 엽니다.

'사용자 삭제' 탭에서 보류 중인 세그먼트 삭제.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

삭제 기록 세부 정보에서 **삭제 취소를** 선택합니다.

'사용자 삭제' 탭의 '삭제 기록 상세정보' 창이 열립니다.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
사용자 일괄 삭제가 진행 중인 경우 언제든지 취소할 수 있습니다. 그러나 취소 전에 이미 삭제한 사용자는 복원할 수 없습니다.
{% endalert %}

## 삭제 상태 확인 {#status}

[세그먼트 필터](#segment-filters), [오디언스 관리](#manage-audience) 페이지 또는 [보안 이벤트 보고서를](#security-event-report) 사용하여 삭제 상태를 확인할 수 있습니다.

### 세그먼트 필터

사용자 세그먼트 삭제를 요청하면 **보류 중인 삭제라는** [세그먼트 필터가]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) 자동으로 생성됩니다. 다음과 같은 용도로 사용할 수 있습니다:

- 특정 삭제 실행 날짜에 연결된 정확한 사용자 집합을 확인하세요.
- 해당 사용자를 캠페인에서 제외하여 삭제하기 전에 메시지를 받지 않도록 하세요.
- 규정 준수 또는 기록 보관을 위해 필요한 경우 목록을 내보내세요.

### 오디언스 관리

{% alert note %}
삭제될 정확한 사용자 목록을 얻으려면 삭제 [대기 중 세그먼트 필터를](#segment-filters) 대신 사용하세요.
{% endalert %}

**오디언스** > **오디언스 관리로** 이동한 다음 **사용자 삭제** 탭을 선택합니다.

Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭을 클릭합니다.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

이 페이지에서는 현재 진행 중이거나 보류 중인 모든 삭제에 대한 다음과 같은 일반 정보를 확인할 수 있습니다:

| 필드 | 설명 |
|-------|-------------|
| 요청 날짜 | 요청이 처음 이루어진 날짜입니다. 삭제 **대기** 중 필터와 함께 사용하면 삭제 대기 중인 프로필 목록을 확인할 수 있습니다. |
| 요청자 | 삭제 요청을 시작한 사용자입니다. |
| 세그먼트 이름 | 삭제 보류 중인 사용자를 선택하는 데 사용되는 세그먼트의 이름입니다. |
| 상태 | 삭제 요청이 보류 중인지, 진행 중인지, 완료되었는지 여부를 표시합니다. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

특정 요청에 대한 자세한 내용을 보려면 <i class="fa-solid fa-eye"></i> 을 선택하면 삭제 기록 세부 정보가 표시됩니다. 여기에서 [보류 중인 세그먼트 삭제를 취소할](#cancel) 수도 있습니다.

'사용자 삭제' 탭에서 보류 중인 세그먼트 삭제.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### 보안 이벤트 보고서

보안 이벤트 보고서를 다운로드하여 이전 삭제 상태를 확인할 수도 있습니다. 자세한 내용은 [보안 설정을]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report) 참조하세요.

## 자주 묻는 질문 {#faq}

### 사용자가 1억 명이 넘는 세그먼트를 삭제할 수 있나요?

아니요. 사용자가 1억 명을 초과하는 세그먼트는 삭제할 수 없습니다. 이 크기의 세그먼트를 삭제하는 데 도움이 필요하면 [지원팀](mailto:support@braze.com)( [braze.com )으로 문의하세요.](mailto:support@braze.com)

### 사용자 병합 자동화가 사용자 삭제에 영향을 주나요?

예약된 병합에 삭제 대기 중인 고객 프로필이 포함되어 있는 경우 Braze는 해당 프로필을 건너뛰고 병합하지 않습니다. 이러한 프로필을 병합하려면 해당 프로필을 삭제에서 제거해야 합니다.

### 삭제 대기 중인 사용자에게 전송된 데이터는 어떻게 되나요?

외부 시스템이나 SDK에서 전송된 데이터는 계속 허용되지만 사용자는 활동 여부와 관계없이 예정대로 삭제됩니다.

### 삭제 대기 중인 사용자에 대해 캔버스와 캠페인이 트리거되나요?

예. 그러나 세그먼트 포함 필터를 추가하여 **보류 중인 삭제** [세그먼트 필터로](#segment-filters) 모든 사용자를 제외할 수 있습니다.

### 삭제된 고객 프로필을 복구할 수 있나요?

개별 사용자 삭제는 영구적으로 이루어집니다.

이후 7일 이내에 [세그먼트 삭제를 취소할](#cancel) 수 있습니다. 그러나 취소하기 전에 이미 삭제한 사용자는 복원할 수 없습니다.
