--- 
nav_title: SessionM
article_title: SessionM 
description: "SessionM Loyalty Platform Integration" 
alias: /partners/sessionm/ 
page_type: partner 
search_tag: Partner 
layout: dev_guide 
--- 

# SessionM Loyalty Platform
> SessionM is a customer engagement and loyalty platform empowering the world’s most innovative brands to forge stronger, more loyal, and more profitable consumer relationships. With powerful data management at the core, SessionM provides campaign management capabilities coupled with flexible and comprehensive loyalty management solutions to help marketers drive targeted outreach to increase engagement and profitability.

## Prerequisites

| Requirement | Description | Source |
| --- | --- | --- |
| A SessionM account | A SessionM account is required to take advantage of this partnership. | Braze |
| A Braze REST API key | A Braze REST API key with `trigger_send` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**. | Braze |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. | Braze |
| A SessionM Core REST endpoint | Your endpoint will depend on the SessionM url of your instance. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Core REST API key | The SessionM API key associated with your instance and the Braze integration. This key can be utilized for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Core REST API secret | The SessionM API secret associated with your instance and the Braze integration. This key can be utilized for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Connect REST endpoint | Your endpoint will depend on the SessionM url of your instance. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| A SessionM Connect REST Authorization string | The SessionM Connect Basic Authstring associated with your instance. This authentication string can be utilized for all connect based calls including get_user_offers. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| A SessionM Connect REST Retailer ID | A unique guid identification to the specific customer associated with your instance. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| Matching Identifier | To use the integration, ensure that both SessionM and Braze have a record of the identifiers used by each platform. References to `user_id` correspond to SessionM's user identifier generated at the time of profile creation within SessionM. | Braze and SessionM |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %} 
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**. 
{% endalert %} 

## Use cases 
- Create segmentation that incorporates data across all loyalty, customer management, and messaging platforms.
- Use robust segmentation to target specific user sets with offers and promotions.
- Take advantage of the most up-to-date user, offer, and loyalty information when sending messages.
- Provide detailed notifications to customers on the progress and completion of promotional and loyalty activities.
- Notify customers when a new offer is awarded and provide the offer details.

## Integrating Braze Segmentation into SessionM Platform

Integrating SessionM with Braze eliminates the need to duplicate customer information between platforms. Complex user segmentation can be done in Braze utilizing the data Braze already is being fed, and SessionM can take these segments and ingest them. This data can be utilized with any segmentation for promotion, loyalty, or offer logic built in SessionM. This pattern reduces the risk of data loss/leaks by eliminating the need to transmit sensitive user data between systems.

### Step 1: Create a Segment in Braze

Within Braze, create a segment of users to target with SessionM promotions and offers. 

![Create a segment.]({% image_buster /assets/img/SessionM/CreateSegment.png %})

### Step 2: Import Braze Segments into SessionM

#### Option 1: CSV Import
Export your Braze segment via the Braze segmenter tool UI and provide a CSV file  to SessionM containing all of the customers to tag, the tagname and a time to live for each user either in the file.

#### Option 2 (recommended): Export to the [SessionM Tag Endpoint](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)
Create a webhook campaign in Braze and set the Webhook URL to {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Use liquid to define the user_id within the URL. 

Using a Raw Text **Request Body** compose the body of the webhook to include the desired tags that should be added to the user profile in sessionM and the desired time to live. For example:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![Webhook composer.]({% image_buster /assets/img/SessionM/SessionMWebhookComposer.png %})

In the **Settings** tab, add the key-value pairs for each request header field.
    - Create a Key `Content-Type` with a corresponding Value `application/json`
    - Create a Key `Authorization` with a corresponding Value `Basic YOUR-ENCODED-STRING-KEY`. Ask your SessionM team for the encoded string key for your endpoint. 

![Webhook settings.]({% image_buster /assets/img/SessionM/SessionMWebhookSettings.png %})

Schedule your delivery, set your Target Audiences to target the segment created in Step 1, finalize and launch your campaign

{% alert important %}

This process can also be done through an API client, such as Postman, by making a request directly to the [SessionM Tag Endpoint](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) specifying the customer, the tagname and a time to live for each user in the call (Single User Per Call).

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

## Allowing Braze to Retrieve Real-time Offer Wallet

Data recency is critical in any form of customer communication.

Integrating SessionM with Braze allows for the real-time pulling of SessionM user data at time of message send, via Connected Content, to eliminate the risk of communicating outdated, expired or already redeemed loyalty offers to customers. The below example shows Connected Content being used to template Offer Wallet data into a message; however, Connected Content can be used with any of SessionM's Connect endpoints. 

### Step 1: Issue Offer within SessionM

SessionM issues offers to customers from several different internal levers that can be configured. Once issued, the offers are moved to a state which SessionM calls the “offer wallet”.

A customer must complete the required action or meet the targeting and is issued the offer within SessionM.

SessionM then adds the offer to the customer's wallet in the ISSUED state.

### Step 2: Call SessionM Offer Wallet API

Inside of the Campaign or Canvas Step that should include the SessionM Offers, use [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) to make an API call to the [SessionM get_user_offers endpoint](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/)

Within the Connected Content request, specify the customer's SessionM `user_id` and your `retailer_id` to retrieve the full list of active offers the customer has in their wallet. Each request to this endpoint can include a single user. Ask your SessionM team for the encoded string key for the Basic Authorization header in your Connected Content call. 


Within the body of the request, `culture` defaults to `en-US`, but Liquid can be used to template a user's language for multi-lingual SessionM offers. For example, by using {% raw %}`"culture":"{{${language}}}"`{% endraw %}.

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

### Step 3: Populate Offer Wallet into Braze Messaging
After a request is made to the endpoint, SessionM returns the complete list of offers in the issued state, along with the full details for each offer.

Example returned response:

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

These can be populated into the message using Liquid dot notation. For example, if you wanted to personalize the message with the resulting offer_id, you could leverage the return payload by using {% raw %}`{{wallet.payload.available_points}`{% endraw %} which returns `100`.

{% alert important %}
This is an individual API. If you intend to send a batch of over 500+ users, please reach out to your SessionM account team to inquire about how to incorporate bulk data in the integration.
{% endalert %}

## SessionM Triggered Messaging

Integrating SessionM with Braze allows for the creation of complex loyalty promotions in SessionM and the communication to customers directly upon the completion of specified loyalty promotions, leveraging the creative and communication functionality of Braze.

The integration between SessionM and Braze allows user profile data, offer details, and point balances to be dynamically populated into messaging and sent in real-time to the customer at the point of action.

### Step 1: SessionM Delivery Team Configures Templates

Collaborate with your SessionM Delivery team to develop templates for use in your triggered messaging. SessionM will insert user profile data, offer details, and point balances into the messaging and trigger them in Braze for real-time customer messaging at the point of action.

Standard fields present in all templates from SessionM include:
- canvas_id
- campaign_id
- broadcast flag
- customer identifier
- email address

{% alert important %}
When setting the broadcast flag to `true` the message will be sent to the entire segment that the Campaign or Canvas targets in Braze.
{% endalert %}

Additional fields can be configured based on specific needs:

- Offer data: offer_id, offer title, user offer id, description, terms and conditions, logo, pos discount id, expiration date
- Point award data: point award amount, point account name
- Event trigger data: any data in the trigger event that utilizes the trigger/send Webhook outcome
- Campaign-specific Data: Campaign runtime, campaign id, campaign name, campaign custom data

Additional fields are sent to Braze as `trigger_properties` for personalizing the message. 

### Step 2: Create a Braze Campaign or Canvas

Create an API-triggered Campaign or Canvas within Braze that will be triggered by SessionM. 

If additional fields have been configured, such as `offer_id` or `offer title`, use Liquid like {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} to add the personalized fields into your messaging.

![API trigger properties.]({% image_buster /assets/img/SessionM/apiTriggerProperties.png %})

Within the **Schedule Delivery** tab in the dashboard composer, capture the Campaign or Canvas ID. This ID will be added to SessionM Campaign **Advanced Settings**.

![API triggered campaign.]({% image_buster /assets/img/SessionM/apiTriggerCampaign.png %})

Finalize your Campaign or Canvas details and **Launch**. 

### Step 3: Create a SessionM Promotional or Messaging Campaign

Create your campaign in SessionM. 

![SessionM Campaign Creation.]({% image_buster /assets/img/SessionM/SessionMCampaignCreation.png %})

Update the advanced settings within the SessionM campaign to include the following JSON payload containing the `braze_campaign_id` or `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![SessionM advanced settings.]({% image_buster /assets/img/SessionM/SessionMAdvancedSettings.png %})

Create a message trigger on the desired schedule or behavior and select the **Braze Messaging Variant** as the **Messaging Variant** in the **External Message** dropdown menu to utilize the preconfigured template.

![SessionM external message.]({% image_buster /assets/img/SessionM/SessionMExternalMessage.png %})

This template will pull in all the relevant static and dynamic attributes and call out to the Braze Endpoint.

![SessionM Braze template.]({% image_buster /assets/img/SessionM/SessionMBrazeTemplate.png %})
