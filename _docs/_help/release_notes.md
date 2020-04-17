---
page_order: 2
nav_title: Release Notes
layout: featured
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>, listed below. You can also
check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."

guide_featured_title: "Release Notes"
guide_featured_list:
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code


---

# Most Recent Braze Release Notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## April 2020

### Movable Ink Partnership

Movable Ink provides Braze customers the ability to use Intelligent Creative features like __Countdown Timers, Polls, and Scratch Offs in their Push, In-App Message and Content Card campaigns__. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

For more information on how to start integrating Movable Ink into your campaigns, check out our [documentation]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/).

### Intelligent Timing

When scheduling a campaign, you can use Intelligent Timing (previously Intelligent Delivery) to deliver your message to each user at the time which Braze determines that an individual is most likely to engage.

Updates to this feature include:
- __Clarification of Quiet Hours__ - Quiet Hours functionality remains the same, but the UI has been adjusted for clar
- __Addition of Preview Chart__ - you may now generate a chart to see how many users will receive messages for each hour of the day with Intelligent Timing, as well as what proportion of users have enough data to compute an optimal time.
- __Addition of Custom Fallback__ - you may now choose the local time at which to send users a message when they lack sufficient engagement data to compute an optimal time

Check out our [documentation]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) for more information. 

### Facebook Audience Export

Braze provides the ability to manually export your users from the Braze Segments page to create Facebook Custom Audiences. This is a one-time, static audience export and will only create new Facebook Custom Audiences.

__Currently available for all Clusters__, a new Braze Facebook Audience Export process exists, streamlining the process with simple integration steps. You will no longer need to whitelist OAuth Redirect URI's to send custom audiences or mess around within Facebook App Settings to integrate. 

{% alert important %}
__Please note that all clients currently using Facebook Custom Audiences, MUST reintegrate their Braze Segments with these new steps.__
{% endalert%}

For access to the new simplified Facebook Audience Export steps, check out our documentation [here]({{site.baseurl}}/partners/facebook/).

### Content Block and Email Template API Updates

The [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) and [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API endpoints have been updated to include a new `tags` field. This field will list as an array, any tags that apply to the current block or email template.

## March 2020

### Custom Attribute Filter Behavior

The Dashboard has improved filters to include more intuitive behaviors.
There have been two significant changes to how certain custom attributes filters work. 
The custom attribute filter changes are reflected in the filters: 
- Less than __X__ Days Ago
- Less than __X__ Days in the Future
- Day of Recurring Event<br>

__If you use these filters in your segmentation, we recommend readjusting your segments to take these changes into account.__ 

Check out our [documentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#dates) for an explanation of the new behaviors.

## February 2020

### Retention Reports

Braze is proud to now offer Retention Reports for Campaigns. This feature helps measure user retention for users who have received any message in a specific campaign. Retention Reports can be found conveniently on the Campaign Analytics page within the Dashboard. 

Information on this new feature can be found in our [documentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/)

![Full Report][4]

{% alert important %}
As of February 13th, 2020 this feature is not yet available to our client deployed in our EU region or our HIPPA-compliant cluster. We will make this report available to those regions as we continue to deploy functionality across our entire platform.
{% endalert %}

### New Email Content Block API Endpoint

You can now [update]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_email_content_block/) your Email Content Blocks via API!

## January 2020

### Added SMS Capability

Braze now allows you to [cap the frequency]({{ site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/) of SMS messages as well as implement an added [segment filter]({{ site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) "Last Received SMS".

In the SMS channel, the New User settings and behavior have been outlined and can be checked out [here]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/).


[support]: {{site.baseurl}}/support_contact/
[4]: {% image_buster /assets/img/retention_report_full_report.png %}

