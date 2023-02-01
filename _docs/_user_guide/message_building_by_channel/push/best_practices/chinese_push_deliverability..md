---
nav_title: Deliverability for Chinese Android Devices
article_title: Push deliverability for Chinese Android Devices
page_order: 10

page_type: reference
description: "This article covers push deliverability nuances you should be aware of when targeting users on Android devices manufactured by Chinese OEMs."
channel: push

---

# Push deliverability for Chinese Android devices

Some Android devices manufactured by Chinese Original Equipment Manufacturers (OEMs), such as Xiaomi, OPPO, and Vivo, optimize for longer battery lives. This optimization may have the unintended consequence of shutting down background app processing, which can reduce deliverability of your push notifications.  

After your users opt in to receive push notifications, there are additional steps they can take on their end to improve message delivery for these devices. We recommend you follow up your [push primer message]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) with an in-app message targeted to users on Chinese OEM devices with these additional steps:

- Enable “auto-start” for the app
- Disable battery optimization for the app

For more information on how to bring up the autostart permission manager of a phone, see `[add link to developer guide section]`.

To further amplify your message, add other channels to resurface information from unopened push notifications. For example, out-of-app channels like SMS, WhatsApp, and LINE and in-app channels like in-app messages and Content Cards. Your users will be able to see anything they might have missed the next time they open the app.
