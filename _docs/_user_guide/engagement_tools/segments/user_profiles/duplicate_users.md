---
nav_title: Duplicate Users
article_title: Duplicate users
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

![The "User Search" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %})

Enter a unique identifier, such as an email address or phone number, for the duplicate profile, then select **Search**.

![The "User Search" page in the Braze dashboard with an email entered in the search bar.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Step 2: Merge duplicates

To begin the merge process, select **Merge duplicates**.

![One of the duplicate user's profiles.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:55%;"}

Choose which user profile to keep and which to merge, then select **Merge profiles**. Repeat this process until you've merged all duplicate profiles.

![The individual merge page for a duplicate profile.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

## Bulk merging

When you bulk merge duplicate users, Braze finds profiles with matching identifiers (such as an email address) and merges all their data into the most recently updated profile with an `external_id`. If there's no profiles with an `external_id`, the most recently updated profile without an `external_id` will be used instead.

### Step 1: Go to Manage Audience

In the Braze dashboard, select **Audience** > **Manage Audience**.

![The "Manage Audience" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %})

### Step 2: Preview the results (optional)

To preview your results before merging your duplicates, select **Generate list of duplicates**.

![The "Manage Audience" page with "Generate list of duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze will generate your preview and send it to your email address as a CSV file.

![An email from Braze with a link to the generated CSV file.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

In the following example, Braze uses the user's external ID to flag duplicate profiles and identify which one to keep. If these profiles are bulk merged, Braze will use the profile with an external ID as the user's new primary profile. Now if that user logs in using a merged profile, Braze will update their new primary profile instead.

{% tabs local %}
{% tab example csv file %}
| Email Address        | External ID | Phone Number | Braze ID                 | Identifier for rule | Profile to keep | Profile to merge |
|----------------------|-------------|--------------|--------------------------|---------------------|-----------------|------------------|
| alex@company.com     |   A8i3mkd99          |      (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |  |      (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |   |      (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

### Step 3: Merge your duplicates

If you're satisfied with the results of your preview, select **Merge all duplicates**.

{% alert warning %}
Duplicate user profiles cannot be recovered after merging.
{% endalert %}

![The "Manage Audience" page with "Merge all duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}
