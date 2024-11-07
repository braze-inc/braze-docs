---
nav_title: SDK トラッキングの無効化
article_title: Android と FireOS のデータ収集を無効にする
platform: 
  - Android
  - FireOS
page_order: 8
description: "この記事では、Android または FireOS アプリケーションのデータ収集を無効にする方法を説明します。"

---

# SDK トラッキングの無効化

> この記事では、Android または FireOS アプリケーションのデータ収集を無効にする方法を説明します。

データプライバシー規制に準拠するために、Android SDK のデータ追跡アクティビティはメソッド[`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html)で完全に停止できます。このメソッドでは、すべてのネットワーク接続がキャンセルされ、Braze SDK は Braze サーバーにデータを渡しません。後の時点でデータ収集を再開するには、[`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html)メソッドを使用します。

さらに、メソッド[`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html)を使用して、デバイスに保存されているすべてのクライアント側データを完全に消去できます。

