---
nav_title: "SMS Campaign Analytics"
page_order: 7
description: "This reference article covers SMS metrics used at Braze, as well as how to view them in your campaign."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# Reporting & Analytics
To see the meanings of all SMS metrics, check the [Metrics Glossary][1].

## SMS Metrics
- **Sent**: A campaign or canvas step has been launched or triggered and an SMS has been sent from Braze. It is possible that the SMS does not reach a user's device due to errors, as explained below.
- **Sent to Carrier**: Braze has attempted to send the SMS through to the carriers. This stat is the sum of Confirmed Deliveries, Rejections, and sends where delivery or rejection was not confirmed by the carrier. There are instances where carriers do not provide delivery or rejected confirmation, as some carriers do not provide this confirmation or were unable to do so at the time of send.
- **Delivery Failures**: The SMS could not be sent due to queues overflow (sending SMS at a rate higher than your long or short codes can handle).
- **Confirmed Delivery**: The carrier has confirmed that the SMS was delivered to the target phone number. As a Braze customer, deliveries are charged toward your SMS allotment.
- **Rejections**: The SMS has been rejected by the carrier. This can happen for several reasons including carrier content filtering, availability of the destination device, the phone number is no longer in service, etc. As a Braze customer, rejections are charged toward your SMS allotment.
- **Opt-Out**: A user replied to your message with an [Opt-Out Keyword][3] and was unsubscribed from your SMS program. A user reply is measured anytime a user sends an inbound message within four hours of receiving your message. 
- **Help**: A user replied to your message with a [HELP Keyword][3] and was dispatched a HELP auto-response. A user reply is measured anytime a user sends an inbound message within four hours of receiving your message. 


### Control Groups

To measure the impact of an individual SMS, a [Control Group][2] can be added to an A/B Test.

The top-level campaign details __will not__ include metrics from the Control Group variant.

## Reporting in Campaigns

Campaigns will deliver your reports in a series of blocks. You may see more or less than those listed in the tabs below, but each has its useful purpose.

{% tabs %}

{% tab Campaign Details %}

**Campaign Details**

The Campaign Details analytics block will give you a high-level overview of the entire SMS campaign.

![sms_campaign_details]({% image_buster /assets/img/sms/sms_campaign_details.png %})

{% endtab %}

{% tab Message Performance %}

**Message Performance**

This block will define the performance of the message on multiple levels (by Variant, Audience %, Unique Recipients, Sends, Sends to Carriers, Confirmed Deliveries, Delivery Failures, Rejections, and more!) 

Click on the <i class="fa fa-eye preview-icon"></i> to view your message.

![sms_message_performance]({% image_buster /assets/img/sms/sms_message_performance.png %})

{% endtab %}

{% tab Historical Performance %}

**Historical Performance**

This block allows you to see the message's performance over a set time period on a timeline.

![sms_historical_performance]({% image_buster /assets/img/sms/sms_historical_performance.png %})

{% endtab %}

{% tab Keyword Responses %}

**Keyword Responses**

This block allows you to see the inbound keywords users replied with after receiving your message on a timeline 

![keyword_responses]({% image_buster /assets/img/sms/keyword_responses.png %})

{% endtab %}

{% tab Conversion Event Details %}

**Conversion Event Details**

This block will show you the performance of your conversion events for the SMS message campaign or canvas.

![CC_Conversion]({% image_buster /assets/img/cc-conversion.png %})

{% endtab %}
{% endtabs %}

## SMS Curent Events
Just like email, Braze receives user level events related to an SMS message as it makes its journey to a user. Any inbound SMS event will also be sent as a Currents [event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) through the SMS InboundReceived event. This will allow you to perform additional actions or reporting on the messages your users are texting in outside of the Braze platform. Please note that inbound messages are truncated past 1600 characters. 

![picture][9]{: style="max-width:80%;"}



[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
<<<<<<< HEAD
[9]: {% image_buster /assets/img/sms/sms_currents.png %}

=======
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords
>>>>>>> a536229ffbdc9a19e7ee8f3854cf6c1641799297
