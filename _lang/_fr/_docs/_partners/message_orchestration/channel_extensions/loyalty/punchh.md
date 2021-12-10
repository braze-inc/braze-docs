---
nav_title: Punchh
article_title: Punchh
page_order: 5
description: "This article outlines the partnership between Braze and Punchh, a loyalty and engagement platform, enabling you to sync data across the two platforms. Data published in Braze will be available for segmentation and can sync user data back into Punchh via webhook templates setup in Braze."
alias: /fr/partners/punchh/
page_type: partenaire
search_tag: Partenaire
---

# Punchh

> [Punchh](https://punchh.com/) is an industry-leading loyalty and engagement platform that enables brands to deliver omnichannel customer loyalty programs both in-store and digitally.

The Braze and Punchh integration allows you to sync data for gifting and loyalty purposes across the two platforms. Data published in Braze will be available for segmentation and can sync user data back into Punchh via Braze webhooks.

## Prerequisites

| Exigences           | Description                                                                                                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Punchh Account      | You need an active Punchh account to take advantage of this partnership.                                                                                                                |
| Braze REST API key  | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST Endpoint | [Your REST Endpoint URL][6]. Your endpoint depends on the Braze URL for your instance.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Punchh offers several endpoints available to Braze customers to help add external IDs into the Punchh platform using the Punchh API endpoints below. Once the external IDs have been added, create an adapter in Punchh, provide your Braze credentials, and select which events you'd like to sync. Next, you can take the Punchh segment ID and use it to build a Punchh webhook to trigger customer syncing in a Canvas journey.

### Available Events to Sync {#available-events-to-sync}
1. Invité
2. Check-in de fidélité
3. Check-in cadeau
4. Rédemption
5. Récompenses
6. Notifications de transaction
7. Notifications marketing

{% alert note %}
Reportez-vous à la documentation Punchh sur les exemples de charges disponibles pour ces événements.
{% endalert %}

### Step 1: Set up external ID ingestion endpoints

External IDs from Braze can be added using the following endpoints for new and existing Punchh users.

{% alert important %}
The `external_source` and `external_source_id` field values must be unique to Punchh and not associated with existing profiles.
{% endalert %}

1. New Punchh users<br> Create new users in Punchh with a Punchh signup endpoint using the `external_source` and `external_source_id` fields. Punchh allows external identifiers to be sent with a user profile via one of the following signup endpoints:
- [API d'inscription mobile](https://developers.punchh.com/mobile-apis/users/mobile-sign-up)
- [SSO Inscription API](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup)<br><br>
2. Existing Punchh users <br> Update `external_source_id` for existing Punchh users. Punchh allows external identifiers to be added to a profile via a user API update endpoint:
- [Mobile User Update](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile)
- [SSO User Update](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update) <br><br>
{% tabs %}
{% tab User signup API example %}
This example allows you to send external identifiers with a user profile at the time of signup. This is done below by sending `external_source` as “customer_id” and `external_source_id` as “556644557788334412” as a string data type.

```json
curl --location --request POST 'https://sandbox.punchh. om/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: eac5b04cbf7362c5359a4c259cf8fc18941646bf2e11bfe46be0031ffaa1100b' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: fr' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user" : {
      "email": "example@braze. om",
      "mot de passe": "p@ssw0rd",
      "prénom":"Amit",
      "nom_du_famille":"K",
      "terms_and_conditions":"true",
      "anniversaire":"2014-02-02-02",
      "zip_code":"94497",
      "anniversaire":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"556644557788334412"
      }
}'
```
{% endtab %}
{% tab User update API example %}
This example allows you to update external identifiers with a user profile. This is done below by sending `external_source` as “customer_id” and `external_source_id` as “556644557788334412” as a string data type.

```json
curl --location --request PUT 'https://sandbox.punchh. om/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: fr' \
--header 'x-pch-digest: 953d896eebfdb5a84aacb9d1b8eaae1fa0cd710b68bcd3b2324415ac40fee99c' \
--header 'Authorization: Bearer c90b819bf962db9882eac6993b57c0a22816ecad0e5229b27320d63' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4
    "user": {
        "external_source":"customer_id",
        "external_source_id":"556644557788334412"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
Platform configuration: In order to enable external identifiers in Punchh, from the Punchh dashboard, navigate to __Cockpit -> Dashboard -> External User Identifier__.
{% endalert %}

### Step 2: Braze adapter setup in Punchh

To set up the Braze and Punchh integration:

1. In the Punchh dashboard, navigate to __Cockpit -> Dashboard -> Major Features -> Enable Webhook Management__ and toggle on __Enable Webhook Management__.<br><br>
2. Next, enable adapters by navigating to __Settings -> Webhooks Manager -> Configurations -> Show Adapters Tab__ and toggle on __Show Adapters Tab__.<br><br>
3. Navigate to __Webhooks Manager__ under the __Settings__ tab, select the __Adapters__ tab, and click __Create Adapter__. <br><br>!\[Punch Platform\]\[1\]<br><br>
5. Fill in the adapter name, description, and admin email. Select __Braze__ as your adapter and provide your Braze REST API endpoint and Braze API key.<br><br>
6. Next, select the available events you would like to enable. A list of these events can be found in [Available events to sync](#available-events-to-sync) above.<br><br>!\[Punch Platform\]\[3\]<br><br>
7. Click __Submit__ to enable the webhook. comm
### Step 3: Create Punchh webhook in Braze

The Braze and Punchh integration allows you to leverage Braze webhook capabilities to create Punchh segments:

1. Créez un segment personnalisé dans Punchh et notez le `custom_segment_id` présent dans l'URL du tableau de bord du segment Punchh. <br><br>Par exemple, la page ci-dessous est située à `www.dashboard.punchhtest.com/segments/11646`. Le numéro "11646" à la fin de ce lien est le `custom_segment_id`.<br><br>!\[Punch Platform\]\[5\]<br><br>
2. Next, navigate to __Webhook Templates__ in Braze and select the Punchh template. Ici, vous pouvez fournir les paires `custom_segment_id` et `user_id` comme valeur clé.<br><br>!\[Punch Platform\]\[4\]<br><br>
3. Once the webhook is saved, it can be triggered in Canvas to sync users as shown below:<br><br>!\[Punch Platform\]\[7\]

For more information on how webhooks are used at Braze, check out [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
[1]: {% image_buster /assets/img/punchh/punchh1.png %} [2]: {% image_buster /assets/img/punchh/punchh2.png %} [3]: {% image_buster /assets/img/punchh/punchh3.png %} [4]: {% image_buster /assets/img/punchh/punchh4.png %} [5]: {% image_buster /assets/img/punchh/punchh5.png %} [7]: {% image_buster /assets/img/punchh/punchh6.png %}

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints