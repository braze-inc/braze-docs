---
nav_title: April
page_order: 9
no_index: true
page_type: update
description: "This article contains release notes for April 2020."
---
# April 2020

## Movable Ink Partnership

Movable Ink provides Braze customers the ability to use Intelligent Creative features like __Countdown Timers, Polls, and Scratch Offs in their Push, In-App Message and Content Card campaigns__. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

For more information on how to start integrating Movable Ink into your campaigns, check out our [documentation]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/).

## Intelligent Timing

When scheduling a campaign, you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage.

Updates to this feature include:
- __Clarification of Quiet Hours__ - Quiet Hours functionality remains the same, but the UI has been adjusted for clarification.
- __Addition of Preview Chart__ - you may now generate a chart to see how many users will receive messages for each hour of the day with Intelligent Timing, as well as what proportion of users have enough data to compute an optimal time.
- __Addition of Custom Fallback__ - you may now choose the local time at which to send users a message when they lack sufficient engagement data to compute an optimal time

Check out our [documentation]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) for more information.

## Facebook Audience Export

Braze provides the ability to manually export your users from the Braze Segments page to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

__Currently available for all Clusters__, a new Braze Facebook Audience Export process exists, streamlining the process with simple integration steps. You will no longer need to whitelist OAuth Redirect URI's to send custom audiences or mess around within Facebook App Settings to integrate.

{% alert important %}
__Please note that all clients currently using Facebook Custom Audiences, MUST reintegrate their Braze Segments with these new steps.__
{% endalert%}

For access to the new simplified Facebook Audience Export steps, check out our documentation [here]({{site.baseurl}}/partners/facebook/).

## Content Block and Email Template API Updates

The [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) and [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API endpoints have been updated to include a new `tags` field. This field will list as an array, any tags that apply to the current block or email template.

## Personalized From-Address

When creating an email message within Braze, you can now personalize the From Address of the message in the "Sending Info" section of email composition. You can use any of [our supported personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

![Personalized From Address][0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
