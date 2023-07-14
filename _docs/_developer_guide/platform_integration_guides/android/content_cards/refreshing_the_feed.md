---
nav_title: Refreshing the Feed
article_title: Refreshing the Content Card Feed for Android and FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "This reference article covers how to implement Content Card refreshing in your Android or FireOS application."
channel:
  - content cards

---

# Refreshing the Feed

> This reference article covers how to implement Content Card refreshing in your Android or FireOS application.

{% alert tip %}
To dynamically show up-to-date Content Cards without manually refreshing, select **At first impression** during card creation. These cards will be refreshed once they are available.
{% endalert %}

You can queue a manual refresh of Braze Content Cards at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

Refer to our [corresponding KDoc][1] for more information on this method.

{% alert important %}
The default rate limit for calling `requestContentCardsRefresh` is 3 calls per 10 minutes per device to prevent performance degradation and errors.
{% endalert %}

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html
