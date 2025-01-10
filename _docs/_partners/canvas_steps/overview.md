---
nav_title: Overview
article_title: Overview
description: "This reference article will cover how to use Braze Audience Sync to Facebook, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 0
Tool:
  - Canvas

---

# Audience sync overview

> The Braze Audience Sync feature helps you extend the reach of your campaigns to many of the top social and advertising technologies. Through [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), brands can dynamically and securely sync first-party user data into the advertising ecosystem to drive marketing and operational efficiencies.

## Use cases

- Targeting high-value users via owned and paid channels to drive incremental purchases or engagement.
- Creating lookalike audiences of your high-value users to optimize new user acquisition costs and conversions.
- Retargeting users with ads who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand.

## Feature availability

All Braze customers will immediately have access to Audience Sync to Google and Facebook. To unlock additional Audience Sync destinations including TikTok, Pinterest, Snapchat, or Criteo, you will need to purchase Audience Sync Pro. Contact your Braze account manager for more details.

## How it works

To use Audience Sync to Google or Facebook, connect your ad account by searching for the partner on the **Technology Partners** page.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

After connecting your ads account, you can create a Canvas with an Audience Sync step.

![][22]{: style="max-width:75%;"}

Next, select the partner to sync audiences.

![][19]{: style="max-width:85%;"}

For each partner, you’ll need to configure the following as part of your Audience Sync step: 
- Ad account
- Audience 
- Action to either add or remove users 
- Fields to match 

Keep in mind that Braze will sync users as soon as they enter the Audience Sync step within your Canvas. 

For each Audience Sync destination, the partner may have different requirements for which fields we can send. Refer to the specific partner documentation for more details. 

### Audience Sync Pro

To use an Audience Sync Pro partner including TikTok, Pinterest, Snapchat, or Criteo, you’ll be able to select your partners based on your Audience Sync Pro purchase allotments in the **Audience Sync Pro** section on the **Technology Partners** page.

![][5]{: style="max-width:75%;"}

First, select the partners you intend to use by selecting Select Partners. Each purchase of Audience Sync Pro will provide you 3 allotted Audience Sync Pro destinations, which will be available within each of your workspaces within your dashboard.

![][6]{: style="max-width:65%;"}

After selecting your Audience Sync Pro destinations, connect your selected partner ad account by clicking on the partner tile.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

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

![][2]

If you are collecting `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![A Canvas with an entry audience of "opted_in_marketing" equals "true".][1]

To learn more on how to comply with these Data Protection laws within the Braze platform, see [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/).

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}