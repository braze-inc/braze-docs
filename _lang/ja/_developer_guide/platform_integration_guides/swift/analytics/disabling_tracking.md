---
nav_title: iOS SDK トラッキングを無効にする
article_title: iOS の SDK トラッキングを無効にする
platform: Swift
page_order: 8
description: "この記事では、Swift SDK のデータ収集を無効にする方法を紹介します。"

---

# iOS SDK トラッキングを無効にする

> データプライバシー規制を遵守するため、Braze インスタンスの [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) プロパティを `false` に設定することで、iOS SDK のデータトラッキングアクティビティを完全に停止できます。 

`enabled` が `false` に設定されると、Braze SDK でパブリック API への呼び出しがすべて無視されます。SDKはまた、ネットワークリクエストやイベント処理など、飛行中のすべてのアクションをキャンセルする。データ収集を再開するには、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) を `true` に設定します。

また [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())メソッドを使用して、ユーザーのデバイスにローカルに保存されたSDKデータを完全に消去することもできる。Swift SDK バージョン 5.7.0 以前を使用している場合、または `useUUIDAsDeviceId` が `false` に設定されている場合、Vendors の ID (IDFV) がデバイス ID として使用されるため、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) への POST リクエストも必要になります。Braze Swift バージョン 7.0.0 以降では、代わりに SDK と `wipeData()` メソッドによってデバイス ID の UUID がランダムに生成されます。
