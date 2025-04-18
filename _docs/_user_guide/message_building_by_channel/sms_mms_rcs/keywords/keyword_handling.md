---
nav_title: Custom Keyword Handling
article_title: Custom Keyword Handling
page_order: 3
description: "This reference article covers how Braze deals with two-way SMS messaging and auto-responses. This includes explanations on how keyword triggering works as well as custom keyword categories and multi-language support."
page_type: reference
channel:
  - SMS

---

# Custom keyword handling

> This reference article covers how Braze deals with two-way SMS messaging and auto-responses. This includes explanations on how keyword triggering works as well as custom keyword categories and multi-language support.

## Two-way messaging (custom keyword responses)

Two-way messaging allows you to send messages and process the responses to those messages. It requires end-users to send a keyword to Braze, to which that user will receive an automatic reply. Applied correctly, two-way messaging can be a simple, immediate, and dynamic solution to customer marketing, saving time and resources along the way.

## Managing keywords and auto responses

SMS with Braze gives you the option to create keyword triggers, custom responses, define keyword sets for multiple languages, and establish custom keyword categories. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Add keyword triggers

In addition to the default opt-in and opt-out keywords, you may also define your own keywords to trigger Opt-In, Opt-Out, and Help responses.

To define your own keywords, do the following:

1. In the Braze dashboard, go to **Audience** > **Subscription Groups** and select your SMS subscription group.<br><br>
2. Under **SMS Global Keywords**, click the pencil icon next to the keyword category you want to add a keyword to. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. In the tab that opens, add a keyword you want to trigger this keyword category. Note that keywords are case insensitive, and universal keywords like `START`, `YES`, and `UNSTOP` cannot be changed. ![Editing keywords for "Opt-In" category. Added keywords are "START", "UNSTOP", and "YES". The reply message field reads "You have been unsubscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe. Message and data rates may apply."]({% image_buster /assets/img/sms/keyword_edit2.png %})

The following rules apply to keywords and keyword responses:

| Keywords | Keyword responses |
| -------- | ----------------- |
| - Valid UTF-8 encoded characters<br>- Maximum of 20 keywords per category total<br>- Maximum length of 34 characters<br>- Minimum length of 1 character <br>- Cannot contain spaces<br>- Required to be case insensitive and unique across the subscription group | - Cannot be blank<br>- Maximum length of 300 characters<br>- Valid UTF-8 characters |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Interested in seeing how these keywords can be used in your campaigns and Canvases to retarget and trigger messages? Visit our [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) article for more information.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Manage responses

You can manage your own responses that are sent to users after they text in a keyword to a specific keyword category.

1. In the Braze dashboard, go to **Audience** > **Subscription Groups** and select your SMS subscription group. <br><br>
2. Under **SMS Global Keywords**, select a keyword category to edit a response for by selecting the pencil icon. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. In the tab that opens, edit your response. Be mindful of our [six rules to get compliance right]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) as you create your response, and read the following rules that apply to keywords and keyword responses. ![Responses]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. To automatically shorten static URLs in your response, select the **Link Shortening** toggle. The character counter will update to show the expected length of the shortened URL. ![A GIF showing the character counter updating when the "Link Shortening" toggle is on.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### Considerations

| Keywords | Keyword responses |
| -------- | ----------------- |
| - Valid UTF-8 encoded characters<br>- Maximum of 20 keywords per category total<br>- Maximum length of 34 characters<br>- Minimum length of 1 character <br>- Cannot contain spaces<br>- Required to be case insensitive and unique across the subscription group | - Cannot be blank<br>- Maximum length of 300 characters<br>- Valid UTF-8 characters |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %} 
If an action-based Canvas is triggered by an inbound SMS message, you can reference SMS properties in the first [message step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) of the Canvas.
{% endalert %}

## Multi-language support

When sending to certain countries, a sender may be required to support inbound keywords and outbound replies with a local language. To support this, Braze allows you to create a language-specific keyword setting. 
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### Creating language-specific keywords

Click **Add a Language** and select your target language or search for a language within the dropdown.

{% alert important %}
Note that other languages do not come with preset keywords and responses like English, so senders will need to work with their marketing and legal teams to add any required keywords to this set. Otherwise, Braze will not handle localized incoming messages for those languages. 
{% endalert %}

If you need to delete a language, click the **Delete Language** button at the bottom right.

![SMS Global Keywords page with the "French" tab selected. Additional tabs exist for each added language.][5]

## Custom keyword categories

In addition to the three default keyword categories (Opt-in, Opt-out, and Help), you can also create up to 25 of your own keyword categories. This allows you to identify arbitrary keywords and set up responses specific to your business. An example category might be "PROMO" or "DISCOUNT", which might prompt a response about promos that are happening this month. 

These custom keywords operate in an "always-on" capacity, meaning that any user subscribed to your message service can text keywords and receive a response at any point. In addition to this behavior, you also have the option to define specific keywords that can only be sent to at [certain points]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) of your user's lifecycle. 

![Keywords for a "Doubleoptin" category. If a user texts "Y", they receive the message "Thank you for confirming your enrollment in Hair Cuttery SMS."][12]

### Creating a custom category

To create a custom keyword category, do the following:

1. Edit the appropriate subscription group.
2. Click **Add custom keyword**. ![][13]{: style="max-width:90%;"}
3. Provide a keyword category name and define which keywords a user can text in to receive the reply message.

After this keyword category is created, it will be available to [filter and trigger]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) against in your campaigns and Canvases.

Keywords created in custom keyword categories adhere to all of the rules and validations for the creation of new keywords. 

### Lifecycle-specific keywords

If you have a use case where you would like to limit when a customer can send a specific keyword during their lifecycle (for example, during their first initial onboarding) to receive a response, you can use the trigger **Sent inbound SMS to subscription group within keyword category OTHER** in your campaign or Canvas and define keywords that your users can send in at a point in time.

This trigger supports filtering on the specific inbound message using is or is not comparisons of the message, as well as matches or does not match regex rules to validate the user's input.

#### Canvas

![Action-based Canvas step with the trigger Send inbound SMS to subscription group "Messaging Service" within keyword category "Other" where the message body matches the regular expression "caret symbol skip."][14]{: style="max-width:90%;"}

#### Campaign

![Action-based campaign with the trigger Send inbound SMS to subscription group "Marketing Message Service A" within keyword category "Other" where the message body is "Keyword1" or is "Keyword2" or is not "Keyword A".][15]{: style="max-width:90%;"}

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
