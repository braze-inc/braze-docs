---
nav_title: Facebook
alias: /partners/facebook/
hidden: true
description: "This article outlines the updated integration for Facebook Audience Exports through Segments."
---

{% alert note %}
This Facebook Audience Export feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Facebook

Facebook is a leading social platform for brands to reach and engage with their customers. Marketers and developers can utilize a plethora of tools, like Facebook Ads and the Facebook Developer Console, to make meaningful relationships with their customers.

Braze provides the ability to export custom audiences into Facebook Audiences through the Segments view within the Braze dashboard. This is a one-time audience export and will only create custom audiences into Facebook Audiences.

Common use cases for exporting custom audiences include:
- Retarget users at specific points within their lifecycle
- [Lookalike Audiences][4] to acquire new users more efficiently

## Prerequisites

{% raw %}
Requirement   |Origin| Description
--------------|------|-------------
Facebook Business Manager    |[Facebook][1]| A centralized tool to manage your brand's Facebook assets (i.e. ad accounts, pages, apps).
Facebook ad account    |[Facebook][2]| An active Facebook ad account tied to your brand's Business Manager that you want to use your custom audiences from Braze.
Facebook Custom Audiences Terms    |[Facebook][3]| You have accepted Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze.
{% endraw %}

## Integration

### Activate Facebook

In the Braze dashboard, go to Technology Partners and select Facebook. In the Facebook Audience Export module, click <b>Connect Facebook</b>.

![Activate Facebook][6]

A Facebook dialog window will appear to authorize Braze to create custom audiences into your Facebook ad accounts and retrieve your associated Facebook app IDs if you plan to use the Facebook user ID when exporting your audiences (this is optional).

![Facebook Dialog][7]

Once you have successfully linked your Facebook account, you should see a "Connected" status in the Facebook Audience Export module. You should also see the Facebook ad account names and their associated ad account IDs listed.

![Facebook Connected][8]

At any point in time, you will also be able to disconnect your Facebook account from Braze by simply clicking the <b>Disconnect Facebook</b> button.

### Exporting Your Users into Facebook

Braze's Facebook Audience Export is accessible through the Segments page. Simply click on the gear next to the segment that you'd like to export. Then click on <b> Export as Facebook Audience </b>.

If you haven't already activated Facebook within Braze, it will prompt you to go to the Facebook Technology Partners page of the dashboard. If you have already activated Facebook through Technology Partners > Facebook, you will be able to select the user field to export and a dropdown to select your Facebook ad account.

There are 4 possible user fields you can export:  

- Email
- Device IDFA
- Phone number
- Facebook user ID (UID)
  - If you would like to export the Facebook UID you will need to enable Facebook social data tracking natively through the  Braze's [iOS][10] and [Android][11] SDKs.
  - A [Facebook Application ID][12] is required if you are looking to export Facebook UIDs. After you are successfully collecting your users' Facebook UIDs through the Braze's SDKs, you will be able to select <b> Facebook UID </b> as an export field and select which Facebook Application IDs to include within the export modal.

{% alert note %}
You can only select one user field within a single export. If you choose more than 1 data type, Braze will create a separate custom audience for each.
{% endalert %}

Once you have selected the user field, click on the export button. Similar to CSV exports, you will receive an email when the segment has finished exporting into Facebook.

You can view the custom audience on the [Facebook Ads Manager][13].

#### Lookalike Audiences

Once you've successfully exported a segment as a Facebook Audience, you can create additional groups using Facebook's [Lookalike Audiences][14]. This feature looks at demographics, interests, and other attributes of your chosen audience and creates a new audience of people with similar attributes.

## Facebook Audience Export FAQ

- Can I see the exact users that were successfully added to a Custom Audience?
  - Facebook does **not** allow this for user privacy reasons. Learn more [here][14].

- Why can't I see the Custom Audience size?
  - Due to recent user privacy implications, Facebook announced that they will [stop showing audience reach estimates using Custom Audience targeting][16].


[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[5]: https://developers.facebook.com/docs/marketing-apis
[6]: {% image_buster /assets/img/fb_activate.png %}
[7]: {% image_buster /assets/img/fb_dialog.png %}
[8]: {% image_buster /assets/img/fb_connected.png %}
[10]: https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/social_data_tracking/#social-data-tracking
[11]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/social_data_tracking/
[12]: https://developers.facebook.com/docs/apps/#app-id
[13]: https://www.facebook.com/ads/manager/audiences/manage/
[14]: https://www.facebook.com/business/help/112061095610075
[15]: https://developer.android.com/training/articles/user-data-ids.html
[16]: https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923
