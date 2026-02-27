---
nav_title: Push setup
article_title: Push setup
page_order: 1
layout: dev_guide
guide_top_header: "Push setup"
guide_top_text: "Understand push token lifecycle and subscription states to ensure your push notifications reach the right users."

page_type: landing
description: "Learn about push token lifecycle and subscription states for push notifications in Braze."

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Push token lifecycle
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Push subscription states
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states/
    image: /assets/img/braze_icons/users-01.svg
---

## Prerequisites

Before you can create and send any push messages using Braze, you need to work with your developers to integrate push into your website or app. For detailed steps, refer to our integration guides for each platform:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)

## Push priming

Keep in mind that users need to opt-in to push to receive your messages, which means it's a good idea to use in-app messages to explain to your customers why you want to send them push notifications, and how enabling push will benefit them. This process is called [push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/).
