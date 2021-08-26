---
nav_title: Badges
page_order: 4
platform: FireOS
description: "This article covers how to add badges to your Content Cards in your Android application."
channel:
  - content cards
hidden: true
---

# Adding a Badge

You can [request the number of unread cards][1] at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#getContentCardUnviewedCount--
