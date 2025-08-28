---
nav_title: Criteo
article_title: Canvas Audience Sync to Criteo
description: "This reference article will cover how to use Braze Audience Sync to Criteo, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 1
alias: /audience_sync_criteo/

Tool:
  - Canvas
---

# Audience Sync to Criteo

Using the Braze Audience Sync to Criteo, brands can elect to add user data from their own Braze integration to Criteo customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now be used to trigger an ad to that user in your Criteo customer lists.

**Common use cases for audience syncing include:**

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand
- Creating Lookalike Audiences to acquire new users more efficiently

This feature gives brands the option to control what specific first-party data is shared with Criteo. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
**Audience Sync Pro disclaimer**<br>
Braze Audience Sync to Criteo is an Audience Sync Pro integration. For more information on this integration, reach out to your Braze account manager. <br> 
{% endalert %}

## Prerequisites 

You will need to ensure that you have the following items created and/or completed prior to setting up your Audience Sync to Criteo.

| Requirement | Origin | Description |
| --- | --- | --- |
| Criteo ad account | [Criteo](https://marketing.criteo.com/) | An active Criteo ad account tied to your brand.<br><br>Ensure that your Criteo admin has granted you the appropriate permissions to access Audiences. |
| [Criteo Advertising Guidelines](https://www.criteo.com/advertising-guidelines/)<br>and<br>[Criteo Brand Safety Guidelines](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | As an active Criteo customer, you must ensure that you can comply with Criteo’s Advertising and Brand Safety Guidelines prior to launching any Criteo campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration 

### Step 1: Connect to Criteo

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Criteo**. Under Criteo Audience Export, select **Connect Criteo**.

![Criteo technology page in Braze that includes an Overview section and Criteo section with the Connected Criteo button.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

A Criteo oAuth page will appear to authorize Braze for the permissions related to your Audience Sync integration.

Once you have selected confirm, you’ll then be redirected back into Braze to select which Criteo ad accounts you wish to sync to. 

![A list of available ad accounts you can connect to Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Once you have successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![An updated version of the Criteo technology partners page showing the ad accounts successfully connected.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Your Criteo connection will be applied at the Braze workspace level. If your Criteo admin removes you from your Criteo ad account, Braze will detect an invalid token. As a result, your active Canvases using Criteo will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options.

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), you will be able to use the Ads Tracking Enabled filter. Select the value as true to only send users into Audience Sync destinations where they have opted in.

![]({% image_buster /assets/img/criteo/criteo11.png %})

If you are collecting `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![]({% image_buster /assets/img/criteo/criteo12.png %})

To learn more on how to comply with these Data Protection laws within the Braze platform, see [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/).

### Step 3: Add an Audience Sync Step with Criteo

Add a component in your Canvas and select **Audience Sync**.

![Workflow of the previous steps to add a Criteo Audience component in Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Workflow of the previous steps to add a Criteo Audience component in Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Step 4: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **Criteo** as the desired Audience Sync partner. 

![]({% image_buster /assets/img/criteo/criteo6.png %})

Then select your desired Criteo ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

{% tabs %}
{% tab Create a New Audience %}
**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with Criteo. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account is selected, and a new audience is created.]({% image_buster /assets/img/criteo/criteo3.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/criteo/criteo1.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.
{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing Criteo audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the Audience Sync component.

![Expanded view of the Custom Audience Canvas step. Here, the desired Ad account and existing audience are selected.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Audience Sync to Criteo, simply launch the Canvas! The new audience will be created, and users who go through the Audience Sync step will be passed into this audience on Criteo. If your Canvas contains subsequent components, your users will then advance to the next step in their user journey.

You can view the audience in Criteo by going into your ads manager account and then selecting Segments from the **Audience Library** of the navigation. From the **Segments** page, you can see the size of each audience after it reaches ~1,000.

![The audience library showing the segment, id, source, type, size, currently used, and last update.]({% image_buster /assets/img/criteo/criteo.png %})

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze will sync these users in near real-time while also respecting Criteo's API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to Criteo.

Criteo's API rate limit states no more than 250 requests per minute. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to ~13 hours. If the sync is not possible, these users are listed under the Users Errored metric. 

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Criteo. |
| Proceeded to Next Step | How many users advanced to the next component if there is one. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Criteo. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Criteo. |
| Users Errored | Number of users who were not synced to Criteo due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Criteo token or if the audience was deleted on Criteo. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Frequently asked questions

### What should I do next if I receive an invalid token error?
You can simply disconnect and reconnect your Criteo account on the Criteo partner page. Ensure with your Criteo admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Confirm that your Criteo ad account has successfully connected to Braze on the Criteo partner page. Next, check that you've selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to Criteo?

Criteo does not provide this information for their own data privacy policies.

### How many audiences can Criteo support?

At this time, you can only have 1,000 audiences within your Criteo account. If you're exceed this limit, Braze will notify you that we are unable to create new audiences. You'll need to remove audiences that you're no longer using in your Criteo ad account.


