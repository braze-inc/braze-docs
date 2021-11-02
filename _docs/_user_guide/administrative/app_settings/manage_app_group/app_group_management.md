---
nav_title: App Group Management
article_title: App Group Management
page_order: 0
page_type: reference
description: "This reference article covers managing app groups in your Braze dashboard. "

---

# App group management

You can manage, segment, and communicate with multiple applications simultaneously all from the **Manage Settings** page in the Braze dashboard.

![Manage App Group Call Out][69]

App groups are designed to house versions of the same application across multiple platforms. Many Braze customers also use app groups to contain free and premium versions of their application on the same platform.

## Multiple apps in an app group

There is no limit to the number of apps that can exist in a single app group. The draw to have multiple apps under one app group can be enticing, as it lets you rate limit messaging across your entire app portfolio. However, as a best practice we suggest only putting different versions of the same (or very similar) apps together under one app group.

For example, you might have your iOS and Android versions of the same app in one app group, or your free and premium versions of the same app in one app group.

Whichever apps you choose to have in one app group will have their data aggregated—which will have a notable impact on the following filters in Braze:

- Last Used App
- First Used App
- Session Count
- Money Spent In-App
- Push Subscription (This becomes an all or none situation—if your users unsubscribe from one app, they are unsubscribed from all apps in the app group.)
- Email Subscription (This becomes an all or none situation, and can leave you open to compliance issues.)

This is not an exhaustive list.

## Administrating app groups

We recommend having multiple Braze users with admin permissions for a single app group. As a general rule, you want to ensure there are enough people with your organization to manage other users' permissions.

## Renaming or deleting your app group

To rename your app group, click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-pencil-alt" ></span>**Edit** on the [Settings][19] page.

To delete your App Group entirely from the Dashboard, click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-cog" ></span>**Settings** on the same page and select **Delete App Group**.

![appsettingsview1.png][70]

{% alert warning %}
Be careful when deleting app groups! Once an app group is deleted, it can't be restored.
{% endalert %}

[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[69]: {% image_buster /assets/img_archive/manageappgroupnavigation1.png %}
[70]: {% image_buster /assets/img_archive/appsettingsview1.png %}
