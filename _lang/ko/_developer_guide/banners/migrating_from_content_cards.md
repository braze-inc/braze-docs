---
nav_title: "콘텐츠 카드에서 마이그레이션"
article_title: "콘텐츠 카드에서 배너로 마이그레이션"
description: "모든 지원되는 SDK에 대한 코드 예제, 제한 사항 및 이점을 포함하여 콘텐츠 카드에서 배너로 마이그레이션하는 방법을 배우십시오."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# 콘텐츠 카드에서 배너로 마이그레이션

> 이 가이드는 배너 스타일 메시징 사용 사례를 위해 콘텐츠 카드에서 배너로 마이그레이션하는 데 도움을 줍니다. 배너는 애플리케이션의 특정 위치에 나타나는 인라인, 지속적인 인앱 및 웹 메시지에 이상적입니다.

## 왜 배너로 마이그레이션해야 할까요?

- 귀하의 엔지니어링 팀이 커스텀 콘텐츠 카드를 구축하거나 유지 관리하고 있다면, 배너로 마이그레이션하면 지속적인 투자를 줄일 수 있습니다. 배너는 마케터가 UI를 직접 제어할 수 있게 하여 개발자가 다른 작업에 집중할 수 있도록 합니다.
- 새로운 홈페이지 메시지, 온보딩 흐름 또는 지속적인 공지를 시작하는 경우, 콘텐츠 카드에서 구축하기보다는 배너로 시작하십시오. 실시간 개인화, 30일 만료 없음, 크기 제한 없음, 그리고 첫날부터 네이티브 우선 순위를 누릴 수 있습니다.
- 30일 만료 제한을 우회하거나 복잡한 재자격 논리를 관리하거나 오래된 개인화에 불만이 있는 경우, 배너는 이러한 문제를 네이티브로 해결합니다.

배너는 배너 스타일 메시징을 위해 콘텐츠 카드보다 여러 가지 장점을 제공합니다:

### 생산 가속화

- **필요한 지속적인 엔지니어링 지원 감소**: 마케터는 개발자의 도움 없이 드래그 앤 드롭 편집기와 커스텀 HTML을 사용하여 커스텀 메시지를 구축할 수 있습니다.
- **유연한 커스터마이징 옵션**: 편집기에서 직접 디자인하고, HTML을 사용하거나 커스텀 속성이 있는 기존 데이터 모델을 활용하십시오.

### 더 나은 UX

- **동적 콘텐츠 업데이트**: 배너는 매번 새로 고침할 때 Liquid 논리와 자격을 새로 고쳐 사용자가 항상 가장 관련성 높은 콘텐츠를 볼 수 있도록 합니다.
- **네이티브 배치 지원**: 메시지는 피드가 아닌 특정 상황에서 나타나며, 더 나은 상황별 관련성을 제공합니다.
- **네이티브 우선순위 지정**: 사용자 정의 논리 없이 표시 순서를 제어하여 메시지 계층 구조를 더 쉽게 관리할 수 있습니다.

### 지속성

- **만료 제한 없음**: 배너 캠페인은 콘텐츠 카드처럼 30일 만료 제한이 없으며, 메시지의 진정한 지속성을 허용합니다.

## 마이그레이션 시기

콘텐츠 카드를 사용 중이라면 배너로 마이그레이션하는 것을 고려하세요:

- 홈페이지 히어로, 제품 페이지 프로모션, 체크아웃 제안
- 지속적인 내비게이션 공지 또는 사이드바 메시지
- 30일 이상 실행되는 항상 켜져 있는 메시지
- 실시간 개인화 및 적격성을 원하는 메시지

## 콘텐츠 카드를 유지해야 할 때

다음이 필요한 경우 콘텐츠 카드를 계속 사용하세요:

- **피드 경험:** 여러 개의 스크롤 가능한 메시지 또는 카드 기반 "받은편지함"과 관련된 모든 사용 사례.
- **특정 기능:** 연결된 콘텐츠 또는 프로모션 코드가 필요한 메시지, 배너는 이러한 기능을 기본적으로 지원하지 않습니다.
- **트리거된 전달:** API 트리거 또는 실행 기반 전달이 엄격하게 필요한 사용 사례. 배너는 API 트리거 또는 실행 기반 전달을 지원하지 않지만, 실시간 적격성 평가를 통해 사용자가 각 새로고침 시 세그먼트 멤버십에 따라 즉시 자격을 부여받거나 자격을 상실합니다.

## 마이그레이션 가이드

### 필수 조건

마이그레이션하기 전에 Braze SDK가 최소 버전 요구 사항을 충족하는지 확인하십시오:

{% multi_lang_include sdk_versions.md feature='banners' %}

### 업데이트 가입

#### 콘텐츠 카드 접근 방식

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### 배너 접근 방식

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const globalBanner = braze.getBanner("global_banner");
  if (globalBanner) {
    console.log("Banner received for placement:", globalBanner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val globalBanner = Braze.getInstance(context).getBanner("global_banner")
  if (globalBanner != null) {
    Log.d(TAG, "Banner received for placement: ${globalBanner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "global_banner") { banner in
    if let banner = banner {
      print("Banner received for placement: \(banner.placementId)")
    }
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("global_banner").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("global_banner").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### 콘텐츠 표시

{% alert note %}
콘텐츠 카드는 커스텀 UI 로직으로 수동으로 렌더링할 수 있지만, 배너는 기본 제공 SDK 메서드로만 렌더링할 수 있습니다.
{% endalert %}

#### 콘텐츠 카드 접근 방식

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### 배너 접근 방식

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="global_banner" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("global_banner"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["global_banner"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='global_banner'
/>

// Or get banner data
const banner = await Braze.getBanner("global_banner");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "global_banner",
)

// Or get banner data
final banner = await braze.getBanner("global_banner");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% endtabs %}

### 로그 분석 (커스텀 구현)

{% alert note %}
콘텐츠 카드와 배너는 기본 UI 구성 요소를 사용할 때 자동으로 분석을 추적합니다. 아래 예시는 자신만의 UI를 구축하는 커스텀 구현을 위한 것입니다.
{% endalert %}

#### 콘텐츠 카드 접근 방식

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
    braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
    card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
    card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
    Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
    braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### 배너 접근 방식

{% tabs %}
{% tab Web %}

{% alert important %}
`insertBanner()`를 사용할 때 분석이 자동으로 추적됩니다. `insertBanner()`을 사용할 때 수동 로그 기록은 사용하지 않아야 합니다.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([globalBanner]);

// Log click (with optional buttonId)
braze.logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
BannerView를 사용할 때 분석이 자동으로 추적됩니다. BannerView를 사용할 때 수동 로그 기록은 사용하지 않아야 합니다.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("global_banner");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
BannerUIView를 사용할 때 분석이 자동으로 추적됩니다. 기본 BannerUIView에 대해 수동 로그 기록은 사용하지 않아야 합니다.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Log impression
braze.banners.logImpression(placementId: "global_banner")

// Log click (with optional buttonId)
braze.banners.logClick(placementId: "global_banner", buttonId: buttonId)

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
BrazeBannerView를 사용할 때 분석이 자동으로 추적됩니다. 수동 로그 기록이 필요하지 않습니다.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
BrazeBannerView를 사용할 때 분석이 자동으로 추적됩니다. 수동 로그 기록이 필요하지 않습니다.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### 대조군 처리

#### 콘텐츠 카드 접근 방식

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### 배너 접근 방식

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  
  // Always call insertBanner to track impression (including control)
  braze.insertBanner(globalBanner, container);
  
  // Hide if control group
  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "global_banner",
)
```
{% endtab %}
{% endtabs %}

## Limitations

콘텐츠 카드에서 배너로 마이그레이션할 때 다음 제한 사항을 인식해야 합니다:

### 트리거된 메시지 마이그레이션

배너는 예약된 배달 캠페인만 지원합니다. 이전의 API 트리거 또는 액션 기반 메시지를 마이그레이션하려면 세그먼트 기반 타겟팅으로 변환하십시오:

- **예시:** API로 "프로필 완성" 카드를 트리거하는 대신, 지난 7일 이내에 가입했지만 프로필을 완료하지 않은 사용자에 대한 세그먼트를 만드십시오.
- **실시간 자격:** 사용자는 세그먼트 멤버십에 따라 각 새로 고침 시 배너에 즉시 자격을 부여하거나 자격을 박탈당합니다.

### 기능 차이

| Feature | 콘텐츠 카드 | Banners |
|---------|--------------|---------|
| **콘텐츠 구조** |
| 피드의 여러 카드 | ✅ 지원됨 | ✅ 캐러셀과 같은 구현을 달성하기 위해 여러 배치를 만들 수 있습니다. 배치당 하나의 배너만 반환됩니다. |
| 여러 배치 | N/A | ✅ 여러 배치 지원 |
| 카드 유형 (클래식, 캡션, 이미지 전용) | ✅ 여러 미리 정의된 유형 | ✅ 단일 HTML 기반 배너 (더 유연함) |
| **콘텐츠 관리** |
| 드래그 앤 드롭 편집기 | ❌ 사용자 정의를 위해 개발자가 필요합니다. | ✅ 마케터는 엔지니어링 없이 생성/업데이트할 수 있습니다. |
| 커스텀 HTML/CSS | ❌ 카드 구조로 제한됨 | ✅ 전체 HTML/CSS 지원 |
| 사용자 지정을 위한 키-값 쌍 | ✅ 고급 사용자 지정을 위해 필요 | ✅ 고급 사용자 지정을 위한 "속성"이라고 불리는 강력한 타입의 키-값 쌍 |
| **영속성 & 만료** |
| 카드 만료 | ✅ 지원됨 (30일 제한) | ✅ 지원됨 (만료 제한 없음) |
| 진정한 영속성 | ❌ 30일 최대 | ✅ 무제한 영속성 |
| **디스플레이 & 타겟팅** |
| 피드 UI | ✅ 기본 피드 사용 가능 | ❌ 배치 기반만 가능 |
| 맥락별 배치 | ❌ 피드 기반 | ✅ 네이티브 배치 지원 |
| 네이티브 우선 순위 | ❌ 사용자 정의 논리가 필요합니다 | ✅ 내장 우선 순위 지정 |
| **사용자 상호작용** |
| 수동 해제 | ✅ 지원됨 | ❌ 지원되지 않음 |
| 고정 카드 | ✅ 지원됨 | N/A |
| **분석** |
| 자동 분석(기본 UI) | ✅ 지원됨 | ✅ 지원됨 |
| 우선 순위 정렬 | ❌ 지원되지 않음 | ✅ 지원됨 | 
| **콘텐츠 업데이트** |
| Liquid 템플릿 새로 고침 | ❌ 카드 전송/시작 시 한 번만 | ✅ 매번 새로 고침 시 새로 고침 |
| 자격 새로 고침 | ❌ 카드 전송/시작 시 한 번만 | ✅ 매 세션마다 새로 고침 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 제품 제한

- 배치당 최대 25개의 활성 메시지.
- 새로 고침 요청당 최대 10개의 배치 ID; 이 이상 요청은 잘립니다.

### SDK 제한 사항

- .NET MAUI(Xamarin), Cordova, Unity, Vega 또는 TV 플랫폼에서는 배너가 현재 지원되지 않습니다.
- 필수 조건에 나열된 최소 SDK 버전을 사용하고 있는지 확인하십시오.

## 관련 문서

- [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)
- [튜토리얼: 배너를 배치 ID로 표시하기]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [배너 분석]({{site.baseurl}}/developer_guide/banners/analytics)
- [배너 FAQ]({{site.baseurl}}/developer_guide/banners/faq)

