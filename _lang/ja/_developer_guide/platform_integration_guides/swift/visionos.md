---
nav_title: visionOSサポート
article_title: visionOSサポート
page_order: 7.2
platform: 
  - iOS
description: "この記事では、visionOSでサポートされている機能について説明する。"
---

# visionOSサポート

> [Braze Swift SDK 8.0.0から](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)、Apple Vision Pro用のAppleの空間コンピューティングプラットフォームである[visionOSで](https://developer.apple.com/visionos/)Brazeを活用できるようになった。Brazeを使用したvisionOSアプリのサンプルは、[サンプルアプリを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/)参照のこと。

## 完全にサポートされた機能

iOSで利用できるほとんどの機能は、visionOSでも利用できる：

- アナリティクス（セッション、カスタムイベント、購入など）
- アプリ内メッセージング（データモデルとUI）
- コンテンツ・カード（データ・モデルとUI）
- プッシュ通知（アクションボタンとサイレント通知でユーザーが確認できる）
- フィーチャーフラグ
- ロケーション分析

## 部分的にサポートされている機能

一部の機能はvisionOSでは部分的にしかサポートされていないが、アップルは将来的にこれらに対応する可能性が高い：

- リッチなプッシュ通知
  - 画像はサポートされている。
  - GIFとビデオはプレビューサムネイルを表示するが、再生はできない。
  - オーディオ再生はサポートされていない。
- Push Stories
  - プッシュストーリーページのスクロールと選択がサポートされている。
  - **Nextを**使ったPush Storyページ間の移動はサポートされていない。

## サポートされていない機能

- ジオフェンスのモニタリングはサポートされていない。アップルは、地域監視のためのコアロケーションAPIをvisionOSで利用可能にしていない。
- ライブ活動はサポートされていない。現在、ActivityKitはiOSとiPadOSでのみ利用可能だ。
