---
nav_title: コンテンツカード
article_title: Unity用コンテンツカード
platform: 
  - Unity
  - iOS
  - Android
channel: content cards
page_order: 4
description: "このリファレンス記事では、カードの表示、カードの解析、分析など、Unityプラットフォームにおけるコンテンツカードの実装ガイドラインについて説明します。"

---

# コンテンツカードの統合

> このリファレンス記事では、カードの表示、カードの解析、分析など、Unityプラットフォームにおけるコンテンツカードの実装ガイドラインについて説明します。

## コンテンツカードのネイティブ表示 {#unity-content-cards-native-ui}

コンテンツ・カードのデフォルトUIは、以下の呼び出しで表示できる：

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Unityでコンテンツカードのデータを受け取る

Unityのゲームオブジェクトを登録して、コンテンツカードの受信を通知することができます。ゲームオブジェクトのリスナーは、Braze設定エディターから設定することをお勧めします。

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使い、`BrazeUnityMessageType.CONTENT_CARDS_UPDATED` を指定してください。

iOSのゲーム・オブジェクト・リスナーでデータの受信を開始するには、`AppboyBinding.RequestContentCardsRefresh()` 。

## コンテンツカードの解析

Content Cardsゲームオブジェクトのコールバックで受信した`string` メッセージは、あらかじめ用意された [`ContentCard`][17]モデルオブジェクトに解析されます。

コンテンツ・カードの解析にはJson解析が必要です。 details:

##### コンテンツカードのコールバック例

\`\`\`csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message)；

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
    throw new ArgumentException("Could not parse content card JSON message.")；
  ()
}
\`\`\`

## コンテンツカードの更新

Brazeからコンテンツカードをリフレッシュするには、以下のいずれかの方法を呼び出します：

\`\`\`csharp
// Brazeへのネットワークリクエストの結果
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
\`\`\`

## 分析

Brazeが直接表示しないコンテンツカードについては、クリック数とインプレッション数を手動で記録する必要があります。

[ContentCard][17]の`LogClick()` と`LogImpression()` を使って、特定のカードのクリック数とインプレッション数を記録する。

[17]: https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs
