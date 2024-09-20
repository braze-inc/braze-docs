---
nav_title: スマートTVとの統合
article_title: スマートTVのウェブ統合
platform: Web
page_order: 20
description: "この記事では、Braze Web SDKを使用してスマートテレビ（サムスンおよびLG）と統合する方法について説明する。"

---

# スマートTVとの統合

> Braze Web SDKを使えば、[Samsung Tizen TVや][1] [LG TV (webOS)を][2]含むスマートTVユーザーに対して、アナリティクスを収集し、リッチなアプリ内メッセージやコンテンツカードメッセージを表示することができる。この記事では、Braze Web SDKを使用してスマートTVと統合する方法について説明する。

完全なテクニカル・リファレンスについては、[JavaScriptドキュメンテーションや][3]、TV上で動作するWeb SDKを確認するための[サンプル・アプリケーションを][9]チェックしてほしい。

## Braze SDKをインストールする

始めるには、Web SDKの[初期SDKセットアップ][4]ガイドに従う。

スマートTVとの統合には2つの変更が必要だ：

1. Web SDKをダウンロードまたはインポートする際は、必ず "core "バンドル（https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js で入手可能、x.y は希望のバージョン）を使用すること。NPMバージョンはネイティブのESモジュールで書かれているのに対し、CDNバージョンはES5にトランスパイルされているからだ。[NPMバージョンを][6]使いたい場合は、webpackのようなバンドルツールを使って、未使用のコードを削除し、コードがES5にトランスパイルされていることを確認すること。
2. Web SDK を初期化する際には、`disablePushTokenMaintenance` と`manageServiceWorkerExternally` の初期化オプションを`true` に設定する必要がある。

## 分析

アナリティクスのための同じWeb SDKメソッドはすべて、スマートTVで使用できる。

カスタム・イベントやカスタム属性などのトラッキングに関する完全なガイドは、[アナリティクスの]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/)ドキュメントを参照のこと。

## アプリ内メッセージとコンテンツカード

Braze Web SDKは、[アプリ内メッセージと][7]スマートTV上の[コンテンツカードの][8]両方をサポートしている。アプリ内メッセージやコンテンツカードのレンダリングは、標準のUI表示ではサポートされていないため、[「Core」Web SDKを][6]使用する必要がある。

Smart TVアプリがアプリ内メッセージを受信して表示する方法の詳細については、[アプリ内メッセージ表示マニュアルを][5]参照のこと。


[1]: https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html
[2]: https://webostv.developer.lge.com/discover
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display
[6]: https://www.npmjs.com/package/@braze/web-sdk
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/
[9]: https://github.com/Appboy/smart-tv-sample-apps
