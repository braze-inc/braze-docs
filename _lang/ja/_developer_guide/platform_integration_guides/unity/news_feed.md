---
nav_title: ニュースフィード
article_title: Unity のニュースフィード
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "このリファレンス記事では、カードの解析、ニュースフィードデータの受信、分析など、Unity プラットフォームのニュースフィードの統合について説明します。"

---

# ニュースフィード統合

> この記事では、Unityプラットフォーム用のニュースフィードの設定方法について説明します。

{% alert note %}
ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## Unity でニュースフィードデータを受信する

Unity のゲームオブジェクトを登録して、ニュースフィードカードの受信を通知することができます。 

iOSでは、Brazeコンフィグレーションエディタからゲームオブジェクトリスナーを設定することをお勧めします。

Android では、 `com_braze_feed_listener_callback_method_name` Unity `com_braze_feed_listener_game_object_name` プロジェクトの `braze.xml`.

いずれかのプラットフォームで実行時にゲームオブジェクトリスナーを設定するには、 を使用して `AppboyBinding.ConfigureListener()` 指定 `BrazeUnityMessageType.NEWS_FEED`します。

## カードの解析

ゲームオブジェクトのコールバックで受信した受信`string`メッセージは、便宜上[Card][12]オブジェクトのリストを持つ、事前に提供されている[Feed][11]オブジェクトに解析できます。

次の例を参照してください。 details:

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

Brazeからニュースフィードを更新するには、次のいずれかのメソッドを呼び出します。

\`\`\`csharp
Brazeへのネットワークリクエストが発生します
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()を呼び出します。
\`\`\`

どちらのメソッドも、ニュースフィードのリスナーに通知し、ニュースフィードをコールバックメソッドに渡します。

## 分析

クリック数とインプレッション数は、Brazeが直接表示しないカードに対して手動で記録する必要があります。

`LogClick()`[カード] と `LogImpression()` [[カード][12]] を使用して、特定のカードのクリック数と表示回数を記録します。

ユーザーがフィード全体を表示したことをログに記録するには、 を呼び出し `AppboyBinding.LogFeedDisplayed()`ます。

[11]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs
[12]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs
