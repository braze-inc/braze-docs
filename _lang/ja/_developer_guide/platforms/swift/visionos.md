---
nav_title: ヴィジョノスのサポート
article_title: visionOSサポート
page_order: 7.2
platform: 
  - iOS
description: "この記事では、visionOSでサポートされている機能について説明する。"
---

# visionOSサポート

> [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)以降、Apple Vision Pro 用の Apple 空間コンピューティングプラットフォームである [visionOS](https://developer.apple.com/visionos/) で Braze を活用できます。Brazeを使用したvisionOSアプリのサンプルは、[サンプルアプリを]({{site.baseurl}}/developer_guide/references/?tab=swift)参照のこと。

## 完全にサポートされた機能

iOS で利用できるほとんどの機能は、visionOS でも利用できます。以下に例を示します。

- 分析（セッション、カスタムイベント、購入など）
- アプリ内メッセージング（データモデルとUI）
- コンテンツカード（データモデルとUI）
- プッシュ通知（ユーザーが見えるアクションボタン付きの通知とサイレント通知）
- フィーチャーフラグ
- ロケーション分析

## 部分的にサポートされている機能

一部の機能は visionOS では部分的にしかサポートされていませんが、Apple 社が将来的にこれらに対応する可能性は高いと思われます。

- リッチなプッシュ通知
  - 画像はサポートされている。
  - GIF とビデオでプレビューのサムネイルが表示されますが、再生することはできません。
  - オーディオ再生はサポートされていない。
- Push Stories
  - プッシュストーリーページのスクロールと選択がサポートされている。
  - [**次へ**] を使ったプッシュ通知ストーリーページ間の移動がサポートされていません。

## サポートされていない機能

- ジオフェンスのモニタリングがサポートされていません。Apple 社は、地域監視用の Core Location API を visionOS で使用できるようにしていません。
- ライブアクティビティはサポートされていません。現在、ActivityKitはiOSとiPadOSでのみ利用可能だ。
