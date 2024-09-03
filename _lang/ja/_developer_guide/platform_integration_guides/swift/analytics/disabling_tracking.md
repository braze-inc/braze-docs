---
nav_title: iOS SDK トラッキングを無効にする
article_title: iOS の SDK トラッキングを無効にする
platform: Swift
page_order: 8
description: "この記事では、Swift SDK のデータ収集を無効にする方法を紹介します。"

---

# iOS SDK トラッキングを無効にする

> データプライバシー規制を遵守するため、iOS SDKのデータ追跡アクティビティは、Brazeインスタンスの [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled)プロパティを`false` 。 

`enabled` が`false` に設定されている場合、Braze SDK はパブリック API への呼び出しをすべて無視する。SDKはまた、ネットワークリクエストやイベント処理など、飛行中のすべてのアクションをキャンセルする。データ収集を再開するには [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)を`true` に設定する。

また [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())メソッドを使用して、ユーザーのデバイスにローカルに保存されたSDKデータを完全に消去することもできる。Swift SDKバージョン5.7.0以前を使用しているか、`useUUIDAsDeviceId` が`false` に設定されている場合、あなたのベンダー用識別子（IDFV）が彼らのデバイスIDとして使用されるため、あなたはまた、 にポストリクエストを行う必要がある。 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)あなたのIdentifier for Vendors (IDFV)がデバイスIDとして使用されるからだ。Braze Swiftのバージョン7.0.0以降では、SDKと`wipeData()` メソッドが、デバイスIDの代わりにUUIDをランダムに生成する。
