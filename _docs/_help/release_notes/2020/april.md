---
nav_title: April
page_order: 9
---
# April 2020

## Movable Ink Partnership

Movable Ink provides Braze customers the ability to use Intelligent Creative features like __Countdown Timers, Polls, and Scratch Offs in their Push, In-App Message and Content Card campaigns__. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

For more information on how to start integrating Movable Ink into your campaigns, check out our [documentation]({{ site.baseurl }}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/).

## Intelligent Timing

When scheduling a campaign, you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage.

Updates to this feature include:
- __Removal of Quiet Hours__ - the time in which Braze may not send messages
- __Addition of Sending Window__ - the time in which Braze may send messages
- __Addition of Preview Chart__ - you may now generate a chart to see how many users will receive messages based on Intelligent Timing for each hour of the day, as well as what portion of users have provided enough information to compute an optimal time.

Check out our [documentation]({{ site.baseurl }}/user_guide/intelligence/intelligent_timing/) for more information. 

## Facebook Audience Export

Braze provides the ability to manually export your users from the Braze Segments page. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

__Currently available for US-02 & US-04 clusters (more clusters coming soon)__, a new Braze Facebook Audience Export process exists, streamlining the process with simple integration steps. You will no longer need to whitelist OAuth Redirect URI's to send custom audiences or mess around within Facebook App Settings to integrate. 

{% alert important %}
__Please note that all clients currently using Facebook Custom Audiences, MUST reintegrate their Braze Segments with these new steps once it becomes available to them.__
{% endalert%}

For access to the new simplified Facebook Audience Export steps, check out our documentation [here]({{ site.baseurl }}/hidden/private_betas/facebook_setup/).

## Content Block and Email Template API Updates

The [template/email/list]({{ site.baseurl }}/api/endpoints/templates/email_templates/get_list_email_templates/) and [content_block/list]({{ site.baseurl }}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API endpoints have been updated to include a new `tags` field. This field will list as an array, any tags that apply to the current block or email template.
