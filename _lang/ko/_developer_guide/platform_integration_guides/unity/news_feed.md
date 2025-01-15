---
nav_title: 뉴스피드
article_title: Unity용 뉴스 피드
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "이 참조 문서에서는 카드 구문 분석, 뉴스피드 데이터 수신 및 분석과 같은 Unity 플랫폼의 뉴스피드 통합을 다룹니다."

---

# 뉴스피드 통합

> 이 문서에서는 Unity 플랫폼용 뉴스 피드를 설정하는 방법을 다룹니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Unity에서 뉴스 피드 데이터 수신

수신 뉴스피드 카드에 대한 알림을 받도록 Unity 게임 오브젝트를 등록할 수 있습니다. 

iOS에서는 Braze 구성 편집기에서 게임 오브젝트 리스너를 설정하는 것이 좋습니다.

Android의 경우 Unity 프로젝트의 `braze.xml`에서 `com_braze_feed_listener_callback_method_name` 및 `com_braze_feed_listener_game_object_name`을 설정합니다.

어느 플랫폼에서든 런타임에 게임 오브젝트 리스너를 구성하려면 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.NEWS_FEED`를 지정합니다.

## 카드 구문 분석

게임 오브젝트 콜백으로 수신되는 `string` 메시지는 편의를 위해 [카드](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) 오브젝트 목록이 포함된 사전 제공된 [피드](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs) 오브젝트로 파싱할 수 있습니다.

자세한 내용은 다음 예시를 참조하세요:

### 콜백 예제

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## 뉴스피드 새로 고침

Braze에서 뉴스피드를 새로고침하려면 다음 방법 중 하나를 호출하세요:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

두 메서드 모두 뉴스피드 리스너에 알림을 보내고 뉴스피드를 콜백 메서드에 전달합니다.

## 분석

Braze가 직접 표시하지 않는 카드의 경우 클릭 수와 노출 수를 수동으로 기록해야 합니다.

[카드에서](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) `LogClick()` 및 `LogImpression()` 을 사용하여 특정 카드의 클릭 수와 노출 수를 기록합니다.

사용자가 피드를 전체적으로 조회했음을 기록하려면 `AppboyBinding.LogFeedDisplayed()`를 호출합니다.

