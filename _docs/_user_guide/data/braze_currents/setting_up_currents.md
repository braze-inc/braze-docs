---
nav_title: Setting up Currents
article_title: Setting Up Currents
page_order: 0
page_type: tutorial
description: "This how-to article walks you through the process for integrating and configuring Braze Currents."
tool: Currents
search_rank: 8
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Setting up Currents

> This page outlines and describes the generic process for integrating and configuring Braze Currents.

{% alert important %}
Currents are included with certain Braze packages. Contact your Braze representative if you have any questions or want to gain access.
{% endalert %}

## Requirements

Using Currents with any of our partners requires the same basic parameters and connection methodology.

Each partner requires that Braze has permission to write and send data files to them, and Braze asks for the location they should write those files to, specifically bucket names or keys.

The following requirements are the basic, minimum requirements to integrate with most of our partners. Some partners will require additional parameters, which are listed in their respective [partner documentation]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) along with any nuances associated with these basic requirements.

| Requirement | Origin | Access | Description
|---|---|---|---|
| Account with partner | Arrange account with that partner or reach out to your Braze account manager for suggestions. | Check that partner's site or reach out to that partner to sign up. | Braze will not send data to a partner if you don't have access to that data through your company's account.
| Partner API Key or Token | Usually the partner's dashboard. | Just copy and paste it into the designated Braze field. | Braze has a designated field for this in the integrations page for that partner. We need this to map where we are sending your data. **It's important to keep your Partner Keys or Tokens up to date; invalid credentials may result in disabling your connector, and dropping events.**
| Authentication Code/Key, Secret Key, Certification File | Contact a representative for your account with that partner. May also exist in the partner's dashboard. | Copy and paste keys into the designated Braze field. Generate and upload `.json` or other certification files into the appropriate place in Braze. | Braze has a designated field for this in the integrations page for that partner. This gives Braze credentials and authorizes us to write files to your partner account. **It's important to keep your authentication details up to date; invalid credentials may result in disabling your connector, and dropping events.**
| Bucket, Folder Path | Some partners organize and sort data by buckets. This should be found in the partner's dashboard. | If this is required, be sure to copy the bucket name or file path exactly into the designated space in Braze. We don't want your data to get lost! | Though this is required for some partners, it's important to get right when you do need it. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
It's important to keep your Partner Keys, Partner Tokens, and authentication details updated; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

## Setting up Currents

### Step 1: Choose your partner

Braze Currents allows you to integrate through Data Storage using flat files or to our behavioral analytics and customer data partners using a batched JSON payloads to a designated endpoint.  

Before you begin your integration, it's best to decide which integration is best for your purposes. For example, if you already use mParticle and Segment and would like Braze data to stream there, it would be best to use a batched JSON payload. If you would prefer to manipulate the data on your own or have a more complex system of data analysis, it might be best to use Data Storage ([Braze uses this method]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!)

### Step 2: Open Currents

To get started, go to **Partner Integrations** > **Data Export**. You'll be taken to the Currents integration management page.

![Currents page in the Braze dashboard]({% image_buster /assets/img_archive/currents-main-page.png %})

### Step 3: Add your partner

Add a partner, sometimes called a "Currents connector," by selecting the dropdown at the top of the screen.

Each partner requires a different set of configuration steps. To enable each integration, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) and follow the instructions on their respective pages.

### Step 4: Configure your events

Choose the events you wish to pass to that partner by checking from the available options. You can find listings of these events in our [Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) and [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) libraries.

![]({% image_buster /assets/img/current4.png %})

If needed, you can learn more about our events in our [event delivery semantics]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/) article.

### Step 5: Set up field transformations

You can use Currents field transformations to remove or hash a string field.

- **Remove:** Replaces the string field with `[REDACTED]`. This is helpful if your partner rejects events with missing or empty fields.
- **Hash:** Applies an SHA-256 hashing algorithm to the string field.

Selecting a field for one of these transformations will apply that transformation to all events in which that field appears. For example, selecting `email_address` for hashing will hash the `email_address` field in Email Send, Email Open, Email Bounce, and Subscription Group State Change events.

![Adding field transformations]({% image_buster /assets/img/current3.png %})

### Step 6: Test your integration

{% alert important %}
Currents will drop events with excessively large payloads of greater than 900&nbsp;KB. 
{% endalert %}

Before you test, consider checking out our [sample Currents data in GitHub](https://github.com/Appboy/currents-examples). When you're ready to test, you choose an option below:

#### Sending test events

To test your integration, you can select **Send Test Events** to send one event from each of your selected event types to this Current. For detailed information about each event type, refer to our [Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) and [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) libraries.

![The "Currents Test" page in the Braze dashboard.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Testing Currents connectors

Test Currents connectors are free versions of our existing connectors that can be used for testing and trying out different destinations. Test Currents have:

- No limit to the number of Test Currents connectors you may build.
- An aggregate maximum of 10,000 events per seven-day rolling period. This event total is updated hourly on the dashboard.

After your Test Currents connectors reach the sending limit, your connector will not send events until the next seven-day period.

To upgrade your Test Currents connector, edit the integration in the dashboard and select **Upgrade Test Integration**.

## Updating Currents

{% multi_lang_include updating_currents.md %}

## IP allowlisting

Braze will send Currents data from the listed IPs:

{% multi_lang_include data_centers.md datacenters='ips' %}
