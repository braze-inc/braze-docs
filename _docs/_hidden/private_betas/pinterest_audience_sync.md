---
nav_title: Audience Sync to Pinterest
article_title: Canvas Audience Sync to Pinterest
description: "This reference article will cover how to use Braze Audience Sync to Pinterest, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 4
alias: "/audience_sync_pinterest/"
hidden: true

Tool:
  - Canvas

---

## Audience Sync to Pinterest

Using the Braze Audience Sync to Pinterest, brands can elect to add user data from their own Braze integration to Pinterest Audiences to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you'd normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in your Pinterest Audiences.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand
- Creating Actalike Audiences to acquire new users more efficiently

This feature allows brands to control what specific first-party data is shared with Pinterest. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to Pinterest is currently in beta. Contact your Braze account manager if you're interested in participating in the beta.
{% endalert %}

## Prerequisites 
You will need to ensure that you have the following items created and/or completed before setting up your Audience Sync to Pinterest.

| Requirement | Origin | Description |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | A centralized tool to manage your brand's Pinterest assets (i.e., ad accounts, pages, apps). |
| Pinterest ad account | [Pinterest](https://ads.pinterest.com/) | An active Pinterest ad account tied to your brand's Pinterest Business Hub.<br><br>Ensure that your Pinterest Business Hub admin has granted you admin permissions to the Pinterest ad accounts you plan to use with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration 

### Step 1: Connect to Pinterest

In the Braze dashboard, go to **Technology Partners** and select **Pinterest**. In the Pinterest Audience Export module, click **Connect Pinterest**.

![Pinterest technology page in Braze that includes an Overview module and Pinterest Audience Sync module with the Connected Pinterest button.][1]{: style="max-width:80%;"}

You'll then be redirected to the Pinterest OAuth page to authorize Braze for Ad Account Management and Audience Management.

Once you have selected confirm, you'll be redirected back into Braze to select which Pinterest ad accounts you wish to sync. 

![A list of available ad accounts you can connect to Pinterest.][2]{: style="max-width:80%;"}

Once successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![An updated version of the Pinterest technology partners page showing the ad accounts successfully connected.][3]{: style="max-width:80%;"}

Your Pinterest connection will be applied at the Braze app group level. If your Pinterest admin removes you from your Pinterest Business Hub or access to the connected Pinterest accounts, Braze will detect an invalid token. As a result, your active Canvases using Pinterest Audience components will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

To prevent sending users that have opted out of ads tracking and/or opted into the "Do Not Sell or Share" as per the [CCPA](https://oag.ca.gov/privacy/ccpa), marketers should ensure they are implementing the proper filters within their Canvas entry criteria.

If you have opted into collecting the [iOS IDFA through the Braze SDK](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the **Ads Tracking Enabled** filter. Set the value as `true` to only send users into Audience Sync destinations where they have opted in. 

![][16]{: style="max-width:75%;"}

If you collect opt-ins or opt-outs as Braze custom attributes, you should also include them within your Canvas entry criteria as a filter:

![][13]{: style="max-width:75%;"}

### Step 3: Add an Audience Sync Step with Pinterest

Add a component in your Canvas and select **Audience Sync**.

![Workflow of the previous steps to add a Pinterest Audience component in Canvas Flow.][4]{: style="max-width:50%;"}

![Workflow of the previous steps to add a Pinterest Audience component in Canvas Flow.][5]{: style="max-width:50%;"}

### Step 4: Sync setup

Click on the **Custom Audience** button to open the component editor. Select Pinterest as the desired Audience Sync partner. 

Then select your desired Pinterest ad account. Under the **Choose a New or Existing Audience dropdown**, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Pinterest. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/pinterest/pinterest8.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![An alert that appears once a new audience is created in the Canvas component.]({% image_buster /assets/img/pinterest/pinterest9.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync step.
{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing Pinterest audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and add to the audience. Braze will then either add users in near real-time as they enter the Audience Sync step.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/pinterest/pinterest10.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Audience Sync to Pinterest, launch the Canvas! The new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on Pinterest. If your Canvas contains subsequent components, your users will then advance to the next step in their user journey.

You can view the audience on Pinterest by going into your ads manager account and selecting Audiences from the Ads dropdown. From the Audience page, you can see the size of each audience after it reaches ~100.

![Audience details for a given Pinterest audience that includes audience name, audience ID, audience type, audience size.][11]

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze will sync these users in near real-time while respecting Pinterest's Marketing API rate limits. In practice, Braze will try to batch and process as many users every 5 seconds before sending these users to Pinterest.

Pinterest's Segment API rate limit states no more than seven queries per second per user and 1,900 users per request. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to ~13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Pinterest. |
| Proceeded to Next Step | How many users advanced to the next component if there is one? All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Pinterest. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Pinterest. |
| Users Errored | Number of users who were not synced to Pinterest due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Pinterest token or if the audience was deleted on Pinterest. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Remember that there will be a delay in reporting for synced users and errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Troubleshooting
{% details What should I do next if I receive an invalid token error? %}
You can simply disconnect and reconnect your Pinterest account on the Pinterest partner page. Ensure with your Pinterest Business Hub admin that you have the appropriate permissions to the ad account you wish to sync.
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Ensure your Pinterest account successfully connects to Braze on the Pinterest partner page.
Make sure you have selected an ad account, entered a name for the new audience, and selected fields to match
{% enddetails %}

{% details How do I know if users have matched after passing users to Pinterest? %}
Pinterest does not provide this information for its own data privacy policies.
{% enddetails %}

{% details How long will it take for my audiences to populate in Pinterest? %}
The audience size will update within 24-48 hours on the Audiences page in Pinterest's Ads Manager.
{% enddetails %}

[1]: {% image_buster /assets/img/pinterest/pinterest1.png %}
[2]: {% image_buster /assets/img/pinterest/pinterest2.png %}
[3]: {% image_buster /assets/img/pinterest/pinterest3.png %}
[4]: {% image_buster /assets/img/pinterest/pinterest4.png %}
[5]: {% image_buster /assets/img/pinterest/pinterest5.png %}
[6]: {% image_buster /assets/img/pinterest/pinterest6.png %}
[7]: {% image_buster /assets/img/pinterest/pinterest7.png %}
[8]: {% image_buster /assets/img/pinterest/pinterest8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[9]: {% image_buster /assets/img/pinterest/pinterest9.png %}
[10]: {% image_buster /assets/img/pinterest/pinterest10.png %}
[11]: {% image_buster /assets/img/pinterest/pinterest11.png %}
