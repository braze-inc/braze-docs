{% multi_lang_include developer_guide/prerequisites/unity.md %}

## 기본적으로 콘텐츠 카드 표시 {#unity-content-cards-native-ui}

다음 호출을 사용하여 콘텐츠 카드의 기본 UI를 표시할 수 있습니다:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Unity에서 콘텐츠 카드 데이터 수신

수신 콘텐츠 카드에 대한 알림을 받도록 Unity 게임 오브젝트를 등록할 수 있습니다. Braze 설정 에디터에서 게임 오브젝트 리스너를 설정하는 것을 권장합니다.

런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`를 지정합니다.

iOS의 게임 오브젝트 리스너에서 데이터 수신을 시작하려면 추가적으로 `AppboyBinding.RequestContentCardsRefresh()`를 호출해야 합니다.

## 콘텐츠 카드 구문 분석

콘텐츠 카드 게임 오브젝트 콜백에서 수신되는 `string` 메시지는 편의를 위해 미리 제공된 [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) 모델 오브젝트로 파싱할 수 있습니다.

콘텐츠 카드 구문 분석에는 JSON 구문 분석이 필요하며, 자세한 내용은 다음 예시를 참조하세요:

##### 콘텐츠 카드 콜백 예시

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

## 콘텐츠 카드 새로 고침

Braze에서 콘텐츠 카드를 새로 고치려면 다음 메서드 중 하나를 호출합니다.

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## 분석

Braze에서 직접 표시하지 않는 콘텐츠 카드의 경우 클릭 수와 노출 수를 수동으로 기록해야 합니다.

특정 카드의 클릭 및 노출 횟수를 기록하려면 [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs)에서 `LogClick()` 및 `LogImpression()`을 사용합니다.

