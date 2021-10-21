---
nav_title: Badges
article_title: Content Card Badges for Android/FireOS
page_order: 5
platform: 
  - Android
  - FireOS
description: "This article covers how to add badges to your Content Cards in your Android application."
channel:
  - content cards

---

# Adding a badge

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
