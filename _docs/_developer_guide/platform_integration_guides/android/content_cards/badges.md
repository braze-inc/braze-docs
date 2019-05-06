---
nav_title: Badges
page_order: 4
search_rank: 5
platform: Android
---
## Adding a Badge

You can [request the number of unread cards](1) at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(context).getContentCardUnviewedCount();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#getContentCardUnviewedCount--
