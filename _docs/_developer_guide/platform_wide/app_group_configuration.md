---
nav_title: Workspace Configuration
article_title: Workspace Configuration
page_order: 1
description: "This reference article covers single and multi-workspace configuration, how to create your workspace, and how to target and relaunch your app."

---

# Workspace configuration

> This article covers how to create and set up an workspace, and some best practices to keep in mind when grouping applications.

## What is an workspace?

Workspaces are where you organize your apps. Think of each of these workspaces as an individual title. For example, you should group the iOS and Android versions of the same app or the free and premium versions of the same app. Grouping these apps into the same workspace allows for ease of navigation, segmentation, and messaging across both platforms.

## Create an workspace

![][3]{: style="max-width:40%;float:right;margin-left:15px;"} 

### Step 1: Add your workspace

1. Select the workspace dropdown and click <i class="fas fa-plus"></i> **New workspace**.
2. Give your workspace a name. 
   - You might want to adopt a naming convention so that others in your company can easily find your workspace. For example: *FinanceApp - Production* and *FinanceApp - Development*.
3. Click **Add workspace** to confirm.

Next, you'll be taken to the **Settings** page. Generally, you can access this page by going to **Manage Settings** > **Settings**.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find this page under **Settings** > **Setup and Testing** > **App Settings**.
{% endalert %}

### Step 2: Add your apps

1. From the **Settings** page, click <i class="fas fa-plus"></i> **Add App**.
2. Give your app a name, and select the platform.
3. Click **Add App** to confirm.

After adding your app, you will have access to its API key. The API key is used when making requests between your app and the Braze API. The API key is also important for integrating the Braze SDK with your app. 

You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android, create four app instances within your workspace (Free iOS app, free Android app, pro iOS app, and pro Android app). This will give you four API keys to use, one for each app instance.

{% alert tip %}
The **Live SDK Version** displayed on the **Settings** page for a specific app is the highest app version with at least 5% of your total daily sessions and has least 500 sessions in the past day.
{% endalert %}

#### Add a testing workspace

Braze recommends that you create a testing workspace for integration and campaign testing. You can perform app testing by completely sandboxing certain users from your production instance. Create a new workspace, and remember to switch your API codes so your production environments are not corrupted with false data. When you publish your application, be sure to change the API key that Braze is using to match that of your production workspace rather than your testing workspace.

## Multiple apps in a single workspace

It can be enticing to group multiple apps under one workspace in an attempt to optimize [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) across your entire app portfolio. However, as a best practice, we suggest only putting different versions of the same or very similar apps together under one workspace. 

All apps in the same workspace will have their data aggregated. This will have a notable impact on filters in Braze. This includes, but isn't limited to, these filters:

- Last Used App
- First Used App
- Session Count
- Money Spent
- Push Subscription
  - If your users unsubscribe from one app, they will be unsubscribed from all of your apps under the workspace.
- Email Subscription
  - This can leave you open to compliance issues.

The aggregation of the data across dissimilar apps in the aforementioned filters is why we do not recommend housing substantially different apps within the same workspace.

## Targeting a singular app

Any reference to a segment for targeting a singular app refers to using the check boxes under **Apps Used** within the segmentation tool. You must be using a segment that fits this criteria of selecting a singular app in order to be sure that you are indeed targeting a singular app.

### Campaigns

For campaigns, it is necessary to specify at the entry or at the **Target Audiences** step of building your campaign. You must use the segment that you have created using the checkbox filters in order to target only one of the apps in your workspace.

### Original Canvas workflow

{% alert important %}
As of February 28, 2023, you can no longer create or duplicate Canvases using the original editor. This article is available for reference to understand segments and targeting in the original editor.<br><br>Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It's an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

For the original Canvas workflow, it is necessary to specify the segment in the Canvas components in order to target a specific app when a user may have two push tokens to different apps in the same workspace. Otherwise, the workflow will find the user and send to all available apps. It's not necessary to segment at the entry level.

### Canvas Flow

[Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#canvas-flow) works similarly to the original Canvas workflow for how users are sent from one step to the next. Use the Delivery Validations feature in the Message Step to segment the users again. You must specify the delivery validation at each message step to ensure it will deliver to the correct app. Similar to the original workflow, it's not necessary to segment at the entry level. 

## Relaunching your app

If users only need to update their app and you're not releasing a new app to the app store, you should not create a new workspace if you plan to still message users on the older version.

By creating a new workspace, all historical data and profiles from the older app version won't exist in this new workspace. So, once existing users upgrade to the new app version, they'll have a new profile created without any of the behavioral data from the old app. Additionally, this user will exist in the old workspace and the new workspace. They can also potentially have the same push token. This may lead to users receiving a marketing message intended for only old workspace users, even if they've already upgraded.

To separate old and new apps, create a new app within the same workspace. This way, you can effectively target users on the new version when you select that app during segmentation. If you want to message users who are on the old version, you can use [Liquid to select the old app and filter the previous app version](https://learning.braze.com/target-different-app-versions-with-liquid/929971).

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
