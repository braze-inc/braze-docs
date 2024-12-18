---
nav_title: ランタイム構成
article_title: Android と FireOS のランタイム構成
platform: 
  - Android
  - FireOS
page_order: 4
description: "このリファレンス記事では、Android または FireOS アプリケーションのランタイム構成を設定する方法について説明します。"

---

# ランタイム構成

>[ランタイム構成は](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)、`braze.xml`の代わりにランタイム時にアプリを設定する際にオプションとなる方法です。このリファレンス記事では、ランタイム構成を設定する方法について説明します。

ランタイム構成と`braze.xml`構成の両方を使用することは可能です。ランタイムに設定された値は、`braze.xml`の同じ値よりも常に優先されます。Braze SDK がランタイム構成内のすべての値を見つけることができれば、`braze.xml`は不要となるため削除できます。 

## 使用例

構成では[ビルダーオブジェクトを](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)使用し、それがビルドされ[`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)に渡されます。以下の例では、利用可能なランタイム構成オプションのサブセットを使用しています。オプションの完全なリストについては、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) を参照してください。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

別の例については、[Hello Braze のサンプルアプリ](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)で確認することができます。

