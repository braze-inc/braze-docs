---
nav_title: Audience Sync to Google
article_title: Canvas Audience Sync to Google
alias: /google_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to Google, to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
---

# Audience Sync to Google 

The Braze Audience Sync to Google integration enables brands to extend the reach of their cross-channel customer journeys to Google Search, Google Shopping, Gmail, YouTube, and Google Display. Using your first-party customer data, you can securely deliver ads based upon dynamic behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (e.g., push, email, SMS, etc.) as part of a Braze Canvas can be used to trigger an ad to that user via Google's [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en).

Common use cases for syncing Custom Audiences include:
- Targeting high-value users via multiple channels to drive purchases or engagement.
- Retargeting users who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand.
- Creating similar audiences to acquire new users more efficiently.

{% alert note %}
This feature gives brands the option to control what specific first-party data is shared with Google. At Braze, the integrations with which you can and cannot share your first-party data are given the utmost consideration. To learn more about our Braze data privacy policy, please click [here](https://www.braze.com/privacy).
{% endalert %}

## Integration

### Integration requirements

You will need to ensure that you have the following items created and/or completed before setting up your Google Audience Step in Canvas.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Google Ads Account | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | An active Google ads account for your brand.<br><br>If you are looking to share an audience across multiple managed accounts, you can upload your audiences into your [manager account](https://support.google.com/google-ads/answer/6139186). |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match is not available for all advertisers.<br><br>__To use Customer Match, your account must have:__<br>• A good history of policy compliance<br>• A good payment history<br>• At least 90 days history in Google Ads<br>• More than USD 50,000 total lifetime spend. For advertisers whose accounts are managed in currencies other than USD, your spend amount will be converted to USD using the average monthly conversion rate for that currency.<br><br>If your account does not meet the above criteria, then your account is currently ineligible to use Customer Match.<br><br>Please chat with your Google Ads Rep for more guidance on Customer Match availability for your account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Implementation process
### Step 1: Connect Google account
To get started, go to the **Google Ads** tab in the **Technology Partners** page and select __Connect Google Ads__. 

![Google Sync][1]

You'll then be prompted with a modal to select the email associated with your Google Ads account and then grant Braze access to your Google Ads account.

Note that Braze will only be managing your audiences. 

![Google Sync][2]{: style="max-width:30%;"}  ![Google Sync][3]{: style="max-width:29%;"}

Once you have successfully connected your Google Ads account, you will be taken back to your Google Ads partner page in Braze. 

![Google Sync][4]

{% alert important %}
If you plan to export iOS IDFA or Google Advertising IDs within your audience sync, Google requires your iOS app ID and Android app ID within the requests. Within the Google Audience Sync module, select __Add Mobile Advertising IDs__, input your iOS app ID and Android app ID (app package name), and save each.

![Google Sync]({% image_buster /assets/img/google_sync/google_sync5.png %})
{% endalert %}

### Step 2: Add a Google Audience step in Canvas

Add a step in your Canvas, select the dropdown at the top of the step, and select the __Google Audience__ step.

![Google Sync][6]

### Step 3: Sync setup

Click on the __Custom Audience__ button to open the step editor.

Select the desired Google ad account. Under the __Choose a New or Existing Audience__ dropdown, type in the name of a new or existing audience. 

{% tabs %}
{% tab Create a New Audience %}
__Create a New Audience__<br>
Enter a name for the new custom audience, select __Add Users to Audience__ and select the first-party user field data to send to with your audience. You can choose either: 
- __Customer Contact Info__ which will contain your users' email and/or phone numbers if they exist in Braze
- __Mobile Advertiser ID__ which you will then need to select either iOS IDFA or Android GAID   

Next, save your audience by clicking the __Create Audience__ button at the bottom of the step editor.

![Google Sync][7]

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode. 

![Google Sync][9]

When you launch a Canvas with a new audience, Braze will create a new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Google Audience Step. 

{% alert important %}
Given Google's Customer Match requirements, you cannot have customer contact info and mobile advertiser IDs in the same customer lists. Google Customer Match will then use this information to determine who is targetable within Google Search, Google Display, YouTube, and Gmail. For more details around Google Customer Match requirements, please review their [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}
__Sync with an Existing Audience__<br>
Braze also offers the ability to either add or remove users from existing Google customer lists to ensure that these audiences are up-to-date. To sync with an existing audience, select an existing custom audience to sync to and then choose whether you want to __Add to the audience__ or __Remove from the audience__. Braze will then either add or remove users in near real-time as they enter the Google Audience Step. 

Once you've configured your Google Audience step, select __Done__. Your Google Audience step will include details about the new audience.

![Google Sync][8]

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas

Complete the remainder of your user journey within Canvas and then launch! If you have opted to create a new audience, Braze will first create the audience within Google and then add users as they reach this step in your Canvas. If you have selected to add or remove users from an existing audience, Braze will either add or remove users when they reach this step in their user journey.

Users will then advance to the next step of the Canvas if there is one or exit the Canvas if it is the last step. 

## User syncing and rate limit considerations

As users reach the Audience Sync Step, Braze will sync these users in near real-time while respecting Google Ads API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to Google. 

Once a customer is close to reaching the Google Ads API rate limit, Google will provide feedback back to Braze around retry recommendations. If a Braze customer reaches their rate limit, Braze the Canvas will retry the sync for up to &#126;13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics 
<br>
__Entered__: Number of users who entered this step to be synced to Google.

__Proceeded to Next Step__: How many users advanced to the next step if there is one. All users will auto-advance. 0 if this is the last step in the Canvas branch.

__Users Synced__: Number of users who have successfully been synced to Google.

__User Not Synced__: Number of users that have not been synced due to missing fields to match.

__Users Errored__: Number of users who were not synced to Google due to an error, after &#126;13 hours of retries. For specific errors, like Google Ads API service disruptions, Canvas will retry the sync for up to &#126;13 hours. If the sync is still not possible at that point, the User Not Synced will be populated.

__Users Pending__: Number of users currently being processed by Braze to sync to Google.

__Exited Canvas__: Number of users who have exited the Canvas. This occurs when the last step in a Canvas is a Google step.

## Troubleshooting
{% details Why am I unable to select multiple fields to match in my Google Audience Step configuration? %}
Google Customer Match has strict requirements around how these audiences are formatted and what customer information is included. Specifically, mobile advertiser IDs need to be uploaded separately from customer contact info (i.e., email and phone number). Please refer to [Google's Customer Match documentation](https://support.google.com/google-ads/answer/7659867?hl=en#undefined) for more details. 
{% enddetails %}

{% details How long will it take for my audiences to sync in Google? %} 
It can take anywhere between 6 to 12 hours for an audience to be synced into Google. 
{% enddetails %}

{% details I've synced an audience, but the audience size in Google is zero. %}
For privacy purposes, the user list size will show as zero until the list has at least __1,000 members__. After that, the size will be rounded to the two most significant digits.
{% enddetails %}

{% details I've synced an audience into Google, but my ads are not serving. %}
Check that your audiences contain at least __5,000__ users to ensure that ads start serving. 
{% enddetails %}

[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[7]: {% image_buster /assets/img/google_sync/google_sync7.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[9]: {% image_buster /assets/img/google_sync/google_sync9.png %}