## ネットワークオフラインモード

[ネットワークオフラインモードは](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean)、Braze SDK からの送信ネットワークリクエストを、ランタイム中の任意の時点で一時停止または再開するオプション機能です。オフライン状態でもイベントは失われません。このリファレンス記事では、このモードを統合する方法を取り上げます。

Braze SDK でネットワークオフラインモードを有効にするには、以下の例を参照してください。

{% tabs %}
{% tab JAVA %}

```java
Braze.setOutboundNetworkRequestsOffline(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.setOutboundNetworkRequestsOffline(true)
```

{% endtab %}
{% endtabs %}

