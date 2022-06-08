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
This feature gives brands the option to control what specific first-party data is shared with Google. At Braze, the integrations with which you can and cannot share your first-party data are given the utmost consideration. To learn more about our Braze data privacy policy, click [here](https://www.braze.com/privacy).
{% endalert %}

## Integration

### Integration requirements

You will need to ensure that you have the following items created and/or completed before setting up your Google Audience Step in Canvas.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Google Ads Account | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | An active Google ads account for your brand.<br><br>If you are looking to share an audience across multiple managed accounts, you can upload your audiences into your [manager account](https://support.google.com/google-ads/answer/6139186). |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match is not available for all advertisers.<br><br>**To use Customer Match, your account must have:**<br>• A good history of policy compliance<br>• A good payment history<br>• At least 90 days history in Google Ads<br>• More than USD 50,000 total lifetime spend. For advertisers whose accounts are managed in currencies other than USD, your spend amount will be converted to USD using the average monthly conversion rate for that currency.<br><br>If your account does not meet this criteria, then your account is currently ineligible to use Customer Match.<br><br>Chat with your Google Ads Rep for more guidance on Customer Match availability for your account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Implementation process
### Step 1: Connect Google account

To get started, go to the **Google Ads** tab in the **Technology Partners** page and select **Connect Google Ads**. You’ll then be prompted with a modal to select the email associated with your Google Ads account and then grant Braze access to your Google Ads account.

Once you have successfully connected your Google Ads account, you will be taken back to your Google Ads partner page. You’ll then be prompted to select which ad accounts you would like to be accessed within the Braze App Group.

![]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

{% alert important %}
If you plan to export iOS IDFA or Google Advertising IDs within your audience sync, Google requires your iOS app ID and Android app ID within the requests. Within the Google Audience Sync module, select **Add Mobile Advertising IDs**, input your iOS app ID and Android app ID (app package name), and save each.
<br><br>
![The updated Google Ads technology page showing the Ad accounts connected, allowing you to re-sync accounts and add mobile advertising IDs.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
{% endalert %}

### Step 2: Add a Google Audience step in Canvas

Add a step in your Canvas, select the dropdown at the top of the step, and select the **Google Audience** step.

![Workflow of the previous steps to add a Google audience in Canvas.][6]

### Step 3: Sync setup

Click on the **Custom Audience** button to open the step editor.

Select the desired Google ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience. 

{% tabs %}
{% tab Create a New Audience %}
**Create a New Audience**<br>
Enter a name for the new custom audience, select **Add Users to Audience** and select the first-party user field data to send to with your audience. You can choose either: 
- **Customer Contact Info** which will contain your users' email and/or phone numbers if they exist in Braze
- **Mobile Advertiser ID** which you will then need to select either iOS IDFA or Android GAID   

Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, a new audience is created, and the "customer contact info" checkbox is selected.]({% image_buster /assets/img/google_sync/google_sync7.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode. 

![An alert that appears once a new audience is created in the Canvas step.]({% image_buster /assets/img/google_sync/google_sync9.png %})

When you launch a Canvas with a new audience, Braze will create a new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Google Audience Step. 

{% alert important %}
Given Google's Customer Match requirements, you cannot have customer contact info and mobile advertiser IDs in the same customer lists. Google Customer Match will then use this information to determine who is targetable within Google Search, Google Display, YouTube, and Gmail. For more details around Google Customer Match requirements, review their [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to either add or remove users from existing Google customer lists to ensure that these audiences are up-to-date. To sync with an existing audience, select an existing custom audience to sync to and then choose whether you want to **Add to the audience** or **Remove from the audience**. Braze will then either add or remove users in near real-time as they enter the Google Audience Step. 

Once you've configured your Google Audience step, select **Done**. Your Google Audience step will include details about the new audience.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience is selected, as well as the "Add user to Audience" radio button.]({% image_buster /assets/img/google_sync/google_sync8.png %})

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
**Entered**: Number of users who entered this step to be synced to Google.

**Proceeded to Next Step**: How many users advanced to the next step if there is one. All users will auto-advance. 0 if this is the last step in the Canvas branch.

**Users Synced**: Number of users who have successfully been synced to Google.

**User Not Synced**: Number of users that have not been synced due to missing fields to match.

**Users Errored**: Number of users who were not synced to Google due to an error, after &#126;13 hours of retries. For specific errors, like Google Ads API service disruptions, Canvas will retry the sync for up to &#126;13 hours. If the sync is still not possible at that point, the User Not Synced will be populated.

**Users Pending**: Number of users currently being processed by Braze to sync to Google.

**Exited Canvas**: Number of users who have exited the Canvas. This occurs when the last step in a Canvas is a Google step.

## Troubleshooting
{% details Why am I unable to select multiple fields to match in my Google Audience Step configuration? %}
Google Customer Match has strict requirements around how these audiences are formatted and what customer information is included. Specifically, mobile advertiser IDs need to be uploaded separately from customer contact info (i.e., email and phone number). Refer to [Google's Customer Match documentation](https://support.google.com/google-ads/answer/7659867?hl=en#undefined) for more details. 
{% enddetails %}

{% details How long will it take for my audiences to sync in Google? %} 
It can take anywhere between 6 to 12 hours for an audience to be synced into Google. 
{% enddetails %}

{% details I've synced an audience, but the audience size in Google is zero. %}
For privacy purposes, the user list size will show as zero until the list has at least **1,000 members**. After that, the size will be rounded to the two most significant digits.
{% enddetails %}

{% details I've synced an audience into Google, but my ads are not serving. %}
Check that your audiences contain at least **5,000** users to ensure that ads start serving. 
{% enddetails %}

[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
