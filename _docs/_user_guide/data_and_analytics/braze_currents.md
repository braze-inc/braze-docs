---
page_order: 3
nav_title: Currents

layout: featured

page_type: landing
description: "This landing page will tell you more about and guide you to articles related to the Braze data product called Currents."
tool: currents

guide_top_header: "Braze Currents"
guide_top_text: "Understanding the impact of your engagement strategy is critical in informing your iteration and optimization of your communications with your users. To ensure that this valuable engagement data is tightly integrated with the rest of your operations and help amplify your investment in data science, the Braze platform tracks a wide array of event data from your integration for analysis, retargeting, and other use-cases elsewhere within your own systems. <br> <br>The Currents tool continuously streams data to one of <a href='https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/available_partners/'>our many data partners</a>, empowering you to use the unique and valuable data Braze creates to power your BI and analytics efforts in other best-in-class platforms."

guide_featured_title: "Section Articles"
guide_featured_list:
- name: "Setting Up Currents"
  link: /docs/user_guide/data_and_analytics/braze_currents/setting_up_currents/
  fa_icon: fas fa-warehouse
- name: "Available Partners"
  link: /docs/user_guide/data_and_analytics/braze_currents/available_partners/
  fa_icon: fas fa-handshake
- name: "Event Delivery Semantics"
  link: /docs/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/
  fa_icon: fas fa-keyboard
- name: "Message Engagement Events"
  link: /docs/user_guide/data_and_analytics/braze_currents/message_engagement_events/
  fa_icon: fas fa-reply-all
- name: "Customer Behavior Events"
  link: /docs/user_guide/data_and_analytics/braze_currents/customer_behavior_events/
  fa_icon: fas fa-user
- name: "How Braze Uses Currents"
  link: /docs/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/
  fa_icon: fas fa-arrows-alt
- name: "Transfer Data from Amazon"
  link: /docs/user_guide/data_and_analytics/braze_currents/s3_to_snowflake/
  fa_icon: fab fa-amazon
- name: "Transfer Data to Redshift"
  link: /docs/user_guide/data_and_analytics/braze_currents/transferring_data_to_redshift/
  fa_icon: fas fa-exchange-alt

---

## Currents Capabilities

Currents allows you to…
* Stream Braze event data into a data warehouse or to one of [our analytics partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) for detailed analysis.
* Stream Braze event data continuously to power business intelligence tools, machine learning algorithms, and more.
* Route Braze event data to a variety of other systems using [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/) or [mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/).
* There’s so much more you can do with event data, accessed by Currents. Trust us—[we use Currents, too]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!

## Access Currents

A Currents connector is already included in many of our pro- and enterprise-level packages. If you’re interested using Currents, reach out to your account manager. Your account manager and our data specialists can assist in your Currents [setup and integration]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/).
<br>



## Change Log

### 2020-07-15
* Added CANVAS_VARIATION_NAME and CANVAS_STEP_NAME to the following events:
  * users.behaviors.subscriptiongroup.StateChange
  * users.canvas.Conversion
  * users.canvas.Entry
  * users.messages.contentcard.Click
  * users.messages.contentcard.Dismiss
  * users.messages.contentcard.Impression
  * users.messages.contentcard.Send
  * users.messages.email.Bounce
  * users.messages.email.Click
  * users.messages.email.Delivery
  * users.messages.email.MarkAsSpam
  * users.messages.email.Open
  * users.messages.email.Send
  * users.messages.email.SoftBounce
  * users.messages.email.Unsubscribe
  * users.messages.inappmessage.Click
  * users.messages.inappmessage.Impression
  * users.messages.pushnotification.Bounce
  * users.messages.pushnotification.IosForeground
  * users.messages.pushnotification.Open
  * users.messages.pushnotification.Send
  * users.messages.sms.CarrierSend
  * users.messages.sms.Delivery
  * users.messages.sms.DeliveryFailure
  * users.messages.sms.Rejection
  * users.messages.sms.Send
  * users.messages.webhook.Send
