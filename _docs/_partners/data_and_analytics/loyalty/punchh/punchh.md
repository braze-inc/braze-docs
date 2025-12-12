---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "This reference article outlines the partnership between Braze and Punchh, a loyalty and engagement platform, enabling you to sync data across the two platforms. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) is an industry-leading loyalty and engagement platform that enables brands to deliver omnichannel customer loyalty programs both in-store and digitally. 

_This integration is maintained by Punchh._

## About the integration

The Braze and Punchh integration allows you to sync data for gifting and loyalty purposes across the two platforms. Data published in Braze will be available for segmentation and can sync user data back into Punchh via Braze webhooks.

## What are the benefits?

- Ingest loyalty data from Punchh to Braze in real-time. 
- Leverage and layer powerful audience data from Braze to deliver meaningful and dynamic cross-channel experiences (app, mobile, web, email, and SMS)
  - Did customers open emails? Did customers open the app near a store?
- Standardize the look and feel of transactional emails sent through Braze.
- Create journeys that allow for A/B testing and optimization as you go.

## Prerequisites

| Requirement | Description |
|---|---|
| Punchh account | You need an active Punchh account to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## What else should I know?

#### Before integrating

- When utilizing the Braze integration, two campaigns will be required, one in Punchh and the second in Braze. For example, if you send a campaign with an offer attached, the gifting campaign will be configured within Punchh, and the notification can be sent from Braze.
- Guests should already exist in Punchh and Braze. Punchh will filter out any customer who is not already a loyalty guest.

#### Important things to note

- Punchh has added the ability to disable the sending of default user attributes to Braze, so the customer does not incur data point overages. This is configured during the adapter setup.
- If using custom segments on recurring campaigns, the campaign name must be used instead of the campaign ID, as the IDs change each time the campaign runs.
- Communication channels available within each Punchh gifting campaign include rich messages, push notifications, SMS, and email.
- After users have been sent to a Punchh custom segment from Braze, they can't be removed. Only new guests can be added to an existing custom segment. If guests need to be removed from an existing Punchh custom segment, a new webhook campaign will need to be created in Braze to send users to a new Punchh custom segment.

## Integration

Punchh offers several endpoints available to Braze customers to help add external IDs to the Punchh platform using the following Punchh API endpoints. After the external IDs have been added, create an adapter in Punchh, provide your Braze credentials, and select which events you'd like to sync. Next, you can take the Punchh segment ID and use it to build a Punchh webhook to trigger customer syncing in a Canvas journey.

Note that the Punchh `user_id` and Braze `external_id` need to be available in either platform for the integration to sync properly. 
- Events sent from Punchh to Braze will include the Braze `external_id` as the identifier. If Punchh is configured to use the `external_source_id`, that value will be set as the Braze `external_id`. Otherwise, the integration will default to setting the Punchh `user_id` as the Braze `external_id`.
- To send webhooks from Braze to Punchh, the Punchh `user_id` must be available on the Braze user profile. If Punchh `user_id` is not used as the Braze `external_id`, it should be set as a custom attribute "punchh_user_id". 

### Step 1: Set up external ID ingestion endpoints (optional)

External IDs from Braze can be added using the following endpoints for new and existing Punchh users.

{% alert important %}
The `external_source` and `external_source_id` field values must be unique to Punchh and not associated with existing profiles.
{% endalert %}

1. New Punchh users<br>
Create new users in Punchh with a Punchh sign-up endpoint using the `external_source` and `external_source_id` fields. Punchh allows external identifiers to be sent with a user profile via one of the following sign-up endpoints:
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO Signup API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Existing Punchh users <br>
Update `external_source_id` for existing Punchh users. Punchh allows external identifiers to be added to a profile via a user API update endpoint: 
- [Mobile User Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO User Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab User sign-up API example %}
This example allows you to send external identifiers with a user profile at sign-up time. This is done by sending `external_source` as "customer_id" and `external_source_id` as "111111111111111111" as a string data type.

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab User update API example %}
This example allows you to update external identifiers with a user profile. This is done by sending `external_source` as "customer_id" and `external_source_id` as "111111111111111111" as a string data type.

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Platform configuration:** To enable external identifiers in Punchh, from the Punchh dashboard, navigate to **Cockpit** > **Dashboard** > **External User Identifier**.
{% endalert %}

### Step 2: Braze adapter setup in Punchh

#### Available events to sync {#available-events-to-sync}

1. **Guest:** Triggered upon any signup, update to guest profile, deactivated or deleted
2. **Loyalty Check-in:** Triggered for loyalty transactions or earning by scanning barcode from the receipt
3. **Gift Check-in:** Triggered for points gifted from a campaign
4. **Redemption:** Triggered in case of any reward redemption excluding Punchh coupons, as those would be sent separately as coupon events, including issuance as well as redemption
5. **Rewards:** Triggered from rewards gifted from campaigns, activity, conversion from points to rewards, or admin gifting
6. **Transaction Notifications:** Triggered upon transactional activity for a user within the Punchh system (for example, point expiration)
7. **Marketing Notifications:** Triggered based on different campaign setups in Punchh for an associated segment of users

{% alert note %}
Reference Punchh documentation on what sample payloads for these available events may look like. 
{% endalert %}

Work with your Punchh Implementation manager to set up this adapter.

To set up the Braze and Punchh integration, do the following:

1. In the Punchh dashboard, navigate to **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management** and toggle on **Enable Webhook Management**.<br><br>
2. Next, enable adapters by navigating to **Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab** and toggle on **Show Adapters Tab**.<br><br>
3. Navigate to **Webhooks Manager** under the **Settings** tab, select the **Adapters** tab, and click **Create Adapter**. <br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Fill in the adapter name, description, and admin email. Select **Braze** as your adapter and provide your Braze REST API endpoint and Braze API key.<br><br>
5. Next, select the available events you would like to enable. A list of these events can be found in [Available events to sync](#available-events-to-sync).<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Click **Submit** to enable the webhook.

## Create Punchh webhook in Braze

Braze can add users to a Punchh segment through webhooks utilizing Punchh Custom Segments.

1. Create a custom segment in Punchh and note the `custom_segment_id` present in the Punchh segment dashboard URL as shown below. Both classic or beta segment builders can be used. However, beta is recommended as classic will eventually be deprecated.<br><br>In the Punchh platform, navigate to **Guest** > **Segment** > **Custom List** > **New Custom List**.<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Create a webhook campaign in Braze using the Punchh endpoint for adding a user to a custom segment as the webhook URL. Here, you can provide the `custom_segment_id` pulled from the URL and `user_id` as key-value pairs.<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. This webhook can be set up as a singular campaign or as a step within a Canvas. Alternatively, if the webhook adding users to this specific Punchh segment will be used in multiple campaigns or Canvases, it can be set up as a [template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template).<br><br>
The `user_id` key within the webhook maps to the Punchh user ID. This identifier will need to be added to all webhooks created in Braze to add users to a Punchh custom segment. The `punch_user_id` custom attribute can be dynamically populated as the value for the `user_id` key using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). You can insert the `punchh_user_id` custom attribute variable using the blue "plus" icon located on the top-right of any templated text field.<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. After the webhook is saved, it can be used to sync users, as shown below. For example, 136 guests would be added to the Punch custom segment when this Braze webhook campaign is launched.<br><br>![An example of syncing users using the saved webhook due to Braze and Punchh integration.]({% image_buster /assets/img/punchh/punchh6.png %})

For more information on how webhooks are used at Braze, check out [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

## Use case campaigns

### Campaign and Canvas configuration

#### Triggering

Use cases for Braze messaging triggered by Punchh events being sent to Braze, such as reward events or guest events, can be created as [action-based campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) or Canvases triggered by the relevant Punchh event.

Adding a trigger will pull up the list of events created in Braze. Choose the event that should trigger your campaign or Canvas to be sent to the user who logged the event.

![]({% image_buster /assets/img/punchh/update5.png %})

Property filters can be added to further filter the triggering event. For example, the message should only be triggered when a customer triggers the "checkins_gift" event where the approved event property is `true`. This is an optional feature that may not be applicable to all use cases. 

#### Segmentation

In many cases, Braze campaigns and Canvases being triggered by Punchh events can be set to an "All Users" audience because the segmentation of users triggering these events is determined within Punchh. However, customers looking to further refine the audience of users who will receive the Braze messaging triggered by the event can do so by adding additional filters and segments in the **Target Audiences** section of the campaign composer or the **Entry Audience** of the Canvas composer. 

### Use cases

{% tabs local %}
{% tab Signup %}
#### Sign-up campaign

When utilizing the Braze configuration for a sign-up campaign with an offer attached, a sign-up gifting campaign will need to be configured within Punchh and a welcome message in Braze. 

Punchh recommends that an execution delay be added to the sign-up campaign, so Braze can first trigger the welcome message based on the guest event. If you want to send a follow-up message informing the user that they have been gifted, you can trigger this based on the reward event.

In the case of a sign-up campaign, all signed up can be used for the segment; therefore, a custom Braze segment will not be required.

Punchh configurations required:
- Campaign: Sign-up 
- Segment: All signed up
- Reward: Customer choice
Events required:
- Reward event
- Guest event
Considerations:
- Execution delay, recommend that the guest add a 5–10-minute delay

![A user segment is configured in punch, and guests sign up for a loyalty program. After this, the guest event, if triggered, and the Braze messaging campaign is triggered. Next, the Punchh sign-up gifting campaign is triggered after 10 minutes, triggering the reward event and optional follow-up message.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze welcome %}
#### Braze welcome campaign

When a new user signs up, Punchh sends Braze a Guest event that creates the user and sends a custom attribute `signup_channel`, which you can use to trigger the Braze welcome campaign.

To set up the Braze welcome campaign, follow these steps:

1. In Braze, create an action-based campaign.
2. For the trigger, select **Change Custom Attribute Value** with the custom attribute `signup_channel` set to **Any new value**.
3. Continue creating your campaign, then send when ready!

{% endtab %}
{% tab Mass offer %}
#### Mass offer campaign

When utilizing a mass offer campaign for gifting, a mass offer campaign will need to be configured within Punchh and a messaging campaign in Braze.

If you want to utilize a Braze segment for your campaign or send communication from Braze before gifting guests in the Punchh platform, then a [custom Punchh segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) will be required for the Punchh gifting campaign. 

Creating the segment of users to receive this offer in Braze is only recommended when using attributes unavailable within Punchh. Otherwise, Punchh segmentation can be used, and the Braze messaging campaign will be created as an action-based campaign triggered by the users receiving their reward (the reward event triggered by Punchh).

Punchh configurations required:
- Campaign: Mass offer
- Segment: Custom list or customer choice
- Reward: Customer choice

**Using Punchh for segmentation and gifting, and Braze for messaging:**<br>
For example, a $2 off reward is sent to a segment configurable within Punchh with messaging sent through Braze.<br>
![A user segment can be configured in Punchh, and users receive a gift through a Punchh mass offer campaign. Next, a reward event is triggered, and then the Braze messaging campaign is triggered.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Using Braze segmentation and messaging, and Punchh for gifting:**<br>
For example, a $2 off reward and messaging sent to a segment with attributes not available in Punchh.<br>
![A user segment can be configured in Braze, and then a message can be sent from a Braze-to-Braze segment. Next, the users are sent to the Punchh custom segment through a Braze webhook with segment and user ID. After this, the user receives a gift through Punchh mass offer campaign with a custom segment. After this the reward event is triggered.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Using Braze segmentation and Punchh for gifting or messaging, or both:**<br>
For example, a $2 off reward is sent to a segment with attributes not available in Punchh, but no messaging is required, or the messaging can be sent through Punchh (note that all guests must be present in Punchh).<br>
![A user segment can be configured in Braze, and the users are sent to Punchh custom segment through a Braze webhook with segment and user ID. After this, the user receives a gift through Punchh mass offer campaign with a custom segment. After this the reward event is triggered.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Recurring mass offer %}
#### Recurring mass offer campaign

When utilizing a recurring mass offer campaign for gifting, a mass offer campaign will need to be configured within Punchh and a messaging campaign set up in Braze. A Punchh custom segment will be required if the customer wants to use Braze segmentation (only recommended if utilizing attributes unavailable within Punchh). Otherwise, Punchh segmentation can be used, and the Braze messaging campaign will be triggered based on the reward event.

Punchh configurations required:
- Campaign: Recurring mass offer
- Segment: Custom list or customer choice
- Reward: Customer choice
Considerations:
- Campaign IDs and campaign names are sent to Braze as an event property on the event. If you want to use a Punchh campaign identifier in Braze to further filter the audience receiving the campaign, you must use the campaign name because the campaign IDs change daily.

{% endtab %}
{% tab Post check-in offer with notification %}
#### Post check-in offer campaign with notification

When utilizing a post check-in offer campaign, Braze will send the notification regarding the gifting, and when the guest makes a check-in, they will then be gifted from the Punchh post check-in campaign. Therefore, a post check-in offer campaign will need to be configured within Punchh and a messaging campaign in Braze (if notifying the customers of the campaign).

Punchh configurations required:
- Campaign: Post check-in offer
- Segment: Custom list
- Reward: Customer choice

For example, an email notifying guests to visit this weekend for double points to a segment with attributes not available in Punchh. Punchh will gift this segment points after a qualifying check-in and optional messaging from Braze. 

![A user segment is configured in Braze, and messages are sent from Braze post check-in campaign. Next, the qualifying users are sent to Punchh custom segment through Braze webhook with segment and user ID. Lastly, the qualifying user in the custom segment checks in and receives the gift and optional message through post check-in campaign]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Post check-in offer without notification %}
#### Post check-in offer campaign without notification

When utilizing a post check-in offer campaign that does not first notify customers, the campaign will gift (optional messaging) and trigger any notification within Braze. Therefore, a post check-in offer campaign must be configured within Punchh; however, a custom list is not required. Instead, you can choose the segment you would like within Punchh. 

Punchh configurations required:
- Campaign: Post check-in offer
- Segment: Customer choice
- Reward: Customer choice

For example, a surprise and delight Braze campaign is sent to a segment available in Punchh, thanking guests for visiting and rewarding them with $2 off their next visit.

![An qualifying user segment can be configured within Punchh, and a qualifying user checks in and receives a gift through a Punchh post-check-in campaign. After this, a reward event is triggered and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversary %}
#### Anniversary campaign 

When utilizing an anniversary campaign, a user will first be gifted for their anniversary from the Punchh campaign. This gifting (reward event) will trigger the messaging campaign within Braze that notifies the user of the gifting. Therefore, a custom list is not required. Instead, you can choose the segment and anniversary setting within Punchh.

Punchh configurations required:
- Campaign: Anniversary campaign
- Segment: Customer choice
- Reward: Customer choice
Considerations:
- Gifting month of sign-up
- Lifespan duration (How long is the birthday reward valid?)
- Recurring campaigns, schedule required 

![An optional segment can be created within Punchh, and a qualifying user receives a reward through a Punchh anniversary campaign. After this, a reward event is triggered and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recall %}
#### Recall campaign

When targeting users based on inactivity, a recall campaign can be used. The customer can create the segment and campaign within Punchh but utilize Braze for messaging.

If you want to use segmentation created in Braze, a [custom Punchh segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) based on inactivity can be attached to a recurring mass offer campaign.

Punchh configurations required:
- Campaign: Recall campaign
- Segment: Customer choice
- Reward: Customer choice
Considerations:
- Campaign runs on a schedule

![An optional segment can be created within Punchh, and a qualifying user receives a reward through a Punchh recall campaign. After this, a reward event is triggered, and the recall message is sent notifying guests of the reward sent from Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


