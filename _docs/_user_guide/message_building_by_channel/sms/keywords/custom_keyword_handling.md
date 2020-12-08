---
nav_title: Custom Keyword Handling
page_order: 2
description: "This reference article covers how Braze processes custom keywords."
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

## Two-Way Messaging (Custom Keyword Responses)

Two-way messaging uses short codes and keywords to deliver text messages to mobile users. It requires end users to send a keyword to Braze to which that user will receieve an automatic reply. Applied correctly, two-way messaging can be an simple, immediate and dynamic solution to customer marketing, saving time and resources along the way. 

### Two Way Messaging Speeds

Two-way messaging leverges custom events to make this seemingly smooth customer client exchange possible. Due to the nature of two-way messaging, you may find a slight increase in response time. Below are the implications of including two-way messaging:

| Type | Speed | Notes | 
| ----- | ----- | ---- | 
| Known Phone Numbers | 3-5 Seconds | A known number is a number that has already been assigned a phone attribute and is already subscribed to a subscription group within Braze.
| Unknown Phone Numbers |  10-15 Seconds | An unknown number is one that has not yet been identifier. For more information on how Unknown phone numbers are dealt with, check out our [documentation][unknown].|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you require a faster sending speeds for unknown phone numbers, reach out to your customer sucess manager to discuss your options.

### Custom Keyword Messaging Handling

| Custom Event Fired |
| ------- | ------ |
| `sms_response_subscriptionName_custom` | Response Examples => Status, Coupons, News |
{: .reset-td-br-1 .reset-td-br-2}

| Included Event Properties |
| ------- | ------ |
| - `message_body`: users SMS response<br>- `to_number`: usually shortcode the clients used to send SMS<br>- `from_number`: user's phone number<br>- `sms_messsage_id`: messaging service ID | Message Body => <br>Users response returned as all lower case |
{: .reset-td-br-1 .reset-td-br-2}

- Anytime a user texts an SMS response that is not a default keyword to a phone number in a given Subscription Group, a custom event like `sms_response_SubscriptionGroupName_custom` with event properties `message_body`, `to_number`, `from_number`, and `sms_message_id` will be sent to Braze. 
- Use this custom event with the property `message_body` assigned as a custom keyword to trigger an SMS campaign from Braze.
- The `message_body` custom keyword value must be __lowercase__.

![picture][IMAGE2]

Note: This feature relies on user aliases in order to properly assign custom events to user profiles in Braze. If no Braze profile exists with a user alias of the user's phone number in E.164 format, the call to the users/track endpoint will fail silently. The alias should be set in the format below either through the SDK or the [new user alias endpoint][endpoint]:
1. alias_label: `phone` and alias_name: `users_phone_number`
2. Phone numbers must be in the E.164 format (e.g +19173337578). 

If using the new user alias endpoint, to ensure E.164 compliance, please add a "+" prefix as the default "phone" field does not automatically include this symbol.

## Managing Keywords and Auto Responses

SMS with Braze gives you the option to create keyword triggers, custom responses, and define keyword sets for multiple languages. 

### Add Keyword Triggers
In addition to the default opt-in and opt-out keywords listed above, you may also define your own keywords to trigger Opt-In, Opt-Out, and Help responses.

![Home][1]{: style="float:right;max-width:40%;margin-left:10px;""}
1. To define your own keywords, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select a keyword category to add a keyword to by selecting the pencil icon. 
3. In the dialogue box that pops up, add a keyword you would like to trigger this keyword category. Note that keywords are case sensitive, and universal keywords like `START`, `YES`, and `UNSTOP` cannot be changed.

### Manage Responses
You are able to manage your own responses that get sent to users after they text in a keyword to a specific keyword category.
1. To manage your keyword responses, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select a keyword category to edit a response for by selecting the pencil icon. 
3. In the dialogue box that pops up, edit and save your response. Please be mindful of the [Six Rules to get Compliance Right]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) as you create your response.<br><br>
![Responses][2]

### Define Keyword Sets
You can create keyword sets for different languages so the keywords received for different languages can be appropriately replied to.
![Language][3]{: style="float:right;max-width:30%;margin-left:15px;margin-top:15px;"}

1. To define a keyword set, navigate to the SMS section of the dashboard located under Subscription Groups. 
2. Under SMS Global Keywords, select __Add a Language__, and choose the appropriate language for your keyword set. Once clicked, a new global keyword list will be added to fill out with the necessary keywords and responses in the language you chose.<br>

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[3]: {% image_buster /assets/img/sms/keyword_language.png %} 

[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#handling-unknown-phone-numbers
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}


