--- 
nav_title: Sessionm
article_title: SessionM
description: "This reference article outlines the partnership between Braze and SessionM, a customer engagement and loyalty platform."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# SessionM Loyalty Platform

> [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) is a customer engagement and loyalty platform that provides campaign management features and loyalty management solutions to help marketers drive targeted outreach to increase engagement and profitability.

## Prerequisites

| Source | Requirement | Description |
| --- | --- | --- |
| Braze | A Braze REST API key | A Braze REST API key with `trigger_send` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze | A Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
| Braze and SessionM | Matching identifier | To use the integration, ensure that both SessionM and Braze have a record of the identifiers used by each platform. References to `user_id` correspond to SessionM's user identifier generated at the time of profile creation in SessionM. |
| SessionM | A SessionM account | A SessionM account is required to take advantage of this partnership. |
| SessionM | A SessionM Core REST endpoint | Your endpoint will depend on the SessionM URL of your instance. This can be created in the SessionM dashboard from **Digital Properties**. |
| SessionM | A SessionM Core REST API key | The SessionM API key associated with your instance and the Braze integration. This key can be used for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. |
| SessionM | A SessionM Core REST API secret | The SessionM API secret associated with your instance and the Braze integration. This key can be used for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. |
| SessionM | A SessionM Connect REST endpoint | Your endpoint will depend on the SessionM URL of your instance. Please reach out to your SessionM technical account manager or Delivery team to provide. |
| SessionM | A SessionM Connect REST Authorization string | The SessionM Connect Basic Authorization string associated with your instance. This authentication string can be used for all connect based calls including get_user_offers. Please reach out to your SessionM technical account manager or Delivery team to provide. |
| SessionM | A SessionM Connect REST Retailer ID | A unique guid identification to the specific customer associated with your instance. Reach out to your SessionM technical account manager or Delivery team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %} 
If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), you can create an API key at **Developer Console** > **API Settings**. 
{% endalert %} 

## Use cases

The following use cases showcase a few ways to leverage the SessionM and Braze integration.

- Create segmentation that incorporates data across all loyalty, customer management, and messaging platforms.
- Use robust segmentation to target specific user sets with offers and promotions.
- Take advantage of the most up-to-date user, offer, and loyalty information when sending messages.
- Provide detailed notifications to customers on the progress and completion of promotional and loyalty activities.
- Notify customers when a new offer is awarded and provide the offer details.

## Integrating SessionM with Braze

### Step 1: Create a segment in Braze

In Braze, create a segment of users to target with SessionM promotions and offers. 

![Segment Builder with the "Custom Attributes" filter selected.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Step 2: Import Braze segments into SessionM

#### Option 1: Export to the SessionM Tag endpoint (recommended)

First, create a webhook campaign in Braze and set the webhook URL to {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Use Liquid to define the `user_id` within the URL. 

Using a raw text **Request Body**, compose the webhook body to include the desired tags to be added to the user profile in SessionM and the desired time to live. An example is:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

In the **Settings** tab, add the key-value pairs for each request header field:
    - Create a key `Content-Type` with a corresponding value `application/json`
    - Create a key `Authorization` with a corresponding value `Basic YOUR-ENCODED-STRING-KEY`. Contact your SessionM team for the encoded string key for your endpoint. 

![Webhook settings.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Schedule your delivery, set your **Target Audiences** to target the segment [you created previously](#step-1-create-a-segment-in-braze), then launch your campaign.

{% alert important %}
This process can also be done through an API client, such as Postman, by making a request directly to the [SessionM Tag endpoint](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) specifying the customer, the tag name, and a time to live for each user in the call (single user per call).
<br><br>
The following example request uses cURL. 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Option 2: CSV import

Export your Braze segment using the Braze segmenter and provide a CSV file to SessionM that contains the customers to tag, the tag name, and a time to live for each user in the file.

## Retrieving real-time offer wallet with Braze

Integrating SessionM with Braze allows for the real-time pulling of SessionM user data at time of message send, using Connected Content, to eliminate the risk of communicating outdated, expired or already redeemed loyalty offers to customers. 

The following example shows Connected Content being used to template offer wallet data into a message. However, Connected Content can be used with any of SessionM's Connect endpoints. 

### Step 1: Issue offer in SessionM

SessionM issues offers to customers from several different internal levers that can be configured. After being issued, the offers are moved to a state which SessionM calls the “offer wallet”.

A customer must complete the required action or meet the targeting and is issued the offer within SessionM.

SessionM then adds the offer to the customer's wallet in the issued state.

### Step 2: Call SessionM Offer Wallet API

In campaign or Canvas step with the SessionM offers, use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) to make an API call to the [SessionM `get_user_offers` endpoint](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

In the Connected Content request, specify the user's SessionM `user_id` and your `retailer_id` to retrieve the full list of active offers the customer has in their wallet. Each request to this endpoint can include a single user. Contact the SessionM team for the encoded string key for the basic authorization header in your Connected Content call.

In the request body, `culture` defaults to `en-US`, but you can use Liquid to template a user's language for multi-lingual SessionM offers (for example, by using {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Step 3: Populate offer wallet to Braze messaging

After a request is made to the endpoint, SessionM returns the complete list of offers in the issued state, along with the full details for each offer. This is an example returned response:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Using Liquid dot notation, this can be populated into the message. For example, to personalize the message with the resulting `offer_id`, you could leverage the return payload by using {% raw %}`{{wallet.payload.available_points}`{% endraw %}, which returns `100`.

{% alert note %}
This is an individual API. If you intend to send a batch of over 500 users, reach out to your SessionM account team to inquire about how to incorporate bulk data in the integration.
{% endalert %}

## Setting up triggered messaging

The integration between SessionM and Braze allows user profile data, offer details, and point balances to be dynamically populated into messaging and sent in real-time to the customer at the point of action.

### Step 1: SessionM Delivery team configures templates

Collaborate with your SessionM Delivery team to develop templates for use in your triggered messaging. SessionM will insert user profile data, offer details, and point balances into the messaging and trigger them in Braze for real-time customer messaging.

Standard fields present in all templates from SessionM include:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
When setting the `broadcast flag` to `true`, the message will be sent to the entire segment that the campaign or Canvas targets in Braze.
{% endalert %}

Additional fields can be configured based on specific needs:

- **Offer data:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Point award data:** `point award amount`, `point account name`
- **Event trigger data:** Any data in the trigger event that utilizes the trigger/send webhook outcome
- **Campaign-specific data:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Additional fields are sent to Braze as `trigger_properties` for personalizing the message. 

### Step 2: Create a Braze campaign or Canvas

Create an API-triggered campaign or Canvas in Braze to be triggered by SessionM. If additional fields have been configured, such as `offer_id` or `offer title`, use Liquid (such as {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) to add the personalized fields into your messaging.

![API trigger properties.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

In the **Schedule Delivery** tab, note down the campaign or Canvas ID as this will be added to SessionM campaign **Advanced Settings**.

![API triggered campaign.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finalize your campaign or Canvas details, and select **Launch**. 

### Step 3: Create a SessionM promotional or messaging campaign

Next, create your campaign in SessionM.

![SessionM Campaign Creation.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Update the advanced settings in the SessionM campaign to include the following JSON payload containing the `braze_campaign_id` or `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![SessionM advanced settings.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Create a message trigger on the desired schedule or behavior. Then, select **Braze Messaging Variant** as the **Messaging Variant** in the **External Message** menu to use the template.

![SessionM external message.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

This template pulls the relevant static and dynamic attributes and call out to the Braze endpoint.

![SessionM Braze template.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
