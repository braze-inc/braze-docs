---
nav_title: Creating and managing workspaces
article_title: Creating and Managing Workspaces
page_order: 0
page_type: reference
description: "This article covers how to create, set up, and manage your workspaces."

---

# Creating and managing workspaces

> This article covers how to create, set up, and manage your workspaces. 

## What is a workspace?

Everything you do in Braze happens within a workspace. Workspaces are a shared environment for you to track and manage engagement for related mobile apps or websites. Workspaces group the same or very similar apps together: for example, the Android and iOS versions of your mobile app. 

## Creating a workspace

### Step 1: Have a plan

Before you begin, make sure you've worked with your team and your Braze onboarding manager to determine the best workspace configuration for your use case. To learn more about planning your workspaces in Braze, check out our [Getting Started: Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces/) guide.

### Step 2: Add your workspace

You can create new workspaces or switch between existing workspaces from the workspace dropdown in the global header.

1. Select the workspace dropdown, then select <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Create workspace**.

![The workspace dropdown with the "Create workspace" button.]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. Give your workspace a name.

{% alert tip %}
You might want to adopt a naming convention so that others in your company can easily find your workspace. For example: "Upon Voyage US – Production" and "Upon Voyage US – Staging".
{% endalert %}

{:start="3"}
3. Select **Create**. It may take a few seconds for Braze to create your workspace.

!["Create Workspace" modal with the name "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

You will be taken to the **App Settings** page to begin adding your app instances. You can access this page at any time from **Settings** > **App Settings**.

!["App Settings" page for the Upon Voyage US - Staging workspace with a button for adding an app.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Step 3: Add your app instances

We refer to the different sites and apps that are collected within a workspace as "app instances".

1. From the **App Settings** page, select **+ Add app**.
2. Give your app instance a name and select what platform or platforms this app instance is on. If you select multiple platforms, Braze will create one app instance for each platform.

!["Add New App to Upon Voyage US - Staging" modal with options to select app details.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. Select **Add app** to confirm.

#### App API keys

After adding your app instance, you will have access to its API key. The API key is used when making requests between your app instance and the Braze API. The API key is also important for integrating the Braze SDK with your app or website.

![Settings page for the Upon Voyage iOS app with fields for the API Key and SDK Endpoint.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android, create four app instances within your workspace (Free iOS app, free Android app, pro iOS app, and pro Android app). This will give you four API keys to use, one for each app instance.
{% endalert %}

#### Live SDK version

The live SDK version displayed on the App Settings page for a specific app is the highest app version with at least 5% of your total daily sessions and has at least 500 sessions in the past day.

This field appears after you have integrated the Braze SDK with your app or website. If a newer version of the Braze SDK is available for your platform, it will be noted here with the tag "Newer Version Available."

!["Live SDK Version" section with a field value of "5.4.0" and an icon that says a new version is available.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Step 4: Repeat as needed

Repeat steps 2 and 3 to set up as many workspaces as your plan requires. As a best practice, we recommend that you create a testing workspace for integration and campaign testing.

{% alert tip %}
**Add a testing workspace**<br>You can perform app testing by completely sandboxing certain users from your production instance. Create a new workspace, and when you publish your application, be sure to change the API key that Braze is using to match that of your production workspace rather than your testing workspace.
{% endalert %}

## Managing workspaces

### Adding favorites

You can add favorite workspaces to access the workspaces you use the most even faster.

![Workspace dropdown with the tab for "Favorite workspaces".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

To add favorite workspaces:

1. Select your profile dropdown, then select **Manage your account**.
2. In the **Account Profile** section, locate the **Favorite workspaces** field.
3. Select your workspaces from the list.
4. Select **Save changes**.

There's no limit to the number of workspaces you can favorite, but we recommend keeping this list short for convenience.

### Renaming workspaces

To rename your workspace:

1. Go to **Settings** > **App Settings**.
2. Hover over your workspace’s name and select <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Give your workspace a new name, then select <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Save**.

![The pencil icon appearing next to the workspace name.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Deleting workspaces and app instances

To delete your workspace or app instance:

1. Go to **Settings** > **App Settings**.
2. Select **Delete workspace** to delete the respective workspace, or select the trash can icon next to the respective app instance.

You cannot delete app instances or workspaces that are currently being used for targeting users or that have over 1,000 users. If you try to do so, you’ll receive an error message. To proceed and delete them, [create a Support case]({{site.baseurl}}/user_guide/administrative/access_braze/support/) that includes a dashboard link and the name of the app instance or workspace to be deleted.

{% alert warning %}
Be careful when deleting workspaces! After a workspace is deleted, it can’t be restored. 
{% endalert %}

![The App Settings page with a button to delete a workspace and a trash can icon to delete an app.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Frequently asked questions

### Should I create a new workspace when I'm releasing an updated app?

This depends on whether you're updating your app or creating an entirely new one.

#### Updating your app

If you're updating your app, you should separate the old and new versions by creating a new app instance within the same workspace. This way, you can effectively target users on the new version when you select that app during segmentation. If you want to message users who are on the old version, you can use filters to [target the previous app version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

If you create a new workspace, your users will exist in two places: the old workspace and the new workspace. They could also potentially have the same push token. This can lead to users receiving a marketing message intended for only old workspace users, even if they’ve already upgraded.

#### Releasing a new app

If you're releasing an entirely new app to the app store, you should create a new workspace. By creating a new workspace, all historical data and user profiles from the older app version won’t exist in this new workspace. So, after existing users upgrade to the new app version, they’ll have a new profile created without any of the behavioral data from the old app.

### I have multiple app instances in one workspace—how can I make sure to only target a single app with my message? {#singular-app}

To make sure your message only targets a specific app, add a segment that only targets users from your chosen app instances. This is especially important if a user might have two push tokens to different app instances in the same workspace. In this scenario, users could receive a notification for a different app than the one they're on. Not an ideal experience!

By default, a segment targets all apps and websites in the workspace. To set up a segment that only targets one app or website:

1. Create a segment with a meaningful name. At Braze, we use the format "All Users ({Name} {Platform})". For example, "All Users (Upon Voyage iOS)".
2. For **Apps and websites targeted**, select **Users from specific apps**.
3. In the **Specific apps** dropdown, select your app or site.

![Segment that is targeting users from specific apps.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

You can then add this segment to your message and begin further refining your audience with additional segments and filters if needed.

#### Campaigns

For campaigns, add your segment to the **Target Audiences** step of the composer.

#### Canvas

In Canvas, add your segment to your Message steps, in the **Delivery Validations** section. Delivery validations double-check that your audience meets your delivery criteria at message send. Remember to specify delivery validations for each Message step to make sure it will be delivered to the correct app. There's no need to segment at the entry level.

{% details Expand for steps in the original Canvas workflow %}

In the original Canvas workflow, add your segment to the Canvas component level in the **Audience** section. There's no need to segment at the entry level.

{% enddetails %}


