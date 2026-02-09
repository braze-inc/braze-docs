---
nav_title: "Geographic permissions"
article_title: Geographic Permissions
description: "This article covers the country allowlist for Geographic Permissions, which allows you to choose which countries SMS, MMS, and RCS can be delivered to."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Geographic Permissions

> Geographic Permissions enhance security and protect against fraudulent SMS, MMS, and RCS traffic by enforcing controls on the countries to which you can send messages. You can specify an allowlist of countries to make sure that SMS, MMS, and RCS messages are only sent to approved regions. Only admins can make changes to the country allowlist. Non-admin users have access to a read-only version of the allowlist that indicates which countries a subscription group is able to send to.

If you're an admin, you can configure the countries that are on the allowlist. The country allowlist is configured at the [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/) level. You can access it by going to **Audience** > **Subscriptions** and selecting an SMS, MMS, or RCS subscription group. The allowlist is under **Geographic Permissions**.

![The editable SMS Geographic Permissions section for an admin with several countries selected in the "Country allowlist".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Selecting countries

Add countries to the allowlist with the dropdown. The most common SMS and RCS countries are shown at the top, with others shown below. You can also search for countries by typing in the text field.

![The "Country allowlist" dropdown with the most common countries displaying at the top.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remove previously selected countries by clearing the respective boxes next to them.

### Saving your changes

Changes will take effect after you select **Save**. Removing countries from your allowlist will prevent all SMS, MMS, and RCS messages from sending to numbers in those countries.

![Warning modal confirming the countries that will be deleted from the allowlist.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## High-risk countries

Certain countries have a higher risk of SMS and RCS traffic pumping. These countries are indicated by a **High Risk** tag in the country dropdown.

![The country dropdown with Azerbaijan having a "High Risk" tag.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

If you allow sending in these countries, you must first acknowledge the risk of doing so before the country is added to your allowlist.

{% alert note %}
Limit the countries on your allowlist to only those required to support your business needs. This will minimize your potential for fraudulent traffic. For more guidance on preventing SMS traffic pumping, view [SMS traffic pumping fraud FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibility of blocked sends

Attempted sends to countries that aren't on your allowlist will be aborted. Aborted messages will be logged to the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) and within the [SMS abort message engagement event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Aborted messages caused by blocked sends show as **Aborted Message Errors** and have the message "The recipient's phone number is in a blocked country".

![Abort log showing several SMS sendds that were blocked because the phone number is in a blocked country.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

