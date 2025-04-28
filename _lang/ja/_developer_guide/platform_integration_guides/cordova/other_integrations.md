---
nav_title: その他の統合
article_title: その他の統合
page_order: 6
---

# その他の統合

> これらは、Cordova Braze SDK でサポートされているその他の統合です。

{% multi_lang_include cordova/prerequisites.md %}

## アプリ内メッセージング

デフォルトでは、Cordova SDK は変更なしでアプリ内メッセージをサポートします。アプリ内メッセージのカスタマイズについては、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/) または [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) の統合例を参照してください。さらに、実装サンプルとして、[Cordova アプリケーションのサンプル](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js)、または [Android](https://github.com/braze-inc/braze-android-sdk) および [iOS](https://github.com/braze-inc/braze-swift-sdk) アプリケーションのサンプルを参照することができます。

### GIFサポート

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## ニュースフィード

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

ニュースフィードを Cordova アプリに統合する方法については、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/integration/) と [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/news_feed/integration/) の統合手順を参照してください。または、Cordova に用意された `launchNewsFeed` プラグインにより、さらなる統合を必要とせずにモーダルニュースフィードを開始できます。

Braze Cordova SDK には、さまざまなカテゴリの既読または未読ニュースフィードカードの数を取得するメソッドがいくつかあります。例については、[サンプルプロジェクトの実装](https://github.com/braze-inc/braze-cordova-sdk/blob/master/sample-project/www/js/index.js)をご確認ください。
