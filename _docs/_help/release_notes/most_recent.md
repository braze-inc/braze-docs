---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]._

## January 2019

Welcome to a new year!

### Push Time to Live (TTL)

In your account, within __Manage App Group__, click the [Push TTL Settings]({{ site.baseurl }}/user_guide/administrative/app_settings/push_ttl_settings/) tab to manage the time duration for attempted resends in the event that a device is offline.

### Connected Content IP Whitelisting

Braze is pleased to announce that due to a number of infrastructure upgrades made by our internal teams, we can now offer IP whitelisting for Connected Content on all clusters. In the future, we plan to add additional IPs for the non-EU clusters.

### Canvas Delay

We have added the option for any Canvas step to be sent __immediately__.

![Canvas Delay][canvas_delay]

### Adjust (Technology Partner) REST Endpoint Field Update

With our updated integration with [Adjust]({{ site.baseurl }}/partners/adjust/), Braze customers will only need to add their rest endpoint from the Adjust partner spotlight page.

This will make it easier for customers wanting to pass attribution data into Braze.


## December 2018

### Content Blocks

[Content Blocks]({{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/content_blocks/) allow you to manage your reusable, cross-channel content in a single, centralized location. To access this feature please go into the __Content Blocks Library__ tab in the __Templates & Media__ section of your Braze account. With Content Blocks, you can:
 - Create a consistent look and feel to your Email campaigns using Content Blocks as Headers and Footers.
 - Distribute the same offer codes through different channels.
 - Create pre-defined assets that can be used to build messages with consistent information and assets.
 - Copy entire message bodies to other messages.

### Gmail Promotional Tool

Gmail has updated the mobile Promotions tab to allow marketers to send more information via annotations in a ‘card’, rather than just the subject line or pre-header information. Braze has built a tool to help you build the card from our product. [Learn how to use it here!]({{ site.baseurl }}/user_guide/message_building_by_channel/email/gmail_promotions_tab/)

## November 2018

### Canvas Entry Settings Wizard

The Canvas UI will be simplified to prevent missed tasks and resulting errors. Canvas configurations, specifically, will now be displayed in a wizard, similar to the design of the Campaigns wizard. See the [updated Canvas documentation here]({{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)!

Want more on this new feature? [Check out our LAB course on the Entry Wizard here](https://lab.braze.com/the-new-canvas-entry-step/264889/scorm/20z5ij5ublxbk)!


### In-App Message Web Modal CSS

The [Web Modal CSS editor]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message/#web-modal-css) has been updated and allows you more control over the look of your In-App Messages with our new [CSS Templates]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/in_app_message_color_templates/#css-template).



[support]: {{ site.baseurl }}/support_contact/
[canvas_delay]: {% image_buster /assets/img/canvas_delay_immediate.png %}
