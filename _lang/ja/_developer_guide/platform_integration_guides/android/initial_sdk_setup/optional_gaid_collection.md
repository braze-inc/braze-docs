---
nav_title: Google 広告 ID (オプション)
article_title: Android 用のオプションの Google 広告 ID
page_order: 9
platform: 
  - Android
description: "このリファレンス記事では、Google 広告 ID と、この広告情報を Android または FireOS アプリケーションの Braze に渡す方法について説明します。"

---

# Google 広告 ID (Android のみ)

> [Google 広告 ID](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) は、Google Play サービスによって提供される、ユーザー固有、匿名、一意、およびリセット可能なオプションの広告用 ID です。このリファレンス記事では、Google 広告 ID と、この広告情報を Android または FireOS アプリケーションの Braze に渡す方法について説明します。

GAID によりユーザーは、自分の識別子をリセットし、Google Play アプリ内の興味・関心に基づく広告をオプトアウトできます。また、開発者は、アプリの収益化を継続するためのシンプルな標準システムを入手できます。

## Google 広告 ID を Braze に渡す

Google 広告 ID は Braze SDK によって自動的に収集されないため、[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) メソッドを使用して手動で設定する必要があります。

{% alert important %}
Google では、非 UI スレッドで広告 ID を収集する必要があります。
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Thread(Runnable {
  try {
    val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext())
    Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.id, idInfo.isLimitAdTrackingEnabled)
  } catch (e: Exception) {
    e.printStackTrace()
  }
}).start()
```

{% endtab %}
{% endtabs %}


