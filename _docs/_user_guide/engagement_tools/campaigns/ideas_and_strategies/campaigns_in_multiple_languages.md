---
nav_title: Campaigns in Multiple Languages
article_title: Campaigns in Multiple Languages
page_order: 4
page_type: tutorial
description: "This how-to article will walk you through how to send messages in different languages within campaigns."
tool: Campaigns

---

# Campaigns in multiple languages

> This how-to article will go over how to send messages in different languages within campaigns.
> <br>
> <br>
> Being able to deliver messages in multiple languages allows users to interact and reach their customers in a truly personalized way. 

Braze allows you to send messages in different languages from our dashboard. When composing a campaign, our language templating feature enables you to easily create one message that appears in different languages depending on the user's phone settings.

Here's how you can set up a message in multiple languages:

## Step 1: Feature opt-in

When composing your campaign, click **Add Languages**.

![][1]{: style="max-width:60%;" }

## Step 2: Select languages {#select-language}

Select the languages that your message will be in. The selections offered in the dropdown menu will be all of the languages that your users currently have. Braze automatically tracks the language in users' device settings and includes this information in each user's profile. 

After you select your languages, the snippet textbox will alter to feature a template that you can copy and paste into the content of your message. This template uses [conditional logic][3] to handle multiple languages in a single campaign.

![][2]

## Step 3: Select fields

Select the fields that you want to appear in different languages. These fields will differ depending on the message channel:

- Email: Subject and body
- Android push: Message, Title, Summary Text, Sound, and Custom URL
- iOS push: Message, Sound, and Custom URL
- In-app message: Message
- Windows Universal push: Text 1, Text 2, Text 3, and Image Name

A warning will display if you have already entered content in any of the selected fields. You can choose to replace existing content with the templated text or insert the templated text after the existing text.

![][4]

## Step 4: Insert fields

Using the buttons at the bottom of the dialogue, choose how you wish to insert the templated text into the message composer, or copy and paste the template into the desired location.

## Step 5: Add language variations

After inserting your templated text into the desired fields, type in different variations for each language. For each field where there is templating, you should enter the variations after the bracketed segment of templating. The variation should correspond to the language code referenced in the brackets before it. For instance, in the message's body, this might look like:

{% raw %}

```liquid
{% if ${language} == 'en' %}
Hello!
{% elsif ${language} == 'fr' %}
Bonjour!
{% else %}
Hello!
{% endif %}
```

For the title of an Android push, this might look like:

```liquid
{% if ${language} == 'en' %}Hello!{% elsif ${language} == 'fr' %}Bonjour!{% else %}Hello!{% endif %}
```

The text you enter after `{% else %}` will display to users who:

- Have a language that was not selected in [Step 2](#select-language).
- Have a language that is not supported by Braze. Braze supports the languages represented by ISO 639-1 two-letter codes, as well as a few additional ones not included in that set. For a complete list, check out our [iOS Localization page][8].
- Have a device where the language is undetectable. (This is highly unlikely).

We recommend entering text here that you think your users are most likely to understand. To ensure smooth delivery, you should always enter content after `{% else %}`.

{% endraw %}

Anything entered outside of the template block will behave like normal content and display for all users.

![][6]

## Step 6: Preview message

Click the **Personalized Preview** button and enter a user's ID or email to see how the message would appear to that individual, depending on their language. You'll also be able to see how your entire message looks as a whole and decide whether to add languages to more fields than the ones you had previously chosen.

![][7]

## Step 7: Finish campaign

Complete the remaining steps for [creating your campaign][9].

[1]: {% image_buster /assets/img_archive/languages_1.png %}
[2]: {% image_buster /assets/img_archive/languages_2.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[4]: {% image_buster /assets/img_archive/languages_3.png %}
[6]: {% image_buster /assets/img_archive/languages_5.png %}
[7]: {% image_buster /assets/img_archive/languages_6.png %}
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/localization/
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/