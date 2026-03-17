---
nav_title: 사용자 삭제
article_title: 사용자 삭제
page_order: 4.2
toc_headers: h2
description: "Braze 대시보드를 통해 개별 사용자 또는 사용자 세그먼트를 직접 삭제하는 방법을 배우십시오."
alias: /delete_users/
hidden: true
---

# 사용자 삭제

> Braze 대시보드를 통해 개별 사용자 또는 사용자 세그먼트를 직접 삭제하는 방법을 배우십시오.

{% alert important %}
이 기능에 대한 조기 액세스는 일시적으로 종료되었습니다. 자세한 내용은 고객 성공 매니저에게 문의하십시오.
{% endalert %}

## 필수 조건

사용자를 삭제하려면 관리자가 되어야 합니다.

## 사용자 삭제에 대하여

사용자 삭제를 통해 더 이상 필요하지 않거나 오류로 생성된 프로필, 또는 규정 준수를 위해 삭제해야 하는 프로필(GDPR 또는 CCPA와 같은)을 제거하여 데이터베이스를 관리할 수 있습니다.

| Consideration | 세부 정보 |
|---------------|---------|
| 최대 크기 | 세그먼트를 삭제할 때 최대 1억 개의 사용자 프로필을 삭제할 수 있습니다. |
| 대기 기간 | 모든 세그먼트 삭제에는 7일의 대기 기간과 삭제 처리에 필요한 시간이 필요합니다. |
| 작업 제한 | 한 번에 하나의 세그먼트만 삭제할 수 있으며, 여기에는 7일의 대기 기간이 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 사용자 삭제

Braze 대시보드를 통해 [개별 사용자](#delete-individual) 또는 [사용자 세그먼트](#delete-segment)를 삭제할 수 있습니다:

### 개별 {#delete-individual} 삭제

Braze에서 개별 사용자를 삭제하려면 **오디언스** > **사용자 검색**로 이동한 다음 사용자를 검색하고 선택하십시오. 중복 사용자 프로필을 삭제하는 경우 올바른 프로필을 선택했는지 확인하십시오.

![Braze의 '사용자 검색' 페이지입니다.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
단일 사용자 삭제는 영구적입니다—삭제된 프로필은 복구할 수 없습니다.  
{% endalert %}

프로필 페이지에서 <i class="fa-solid fa-ellipsis-vertical"></i> **옵션 표시** > **사용자 삭제**를 선택하십시오. 사용자가 Braze에서 완전히 삭제되는 데 몇 분이 걸릴 수 있다는 점을 염두에 두세요.

![사용자가 Braze에서 수직 점 3개 메뉴를 열고 사용자 삭제 옵션을 보여줍니다.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### 세그먼트 삭제 {#delete-segment}

아직 하지 않았다면, [세그먼트 만들기]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) 삭제할 사용자 프로필을 포함하는 세그먼트를 만드세요. 중복 사용자를 삭제하는 경우 모든 사용자 프로필을 포함해야 합니다.

Braze에서 **오디언스** > **오디언스 관리**로 이동한 다음 **사용자 삭제** 탭을 선택하세요.

![Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**사용자 삭제**를 선택하고 삭제할 세그먼트를 선택한 다음 **다음**을 선택하세요.

![삭제를 위해 선택된 세그먼트가 있는 팝업 창.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

요청을 확인하려면 **DELETE**를 입력한 다음 **사용자 삭제**를 선택하세요.

![확인 상자에 'DELETE'가 입력된 확인 페이지.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

이 세그먼트의 사용자들은 즉시 삭제되지 않습니다. 대신, 다음 7일 동안 삭제 대기 상태로 표시됩니다. 이 시간이 지나면 삭제되며, 알려드리기 위해 이메일을 보낼 것입니다.

{% alert tip %}
세그먼트 변경에 관계없이 이러한 정확한 사용자가 삭제되도록 하기 위해 **삭제 대기 중**라는 세그먼트 필터가 자동으로 생성됩니다. 이 필터를 [사용하여]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) 삭제 대기 상태를 확인할 수 있습니다.
{% endalert %}

## 세그먼트 삭제 확인

Braze는 삭제 대기 중인 프로필 수와 함께 확인 이메일을 보냅니다.

삭제를 계속 진행하려면 Braze에 로그인하고 삭제 요청을 확인하세요.

이메일에 표시된 시간 내에 확인하지 않으면 삭제 요청이 만료되고 진행되지 않습니다.

## 세그먼트 삭제 취소 {#cancel}

보류 중인 세그먼트 삭제를 취소할 수 있는 기간은 7일입니다. 취소하려면 **오디언스** > **오디언스 관리**로 이동한 다음 **사용자 삭제** 탭을 선택하세요.

![Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

보류 중인 세그먼트 삭제 옆에서 <i class="fa-solid fa-eye"></i>를 선택하여 삭제 기록 세부정보를 엽니다.

![‘사용자 삭제’ 탭의 보류 중인 세그먼트 삭제입니다.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

삭제 기록 세부정보에서 **삭제 취소**를 선택합니다.

![‘사용자 삭제’ 탭의 ‘삭제 기록 세부정보’ 창입니다.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
대량 사용자 삭제가 진행 중일 때 언제든지 취소할 수 있습니다. 그러나 취소 전에 이미 삭제된 사용자는 복원할 수 없습니다.
{% endalert %}

## 삭제 상태 확인 {#status}

삭제 상태는 [세그먼트 필터](#segment-filters), [오디언스 관리](#manage-audience) 페이지 또는 [보안 이벤트 보고서](#security-event-report)를 사용하여 확인할 수 있습니다.

### 세그먼트 필터

사용자 세그먼트를 삭제 요청하면 [세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters)인 **보류 중 삭제**가 자동으로 생성됩니다. 이를 사용하여:

- 특정 삭제 실행 날짜에 연결된 정확한 사용자 집합을 확인합니다.
- 해당 사용자를 캠페인에서 제외하여 삭제 전 메시지를 받지 않도록 합니다.
- 준수 또는 기록 보관을 위해 목록을 내보냅니다.

### 오디언스 관리

{% alert note %}
삭제될 정확한 사용자 목록을 얻으려면 대신 [보류 중 삭제 세그먼트 필터](#segment-filters)를 사용하세요.
{% endalert %}

**오디언스** > **오디언스 관리**로 이동한 다음 **사용자 삭제** 탭을 선택하세요.

![Braze 대시보드의 '오디언스 관리' 섹션에 있는 '사용자 삭제' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

이 페이지에서는 현재 및 보류 중인 모든 삭제에 대한 일반 정보를 찾을 수 있습니다:

| 필드 | 설명 |
|-------|-------------|
| 요청 날짜 | 요청이 원래 작성된 날짜입니다. **보류 중 삭제** 필터와 함께 사용하여 삭제 대기 중인 프로필 목록을 가져옵니다. |
| 요청자 | 삭제 요청을 시작한 사용자입니다. |
| 세그먼트 이름 | 삭제 대기 중인 사용자를 선택하는 데 사용되는 세그먼트의 이름입니다. |
| 상태 | 삭제 요청이 보류 중인지, 진행 중인지 또는 완료되었는지를 보여줍니다. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

특정 요청에 대한 자세한 내용을 보려면 <i class="fa-solid fa-eye"></i>을 선택하여 삭제 기록 세부정보를 표시합니다. 여기에서 [보류 중인 세그먼트 삭제를 취소](#cancel)할 수도 있습니다.

![‘사용자 삭제’ 탭의 보류 중인 세그먼트 삭제입니다.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### 보안 이벤트 보고서

보안 이벤트 보고서를 다운로드하여 이전 삭제의 상태를 확인할 수도 있습니다. 자세한 내용은 [보안 설정]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report)을 참조하십시오.

## Frequently asked questions {#faq}

### 1억 명 이상의 사용자가 있는 세그먼트를 삭제할 수 있나요?

아니요. 1억 명 이상의 사용자가 있는 세그먼트를 삭제할 수 없습니다. 이 크기의 세그먼트를 삭제하는 데 도움이 필요하면 [support@braze.com](mailto:support@braze.com)에 문의하십시오.

### 100억 명의 사용자를 삭제할 수 없는 것 같고 1천만 명만 삭제할 수 있는 것 같습니다. 이것은 버그인가요?

아니요, 이것은 버그가 아닙니다. 일부 고객은 초기 액세스(EA) 프로그램 동안 삭제할 수 있는 사용자 수에 제한이 있습니다.

EA 프로그램이 진행됨에 따라 이 용량은 증가하도록 설계되어 모든 고객이 최대 1억 명의 사용자를 삭제할 수 있습니다.

이 용량을 늘리고 싶다면 Braze 계정 매니저에게 문의하십시오. 요청은 제품 팀의 재량에 따라 승인됩니다.

### 자동 사용자 병합이 사용자 삭제에 영향을 미칩니까?

예약된 병합에 삭제 대기 중인 사용자 프로필이 포함된 경우, Braze는 해당 프로필을 건너뛰고 병합하지 않습니다. 이 프로필을 병합하려면 삭제에서 제거해야 합니다.

### 삭제 대기 중인 사용자에게 전송된 데이터는 어떻게 됩니까?

외부 시스템이나 SDK에서 전송된 데이터는 여전히 수락되지만, 사용자는 활동과 관계없이 예정대로 삭제됩니다.

### 캔버스와 캠페인이 삭제 대기 중인 사용자에게 트리거됩니까?

예. 그러나 **삭제 대기 중** [세그먼트 필터](#segment-filters)를 사용하여 모든 사용자를 제외하는 세그먼트 포함 필터를 추가할 수 있습니다.

### 삭제된 사용자 프로필을 복구할 수 있습니까?

개별 사용자 삭제는 영구적입니다.

첫 7일 이내에 [세그먼트 삭제 취소](#cancel)를 할 수 있습니다. 그러나 취소하기 전에 이미 삭제된 사용자는 복원할 수 없습니다.
