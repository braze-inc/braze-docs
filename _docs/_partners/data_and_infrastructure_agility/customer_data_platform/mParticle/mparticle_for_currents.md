---
nav_title: mParticle for Currents
page_order: 0.5
alias: /partners/mparticle_for_currents/

description: "This article outlines the partnership between Braze Currents and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: currents

---

# About mParticle & Currents

{% include video.html id="Njhqwd36gZM" align="right" %}

> [mParticle](https://www.mparticle.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

To get started, you must obtain the __mParticle Server to Server Key__ and __mParticle Server to Server Secret__. These can be obtained by navigating to your mParticle dashboard and creating the necessary feeds that allow mParticle to receive Braze interaction data for iOS, Android, and Web platforms. Once obtained, the Key and Secret must be added to the Braze Currents mParticle integration page. 

## mParticle Currents Integration 
### Create Feeds

Within the mParticle dashboard, you must create one feed per platform (iOS, Android, Web). mParticle also offers an unbound feed for events such as emails, that are not connected to an app platform.  

0. From your mParticle Admin account, navigate to __Inputs__ under __Setup__.<br><br>
1. Locate __Braze__ in the mParticle __Directory__ and add the Feed Integration.<br><br>
2. The Braze Feed Integration supports four separate feeds: iOS, Android, Web, and Unbound. You will need to create an input for each feed. You can create additional inputs from __Setup > Inputs__, on the __Feed Configurations__ tab.![mParticle Settings][1]<br><br>For each feed, under "Act as Platform" select the appropriate option from the list. If you do not see an option to select an "act-as" feed, the data will be treated as unbound, but can still be forwarded to data warehourse outputs.<br>![mParticle Settings][2]{: style="max-width:30%;"}  ![mParticle Settings][3]{: style="max-width:28%;"}<br><br>
3. As you create each input, mParticle will provide you with a Key and Secret. Copy these credentials, making sure to note which feed each pair of credentials is for.

### Finish mParticle Integration
To get started, navigate to the Braze dashboard, and select __Currents__ under Integrations. Next, create a new Current, and select __mParticle Data Export__. Here, you must select the apps you would like event tracking for, and provide the following information for each feed you created:

-   mParticle Server to Server Key
-   mParticle Server to Server Secret

Add this information to the mParticle integration page on the dashboard, and press __Launch Current__.

![mParticle]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
It's important to keep your mParticle API Key and mParticle Secret Key up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

All events sent to mParticle will include the user's `external_user_id` as the `customerid`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

### Integration Details

You can export the following data from Braze to mParticle:

{% tabs %}
{% tab Platform-Specific %}
| Event Name| Feed Type| Description| Currents Properties |
| --------- | -------- | ---------- | ------------------- |
| Push Notification Send| Platform-specific Feed | A push notification was successfully sent to a User.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Push Notification Open| Platform-specific Feed | User opened a push notification.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Push Notification Bounce| Platform-specific Feed | Braze was not able to send a push notification to this User.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| In-App Message Impression| Platform-specific Feed | User viewed an In-App Message.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| In-App Message Clicked| Platform-specific Feed | User tapped or clicked a button in an In-App Message.| `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Content Card Sent| Platform-specific Feed | A Content Card was sent to a user's device                                                | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Viewed| Platform-specific Feed | User viewed a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Clicked| Platform-specific Feed | User clicked a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Dismissed| Platform-specific Feed | User dismissed a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Viewed| Platform-specific Feed | User viewed the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Viewed| Platform-specific Feed | User viewed a Card within the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Clicked| Platform-specific Feed | User clicked on a Card within the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Application Uninstalled| Platform-specific Feed | User uninstalled the App.| `app_id`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% tab Unbound %}
| Event Name| Feed Type| Description| Currents Properties |
| --------- | -------- | ---------- | ------------------- |
| Email Sent| Unbound Feed| An email was successfully sent.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Delivered| Unbound Feed| An email was successfully delivered to a User’s mail server.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Opened| Unbound Feed| User opened an email.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Clicked| Unbound Feed| User clicked a link in an email. Email click tracking must be enabled.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Bounced| Unbound Feed| Braze attempted to send an email, but the User’s receiving mail server did not accept it. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Marked As Spam| Unbound Feed| User marked an email as spam.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Unsubscribed| Unbound Feed| User clicked the unsubscribe link in an email.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| SMS Sends| Unbound Feed| An SMS was sent to a user.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`|
| SMS Carrier Sends| Unbound Feed| An SMS was set to a carrier.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number` |
| SMS Deliveries| Unbound Feed| An SMS was delivered successfully.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number` |
| SMS Delivery Failures| Unbound Feed| An SMS unable to be delivered successfully.                                               | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| SMS Rejections| Unbound Feed| An SMS was rejected.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| SMS Inbound Received| Unbound Feed| An inbound SMS was received.| `inbound_phone_number`, `action`, `message_body` |
| Subscription Group State Change| Unbound Feed| User's subscription group state changed to 'Subscribed' or 'Unsubscribed'| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Webhook Sent| Unbound Feed| A webhook message was sent on behalf of a User.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Campaign Conversion Event| Unbound Feed| User performed the primary conversion event for a campaign within its conversion window.  | `campaign_id`|
| Campaign Enrollment in Control Group | Unbound Feed| User was enrolled in a campaign control group.| `campaign_id`|
| Canvas Conversion Event| Unbound Feed| User performed the primary conversion event for a Canvas within its conversion window.| `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Canvas Entry| Unbound Feed | User was entered into a Canvas.| `in_control_group`, `canvas_id`, `canvas_variation_id`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

To read more about the mParticle integration, visit their documentation [here](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
