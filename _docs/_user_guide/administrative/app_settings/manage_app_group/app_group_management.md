---
nav_title: Workspace Management
article_title: Workspace Management
page_order: 0
page_type: reference
description: "This reference article covers managing workspaces in your Braze dashboard. Here, you can find information on the draws of multiple workspaces, how to delete your workspace, and more."

---

# Workspace management

> Workspaces are designed to house versions of the same application across multiple platforms. Many Braze customers also use workspaces to contain free and premium versions of their application on the same platform. Looking for steps on how to create a new workspace? Refer to [Workspace configuration]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/).

You can manage, segment, and communicate with multiple applications simultaneously all from **Manage Settings** > **Settings** in the Braze dashboard.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), **Settings** is now **App Settings** and can be found at **Settings** > **Setup and Testing** > **App Settings**.
{% endalert %}

## Multiple apps in a workspace

There is no limit to the number of apps that can exist in a single workspace. The draw to have multiple apps under one workspace can be enticing, as it lets you rate limit messaging across your entire app portfolio. However, as a best practice we suggest only putting different versions of the same (or very similar) apps together under one workspace.

For example, you might have your iOS and Android versions of the same app in one workspace, or your free and premium versions of the same app in one workspace.

Whichever apps you choose to have in one workspace will have their data aggregated—which will have a notable impact on the following filters in Braze:

- Last Used App
- First Used App
- Session Count
- Money Spent In-App
- Push Subscription (This becomes an all or none situation—if your users unsubscribe from one app, they are unsubscribed from all apps in the workspace.)
- Email Subscription (This becomes an all or none situation, and can leave you open to compliance issues.)

This is not an exhaustive list.

## Administrating workspaces

We recommend having multiple Braze users with admin permissions for a single workspace. As a general rule, you want to ensure there are enough people with your organization to manage other users' permissions.

## Renaming or deleting your workspace

To rename your workspace, click **Manage Settings** in the left sidebar. Then, click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-pencil-alt" ></span>**Edit** next to your workspace's name.

To delete your workspace entirely from the dashboard, click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-cog" ></span>**Settings** on the same page and select **Delete Workspace**.

![Rename workspace from the Settings tab][70]

{% alert warning %}
Be careful when deleting workspaces! Once a workspace is deleted, it can't be restored.
{% endalert %}

[69]: {% image_buster /assets/img_archive/manageappgroupnavigation1.png %}
[70]: {% image_buster /assets/img_archive/appsettingsview1.png %}
