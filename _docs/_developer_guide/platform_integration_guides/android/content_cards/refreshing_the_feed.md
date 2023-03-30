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

You can queue a manual refresh of Braze Content Cards at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestContentCardsRefresh(false);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh(false)
```

{% endtab %}
{% endtabs %}

Refer to our [corresponding KDoc][1] for more information on this method.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html
