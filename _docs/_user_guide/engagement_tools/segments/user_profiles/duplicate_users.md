---
nav_title: Duplicate Users
article_title: Duplicate users
description: "Learn how to find and merge duplicate user profiles in your Braze audience."
---

# Duplicate users

> Learn how to find and merge duplicate users, so you can maximize the effectiveness of your campaigns and Canvases. To merge duplicate profiles using the Braze REST API, see [POST: Merge Users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
 
When you merge duplicate users, Braze finds profiles with matching identifiers (such as an email address) and merges all profile data into the most recently updated profile. This profile will be used as the new primary profile and the other profiles will be deleted.

{% alert warning %}
Duplicate profiles deleted after merging cannot be recovered.
{% endalert %}

## Merging duplicate users

### Step 1: Go to Manage Audience

In the Braze dashboard, select **Audience** > **Manage Audience**.

![The "Manage Audience" tile highlighted in the navigation menu.]()

### Step 2: Preview the results (optional)

To preview your results before merging your duplicates, select **Generate list of duplicates**.

![TODO.]()

Braze will generate your preview and send it to your email address as a CSV file.

![TODO.]()

In the following example, Braze used the user's email address to flag duplicate profiles and identify which one to keep.

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

If you're satisfied with your preview, select **Merge all duplicates.**

{% alert warning %}
Duplicate profiles deleted after merging cannot be recovered.
{% endalert %}

![TODO.]()
