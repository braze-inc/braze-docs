---
nav_title: サンプルアプリ
article_title: iOS 用サンプルアプリ
platform: Swift
page_order: 9
search_rank: 2
description: "この記事では、iOS Swift SDK サンプル アプリについて説明します。"

---

# サンプルアプリ

> Braze SDK にはそれぞれ、利便性を高めるためにリポジトリ内にサンプルアプリケーションが付属しています。これらのアプリはそれぞれ完全にビルド可能であるため、独自のアプリケーション内で実装すると同時に、Braze 機能をテストできます。 

ご自身のアプリケーション内での動作のテストと、予期される動作のテスト、およびサンプルアプリケーション内でのコードパスは、問題が発生した場合に、それをデバッグするための優れた方法です。

## ナビゲーションの例

いくつかのテストアプリケーションが利用可能です `Examples`[Swift SDK GitHub リポジトリ][1]のフォルダー。README には、次のようなサンプル統合のさまざまな組み合わせがすべて説明されています。

1. 統合タイプ (Swift パッケージ マネージャー、CocoaPods、手動)
2. コーディング言語（Swift および Objective-C）
3. プラットフォーム (iOS、tvOS、Mac Catalyst など)
4. 機能（アプリ内メッセージ、コンテンツ カード、位置情報、リッチ プッシュ、プッシュ ストーリーなど）
5. カスタマイズの種類（デフォルト UI、完全カスタム UI）

## テストアプリケーションのビルド

以下の手順に従って、テストアプリケーションをビルドして実行します。

1. 新しい [ワークスペース][2] を作成し、アプリ識別子の API キーとエンドポイントをメモします。
2. 統合方法（Swift Package Manager、CocoaPods、手動）に応じて適切なものを選択してください。 `xcodeproj` 開くファイル。
3. APIキーとエンドポイントを適切なフィールドに入力します。 `Credentials` ファイル。

[1]: https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples
[2]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps
