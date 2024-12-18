---
nav_title: Users
article_title: Managing Braze Users
page_order: 0
page_type: reference
description: "This reference article covers how to manage users in your company account, including adding, suspending, and deleting users."

---

# Managing Braze users

> Learn how to manage users in your company account, including adding, suspending, and deleting users.

{% alert note %}
Several sections on this page refer to the **Company Users** page. If you are using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
{% endalert %}

## Adding Braze users

You must have administrator permissions to add users to your Braze account. 

To add a new user:

1. Go to **Settings** > **Company Users**.
2. Click **+ Add New User**.
3. Enter their information as prompted, including their email, department, and [user role]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role).

{% alert tip %}
The department listed in a user's profile determines what types of communications they receive from Braze. This is so everyone only receives the communications and alerts that are relevant to how they use Braze.
{% endalert %}

![][2]

{:start="4"}

4. For users that aren't administrators, select the company-level and workspace-level [permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) you want this user to have.

![][3]

### Email address requirements

Every email address used in an [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) must be unique. This means that if you try to add an email address that's already associated with a user who had or still has access to a company workspace in that instance, you'll see an error message. 

If your team uses Gmail and you're experiencing issues adding an email address, you can create an alias by adding a plus sign (+) like "+1" or "+test" to the email address. For example, `contractor@braze.com` can have an alias of `contractor+1@braze.com`. Emails to `contractor+1@braze.com` will still be delivered to `contractor@braze.com`, but the alias will be recognized as a unique email address.

### Can I change my Braze account's email address?

For security reasons, users cannot change the email address associate with their Braze account. If a user wants to update their email address, an administrator should [create a new account](#adding-braze-users) for them with their preferred email address.

## Suspending Braze users

Suspending a user puts their account into an inactive state, where the user can no longer log in, but the data associated with their account is preserved. Only administrators can suspend or un-suspend Braze users.

To suspend a user, go to **Settings** > **Company Users**, find their username and select <i class="fa-solid fa-user-lock"></i> **Suspend**.

![Suspend a user][4]

Administrators can also suspend a user by selecting their name from the list and clicking **Suspend user** in the footer.

![Suspend a user when editing the user details.][5]

## Deleting Braze users

To delete a user, go to **Settings** > **Company Users**, find their username and select <i class="fa fa-trash-can"></i> **Delete user**.

![Delete a user][34]

After a user is deleted, Braze does not keep any of the following account data:

- Any attributes that the user had
- Email address
- Phone number
- External user ID
- Gender
- Country
- Language
- Other similar data

Braze will keep the following account data:

- Custom attributes or test data associated with their account
- Campaigns or Canvases they created (but the user's name won't appear in them, such as appearing in the **Last edited by** column)

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}
[27]: {% image_buster /assets/img/add-user.gif %} "Add a New User Process"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}