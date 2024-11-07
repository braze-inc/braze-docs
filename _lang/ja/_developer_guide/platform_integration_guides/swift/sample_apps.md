---
nav_title: サンプルアプリ
article_title: iOS 用サンプルアプリ
platform: Swift
page_order: 9
search_rank: 2
description: "この記事では、iOS SWIFT SDK サンプルアプリについて説明します。"

---

# サンプルアプリ

> Braze SDK にはそれぞれ、利便性を高めるためにリポジトリ内にサンプルアプリケーションが付属しています。これらのアプリはそれぞれ完全にビルド可能であるため、独自のアプリケーション内で実装すると同時に、Braze 機能をテストできます。 

ご自身のアプリケーション内での動作のテストと、予期される動作のテスト、およびサンプルアプリケーション内でのコードパスは、問題が発生した場合に、それをデバッグするための優れた方法です。

## サンプルのナビゲーション

いくつかのテストアプリケーションは、[SWIFT SDK GitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)の`Examples`フォルダー内で利用できます。READMEには、次のようなサンプル統合のさまざまな組み合わせが記載されています。

1. 統合タイプ（SWIFTパッケージマネージャー、CocoaPods、手動）
2. コーディング言語（SWIFTとOBJECTIVE-C）
3. プラットフォーム（iOS、tvOS、Mac Catalystなど）
4. 機能（アプリ内メッセージ、コンテンツカード、位置情報、リッチプッシュ、プッシュストーリーなど）
5. カスタマイズの種類（デフォルトUI、完全カスタムUI）

## テストアプリケーションのビルド

以下の手順に従って、テストアプリケーションをビルドして実行します。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)を作成し、アプリ識別子APIキーおよびエンドポイントに注意してください。
2. 統合方法 (Swift Package Manager、CocoaPods、Manual) に基づいて、適切な `xcodeproj` ファイルを選択して開きます。
3. `Credentials`ファイルの適切なフィールドにAPIキーとエンドポイントを配置します。

