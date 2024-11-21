---
nav_title: Swift Package Manager
article_title: iOS 向け Swift Package Manager の統合
platform: Swift
page_order: 1
description: "このチュートリアルでは、iOS 用 Swift Package Manager を使用した Braze Swift SDK のインストールについて説明します。"

---

# Swift Package Manager の統合

> [Swift Package Manager](https://swift.org/package-manager/) (SPM) 経由で Swift SDK をインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[バージョン情報](https://github.com/braze-inc/braze-swift-sdk#version-information)を確認し、お使いの環境が Braze でサポートされていることを確認してください。

## 依存関係をプロジェクトに追加する

### SDK バージョンのインポート

プロジェクトを開き、プロジェクトの設定に移動します。[**Swift パッケージ**] タブを選択し、パッケージリストの下にある <i class="fas fa-plus"></i>[追加] ボタンをクリックします。

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
バージョン7.4.0から、Braze SWIFT SDKには、[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[ダイナミックなXCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

iOS Swift SDK リポジトリーのURL `https://github.com/braze-inc/braze-swift-sdk` をテキストフィールドに入力します。**依存関係ルール**セクションで、SDKバージョンを選択します。最後に、**パッケージを追加**をクリックします。

![]({% image_buster /assets/img/importsdk_example.png %})

### パッケージの選択

Braze Swift SDK は、開発者がどの機能をプロジェクトにインポートするかをより詳細に制御できるように、機能をスタンドアロンライブラリーに分離しています。

| パッケージ | 詳細 |
| ------- | ------- |
| `BrazeKit` | 分析とプッシュ通知をサポートする主な SDK ライブラリー |
| `BrazeLocation` | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。 |
| `BrazeUI` | アプリ内メッセージおよびコンテンツカード用のBraze提供のユーザーインターフェイスライブラリー。 |
{: .ws-td-nw-1}

#### 拡張ライブラリ

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) と [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) は追加機能を提供する拡張モジュールであり、メインアプリケーションターゲットに直接追加しないでください。代わりにリンクされたガイドに従って、それぞれをそれぞれのターゲット拡張機能に個別に統合してください。
{% endalert %}

| パッケージ | 詳細 |
| ------- | ------- |
| `BrazeNotificationService` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `BrazePushStory` | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリーを提供します。 |
{: .ws-td-nw-1}

 ご自身のニーズに最も適したパッケージを選択し、**パッケージを追加**をクリックしてください。必ず最低でも`BrazeKit`を選択してください。

![]({% image_buster /assets/img/add_package.png %})

## 次のステップ

手順に従って[統合を完了]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)してください。

