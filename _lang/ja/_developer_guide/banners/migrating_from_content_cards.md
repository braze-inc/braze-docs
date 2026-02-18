---
nav_title: "コンテンツカードからの移行"
article_title: "コンテンツカードからバナーへの移行"
description: "サポートされているすべてのSDK、制限、利点のコードサンプルを含む、コンテンツカードからバナーへの移行方法について説明します。"
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

# コンテンツカードからバナーへの移行

> このガイドは、バナースタイルのメッセージング ユースケースのコンテンツカードからバナーへの移行に役立ちます。バナーは、インライン、永続的なインアプリおよびウェブメッセージ用のアイデアl です。これらは、アプリライケーションの特定の場所でイヤーをアプリします。

## なぜバナーに移行するのか?

- 開発チームがカスタムコンテンツカードを作成または管理している場合、バナーに移行すると、その継続的な投資を削減できます。バナーは、マーケター s にUI を直接コントロールさせ、他の作業のために開発者s を解放します。
- 新しいホームページメッセージ、オンボーディングの流れ、または永続的なアナウンスを起動する場合は、コンテンツカードではなく、バナーで開始します。リアルタイムパーソナライゼーション、30 日間の有効期限なし、サイズ制限なし、1 日目からのネイティブ優先順位付けのメリットを得ることができます。
- 30 日間の有効期限の制限を回避したり、複雑な再適格ロジックを管理したり、古いパーソナライゼーションにイライラしたりする場合、バナーはこれらの問題をネイティブに解決します。

バナースタイルのメッセージングのために、バナーはコンテンツカードよりもいくつかのタグを提供しています:

### 生産加速

- **必要な継続開発の短縮**:マーケターは、ドラッグアンドドロップエディターとカスタムHTMLを使用してカスタムメッセージを作成できます。カスタマイズのために開発者な支援は必要ありません
- **柔軟なカスタマイズオプション**:エディタで直接デザインするか、HTMLを使用するか、既存のデータモデルをカスタムプロパティで活用します

### ベターUX

- **動的内容更新s**:リフレッシュごとにリキッドロジックと適格性をリフレッシュし、ユーザーが最も適切な内容を常に確認できるようにします
- **ネイティブ配置サポート**:メッセージは、フィードではなく、特定の文脈でアプリし、より良い文脈に応じた or 状況に即した関連性を提供します
- **ネイティブ優先度**:カスタムロジックなしで表示順序を制御し、メッセージ階層の管理を容易にする

### 永続性

- **有効期限なし**:バナーキャンペーンsには、コンテンツカードのような30日間の有効期限がなく、メッセージの真の持続性を可能にします

## 移行時期

コンテンツカードを使用している場合は、バナーへの移行を検討してください。

- ホームページヒーロー、商品ページプロモーション、チェックアウトオファー
- 永続的なナビゲーションのアナウンスまたはサイドバーメッセージ
- 30 日以上実行されている常時オンメッセージ
- リアルタイムのパーソナライゼーションと適格性が必要なメール

## コンテンツカードをいつ保持するか

必要に応じて、コンテンツカードの使用を続行します。

- **飼料体験:**複数のスクロール可能なメッセージ、またはカードベースの"Inbox"を含むユースケース。
- **特長:**バナーがネイティブにサポートしていないため、接続コンテンツまたはプロモーションコードを必要とするメッセージ。
- **トリガー配信:**API-トリガー ed またはアクション ベースの配信を厳密に必要とするユースケース。Banner はAPI-トリガー ed またはアクション ベースの配信をサポートしていませんが、リアルタイム適格性評価とは、ユーザー s が更新ごとにSegmentメンバーシップに基づいて即座に適格または不適格になることを意味します。

## 移行ガイド

### 前提条件

移行する前に、Braze SDKが最低限必要なバージョンを満たしていることを確認してください。

{% multi_lang_include sdk_versions.md feature='banners' %}

### 更新を購読する

#### コンテンツカードアプリへの侵入

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

#### バナーズ・アプリ・ローチ

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

### 表示内容

{% alert note %}
コンテンツカードは、カスタムUIロジックを使用して手動でレンダリングできますが、バナーは、すぐに使用できるSDK方法でのみレンダリングできます。
{% endalert %}

#### コンテンツカードアプリへの侵入

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

#### バナーズ・アプリ・ローチ

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

### ログ分析(カスタムインプリメンテーション)

{% alert note %}
デフォルトのユーザーインターフェイスコンポーネントを使用すると、コンテンツカードとバナーの両方で分析が自動的に追跡されます。以下の例は、独自のUI を構築するカスタム実装の場合です。
{% endalert %}

#### コンテンツカードアプリへの侵入

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

#### バナーズ・アプリ・ローチ

{% tabs %}
{% tab Web %}

{% alert important %}
`insertBanner()` を使用すると、分析が自動的に追跡されます。`insertBanner()` を使用する場合は、手動ロギングを使用しないでください。
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
BannerView を使用すると、分析が自動的に追跡されます。BannerView を使用する場合は、手動ロギングを使用しないでください。
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
BannerUIView を使用すると、分析が自動的に追跡されます。手動ロギングは、デフォルト BannerUIView には使用しないでください。
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
BrazeBannerView を使用すると、分析が自動的に追跡されます。手動ロギングは不要です。
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
BrazeBannerView を使用すると、分析が自動的に追跡されます。手動ロギングは不要です。
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### コントロールグループの処理

#### コンテンツカードアプリへの侵入

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

#### バナーズ・アプリ・ローチ

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

## 制限事項

コンテンツカードからバナーに移行する場合は、次の制限事項に注意してください。

### トリガーメッセージの移行

バナーはスケジュールされた配信キャンペーンs のみに対応しています。以前にAPI-トリガーされたメッセージまたはアクションベースのメッセージを移行するには、それをSegmentベースのターゲットに変換します。

- **例:**&quot をトリガーする代わりに、プロファイル" API を使用してカードを完了し、過去7 日間にサインアップしたがプロファイルを完了していないユーザーのSegmentを作成します。
- **リアルタイム資格:**ユーザは、Segmentメンバーシップに基づいて、リフレッシュごとに即座にバナーの資格を取得するか、または資格を喪失します。

### 機能の違い

| 機能 | コンテンツカードによって促進された | バナー |
|---------|--------------|---------|
| **コンテンツ構造** |
| フィードにおける多重カードs | ✅ 対応 | ✅ カルーセルのようなインプリメンテーションを実現するために、複数の配置を作成できます。配置ごとに1 つのバナーのみが返されます。 |
| 複数配置 | N/A | ✅ 複数の配置をサポート |
| カードの種類(クラシック、キャプション、イメージのみ) | ✅ 複数の事前定義型 | ✅ 単一HTMLベースのバナー(より柔軟) |
| **コンテンツ管理** |
| ドラッグアンドドロップエディタ | ❌ カスタマイズに開発者が必要 | ✅ マーケターは開発なしで作成/更新できる |
| カスタムHTML/CSS | ❌ カード構成に限定 | ✅ フルHTML/CSS対応 |
| カスタマイズ用のキーと値のペア | ✅ 高度なカスタマイズに必要 | ✅ 詳細なカスタマイズのために、"properties"と呼ばれる厳密に型付けされたキーと値のペア |
| **永続性& 期限切れ** |
| カードの有効期限 | ✅ サポート(30 日制限) | ✅ サポート(有効期限なし) |
| 真の持続性 | ❌ 最大30日間 | ✅ 無限の持続性 |
| **& Targeting の表示** |
| フィードUI | ✅ 使用可能な既定のフィード | ❌ 配置ベースのみ |
| コンテキスト固有の配置 | ❌ 飼料ベース | ✅ ネイティブ配置サポート |
| ネイティブの優先順位付け | ❌ カスタムロジックが必要 | ✅ 組み込みの優先順位付け |
| **ユーザ間アクション** |
| 手動解雇 | ✅ 対応 | ❌ 未対応 |
| 固定カードs | ✅ 対応 | N/A |
| **分析** |
| オート分析(デフォルトユーザーインターフェイス) | ✅ 対応 | ✅ 対応 |
| 優先順位のソート | ❌ 未対応 | ✅ 対応 | 
| **コンテンツの更新** |
| 液体テンプレーティングリフレッシュ | ❌ 送信/起動時にカードごとに1回 | ✅ リフレッシュごとにリフレッシュ |
| 適格性の更新 | ❌ 送信/起動時にカードごとに1回 | ✅ セッションごとに更新 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 製品の制限事項

- 配置ごとに最大25 のアクティブメッセージ。
- リフレッシュ要求ごとに最大 10 個の配置 ID。これを超える要求は切り捨てられます。

### SDK制限

- 現在、バナーは。NET MAUI (Xamarin)、Cordova、Unity、ベガ、またはTV プラットフォームではサポートされていません。
- 前提条件に記載されている最低限のSDKを使用していることを確認します。

## 関連記事

- [バナーの配置]({{site.baseurl}}/developer_guide/banners/placements)
- [チュートリアル:配置ID によるバナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [バナー分析]({{site.baseurl}}/developer_guide/banners/analytics)
- [バナーに関するよくある質問]({{site.baseurl}}/developer_guide/banners/faq)

