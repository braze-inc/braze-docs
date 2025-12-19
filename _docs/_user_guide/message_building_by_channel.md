---
nav_title: Message building by channel
article_title: Message Building by Channel
page_order: 5
layout: dev_guide

guide_top_header: "Message Building by Channel"
guide_top_text: "Messaging channels are ways you can virtually communicate with your customers through push notifications on their phone or web browser, email, in-app messages, and so much more! If you want to learn more about these channels and how to utilize them with Braze, check out the following sections listed. Or check out our Braze Learning courses on <a href='https://learning.braze.com/series/messaging-channels' target='_blank'>Messaging Channels</a>!<br><br>You can use Braze to create accessible messaging campaigns across each channel. Work with your engineers to ensure that you meet accessibility standards in your implementation."
description: "This landing page covers Braze messaging channels. Messaging channels are ways you can virtually communicate with your customers through push notifications on their phone or web browser, email, in-app messages, and so much more!"

guide_featured_title: "Available channels"
guide_featured_list:
- name: Banners
  link: /docs/user_guide/message_building_by_channel/banners/
  image: /assets/img/braze_icons/table.svg
- name: Content Cards
  link: /docs/user_guide/message_building_by_channel/content_cards/
  image: /assets/img/braze_icons/table.svg
- name: Email Messaging
  link: /docs/user_guide/message_building_by_channel/email/
  image: /assets/img/braze_icons/mail-01.svg
- name: "In-App Messaging"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/
  image: /assets/img/braze_icons/annotation-dots.svg
- name: Push Messaging
  link: /docs/user_guide/message_building_by_channel/push/
  image: /assets/img/braze_icons/marker-pin-01.svg
- name: SMS, MMS, and RCS
  link: /docs/user_guide/message_building_by_channel/sms_mms_rcs/
  image: /assets/img/braze_icons/message-text-circle-01.svg
- name: Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/
  image: /assets/img/braze_icons/brackets.svg
- name: WhatsApp
  link: /docs/user_guide/message_building_by_channel/whatsapp/
  image: /assets/img/braze_icons/whatsapp.svg
---

## Accessibility resources

You can use Braze to create accessible messaging campaigns across each channel. Work with your engineers to ensure that you meet accessibility standards in your implementation. If you’d like additional guidance, we recommend:

- [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations): Learn fundamental accessibility principles that apply to brand communications in this Braze Learning course.
- [Building Accessible Messages]({{site.baseurl}}/help/accessibility/): Learn how to add alt text and structure your content for assistive technologies directly within Braze.

{% multi_lang_include accessibility/feedback.md %}

## Choosing a message channel

When determining what message channel is best for your campaigns and Canvases, always think about the content and urgency of your message:

- **Content** is how visually engaging your message is. You can add multimedia and other assets to your copy to make your content more rich.
- **Urgency** is a measure of how quickly a message is able to notify your user and attract their attention. Notifications the user can immediately view have a high urgency, whereas messages that need the user to log in to your app have a low urgency.

The Braze Messaging Matrix streamlines channel selection by mapping **Content Complexity** against **Delivery Urgency**. By balancing these two factors, you can help your message resonate rather than interrupt.

![Mobile/web push are simple content, high urgency; Emails are rich content, high urgency; In-app/browser messages are simple content, low urgency; Content Cards are low urgency, rich content]({% image_buster /assets/img_archive/messaging_matrix.png %})

While the matrix highlights core channels, it is adaptable: SMS and WhatsApp, for instance, are high-urgency tools that scale into rich content when utilizing multimedia formats. To learn more about how you can leverage this matrix, check out our Braze Learning course on [Cross-Channel Messaging](https://learning.braze.com/cross-channel-messaging).

<br><br>
