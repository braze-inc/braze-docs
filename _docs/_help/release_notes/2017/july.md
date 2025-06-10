---
nav_title: July
page_order: 6
noindex: true
page_type: update
description: "This article contains release notes for July 2017."
---

# July 2017

## Large images in web push

We've added support for large images for Web Push on Chrome for Windows and Android, giving you the ability to create rich, engaging customer experiences. Learn more about [web push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web).

## Updates to email fields

You can now lock emails to a specific set of from-addresses, ensuring that you don't accidentally input the wrong address. The email composition form will be pre-populated with addresses used in the last 6 months to streamline the process. Check out [Email best practices]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) for more information.

## Updates to campaign details API

The `/campaign/details` endpoint now gives information about its messages, allowing you to pull subject, HTML body, from-address, and reply-to fields using the API. Learn more about [Braze APIs]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Updates to Liquid templating

We've added the ability to template variant attributes in Canvases and campaigns. In Canvas, you can now template both the variant's API id as well as the variant's name, and in campaigns you can now template a message's `message_api_id` and `message_name`. Both updates allow for more flexibility in your messaging, allowing you to build personalized campaigns. Learn more about [personalized messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## New HTML email editor

You can now easily write and test emails with a fullscreen HTML editor that enables live preview, personalization via Liquid and an improved fullscreen text editor with line numbers and syntax highlighting. Learn more about [email composition]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template).

## Updates to previews

You can now follow the screen window as you scroll down message previews in campaigns and Canvases, ensuring that you can always see the changes reflected. Learn more about [previewing and testing]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message).

## New segment membership filter

We added the [Segment Membership filter]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters), enabling you to target users based off their membership in any of your existing segments. In addition, we've added the ability to use of both "And" and "Or" logic in segment filters, as well as the ability to nest segments within each other. These updates enable you to send customized messages to your customers with more precision. 

## Update to Android preview

We updated the [Android preview]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message) to reflect more recent versions of Android since Android N.


