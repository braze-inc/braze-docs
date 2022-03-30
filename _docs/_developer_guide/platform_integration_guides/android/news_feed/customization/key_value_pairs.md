---
nav_title: Key-Value Pairs
article_title: News Feed Key-Value Pairs for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article covers how to use News Feed key-value pairs  in your Android or FireOS application."
channel:
  - news feed

---

# Key-value pairs

`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down with a `Card` for further handling by the application.

Call the following on a `Card` object to retrieve its extras:

{% tabs %}
{% tab JAVA %}

```java
Map<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras: Map<String, String>
```

{% endtab %}
{% endtabs %}

Refer to our [KDoc][36] for more information.