---
nav_title: コンテンツカード
article_title: Unity用コンテンツカード
platform: 
  - Unity
  - iOS
  - Android
channel: content cards
page_order: 4
description: "このリファレンス記事では、カードsの表示、カードsの解析、分析などのUnity プラットフォームのコンテンツカードインプリメンテーションガイドラインについて説明します。"

---

# コンテンツカードの統合

> このリファレンス記事では、カードsの表示、カードsの解析、分析などのUnity プラットフォームのコンテンツカードインプリメンテーションガイドラインについて説明します。

## コンテンツカードをネイティブで表示する {#unity-content-cards-native-ui}

次の呼び出しを使用して、コンテンツカードのデフォルトユーザーインターフェイスを表示できます。

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Unityでコンテンツカードデータを受信する

Unityのゲームオブジェクトを登録して、受信したコンテンツカードを通知することができます。Brazeコンフィギュレーションエディタから設定のゲームオブジェクトリスナを使用することをお勧めします。

実行時にゲームオブジェクトリスナーを設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.CONTENT_CARDS_UPDATED` を指定します。

さらに、`AppboyBinding.RequestContentCardsRefresh()` を呼び出して、iOS 上のゲームオブジェクトリスナーでデータの受信を開始する必要があります。

## コンテンツカードの解析

Content Cards ゲームオブジェクトコールバックで受信した受信`string` メッセージは、事前に提供されている[`ContentCard`][17] モデルオブジェクトに構文解析すると便利です。

コンテンツカードの解析にはJson 解析が必要です。詳細については、次の例を参照してください。

##### コンテンツカードのコールバックの例

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object 
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

## コンテンツカードの更新

Brazeからコンテンツカードを更新するには、次のいずれかの方法を呼び出します。

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## GIFサポート

{% multi_lang_include wrappers/gif_support/content_cards.md %}

## 分析

クリックとインプレッションは、Braze によって直接表示されないコンテンツカードに対して手動でログ記録する必要があります。

[Content カード][17] で`LogClick()` および`LogImpression()` を使用して、特定のカードs のクリックとインプレッションを記録します。

[17]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs
