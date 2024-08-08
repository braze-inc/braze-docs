---
nav_title: スマートTV統合
article_title: Web向けスマートTV統合
platform: Web
page_order: 20
description: "この記事では、Braze Web SDK を使用してスマートテレビ(Samsung およびLG) と統合する方法について説明します。"

---

# スマートTV統合

> Braze Web SDK では、[Samsung Tizen TVs][1] と[LG TVs (webOS)][2] を含む、アプリ内の豊富なメッセージとコンテンツカードメッセージをスマートTV ユーザーに収集して表示できます。この記事では、Braze Web SDK を使用してスマートテレビに統合する方法について説明します。

完全なテクニカルリファレンスについては、弊社の[JavaScript Documentation][3] または弊社の[サンプルアプリ][9] をチェックして、テレビで実行されているWeb SDK をご覧ください。

## Braze SDK の取り付け

開始するには、Web SDK の[初期SDK セットアップ][4] ガイドに従ってください。

スマートテレビとの統合には、次の2 つの変更が必要です。

1. Web SDK をダウンロードまたはインポートする場合は、必ず "core" bundle (https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, where x.y is the desired version). We recommend using the CDN version of our Web SDK, since the NPM version is written in native ES modules whereas the CDN version is transpiled down to ES5. If you prefer to use the [NPM version][6] で使用可能) を使用してください。未使用のコードを削除する webpack などのバンドラーを使用していて、コードが ES5 にトランスパイルドダウンされていることを確認してください。
2. Web SDK を初期化する場合は、`disablePushTokenMaintenance` および`manageServiceWorkerExternally` 初期化オプションを`true` に設定する必要があります。

## 分析

分析用の同じWeb SDK メソッドはすべて、スマートテレビで使用できます。

カスタムイベント、カスタム属性などを追跡するための完全なガイドについては、[Analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/) のドキュメントを参照してください。

## アプリ内メッセージとコンテンツカード

Braze Web SDK は、スマートテレビで[アプリ内メッセージ][7] と[コンテンツカード][8] の両方をサポートしています。["Core"Web SDK][6]をアプリ内メッセージのレンダリングとして使用する必要があります。また、コンテンツカードは標準のUI ディスプレイを使用することはサポートされておらず、代わりにTV アプリの体験に合わせてアプリでカスタマイズする必要があります。

スマートTVアプリがアプリ内メッセージを受信および表示する方法の詳細については、[アプリ内の手動メッセージ表示][5]をご覧ください。


[1]: https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html
[2]: https://webostv.developer.lge.com/discover
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display
[6]: https://www.npmjs.com/package/@braze/web-sdk
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/
[9]: https://github.com/Appboy/smart-tv-sample-apps
