---
nav_title: Badges
page_order: 4
search_rank: 5
platform: Android
---
## Adding a Badge

You can request the number of unread cards at any time by calling:

{% tabs %}
{% tab JAVA %}

```java
Appboy.getInstance(context).getContentCardUnviewedCount()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Appboy.getInstance(context).contentCardUnviewedCount
```

{% endtab %}
{% endtabs %}
