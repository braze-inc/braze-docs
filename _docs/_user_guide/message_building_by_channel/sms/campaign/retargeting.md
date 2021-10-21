---
nav_title: User Retargeting
article_title: SMS User Retargeting
page_order: 5
description: "This reference article covers how users can retarget their messages by users SMS interactions."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# SMS retargeting

In addition to changing the user’s subscription state and sending auto-responders based on incoming keywords, Braze will also record interactions to the user profile for filtering and triggering messages. These filters and triggers allow you to filter users that have received SMS messages, received SMS messages from a specific SMS campaign, and trigger messages as users receive SMS messages from a specific SMS campaign. 

{% alert tip %}
To read more about custom keywords and how to set up two-way messaging to take advantage of these retargeting options, visit our [custom keyword]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/) article.
{% endalert %}  

## Retargeting options

### Filter users by sms
Users can be filtered by when they last received an SMS or if they have received an SMS from a specific SMS campaign. Filters can be set in the Target Users step of the campaign builder. 

__Filter by Last Received SMS__<br>
![Filter 1][2]

__Filter by Received Messages from SMS Campaign__<br>
Filters users who have received a message from a specific SMS campaign. With this filter, you also have the option to filter off those that have not received messages from an SMS campaign. <br>
![Filter 2][1]

### Trigger messages as users receive sms
To trigger messages as users receive SMS messages from a specific campaign, select __Interact with Campaign__ as the trigger action. Next, select __Receive SMS__ and the SMS campaign you would like to use. <br><br>
![Trigger][3]

## Keyword category specific retargeting

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you are also able to create up to 10 of your own keyword categories, allowing you to identify arbitrary keywords and responses. These categories can be used for filtering and retargeting. To read more about SMS keyword categories and how to set them up, visit our documentation [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Filter by recency

Filter for the recency of a user responding to your SMS Program. This filter will evaluate the LAST date a user sent an inbound SMS that is within one of the keyword categories. 

![picture][6]

### Trigger messages by keyword

Messages can be triggered as users send messages inbound based on keyword categories (user sent any one of the keywords) or other keywords (user sent a keyword that does not fall into one of the existing categories). These triggers are set in the Delivery step of the campaign builder.

__Trigger by Inbound Keyword Category__<br>
![picture][7]{: style="margin-top:10px;"}

__Trigger by Arbitrary Keywords__<br>
Note when triggering a message on an "Other" keyword response, you will have the opportunity to evaluate the keyword body on an exact text match. This match follows the same rules as noted above: Only the __exact, single-word message__ will be processed (case _insensitive_). A keyword sent of `Hello Braze!` would not match the criteria shown in the example below. 
![picture][8]{: style="margin-top:10px;"}

__Template Keywords__<br>
When triggering a campaign or Canvas Step on an inbound SMS or MMS, you can optionally template the text and/or media attachments that your user sent into the body of your campaign or Canvas with Liquid. This will enable you to access the user's response which you can then include in your reply, apply conditional logic to, or anything else you can do with Liquid. 

![picture][16]{: style="max-width:80%;"}
<br><br>
![picture][17]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %} 
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
