---
nav_title: Duplicate Users
article_title: Duplicate users
description: "Learn how to find and merge duplicate users in your Braze dashboard."
page_order: 0
---

# Duplicate users

> Learn how to find and merge duplicate users, so you can maximize the effectiveness of your campaigns and Canvases. To merge duplicate users using the Braze REST API, see [POST: Merge Users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

## Individual merging

If a user search returns duplicate profiles, you can merge each profile individually from the user's profile in the Braze dashboard.

### Step 1: Search for a duplicate profile

In Braze, select **Audience** > **User Search**.

![The "User Search" tile highlighted in the navigation menu.]()

Enter a unique identifier, such as an email address or phone number, for the duplicate profile, then select **Search**.

![The "User Search" page in the Braze dashboard with an email entered in the search bar.]()

### Step 2: Merge duplicates

To begin the merge process, select **Merge duplicates**.

![One of the duplicate user's profiles.]()

Choose which user profile to keep and which to merge, then select **Merge profiles**. Repeat this process until you've merged all duplicate profiles.

![The individual merge page for a duplicate profile.]()

{% alert warning %}
Merged user profiles cannot be recovered after merging.
{% endalert %}

## Bulk merging

When you bulk merge duplicate users, Braze finds profiles with matching identifiers (such as an email address) and merges all their data into the most recently updated profile. This profile is used as the new primary profile and the other profiles are deleted.

### Step 1: Go to Manage Audience

In the Braze dashboard, select **Audience** > **Manage Audience**.

![The "Manage Audience" tile highlighted in the navigation menu.]()

### Step 2: Preview the results (optional)

To preview your results before merging your duplicates, select **Generate list of duplicates**.

![The "Manage Audience" page with "Generate list of duplicates" highlighted.]()

Braze will generate your preview and send it to your email address as a CSV file.

![An email from Braze with a link to the generated CSV file.]()

In the following example, Braze used the user's email address to flag duplicate profiles and identify which one to keep. If these profiles are merged, Braze will make the profile with Braze ID `65fcaa547f470494d1370` the new primary profile and delete the other profiles after merging.

{% tabs local %}
{% tab example csv file %}
| Email Address        | External ID | Phone Number | Braze ID                 | Identifier for rule | Profile to keep | Profile to merge |
|----------------------|-------------|--------------|--------------------------|---------------------|-----------------|------------------|
| alex@company.com     |             |              | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             |              | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             |              | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{% endtab %}
{% endtabs %}

### Step 3: Merge your duplicates

If you're satisfied with the results of your preview, select **Merge all duplicates**.

{% alert warning %}
Merged user profiles cannot be recovered after merging.
{% endalert %}

![The "Manage Audience" page with "Merge all duplicates" highlighted.]()
