---
nav_title: Push TTL Settings
page_order: 4
---

# Push Time to Live Settings

This tab, in the `Manage Settings` section of your account, enables you to control the delivery attempt duration for offline devices. That is to say, if a user's device is offline when your campaign sends, Braze will attempt to deliver the message up to your set time on this page.

Please note that this feature will not remove a notification if it has already been received by the user's device - it will only control how long the push provider will attempt to deliver a notification.

![Time to Live][1]

{% alert tip %}
Remember to save before you leave the page!
{% endalert %}

[1]: {% image_buster /assets/img/push_ttl.png %}
