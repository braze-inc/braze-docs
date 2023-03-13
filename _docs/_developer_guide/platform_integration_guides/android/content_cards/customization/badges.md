---
nav_title: Badges
article_title: Content Card Badges for Android and FireOS
page_order: 4.4
platform: 
  - Android
  - FireOS
description: "This article covers how to add badges to your Content Cards in your Android or FireOS application."
channel:
  - content cards

---

# Badges

## Requesting unread Content Card counts

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

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html
