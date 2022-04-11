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

### Filter users by SMS

Users can be filtered by when they last received an SMS or if they have received an SMS from a specific SMS campaign. Filters can be set in the Target Users step of the campaign builder. 

**Filter by last received SMS**<br>
![Segmentation filter Last Received SMS after December 8, 2020.][2]

**Filter by received messages from SMS campaign**<br>
Filters users who have received a message from a specific SMS campaign. With this filter, you also have the option to filter off those that have not received messages from an SMS campaign. <br>
![Segmentation filter Has received message from campaign "SMS retargeting".][1]

### Trigger messages as users receive SMS

To trigger messages as users receive SMS messages from a specific campaign, select **Interact with Campaign** as the trigger action for an action-based campaign. Next, select **Receive SMS** and the SMS campaign you would like to use.

![][3]

## Keyword category-specific retargeting

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you are also able to create up to 10 of your own keyword categories, allowing you to identify arbitrary keywords and responses. These categories can be used for filtering and retargeting. To read more about SMS keyword categories and how to set them up, refer to [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Filter by recency

Filter for the recency of a user responding to your SMS program. This filter will evaluate the last date a user sent an inbound SMS that is within one of the keyword categories. 

![Segmentation filter Last sent SMS to subscription group "Marketing SMS" with keyword "Opt-in" after August 11, 2020.][6]

### Filter by campaign or Canvas attribution

Filter for users who have replied to a specific SMS campaign or Canvas step, keyword category, or tag.

**Filter by replied to a specific campaign category**<br>
![Campaign with the filter "Has replied to SMS" for campaign "SMS-283" "Promotion". Under the filter the feature mentions "This filter will expire 25 months after the last message is sent from "Promotion" if it is not being used in any active campaign."][12]

**Filter by replied to a campaign or Canvas with a specific tag**
![Campaign with the filter "Has replied to SMS" for campaign or Canvas with tag "Curbside Messaging Service C".][13]

**Filter by replied to a specific step**
![Campaign with the filter "Has replied to SMS" for step "SMS Double Opt" "Step - Help".][11]

### Trigger messages by keyword

Messages can be triggered as users send messages inbound based on keyword categories (user sent any one of the keywords) or other keywords (user sent a keyword that does not fall into one of the existing categories). These triggers are set in the Delivery step of the campaign builder.

**Trigger by inbound keyword category**<br>
![Action-based SMS campaign with the segmentation filter Sent keyword "Opt-in" to subscription group "Marketing SMS".][7]{: style="margin-top:10px;"}

**Trigger by arbitrary keywords**<br>
Note when triggering a message on an "Other" keyword response, you will have the opportunity to evaluate the keyword body on an exact text match. This match follows the same rules as noted: Only the **exact, single-word message** will be processed (case _insensitive_). A keyword sent of `Hello Braze!` would not match the criteria shown in the example below. 
![Action-based SMS campaign with keyword category as "Other" where the message body is exactly "Hello" or "Hey".][8]{: style="margin-top:10px;"}

**Template keywords**<br>
When triggering a campaign or Canvas Step on an inbound SMS or MMS, you can optionally template the text and/or media attachments that your user sent into the body of your campaign or Canvas with Liquid. This will enable you to access the user's response which you can then include in your reply, apply conditional logic to, or anything else you can do with Liquid. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %} 
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %} 
