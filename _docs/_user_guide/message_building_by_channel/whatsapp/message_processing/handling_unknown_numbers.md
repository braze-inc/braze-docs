---
nav_title: Handling unknown phone numbers
article_title: Handling Unknown Phone Numbers
description: "This reference article covers how Braze will go about handling unknown phone numbers for WhatsApp users."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Handling unknown phone numbers

> You may find that after you get WhatsApp up and running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

## Opt-in/out and custom keyword workflow for unknown numbers

Braze will first attempt to find a user with a matching number. If none is found, Braze automatically addresses an unknown number in one of two ways:

1. **If a trigger word with an [opt-in Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) is set up:**
- Braze creates an anonymous profile
- We assign a user alias to the profile with the following details:
  - An `alias_name` with the value being the user's provided phone number
  - An `alias_label` with the value `phone`
- Our system sets the phone attribute
- The user is subscribed to the corresponding subscription group based on the logic that is set up within the Canvas<br><br>
2. **If no opt-in Canvas is set up:**
- Braze creates an anonymous profile
- We assign a user alias to the profile with the following details:
  - An `alias_name` with the value being the user's provided phone number
  - An `alias_label` with the value `phone`
- Our system sets the phone attribute
- The user's subscription status will default to `unsubscribed` for all WhatsApp subscription groups<br><br>

