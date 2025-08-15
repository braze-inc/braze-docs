---
nav_title: Reducing push notification payload size
article_title: Reducing Push Notification Payload Size
page_type: solution
description: "This help article provides some tips to reduce the payload size of your push notifications if you're unable to launch a campaign or Canvas step due to push payload size limits."
channel: push
---

# Reducing push notification payload size

If you can't launch a push campaign or Canvas step because your push payload is too large, check out these tips for reducing your push notification payload size.

{% alert note %}
Our maximum payload size is **3,807 bytes**. If your push exceeds this size, the message may not be sent. As a best practice, keep your payload to a few hundred bytes.
{% endalert %}

## What is a push payload?

Push service providers calculate whether your push notification can be displayed to a user by looking at the byte size of the entire push payload. The payload is limited to **4KB (4,096 bytes)** for most push services, including:

- Apple Push Notification service (APNs)
- Android’s Firebase Cloud Messaging (FCM)
- Web push
- Huawei push

These push services will refuse any notification that exceeds this limit.

Braze reserves a portion of the push payload for integration and analytics purposes. Given that, our maximum payload size is **3,807 bytes**. If your push exceeds this size, the message may not be sent. As a best practice, keep your payload to a few hundred bytes.

The following elements in your push make up your push payload:

- Copy, such as the title and message body
- Final render of any Liquid personalization
- URLs for images (but not the size of the image itself)
- URLs for click targets
- Button names
- Key-value pairs

## Tips to reduce payload size

To reduce payload size:

- Keep your message brief. A good general guideline is to make it actionable and beneficial in less than 40 characters.
- Omit whitespace and line breaks from your copy.
- Consider how Liquid will render on send. Because the final render of any Liquid personalization will vary from user to user, Braze can't determine if a push payload will exceed the size limit when Liquid is included. If your Liquid renders a shorter message, you might be fine. However, if your Liquid results in a longer message, your push may exceed the payload size limit. Always test your push message on a real device before sending it to users.
- Consider shortening URLs using a URL shortener.
