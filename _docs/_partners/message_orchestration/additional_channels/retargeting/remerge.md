---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "This article outlines the partnership between Braze and Remerge, a purpose-built app for retargeting at scale, arming you with tools to efficiently segment app audiences and retarget users."
page_type: partner
search_tag: Partner

---

# Remerge

> Remerge is purpose-built for app retargeting at scale, arming you with tools to efficiently segment app audiences and retarget users.

Develop robust, cross-channel lifecycle marketing campaigns with the powers of Braze and Remerge combined—build segments on the Braze dashboard, then send via webhook to Remerge to retarget users through their mobile DSP.

# Remerge Retargeting Network

To use Remerge, configure the Braze webhook channel to connect Braze with retargeting actions. It is important to have an automatic way of enabling Braze and the retargeting system (i.e. Remerge) to have visibility of what the other system does and adapt from the other’s message. Ad retargeting is helpful if you have users who have push notifications disabled or users who haven’t opened your app recently.

For example, An unregistered user could receive a push campaign saying “Thanks for installing our app, sign up today!” Once the user has signed up after receiving the push campaign they would receive an adapted follow-up message in a retargeted ad such as “Thanks for signing up! Here is 10% off your first order.”

One of the best ways to accomplish this is to use Braze as well as a retargeting partner specialized in mobile, such as Remerge. You want the retargeting partner to receive automated user info from Braze using webhooks. You’ll be able to leverage Braze’s targeting and triggering abilities to send events to Remerge, which could then be used to define retargeting campaign definitions in remerge.io.

## Request URL and Body

For this webhook, all data is passed on alongside the HTTP URL as query string parameters. There are three parameters that need to be defined:

- You'll need to set the event name. This is to define the name of the event that will appear in your [remerge.io][65] dashboard
- Remerge requires you to pass along your app's unique application identifier for Android (i.e. "com.example") and iOS (i.e. "012345678")
- Finally, you need to define a key. This will be provided by Remerge

>  Braze does not automatically collect the device IDFA/AAID so you must store these values yourself. Please be aware that you may require user consent to collect this data.

Below is an example of what your Webhook URL might look like:
{% raw %}
```
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
After defining the parameters above, insert this Liquid code template into the Webhook URL field and edit as needed. You do not have to define a Request Body for this webhook. Here is the template in Braze:

![Webhook Template Remerge][67]

>  Remerge used to offer multiple endpoints depending on where your data is stored, however, they have now updated their docs with one single endpoint:

```
https://remerge.events/event
```
The old endpoints are still valid and will stay valid, however, Remerge recommends that customers switch to this new endpoint for reliability purposes.

You can find more information on Remerge's API endpoint [here][66].

## Request Headers and Method

This webhook does not require any *Request Headers*, but be sure to choose GET in the dropdown for the *HTTP Method*.

![Request Method Remerge][68]

## Preview Your Request

To ensure the request is rendering properly for different users, use the Message Preview. A good approach is to preview the Webhook for both Android as well as iOS users. You can also send test requests for these users. If the request was successful the API responds with `HTTP 204`.

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
