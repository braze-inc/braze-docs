---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers various aspects of Teams in your Braze dashboard, such as creating and archiving teams, or assigning roles."

---

# Teams

Braze admins can group their dashboard users into Teams with varying user roles and permissions. Teams can be set up across customer base location, language, and custom attributes so that members and non-members have different access to messaging features and customer data. Team filters and tags can be assigned across various engagement tools. 

{% include video.html id="UYjKrFcL9sQ" align="right" %}

## Creating Teams

Go to the **Manage Settings** page, select **Manage Teams**, and click <i class="fas fa-plus"></i> **Add Team**. Enter the **Team Name**. Use the **Define Team (Optional)** to select a custom attribute, location, or language to further define permissions. 

Teams can be used to filter end-users for engagement objects like campaigns, Canvases, Content Cards, segments, and more. See [Tags and Filters](#tags-and-filters) below to learn more. 

{% alert note %}
Note that Teams are not available on all Braze contracts. If you’d like to access this feature, reach out to your Braze Account Manager or [contact us](mailto:success@braze.com) for a consultation.
{% endalert %}

![Adding Team][68]

## Assigning roles

Braze admins can assign Team Roles to their dashboard users who are limited to only read or write data available to their particular Teams. Predefined Team Roles include language and location. 

To assign a Team Role, navigate to **Manage Users** and select a user you'd like to add to your team. Using the pencil icon, edit their User Role to **Limited** and add them to the appropriate app group. The assigned app group will populate a row of checkboxes at the bottom of the page. Next, a Team dropdown will appear, select the team you'd like to apply, and assign specific permissions using the team permission checkbox row that appears.

![Teams][2]

To see descriptions of what each user permission includes and how to use them, check out our [User Permissions section]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Assigning tags and filters {#tags-and-filters}

Dashboard objects can be assigned to Teams. Canvases, campaigns, cards, segments, email templates, and media library assets can all be labeled with a Team filter and tag. 
 
![Team Tags][3]{: style="max-width:70%;"}

Based on the definitions applied to the Team created, when a Team filter is assigned, you automatically restrict user profiles that a dashboard object can include based on your team definition. For example, TeamA is defined as end-users from the US. When a TeamA Team filter is assigned to CampaignA, CampaignA will only include end-users from the USA, and only TeamA (other than dashboard admins) will be able to access CampaignA. 

Based on assigned permissions, members of teams will only be allowed to access dashboard engagement tools that have the team filter set. Members are also able to filter Canvases, campaigns, cards, and segments by team to identify Dashboard objects relevant to them.

## Archiving an existing Team

You can archive Teams from the **Manage Teams** page, under **Manage Settings**. Select one or many teams to archive.

If the Team is not associated with any object within Braze, the Team will be archived immediately.

If the Team is associated with an object, you will be presented with an option to remove the Team after the archive process or replace the Team.

![Archiving Team][86]{: style="max-width:70%;"}

Braze admins can unarchive a Team by selecting the archived Team and clicking **Unarchived**.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
