---
nav_title: Setting Up Currents
page_order: 0

page_type: tutorial
description: "This page outlines and describes the generic process for integrating and configuring Braze Currents."
tool: currents
---

# Setting Up Currents

> This page outlines and describes the generic process for integrating and configuring Braze Currents.

{% alert important %}
Currents are included with certain Braze packages. Please contact your Braze representative if you have any questions or want to gain access.
{% endalert %}

## Requirements

Using Currents with any of our partners requires the same basic parameters and connection methodology.

Each partner requires that Braze has permission to write and send data files to them, and Braze asks for the location they should write those files to, specifically bucket names or keys.

The following requirements are the basic, minimum requirements to integrate with most of our partners. Some partners will require additional parameters, but those will be listed on [those partners pages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) along with any nuances associated with these basic requirements.

| Requirement | Origin | Access | Description
|---|---|---|---|
| Account with Partner | Arrange account with that partner or reach out to your Braze account manager for suggestions. | Check that Partner’s site or reach out to that Partner to sign up. | Braze will not send data to a Partner if you don’t have access to that data through your company’s account.
| Partner API Key or Token | Usually the Partner’s dashboard. | Just copy and paste it into the designated Braze field. | Braze has a designated field for this in the Integrations page for that Partner. We need this to map where we are sending your data. It's important to keep your Partner Keys/Tokens up to date; invalid credentials may result in disabling your connector, and dropping events.
| Authentication Code/Key, Secret Key, Certification File | Contact a representative for your account with that Partner. May also exist in the Partner’s dashboard. | Copy and paste keys into the designated Braze field. Generate and upload `.json` or other certification files into the appropriate place in Braze. | Braze has a designated field for this in the Integrations page for that Partner. This gives Braze credentials and authorizes us to write files to your Partner account. It's important to keep your authentication detials up to date; invalid credentials may result in disabling your connector, and dropping events.
| Bucket, Folder Path | Some partners organize and sort data by buckets. This should be found in the Partner’s dashboard. | If this is required, be sure to copy the Bucket name or file path exactly into the designated space in Braze. We don’t want your data to get lost! | Though this is required for some Partners, it’s important to get right when you do need it. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Step 1: Choose Your Partner

Braze Currents allows you to integrate through Data Storage using flat files or to our Behavioral Analytics and Customer Data partners using a batched JSON payloads to a designated endpoint.  

Before you begin your integration, it’s best to decide which integration is best for your purposes. For example, if you already utilize mParticle and Segment and would like Braze data to stream there, it would be best to use a batched JSON payload. If you would prefer to manipulate the data on your own or have a more complex system of data analysis, it might be best to use Data Storage ([Braze uses this method]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!)

## Step 2: Navigate to Currents
To get started, visit the Currents page in the left sidebar, in the "Integrations" section of the Dashboard. You'll be taken to the Currents integration management page.

![Currents]({% image_buster /assets/img_archive/currents-main-page.png %})

## Step 3: Add Partner
Add a partner, sometimes called a "Currents connector", by clicking the dropdown at the top right of the screen.

![Adding an Integration]({% image_buster /assets/img/new_current.png %}){: height="50%" width="50%"}

Each partner requires a different set of configuration steps. To enable each integration, [see the instructions in their respective pages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

## Step 4: Configure Events

Choose the events you wish to pass to that partner by checking from the available options. You can find listings of these events in our [Customer Behavior Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) and [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) libraries.

If needed, you can learn more about our events in our [Event Delivery Semantics]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/) article.

## Step 5: Test Your Integration

You may test your integration or take a look at the sample Currents data in [our Currents Examples Github repo](https://github.com/Appboy/currents-examples).

{% alert important %}
Please note that Currents will drop events with excessively large payloads of greater than 900KB. 
{% endalert %}
