---
nav_title: Handling Unknown Phone Numbers
article_title: Handling Unknown Phone Numbers
description: "This reference article covers how Braze will go about handling unknown phone numbers for WhatsApp users."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Handling unknown phone numbers

> You may find that once you get WhatsApp up and running with Braze that you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

## Opt-in/out and custom keyword workflow for unknown numbers

Braze will attempt to find a user with a matching number first. If none is found, Braze automatically addresses an unknown number in one of two ways:

1. **If a trigger word with an [opt-in Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) is set up:**
- Braze creates an anonymous profile
- Our system sets the phone attribute
- Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.<br><br>
2. **If a trigger word with an opt-out Canvas is set up:**
- Braze creates an anonymous profile
- Our system sets the phone attribute
- Unsubscribes the user from the corresponding subscription group based on what opt-out keyword was received by Braze.<br><br>

