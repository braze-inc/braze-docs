---
nav_title: About Audience Sync
article_title: About Audience Sync
alias: /partners/about_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to Facebook, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 0
Tool:
  - Canvas

---

# About Audience Sync

> The Braze Audience Sync feature helps you extend the reach of your campaigns to many of the top social and advertising technologies. Through [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), brands can dynamically and securely sync first-party user data into the advertising ecosystem to drive marketing and operational efficiencies.

## Feature availability

All Braze customers will immediately have access to Audience Sync to Google and Facebook. To unlock additional Audience Sync destinations including TikTok, Pinterest, Snapchat, or Criteo, you will need to purchase Audience Sync Pro. Contact your Braze account manager for more details.

## Use cases

- Targeting high-value users using owned and paid channels to drive incremental purchases or engagement.
- Creating lookalike audiences of your high-value users to optimize new user acquisition costs and conversions.
- Retargeting users with ads who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand.

## Overview

<style>
table td {
    word-break: break-word;
}
</style>

| Destination | Time for destination to match audience members | Rate limit | Lookalike or actalike | Tips |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Up to 24 hours | 250,000 requests per minute. Batched every 5 seconds with an auto-retry based on Google feedback. | Yes | {::nomarkdown}<ul><li>Criteo supports up to 1,000 ad audiences.</li><li>The minimum audience size is 500, and the recommend is over 20,000.</li></ul>{:/} |
| [Facebook or Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Up to 24 hours | 190,000 ad accounts per hour | Yes | {::nomarkdown}<ul><li>Facebook supports up to 500 ad audiences.</li><li>Facebook requires audiences to be at least 1,000 users.</li></ul>{:/} |
| [Google Ads or YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Between 6 to 12 hours | Batched every 5 seconds with an auto-retry based on Google feedback | No | {::nomarkdown}<ul><li><b>Customer match:</b> Use either mobile ad, or email address or phone number.</li><li>Google Audiences require at least 5,000 users to start serving ads.</li><li>The audience size will show as zero until there are at least 1,000 users.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 hours | LinkedIn processes 10 queries per second and 100,000 users per request. Braze batches users every 5 seconds. | AI predictive audiences | {::nomarkdown}<ul><li>The minimum audience size is 300 members with location targeting taken into consideration.</li><li>LinkedIn shows match the rate in the Braze dashboard.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Between 24 and 48 hours | Pinterest processes 7 queries per second and 1,900 users per request. Braze batches users every 5 seconds. | Yes | Pinterest audiences require at least 100 users. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/A | Snapchat processes 10 queries per second and 100,000 users per request. Braze batches users every 5 seconds. | Yes | Snapchat supports up to 1,000 ad audiences. |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Between 24 and 48 hours | TikTok processes 50 queries per second and 10,000 users per request. Braze batches users every 5 seconds. | Yes | {::nomarkdown}<ul><li>TikTok supports up to 400 ad audiences.</li><li>TikTok audiences require at least 1,000 users to start serving ads.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>When the rate limit is reached, Braze will retry syncs for 13 hours.</sup>

## How it works

To use Audience Sync to Google or Facebook, connect your ad account by searching for the partner on the **Technology Partners** page.

![Facebook technology partner.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Ads technology partner.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

After connecting your ad account, you can create a Canvas with an Audience Sync step.

![Canvas component menu to add the Audience Sync step to the user journey.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Next, select the partner to sync audiences.

![Option to select your audience sync partner in the Audience Sync step.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

For each partner, you’ll need to configure the following as part of your Audience Sync step: 

- Ad account
- Audience 
- Action to either add or remove users 
- Fields to match 

Keep in mind that Braze will sync users as soon as they enter the Audience Sync step within your Canvas. 

For each Audience Sync destination, the partner may have different requirements for which fields we can send. Refer to the specific partner documentation for more details. 

### Audience Sync Pro

To use an Audience Sync Pro partner including TikTok, Pinterest, Snapchat, or Criteo, you’ll be able to select your partners based on your Audience Sync Pro purchase allotments in the **Audience Sync Pro** section on the **Technology Partners** page.

![Audience Sync Pro with no partners selected yet.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

First, select the partners you intend to use by selecting Select Partners. Each purchase of Audience Sync Pro will provide you 3 allotted Audience Sync Pro destinations, which will be available within each of your workspaces within your dashboard.

![Option to select up to three partners to connect to Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

After selecting your Audience Sync Pro destinations, connect your selected partner ad account by clicking on the partner tile.

![An example of Snapchat and TikTok selected as partners for Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchat Audience Sync settings with the message: "You successfully connected 1 Snapchat account".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Lastly, create your Audience Sync step in Canvas using this Audience Sync Pro destination.

### Audience Sync error emails

If the error is related to the overall partner integration (such as an authorization issue), an email is sent to the user who connected the integration. If that user no longer exists, then the administrators will receive the emails. 

If the error is related to issues with the Audience Sync component (such as "Audience Does Not Exist") in Canvas, an email is sent to the user who set up the Canvas. If that user no longer exists, then it falls back to the company administrator.

To configure who will receive these emails, contact your customer success manager to add recipients under **Notification Preferences**. Because this feature will change the current behavior, you'll need to immediately add recipients to this new notification preference as Braze doesn't opt-in anyone by default, and to make sure no error emails are missed.

## Data privacy considerations

{% alert important %}
This documentation is not intended to provide, nor may it be relied upon as providing legal advice. The use of Audience Sync is subject to specific legal requirements. To ensure that you are using it in compliance with all applicable laws, you should seek the advice of your legal counsel.
{% endalert %}

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options.

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the "Ads Tracking Enabled" filter. Select the value as `true` to only send users into Audience Sync destinations where they have opted in.

![A Canvas with an entry audience of "Ad Tracking Enabled is true".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

If you are collecting `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![A Canvas with an entry audience of "opted_in_marketing equals true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

To learn more on how to comply with these Data Protection laws within the Braze platform, see [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/).

## Managing consent for ad targeting

As the advertiser, it is your responsibility to manage consent for ad tracking or targeting of your users.

To send ads to your users, you must comply with all applicable laws and regulations, and the ad platform's policies and requirements. Only use Braze to target and sync users where you have obtained their consent. 

To keep your audience lists in these ad platforms up-to-date and remove users who have revoked their consent, set up a Canvas to remove users from these existing audience lists using an Audience Sync step.


