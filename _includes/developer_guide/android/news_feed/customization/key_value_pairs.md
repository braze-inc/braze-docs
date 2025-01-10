# Key-value pairs

> This reference article covers how to use News Feed key-value pairs in your Android or FireOS application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

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
