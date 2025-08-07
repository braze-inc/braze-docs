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
Several sections on this page refer to the **Company Users** page. If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), **Company Users** is called **Manage Users** and is located under your account icon.
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

![User details fields.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. For users that aren't administrators, select the company-level and workspace-level [permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions) you want this user to have.

![Workspace-level permissions with a section for custom permissions fields.]({% image_buster /assets/img/add_new_user_3.png %})

### Email address requirements

Every email address used in an [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) must be unique. This means that if you try to add an email address that's already associated with a user who had or still has access to a company workspace in that instance, you'll see an error message. 

If your team uses Gmail and you're experiencing issues adding an email address, you can create an alias by adding a plus sign (+) like "+1" or "+test" to the email address. For example, `contractor@braze.com` can have an alias of `contractor+1@braze.com`. Emails to `contractor+1@braze.com` will still be delivered to `contractor@braze.com`, but the alias will be recognized as a unique email address.

### Can I change my Braze account's email address?

For security reasons, users cannot change the email address associate with their Braze account. If a user wants to update their email address, an administrator should [create a new account](#adding-braze-users) for them with their preferred email address.

## Suspending Braze users

Suspending a user puts their account into an inactive state, where the user can no longer log in, but the data associated with their account is preserved. Only administrators can suspend or un-suspend Braze users.

To suspend a user, go to **Settings** > **Company Users**, find their username and select <i class="fa-solid fa-user-lock"></i> **Suspend**.

![Option to suspend a user.]({% image_buster /assets/img_archive/suspend_user.png %})

Administrators can also suspend a user by selecting their name from the list and clicking **Suspend user** in the footer.

![Suspend a user when editing the user details.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Assigning user access and responsibilities

{% multi_lang_include permissions.md content="Differences" %}

## Deleting Braze users

To delete a user, go to **Settings** > **Company Users**, find their username and select <i class="fa fa-trash-can"></i> **Delete user**.

![Delete a user]({% image_buster /assets/img_archive/delete_user_new.png %})

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

### Impact of deleting a dashboard user

When a dashboard user is deleted, there will be no significant impact on the assets they created within the dashboard, such as campaigns, segments, and Canvases. However, it's important to note that the **Created By** field for these assets will display a "null" value instead of the email address of the deleted user.

If a new dashboard user is subsequently created with the same email address as the deleted user, Braze will not re-associate the assets created by the deleted user with the new user. The new dashboard user will start with a clean slate and will not be credited as the creator of any existing assets in the dashboard.

## Troubleshooting

### "Email is already taken" when trying to add a user

If you try to add a new user and receive an error saying the email is already taken, but can't find them in your user list, that user most likely exists within a different instance of the same Braze dashboard cluster.

To create this new user, you can do either of the following:

1. Delete the user from the other instance before you can create them in the new one, or
2. Create the user with a different email string (such as `testing+01@braze.com`) or another email alias. 

If you don't receive the message activation on your inbox when using `testing+01@braze.com`, confirm with your IT team that you can accept messages from that kind of email address. Some administrators filter messages sent to email addresses with a `+`.

