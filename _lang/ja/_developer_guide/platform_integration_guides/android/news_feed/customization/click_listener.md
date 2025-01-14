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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

カスタムニュースフィードクリックリスナーを設定することで、ニュースフィードのクリックを手動で処理できます。これにより、Web リンクを開くためにネイティブ・Web・ブラウザーを選択的に使用するといったユースケースが可能になります。

## ステップ 1:ニュースフィードクリックリスナーを実装する

[`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java) を実装するクラスを作成します。ユーザーがニュースフィードカードをクリックしたときに呼び出される `onFeedCardClicked()` メソッドを実装します。

## ステップ 2:ニュースフィードクリックリスナーを使用するよう Braze に指示する

`IFeedClickActionListener` が作成されたら、`BrazeFeedManager.getInstance().setFeedCardClickActionListener()` を呼び出して `BrazeFeedManager` にカスタムの `IFeedClickActionListener` を使用するよう指示します。

