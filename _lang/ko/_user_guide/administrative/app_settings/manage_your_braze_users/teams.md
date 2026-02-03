---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers how to use Braze Teams in the dashboard. Here, you can learn how to create Teams, assign roles, and assign tags and filters."

---

# Teams

> As a Braze admin, you can group your dashboard users into Teams with varying user roles and permissions. 이렇게 하면 편집할 수 있는 콘텐츠 유형을 분리하여 서로 관련이 없는 여러 대시보드 사용자 그룹이 하나의 작업 공간에서 함께 작업할 수 있습니다.

Teams can be set up across customer base location, language, and custom attributes so that Team members and non-Team members have different access to messaging features and customer data. 다양한 참여 도구에서 팀 필터와 태그를 할당할 수 있습니다. 작업 공간에 만들 수 있는 Teams 수에는 제한이 없습니다.

모든 Braze 계약에서 팀을 사용할 수 있는 것은 아닙니다. 이 기능을 이용하려면 Braze 계정 매니저에게 문의하거나 [당사에 연락](mailto:success@braze.com) 하여 상담을 요청하세요.

## How do Teams differ from permission sets and roles?

{% multi_lang_include permissions.md content="Differences" %}

## Teams 만들기 {#creating-teams}

**설정** > **내부 팀**으로 이동하여 <i class="fas fa-plus"></i> **팀 추가**를 선택합니다.

![창을 열어 새 Teams를 추가합니다.]({% image_buster /assets/img_archive/adding_a_team.png %}){: style="max-width:70%;"}

**팀 이름**을 입력합니다. If desired, use the **Define Team** field to select a custom attribute, location, or language to further define what user data the Team has access to. For example, a possible use case is to perform [testing with Teams](#test-with-teams) by creating a development Team that only has access to test users, identified by a custom attribute. 또 다른 사용 사례는 제품을 기반으로 사용자와의 커뮤니케이션을 제한하는 것입니다.

If a Team is defined by a custom attribute, language, or country, you can then use the Team to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. For more, see [Assigning Team tags](#tags-and-filters).

## Teams에 사용자 할당하기

Braze administrators and limited users with the company-level permission "Can Manage Company Settings" can assign Team-level permissions to a dashboard user with limited access. When assigned to a Team, dashboard users are limited to only read or write data available to their particular Teams, such as user language, location, or custom attribute, as defined when the Team was created.

To assign a user to a Team, navigate to **Settings** > **Company Users** and select a user you'd like to add to your Team.

그런 다음 다음 단계를 수행합니다:

1. **워크스페이스 수준 권한** 섹션에서 해당 사용자가 아직 포함되지 않은 경우 해당 워크스페이스에 사용자를 추가합니다.

!["Swifty & Droidboy" 작업 공간에 대한 권한 세트입니다.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. **팀 수준 권한 추가를** 선택한 다음 이 사용자를 추가하려는 **팀을** 선택합니다.
3\. **팀** 권한 열에서 특정 권한을 할당합니다.

!["고객 지원" 팀에 대한 권한을 선택하는 섹션입니다.]({% image_buster /assets/img/teams.png %})

### Available Team-level permissions

The following are all available permissions you can assign at the Team level. 여기에 나열되지 않은 모든 권한은 작업 영역 수준에서만 부여되며 이러한 권한은 **Teams** 권한 열에 "--"으로 표시됩니다.

- 캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경설정 센터에 액세스합니다.
- 캠페인, 캔버스 발송
- 콘텐츠 카드 시작 및 관리하기
- 세그먼트 편집
- 사용자 데이터 내보내기
- 사용자 프로필 PII 준수사항 보기
- 대시보드 사용자 관리
- 미디어 라이브러리 자산 관리
- 캠페인 승인 및 거부
- 캔버스 승인 및 거부
- 캔버스 템플릿 생성 및 편집
- 캔버스 템플릿 보기
- 캔버스 템플릿 아카이브
- Create and Edit Landing Page Templates
- View Landing Page Templates
- Archive Landing Page Templates

각 사용자 권한에 포함된 항목과 사용 방법에 대한 설명을 보려면 [사용자 권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) 섹션을 참조하세요.

## 팀 태그 할당하기 {#tags-and-filters}

You can assign a Team to Canvases, campaigns, cards, segments, email templates, and media library assets with the **Add Team** filter.
 
![캠페인에 팀 태그 추가하기.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Based on the *definitions* applied when the Team was created, when a Team filter is assigned, that engagement tool's audience is restricted to user profiles that match the definition.
- Based on assigned *permissions*, Team members will only be allowed to access dashboard engagement tools that have their Team filter set. If they have limited or no workspace permissions, they must add a Team filter to certain objects before they can save or launch them. Team members are also able to filter Canvases, campaigns, cards, and segments by Team to identify content relevant to them.

### 사용 사례

다음 두 가지 시나리오는 Braze의 마케터 미셸의 경우를 가정한 것입니다. Michelle is a member of a Team called "Development". She has access to all of the Team-level permissions for the Development Team.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

이 시나리오에서 Michelle은 워크스페이스 수준 권한이 없는 제한된 사용자입니다. 그녀의 권한은 다음과 같습니다:

![워크스페이스 수준 권한이 없는 커스텀 권한과 16개의 팀 기반 권한이 있습니다.]({% image_buster /assets/img_archive/scenario1.png %})

Based on Michelle's assigned permissions, whenever she creates a campaign, she can only assign the "Development" Team to that campaign. She can't launch the campaign unless the Team is assigned, and she can't view or access any other Team tags.

!["개발" 팀 태그만 표시되는 캠페인 팀 태그 드롭다운입니다.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In this scenario, Michelle is still a member of the Development Team, but she also has an additional workspace-level permission.

![하나의 워크스페이스 수준 권한과 15개의 팀 기반 권한이 있는 커스텀 권한.]({% image_buster /assets/img_archive/scenario2.png %})

Because Michelle has the workspace-level permission of "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers", she can view and assign other Team filters to the campaign she creates.

![여러 개의 팀 태그가 있는 캠페인 팀 태그 드롭다운]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Similar to the first scenario, Michelle must add the Development Team tag to the campaign before she can launch it.

{% endtab %}
{% endtabs %}

## Teams로 테스트하기

One possible use case for Teams is to create a Teams-based approval system for testing and launching content in a production environment.

To do so, create a "Development" Team that only has access to test users. You can limit a Team to only access test users if your test users are identifiable by a custom attribute. Then, add the custom attribute as a definition when creating or editing the Team (see the preceding section [Creating Teams](#creating-Teams)). 승인자는 모든 사용자에 대한 액세스 권한이 있어야 합니다.

일반적인 프로세스는 다음과 같습니다:

1. The Development Team creates a campaign and adds the "Development" Team tag.
2. The Development Team launches the campaign to test users.
3. The Approver Team validates the local campaign design, promotes, and launches. 시작하려면 승인자 팀이 팀 태그를 '개발'에서 '[모든 팀]'으로 변경하고 캠페인을 다시 시작합니다.

활성 캠페인에 대한 변경 사항:

1. The Development Team clones the running campaign, adds the "Development" Team tag, and saves.
2. The Development Team makes edits and shares with the Approver Team.
3. The Approver Team removes the "Development" Team tag, pauses the previous campaign, and launches the new campaign.

## 기존 Teams 보관하기

You can archive Teams from the **Internal Teams** page.

Select one or many Teams to archive. 팀이 Braze 내의 어떤 개체와도 연결되지 않은 경우, Braze는 즉시 해당 팀을 보관합니다. 팀이 개체에 연결된 경우, 보관 프로세스 후 Braze에서 해당 팀을 제거하거나 팀을 교체할 수 있는 옵션이 표시됩니다.

![Braze에서 개체에 연결된 팀 보관하기]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze admins can unarchive a Team by selecting the archived Team and selecting **Unarchive**.

