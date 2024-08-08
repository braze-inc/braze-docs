---
nav_title: Swift Package Manager
article_title: iOS 向け Swift Package Manager の統合
platform: Swift
page_order: 1
description: "このチュートリアルでは、Swift Package Manager for iOSを使用したBraze Swift SDKのインストールについて説明します。"

---

# Swift Package Manager の統合

> [Swift Package Manager][1] (SPM) 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[バージョン情報を][2]確認し、お使いの環境がBrazeでサポートされていることを確認してください。

## 依存関係をプロジェクトに追加する

### SDK バージョンのインポート

プロジェクトを開き、プロジェクトの設定に移動します。[**Swift パッケージ**] タブを選択し、パッケージリストの下にある <i class="fas fa-plus"></i>[追加] ボタンをクリックします。

![][3]

{% alert note %}
バージョン7.4.0から、Braze Swift SDKには、[静的XCFrameworksと](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) [動的XCFrameworksという](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)追加の配布チャネルがあります。これらのフォーマットのいずれかを代わりに使いたい場合は、それぞれのリポジトリからインストール手順に従ってください。
{% endalert %}

テキストフィールドにiOS Swift SDKリポジトリ`https://github.com/braze-inc/braze-swift-sdk` のURLを入力してください。**Dependency Rule**セクションで、SDKバージョンを選択します。最後に、**Add Packageを**クリックします。

![][4]

### パッケージの選択

Braze Swift SDKは、開発者がプロジェクトにインポートする機能をよりコントロールできるように、機能をスタンドアロンライブラリに分離しています。

| パッケージ｜詳細
| ------- | ------- |
|`BrazeKit` | アナリティクスとプッシュ通知をサポートするメインSDKライブラリ。|
|`BrazeLocation` | 位置情報解析とジオフェンス監視をサポートする位置情報ライブラリ。|
|`BrazeUI` ｜アプリ内メッセージとコンテンツカードのためのBraze提供のユーザーインターフェースライブラリ。|
{: .ws-td-nw-1}

#### 拡張ライブラリ

{% alert warning %}
[BrazeNotificationServiceと](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) [BrazePushStoryは](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)、追加機能を提供する拡張モジュールであり、メインのアプリケーションターゲットに直接追加すべきではありません。代わりに、リンク先のガイドに従って、それぞれのターゲット拡張機能に個別に統合してください。
{% endalert %}

| パッケージ｜詳細
| ------- | ------- |
|`BrazeNotificationService` | リッチなプッシュ通知をサポートする通知サービス拡張ライブラリ。|
|`BrazePushStory` | Push Storiesをサポートする通知コンテンツ拡張ライブラリ。|
{: .ws-td-nw-1}

 お客様のニーズに最も適したパッケージを選択し、**パッケージの追加**をクリックします。最低でも`BrazeKit` 。

![][5]

## 次のステップ

手順に従って[統合を完了します]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)。

[1]: https://swift.org/package-manager/
[2]: https://github.com/braze-inc/braze-swift-sdk#version-information
[3]: {% image_buster /assets/img/swiftpackages.png %}
[4]: {% image_buster /assets/img/importsdk_example.png %}
[5]: {% image_buster /assets/img/add_package.png %}
