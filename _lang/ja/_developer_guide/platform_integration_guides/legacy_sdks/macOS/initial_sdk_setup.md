---
nav_title: SDK の初期設定
article_title: MacOS 用の SDK の初期設定
platform: MacOS
page_order: 0
page_type: reference
description: "この参照記事では、macOS にBraze SDK を初期統合するためのリソースを提供します。"
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SDK の初期セットアップ

> この参照記事では、MacOS 用の Braze SDKのインストール方法について説明します。 

バージョン [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0)以降、Braze SDK は Swift Package Manager を介して統合する場合、[Mac Catalyst](https://developer.apple.com/mac-catalyst/) を使用するアプリの macOS をサポートします。現在、SDK は CocoaPods または Carthage を使用する場合、Mac Catalyst をサポートしていません。

{% alert note %}
Mac Catalyst でアプリを構築するには、<a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Apple のドキュメント</a>を参照してください。
{% endalert %}

アプリで Catalyst がサポートされたら、[次の手順に従ってSwift Package Manager を使用して]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) Braze SDKをアプリにインポートします。

## サポートされている機能

Braze は、Mac Catalyst 上で実行している場合、[プッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)、[コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/#content-cards-data-model)、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)、[および自動位置情報収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)をサポートしています。

Push Stories、リッチプッシュ、ジオフェンスは macOS ではサポートされていません。

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
