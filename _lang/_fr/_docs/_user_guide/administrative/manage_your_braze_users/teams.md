---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers various aspects of Teams in your Braze dashboard, such as creating and archiving teams, or assigning roles."
---

# Teams

Braze Admins can divide subsets of their Dashboard users into Teams with varying user roles and permissions. Teams can be set up across customer base location, language, and custom attributes such that members and non-members have different access to messaging features and customer data. Once created, Team filters and tags can be assigned across various engagement tools providing teams access and filtering end-users based on assigned team definitions.

{% include video.html id="UYjKrFcL9sQ" align="right" %}

## Creating a team

Go to the __Manage Settings__ page and click __Manage Teams__. From there, you will see an option to __+Add Team__ that then populates a modal window. Here you will not only give the Team a name, but also have the option to use a custom attribute, location, or language to further define the access that will be granted.

This Team can later be used to filter end-users for engagement objects like campaigns, Canvases, cards, segments, and more, granting members of this team access. See [Tags and Filters](#tags-and-filters) below to learn more.

!\[Adding a team\]\[68\]

## Assign team roles

Braze Admins can assign Team Roles to their Dashboard users, who are limited to only read/write data available to their particular Teams. Predefined Team Roles include language and location (by Countries and Regions).

To assign a Team Role, navigate to __Manage Users__ and select a user you'd like to add to your team. Using the pencil icon, edit their User Role to __Limited__ and add them to the appropriate app group. The assigned app group will populate a row of checkboxes at the bottom of the page. Next, a team dropdown will appear, select the team you'd like to apply, and assign specific permissions using the team permission checkbox row that appears.

!\[Teams\]\[2\]

To see descriptions of what each user permission includes and how to use them, check out our [User Permissions section]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Assign teams tags and filters {#tags-and-filters}

Dashboard objects can be assigned to Teams. Canvases, campaigns, cards, segments, email templates, and media library assets can all be labeled with a Team filter and tag.

!\[Teams\]\[3\]{: style="max-width:70%;"}

Based on the definitions applied to the Team created, when a Team filter is assigned, you automatically restrict user profiles that a dashboard object can include based on your team definition. For example, TeamA is defined as end-users from the USA. When a TeamA Team filter is assigned to CampaignA, CampaignA will only include end-users from the USA, and only TeamA (other than dashboard admins) will be able to access CampaignA.

Based on assigned permissions, members of teams will only be allowed to access Dashboard engagement tools that have the team filter set. Members are also able to filter Canvases, campaigns, cards, and segments by team to identify Dashboard objects relevant to them.

Note that Teams are not available on all Braze contracts. If you’d like to access this feature, reach out to your account executive and customer success manager or contact us at [hello@braze.com](mailto:success@braze.com) for a consultation.

## Archive an existing team

You can archive Teams from the **Manage Teams** page, under **Manage Settings**. Select one or many teams to archive.

If the team is not associated with any object within Braze, the team will be archived immediately. If the team is associated with an object, you will be presented with an option to 'remove the team after the archive process' or 'replace the team with another team'

!\[Archiving a team\]\[86\]{: style="max-width:70%;"}

Admins can unarchive a team by selecting the archived team and then clicking **Unarchived**.
[2]: {% image_buster /assets/img/teams.png %} [3]: {% image_buster /assets/img/teams1.png %} [68]: {% image_buster /assets/img_archive/adding_a_team.png %} [86]: {% image_buster /assets/img_archive/archive_a_team.png %}
