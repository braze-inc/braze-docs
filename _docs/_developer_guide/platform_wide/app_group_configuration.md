---
nav_title: App Group Configuration
article_title: App Group Configuration
page_order: 1
description: "This reference article covers app group configuration and how to create your app group."

---

# App group configuration

Braze organizes your apps via "App Groups." Think of each of these app groups as an individual title. For example, you should group the iOS and Android versions of the same application or a free and paid versions. These two apps should be in the same group to allow for ease of navigation, segmentation, and messaging across both platforms.

## Creating your app group in "my apps"

### Step 1: click on the "<i class='icon-plus'> </i>  add app group" button in the sidebar

![Add App Group][3]

Type the name of your app group into the form.

Once you have created your app group, you will be taken to the settings page. Generally, you can access this page by navigating to the Apps tab at the top of the page and pressing the <i class='icon-cog'></i> icon on the sidebar.

![Braze Settings][4]

### Step 2: add your apps

Using the form at the top right of your screen, select your platform, type in the name of your app, and click "Add App"

- After adding your app, you will have access to its API key, which you will need to complete SDK integration.
    - You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android you will have 4 app instances within your app group and must use the appropriate API key that is generated for each app.

![Braze API Input][5]

### Step 3: add a testing app group

Braze recommends that you create a "Testing App Group" for integration and campaign testing. The App Group feature can also be utilized for app testing by completely sandboxing certain users from your production instance. Simply create a new app group and remember to switch your API codes so your production environments are not corrupted with false data. When you publish your application, be sure to change the API key that Braze is using to match that of your "Production App Group" rather than your "Testing App Group"

## Multiple apps in a single app group

The draw to have multiple apps under one App Group can be enticing as it can lead to the ability to rate limit messaging across your entire app portfolio. However, as a best practice, we suggest only putting different versions of the same or very similar apps together under one app group. For example, your iOS and Android versions of the same app or your free and premium versions of the same app.

Whichever apps you choose to have in one app group will have their data aggregated which will have a notable impact on filters in Braze:

- Last Used App
- First Used App
- Session Count
- Money Spent
- Push subscription (this becomes an all or none situation, if your users unsubscribe from one app they will be unsubscribed from all of your apps under the app group)
- Email subscription (this becomes an all or none situation and can leave you open to compliance issues)

This is not an exhaustive list. The aggregation of the data across dissimilar apps in filters like those listed above is why we do not recommend housing substantially different apps within the same app group.

## Managing app groups when relaunching your app

If users will simply have to update the app and it’s not a new app being released to the app store, you should not create a new app group if you plan to still message users on the older version.

By creating a new app group, all of the historical data and profiles from the older version of your app will not exist in this new app group. So, once existing users upgrade to the new app version, they’ll have a new profile created that does not contain any of the behavioral data from the old app. Additionally, this user will exist on both the old app group and the new app group and can potentially have the same push token. If this happens, it can lead to users receiving an “upgrade now” marketing message intended for only old app group users, even if they’ve already upgraded.

The best way to go about this if you want to separate the old vs. new app would be to create a new app within the same app group. This way, you can effectively target only users on the new version by selecting that app as you create your segments. If you did want to message users who are still on the old version, you can use [Liquid to select the old app and filter the previous app version](https://www.youtube.com/watch?v=Dv__RAUwamA).

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
[4]: {% image_buster /assets/img_archive/new_app_landing.png %} "Braze Settings"
[5]: {% image_buster /assets/img_archive/App_Setup_API.png %} "Braze API Input"
