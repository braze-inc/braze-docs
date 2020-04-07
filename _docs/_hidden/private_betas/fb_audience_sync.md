---
nav_title: Audience Sync to Facebook
title: Audience Sync to Facebook
description: ""
permalink: "/audience_sync_facebook/"
hidden: true
---
{% alert note %}
This Audience Sync to Facebook feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Audience Sync to Facebook

Using the Braze Audience Sync to Facebook, brands can elect to add user data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation and more. Any criteria you’d normally use to trigger a message (Push, Email, SMS, Webhook, etc) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in Facebook via Custom Audiences.

Common use cases for syncing Custom Audiences include:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand
- Creating Lookalike Audiences to acquire new users more efficiently

Please note: this feature gives brands the option to control what specific first-party data is shared with Facebook. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. To learn more about our Braze data privacy policy, please click [here][0].

## Integration

### Integration Requirements

You will need to ensure that you have the following items created and/or completed prior to setting up your Facebook Audience Step in Canvas. 

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][3] | A centralized tool to manage your brand’s Facebook assets (i.e. ad accounts, pages, apps). |
| Facebook Ad Account | [Facebook][4] | An active Facebook ad account tied to your brand’s Business Manager.<br><br>Please ensure that your Facebook Business Manager admin has granted you admin permissions to the Facebook ad accounts you plan to use with Braze and that you have accepted your ad account terms and conditions. |
| Facebook App | [Facebook][5] | Ensure that you have created a Facebook app through [developers.facebook.com][2] and added the app to your Facebook Business Manager. <br><br>Please ensure that your Facebook Business Manager admin has granted you admin permissions to the Facebook apps you plan to use with Braze. |
| Facebook Custom Audiences Terms | [Facebook][6] | Accept Facebook’s Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze. |
| Facebook System User Access Token | [Facebook][7] | System users represent servers or software that make API calls to assets owned or managed by a Business Manager. <br><br>You will need to follow the instructions [here][1] to generate a system user access token.<br><br>See below for more details. |
| Facebook App Review | [Facebook][8] | See below for more details |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Facebook App Review Process

Customers looking to use the Audience Sync to Facebook step in Canvas will need to undergo Facebook’s App Review process for the following permissions. This ensures each customer is adhering to Facebook’s permission and authorization protocols when using the Facebook marketing API. 

- Ads Management Standard Access
- Ads Management
- Business Management

Granting these permissions enables Braze to sync data seamlessly into Facebook. The Audience Sync to Facebook feature will not have access to perform any of the following actions: 
- Manage or edit a customer’s Facebook Campaigns
- Manage or edit a customer’s Facebook page
- Manage or edit a customer’s Facebook business assets 

__Before you begin the Facebook App Review process__

1. Ensure that your team has created a Facebook app through the [Facebook Developer Console][9].<br><br>
2. Through the Facebook Developer Console, select the app you’d like to use, and then navigate to __Permissions and Features__ on the left-hand menu. Here you will see all of the available permissions.![audience sync][23]<br><br>For ads management and business management permissions, please ensure that you have completed [Business Verification][10] and sign the [supplemental terms][11]. In order to do this, you can go to your Business Settings within Facebook Business Manager. On the left-hand side, navigate to Business Info and then scroll down to the Business Contracts section.<br><br>![audience sync][22]
3. Once you have completed the additional requirements, you should be ready to submit your Facebook App Review. <br><br>
4. When your Facebook App Review has been approved, you will need to switch your app to “Live Mode” within the Facebook Developer Dashboard. 

### Facebook System User Access Token

You must create a Facebook system user access token in order to send requests to Facebook’s APIs. Authorizing with a system user access token will not be tied to a specific user, which in turn, will be more reliable long-term and significantly reduce the risk of audience sync disruptions for your brand.

In order to generate a system user access, please follow Facebook’s instructions [here][12]. 

Please note that when you create a system user access token, Facebook will only let you access it upon creation. If you generate a new system user access token, the old token will still be valid and have the same permissions as the new token unless it is revoked.

## Implementation Process
### Step 1: Authenticate System User Token

Enter an authenticated Facebook System User Token in the Technology Partners page of your Braze dashboard. Make sure that this System User Token has access to the ad accounts you want to use in Canvas.

![audience sync][21]{:height="200px"}

### Step 2: Add a Facebook Audience Step in Canvas

Add a step in your Canvas, select the dropdown at the top of the step, and select “Facebook Audience Step”.

![audience sync][20]{:height="200px"}

### Step 3: Sync Setup

Click on the “Custom Audience” button to open the step editor. Currently, functionality in the beta allows brands to create a new custom audience with users who flow through the step.

Select the desired ad account, enter a name for the new custom audience, and select the first-party user field data to send to Facebook. Facebook uses this information to determine who the user is in their database.

![audience sync][19]{:height="400px"}

Click the “Done” button to return back to your Canvas.

![audience sync][18]{:height="200px"}

### Step 4: Launch Canvas
![audience sync][17]{: style="float:right;max-width:35%;margin-left:15px;"}

Complete your Canvas. After launching the Canvas, the new custom audience will be created and users who flow through the Facebook Audience step will be passed into this custom audience in Facebook. Users will then advance to the next step in Canvas if there is one.

The History tab of the custom audience in the Facebook Audience Manager will reflect the number of users that were sent to the audience from Braze. If a user re-enters the step, they will be sent to Facebook again.

## Understanding Analytics

![audience sync][16]{: style="float:right;max-width:30%;margin-left:15px;"}

__Entered__: Number of users who entered this step to be synced to Facebook

__Proceeded to Next Step__: How many users advanced to the next step if there is one. All users will auto-advance. 0 if this is the last step in the Canvas branch.

__User Not Synced__: Number of users who were not synced to Facebook due to an error, after ~13 hours of retries. When there is an error, Canvas will retry the sync for up to ~13 hours. If the sync is still not possible at that point, the User Not Synced will be populated.<br>
__Potential causes of errors__:<br>
    - System user token is invalid<br>
    - Custom audience was deleted on Facebook

## Troubleshooting

{% details What if my App Review was rejected by Facebook? %}
- For common reasons around why your App Review was rejected, please go [here](https://developers.facebook.com/docs/apps/review/common-rejection-reasons/).
- If you think that your app should have been approved, go to your App Review request in the Facebook Developer Console and click on the Messenger icon to get in touch with a Facebook representative:<br>![audience sync]({% image_buster /assets/img/FB_audience_sync/FB1.png %}){:height="200px"}
{% enddetails %}

{% details What if my system user token is invalid? %}
- A Facebook system user token will be invalidated if it is revoked within your Facebook Business Manager. If it has been revoked, simply create a new Facebook system user access token and replace the invalid system user token in Braze. 
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
- Make sure your system user token is authenticated and has access to the desired ad accounts in Facebook Business Manager
- Make sure you have selected an ad account, entered a name for the new custom audience, and selected fields to match
- You may have reached the 500 custom audience limit on Facebook. Go into Facebook Audience Manager to delete some unneeded ones before creating any new Custom Audiences using Canvas.
{% enddetails %}

{% details How do I know if users have matched after passing users to Facebook? %}
- Facebook does not provide this information for privacy reasons.
{% enddetails %}

[0]: https://www.braze.com/privacy
[1]: https://developers.facebook.com/docs/audience-network/guides/reporting/system-user/
[2]: https://developers.facebook.com/
[3]: https://www.facebook.com/business/help/113163272211510
[4]: https://www.facebook.com/business/help/910137316041095
[5]: https://developers.facebook.com/docs/apps
[6]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[7]: https://developers.facebook.com/docs/audience-network/guides/reporting/system-user/
[8]: https://developers.facebook.com/docs/apps/review/
[9]: http://developer.facebook.com/
[10]: https://developers.facebook.com/docs/apps/review/#business-verification
[11]: https://developers.facebook.com/docs/apps/review/#supplemental-terms
[12]: https://developers.facebook.com/docs/audience-network/guides/reporting/system-user/
[13]: https://developers.facebook.com/docs/apps/review/common-rejection-reasons/
[15]: {% image_buster /assets/img/FB_audience_sync/FB1.png %}
[16]: {% image_buster /assets/img/FB_audience_sync/FB2.png %}
[17]: {% image_buster /assets/img/FB_audience_sync/FB3.png %}
[18]: {% image_buster /assets/img/FB_audience_sync/FB4.png %}
[19]: {% image_buster /assets/img/FB_audience_sync/FB5.png %}
[20]: {% image_buster /assets/img/FB_audience_sync/FB6.png %}
[21]: {% image_buster /assets/img/FB_audience_sync/FB7.png %}
[22]: {% image_buster /assets/img/FB_audience_sync/FB8.png %}
[23]: {% image_buster /assets/img/FB_audience_sync/FB9.png %}