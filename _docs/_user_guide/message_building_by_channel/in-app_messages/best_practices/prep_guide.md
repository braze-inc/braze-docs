---
nav_title: Prep guide
article_title: In-App Message Prep Guide
page_order: 0.5

page_type: reference
description: "This article covers questions and best practices to consider before building in-app messages, including targeting, scheduling, content, and conversions."
channel: in-app messages
toc_headers: h2
---

# In-app message prep guide

> Before you build your in-app messages, you should consider a few of the following topics so building your message is quick and easy.

## General considerations

- If you are building a campaign, how many variants of this message would you like to display? For variant testing ideas, check out [Tips for different channels]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- If you are building a Canvas, will this message be paired with other messaging channels in that step?
- When would you like [your message to expire]({{site.baseurl}}/canvas_in-app_messages/)?

## Targeting considerations

- In-app messages are best for users who regularly visit your app. Are you including this audience?
- Where do you want your users to see your message? In your Web app? In your mobile app?
- Which event should trigger this message?
- Are any of your users using older versions of your app? If so, they might not be able to see some elements of your message.
- What type of device or devices are you building this message for? Remember, you can preview your message using the **Preview** box or **Test** tab. Refer to [Testing]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) for more information.

## Scheduling, delays, and session starts

When an in-app message campaign has **Schedule Delay** with a trigger on session start, a user who starts a session and then closes the app before the in-app message displays can still get that message on the next session start, after the delay expires.

That timing can produce unexpected display behavior, especially if **Re-evaluate campaign eligibility before displaying** isn't selected on the campaign.

For example, a user might receive an in-app message with an eight-second delay a month after the campaign launched. That can happen if they started a session, immediately ended the session, started a session a month later, and then eight seconds later received the in-app message. If they navigate away from the app without closing it, the in-app message displays when they return to the app.

## Content considerations

- Which languages will you be using in this message?
- What is your header and body copy? Are they eye-catching and relevant to your user?
- In-app messages only appear for a set amount of time. Is your copy concise and memorable?
- Will you be using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) to add custom copy?
- For fullscreen in-app messages, is your image or other media within the [safe zone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- For survey in-app messages, do you want to log attributes or submissions? Have you set up your confirmation page?

## Conversion considerations

- What is your goal for this message? How can you represent that in your message?
- Do your buttons offer options that make sense to your user? What is your [primary call to action]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Are you [deep linking to other in-app content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)? Are you using this in-app message to send and accept a [permission or push priming request]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)?
- Do you have a message exit option? If not, you can always copy and paste this snippet to create a quick button:
    ```html
    <a href="appboy://close">X</a>
    ```

## Drag-and-drop editor considerations

### Adding deep links for different devices

The drag-and-drop editor doesn't support adding different deep links for different devices (unlike the traditional editor).

### Adjusting background image opacity 

The opacity setting doesn't allow complete transparency of background images (unlike the traditional IAM editor). You can use opacity settings to make the message background color completely transparent.

### Setting the maximum width 

The maximum width in the drag-and-drop editor is limited at 325px; this is primarily meant to accommodate the dashboard preview. Messages can display properly on smaller screen devices.

### Selecting different backgrounds for different platforms 

It's not possible to show two different backgrounds for the same message on different platforms (such as web and mobile).

### Applying message styles 

Background images apply to the full message and can't be customized per page. Message styles apply to the full message, not individual pages.

### Measuring Spacer blocks height

The measurement unit for Spacer blocks is pixels (px) and can't be changed.

### Supported formats

Currently, only modal and fullscreen in-app messages are supported in the drag-and-drop editor.

### Adjusting to size and aspect ratio

The background image will stretch the in-app message, as the modal adjusts to fit the size and aspect ratio of the background image; you can adjust the ratio as needed.

### Background images and on-click behavior

These persist across pages. For multi-page in-app messages with different full images on each page, add a button to allow users to click to the next page.


