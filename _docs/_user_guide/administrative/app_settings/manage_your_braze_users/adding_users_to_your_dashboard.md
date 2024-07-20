---
nav_title: Managing Braze Users
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

There is no limit to the number of users (administrators or limited users) you can have on your company account. Your company admins will be responsible for adding users and setting relevant permissions. However, if there is only one admin left in your workspace, that individual will not be able to remove their own admin permissions.

To add a new user to your Braze account, ensure you have admin privileges and perform the following:

1. Go to **Settings** > **Company Users**.
2. Click **+ Add New User**.
3. Enter their information as prompted, including their email, department, and [user role]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).<br><br>![]({% image_buster /assets/img/add_new_user_2.png %})<br><br>
4. For users with a limited role, select the company level and workspace level permissions you want this user to have.<br><br>![]({% image_buster /assets/img/add_new_user_3.png %})

Every email address used in a workspace must be unique. This means that if you try to add an email address that's already associated with a user who had or still has access to the workspace, you'll see an error message. As a workaround for Gmail accounts that recognize the alias created by adding a plus sign (+) to the email address, you could add "+example" to the email address. For example, `contractor@braze.com` can be `contractor+1@braze.com`.

### Selecting a department

You must select a department for each user added to your company's Braze account.

Adding your department to your user profile helps ensure you receive relevant communications built around how you use Braze. You will receive support and alerts that apply to you.

## Suspending Braze users

Suspending a user puts their account into an inactive state, where the user can no longer log in, but the data associated with their account is preserved. Only administrators can suspend or un-suspend Braze users.

To suspend a user, go to **Settings** > **Company Users**, find their username and click <i class="fa-solid fa-user-lock"></i> **Suspend**.

![Suspend a user]({% image_buster /assets/img_archive/suspend_user.png %})

Administrators can also suspend a user by selecting their name from the list and clicking **Suspend user** in the footer.

![Suspend a user when editing the user details.]({% image_buster /assets/img_archive/suspend_user2.png %})

## Deleting Braze users

To delete a user, go to **Settings** > **Company Users**, find their username and select <i class="fa fa-trash-can"></i> **Delete user**.

![Delete a user]({% image_buster /assets/img_archive/delete_user_new.png %})

After a user is deleted, Braze does not keep any of the following data:

- Any attributes that the user had
- Email address
- Phone number
- External user ID
- Gender
- Country
- Language
- Other similar data

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}

[27]: {% image_buster /assets/img/add-user.gif %} "Add a New User Process"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}