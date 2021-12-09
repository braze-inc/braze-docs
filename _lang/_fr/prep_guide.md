---
nav_title: Prep Guide
article_title: In-App Message Prep Guide
page_order: 0.5
page_type: reference
description: "This article covers some questions and best practices you should consider before building your in-app messages."
channel: in-app messages
---

# In-app message prep guide

Before you start building your in-app message, you should consider a few of the following topics so building your message is quick and easy.

## General considerations

- If you are building in campaigns, how many variants of this message would you like to display? For variant testing ideas, check out [Tips for different channels]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#tips-different-channels).
- If you are building in Canvas, will this message be paired with other messaging channels in that step?
- When would you like [your message to expire]({{site.baseurl}}/canvas_in-app_messages/)?

## Targeting considerations

- In-app messages are best for users who regularly visit your app—are you including this audience?
- Where do you want your users to meet your message? In your Web app? In your mobile app?
- Which event triggers this message?
- Are any of your users using older versions of your app? If so, they might not be able to see some elements of your message. Learn more about [generations]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/generations/).
- What type of device or devices are you building this message for? Remember, you can preview your message using the **Preview** box or **Test** tab. Refer to [Testing]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) for more information.

## Content considerations

- Which languages will you be using in this message?
- What is your Header and Body copy? Are they eye-catching and relevant to your user?
- In-app messages only appear for a set amount of time. Is your copy concise and memorable?
- Will you be using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) to build more custom copy?
- For full-screen in-app messages, is your image or other media within the [safe zone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

## Conversion considerations

- What is your goal for this message? How can you represent that in your message?
- Do your buttons offer options that make sense to your user? What is your [primary call to action]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Are you [deep-linking to other in-app content][1]? Are you using this in-app message to send and accept a [permission or push priming request][21]?
- Do you have a message exit option? If not, you can always copy and paste this snippet to create a quick button:
    ```html
    <a href="appboy://close">X</a>
    ```


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[21]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
