---
nav_title: Content Cards In Canvas
platform: Canvas
subplatform: Create a Canvas
page_order: 5
---

# Content Cards In Canvas

Content Cards can be sent to your customers as part of their Canvas journey. This article describes features and nuances specific to using Content Cards as a messaging channel within Canvas.

As with other Canvas messaging channels, Content Cards will be sent to a user's device when they meet the audience and targeting criteria specified for its step. After the Content Card is sent, it will be available in each eligible user's feed the next time their cards feed is refreshed.

Two options which will change how the Content Card step will interact with Canvas are its [Expiration](#content-card-expiration) and [Advancement Behavior](#advancement-behavior-options).

## [Content Card Expiration](#content-card-expiration)
When composing a new Content Card you have the option to choose when it should expire from the user's feed, based on its send time. The expiration time will begin only once the card reaches the canvas step and the card is sent.

If a sent card expires before a user has viewed it in your app, they will no longer be eligible to receive this card as it will be removed from their feed the next time their cards are refreshed.


{% alert important %}
 The content card will be available until it expires, even if the user has moved to subsequent steps. If you do not want the content card to be live when next steps in the Canvas are delivered, ensure that the expiration is shorter than the delay on subsequent steps.
{% endalert %}

## [Advancement Behavior Options](#advancement-behavior-options)

The Advancement Behavior option allows you to control when a user should advance to their next eligible step. [Steps that send only Content Cards](#steps-with-in-content-cards-only) have different advancement options than [steps with multiple message types](#steps-with-multiple-message-channels) (push, email, etc.).

### [Steps with Content Cards Only](#steps-with-in-content-cards-only)

If a step conatins only Content Cards (and no other messaging channel), you can control the advancement behavior with the following options:

![content-card-single-channel.png][2]

| Option | Description |
|---|---|
| Advance When Message Sent | Users will advance to the next steps of the Canvas when the Content Card has been succesfully sent. Use this option when you want users to advance only if the card will be sent and not aborted. |
| Immediately Advance Audience | Users will advance to the next steps of the Canvas when the Content Card sending is attempted. If the card is aborted and not sent, users will still advance to the next step. Use this option when you want users to advance regardless of whether the content card is sent succesfully or aborted. |



### [Steps with Multiple Channels](#steps-with-multiple-message-channels)

![content-card-multiple-channels.png][3]

Canvas steps with a Content Card and another messaging channel have the following advancement options:

| Option | Description |
|---|---|
| Message Sent | When message sent is selected, users must be successfully sent at least one of the message types in the step <br> <br>  _If the content card expires and the user hasn't been sent the email/webhook/push or viewed the content card, they will exit the Canvas and will not advance to subsequent steps._ |
| Immediately Advance Audience | When this option is selected, everyone in the step's audience will advance to next steps after the delay elapses, whether they have seen the noted message or not.  <br> <br> _Users must match the step's segment and filter criteria in order to advance to next steps._ |


## Use Cases

When should you use this feature? 

#### Promotional Offers

Add cards to a user's feed as they qualify for specific promotions and advertisements. For example, if a user becomes eligible for a new offer after performing an action or making a purchase, using Canvas you can send them a Content Card, in addition to other messaging channels, so that the next time they open the app the offer is available to them.

#### Push Notification Inbox

There are times when a user may dismiss a push notification or delete an email, but you want to remind them or promote the offer in case they change their mind.

Using Canvas, you can add a step that sends both a Content Card and Push Notification to give users a persistent "inbox" of cards that align with promotional messages sent via Push. 

#### Categories for Offers and Promotions

Give users different categories for offers or content they can browser through. This can be done using Key Value Pairs within your Content Card campaign: **LINK NEEDED to KVP customization**