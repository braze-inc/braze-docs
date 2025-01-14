---
nav_title: ニュースフィード
article_title: Unityのニュースフィード
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "このリファレンス記事では、カードの解析、ニュースフィードデータの受信、分析など、Unity プラットフォームのニュースフィード統合について説明します。"

---

# ニュースフィード統合

> この記事では、Unityプラットフォーム用にニュースフィードを設定する方法を説明する。

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Unityでニュースフィードのデータを受信する

Unity ゲームオブジェクトを登録して、ニュースフィードカードの受信について通知を受けることができます。 

iOSでは、Brazeコンフィギュレーションエディターからゲームオブジェクトリスナーを設定することを推奨する。

ご使用の Android で、Unity プロジェクトの `braze.xml`で `com_braze_feed_listener_callback_method_name` と `com_braze_feed_listener_game_object_name` を設定します。

どちらかのプラットフォームでゲームオブジェクトのリスナーを実行時に設定するには、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.NEWS_FEED` を指定します。

## カードを解析する

ゲームオブジェクトコールバックで受信した受信 `string` メッセージは、事前に指定された[フィード](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs)オブジェクトに解析できます。このオブジェクトには、便宜上、[カード](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs)オブジェクトの一覧があります。

詳細は以下の例を参照のこと：

### コールバックの例

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## ニュースフィードの更新

Brazeからニュースフィードを更新するには、以下のいずれかの方法を呼び出す：

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

どちらのメソッドも、ニュース・フィード・リスナーに通知し、コールバック・メソッドにニュース・フィードを渡す。

## 分析

Braze によって直接表示されないカードについては、クリックとインプレッションを手動でログに記録する必要があります。

`LogClick()` と`LogImpression()` on[Card](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs)を使って、特定のカードのクリック数とインプレッション数を記録する。

ユーザーがフィード全体を閲覧したことを記録するには、`AppboyBinding.LogFeedDisplayed()` をコールする。

