---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "This reference article covers how to use Braze teams in the dashboard. Here, you can learn how to create teams, assign roles, and assign tags and filters."

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/dive-into-braze-teams/869939){: style="float:right;width:120px;border:0;" class="noimgborder"}Teams

> Braze admins can group their dashboard users into Teams with varying user roles and permissions.

{% multi_lang_include video.html id="UYjKrFcL9sQ" align="right" %}

Teams can be set up across customer base location, language, and custom attributes so that team members and non-team members have different access to messaging features and customer data. Team filters and tags can be assigned across various engagement tools.

Teams are not available on all Braze contracts. If you'd like to access this feature, reach out to your Braze account manager or [contact us](mailto:success@braze.com) for a consultation.

## Creating Teams

Go to **Settings** > **Internal Teams** and click <i class="fas fa-plus"></i> **Add Team**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), **Internal Teams** is located under **Manage Settings** > **Manage Teams**.
{% endalert %}

Enter the **Team Name**. Use the **Define Team (Optional)** to select a custom attribute, location, or language to further define permissions.

Teams can be used to filter end-users for features like campaigns, Canvases, Content Cards, segments, and more. See the section in this article on [Assigning tags and filters](#tags-and-filters) to learn more.

![Adding a new team][68]

## Assigning roles

Braze admins can assign Team roles to their dashboard users who are limited to only read or write data available to their particular Teams. Predefined Team roles include language and location. 

To assign a Team role, navigate to **Settings** > **Company Users** and select a user you'd like to add to your team.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find this page by selecting your account icon and clicking **Manage Users**..
{% endalert %}

Then perform the following steps:

1. Click <i class="fa fa-edit"></i> **Edit**.
2. Set their User Role to **Limited**.
3. Add them to the appropriate workspace. 
4. Select the **Team** you'd like to add this user to, and assign specific permissions from the **Team** permissions column.

Note that some permissions are only granted on the workspace level, and these permissions will appear as "--" in the **Teams** permissions column.

![Assigning Team roles][2]

To see descriptions of what each user permission includes and how to use them, check out our [User Permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) section.

## Assigning tags and filters {#tags-and-filters}

You can assign a team to Canvases, campaigns, cards, segments, email templates, and media library assets with the Team filter.
 
![Adding a Team tag to a campaign][3]{: style="max-width:70%;"}

Based on the definitions applied to the Team created, when a Team filter is assigned, you automatically restrict user profiles that an engagement tool can include based on your team definition.

For example, Team Japan is defined as end-users from Japan. When Team Japan is assigned to Campaign A:

- Campaign A will only include end-users from Japan
- Only Team Japan (other than dashboard admins) will be able to access Campaign A

Based on assigned permissions, team members will only be allowed to access dashboard engagement tools that have the team filter set. Team members are also able to filter Canvases, campaigns, cards, and segments by team to identify content relevant to them.

## Archiving an existing Team

You can archive Teams from the **Internal Teams** page. 

Select one or many teams to archive. If the Team is not associated with any object within Braze, the Team will be archived immediately. If the Team is associated with an object, you will be presented with an option to remove the Team after the archive process or replace the Team.

![Archiving a Team that is associated with an object in Braze][86]{: style="max-width:70%;"}

Braze admins can unarchive a Team by selecting the archived Team and clicking **Unarchive**.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
