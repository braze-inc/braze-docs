---
nav_title: App Group Configuration
article_title: App Group Configuration
page_order: 1
description: "This reference article covers app group configuration and how to create your app group."

---

# App group configuration

> This article covers how to create and set up an app group, and some best practices to keep in mind when grouping applications.

## What is an app group?

App groups are where you organize your apps. Think of each of these app groups as an individual title. For example, you should group the iOS and Android versions of the same app or the free and premium versions of the same app. Grouping these apps into the same app group allows for ease of navigation, segmentation, and messaging across both platforms.

## Create an app group

![][3]{: style="max-width:40%;float:right;margin-left:15px;"} 

### Step 1: Add your app group

1. Select the app group dropdown and click <i class="fas fa-plus"></i> **New App Group**.
2. Give your app group a name. 
   - You might want to adopt a naming convention so that others in your company can easily find your app group. For example: *FinanceApp - Production* and *FinanceApp - Development*.
3. Click **Add App Group** to confirm.

Next, you'll be taken to the **Settings** page. Generally, you can access this page by going to **Manage Settings** > **Settings**.

### Step 2: Add your apps

1. From the **Settings** page, click <i class="fas fa-plus"></i> **Add App**.
2. Give your app a name, and select the platform.
3. Click **Add App** to confirm.

After adding your app, you will have access to its API key, which you will need to complete SDK integration. You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android you will have four app instances within your app group and must use the appropriate API key that is generated for each app.

{% alert tip %}
The **Live SDK Version** displayed on the **Settings** page for a specific app is the highest app version with at least 5% of your total daily sessions and has least 500 sessions in the past day.
{% endalert %}

#### Add a testing app group

Braze recommends that you create a testing app group for integration and campaign testing. You can perform app testing by completely sandboxing certain users from your production instance. Create a new app group, and remember to switch your API codes so your production environments are not corrupted with false data. When you publish your application, be sure to change the API key that Braze is using to match that of your production app group rather than your testing app group.

## Multiple apps in a single app group

It can be enticing to group multiple apps under one app group in an attempt to optimize [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) across your entire app portfolio. However, as a best practice, we suggest only putting different versions of the same or very similar apps together under one app group. 

All apps in the same app group will have their data aggregated. This will have a notable impact on filters in Braze. This includes, but isn't limited to, these filters:

- Last Used App
- First Used App
- Session Count
- Money Spent
- Push Subscription
  - If your users unsubscribe from one app, they will be unsubscribed from all of your apps under the app group.
- Email Subscription
  - This can leave you open to compliance issues.

The aggregation of the data across dissimilar apps in the aforementioned filters is why we do not recommend housing substantially different apps within the same app group.

## Targeting a singular app

Any reference to a segment for targeting a singular app refers to using the check boxes under **Apps Used** within the segmentation tool. You must be using a segment that fits this criteria of selecting a singular app in order to be sure that you are indeed targeting a singular app.

### Campaigns

For campaigns, it is necessary to specify at the entry or at the **Target Audiences** step of building your campaign. You must use the segment that you have created using the checkbox filters in order to target only one of the apps in your app group.

### Original Canvas workflow

For the original Canvas workflow, it is necessary to specify the segment in the Canvas components in order to target a specific app when a user may have two push tokens to different apps in the same app group. Otherwise, the workflow will find the user and send to all available apps. It's not necessary to segment at the entry level.

### Canvas Flow

[Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#canvas-flow) works similarly to the original Canvas workflow for how users are sent from one step to the next. Use the Delivery Validations feature in the Message Step to segment the users again. You must specify the delivery validation at each message step to ensure it will deliver to the correct app. Similar to the original workflow, it's not necessary to segment at the entry level. 

## Relaunching your app

If users only need to update their app and you're not releasing a new app to the app store, you should not create a new app group if you plan to still message users on the older version.

By creating a new app group, all historical data and profiles from the older app version won't exist in this new app group. So, once existing users upgrade to the new app version, they’ll have a new profile created without any of the behavioral data from the old app. Additionally, this user will exist in the old app group and the new app group. They can also potentially have the same push token. This may lead to users receiving a marketing message intended for only old app group users, even if they’ve already upgraded.

To separate old and new apps, create a new app within the same app group. This way, you can effectively target users on the new version when you select that app during segmentation. If you want to message users who are on the old version, you can use [Liquid to select the old app and filter the previous app version](https://learning.braze.com/target-different-app-versions-with-liquid/929971).

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
