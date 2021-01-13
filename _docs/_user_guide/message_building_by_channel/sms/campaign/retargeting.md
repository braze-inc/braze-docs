---
nav_title: SMS User Retargeting
page_order: 5
description: "This reference article covers how users can retarget their messages by users SMS interactions."
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

# SMS Retargeting

In addition to changing the user’s subscription state and sending auto-responders based on incoming keywords, Braze will also record interactions to the user profile for filtering and triggering messages. These filters and triggers allow you to filter users that have received SMS messages, received an SMS messages from a specific SMS campaign, and trigger messages as users receive an SMS messages from a specific SMS campaign.  

## Filter Users by SMS
Users can be filtered by when they last received an SMS or if they have received an SMS from a specific SMS campaign. Filters can be set in the Target Users step of the campaign builder. 

__Filter by Last Received SMS__<br>
![Filter 1][2]

__Filter by Received Messages from SMS Campaign__<br>
Filters users who have received a message from a specific SMS campaign. With this filter, you also have the option to filter off those that have not received messages from an SMS campaign. <br>
![Filter 2][1]

## Trigger Messages as Users Receive SMS
To trigger messages as users receive SMS messages from a specific campaign, select __Interact with Campaign__ as the trigger action. Next, select __Receive SMS__ and the SMS campaign you would like to use. <br><br>
![Trigger][3]

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %} 