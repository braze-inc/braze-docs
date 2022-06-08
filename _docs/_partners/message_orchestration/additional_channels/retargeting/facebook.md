---
nav_title: Facebook
article_title: Facebook Audience Export
alias: /partners/facebook/
description: "This article outlines the partnership between Braze and Facebook, a leading social platform for brands to reach and engage with their customers."
page_type: partner
search_tag: Partner
page_order: 1

---

# Facebook Audience export

The Braze and Facebook integration allows you to manually export your Braze users Segments to Facebook to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

Common use cases for exporting Facebook Custom Audiences include:
- Retarget users at specific points within their lifecycle
- Create exclusion targeting lists
- [Lookalike Audiences][4] to acquire new users more efficiently
<br><br>

{% alert note %}
Facebook audience export uses the **User Access Token** to authorize requests.<br><br>
If you are using this feature alongside the [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) feature (currently in Beta), Braze will default to using the more reliable **System User Token** that you have already generated, to authorize requests.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| [Facebook Business Manager][1] | A centralized tool to manage your brand's Facebook assets (e.g., ad accounts, pages, apps). |
| [Facebook ad account][2] | An active Facebook ad account tied to your brand's business manager that you want to use Braze custom audiences with.<br><br>Ensure that your Facebook business manager admin has granted you admin permissions to the Facebook ad accounts you plan to use with Braze, and that you have accepted your ad account terms and conditions. Otherwise, you will not be able to access any Facebook ad accounts within Braze. |
| [Facebook Custom Audiences Terms][3]| You must accept Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze.|
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Connect to Facebook

In the Braze dashboard, go to **Technology Partners** and select **Facebook**. In the Facebook Audience Export module, click **Connect Facebook**.

![Facebook technology partners page in the Braze platform.][6]{: style="max-width:70%;"}

A Facebook oAuth dialog window will appear to authorize Braze to create Custom Audiences into your Facebook ad accounts.

![The first facebook dialog box prompting to "Connect as X", where X is your Facebook username.][8]{: style="max-width:30%;"}  ![The second Facebook dialog box prompting for permission to manage ads for your ad accounts.][7]{: style="max-width:40%;"}

Once you have linked Braze to your Facebook account, you will then be able to select which ad accounts you would like to sync within your Braze app group. 

![A list of available ad accounts you can connect to Facebook.][9]{: style="max-width:70%;"}

Once you have successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![An updated version of the Facebook technology partners page showing the ad accounts successfully connected.][10]{: style="max-width:70%;"}

Your Facebook connection will be applied at the Braze app group level. If your Facebook admin removes you from your Facebook Business Manager or access to the connected Facebook accounts, Braze will detect an invalid token. As a result, your active Canvases using Facebook audience steps will show errors, and Braze will not be able to sync users. 

{% alert important %}
For customers that have previously undergone the Facebook app review process for [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) and [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), your system user token will still be valid for the Facebook audience step. You will not be able to edit or revoke the Facebook system user token through the Facebook partner page. Instead, you can connect your Facebook account to replace your Facebook system user token within your Braze app group. 

<br><br>The new Facebook oAuth configuration will also apply to [Facebook exports via segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites). 
{% endalert %}

### Exporting your users into Facebook

Braze's Facebook audience export is accessible through the **Segments** page. Click on the gear next to the segment you'd like to export. Then click on **Export as Facebook Audience**.

![A list of Braze segments. For the first segment, the setting symbol is selected and the "Export as Facebook Audience" button is shown.][11]

If you haven't already activated Facebook within Braze, it will prompt you to go to the Facebook Technology Partners page in the dashboard. If you have already activated Facebook through **Technology Partners > Facebook**, you will be able to select the user field to export, and a dropdown to select your Facebook ad account will show.

There are three possible user fields you can export:  

- Email
- Device IDFA
- Phone number

{% alert note %}
You can only select one user field within a single export. If you choose more than one data type, Braze will create a separate custom audience for each.
{% endalert %}

Once you have selected the user field, click on the **Export** button. Like CSV exports, you will receive an email when the segment has finished exporting into Facebook.

You can view the custom audience on the [Facebook Ads Manager][13].

{% alert important %}
Due to user privacy reasons, Facebook doesn't allow you to see:

- The exact users that were successfully added to a Custom Audience. [Learn more.](https://www.facebook.com/business/help/112061095610075)
- The size of the Custom Audience. [Learn more.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Lookalike Audiences

Once you've successfully exported a segment as a Facebook Audience, you can create additional groups using Facebook's [Lookalike Audiences][4]. This feature looks at your chosen audience's demographics, interests, and other attributes and creates a new audience of people with similar attributes.

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
