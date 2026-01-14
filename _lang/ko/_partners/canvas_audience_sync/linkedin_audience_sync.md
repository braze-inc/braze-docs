---
nav_title: LinkedIn
article_title: Canvas Audience Sync to LinkedIn
alias: /linkedin_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to LinkedIn to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
page_order: 4

---

# Audience Sync to LinkedIn

Using the Braze Audience Sync to LinkedIn, brands can add user data from their Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (push, email, SMS, webhook, etc.) in a Braze Canvas based on your user data can now trigger an ad to that user in your LinkedIn customer lists.

**Common use cases for Audience Syncing include**:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand

This feature allows brands to control what specific first-party data is shared with LinkedIn. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

{% alert important %}
Audience Sync to LinkedIn is currently in beta. Contact your Braze account manager if you want to participate in the beta.
{% endalert %}

## Prerequisites

You must make sure that you have the following items created, completed, or accepted before setting up your LinkedIn Audience Sync step in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| LinkedIn ad account | [LinkedIn](https://www.linkedin.com/campaignmanager) | An active LinkedIn ad account tied to your brand.<br><br>Make sure that you have accepted any relevant LinkedIn terms and conditions to access and use that account and that your LinkedIn admin has granted you the appropriate permissions to manage Audiences. |
| LinkedIn Terms & Policies | LinkedIn | Agree to comply with any of LinkedIn’s required terms, policies, guidelines, and documentation related to your use of the LinkedIn Audience Sync, including any terms, policies, guidelines, and documentation incorporated by reference therein, which may include LinkedIn’s: Services Terms, Ads Agreement, Data Processing Agreement, and Professional Community Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Step 1: Connect to LinkedIn

In the Braze dashboard, go to **Technology Partners** and select **LinkedIn**. In the **LinkedIn Audience Sync** section, select **Connect LinkedIn**.

![LinkedIn technology page in Braze includes an Overview section and LinkedIn Audience Sync section with the Connected LinkedIn button.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

You’ll then be redirected to the LinkedIn OAuth page to authorize Braze for the permissions related to your Audience Sync integration. After you have selected **Confirm**, you’ll be redirected back into Braze to select which LinkedIn ad accounts you wish to sync to. 

!["Braze Self Service" is selected as the ad account to connect.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Once you have successfully connected, you will be returned to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![A successfully connected LinkedIn account.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Your LinkedIn connection will be applied at the Braze workspace level. If your LinkedIn admin removes you from your LinkedIn ad account, Braze will detect an invalid token. As a result, your active Canvases using LinkedIn will show errors, and Braze will not be able to sync users.

### Step 2: Configure your Canvas entry criteria

When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and to comply with privacy laws, such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options. 

If you have collected the [iOS IDFA through the Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), you will be able to use the **Ads Tracking Enabled** filter. Select the value as `true` to only send users into Audience Sync destinations where they have opted in. 

![An entry audience with the filter "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

If you are collecting `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

![A Canvas with an entry audience of "opted_in_marketing" equals "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

To learn more on how to comply with these Data Protection laws within the Braze platform, see [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance/).

### Step 3: Add an Audience Sync step with LinkedIn

Add a component in your Canvas and select Audience Sync. Click on the **Custom Audience** button to open the component editor.

![The Canvas editor with the list of available components.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![The selected Audience Sync component.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Step 4: Sync setup

Select **LinkedIn** as the desired Audience Sync partner.

![The "Set up Audience Sync" details with the multiple partners to choose from.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Then select the desired LinkedIn ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience.

![Audience Sync to LinkedIn with Braze selected as the ad account.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Create a New Audience %}

**Create a New Audience**<br>
Enter a name for the new audience, select **Add Users to Audience**, and select which fields you would like to sync with LinkedIn. For this integration, we currently support the following: 
- Email
- First and Last name
- Android GAID

Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![An example "leads" audience with the selected Braze ad account, "leads" audience, the action to add users to the audience, and email, Android GAID, and first and last name as fields to match.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![Confirmation that the "leads" audience was created.]({% image_buster /assets/img/linkedin/linkedin9.png %})

When you launch a Canvas with a new audience, Braze syncs users in near real-time as they enter the Audience Sync component.

{% endtab %}
{% tab Sync with an Existing Audience %}

**Sync with an Existing Audience**<br>
Braze also offers the ability to add users to existing LinkedIn audiences to confirm that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and **Add to the Audience**. Braze will then add users in near real-time as they enter the Audience Sync component.

![Expanded view of the Custom Audience Canvas step. Here, the desired ad account and existing audience are selected.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Audience Sync to LinkedIn, simply launch the Canvas! The new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on LinkedIn. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

You can view the audience on LinkedIn by going into your ad account and selecting **Audiences** under the **Assets** section of the navigation. From the **Audiences** page, you can see each audience's size after reaching more than 300 members.

![LinkedIn page listing the following metrics for the given audience.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## User syncing and rate limit considerations

As users reach the Audience Sync Step, Braze will sync these users in near real-time while respecting LinkedIn’s API rate limits. In practice, Braze will try to batch and process as many users every 5 seconds before sending these users to LinkedIn.

LinkedIn’s API rate limit states no more than ten queries per second and 100,000 users per request. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to about 13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| METRIC | DESCRIPTION |
| ------ | ----------- | 
| Entered | Number of users who entered this component to be synced to LinkedIn. |
| Proceeded to Next Step | How many users advanced to the next component if there is one? All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to LinkedIn. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into LinkedIn. |
| Users Errored | Number of users who were not synced to LinkedIn due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid LinkedIn token or if the audience was deleted on LinkedIn. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

{% alert important %}
LinkedIn provides additional metrics around match rates within their platform. To review the match of your specific Audience Sync, select the Audience Sync step metrics to go into the **Canvas Step Details** page.
<br><br>
Select the partner as **LinkedIn**, your ad account, and the audience to see the audience size and match rate from LinkedIn.

![An example of Audience Sync step metrics with 10,000 entered users.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Frequently asked questions

### How long will it take for the audience sizes to populate in LinkedIn?

There is up to a 48-hour delay to view the audiences within your LinkedIn account.

### What is the minimum audience size for LinkedIn to populate within your ad account?

The audience must include at least 300 members to populate the audience size within your LinkedIn account.

### What should I do next if I receive an invalid token error?

You can disconnect and reconnect your LinkedIn account on the LinkedIn partner page. Confirm with your LinkedIn admin that you have the appropriate permissions to the ad account you wish to sync with.

### Why is my Canvas not allowed to launch?

Confirm your LinkedIn ad account has successfully connected to Braze on the LinkedIn partner page. Next, make sure you've selected an ad account, entered a name for the new audience, and selected fields to match.

### How do I know if users have matched after passing users to LinkedIn?

LinkedIn does provide information around match rates in their dashboard. You can review it on LinkedIn under the **Audiences** section. You can review the match rate for your LinkedIn Audience in the Canvas step details of your Audience Sync step.

### How many audiences can LinkedIn support?

Currently, there is no limit on the number of audiences in your LinkedIn ad account.

### Why is a segment stuck in BUILDING status and not updated?

A segment is considered unused and set to ARCHIVED after it is not continuously used for 30 days in a draft or active campaign. Because of this, a segment may appear "stuck" in BUILDING when updates are streamed to an ARCHIVED segment, thus pushing it into the BUILDING state, and right before it is archived again, new updates are streamed to the unused segment.


