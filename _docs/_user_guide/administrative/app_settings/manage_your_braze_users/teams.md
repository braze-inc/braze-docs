---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers how to use Braze teams in the dashboard. Here, you can learn how to create teams, assign roles, and assign tags and filters."

---

# Teams

> As a Braze admin, you can group your dashboard users into teams with varying user roles and permissions. This allows you to have multiple, unrelated groups of dashboard users working together in one workspace by separating the types of content that can be edited.

Teams can be set up across customer base location, language, and custom attributes so that team members and non-team members have different access to messaging features and customer data. Team filters and tags can be assigned across various engagement tools.

Teams are not available on all Braze contracts. If you'd like to access this feature, reach out to your Braze account manager or [contact us](mailto:success@braze.com) for a consultation.

## How do teams differ from permission sets and roles?

{% multi_lang_include permissions.md content="Differences" %}

## Creating teams

Go to **Settings** > **Internal Teams** and select <i class="fas fa-plus"></i> **Add Team**.

![Adding a new team][68]

Enter the **Team Name**. If desired, use the **Define Team** field to select a custom attribute, location, or language to further define what user data the team has access to. For example, a possible use case is to perform [testing with teams](#testing-with-teams) by creating a development team that only has access to test users, identified by a custom attribute. Another use case is to restrict communication with users based on product.

If a team is defined by a custom attribute, language, or country, you can then use the team to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. For more, see [Assigning team tags](#tags-and-filters).

## Assigning users to teams

Braze administrators and limited users with the company-level permission "Can Manage Company Settings" can assign team-level permissions to a dashboard user with limited access. When assigned to a team, dashboard users are limited to only read or write data available to their particular teams, such as user language, location, or custom attribute, as defined when the team was created.

To assign a user to a team, navigate to **Settings** > **Company Users** and select a user you'd like to add to your team.

Then perform the following steps:

1. Select **Edit**.
2. Set their User Role to **Limited**.
3. Add them to the appropriate workspace. 
4. Select the **Team** you'd like to add this user to, and assign specific permissions from the **Team** permissions column.

![][2]

### Available team-level permissions

The following are all available permissions you can assign at the team level. Any permissions not listed here are only granted on the workspace level, and these permissions will appear as "--" in the **Teams** permissions column.

- Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers
- Send Campaigns, Canvases
- Publish Cards
- Edit Segments
- Export User Data
- View User Profiles PII Compliant
- Manage Dashboard Users
- Manage Media Library Assets

To see descriptions of what each user permission includes and how to use them, check out our [User Permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) section.

## Assigning team tags {#tags-and-filters}

You can assign a team to Canvases, campaigns, cards, segments, email templates, and media library assets with the **Add Team** filter.
 
![Adding a Team tag to a campaign][3]{: style="max-width:70%;"}

- Based on the *definitions* applied when the team was created, when a team filter is assigned, that engagement tool's audience is restricted to user profiles that match the definition.
- Based on assigned *permissions*, team members will only be allowed to access dashboard engagement tools that have their team filter set. If they have limited or no workspace permissions, they must add a team filter to certain objects before they can save or launch them. Team members are also able to filter Canvases, campaigns, cards, and segments by team to identify content relevant to them.

### Use cases

Consider the following two scenarios for a marketer in Braze named Michelle. Michelle is a member of a team called "Development". She has access to all of the team-level permissions for the Development team.

{% tabs %}
{% tab Scenario 1 - Only team permissions %}

In this scenario, Michelle is a limited user that has no workspace-level permissions. Her permissions look something like this:

![]({% image_buster /assets/img_archive/scenario1.png %})

Based on Michelle's assigned permissions, whenever she creates a campaign, she can only assign the "Development" team to that campaign. She can't launch the campaign unless the team is assigned, and she can't view or access any other team tags.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

In this scenario, Michelle is still a member of the Development team, but she also has an additional workspace-level permission.

![]({% image_buster /assets/img_archive/scenario2.png %})

Because Michelle has the workspace-level permission of "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers", she can view and assign other team filters to the campaign she creates.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Similar to the first scenario, Michelle must add the Development team tag to the campaign before she can launch it.

{% endtab %}
{% endtabs %}

## Testing with teams

One possible use case for teams is to create a teams-based approval system for testing and launching content in a production environment.

To do so, create a "Development" team that only has access to test users. You can limit a team to only access test users if your test users are identifiable by a custom attribute. Then, add the custom attribute as a definition when creating or editing the team (see the preceding section [Creating teams](#creating-teams)). Your approvers should have access to all users.

The general process would be as follows:

1. Development team creates a campaign and adds the "Development" team tag.
2. Development team launches the campaign to test users.
3. Approver team validates the local campaign design, promotes, and launches. To launch, the Approver team changes the team tag from "Development" to "[All Teams]" and relaunches the campaign.

For changes to active campaigns:

1. Development team clones the running campaign, adds the "Development" team tag, and saves.
2. Development team makes edits and shares with the Approver team.
3. Approver team removes the "Development" team tag, pauses the previous campaign, and launches the new campaign.

## Archiving an existing team

You can archive teams from the **Internal Teams** page.

Select one or many teams to archive. If the team is not associated with any object within Braze, the team will be archived immediately. If the team is associated with an object, you will be presented with an option to remove the team after the archive process or replace the team.

![Archiving a Team that is associated with an object in Braze][86]{: style="max-width:70%;"}

Braze admins can unarchive a team by selecting the archived team and selecting **Unarchive**.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
