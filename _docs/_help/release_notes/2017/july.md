---
nav_title: July
page_order: 6
noindex: true
page_type: update
description: "This article contains release notes for July 2017."
---

# July 2017

## Large images in web push

We’ve added support for large images for Web Push on Chrome for Windows and Android, giving you the ability to create rich, engaging customer experiences. Learn more about web push [here][58].

## Updates to email fields

You can now lock emails to a specific set of from-addresses, ensuring that you don’t accidentally input the wrong address. The email composition form will be pre-populated with addresses used in the last 6 months to streamline the process. Learn more about email best practices [here][57].

## Updates to campaign details API

The /campaign/details API endpoint now gives information about its messages, allowing you to pull subject, HTML body, from-address, and reply-to fields using the API. Learn more about our APIs [here][56].

## Updates to Liquid templating

We’ve added the ability to template variant attributes in Canvases and campaigns. In Canvas, you can now template both the variant’s API id as well as the variant’s name, and in campaigns you can now template a message’s message_api_id and message_name. Both updates allow for more flexibility in your messaging, allowing you to build personalized campaigns. Learn more about personalized messaging [here][55].

## New HTML email editor

You can now easily write and test emails with a full-screen HTML editor that enables live preview, personalization via Liquid and an improved full-screen text editor with line numbers and syntax highlighting. Learn more about email composition [here][54].

## Updates to previews

You can now follow the screen window as you scroll down message previews in campaigns & Canvas, ensuring that you can always see the changes reflected. Learn more about previewing and testing [here][53].

## New segment membership filter

We added a new filter, Segment Membership, enabling you to target users based off their membership in any of your existing segments. In addition, we’ve added the ability to use of both “And” and “Or” logic in segment filters, as well as the ability to nest segments within each other. These updates enable you to send customized messages to your customers with more precision. Learn more about filters [here][52].

## Update to Android preview

We updated the Android preview to reflect more recent versions of Android since Android N.  Learn more about preview messages [here][51].


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/help/best_practices/web_sdk/#web-push
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
