---
nav_title: Punchh
article_title: Punchh
page_order: 5
description: "This article outlines the partnership between Braze and Punchh. This integration enables you to..."
alias: /partners/punchh/
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) is the industry-leading loyalty & engagement platform that enables brands to deliver omnichannel customer loyalty programs both in-store and digitally. 

Punchh has partnered with Braze to sync data across the two platforms for gifting purposes. Data published in Braze will be available for segmentation and can sync those user data back in Punchh via webhook templates setup in Braze.  

## Requirements

| Requirement | Access | Description |
|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. |
| Braze REST Endpoint | Braze | [Your REST Endpoint URL][6]. Your endpoint will depend on the Braze URL for your instance. |
| Punchh Account | Punchh Platform | You will need an active Punchh account to leverage this partnership integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

Punchh offers several endpoints available to Braze customers to help add external ids into the pinch platform. This can be done using the Punchh API endpoints listed below. Once the external ids have been added, you must create an adapter in PUnch and provide your Braze credentials. Listed below is the list of available events to sync. Next, you can take the Punchh segment ID and use it within the Punchh webhook template to trigger customer syncing in a Canvas journey.

### Available Events
1. Guest
2. Loyalty Checkin
3. Gift Checkin
4. Redemption
5. Rewards
6. Transacion Notifications
7. Marketing Notifications

### External ID Ingestion Endpoints

External IDs from Braze can be added in several different ways:

1. Create new users in Punchh with the Punchh signup API under the `external_source` and `external_source_id` fields.<br>The field values must be unique within Punchh. For more information on applicable Punchh APIs, visit the [Mobile signup API](https://developers.punchh.com/mobile-apis/users/mobile-sign-up) and [SSO Signup API](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup) Punchh documentation.<br><br>
2. Update `external_source_id` for existing users. <br>The field value must be unique with Punchh. For more information on applicable Punchh APIs, visit the [Mobile User update API](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile), [SSO User update API](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information), and [Dashboard User Update API](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update) Punchh documetation.

{% alert note %}
Platform Configuration: In order to enable external identifiers in Punchh, from the Punchh dashboard, navigate to __Cockpit -> Dashboard -> External User Identifier__.
{% endalert %}

## Braze and Punchh Integration

1. To set up the Braze and Punchh integration on the Punchh platform, navigate to __Webhooks Manager__ under the __Settings__ tab and select the __Adapters__ tab. <br><br>![Punch Platform][1]<br><br>

2. Click on __Create Adapter__.<br><br>![Punch Platform][2]<br><br>

3. Fill in the adapter name, description, admin email. Select __Braze__ as your adapter, and provide your [REST API endpoint]({{site.baseurl}}/api/basics/#endpoints) and Braze API key.<br><br>

4. Next, select the available events you would like to enable. A list of these events can be found above.<br><br>![Punch Platform][3]<br><br>

5. Click on __Submit__ to enable the webhook.

## Segment Sync Webhook Setup in Braze 

The Braze and Punchh integration allows you to leverage Braze webhook capabilities to create segments. This can be done by:

1. Create a custom segment in Punchh and note the `custom_segment_id` present in the Punchh segment dashboard URL. <br><br>For example, the page below is located at `www.dashboard.punchhtest.com/segments/11646`. The numer at the end of this link is the `custom_segment_id`.<br><br>![Punch Platform][5]<br><br>
2. From the Braze dashboard, navigate to the __Webhook Templates__ and select the Punchh template. Here, you can provide the `custom_segment_id` and `user_id` as key-value pairs.<br><br>![Punch Platform][4]<br><br>
3. Once the webhook is saved, it can be saved and used to trigger in Canvas to run the webhook and sync users as shown below:<br><br>![Punch Platform][7]

For more information on how webhooks are used at Braze, check out our webhook documentaion [here]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints