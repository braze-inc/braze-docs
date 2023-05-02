---
nav_title: Audience Sync to TikTok
article_title: Canvas Audience Sync to TikTok
alias: /tiktok_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to TikTok to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
hidden: true
layout: dev_guide
---

# Audience Sync to TikTok

Using the Braze Audience Sync to TikTok, brands can elect to add user data from their own Braze integration to TikTok Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas. 

**Common use cases for Audience Syncing include**:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating Actalike Audiences to acquire new users more efficiently

This feature allows brands to control what specific first-party data is shared with TikTok. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to TikTok is currently in beta. Contact your Braze account manager if you're interested in participating in the beta.
{% endalert %}

## Prerequisites

You must ensure that you have the following items completed before setting up your Audience Sync to TikTok.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| TikTok for Business Center Account | [TikTok](https://business.tiktok.com/) | A centralized tool to manage your brand's TikTok assets (i.e., ad accounts, pages, apps). |
| TikTok Ad Account | [TikTok](https://ads.tiktok.com/) | An active TikTok ad account tied to your brand's Business Center account.<br><br>Ensure that your TikTok Business Center manager admin has granted you admin permissions to the TikTok ad accounts you plan to use with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration 

### Step 1: Connect to TikTok

In the Braze dashboard, go to **Technology Partners** and select **TikTok**. In the TikTok Audience Export module, click **Connect TikTok**.

![TikTok technology page in Braze includes an Overview module and TikTok Audience Export module with the Connected TikTok button.][1]{: style="max-width:75%;"}

You'll then be redirected to the TikTok OAuth page to authorize Braze for ad account management and Audience Management. Once you have selected **Confirm**, you'll be redirected back into Braze to select which TikTok ad accounts you wish to sync to. 

![][2]{: style="max-width:75%;"}

Once successfully connected, you will return to the partner page. Here, you can view which accounts are connected and disconnect existing accounts.

![][3]{: style="max-width:75%;"}

Your TikTok connection will be applied at the Braze app-group level. If your TikTok admin removes you from your TikTok Business Center or access to the connected TikTok accounts, Braze will detect an invalid token. As a result, your active Canvases using TikTok Audience components will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options. 

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), you will be able to use the **Ads Tracking Enabled** filter. Select the value as `true` to only send users into Audience Sync destinations where they have opted in. 

![][16]{: style="max-width:75%;"}

If you are collecting ‘opt-ins’,  ‘opt-outs’, ‘Do Not Sell Or Share’ or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![A Canvas with an entry audience of "opted_in_marketing" equals "true".][13]{: style="max-width:75%;"}

### Step 3: Add a TikTok Audience component in Canvas Flow

Add a component in your Canvas and select **Audience Sync**. Click on the **Custom Audience** button to open the component editor.

![][14]{: style="max-width:45%;"} ![][15]{: style="max-width:50%;"}

### Step 4: Sync setup

Select **TikTok** as the desired Audience Sync partner.

![][12]{: style="max-width:50%;"}

Then select the desired TikTok ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

![][11]

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with TikTok. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![]({% image_buster /assets/img/tiktok/tiktok10.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![]({% image_buster /assets/img/tiktok/tiktok9.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the audience step.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing TikTok audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the TikTok Audience step.

![Expanded view of the Custom Audience Canvas step. Here, the desired ad account and existing audience are selected.]({% image_buster /assets/img/tiktok/tiktok17.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas
Once you have configured your TikTok Audience component, simply launch the Canvas! A new audience will be created, and users who flow through the TikTok Audience component will be passed into this audience on TikTok. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience in TikTok by going into your **Ads Manager Account** and then selecting **Audiences** from the **Assets** dropdown. From the **Audience** page, you can see the size of each audience after it reaches &#126;1,000.

![TikTok page listing the following metrics for the given audience.][5]

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze will sync these users in near real-time while respecting TikTok's Marketing API rate limits. This means that Braze will try to batch and process as many users every 5 seconds before sending these users to TikTok.

TikTok's Segment API rate limit states no more than 50 queries per second and 10k users per request. If a Braze customer reaches this rate limit, the Canvas will retry the sync for up to &#126;13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

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
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Troubleshooting

{% details What should I do next if I receive an invalid token error? %}
You can disconnect and reconnect your TikTok account on the TikTok partner page. Ensure with your TikTok Business Center admin that you have the appropriate permissions to the ad account you wish to sync.
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Ensure your TikTok account successfully connects to Braze on the TikTok partner page.
Make sure you have selected an ad account, entered a name for the new audience, and selected fields to match
{% enddetails %}

{% details How do I know if users have matched after passing users to TikTok? %}
TikTok does not provide this information for their data privacy policies.
{% enddetails %}

{% details How long will it take for my audiences to populate in TikTok? %}
The audience size will update within 24-48 hours on the Audiences page in TikTok’s Ads Manager.
{% enddetails %}

{% details What is the maximum number of audiences I can have in my TikTok ads account? %}
400
{% enddetails %}

[1]: {% image_buster /assets/img/tiktok/tiktok1.png %}
[2]: {% image_buster /assets/img/tiktok/tiktok2.png %}
[3]: {% image_buster /assets/img/tiktok/tiktok3.png %}
[4]: {% image_buster /assets/img/tiktok/tiktok4.png %}
[5]: {% image_buster /assets/img/tiktok/tiktok5.png %}
[6]: {% image_buster /assets/img/tiktok/tiktok6.png %}
[7]: {% image_buster /assets/img/tiktok/tiktok7.png %}
[8]: {% image_buster /assets/img/tiktok/tiktok8.png %}
[9]: {% image_buster /assets/img/tiktok/tiktok9.png %}
[10]: {% image_buster /assets/img/tiktok/tiktok10.png %}
[11]: {% image_buster /assets/img/tiktok/tiktok11.png %}
[12]: {% image_buster /assets/img/tiktok/tiktok12.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[14]: {% image_buster /assets/img/tiktok/tiktok14.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok15.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[17]: {% image_buster /assets/img/tiktok/tiktok17.png %}