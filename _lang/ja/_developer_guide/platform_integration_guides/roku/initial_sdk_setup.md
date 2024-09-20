---
nav_title: SDK の初期セットアップ
article_title: Roku の SDK 初期設定
platform: Roku
page_order: 0
page_type: reference
description: "このページでは、Braze Roku SDK の初期設定ステップについて説明します。"
search_rank: 1
---

# SDK の初期統合

> このリファレンス記事では、Roku 向け Braze SDK のインストール方法について説明します。Braze Roku SDK をインストールすると、基本的な分析およびセグメンテーション機能が提供されます。

{% alert tip %}
GitHubのサンプルRokuアプリをチェックしよう：[TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)だ。
{% endalert %}

## ステップ1:ファイルの追加

Braze SDKファイルは、[Braze Roku SDK][1]リポジトリの`sdk_files` ディレクトリにある。

1. `source` ディレクトリで、アプリに `BrazeSDK.brs` を追加します。
2. `components` ディレクトリで、アプリに `BrazeTask.brs` と `BrazeTask.xml` を追加します。

## ステップ2:参照の追加

次の `script` 要素を使用して、メインシーンに `BrazeSDK.brs` への参照を追加します。

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## ステップ3:構成

`main.brs` 内で、グローバルノードにBrazeのコンフィギュレーションを設定する：

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

[SDKエンド]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)ポイントとAPIキーは、Brazeダッシュボードで確認できる。

## ステップ4: Braze の初期化

Braze インスタンスを初期化します。

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## ログを有効にする（オプション） {#logging}

Braze 統合をデバッグするため、Braze ログの Roku デバッグコンソールを表示できます。詳しくはRoku Developersの[Debugging codeを](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md)参照のこと。

## SDKの基本的な統合が完了した

Braze で、Braze Roku SDK を使用してアプリケーションからデータが収集されるようになりました。 

当社のSDKに[属性][2]、[イベント][3]、[購入を][4] [記録する][2]方法については、以下の記事を参照のこと。

Rokuでのアプリ内メッセージの詳細については、[アプリ内メッセージ統合ガイドを][5]参照のこと。


[1]: https://github.com/braze-inc/braze-roku-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
