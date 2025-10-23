---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "This reference article outlines the partnership between Braze and Remerge, a purpose-built app for retargeting at scale, arming you with tools to efficiently segment app audiences and retarget users."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) is purpose-built for app retargeting at scale, arming you with tools to efficiently segment app audiences and retarget users.

_This integration is maintained by Remerge._

## About the integration

The Braze and Remerge integration helps you develop robust, cross-channel lifecycle marketing campaigns by sending user data to Remerge via webhook events to help retarget users through their mobile demand-side platform.

## Prerequisites

| Requirement | Description |
|---|---|
| Remerge account | A Remerge account is required to take advantage of this partnership. |
| Remerge webhook key | This key will be provided by Remerge. |
| Android app ID | Your unique Braze application identifier for Android (such as "com.example"). |
| iOS app ID | Your unique Braze application identifier for iOS (such as "012345678"). |
| Enable IDFA collection in Braze SDK | IDFA collection is optional within the Braze SDK and disabled by default. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create your Braze webhook template

To create a Remerge webhook template for future campaigns or Canvases, navigate to the **Templates** > **Webhook Templates** in the Braze platform. 

If you would like to create a one-off Remerge webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.

In your new Webhook template, fill out the following fields:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In the webhook URL, you must:
- Use the `https://remerge.events/event` API to send your webhook events.
- Set the event name. This name will appear in your [remerge.io](https://www.remerge.io/) dashboard.
- Pass your app's unique application identifier for Android (such as "com.example") and iOS (such as "012345678") to remerge.
- Define a key; Remerge will provide this.

![The webhook URL and message preview shown in the Braze webhook builder.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze does not automatically collect the device IDFA/AAID, so you must store these values yourself. Be aware that you may require user consent to collect this data.
{% endalert %}

#### Request headers and method

The Remerge webhook requires an HTTP method and request header.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![The request headers, HTTP method, and message preview shown in the Braze webhook builder.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Request body

You do not have to define a request body for this webhook.

## Step 2: Preview your request

Preview the message to ensure the request is rendering properly for different users. We recommend previewing and sending test requests for both Android and iOS users. If the request is successful, the API will respond with `HTTP 204`.

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


