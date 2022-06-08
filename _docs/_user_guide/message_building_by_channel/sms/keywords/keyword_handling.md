---
nav_title: Custom Keyword Handling
article_title: Custom Keyword Handling
page_order: 2
description: "This reference article covers how Braze deals with two-way SMS messaging and auto-responses. This includes explanations on how keyword triggering works as well as custom keyword categories and multi-language support."
page_type: reference
channel:
  - SMS

---

<br>
{% alert important %}
Are you currently a non-native SMS client? If so, visit the [non-native SMS documentation](/docs/user_guide/message_building_by_channel/sms/non_native/) for your corresponding keyword handling article.
{% endalert %}

## Two-way messaging (custom keyword responses)

Two-way messaging allows you to send messages and process the responses to those messages. It requires end-users to send a keyword to Braze, to which that user will receive an automatic reply. Applied correctly, two-way messaging can be a simple, immediate, and dynamic solution to customer marketing, saving time and resources along the way.

## Managing keywords and auto responses

SMS with Braze gives you the option to create keyword triggers, custom responses, define keyword sets for multiple languages, and establish custom keyword categories. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Add keyword triggers

In addition to the default opt-in and opt-out keywords, you may also define your own keywords to trigger Opt-In, Opt-Out, and Help responses.

![Editing keywords for "Opt-In" category. Added keywords are "START", "UNSTOP", and "YES". The reply message field reads "You have been unsubscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe. Message and data rates may apply."]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. To define your own keywords, navigate to the SMS section of the dashboard located under Subscription Groups.<br><br>
2. Under SMS global keywords, select a keyword category to add a keyword to by selecting the pencil icon.<br><br>
3. In the dialogue box that pops up, add a keyword you would like to trigger this keyword category. Note that keywords are case sensitive, and universal keywords like `START`, `YES`, and `UNSTOP` cannot be changed. 

![]({% image_buster /assets/img/sms/sms_keywords.png %})

The following rules apply to keywords and keyword responses:

| Keywords | Keyword responses |
| -------- | ----------------- |
| - Valid UTF-8 encoded characters<br>- Maximum of 20 keywords per category total<br>- Maximum length of 34 characters<br>- Minimum length of 1 character <br>- Cannot contain spaces<br>- Required to be case insensitive and unique across the subscription group | - Cannot be blank<br>- Maximum length of 300 characters<br>- Valid UTF-8 characters |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Interested in seeing how these keywords can be used in your campaigns and Canvases to retarget and trigger messages? Visit our [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) article for more information.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Manage responses

You are able to manage your own responses that get sent to users after they text in a keyword to a specific keyword category.

![Home]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. To manage your keyword responses, navigate to the SMS section of the dashboard located under Subscription Groups. <br><br>
2. Under SMS Global Keywords, select a keyword category to edit a response for by selecting the pencil icon.<br><br> 
3. In the dialogue box that pops up, edit and save your response. Be mindful of the [Six rules to get compliance right]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) as you create your response and read the following rules that apply to keywords and keyword responses.<br><br>

![Responses]({% image_buster /assets/img/sms/keyword_home.png %})

| Keywords | Keyword responses |
| -------- | ----------------- |
| - Valid UTF-8 encoded characters<br>- Maximum of 20 keywords per category total<br>- Maximum length of 34 characters<br>- Minimum length of 1 character <br>- Cannot contain spaces<br>- Required to be case insensitive and unique across the subscription group | - Cannot be blank<br>- Maximum length of 300 characters<br>- Valid UTF-8 characters |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Multi-language support

When sending to certain countries, a sender may be required to support inbound keywords and outbound replies with a local language. To support this, Braze allows you to create a language-specific keyword setting. 
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

To get started, click **Add a Language** and select your target language or search for a language within the dropdown.

{% alert important %}
Note that other languages do not come with preset keywords and responses like English, so senders will need to work with their marketing and legal teams to add any required keywords to this set. Otherwise, Braze will not handle localized incoming messages for those languages. 
{% endalert %}

If you need to delete a language, click the **Delete Language** button at the bottom right.

![SMS Global Keywords page with the "French" tab selected. Additional tabs exist for each added language.][5]

## Custom keyword categories

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you are also able to create up to 25 of your own keyword categories. This allows you to identify arbitrary keywords and set up responses specific to your business. An example category might be "PROMO" or "DISCOUNT", which might prompt a response about promos that are happening this month. 

These custom keywords operate in an "always-on" capacity, meaning that any user subscribed to your message service can text keywords and receive a response at any point. In addition to this behavior, you also have the option to define specific keywords that can only be sent to at [certain points]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) of your user's lifecycle. 

![Keywords for a "Promotions" category. If a user texts "DEALS", "PROMOS", or "PROMOTIONS", they receive the message "Check out our specialized promos just for you at example.com/promos".][12]

### Create a custom category

![][13]{: style="float:right;max-width:40%;margin-left:10px;"}

To create a custom keyword category, edit the appropriate subscription group, and click **Add Custom Keyword Category**. Here, you will be able to provide a keyword category name and define which keywords a user can text in to receive the reply message.

Once created, this keyword category will be available to [filter and trigger]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) against in your campaigns and Canvases.

Keywords created in custom keyword categories adhere to all of the rules and validations for the creation of new keywords. 

### Lifecycle-specific keywords

If you have a use case where you would like to limit when a customer can send a specific keyword during their lifecycle (e.g., during their first initial onboarding) to receive a response, you can use the trigger "Sent inbound SMS to subscription group within keyword category OTHER" in your campaign or Canvas and define some ad-hoc keywords that your users can send in at a point in time.

This trigger supports filtering on the specific inbound message using is or is not comparisons of the message, as well as matches or does not match regex rules to validate the user's input.

#### Canvas

![Action-based Canvas step with the trigger Send inbound SMS to subscription group "Marketing Message Service A" within keyword category "Other" where the message body matches the regular expression "caret symbol skip."][14]{: style="max-width:80%;"}

#### Campaign

![Action-based campaign with the trigger Send inbound SMS to subscription group "Marketing Message Service A" within keyword category "Other" where the message body is "Keyword1" or is "Keyword2" or is not "Keyword A".][15]{: style="max-width:80%;"}

### Dealing with unknown keywords

While not required, we strongly recommend setting up an auto-response for when users send inbound SMS keywords that do not match an existing keyword. This message will notify the user that the keyword is not recognized and offer some guidance. 

This can be done by creating an SMS campaign with a message like "Sorry! We didn't recognize that keyword, text STOP to stop or HELP to help." Next, in the delivery step, select **Action-Based Delivery** and use the trigger **Sent inbound SMS to subscription group within keyword category OTHER**.

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Interested in seeing how these keywords and keyword categories can be used in your campaigns and Canvases to retarget and trigger messages? Visit our [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) article for more information.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
