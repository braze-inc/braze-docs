---
nav_title: Key-Value Pairs
page_order: 8
search_rank: 5
platform: Android
---

# Key-Value Pairs
`Card` objects may optionally carry key-value pairs as `extras`. These can be used to send data down along with a `Card` for further handling by the application.

Call the following on a `Card` object to retrieve its extras:

```java
Map<String, String> getExtras()
```

See the [Javadoc][36] for more information.

[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras()
