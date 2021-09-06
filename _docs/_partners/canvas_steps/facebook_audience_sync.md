---
nav_title: Audience Sync to Facebook
article_title: Canvas Audience Sync to Facebook
description: "This reference article will cover how to use Braze Audience Sync to Facebook, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 4
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Audience Sync to Facebook

Using the Braze Audience Sync to Facebook, brands can elect to add their own users' data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (Push, Email, SMS, Webhook, etc.) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in Facebook via Custom Audiences.

__Common use cases for syncing Custom Audiences include__:

- Targeting high-value users via multiple channels to drive purchases or engagement.
- Retargeting users who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand.
- Creating Lookalike Audiences to acquire new users more efficiently.

This feature gives brands the option to control what specific first-party data is shared with Facebook. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. To learn more about our Braze data privacy policy, click [here](https://www.braze.com/privacy).

## Integration

### Integration Requirements

You will need to ensure that you have the following items created and/or completed before setting up your Facebook Audience Step in Canvas. 

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][3] | A centralized tool to manage your brand's Facebook assets (e.g., ad accounts, pages, apps). |
| Facebook Ad Account | [Facebook][4] | An active Facebook ad account tied to your brand's Business Manager.<br><br>Please ensure that your Facebook Business Manager admin has granted you admin permissions to the Facebook ad accounts you plan to use with Braze and that you have accepted your ad account terms and conditions. |
| Facebook Custom Audiences Terms | [Facebook][6] | Accept Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

### Step 1: Connect to Facebook

In the Braze dashboard, go to __Technology Partners__ and select __Facebook__. In the Facebook Audience Export module, click __Connect Facebook__.

![Activate Facebook][34]{: style="max-width:70%;"}

A Facebook oAuth dialog window will appear to authorize Braze to create Custom Audiences into your Facebook ad accounts.

![Facebook Dialog][36]{: style="max-width:30%;"}  ![Facebook Dialog][35]{: style="max-width:40%;"}

Once you have linked Braze to your Facebook account, you will then be able to select which ad accounts you would like to sync within your Braze app group. 

![Facebook Dialog][37]{: style="max-width:70%;"}

Once you have successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![Facebook Connected][38]{: style="max-width:70%;"}

Your Facebook connection will be applied at the Braze app group level. If your Facebook admin removes you from your Facebook Business Manager or access to the connected Facebook accounts, Braze will detect an invalid token. As a result, your active Canvases using Facebook Audience Steps will show errors, and Braze will not be able to sync users. 

{% alert important %}
For customers who have previously undergone the Facebook App Review process for [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) and [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), your System User Token will still be valid for the Facebook Audience Step. You will not be able to edit or revoke the Facebook System User Token through the Facebook partner page. Instead, you can connect your Facebook account to replace your Facebook System User Token within your Braze app group. 

<br><br>The Facebook oAuth configuration will also apply to [Facebook exports via Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites). 
{% endalert %}

### Step 2: Add a Facebook Audience Step in Canvas

Add a step in your Canvas, select the dropdown at the top of the step, and select __Facebook Audience Step__.

![audience sync][20]{:style="max-width:70%"}

### Step 3: Sync Setup

Click on the __Custom Audience__ button to open the step editor.

Select the desired Facebook ad account. Then you will have to option to __Sync with an Existing Audience__ or __Create a New Audience__.

{% tabs %}
{% tab Create a New Audience %}
__Create a New Audience__<br>
Select the option to __Create a New Audience__ and enter a name for the new custom audience. You will also be able to select which fields you would like to sync with Facebook. 

![Google Sync]({% image_buster /assets/img/fb_audience_sync/google_sync7.png %})

When you launch a Canvas with __Create a New Audience__ selected, Braze will create the new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Facebook Audience Step. 

{% endtab %}
{% tab Sync with an Existing Audience %}
__Sync with an Existing Audience__<br>
Braze also offers the ability to either add or remove users from existing Facebook custom audiences to ensure that these audiences are up-to-date. To sync with an existing audience, select an existing custom audience to sync to and then choose whether you want to __Add to the audience__ or __Remove from the audience__. Braze will then either add or remove users in near real-time as they enter the Facebook Audience Step. 

![Google Sync]({% image_buster /assets/img/fb_audience_sync/google_sync8.png %})

It's important to note that Facebook prohibits removing users from custom audiences where the audience sizes are too low (typically fewer than 1,000). As a result, Braze will be unable to sync users for a Remove from Audience step until the audience reaches the appropriate audience size.

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas

Once you have configured your Facebook Audience Step, simply launch the Canvas! The new custom audience will be created, and users who flow through the Facebook Audience step will be passed into this custom audience on Facebook. If your Canvas contains subsequent steps, your users will then advance to the next step in their user journey.

The __History__ tab of the custom audience in the Facebook Audience Manager will reflect the number of users sent to the audience from Braze. If a user re-enters the step, they will be sent to Facebook again.

![Google Sync][39]{: style="max-width:80%;"}

## User Syncing & Rate Limit Considerations 
As users reach the Audience Sync Step, Braze will sync these users in near real-time while also respecting Facebook's Marketing API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to Facebook. 

Facebook's Marketing API rate limit states no more than &#126;190k API requests for each ad account in a 1 hour time period. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to &#126;13 hours. If the sync is not possible at that point, these users are listed under the Users Errored metric.

Given these processing and rate-limiting considerations, Braze recommends no more than __10-15 million users synced per day__ to ensure that Braze can successfully process and sync users with Facebook. If you have an audience larger than 10-15 million users, you can sync this custom audience at a lower frequency (ex: once per week). 

## Understanding Analytics

![audience sync][16]{: style="float:right;max-width:15%;margin-left:15px;"}

__Entered__: Number of users who entered this step to be synced to Facebook

__Proceeded to Next Step__: How many users advanced to the next step if there is one. All users will auto-advance. 0 if this is the last step in the Canvas branch.

__Users Synced__: Number of users who have successfully been synced to Facebook

__Users Not Synced__:  Number of users that have not been synced due to missing fields to match.

__Users Pending__: Number of users currently being processed by Braze to sync into Facebook. 

__Users Errored__: Number of users who were not synced to Facebook due to an API error after &#126;13 hours of retries.<br>- Potential causes of errors can include an invalid Facebook token or if the custom audience was deleted on Facebook. 

__Exited Canvas__: Number of users who have exited the Canvas. This occurs when the last step in a Canvas is a Facebook step.

{% alert important %}
Keep in mind that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Troubleshooting

{% details What should I do next if I receive an invalid token error? %}
You can simply disconnect and reconnect your Facebook account on the Facebook partner page. Please ensure with your Facebook Business Manager Admin that you have the appropriate permissions to the ad account you wish to sync with.
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
- Make sure your system user token is authenticated and has access to the desired ad accounts in Facebook Business Manager
- Make sure you have selected an ad account, entered a name for the new custom audience, and selected fields to match
- You may have reached the 500 custom audience limit on Facebook. Go into Facebook Audience Manager to delete some unneeded ones before creating any new Custom Audiences using Canvas.
{% enddetails %}

{% details How do I know if users have matched after passing users to Facebook? %}
Facebook does not provide this information for privacy reasons.
{% enddetails %}

{% details Does Braze support value-based custom audiences? %}
At this time, value-based custom audiences are not supported by Braze. If you are interested in syncing these types of custom audiences please reach out to your Customer Success Manager.
{% enddetails %}

[0]: https://www.braze.com/privacy
[3]: https://www.facebook.com/business/help/113163272211510
[4]: https://www.facebook.com/business/help/910137316041095
[6]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[34]: {% image_buster /assets/img/fb/afb_1.png %}
[35]: {% image_buster /assets/img/fb/afb_2.png %}
[36]: {% image_buster /assets/img/fb/afb_3.png %}
[37]: {% image_buster /assets/img/fb/afb_4.png %}
[38]: {% image_buster /assets/img/fb/afb_5.png %}
[16]: {% image_buster /assets/img/fb_audience_sync/FB2.jpg %}
[20]: {% image_buster /assets/img/fb_audience_sync/FB6.png %}
[39]: {% image_buster /assets/img/fb_audience_sync/google_sync9.png %}
