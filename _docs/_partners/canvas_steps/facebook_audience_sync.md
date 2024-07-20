---
nav_title: Facebook
article_title: Canvas Audience Sync to Facebook
description: "This reference article will cover how to use Braze Audience Sync to Facebook, to deliver advertisements based upon behavioral triggers, segmentation, and more."
page_order: 1
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Audience Sync to Facebook

Using the Braze Audience Sync to Facebook, brands can elect to add their own users' data from their own Braze integration to Facebook Custom Audiences to deliver advertisements based upon behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (Push, Email, SMS, Webhook, etc.) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in Facebook via Custom Audiences.

**Common use cases for syncing Custom Audiences include**:

- Targeting high-value users via multiple channels to drive purchases or engagement.
- Retargeting users who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand.
- Creating Lookalike Audiences to acquire new users more efficiently.

This feature gives brands the option to control what specific first-party data is shared with Facebook. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).

## Prerequisites

You will need to confirm that you have the following items created and completed before setting up your Facebook Audience Step in Canvas. 

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | A centralized tool to manage your brand's Facebook assets (for example, ad accounts, pages, apps). |
| Facebook Ad Account | [Facebook](https://www.facebook.com/business/help/910137316041095) | An active Facebook ad account tied to your brand's business manager.<br><br>Ensure that your Facebook business manager admin has granted you either "Manage Campaigns" or "Manage ad accounts" permissions to the Facebook ad accounts you plan to use with Braze. Also ensure that you have accepted your ad account terms and conditions. |
| Facebook Custom Audiences Terms | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Accept Facebook's Custom Audiences Terms for your Facebook ad accounts you plan to use with Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

### Step 1: Connect to Facebook

In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Facebook**. In the Facebook Audience Export module, click **Connect Facebook**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Technology Partners** under **Integrations**.
{% endalert %}

![Facebook technology page in Braze that includes an Overview module and Facebook Audience Export module with the Connected Facebook button.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

A Facebook oAuth dialog window will appear to authorize Braze to create Custom Audiences into your Facebook ad accounts.

![The first facebook dialogue box prompting to "Connect as X", where X is your Facebook username.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![The second Facebook dialogue box prompting for permission to manage ads for your ad accounts.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Once you have linked Braze to your Facebook account, you will then be able to select which ad accounts you would like to sync within your Braze workspace. 

![A list of available ad accounts you can connect to Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}

Once you have successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.

![An updated version of the Facebook technology partners page showing the ad accounts successfully connected.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}

Your Facebook connection will be applied at the Braze workspace level. If your Facebook admin removes you from your Facebook Business Manager or access to the connected Facebook accounts, Braze will detect an invalid token. As a result, your active Canvases using Facebook Audience components will show errors, and Braze will not be able to sync users. 

{% alert important %}
For customers who have previously undergone the Facebook App Review process for [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) and [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), your System User Token will still be valid for the Facebook Audience component. You will not be able to edit or revoke the Facebook System User Token through the Facebook partner page. Instead, you can connect your Facebook account to replace your Facebook System User Token within your Braze workspace. 

<br><br>The Facebook oAuth configuration will also apply to [Facebook exports via Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites). 
{% endalert %}

### Step 2: Accept custom audiences terms of service

Before building out your Canvas, you must first accept the Facebook custom audiences terms of service. Your terms of service can be found at the following link:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### Step 3: Add a Facebook Audience component in Canvas Flow

Add a component in your Canvas and select **Facebook Audience**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Step 4: Sync setup

Click on the **Custom Audience** button to open the component editor.

Select **Facebook** as the desired Audience Sync partner.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Select the desired Facebook ad account. Under the **Choose a New or Existing Audience** dropdown, type in the name of a new or existing audience. 

{% tabs %}
{% tab Create a New Audience %}
**Create a New Audience**<br>
Enter a name for the new custom audience, select **Add Users to Audience** and select which fields you would like to sync with Facebook. Next, save your audience by clicking the **Create Audience** button at the bottom of the step editor.

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Next, save your audience by clicking the Create Audience button at the bottom of the step editor. Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

When you launch a Canvas with a new audience, Braze will create the new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Audience Sync Step.

{% endtab %}
{% tab Sync with an Existing Audience %}
**Sync with an Existing Audience**<br>
Braze also offers the ability to either add or remove users from existing Facebook custom audiences to confirm that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and choose whether you want to **Add to the Audience** or **Remove from the Audience**. Braze will then either add or remove users in near real-time as they enter the Facebook Audience step. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

It's important to note that Facebook prohibits removing users from custom audiences where the audience sizes are too low (typically fewer than 1,000). As a result, Braze will be unable to sync users for a Remove from Audience step until the audience reaches the appropriate audience size.

{% endtab %}
{% endtabs %}

### Step 5: Launch Canvas

Once you have configured your Facebook Audience component, simply launch the Canvas! The new custom audience will be created, and users who flow through the Facebook Audience component will be passed into this custom audience on Facebook. If your Canvas contains subsequent components, your users will then advance to the next step in their user journey.

The **History** tab of the custom audience in the Facebook Audience Manager will reflect the number of users sent to the audience from Braze. If a user re-enters the step, they will be sent to Facebook again.

![Audience details and the History tab for a given Facebook audience that includes an Audience History table with columns for the activity, activity details, items changed, and the date and time.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Migrating to Meta work accounts

Starting in July 2023, Meta is rolling out Meta work accounts to a small set of businesses who are interested in adopting this new account type. If you have a Business Account integrated with Braze, make sure you disconnect and reconnect to the [Facebook partner page]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) with your Business Account in order to perserve this implementation and not disrupt any active Canvases.

## User syncing and rate limit considerations
 
As users reach the Audience Sync Step, Braze will sync these users in near real-time while also respecting Facebook's Marketing API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to Facebook. 

Facebook's Marketing API rate limit states no more than &#126;190k API requests for each ad account in a 1 hour time period. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to &#126;13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Facebook. |
| Proceeded to Next Step | How many users advanced to the next component if there is one. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to Facebook. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into Facebook. |
| Users Errored | Number of users who were not synced to Facebook due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid Facebook token or if the custom audience was deleted on Facebook. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is a Facebook step. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}   

## Troubleshooting

{% details What should I do next if I receive an invalid token error? %}
You can simply disconnect and reconnect your Facebook account on the Facebook partner page. Confirm with your Facebook Business Manager Admin that you have the appropriate permissions to the ad account you wish to sync with.
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
At this time, value-based custom audiences are not supported by Braze. If you are interested in syncing these types of custom audiences, submit [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details How do I resolve an issue with syncing a value-based lookalike custom audience? %}

At this time, value-based lookalike custom audiences are not supposed by Braze. If you attempt to sync to this audience, this can cause errors for your Audience Sync step. To resolve this, follow these steps:

1. Go to your Facebook Ad Manager dashboard and select **Audiences**.
2. Select **Create audience** > **Custom audience**.
3. Select **Customer list**.
4. Upload your CSV or list without the **Value** column. Select **No, continue with a customer list that doesn't include customer value**.
5. Finish creating your custom audience.
6. In Braze, update the Facebook Audience Sync step with the custom audience you created.
{% enddetails %}

{% details I’ve received an email related to Facebook custom audience terms of service. What should I do to resolve this? %}
In order to use Audience Sync to Facebook, you will need to ensure that you have accepted these terms of service agreement. 

If your ad account is directly associated with your personal Facebook account, follow this link and accept the TOS: [https://www.facebook.com/ads/manage/customaudiences/tos.php](https://www.facebook.com/ads/manage/customaudiences/tos.php)

If your ad account is tied to your company's Business Manager account you will also need to accept the TOS from within your business manager account. following this link:<br>
[https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID](https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID)

Once you have accepted your Facebook custom audiences terms of service, you will need to do the following:
1. Refresh your Facebook access token with Braze by disconnecting and reconnecting your Facebook account.
2.  Re-enable your Facebook Audience Sync step by editing and updating your Canvas.
Braze will then be able to sync users as soon as they reach the Facebook audience step.
{% enddetails %}


