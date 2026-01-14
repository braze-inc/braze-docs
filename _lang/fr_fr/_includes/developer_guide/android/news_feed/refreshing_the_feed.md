# Actualiser un fil d'actualité

> Cet article de référence montre comment rafraîchir le fil d'actualité dans votre application Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Rafraîchir le flux

Vous pouvez à tout moment mettre en file d'attente une actualisation manuelle du fil d'actualité de Braze en appelant la méthode suivante. Pour une documentation de référence complète, voir [`requestFeedRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html).

```java
Braze.requestFeedRefresh()
```
