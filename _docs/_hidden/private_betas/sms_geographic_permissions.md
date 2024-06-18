---
nav_title: "SMS Geographic Permissions Allowlist"
article_title: SMS Geographic Permissions Allowlist
description: "This article covers the SMS geographic permissions allowlist, which allows you to choose which countries SMS can be delivered to."
page_type: reference
channel:
  - SMS
hidden: true
permalink: "/sms_geographic_permissions/"
  
---

# SMS geographic permissions allowlist

> The SMS geographic permissions allowlist enhances security and protects against fraudulent SMS traffic by enforcing controls on the countries to which you can send SMS messages. 

You can specify an allowlist of countries where SMS messages are permitted, making sure that messages are only sent to approved regions. You'll need the X permission to make changes to the allowlist.

## Configuring your SMS geographic permissions allowlist

The SMS geographic permissions allowlist is configured at the [Subscription Group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group) level. You can access it by going to **Audience** > **Subscriptions** and selecting an SMS subscription group. The allowlist is under **SMS Geographic Permissions**.

![The SMS Geographic Permissions section with Australia, Canada, and the United States selected in the "Country allowlist".][1]{: style="max-width:80%;"}

### Selecting countries

Add countries to the allowlist with the dropdown. The most common SMS countries are shown at the top, with others shown below. You can also search countries by typing into the textbook.

![The "Country allowlist" dropdown with the most common countries displaying at the top.][2]{: style="max-width:80%;"}

Remove previously selected coutnries by unchecking the respective boxes next to them.

### Saving your changes

Changes will take effect after you select **Save**. You'll receive a warning message when removing countries to confirm that you intended to do so.

![Warning modal confirming the countries that will be deleted from the allowlist.][3]{: style="max-width:70%;"}

{% alert important %}
Removing countries from your allowlist will prevent all SMS and MMS messages from sending to numbers in those countries.
{% endalert %}

## High-risk countries

Certain countries have a higher risk of SMS traffic pumping. These countries are indicated by a **High Risk** tag in the country dropdown.

![The country downdown with Azerbaijan having a "High Risk" tag.][4]{: style="max-width:80%;"}

If you allow sending in thse countries, you'll be asked to acknowledge the risk of doing so before the country is added to your allowlist.

{% alert note %}
We recommend limiting the countries on your allowlist to those required to support your business needs. This will minimize your potential for fradulent traffic. For more guidance on preventing SMS traffic pumping, view [SMS traffic pumping fraud FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}