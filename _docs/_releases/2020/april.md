---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "This article contains release notes for April 2020."
---
# April 2020

## Movable Ink partnership

Movable Ink provides Braze customers the ability to use Intelligent Creative features like countdown timers, polls, and scratch offs in their push, in-app message and Content Card campaigns. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

Start [integrating Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) into your campaigns!

## Intelligent Timing

When scheduling a campaign, you can use [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage.

Updates to this feature include:
- **Clarification of Quiet Hours**: Quiet Hours functionality remains the same, but the UI has been adjusted for clarification.
- **Addition of Preview Chart**: You may now generate a chart to see how many users will receive messages for each hour of the day with Intelligent Timing, as well as what proportion of users have enough data to compute an optimal time.
- **Addition of Custom Fallback**: You may now choose the local time at which to send users a message when they lack sufficient engagement data to compute an optimal time

## Facebook Audience export

Braze provides the ability to manually export your users from the Braze Segments page to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new [Facebook Custom Audiences]({{site.baseurl}}/partners/facebook/).

Currently available for all clusters, a new Braze Facebook Audience Export process exists, streamlining the process with simple integration steps. You will no longer need to whitelist OAuth Redirect URI's to send custom audiences or mess around within Facebook App Settings to integrate.

{% alert important %}
Note that all clients currently using Facebook Custom Audiences, must reintegrate their Braze Segments with these new steps.
{% endalert%}


## Content Block and email template API updates

The [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) and [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API endpoints have been updated to include a new `tags` field. This field will list as an array, any tags that apply to the current block or email template.

## Personalized from-address

When creating an email message within Braze, you can now personalize the From Address of the message in the **Sending Info** section of email composition. You can use any of our supported [personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

![Personalized From Address]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

