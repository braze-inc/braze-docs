---
nav_title: Handling Unknown Phone Numbers
article_title: Handling Unknown SMS Phone Numbers
page_order: 4
description: "This reference article covers how Braze processes unknown SMS phone numbers from new users."
page_type: reference
channel:
  - SMS
  
---

# Handling unknown phone numbers - new users

> You may find that after you get SMS up and running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

{% alert important %}
Are you currently a non-native SMS client? If so, visit the [non-native SMS documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) for your corresponding handling unknown phone numbers article.
{% endalert %}

## Opt-in/out and custom keyword workflow for unknown numbers

Braze automatically addresses an unknown number in one of three ways:

1. If an opt-in keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.<br><br>
2. If an opt-out keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Unsubscribes the user from the corresponding subscription group based on what opt-out keyword was received by Braze.<br><br>
3. If any other custom keyword is texted:
  * Braze ignores the text message and does nothing.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164