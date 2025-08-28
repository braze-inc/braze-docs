---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers how to use Braze Teams in the dashboard. Here, you can learn how to create Teams, assign roles, and assign tags and filters."

---

# Teams

> As a Braze admin, you can group your dashboard users into Teams with varying user roles and permissions. 이렇게 하면 편집할 수 있는 콘텐츠 유형을 분리하여 서로 관련이 없는 여러 대시보드 사용자 그룹이 하나의 작업 공간에서 함께 작업할 수 있습니다.

Teams can be set up across customer base location, language, and custom attributes so that Team members and non-Team members have different access to messaging features and customer data. 다양한 참여 도구에서 팀 필터와 태그를 할당할 수 있습니다.

모든 Braze 계약에서 팀을 사용할 수 있는 것은 아닙니다. 이 기능을 이용하고 싶으시면 Braze 계정 매니저에게 [문의하거나](mailto:success@braze.com) 상담을 요청하세요.

## How do Teams differ from permission sets and roles?

{% multi_lang_include permissions.md content="Differences" %}

## Creating Teams

**설정** > **내부 팀**으로 이동하여 <i class="fas fa-plus"></i> **팀 추가**를 선택합니다.

![Adding a new Team]({% image_buster /assets/img_archive/adding_a_team.png %})

**팀 이름**을 입력합니다. If desired, use the **Define Team** field to select a custom attribute, location, or language to further define what user data the Team has access to. For example, a possible use case is to perform [testing with Teams](#testing-with-Teams) by creating a development Team that only has access to test users, identified by a custom attribute. 또 다른 사용 사례는 제품에 따라 사용자와의 커뮤니케이션을 제한하는 것입니다.

If a Team is defined by a custom attribute, language, or country, you can then use the Team to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. For more, see [Assigning Team tags](#tags-and-filters).

## Assigning users to Teams

Braze administrators and limited users with the company-level permission "Can Manage Company Settings" can assign Team-level permissions to a dashboard user with limited access. When assigned to a Team, dashboard users are limited to only read or write data available to their particular Teams, such as user language, location, or custom attribute, as defined when the Team was created.

To assign a user to a Team, navigate to **Settings** > **Company Users** and select a user you'd like to add to your Team.

그런 다음 다음 단계를 수행합니다:

1. **편집**을 선택합니다.
2. 사용자 역할을 **제한으로** 설정합니다.
3. 적절한 작업 공간에 추가합니다. 
4. 이 사용자를 추가하려는 **팀**을 선택하고 **팀** 권한 열에서 특정 권한을 할당합니다.

![]({% image_buster /assets/img/teams.png %})

### Available Team-level permissions

The following are all available permissions you can assign at the Team level. 여기에 나열되지 않은 모든 권한은 작업 영역 수준에서만 부여되며 이러한 권한은 **Teams** 권한 열에 "--"으로 표시됩니다.

- 캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경설정 센터에 액세스합니다.
- 캠페인, 캔버스 발송
- 카드 게시
- 세그먼트 편집
- 사용자 데이터 내보내기
- 사용자 프로필 PII 준수사항 보기
- 대시보드 사용자 관리
- 미디어 라이브러리 자산 관리

각 사용자 권한에 포함된 항목과 사용 방법에 대한 설명을 보려면 [사용자 권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) 섹션을 참조하세요.

## Assigning Team tags {#tags-and-filters}

You can assign a Team to Canvases, campaigns, cards, segments, email templates, and media library assets with the **Add Team** filter.
 
![Adding a Team tag to a campaign]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Based on the *definitions* applied when the Team was created, when a Team filter is assigned, that engagement tool's audience is restricted to user profiles that match the definition.
- Based on assigned *permissions*, Team members will only be allowed to access dashboard engagement tools that have their Team filter set. If they have limited or no workspace permissions, they must add a Team filter to certain objects before they can save or launch them. Team members are also able to filter Canvases, campaigns, cards, and segments by Team to identify content relevant to them.

### 사용 사례

다음 두 가지 시나리오는 Braze의 마케터 미셸의 경우를 가정한 것입니다. Michelle is a member of a Team called "Development". She has access to all of the Team-level permissions for the Development Team.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

이 시나리오에서 Michelle은 워크스페이스 수준 권한이 없는 제한된 사용자입니다. 그녀의 권한은 다음과 같습니다:

![]({% image_buster /assets/img_archive/scenario1.png %})

Based on Michelle's assigned permissions, whenever she creates a campaign, she can only assign the "Development" Team to that campaign. She can't launch the campaign unless the Team is assigned, and she can't view or access any other Team tags.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab 시나리오 2 - 팀 권한 및 워크스페이스 권한 %}

In this scenario, Michelle is still a member of the Development Team, but she also has an additional workspace-level permission.

![]({% image_buster /assets/img_archive/scenario2.png %})

Because Michelle has the workspace-level permission of "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers", she can view and assign other Team filters to the campaign she creates.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Similar to the first scenario, Michelle must add the Development Team tag to the campaign before she can launch it.

{% endtab %}
{% endtabs %}

## Testing with Teams

One possible use case for Teams is to create a Teams-based approval system for testing and launching content in a production environment.

To do so, create a "Development" Team that only has access to test users. You can limit a Team to only access test users if your test users are identifiable by a custom attribute. Then, add the custom attribute as a definition when creating or editing the Team (see the preceding section [Creating Teams](#creating-Teams)). 승인자는 모든 사용자에 대한 액세스 권한이 있어야 합니다.

일반적인 프로세스는 다음과 같습니다:

1. The Development Team creates a campaign and adds the "Development" Team tag.
2. The Development Team launches the campaign to test users.
3. The Approver Team validates the local campaign design, promotes, and launches. To launch, the Approver Team changes the Team tag from "Development" to "[All Teams]" and relaunches the campaign.

활성 캠페인에 대한 변경 사항:

1. The Development Team clones the running campaign, adds the "Development" Team tag, and saves.
2. The Development Team makes edits and shares with the Approver Team.
3. The Approver Team removes the "Development" Team tag, pauses the previous campaign, and launches the new campaign.

## Archiving an existing Team

You can archive Teams from the **Internal Teams** page.

Select one or many Teams to archive. If the Team is not associated with any object within Braze, the Team will be archived immediately. If the Team is associated with an object, you will be presented with an option to remove the Team after the archive process or replace the Team.

![Archiving a Team that is associated with an object in Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze admins can unarchive a Team by selecting the archived Team and selecting **Unarchive**.

