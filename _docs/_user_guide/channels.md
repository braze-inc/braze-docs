---
nav_title: Channels
article_title: Channels
page_order: 5
layout: dev_guide
guide_top_header: "Channels"
guide_top_text: "Reach your users through the right channel at the right time. Choose from in-product channels like in-app messages, Content Cards, and banners, or out-of-product channels like push, email, SMS, and WhatsApp."

page_type: landing
description: "Reach your users through in-product and out-of-product messaging channels in Braze."

guide_featured_title: "In-product channels"
guide_featured_list:
  - name: In-app messages
    link: /docs/user_guide/channels/in_app_messages/
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards/
    image: /assets/img/braze_icons/sticker-square.svg
  - name: Banners
    link: /docs/user_guide/channels/banners/
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "Out-of-product channels"
guide_menu_list:
  - name: Email
    link: /docs/user_guide/channels/email/
    image: /assets/img/braze_icons/mail-01.svg
  - name: Transactional email
    link: /docs/user_guide/channels/transactional_email/
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: Landing pages
    link: /docs/user_guide/messaging/landing_pages/
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line/
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: Live notifications
    link: /docs/developer_guide/live_notifications/
    image: /assets/img/braze_icons/phone-02.svg
  - name: Push
    link: /docs/user_guide/channels/push/
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS, and RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs/
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhooks
    link: /docs/user_guide/channels/webhooks/
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp/
    image: /assets/img/braze_icons/whatsapp.svg
---

## Choosing a message channel

When determining what message channel is best for your campaigns and Canvases, always think about the content and urgency of your message:

- **Content** is how visually engaging your message is. You can add multimedia and other assets to your copy to make your content more rich.
- **Urgency** is a measure of how quickly a message is able to notify your user and attract their attention. Notifications the user can immediately view have a high urgency, whereas messages that need the user to log in to your app have a low urgency.

The Braze Messaging Matrix streamlines channel selection by mapping **Content Complexity** against **Delivery Urgency**. By balancing these two factors, you can help your message resonate rather than interrupt.

![Mobile/web push are simple content, high urgency; Emails are rich content, high urgency; In-app/browser messages are simple content, low urgency; Content Cards are low urgency, rich content]({% image_buster /assets/img_archive/messaging_matrix.png %})

While the matrix highlights core channels, it is adaptable: SMS and WhatsApp, for instance, are high-urgency tools that scale into rich content when utilizing multimedia formats. To learn more about how you can leverage this matrix, check out our Braze Learning course on [Cross-Channel Messaging](https://learning.braze.com/cross-channel-messaging).
