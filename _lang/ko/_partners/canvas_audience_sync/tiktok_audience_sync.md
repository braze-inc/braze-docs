---
nav_title: TikTok
article_title: Canvas Audience Sync to TikTok
alias: /tiktok_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to TikTok to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
page_order: 7

---

# Audience Sync to TikTok

Using the Braze Audience Sync to TikTok, brands can elect to add user data from their own Braze integration to TikTok Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas. 

**Common use cases for Audience Syncing include**:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating Actalike Audiences to acquire new users more efficiently

This feature lets brands control what specific first-party data is shared with TikTok. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to TikTok is an Audience Sync Pro integration. For more information on this integration, reach out to your Braze account manager.
{% endalert %}

## Prerequisites

You must ensure the following items are created, completed, and/or accepted before setting up your TikTok Audience Step in Canvas.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| TikTok for Business Center Account | [TikTok](https://business.tiktok.com/) | A centralized tool to manage your brand's TikTok assets (such as ad accounts, pages, apps). |
| TikTok Ad Account | [TikTok](https://ads.tiktok.com/) | An active TikTok ad account tied to your brand's Business Center account.<br><br>Ensure that your TikTok Business Center manager admin has granted you admin permissions to the TikTok ad accounts you plan to use with Braze. |
| TikToK terms & policies | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Agree to comply with any of TikTok’s required terms, policies, guidelines, and documentation related to your use of the Pinterest Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include: the Commercial Terms of Service, Advertising Terms, Privacy Policy, Custom Audience Terms, Developer Terms of Service, Developer Data Sharing Agreement, Advertising Policies, Brand Guidelines, and Community Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to TikTok

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **TikTok**. Under TikTok Audience Sync, select **Connect TikTok**.

![TikTok technology page in Braze includes an Overview section and TikTok Audience Sync section with the Connected TikTok button.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

You'll then be redirected to the TikTok OAuth page to authorize Braze for ad account management and Audience Management. After you have selected **Confirm**, you'll be redirected back into Braze to select which TikTok ad accounts you wish to sync to. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Once successfully connected, you will return to the partner page. Here, you can view which accounts are connected and disconnect existing accounts.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Your TikTok connection will be applied at the Braze app-group level. If your TikTok admin removes you from your TikTok Business Center or access to the connected TikTok accounts, Braze will detect an invalid token. As a result, your active Canvases using TikTok Audience components will show errors, and Braze will not be able to sync users.

### Step 2: Add a TikTok Audience component in Canvas Flow

Add a component in your Canvas and select **Audience Sync**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Step 3: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **TikTok** as the desired Audience Sync partner.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Then select the desired TikTok ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with TikTok. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the audience step.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing TikTok audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the TikTok Audience step.

![Expanded view of the Custom Audience Canvas step. Here, the desired ad account and existing audience are selected.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas
Once you have configured your TikTok Audience component, simply launch the Canvas! A new audience will be created, and users who flow through the TikTok Audience component will be passed into this audience on TikTok. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience in TikTok by entering your **Ads Manager Account** and selecting **Audiences** from the **Assets** dropdown. From the **Audience** page, you can see the size of each audience after it reaches ~1,000.

![TikTok page listing the following metrics for the given audience.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze will sync these users in near real-time while respecting TikTok's Marketing API rate limits. This means that Braze will try to batch and process as many users every 5 seconds before sending these users to TikTok.

TikTok's Segment API rate limit states no more than 50 queries per second and 10k users per request. If a Braze customer reaches this rate limit, the Canvas will retry the sync for up to ~13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| ------ | ----------- |
| Entered | Number of users who entered this component to be synced to TikTok. |
| Proceeded to Next Step | Number of users that advanced to the next component if one exists. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to TikTok. Note that this does not equate to users matched on TikTok. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into TikTok. |
| Users Errored | Number of users who were not synced to TikTok due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid TikTok token or if the audience was deleted on TikTok. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Frequently asked questions

### What should I do next if I receive an invalid token error?

You can disconnect and reconnect your TikTok account on the TikTok partner page. Ensure with your TikTok Business Center admin that you have the appropriate permissions to the ad account you wish to sync.

### Why is my Canvas not allowed to launch?

Confirm that your TikTok account successfully connects to Braze on the TikTok partner page. Next, make sure you've selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to TikTok?

TikTok does not provide this information for their data privacy policies.

### How long will it take for my audiences to populate in TikTok?

The audience size will update within 24-48 hours on the Audiences page in TikTok’s Ads Manager.

### What is the maximum number of audiences I can have in my TikTok ad account?

You can have up to 400 audiences per TikTok ad account.

### Why is my audience size or match rate in TikTok higher than the users synced in Braze with Audience Sync?

This is because in TikTok, one ID may be associated with multiple TikTok users. This occurs most often when clients use mobile ad IDs (iOS IDFA and Android GAID) because one device may have multiple TikTok users logged in. 

Additionally, TikTok also counts Pangle users as matched users, which in some cases can result in an elevated match rate. However, when you use the audience for ad delivery, the actual deliverable audience size may not be as high as the matched user size as it depends on placement and other influencing factors.


