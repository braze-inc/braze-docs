---
nav_title: Testing banners
article_title: Testing Banners
page_order: 2
description: "Learn how to test your Banner message before launching your campaign so you can ensure all media, copy, personalization, and custom attributes render correctly."
channel:
  - banners
noindex: true
---

# Testing Banners

> Learn how to test your Banner message before launching your campaign so you can ensure all media, copy, personalization, and custom attributes render correctly. For more general information, see [About Banners]({{site.baseurl}}/developer_guide/banners).

## Prerequisites

Before you can test Banner messages in Braze, you'll need to create a [Banner campaign in Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/). Additionally, verify that the placement you want to test is already [placed in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements). 

To send a test to either [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) or individual users, push must be enabled on your test devices with valid push tokens registered for the test user before sending.

## Testing a Banner

{% multi_lang_include banners/testing.md page="testing" %}
