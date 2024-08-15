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
SessionM is a customer engagement and loyalty platform empowering the world’s most innovative brands to forge
stronger, more loyal, and more profitable consumer relationships. With powerful data management at the core, SessionM provides campaign management capabilities coupled with flexible and comprehensive loyalty management solutions to help marketers drive targeted outreach to increase engagement and profitability.

## Prerequisites

Before you start, you'll need the following:
| Prerequisite | Description | Source |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------|
| A SessionM account | A SessionM account is required to take advantage of this partnership. | Braze |
| A Braze REST API key | A Braze REST API key with `trigger_send` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**. | Braze |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. | Braze |
| A SessionM Core REST endpoint | [SessionM CORE endpoint URL]/priv/v1/apps/{{core_apikey}}/users/{{user_id}}/tags Your endpoint will depend on the SessionM url of your instance. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Core REST API key | The SessionM API key associated with your instance and the Braze integration. This key can be utilized for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Core REST API secret | The SessionM API secret associated with your instance and the Braze integration. This key can be utilized for all core based calls including tags. This can be created in the SessionM dashboard from **Digital Properties**. | SessionM |
| A SessionM Connect REST endpoint | [SessionM connect endpoint URL]/offers/api/2.0/offers/get_user_offers Your endpoint will depend on the SessionM url of your instance. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| A SessionM Connect REST Authorization string | The SessionM Connect Basic Authstring associated with your instance. This authentication string can be utilized for all connect based calls including get_user_offers. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| A SessionM Connect REST Retailer ID | A unique guid identification to the specific customer associated with your instance. Please reach out to your SessionM Technical Account Manager or Delivery team to provide. | SessionM |
| Matching Identifier | To use the integration, ensure that both SessionM and Braze have a record of the identifiers used by each platform. References to `user_id` correspond to SessionM's user identifier generated at the time of profile creation within SessionM. | Braze and SessionM |
{: .reset-td-br-1 .reset-td-br-2} 

{% alert note %} 
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**. 
{% endalert %} 

## Use cases 
- As a Marketer I would like to create segmentation that incorporates data across all of my loyalty, customer management and messaging platforms.
- As a Marketer I would like to be able to use robust segmentation to target my offers and promotions at specific user sets.
- As a Marketer I would like to have my client messaging take advantage of the most up to date information as possible at time of message sending (profile, offers, loyalty, etc.).
- As a Marketer I would like to provide detailed notifications to my customers of the progress and subsequent completion of promotional and loyalty activities.
- As a Marketer I would like to notify my customers when a new offer was awarded to them and the offer details.

## Integrating Braze Segmentation into SessionM Platform

Integrating SessionM with Braze eliminates the need to duplicate data between platforms in terms of customer information.

Complex user segmentation can be done in Braze utilizing the data Braze already is being fed and SessionM can take these segments and ingest.

This data can be utilized in conjunction with any segmentation for promotion/loyalty/offer logic being built in SessionM.

This pattern reduces the risk of data loss/leaks by eliminating the need to transmit sensitive user data between systems.

### Step 1: Create a Segment in Braze

Within Braze, create a segment of users to target with SessionM promotions and offers. 

![Create a segment.]({% image_buster /assets/img/SessionM/CreateSegment.png %})

### Step 2: Import Braze Segments into SessionM


**Option 1: CSV Import**
Export your Braze segment via the Braze segmenter tool UI and provide a CSV file  to SessionM containing all of the customers to tag, the tagname and a time to live for each user either in the file.

**Option 2 (recommended): Export to the [SessionM Tag Endpoint](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)**
 1. Create a webhook campaign in Braze 
 2. Set the Webhook URL to '{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags'. Use liquid to define the user_id within the url. 
 3. Using a Raw Text **Request Body** compose the body of the webhook to include the desired tags that should be added to the user profile in sessionM and the desired time to live. For example:
 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```
 {{WEBHOOK COMPOSE SCREENSHOT}}

 4. In the **Settings** tab add in the key-value pairs for each request header field.
    - Create a Key `Content-Type` with a corresponding Value `application/json`
    - Create a Key `Authorization` with a corresponding Value ` Basic YOUR-ENCODED-STRING-KEY`. Ask your SessionM team for the encoded string key for your endpoint. 

{{WEBHOOK SETTINGS SCREENSHOT}}

 5. Schedule your delivery 
 6. Set your Target Audiences to target the segment created in Step 1
 7. Finalize and launch your campaign

{% alert important %}
This process can also be done directly by making a request to the [SessionM Tag Endpoint](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) specifying the customer, the tagname and a time to live for each user in the call (Single User Per Call).

The following example request uses cURL. For better API request management, we recommend using an API client, such as Postman.

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
{% endalert %}

## Allowing Braze to Retrieve Real-time Offer Wallet

Data recency is critical in any form of customer communication.

Integrating SessionM with Braze allows for the real-time pulling of SessionM user data at time of message send, via Connected Content, to eliminate the risk of communicating outdated/expired or already redeemed loyalty offers to customers. The below example shows Connected Content being used to template Offer Wallet data into a message; however, Connected Content can be used with any of SessionM's Connect endpoints. 

### Step 1: Issue Offer within SessionM

SessionM issues offers to customers from several different internal levers that can be configured. Once issued, the offers are moved to a state which SessionM calls the “offer wallet”.

A customer must complete the required action or meet the targeting and is issued the offer within SessionM.
SessionM then adds the offer to the customer's wallet in the ISSUED state.

### Step 2: Call SessionM Offer Wallet API

Inside of the Campaign or Canvas Step that should include the SessionM Offers, use [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) to make an API call to the [SessionM get_user_offers endpoint] (https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers)

Within the Connected Content request, specify the customer's SessionM `user_id` and your `retailer_id` to retrieve the full list of active offers the customer has in their wallet (single user per call). Ask your SessionM team for the encoded string key for the Basic Authorization header in your Connected Content call. 


The `culture` defaults to `en-US` but Liquid can be used to pull in a user's language for multi-lingual SessionM offers. For example, using `"culture":"{{${language}}}"`.


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

### Step 2: Populate Offer Wallet into Braze Messaging
SessionM returns in the response the full list of offers in the issued state along with the full details for each offer.

Example returned response
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
These can be populated into the message using Liquid dot notation. If you wanted to personalize the message with the resulting offer_id, you could leverage the return payload by using `{{wallet.payload.available_points}` which returns `100`.

{{ ONCE TESTED - INCLUDE SCREENSHOT OF EXAMPLE HERE}}

{% alert important %}
This is an individual API, if you intend to do a batch send of over 500+ users please reach out to your SessionM account team to inquire about how to incorporate bulk data in the integration.
{% endalert %}

## SessionM Triggered Scheduled messaging

Integrating SessionM with Braze allows for the ability create complex loyalty promotions in SessionM and to communicate to customers directly on the completion of specified loyalty promotions leveraging the creative and communication functionality of Braze.

The integration between SessionM and Braze allows for the additional details of user profile data, offer details and point balances to be sent in real-time to the customer at the point of action.

### Step 1: SessionM Delivery Team Configures Templates

Working in conjunction with the customer the SessionM Delivery team will create generic templates to enable Marketers to trigger calls to the Braze's API-Triggered Campaings/Canvases endpoints, providing real time message triggering along with specific customer and award datapoints to be utilized within the Braze journeys.

Standard fields present in all templates from SessionM:
-canvas_id
-campaign_id
-broadcast flag
-customer identifier
-email address

{% alert important %}
When setting the broadcast flag to `true` the message will be sent to the entire segment that the campaign or Canvas targets.
{% endalert %}

Additional fields configurable based on need:
-Offer data: offer_id, offer title, user offer id, description, terms and conditions, logo, pos discount id, expiration date
-point award data: point award amount, point account name
-Event trigger data: any data contained in the event that triggered the behavior that utilizes the trigger/send Webhook outcome
-Campaign specific Data: Campaign runtime, campaign id, campaign name, campaign custom data

{% alert important %}
Additional fields are sent to Braze as trigger_properties for use in personalizing the message. 
{% endalert %}

### Step 2: Create the Braze Campaign or Canvas

Create an API-triggered Campaign or Canvas within Braze that will be triggered by SessionM. 

If you will be using the additional configurable fields, such as `offer_id` or `offer title`, use Liquid like {{api_trigger_properties.${offer_id}}} to add the personalization into your messaging.

{{LIQUID PERSONALIZATION SCREENSHOT}}

Within the Schedule Delivery tab in the dashboard composer, capture the Campaign or Canvas ID. This ID will be added to SessionM Campaign Advanced Settings.

{{API TRIGGERED CAMPAIGN ID SCREENSHOT}}

Finalize your Campaign or Canvas details and Launch. 

### Step 3: SessionM Creates Promotional/Messaging Campaign

Create your campaign in SessionM

Update the advanced settings within the SessionM campaign to include the following JSON payload containing the Braze Campaign_id
{
"braze_campaign_id": "{{campaign/Canvas id}}"
}
{{Insert Screenshot: "Campaign Creation"}}
{{Insert Screenshot: "Advanced Settings"}}

Create a message trigger based on required schedule or behavior and select the Braze Messaging Variant as the Messaging Variant in the External Message Dropdown Menu to utilize the preconfigured template.

This template will pull in all the relevant static and dynamic attributes and call out to the Braze Endpoint
{{Insert Screenshot: "Add Message"}}
{{Insert Screenshot: "External Message"}}
{{Insert Screenshot: "Braze Template"}}
