---
nav_title: Punchh
article_title: Punchh
page_order: 5
description: "This article outlines the partnership between Braze and Punchh. This integration enables you to sync data across the two platforms for gifting and loyalty purposes. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze."
alias: /partners/punchh/
page_type: partner
search_tag: Partner
---

# Punchh

> [Punchh](https://punchh.com/) is an industry-leading loyalty & engagement platform that enables brands to deliver omnichannel customer loyalty programs both in-store and digitally.

Punchh has partnered with Braze to sync data across the two platforms for gifting and loyalty purposes. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze.

## Requirements

| Requirement         | Access | Description                                                                                                                                                                 |
| ------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braze API Key       | Braze  | You need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with `users.track` permissions. |
| Braze REST Endpoint | Braze  | [Your REST Endpoint URL][6]. Your endpoint depends on the Braze URL for your instance.                                                                                      |
| Punchh Account      | Punchh | You need an active Punchh account to leverage this partnership integration.                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

Punchh offers several endpoints available to Braze customers to help add external IDs into the Punchh platform. This can be done by using the Punchh API endpoints listed below. Once the external IDs have been added, you must create an adapter in Punchh, provide your Braze credentials, and select which events you'd like to sync. Next, you can take the Punchh segment ID and use it within the Punchh webhook template to trigger customer syncing in a Canvas journey.

### Available Events to Sync
1. Guest
2. Loyalty Check-in
3. Gift Check-in
4. Redemption
5. Rewards
6. Transaction Notifications
7. Marketing Notifications

{% alert note %}
Reference Punchh documentation on what sample payloads for these available events may look like.
{% endalert %}

### External ID Ingestion Endpoints

External IDs from Braze can be added in several different ways:

1. Create new users in Punchh with a Punchh signup endpoing using the `external_source` and `external_source_id` fields.<br>Punchh allows external identifiers to be sent with a user profile via a signup API endpoint. The field values must be unique to Punchh and not associated with any other existing profile. <br><br>For more information on applicable Punchh APIs, visit the following API documentation:
- [Mobile Signup API](https://developers.punchh.com/mobile-apis/users/mobile-sign-up)
- [SSO Signup API](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup)<br><br>
2. Update `external_source_id` for existing Punchh users. <br>Punchh allows external identifiers to be added to a profile via a user API update endpoint where the value is unique to Punchh and is not associated with any other existing profile.<br><br>For more information on applicable Punchh APIs, visit the following API documentation:
- [Mobile User Update](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile) - [SSO User Update](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information) - [Dashboard User Update](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update) <br><br>
{% tabs %}
{% tab User Signup API Example %}
This example allows you to send external identifiers with the user profile at the time of signup. This is done below by sending `external_source` as “customer_id” and `external_source_id` as “556644557788334412” as a string data type.

```json
curl --location --request POST 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: eac5b04cbf7362c5359a4c259cf8fc18941646bf2e11bfe46be0031ffaa1100b' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user" : {
      "email": "example@braze.com",
      "password": "p@ssw0rd",
      "first_name":"Amit",
      "last_name":"K",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"556644557788334412"
      }
}'
```
{% endtab %}
{% tab User Update API Example %}
This example allows you to update external identifiers with user profile. This is done below by sending `external_source` as “customer_id” and `external_source_id` as “556644557788334412” as a string data type.

```json
curl --location --request PUT 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: 953d896eebfdb5a84aacb9d1b8eaae1fa0cd710b68bcd3b2324415ac40fee99c' \
--header 'Authorization: Bearer c90b819bf962db9882eeac6993b57c0a22816ecad0e5229b27320d63' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"556644557788334412"
    }
}'
```

{% endtab %}
{% endtabs %}

{% alert note %}
Platform Configuration: In order to enable external identifiers in Punchh, from the Punchh dashboard, navigate to __Cockpit -> Dashboard -> External User Identifier__.
{% endalert %}

### Braze Adapter Setup in Punchh

To set up the Braze and Punchh integration, on the Punchh platform:

1. Navigate to __Cockpit -> Dashboard -> Major Features -> Enable Webhook Management__ and toggle on __Enable Webhook Management__.<br><br>

2. To enable adapters, navigate to __Settings -> Webhooks Manager -> Configurations -> Show Adapters Tab__ and toggle on __Show Adapters Tab__.<br><br>

1. Navigate to __Webhooks Manager__ under the __Settings__ tab and select the __Adapters__ tab. <br><br>!\[Punch Platform\]\[1\]<br><br>

2. Click on __Create Adapter__.<br><br>!\[Punch Platform\]\[2\]<br><br>

3. Fill in the adapter name, description, and admin email. Select __Braze__ as your adapter, and provide your [REST API endpoint]({{site.baseurl}}/api/basics/#endpoints) and Braze API key.<br><br>

4. Next, select the available events you would like to enable. A list of these events can be found [above](#available-events-to-sync).<br><br>!\[Punch Platform\]\[3\]<br><br>

5. Click on __Submit__ to enable the webhook.

### Segment Sync Webhook Setup in Braze

The Braze and Punchh integration allows you to leverage Braze webhook capabilities to create segments. This can be done by:

1. Create a custom segment in Punchh and note the `custom_segment_id` present in the Punchh segment dashboard URL. <br><br>For example, the page below is located at `www.dashboard.punchhtest.com/segments/11646`. The numer "11646" at the end of this link is the `custom_segment_id`.<br><br>!\[Punch Platform\]\[5\]<br><br>
2. From the Braze dashboard, navigate to __Webhook Templates__ and select the Punchh template. Here, you can provide the `custom_segment_id` and `user_id` as key-value pairs.<br><br>!\[Punch Platform\]\[4\]<br><br>
3. Once the webhook is saved, it can be used to trigger in Canvas to run the webhook and sync users as shown below:<br><br>!\[Punch Platform\]\[7\]

For more information on how webhooks are used at Braze, check out [Creating a Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) article.
[1]: {% image_buster /assets/img/punchh/punchh1.png %} [2]: {% image_buster /assets/img/punchh/punchh2.png %} [3]: {% image_buster /assets/img/punchh/punchh3.png %} [4]: {% image_buster /assets/img/punchh/punchh4.png %} [5]: {% image_buster /assets/img/punchh/punchh5.png %} [7]: {% image_buster /assets/img/punchh/punchh6.png %}

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints