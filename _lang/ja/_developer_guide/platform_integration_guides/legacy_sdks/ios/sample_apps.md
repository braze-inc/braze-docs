---
nav_title: サンプルアプリ
article_title: iOS 用サンプルアプリ
platform: iOS
page_order: 9
description: "この参照記事では、iOS サンプルアプリについて説明します。"

noindex: true
---

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

# サンプルアプリ

Braze SDK にはそれぞれ、利便性を高めるためにリポジトリ内にサンプルアプリケーションが付属しています。これらのアプリはそれぞれ完全にビルド可能であるため、独自のアプリケーション内で実装すると同時に、Braze 機能をテストできます。ご自身のアプリケーション内での動作のテストと、予期される動作のテスト、およびサンプルアプリケーション内でのコードパスは、問題が発生した場合に、それをデバッグするための優れた方法です。

## テストアプリケーションのビルド
[iOS SDK GitHub リポジトリ][1] では、いくつかのテストアプリケーションを使用できます。以下の手順に従って、テストアプリケーションをビルドして実行します。

1. 新しい[ワークスペース][25]を作成し、アプリ ID API キーを書き留めます。
2. API キーを `AppDelegate.m` ファイルの適切なフィールドに配置します。

iOS テストアプリケーションのプッシュ通知には、追加の設定が必要です。詳細については、[iOS プッシュ統合][7]を参照してください。

[1]: https://github.com/appboy/appboy-ios-sdk "Appboy iOS GitHub リポジトリ"
[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
