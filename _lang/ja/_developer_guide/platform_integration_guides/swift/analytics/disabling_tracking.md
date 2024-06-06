---
nav_title: iOS SDK トラッキングを無効にする
article_title: iOS の SDK トラッキングを無効にする
platform: Swift
page_order: 8
description: "この記事では、Swift SDK のデータ収集を無効にする方法を紹介します。"

---

# iOS SDK トラッキングを無効にする

> データプライバシー規制を遵守するため、Braze インスタンスの [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) プロパティを `false` に設定することで、iOS SDK のデータトラッキングアクティビティを完全に停止できます。 

`false` に設定されると、Braze SDK でパブリック API の呼び出しがすべて無視されます。また、SDK で実行中のアクション (ネットワークリクエスト、イベント処理など) がすべてキャンセルされます。データ収集を再開する場合は、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) プロパティを `true` に設定できます。

さらに、メソッド [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) を使用して、デバイスにローカルで保存された SDK データを完全にクリアすることもできます。

特定のデバイスで、ベンダーのアプリをユーザーがすべてアンインストールしない限り、`wipeData()` を呼び出した後の Braze SDK の次回実行時に、サーバーでデバイス識別子によってそのユーザーが再識別されます。すべてのユーザーデータを完全に削除するには、`wipeData()` の呼び出しと、Braze [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) を介したサーバーのデータ削除リクエストを組み合わせる必要があります。
