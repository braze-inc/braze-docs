---
nav_title: SDK の初期設定
article_title: Roku の SDK 初期設定
platform: Roku
page_order: 0
page_type: reference
description: "このページでは、Braze Roku SDK の初期設定ステップについて説明します。"
search_rank: 1
---

# SDK の初期統合

> このリファレンス記事では、Roku 向け Braze SDK のインストール方法について説明します。Braze Roku SDK をインストールすると、基本的な分析およびセグメンテーション機能が提供されます。

## ステップ1: ファイルの追加

Braze SDK ファイルは、[Braze Roku SDK リポジトリ][1] の `sdk_files` ディレクトリにあります。

1. `source` ディレクトリで、アプリに `BrazeSDK.brs` を追加します。
2. `components` ディレクトリで、アプリに `BrazeTask.brs` と `BrazeTask.xml` を追加します。

## ステップ2: 参照の追加

次の `script` 要素を使用して、メインシーンに `BrazeSDK.brs` への参照を追加します。

\`\`\`
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"></script>
```

## ステップ3: 構成

「main.brs」内で、グローバルノードの Braze 構成を設定します。

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDK エンドポイント]({{site.baseurl}})/user_guide/administrative/access_braze/sdk_endpoints/) and API key within the Braze dashboard. が見つかります

## ステップ4: Braze の初期化

Braze インスタンスを初期化します。

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Enable Logging (optional) {#logging}

Braze 統合をデバッグするため、Braze ログの Roku デバッグコンソールを表示できます。[デバッグコード] を参照してください (https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) from Roku Developers to learn more.

## Basic SDK integration complete

Braze で、Braze Roku SDK を使用してアプリケーションからデータが収集されるようになりました。

SDK への [属性][2]、[イベント][3]、[購入][4] のロギング方法については、以下の記事を参照してください。

Roku のアプリ内メッセージングの詳細については、[アプリ内メッセージ統合ガイド][5] を参照してください。


[1]: https://github.com/braze-inc/braze-roku-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
