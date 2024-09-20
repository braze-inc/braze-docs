---
nav_title: ニュースフィード
article_title: Unityのニュースフィード
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "このリファレンス記事では、カードの解析、ニュースフィードデータの受信、分析など、Unityプラットフォームのニュースフィード統合について説明する。"

---

# ニュースフィード統合

> この記事では、Unityプラットフォーム用にニュースフィードを設定する方法を説明する。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## Unityでニュースフィードのデータを受信する

Unityのゲーム・オブジェクトを登録して、ニュース・フィード・カードの受信を通知することができる。 

iOSでは、Brazeコンフィギュレーションエディターからゲームオブジェクトリスナーを設定することを推奨する。

`com_braze_feed_listener_callback_method_name` `com_braze_feed_listener_game_object_name` Androidでは、Unityプロジェクトの`braze.xml` 。

どちらのプラットフォームでも、実行時にゲーム・オブジェクト・リスナーを設定するには、`AppboyBinding.ConfigureListener()` を使い、`BrazeUnityMessageType.NEWS_FEED` を指定する。

## カードを解析する

ゲームオブジェクトのコールバックで受信した`string` メッセージは、あらかじめ用意されている[Feed][11]オブジェクトにパースされる。

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

Brazeが直接表示しないカードについては、クリック数とインプレッション数を手動で記録する必要がある。

`LogClick()` と`LogImpression()` on[Card][12]を使って、特定のカードのクリック数とインプレッション数を記録する。

ユーザーがフィード全体を閲覧したことを記録するには、`AppboyBinding.LogFeedDisplayed()` をコールする。

[11]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs
[12]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs
