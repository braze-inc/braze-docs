---
nav_title: スマートTVとの統合
article_title: Web 向けスマート TV の統合
platform: Web
page_order: 20
description: "この記事では、Braze Web SDKを使用してスマートテレビ（サムスンおよびLG）と統合する方法について説明する。"

---

# スマートTVとの統合

> Braze Web SDK を使えば、[Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) や [LG TV (webOS)](https://webostv.developer.lge.com/discover) を含むスマート TV ユーザーに対して、分析を収集し、リッチなアプリ内メッセージやコンテンツカードメッセージを表示できます。この記事では、Braze Web SDKを使用してスマートTVと統合する方法について説明する。

完全なテクニカル・リファレンスについては、[JavaScriptドキュメンテーションや](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)、TV上で動作するWeb SDKを確認するための[サンプル・アプリケーションを](https://github.com/Appboy/smart-tv-sample-apps)チェックしてほしい。

## Braze SDKをインストールする

開始するには、Web SDK の[初期 SDK 設定]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)ガイドに従ってください。

スマートTVとの統合には2つの変更が必要だ：

1. Web SDK をダウンロードまたはインポートする際は、必ず「コア」バンドル (https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js で入手可能、x.y は任意のバージョン) を使用してください。NPM バージョンはネイティブ ES モジュールで記述されているのに対し、CDN バージョンは ES5 にトランスパイルされるため、Web SDK の CDN バージョンを使用することをおすすめします。[NPMバージョンを](https://www.npmjs.com/package/@braze/web-sdk)使いたい場合は、webpackのようなバンドルツールを使って、未使用のコードを削除し、コードがES5にトランスパイルされていることを確認すること。
2. Web SDK を初期化する際には、`disablePushTokenMaintenance` と`manageServiceWorkerExternally` の初期化オプションを `true` に設定する必要があります。

## 分析

アナリティクスのための同じWeb SDKメソッドはすべて、スマートTVで使用できる。

カスタムイベントやカスタム属性などのトラッキングに関する完全なガイドについては、[分析]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/)ドキュメントを参照してください。

## アプリ内メッセージとコンテンツカード

Braze Web SDK は、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/)とスマート TV 上の[コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/)の両方をサポートしています。アプリ内メッセージとコンテンツカードのレンダリングは、標準の UI 表示ではサポートされていないため、[「Core」Web SDK](https://www.npmjs.com/package/@braze/web-sdk) を使用する必要があります。代わりに、TV アプリのエクスペリエンスに合わせてアプリでカスタマイズする必要があります。

Smart TVアプリがアプリ内メッセージを受信して表示する方法の詳細については、[アプリ内メッセージ表示マニュアルを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display)参照のこと。


