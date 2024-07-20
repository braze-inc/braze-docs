---
nav_title: Push TTL Settings
article_title: Push TTL Settings
page_order: 16
page_type: reference
description: "This reference article covers the Push Time to Live settings page in the Braze dashboard."
channel: push

---

# Push TTL settings

> Learn about the Push Time-to-Live settings page in the Braze dashboard.

The **Push Time-To-Live (TTL)** page enables you to control the delivery attempt duration for offline devices. This means if a user's device is offline when your campaign sends, Braze will attempt to deliver the message up to your set time.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find this page at **Settings** > **Manage Settings** > **Push TTL Settings**.
{% endalert %}

This feature will not remove a notification if it has already been received by the user's device—it will only control how long the push provider will attempt to deliver a notification.

![Push Time to Live Settings tab under Manage Settings]({% image_buster /assets/img/push_ttl.png %})

{% alert tip %}
Remember to click **Save** before you leave the page!
{% endalert %}

