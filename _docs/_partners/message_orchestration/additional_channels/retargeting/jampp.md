---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "This article outlines the partnership between Braze and Jampp, a performance marketing platform for acquiring and retargeting mobile customers."
page_type: partner
search_tag: Partner

---

# Jampp

> Jampp is a performance marketing platform for acquiring and retargeting mobile customers. It combines behavioral data with predictive and programmatic technology to generate revenue for advertisers by showing personal, relevant ads that inspire consumers to purchase for the first time, or more often.

Braze customers can integrate with Jampp by configuring the Braze webhook channel to stream events into Jampp. As a result, customers can add richer data sets to their retargeting initiatives with Jampp within the mobile advertising ecosystem.

## Retargeting cases

Some examples of when you would want to retarget customers with an ad:
- When a customer’s email or push subscription state changes.
- How a customer interacted with a Braze messaging campaign.
- If the customer has triggered a specific geofence.

One of the best ways to accomplish this is to use Braze as well as a retargeting partner specialized in mobile, such as Jampp. You want the retargeting partner to receive automated user info from Braze using webhooks. You’ll be able to leverage Braze’s targeting and triggering abilities to send events to Jampp, which could then be used to define retargeting campaign definitions in Jampp.

## Prerequisites for integration

This integration supports iOS and Android apps.

Requirement   | Source | Description
--------------|--------| -----
Android App ID | Braze | Your unique application identifier for Android (i.e. “com.example”).
iOS App ID | Braze | Your unique application identifier for iOS (i.e. “012345678”).
Enable IDFA Collection in Braze SDK | Braze | [IDFA Collection][4] is optional within the Braze SDK and disabled by default.
Collection of Google Advertising ID via custom attribute | Google | Google Advertising ID collection is optional for customers and can be collected as a [custom attribute][5].
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Braze does not automatically collect the device IDFA/AAID so you must store these values yourself. Please be aware that you may require user consent to collect this data.
{% endalert %}

# Integration

### Step 1: Create a webhook template in Braze

You can create this from the `Templates & Media` section, or create a new webhook campaign in Braze.

![Jampp_Webhook_Template][6]

### Step 2: Fill out your template

For this webhook, all data is passed on alongside the HTTP URL as query string parameters. The following parameters that need to be defined:

- You’ll need to set the event name. This is to define the name of the event that will appear in your Jampp dashboard.
- Jampp requires you to pass along your app’s unique application identifier for Android (i.e. “com.example”) and iOS (i.e. “012345678”).
- You’ll also need to insert [Liquid][1] for the appropriate custom attribute you’re tracking the Google Advertising ID.

Below is an example of what your Webhook URL might look like:

{% raw %}
```
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```

Elements (from sample above) to modify before sending the campaign:
1. `{% assign event_name = 'your_jampp_event_name' %}`
2. `{% assign android_app_id = 'your_android_app_id' %}`
3. `{% assign iOS_app_id = 'your_iOS_app_id' %}`
4. `&google_advertising_id={{custom_attribute.${aaid}}`
{% endraw %}

Please note that in this example the Google Advertising ID is listed as `aaid` but you will need to replace it with the custom attribute name your developers set.

After defining the parameters above, insert this Liquid code template into the Webhook URL field and edit as needed. You do not have to define a Request Body for this webhook. Here is the template in Braze:

![Webhook Template Jampp][2]

#### Request headers and method

The `Content-Type` should be pre-populated as a key-value pair within the webhook template.

![Jampp Method][3]

### Step 3: Preview your request

To ensure the request is rendering properly for different users, use the Message Preview. A good approach is to preview the Webhook for both Android as well as iOS users. You can also send test requests for these users. If the request was successful the API responds with `HTTP 204`.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[6]: {% image_buster /assets/img/jampp_webhook_template.png %}
