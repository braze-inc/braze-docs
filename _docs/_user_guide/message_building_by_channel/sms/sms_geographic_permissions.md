---
nav_title: "SMS Geographic Permissions"
article_title: SMS Geographic Permissions
description: "This article covers the country allowlist for SMS Geographic Permissions, which allows you to choose which countries SMS can be delivered to."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# SMS Geographic Permissions

> SMS Geographic Permissions enhance security and protect against fraudulent SMS traffic by enforcing controls on the countries to which you can send SMS messages. You can specify an allowlist of countries to make sure that SMS messages are only sent to approved regions. Only admins can make changes to the country allowlist. Non-admin users have access to a read-only version of the allowlist that indicates which countries a subscription group is able to send to.

![The read-only SMS Geographic Permissions section for a non-admin user with the United States and United Kingdom selected in the "Country allowlist".][6]{: style="max-width:80%;"}

## Configuring your SMS country allowlist

If you're an admin, you can configure the countries that are on the allowlist. The country allowlist is configured at the [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) level. You can access it by going to **Audience** > **Subscriptions** and selecting an SMS subscription group. The allowlist is under **SMS Geographic Permissions**.

![The editable SMS Geographic Permissions section for an admin with Australia, Canada, and the United States selected in the "Country allowlist".][1]{: style="max-width:80%;"}

### Selecting countries

Add countries to the allowlist with the dropdown. The most common SMS countries are shown at the top, with others shown below. You can also search for countries by typing in the text field.

![The "Country allowlist" dropdown with the most common countries displaying at the top.][2]{: style="max-width:80%;"}

Remove previously selected countries by clearing the respective boxes next to them.

### Saving your changes

Changes will take effect after you select **Save**. Removing countries from your allowlist will prevent all SMS and MMS messages from sending to numbers in those countries.

![Warning modal confirming the countries that will be deleted from the allowlist.][3]{: style="max-width:70%;"}

## High-risk countries

Certain countries have a higher risk of SMS traffic pumping. These countries are indicated by a **High Risk** tag in the country dropdown.

![The country dropdown with Azerbaijan having a "High Risk" tag.][4]{: style="max-width:80%;"}

If you allow sending in these countries, you must first acknowledge the risk of doing so before the country is added to your allowlist.

{% alert note %}
Limit the countries on your allowlist to only those required to support your business needs. This will minimize your potential for fraudulent traffic. For more guidance on preventing SMS traffic pumping, view [SMS traffic pumping fraud FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibility of blocked sends

Attempted sends to countries that aren't on your allowlist will be aborted. Aborted messages will be logged to the [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) and within the [SMS abort message engagement event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Aborted messages caused by blocked sends show as **Aborted Message Errors** and have the message "The recipient's phone number is in a blocked country".

![Abort log showing several SMS sendds that were blocked because the phone number is in a blocked country.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}