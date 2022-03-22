---
nav_title: mParticle for Currents
article_title: mParticle for Currents
page_order: 0.5
alias: /partners/mparticle_for_currents/
description: "This article outlines the partnership between Braze Currents and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle for Currents

> [mParticle](https://www.mparticle.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and mParticle integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to mParticle to make it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| mParticle account | An [mParticle account](https://app.mparticle.com/login) is required to take advantage of this partnership. |
| Currents | In order to export data back into mParticle, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| mParticle server to server key<br><br>mParticle server to server secret | These can be obtained by navigating to your mParticle dashboard and creating the [necessary feeds](#step-1-create-feeds) that allow mParticle to receive Braze interaction data for iOS, Android, and Web platforms.|
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create feeds

From your mParticle admin account, navigate to **Setup > Inputs**. Locate **Braze** in the mParticle **Directory** and add the feed integration.

The Braze feed integration supports four separate feeds: iOS, Android, Web, and Unbound. The unbound feed can be used for events such as emails that are not connected to a platform. You will need to create an input for each main platform feed. You can create additional inputs from **Setup > Inputs**, on the **Feed Configurations** tab.

![][1]

For each feed, under **Act as Platform** select the matching platform from the list. If you do not see an option to select an **act-as** feed, the data will be treated as unbound, but can still be forwarded to data warehourse outputs.

![The first integration dialog box, prompting you to provide a configuration name, determine a feed status, and select a platform to act as.][2]{: style="max-width:40%;"}  ![The second integration dialog box showing the server-to-server key and server-to-server secret.][3]{: style="max-width:37%;"}

As you create each input, mParticle will provide you with a key and secret. Copy these credentials, making sure to note which feed each pair of credentials is for.

### Step 2: Create Current

In Braze, navigate to **Currents > + Create Current > Create mParticle Export**. Provide an integration name,  contact email and the mParticle API key and mParticle secret key for each platform. Next, select the events you want to track; a list of available events is provided below. Lastly, click **Launch Current**

![The mParticle Currents page in Braze. Here, you can find fields for integration name, contact email, API key, and secret key.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
It's important to keep your mParticle API Key and mParticle Secret Key up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

All events sent to mParticle will include the user's `external_user_id` as the `customerid`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

## Integration details

You can export the following data from Braze to mParticle:

{% tabs %}
{% tab Platform-Specific %}
| Event Name| Feed Type| Description| Currents Properties |
| --------- | -------- | ---------- | ------------------- |
| Push Notification Sends| Platform-specific Feed | A push notification was successfully sent to a User.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Push Notification Opens| Platform-specific Feed | User opened a push notification.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Push Notification Bounces| Platform-specific Feed | Braze was not able to send a push notification to this User.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| In-App Message Impressions| Platform-specific Feed | User viewed an In-App Message.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| In-App Message Clicks| Platform-specific Feed | User tapped or clicked a button in an In-App Message.| `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Content Card Sent| Platform-specific Feed | A Content Card was sent to a user's device                                                | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Viewed| Platform-specific Feed | User viewed a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Clicked| Platform-specific Feed | User clicked a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Content Card Dismissed| Platform-specific Feed | User dismissed a Content Card| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Views| Platform-specific Feed | User viewed the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Views| Platform-specific Feed | User viewed a Card within the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| News Feed Card Clicks| Platform-specific Feed | User clicked on a Card within the native Braze News Feed.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Application Uninstalled| Platform-specific Feed | User uninstalled the App.| `app_id`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% tab Unbound %}
| Event Name| Feed Type| Description| Currents Properties |
| --------- | -------- | ---------- | ------------------- |
| Email Sends| Unbound Feed| An email was successfully sent.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Deliveries| Unbound Feed| An email was successfully delivered to a User’s mail server.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Opens| Unbound Feed| User opened an email.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`, `machine_open`|
| Email Clicks| Unbound Feed| User clicked a link in an email. Email click tracking must be enabled. Link ID and Alias require Link Aliasing to be enabled | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `link_id`, `link_alias`, `user_agent`|
| Email Bounces| Unbound Feed| Braze attempted to send an email, but the User’s receiving mail server did not accept it. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Email Marks As Spam| Unbound Feed| User marked an email as spam.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`|
| Email Unsubscribes| Unbound Feed| User clicked the unsubscribe link in an email.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| SMS Sends| Unbound Feed| An SMS was sent to a user.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`|
| SMS Carrier Sends| Unbound Feed| An SMS was set to a carrier.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number` |
| SMS Deliveries| Unbound Feed| An SMS was delivered successfully.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number` |
| SMS Delivery Failures| Unbound Feed| An SMS unable to be delivered successfully.                                               | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| SMS Rejections| Unbound Feed| An SMS was rejected.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| SMS Inbound Received| Unbound Feed| An inbound SMS was received.| `inbound_phone_number`, `action`, `message_body` |
| Subscription Group State Change| Unbound Feed| User's subscription group state changed to 'Subscribed' or 'Unsubscribed'| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Webhook Sends| Unbound Feed| A webhook message was sent on behalf of a User.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Campaign Conversions| Unbound Feed| User performed the primary conversion event for a campaign within its conversion window.  | `campaign_id`|
| Campaign Control Group Enrollments | Unbound Feed| User was enrolled in a campaign control group.| `campaign_id`|
| Canvas Conversions| Unbound Feed| User performed the primary conversion event for a Canvas within its conversion window.| `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Canvas Entries| Unbound Feed | User was entered into a Canvas.| `in_control_group`, `canvas_id`, `canvas_variation_id`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

To read more about the mParticle integration, visit their documentation [here](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
