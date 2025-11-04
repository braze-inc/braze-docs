---
nav_title: Handling unknown phone numbers
article_title: Handling Unknown Phone Numbers
page_order: 4
description: "This reference article covers how Braze processes unknown phone numbers from new users."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Handling unknown phone numbers - new users

> You may find that after you get SMS, MMS, and RCS up and running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

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

