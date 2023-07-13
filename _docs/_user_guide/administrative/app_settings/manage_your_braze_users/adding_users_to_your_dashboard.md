---
nav_title: Adding and Deleting Braze Users
article_title: Adding and Deleting Braze Users
page_order: 0
page_type: reference
description: "This reference article covers how to add users to your company account or delete users."

---

# Adding and deleting Braze users

> Learn how to add users to your company account or delete users.

## Adding Braze Users

There is no limit to the number of users (administrators or limited users) you can have on your company account. Your company admins will be responsible for adding users and setting relevant permissions. However, if there is only one admin left in your workspace, that individual will not be able to remove their own admin permissions.

To add a new user to your Braze account, ensure you have admin privileges and perform the following:

1. Go to **Settings** > **Company Users**.
  {% alert note %}
  If you are using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
  {% endalert %}

{:start="2"}
2. Click **+ Add New User**.
3. Enter their information as prompted, including their email, department, and [user role]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).<br><br>![][2]<br><br>
4. For users with a limited role, select the company level and workspace level permissions you want this user to have.<br><br>![][3]

### Selecting a department

You must select a department for each user added to your company's Braze account. 

Adding your department to your user profile helps ensure you receive relevant communications built around how you use Braze. You will receive support and alerts that apply to you.

## Deleting Braze Users

To delete a user, go to **Settings** > **Company Users**, find their username and click <i class="fa fa-trash-can"></i> **Delete**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), **Company Users** is called **Manage Users** and is located under your account icon.
{% endalert %}

![Delete a user][34]

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

[27]: {% image_buster /assets/img/add-user.gif %} "Add a New User Process"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}