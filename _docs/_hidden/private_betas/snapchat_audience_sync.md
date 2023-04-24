---
nav_title: Audience Sync to Snapchat
article_title: Canvas Audience Sync to Snapchat
description: "This reference article will cover how to use Braze Audience Sync to Snapchat, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 4
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas
hidden: true
---

# Audience Sync to Snapchat

Using the Braze Audience Sync to Snapchat, brands can elect to add user data from their own Braze integration to Snapchat customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you'd normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now be used to trigger an ad to that user in your Snapchat customer lists.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating lookalike audiences to acquire new users more efficiently

This feature allows users to control what specific first-party data is shared with Snapchat. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to Snapchat is currently in beta. Contact your Braze account manager if you're interested in participating in the beta.
{% endalert %}

## Prerequisites 

You will need to ensure that you have the following items created and/or completed before setting up your Audience Sync to Snapchat.

| Requirement | Origin | Description |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | A centralized tool to manage your brand's Snapchat assets (i.e., ad accounts, pages, apps). |
| Snapchat ad account | Snapchat | An active Snapchat ad account tied to your brand's Snapchat Business Manager.<br><br>Ensure that your Snapchat Business Manager admin has granted you admin permissions to the Snapchat ad accounts you plan to use with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration 

### Step 1: Connect to Snapchat

In the Braze dashboard, go to **Technology Partners** and select **Snapchat**. In the Snapchat Audience Export module, click **Connect Snapchat**.

![Snapchat technology page in Braze that includes an Overview module and Snapchat Audience Sync module with the Connected Snapchat button.][1]{: style="max-width:80%;"}

You'll then be redirected to the Snapchat OAuth page to authorize Braze for the permissions related to your Audience Sync integration.

Once you have selected confirm, you'll be redirected back into Braze to select which Snapchat ad accounts you wish to sync. 

![A list of available ad accounts you can connect to Snapchat.][2]{: style="max-width:80%;"}

Once successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![An updated version of the Snapchat technology partners page showing the ad accounts successfully connected.][3]{: style="max-width:80%;"}

Your Snapchat connection will be applied at the Braze app group level. If your Snapchat admin removes you from your Snapchat Business Manager or access to the connected Snapchat ad accounts, Braze will detect an invalid token. As a result, your active Canvases using Snapchat will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filter/s for users’ eligibility within their Canvas entry criteria. Below we list some options. 

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the **Ads Tracking Enabled** filter. Select the value as `true` to only send users into Audience Sync destinations where they have opted in. 
![][16]{: style="max-width:75%;"}

If you collect opt-ins or opt-outs as Braze custom attributes, you should also include them within your Canvas entry criteria as a filter:

![A Canvas with an entry audience of "opted_in_marketing" equals "true".][13]{: style="max-width:75%;"}

### Step 3: Add an Audience Sync Step with Snapchat

Add a component in your Canvas and select **Audience Sync**.

![Workflow of the previous steps to add a Snapchat Audience component in Canvas Flow.][4]{: style="max-width:60%;"}

![Workflow of the previous steps to add a Snapchat Audience component in Canvas Flow.][5]{: style="max-width:60%;"}

### Step 4: Sync setup

Click on the **Custom Audience** button to open the component editor. Select Snapchat as the desired Audience Sync partner. 

Then select your desired Snapchat ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Snapchat. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/snapchat/snapchat4.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![An alert that appears once a new audience is created in the Canvas component.]({% image_buster /assets/img/snapchat/snapchat5.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.

{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to either add users to existing Snapchat audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then either add users in near real-time as they enter the Audience Sync component.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/snapchat/snapchat6.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Audience Sync to Snapchat, simply launch the Canvas! A new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on Snapchat. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience in Snapchat by going into your ads manager account and selecting **Audiences** from the Assets section of the navigation. From the **Audiences** page, you can see the size of each audience after it reaches ~1,000.

![Audience details for a given Snapchat audience that includes audience name, audience type, audience size, and audience renetion in days.][9]

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze will sync these users in near real-time while also respecting Snapchat's API rate limits. In practice, Braze will try to batch and process as many users every 5 seconds before sending these users to Snapchat.

Snapchat's API rate limit states no more than ten queries per second and 100,000 users per request. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to ~13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

### Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Snapchat. |
| Proceeded to Next Step | How many users advanced to the next component if there is one? All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Snapchat. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Snapchat. |
| Users Errored | Number of users who were not synced to Snapchat due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Snapchat token or if the audience was deleted on Snapchat. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Remember that there will be a delay in reporting for synced users and errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Troubleshooting

{% details What should I do next if I receive an invalid token error? %}
You can disconnect and reconnect your Snapchat account on the Snapchat partner page. Ensure with your Snapchat Business Manager admin that you have the appropriate permissions to the ad account you wish to sync with.
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Ensure that your Snapchat ad account successfully connects to Braze on the Snapchat partner page. Make sure you have selected an ad account, entered a name for the new audience, and selected fields to match
{% enddetails %}

{% details How do I know if users have matched after passing users to Snapchat? %}
Snapchat does not provide this information for their data privacy policies.
{% enddetails %}

{% details How many audiences can Snapchat support? %}
At this time, you can only have 1,000 audiences within your Snapchat account. 
If you breach this limit, Braze will notify you that we cannot create new audiences. 
You will need to go into your Snapchat ads account and remove audiences you are no longer using. 
{% enddetails %}

[1]: {% image_buster /assets/img/snapchat/snapchat1.png %}
[2]: {% image_buster /assets/img/snapchat/snapchat2.png %}
[3]: {% image_buster /assets/img/snapchat/snapchat3.png %}
[6]: {% image_buster /assets/img/snapchat/snapchat4.png %}
[7]: {% image_buster /assets/img/snapchat/snapchat5.png %}
[8]: {% image_buster /assets/img/snapchat/snapchat6.png %}
[9]: {% image_buster /assets/img/snapchat/snapchat7.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
