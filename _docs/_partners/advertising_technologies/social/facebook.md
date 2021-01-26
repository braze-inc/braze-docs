---
nav_title: Facebook
alias: /partners/facebook/
description: "This article outlines the partnership between Braze and Facebook, a leading social platform for brands to reach and engage with their customers."
page_type: partner
---

# Facebook Audience Export

Braze provides the ability to manually export your users from the Braze Segments page. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

Common use cases for exporting Facebook Custom Audiences include:
- Retarget users at specific points within their lifecycle
- Create exclusion targeting lists
- [Lookalike Audiences][4] to acquire new users more efficiently
<br><br>

{% alert note %}
Facebook Audience Export uses the __User Access Token__ to authorize requests.<br>
If you are using this feature alongside the [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) feature (currently in Beta), Braze will default to using the more reliable __System User Token__ that you have already generated, to authorize requests.
{% endalert %}

## Prerequisites

{% raw %}
Requirement   |Origin| Description
--------------|------|-------------
Facebook Business Manager|[Facebook][1]| A centralized tool to manage your brand's Facebook assets (e.g. ad accounts, pages, apps).|
Facebook ad Account|[Facebook][2]| An active Facebook ad account tied to your brand's Business Manager that you want to use your Custom Audiences from Braze. <br> Please ensure that your Facebook Business Manager admin has granted you admin permissions to the Facebook ad accounts you plan to use with Braze and that you have accepted your ad account terms and conditions.|
Facebook Custom Audiences Terms|[Facebook][3]| You have accepted Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endraw %}

## Integration

### Activate Facebook

In the Braze dashboard, go to Technology Partners and select Facebook. In the Facebook Audience Export module, click <b>Connect Facebook</b>.

![Activate Facebook][6]

A Facebook dialog window will appear to authorize Braze to create Custom Audiences into your Facebook ad accounts and retrieve your associated Facebook app IDs.

![Facebook Dialog][7]

Make sure that you've accepted [Facebook's Custom Audience Terms][3] for your personal user account __and__ Facebook ad account before proceeding. Once you've successfully linked your Facebook accounts, you should see a "Connected" status in the Facebook Audience Export module. You should also see the Facebook ad account names, your personal account, and the associated account IDs listed. 

![Facebook Connected][8]

At any point in time, you will also be able to disconnect your Facebook account from Braze by simply clicking the <b>Disconnect Facebook</b> button.

### Exporting Your Users into Facebook

Braze's Facebook Audience Export is accessible through the Segments page. Simply click on the gear next to the segment that you'd like to export. Then click on <b> Export as Facebook Audience </b>.

If you haven't already activated Facebook within Braze, it will prompt you to go to the Facebook Technology Partners page of the dashboard. If you have already activated Facebook through Technology Partners > Facebook, you will be able to select the user field to export and a dropdown to select your Facebook ad account.

There are 3 possible user fields you can export:  

- Email
- Device IDFA
- Phone number

{% alert note %}
You can only select one user field within a single export. If you choose more than 1 data type, Braze will create a separate custom audience for each.
{% endalert %}

Once you have selected the user field, click on the export button. Similar to CSV exports, you will receive an email when the segment has finished exporting into Facebook.

You can view the custom audience on the [Facebook Ads Manager][13].

#### Lookalike Audiences

Once you've successfully exported a segment as a Facebook Audience, you can create additional groups using Facebook's [Lookalike Audiences][4]. This feature looks at demographics, interests, and other attributes of your chosen audience and creates a new audience of people with similar attributes.

## Facebook Audience Export FAQ

{% details What if I can't access any Facebook ad accounts within Braze? %}
- Please ensure that you work with your brand's Facebook Business Manager admin to get invited to Facebook Business Manager and become an admin for the ad accounts you wish to sync with Facebook.
{% enddetails %}

{% details Can I see the exact users that were successfully added to a Custom Audience? %}
- Facebook does **not** allow this for user privacy reasons. Learn more [here](https://www.facebook.com/business/help/112061095610075).
{% enddetails %}

{% details Why can't I see the Custom Audience size? %}
- Due to recent user privacy implications, Facebook announced that they will [stop showing audience reach estimates using Custom Audience targeting](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% enddetails %}

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb_activate.png %}
[7]: {% image_buster /assets/img/fb_dialog.png %}
[8]: {% image_buster /assets/img/fb_connected.jpg %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
