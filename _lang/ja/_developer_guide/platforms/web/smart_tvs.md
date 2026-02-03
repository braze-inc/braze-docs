---
nav_title: スマート TV 対応
article_title: Web Braze SDKのスマートTVサポート
platform: Web
page_order: 30
description: "この記事では、Braze Web SDKを使用してスマートテレビ（サムスンおよびLG）と統合する方法について説明する。"

---

# スマート TV 対応

> Braze Web SDK を使えば、[Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) や [LG TV (webOS)](https://webostv.developer.lge.com/discover) を含むスマート TV ユーザーに対して、分析を収集し、リッチなアプリ内メッセージやコンテンツカードメッセージを表示できます。この記事では、Braze Web SDKを使用してスマートTVと統合する方法について説明する。

{% alert tip %}
完全なテクニカル・リファレンスについては、[JavaScriptドキュメンテーションや](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)、TV上で動作するWeb SDKを確認するための[サンプル・アプリケーションを](https://github.com/Appboy/smart-tv-sample-apps)チェックしてほしい。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Web Braze SDKの設定

スマートTVとの統合には2つの変更が必要だ：

1. Web SDK をダウンロードまたはインポートする際は、必ず「コア」バンドル (`https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js` で入手可能、`x.y` は任意のバージョン) を使用してください。NPM バージョンはネイティブ ES モジュールで記述されているのに対し、CDN バージョンは ES5 にトランスパイルされるため、Web SDK の CDN バージョンを使用することをおすすめします。[NPMバージョンを](https://www.npmjs.com/package/@braze/web-sdk)使いたい場合は、webpackのようなバンドルツールを使って、未使用のコードを削除し、コードがES5にトランスパイルされていることを確認すること。
2. Web SDK を初期化する際には、`disablePushTokenMaintenance` と`manageServiceWorkerExternally` の初期化オプションを `true` に設定する必要があります。

## 分析

アナリティクスのための同じWeb SDKメソッドはすべて、スマートTVで使用できる。カスタムイベントやカスタム属性などのトラッキングの詳細については、[Analytics]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web) を参照してください。

## アプリ内メッセージとコンテンツカード

Braze Web SDK は、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web)とスマート TV 上の[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)の両方をサポートしています。アプリ内メッセージとコンテンツカードのレンダリングは、標準の UI 表示ではサポートされていないため、[「Core」Web SDK](https://www.npmjs.com/package/@braze/web-sdk) を使用する必要があります。代わりに、TV アプリのエクスペリエンスに合わせてアプリでカスタマイズする必要があります。

Smart TVアプリがアプリ内メッセージを受信して表示する方法の詳細については、[トリガーメッセージを]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)参照。
