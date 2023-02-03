---
nav_title: Deliverability for Chinese Android Devices
article_title: Push deliverability for Chinese Android Devices
page_order: 10

page_type: reference
description: "This article covers push deliverability nuances you should be aware of when targeting users on Android devices manufactured by Chinese OEMs."
channel: push

---

# Push deliverability for Chinese Android devices

Some Android devices manufactured by Chinese Original Equipment Manufacturers (OEMs), such as Xiaomi, OPPO, and Vivo, optimize for longer battery lives. This optimization may have the unintended consequence of shutting down background app processing, which can reduce deliverability of your push notifications. To make sure that your app's messaging performance works as expected on these devices, your Marketing and Engineering teams should collaborate and follow the steps outlined in this article.

## Steps for developers
The way that OEMs optimize for battery life is by adding "unrecognized apps" to a blocklist that prevents them from running in the background. As a developer, you'll need to configure your app so that the user can easily place it on the OEM's allowlist. 

This can be achieved by having your app automatically start on your end user's device, which gives your app permission to run in the background and listen for messages from Braze. Unfortunately, since this is an OEM-specific problem and not an Android problem, there is no documented API for bringing up the startup permission manager. Each OEM has their own version of a startup permission manager with different package names. 

To solve for this, integrate a library like [AutoStarter](https://github.com/judemanutd/AutoStarter) into your application. AutoStarter supports multiple manufacturers, giving you an easy way to call the startup permission manager on a wide array of devices. Once you have integrated AutoStarter, call `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` to bring up the startup permission manager on your end user's device. Couple this action with a prompt encouraging the end user to enable "auto-start" for your app. Your Marketing team will craft this message—see below!

## Steps for marketers
After your users opt in to receive push notifications, there are additional steps they can take on their end to improve message delivery for these devices. We recommend you follow up your [push primer message]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) with an in-app message targeted to users on Chinese OEM devices with these additional steps:

- Enable “auto-start” for the app
- Disable battery optimization for the app

To further amplify your message, add other channels to resurface information from unopened push notifications. For example, out-of-app channels like SMS, WhatsApp, and LINE and in-app channels like in-app messages and Content Cards. Your users will be able to see anything they might have missed the next time they open the app.