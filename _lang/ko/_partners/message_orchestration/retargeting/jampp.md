---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "This reference article outlines the partnership between Braze and Jampp, a performance marketing platform used for acquiring and retargeting mobile customers."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) is a performance marketing platform used for acquiring and retargeting mobile customers. Jampp combines behavioral data with predictive and programmatic technology to generate revenue for advertisers by showing personal, relevant ads that inspire consumers to purchase for the first time or more often.

_This integration is maintained by Jampp._

## About the integration

The Braze and Jampp integration allows Braze users to sync events into Jampp via Braze webhook events. As a result, customers can add richer data sets to their retargeting initiatives within their mobile advertising ecosystems.

Some examples of when you would want to retarget customers with an ad:
- When a customer's email or push subscription state changes.
- How a customer interacted with a Braze messaging campaign.
- If the customer has triggered a specific geofence.

## Prerequisites

This integration supports iOS and Android apps.

| Requirement | Description |
|---|---|
| Jampp account | A [Jampp account](https://www.jampp.com/) is required to take advantage of this partnership. |
| Android app ID | Your unique Braze application identifier for Android (such as "com.example"). |
| iOS app ID | Your unique Braze application identifier for iOS (such as "012345678"). |
| Enable IDFA collection in Braze SDK | IDFA collection is optional within the Braze SDK and disabled by default. | 
| Collection of Google advertising ID via custom attribute | Google advertising ID collection is optional for customers and can be collected as a [custom attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Step 1: Create a webhook template in Braze

To create a Jampp webhook template to use in future campaigns or Canvases, navigate to **Templates** > **Webhook Templates** in the Braze platform.

If you would like to make a one-off Jampp webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In the webhook URL, you must:
- Set the event name. This name will appear in your Jampp dashboard.
- Pass your app's unique application identifier for Android (such as "com.example") and iOS (such as "012345678").
- Insert [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) for the appropriate custom attribute you're tracking as the Google advertising ID. Note that the Google advertising ID is listed as `aaid` in this example, but you will need to replace it with the custom attribute name your developers set.

![The webhook URL and message preview shown in the Braze webhook builder.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze does not automatically collect the device IDFA/AAID, so you must store these values yourself. Be aware that you may require user consent to collect this data.
{% endalert %}

#### Request headers and method

The Jampp webhook requires an HTTP method and request header.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![The request headers, HTTP method, and message preview shown in the Braze webhook builder.]({% image_buster /assets/img/jampp_method.png %})

#### Request body

You do not have to define a request body for this webhook.

### Step 2: Preview your request

Preview the message to ensure the request is rendering properly for different users. We recommend previewing and sending test requests for both Android and iOS users. If the request is successful, the API will respond with `HTTP 204`.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


