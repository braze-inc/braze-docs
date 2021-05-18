---
nav_title: "MMS FAQs"
page_order: 3
description: "This reference article covers some of the most common MMS FAQs."
page_type: reference

channel:
  - MMS
---

# MMS FAQs

> On this page, we’ll attempt to answer your most stringent questions about MMS!

{% details Does MMS require a separate onboarding process? %}
No. MMS is now included in our SMS onboarding process. Existing customers who already went through onboarding can start sending MMS campaigns after completing the following steps. 

1. Complete MMS purchase.
2. Reach out to Braze Onboarding to request the MMS feature to be flipped on. This will enable MMS and an SMS/MMS Subscription group will be updated/created for you. 

Next, the Braze onboarding team will make sure your short and long codes are enabled (in the US and Canada) for MMS. They will also update your subscription groups to show your current numbers that were added or enabled for MMS. 
Once these steps are complete, you can send MMS messages right away from our native SMS composer. 
{% enddetails %}

{% details Does MMS and SMS pricing differ? %}
MMS and SMS have different costs and are charged separately based on volume. Please reach out to the Braze Onboarding team for pricing information.
{% enddetails %}

{% details Are there any changes to Currents data? %}
No, the same level of insight will be provided when sending an MMS message. 
{% enddetails %}

{% details Why can't I find MMS on my dashboard even though the feature is enabled? %}
MMS is only displayed on the Braze dashboard when a subscription group is considered "MMS enabled". This is reflected by an MMS tag when selecting the subscription group on the composer of an SMS/MMS message. This means that at least one number in the subscription group is capable of sending an MMS message. 
{% enddetails %}

{% details When receiving an MMS message, the image and message body order are inconsistent, sometimes showing the image second. Can I control the prioritization? %}
Braze has no control over the display order for when both a message-body and images are included in an MMS message. This is dependent on several factors including but not limited to, the carrier receiving the message, the device receiving the message, and the overall size of the message.
{% enddetails %}