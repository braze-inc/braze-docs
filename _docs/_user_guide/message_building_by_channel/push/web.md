---
nav_title: "Web push"
article_title: Web Push Notifications
page_order: 8.5
page_type: reference
description: "This reference page briefly covers web push notifications, and links out to the necessary steps to create one."
platform: Web
channel:
  - push

---

# Web push

> Learn about web push notifications at Braze and find resources for creating your own.

Web push is another great way to engage with users of your web application. Customers visiting your website from [supported browsers](#supported-browsers) can opt-in to receive web push from your web application whether or not the web page is loaded.

## Overview

Web push notifications deliver urgent, actionable updates that drive quick conversions. With web push, you can:

- Trigger messages right when important data changes, like a price decreases
- Drive people back to your website with simple call-to-action buttons
- Personalize your push with product and customer information to make your message relevant

Web push works the same way app push notifications operate on your phone. For more information on composing a web push, check out [Creating a push notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).

![Web push example with the same push message displayed on a laptop and phone.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## Potential use cases

Here are some examples of common web push message use cases.

| Use case | Description |
| --- | --- | 
| Free trial | Encourage new visitors on your website to sign up for free trials. By hooking users with the chance to experience what makes you special, you can make it more likely they become a paying customer. |
| App download | Draw web users to your mobile app to help them get even more value out of your products. Consider leveraging personalization to highlight app benefits based on their current engagement patterns. |
| Discounts and sales | Increase customer awareness of time-sensitive events and promotions. Message across multiple channels, including web push, to increase awareness of your brand's promotions. |
| Cart abandonment | Send automated reminders to users who haven't finished their transactions to bring them back to the checkout flow. <br><br>Research conducted by Braze found that web push is 53% more effective than email and 23% more impactful than mobile push at getting recipients to come back and complete a purchase. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prerequisites to use web push

Before you can create and send any push messages using Braze, you need to work with your developers to integrate push into your website. For detailed steps, refer to our [Web push integration guide]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

### Push permission

Any brand can integrate and use web push notifications on their website. The notifications can reach both current and previous web visitors as long as they have a web browser open, but visitors must [opt in to receive notifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-permission)—just like with traditional mobile app push.

{% alert tip %}
Consider using an in-browser message to prime users to opt in for web push, also known as a [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Supported browsers

The following browsers support web push notifications. However, private browsing windows do not currently support web push.

- Chrome (and Chrome for Android mobile)
- Safari
- Firefox (and Firefox for Android mobile)
- Opera
- Edge

For more information on the push protocol standards and browser support, you can review resources based on your browser:

- [Safari (desktop)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari (mobile)]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)


