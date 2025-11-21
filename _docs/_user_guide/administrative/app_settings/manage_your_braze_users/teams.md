---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers how to use Braze Teams in the dashboard. Here, you can learn how to create Teams, assign roles, and assign tags and filters."

---

# Teams

> As a Braze admin, you can group your dashboard users into Teams with varying user roles and permissions. This allows you to have multiple, unrelated groups of dashboard users working together in one workspace by separating the types of content that can be edited.

Teams can be set up across customer base location, language, and custom attributes so that Team members and non-Team members have different access to messaging features and customer data. Team filters and tags can be assigned across various engagement tools.

Teams are not available on all Braze contracts. If you'd like to access this feature, contact your Braze account manager or [contact us](mailto:success@braze.com) for a consultation.

## How do Teams differ from permission sets and roles?

{% multi_lang_include permissions.md content="Differences" %}

## Creating Teams

Go to **Settings** > **Internal Teams** and select <i class="fas fa-plus"></i> **Add Team**.

![Window to add a new Team.]({% image_buster /assets/img_archive/adding_a_team.png %}){: style="max-width:70%;"}

Enter the **Team Name**. If desired, use the **Define Team** field to select a custom attribute, location, or language to further define what user data the Team has access to. For example, a possible use case is to perform [testing with Teams](#testing-with-Teams) by creating a development Team that only has access to test users, identified by a custom attribute. Another use case is to restrict communication with users based on product.

If a Team is defined by a custom attribute, language, or country, you can then use the Team to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. For more, see [Assigning Team tags](#tags-and-filters).

## Assigning users to Teams

Braze administrators and limited users with the company-level permission "Can Manage Company Settings" can assign Team-level permissions to a dashboard user with limited access. When assigned to a Team, dashboard users are limited to only read or write data available to their particular Teams, such as user language, location, or custom attribute, as defined when the Team was created.

To assign a user to a Team, navigate to **Settings** > **Company Users** and select a user you'd like to add to your Team.

Then perform the following steps:

1. In the **Workspace-level permissions** section, add the user to the appropriate workspace if they aren't already included.

![A permission set for the "Swifty & Droidboy" workspace.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Select **+ Add team-level permissions**, then select the **Team** you'd like to add this user to.
3. Assign specific permissions from the **Team** permissions column.

![A section to select permissions for the "Customer Support" team.]({% image_buster /assets/img/teams.png %})

### Available Team-level permissions

The following are all available permissions you can assign at the Team level. Any permissions not listed here are only granted on the workspace level, and these permissions will appear as "--" in the **Teams** permissions column.

- Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers
- Send Campaigns, Canvases
- Launch and Manage Content Cards
- Edit Segments
- Export User Data
- View User Profiles PII Compliant
- Manage Dashboard Users
- Manage Media Library Assets
- Approve and Deny Campaigns
- Approve and Deny Canvases
- Create and Edit Canvas Templates
- View Canvas Templates
- Archive Canvas Templates
- Create and Edit Landing Page Templates
- View Landing Page Templates
- Archive Landing Page Templates

To see descriptions of what each user permission includes and how to use them, check out our [User Permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) section.

## Assigning Team tags {#tags-and-filters}

You can assign a Team to Canvases, campaigns, cards, segments, email templates, and media library assets with the **Add Team** filter.
 
![Adding a Team tag to a campaign.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Based on the *definitions* applied when the Team was created, when a Team filter is assigned, that engagement tool's audience is restricted to user profiles that match the definition.
- Based on assigned *permissions*, Team members will only be allowed to access dashboard engagement tools that have their Team filter set. If they have limited or no workspace permissions, they must add a Team filter to certain objects before they can save or launch them. Team members are also able to filter Canvases, campaigns, cards, and segments by Team to identify content relevant to them.

### Use cases

Consider the following two scenarios for a marketer in Braze named Michelle. Michelle is a member of a Team called "Development". She has access to all of the Team-level permissions for the Development Team.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

In this scenario, Michelle is a limited user who has no workspace-level permissions. Her permissions look something like this:

![Custom permissions with no workspace-level permissions and 16 team-based permissions.]({% image_buster /assets/img_archive/scenario1.png %})

Based on Michelle's assigned permissions, whenever she creates a campaign, she can only assign the "Development" Team to that campaign. She can't launch the campaign unless the Team is assigned, and she can't view or access any other Team tags.

![Campaign Team tag dropdown that only displays the "Development" Team tag.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In this scenario, Michelle is still a member of the Development Team, but she also has an additional workspace-level permission.

![Custom permissions with one workspace-level permission and 15 team-based permissions.]({% image_buster /assets/img_archive/scenario2.png %})

Because Michelle has the workspace-level permission of "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers", she can view and assign other Team filters to the campaign she creates.

![Campaign Team tag dropdown with multiple Team tags]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Similar to the first scenario, Michelle must add the Development Team tag to the campaign before she can launch it.

{% endtab %}
{% endtabs %}

## Testing with Teams

One possible use case for Teams is to create a Teams-based approval system for testing and launching content in a production environment.

To do so, create a "Development" Team that only has access to test users. You can limit a Team to only access test users if your test users are identifiable by a custom attribute. Then, add the custom attribute as a definition when creating or editing the Team (see the preceding section [Creating Teams](#creating-Teams)). Your approvers should have access to all users.

The general process would be as follows:

1. The Development Team creates a campaign and adds the "Development" Team tag.
2. The Development Team launches the campaign to test users.
3. The Approver Team validates the local campaign design, promotes, and launches. To launch, the Approver Team changes the Team tag from "Development" to "[All Teams]" and relaunches the campaign.

For changes to active campaigns:

1. The Development Team clones the running campaign, adds the "Development" Team tag, and saves.
2. The Development Team makes edits and shares with the Approver Team.
3. The Approver Team removes the "Development" Team tag, pauses the previous campaign, and launches the new campaign.

## Archiving an existing Team

You can archive Teams from the **Internal Teams** page.

Select one or many Teams to archive. If the Team is not associated with any object within Braze, Braze archives the Team immediately. If the Team is associated with an object, Braze presents you with an option to remove the Team after the archive process or replace the Team.

![Archiving a Team that is associated with an object in Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze admins can unarchive a Team by selecting the archived Team and selecting **Unarchive**.

