---
nav_title: Refreshing the Feed
article_title: Refreshing the Content Card Feed for Android/FireOS
page_order: 4
platform: 
  - Android
  - FireOS
description: "This reference article covers how to implement Content Card refreshing in your Android application."
channel:
  - content cards

---

# Refreshing content cards

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

For more information on this method, please see [our corresponding Javadocs](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#requestContentCardsRefresh-boolean-).
