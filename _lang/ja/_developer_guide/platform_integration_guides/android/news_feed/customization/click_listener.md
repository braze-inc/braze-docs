---
nav_title: クリックの手動処理
article_title: Android と FireOS のニュースフィードクリックの手動処理
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードのクリックを手動で処理する方法について説明します。"
channel:
  - news feed
  
---

# クリックの手動処理

> このリファレンス記事では、Android または FireOS アプリケーションでニュースフィードのクリックを手動で処理する方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、ニュースフィードツールを利用しているお客様に、コンテンツカードのメッセージングチャネルへの移行をお勧めしています。移行により、柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

カスタムニュースフィードクリックリスナーを設定することで、ニュースフィードのクリックを手動で処理できます。これにより、Web リンクを開くためにネイティブ・Web・ブラウザーを選択的に使用するといったユースケースが可能になります。

## ステップ 1:ニュースフィードクリックリスナーを実装する

[`IFeedClickActionListener`][37] を実装するクラスを作成します。ユーザーがニュースフィードカードをクリックしたときに呼び出される `onFeedCardClicked()` メソッドを実装します。

## ステップ 2:ニュースフィードクリックリスナーを使用するよう Braze に指示する

`IFeedClickActionListener` が作成されたら、`BrazeFeedManager.getInstance().setFeedCardClickActionListener()` を呼び出して `BrazeFeedManager` にカスタムの `IFeedClickActionListener` を使用するよう指示します。

[37]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java
