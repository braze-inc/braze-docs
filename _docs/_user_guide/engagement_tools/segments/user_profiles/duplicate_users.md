---
nav_title: Duplicate users
article_title: Duplicate Users
description: "Learn how to find and merge duplicate users in your Braze dashboard."
page_order: 0
---

# Duplicate users

> Learn how to find and merge duplicate users, so you can maximize the effectiveness of your campaigns and Canvases.

{% alert tip %}
To merge duplicate users using the Braze REST API, see [POST: Merge Users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Individual merging

If a user search returns duplicate profiles, you can merge each profile individually from the user's profile in the Braze dashboard.

### Step 1: Search for a duplicate profile

In Braze, select **Audience** > **User Search**.

![The "User Search" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Enter a unique identifier, such as an email address or phone number, for the duplicate profile, then select **Search**.

![The "User Search" page in the Braze dashboard.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Step 2: Merge duplicates

To begin the merge process, select **Merge duplicates**.

![One of the duplicate user's profiles.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Choose which user profile to keep and which to merge, then select **Merge profiles**. Repeat this process until you've merged all duplicate profiles.

![The individual merge page for a duplicate profile.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Bulk merging

When you bulk merge duplicate users, Braze finds profiles with matching identifiers (such as an email address) and merges all their data into the most recently updated profile with an `external_id`. If there are no profiles with an `external_id`, the most recently updated profile without an `external_id` will be used instead.

### Step 1: Go to Manage Audience

In the Braze dashboard, select **Audience** > **Manage Audience**.

![The "Manage Audience" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Step 2: Preview the results (optional)

To preview your results before merging your duplicates, select **Generate list of duplicates**.

![The "Manage Audience" page with "Generate list of duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze will generate your preview and send it to your email address as a CSV file.

![An email from Braze with a link to the generated CSV file.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

In the following example, Braze uses the user's external ID to flag duplicate profiles and identify which one to keep. If these profiles are bulk merged, Braze will use the profile with an external ID as the user's new primary profile.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Merge behavior

Braze will fill empty fields on the kept profile with values from the merged profile. For a list of the fields that will be filled, refer to [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Step 3: Merge your duplicates

If you're satisfied with the results of your preview, select **Merge all duplicates**.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

![The "Manage Audience" page with "Merge all duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Rules-based merging

You can use rules to control how duplicate profiles are resolved when running a merge so the most relevant user profile is kept. When rules are set, Braze will keep profiles that match your criteria.

### Step 1: Define your rules

1. Go to **Audience** > **Manage Audience** > **Edit rules**.
2. In the **Profile to keep** section of the **Edit rules** panel, select the **Identifier** for the profiles that will be kept when merging duplicates. This can be the email address or phone number.
3. In the **Resolving ties** section, select the criteria to determine how to solve ties between profiles with matching criteria from **Profile to keep**. You can select the following:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![The "Edit rules" panel with sections to select options for "Profile to keep" and "Resolving ties".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

For example, you could keep the profile that has a phone number. If multiple users have the same phone number, you could resolve ties using the **Updated date** field and prioritize the most recently updated user.

### Step 2: Preview the results (optional)

After saving your rules, you can preview how they'll work by selecting **Generate a list of duplicates**. Braze will generate your preview and send it to your email address as a CSV file that shows which users would be kept and merged if your rules were applied. 

### Step 3: Merge duplicates

If you're satisfied with the results of your preview, return to the **Manage Audience** page and select **Merge all duplicates**.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Scheduled merging

Similar to rules-based merging, scheduled merging allows you to automate the merging of user profiles on a daily basis using preconfigured rules.

![The "Manage Audience" page with "schedule" button.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

After the feature is turned on, Braze will automatically assign a timeslot to perform the merge process daily at approximately 12 am in the user's company time zone. You can turn off scheduled merging at any time. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}
