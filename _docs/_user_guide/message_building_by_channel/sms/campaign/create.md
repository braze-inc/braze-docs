---
nav_title: Creating an SMS Campaign
article_title: Creating an SMS Campaign
page_order: 5
description: "This reference article covers the steps involved in building out and creating an SMS campaign."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS
---

# Create an SMS Campaign

> SMS campaigns are great for directly reaching and programmatically conversing with your customers. You can use Liquid and other dynamic content to create a personal experience with your users and create an environment that fosters and enhances an unobtrusive user experience with your brand. 

## Step 1: Choose Where to Build Your Message

SMS is available in both campaigns and Canvas.

{% tabs local %}
  {% tab Campaigns %}
  Click __Create Campaign__ to open a new messaging wizard for in-app message campaigns. Then, follow the flow of the messaging wizard to quickly create and launch your SMS campaign.

  ![Create SMS Campaign]({% image_buster /assets/img/sms_campaign_setup.gif %})

1. Name your campaign something clear and meaningful.
2. Add __Teams__ and __Tags__, as necessary.
3. Add and name as many Variants as you need for this campaign.
  - You can choose different platforms, message types, and layouts for each of your added Variants.
4. Select the __Subscription Group__ to ensure you're sending your message to the proper users. When selecting a subscription group, Braze will automatically add a segmenting filter, ensuring that only users subscribed will receive the campaign. Only long codes and short codes that belong to that subscription group will be used to send SMS to target users. 

  {% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional Variants - you will be able to choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

 {% endtab %}
 {% tab Canvas %}
 After you have [created and set up your Canvas using the Canvas wizard]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/),

1. Name your step something clear and meaningful.
2. Add a Delay, as necessary.
3. Filter your Audience, as necessary.
4. Choose your advancement options, as necessary.
5. Choose all other messaging channels which you would like to pair with your message.

{% alert important %}
You cannot have multiple in-app message variants in a single step.
{% endalert %}

{% endtab %}
{% endtabs %}


## Step 2: Compose Your SMS

Composing an SMS is easy! Just write your message using languages and personalization (Liquid, Connected Content, and Emojis) as needed. Be sure to adhere to our Message Copy Limits to reduce your chances of overage charges.

{% alert important %}
Before proceeding, read our [SMS Message Copy Limits and Message Segment documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/). SMS message segments are the character batches that phone carriers use to measure text messages. Messages are charged per message segment, so clients leveraging SMS greatly benefit from understanding the nuances of how messages will be split.
{% endalert %}

![Compose SMS]({% image_buster /assets/img/sms_campaign_compose.gif %})

{% alert tip %}
{% raw %}
If you plan to use Liquid, be sure to include a default value for your chosen personalization so, in the event your user profile of the recipient is incomplete, they will not receive a blank placeholder `Hi, !`, instead of their name or a coherent sentence.
{% endraw %}
{% endalert %}

## Step 3: Preview and Test Your Message

Braze always recommends previewing and testing your message before sending.

![Test SMS]({% image_buster /assets/img/sms_campaign_test.gif %})

{% alert tip %}
If you'd like to test how many segments yout SMS may be split into, test your copy length [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#sms-segment-calculator).
{% endalert %}

## Step 4: Configure Message Delivery

Decide how, when, and why your message will be delivered. You can either schedule your message for a specific time or trigger it off of a user's action. You can also trigger it via API for both [campaigns]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) and [canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/).

![SMS Delivery]({% image_buster /assets/img/sms_campaign_delivery.gif %})

## Step 5: Target Users & Select Segment

In this step, you'll choose which users receive your message. You should have already chosen the Subscription Group, which narrows users by the level or category of communication they wish to have with you. In this step, you will select the larger audience from your Segments, and narrow that segment further with our Filters, if you choose.

![SMS Targeting]({% image_buster /assets/img/sms_campaign_targeting.gif %})

{% alert tip %}
Interesting in SMS retargeting? Visit our SMS [retargeting article]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) to learn more. 
{% endalert %}

## Step 6: Choose Conversion Events

Conversion events help you measure the success of your campaign:
- If you are using Geotargeting to trigger an SMS message that has an end goal of the user making a purchase, set the conversion event to a "Purchase".
- If you are attempting to drive the user to your app, set the conversion event to "Starts Session".

You can also set custom conversion events based on your specific use case. Get creative and think about how you truly want to measure this campaign's success.

![SMS Conversion Events]({% image_buster /assets/img/sms_campaign_conversion.gif %})

## Step 7: Confirm Details and Launch!

If you're using campaigns, you'll have the opportunity to confirm its details. If you're using Canvas, be sure to confirm the details of each of the pieces.

![SMS Confirm]({% image_buster /assets/img/sms_campaign_confirm.gif %})
