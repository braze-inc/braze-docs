---
nav_title: "コンテンツカードから移行する"
article_title: "コンテンツカードからバナーへ移行する"
description: "コンテンツカードからバナーへの移行方法を学習する。サポートされている全SDKのコード例、制限事項、利点を含む。"
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

# コンテンツカードからバナーへ移行する

> このガイドは、バナー形式のメッセージングユースケースにおいて、コンテンツカードからバナーへの移行を支援するものである。バナーは、アプリ内の特定の配置に表示される、インラインで持続的なアプリ内メッセージおよびWeb メッセージングに最適である。

## なぜバナーズに移行するのか？

- 開発チームがカスタムコンテンツカードを作成または保守している場合、バナーへの移行によりその継続的な投資を削減できる。バナーはマーケターがUIを直接コントロールできるようにし、開発者を他の作業に解放する。
- 新しいホームページメッセージやオンボーディングフロー、常時表示の告知を立ち上げるなら、コンテンツカードで構築するよりバナーから始めるべきだ。リアルタイムのパーソナライゼーションが利用できる。30日間の有効期限はなく、サイズ制限もない。導入初日からネイティブな優先順位付けが適用される。
- 30日間の有効期限制限を回避する必要がある場合、複雑な再適格性ロジックを管理している場合、あるいは陳腐化したパーソナライゼーションに悩まされている場合、Bannersはこれらの問題をネイティブに解決する。

バナーは、バナー形式のメッセージングにおいてコンテンツカードよりもいくつかの利点がある：

### 生産の加速

- **継続的な開発サポートの必要性が減少した**。マーケターは、カスタマイズに開発者の支援を必要とせずに、ドラッグ＆ドロップエディターとカスタムHTMLを使用して独自のメッセージを作成できる。
- **柔軟なカスタマイズオプション**：エディタ内で直接デザインする。HTMLを使うか、カスタムプロパティで既存のデータモデルを活用する。

### より良いユーザー体験

- **ダイナミックなコンテンツの更新**：バナーはリロードのたびにLiquidロジックと適格性を更新する。これによりユーザーは常に最も関連性の高いコンテンツを閲覧できる。
- **ネイティブ配置サポート**：メッセージはフィードではなく特定の文脈で表示されるため、文脈に応じた関連性が高くなる。
- **ネイティブ優先順位付け**カスタムロジックなしで表示順序をコントロールできるため、メッセージの階層構造を管理しやすくなる。

### 永続性

- **有効期限なし**：バナーキャンペーンはコンテンツカードのような30日間の有効期限がなく、メッセージを永続的に表示できる。

## 移行するタイミング

以下の目的でコンテンツカードを使用している場合は、バナーへの移行を検討するといい。

- ホームページのヒーロー広告、商品ページのプロモーション、チェックアウト時のオファー
- しつこいナビゲーションの案内やサイドバーのメッセージング
- 30日以上継続する常時表示メッセージ
- リアルタイムでのパーソナライゼーションと適格性を求めるメッセージ

## コンテンツカードをいつ保持するか

必要ならコンテンツカードを使い続けろ。

- **フィード体験：**複数のスクロール可能なメッセージやカード形式の「受信トレイ」を伴うあらゆるユースケース。
- **特定の特徴：**バナーはネイティブで対応していないため、コネクテッドコンテンツやプロモーションコードを必要とするメッセージは使用できない。
- **トリガー配信：**APIトリガーまたはアクションベースの配信を厳密に要求するユースケース。バナー広告はAPIトリガー型やアクションベースの配信をサポートしていないが、リアルタイム適格性評価により、ユーザーは各リフレッシュ時にセグメント所属に基づいて即座に適格か不適格かが判定される。

## 移行ガイド

### 前提条件

移行前に、Braze SDKが最低バージョン要件を満たしていることを確認せよ。

{% multi_lang_include sdk_versions.md feature='banners' %}

### 更新を購読する

#### コンテンツカード方式

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

#### バナーが近づいてくる

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
コンテンツカードはカスタムUIロジックで手動レンダリングできるが、バナーは標準のSDKメソッドでのみレンダリングできる。
{% endalert %}

#### コンテンツカード方式

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

#### バナーが近づいてくる

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

### ログ分析（カスタム実装）

{% alert note %}
コンテンツカードとバナーは、デフォルトのUIコンポーネントを使用する場合、自動的に分析データをトラッキングする。以下の例は、独自のUIを構築するカスタム実装向けである。
{% endalert %}

#### コンテンツカード方式

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

#### バナーが近づいてくる

{% tabs %}
{% tab Web %}

{% alert important %}
分析は自動的にトラッキングされる。`insertBanner()`手動でのログ記録は、.`insertBanner()`を使用している場合には使用すべきではない。
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
BannerViewを使用すると、分析データは自動的にトラッキングされる。BannerViewを使用する際には、手動でのログ記録は使用すべきではない。
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
BannerUIViewを使用すると、分析は自動的にトラッキングされる。デフォルトのBannerUIViewには手動でのロギングを使用すべきではない。
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
BrazeBannerViewを使用すると、分析は自動的にトラッキングされる。手動での記録は不要だ。
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
BrazeBannerViewを使用すると、分析は自動的にトラッキングされる。手動での記録は不要だ。
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### コントロールグループの取り扱い

#### コンテンツカード方式

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

#### バナーが近づいてくる

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

コンテンツカードからバナーへ移行する際は、以下の制限事項に注意すること：

### トリガーメッセージの移行

バナーはスケジュールされた配信キャンペーンのみをサポートする。APIトリガーまたはアクションベースで送信されていたメッセージを移行するには、セグメントベースのターゲティングに変換する。

- **例:**APIで「プロファイルを完了」カードをトリガーとして発動させる代わりに、過去7日以内に登録したがプロファイルを完了していないユーザー向けのセグメントを作成する。
- **リアルタイム適格性：**ユーザーは、各リフレッシュ時に自身のセグメント所属に基づいて、バナーの表示対象となるか否かが即座に判定される。

### 機能の違い

| 機能 | コンテンツカードによって促進された | バナー |
|---------|--------------|---------|
| **コンテンツ構造** |
| フィード内の複数のカード | ✅ サポートされている | ✅ 複数の配置を作成でき、カルーセルのような実装を実現できる。各配置につき、バナーは1つだけ返される。 |
| 複数の配置 | N/A | ✅ 複数配置に対応している |
| カードの種類（クラシック、キャプション付き、画像のみ） | ✅ 複数の事前定義済みタイプ | ✅ 単一のHTMLベースのバナー（より柔軟性がある） |
| **コンテンツ管理** |
| ドラッグアンドドロップエディタ | カスタマイズには開発者が必要だ | マーケターは開発なしで作成・更新できる |
| カスタムHTML/CSS | ❌ カード構造に限定される | ✅ HTML/CSSの完全サポート |
| カスタマイズ用のキーと値のペア | ✅ 高度なカスタマイズに必要なもの | ✅ 高度なカスタマイズのための「プロパティ」と呼ばれる強型キーと値のペア |
| **永続性&  有効期限** |
| カードの有効期限 | ✅ サポート対象（30日間制限あり） | ✅ サポート対象（有効期限なし） |
| 真の粘り強さ | ❌ 最大30日間 | ✅ 無限の持続性 |
| **ディスプレイターゲティング&** |
| フィードUI | ✅ デフォルトのフィードが利用可能だ | 配置ベースのみ |
| 文脈に応じた配置 | ❌ フィードベースの | ✅ ネイティブ配置のサポート |
| ネイティブ優先順位付け | カスタムロジックが必要だ | ✅ 内蔵優先順位付け |
| **ユーザーインタラクション** |
| 手動での解除 | ✅ サポートされている | ❌ サポートされていない |
| 固定されたカード | ✅ サポートされている | N/A |
| **分析** |
| 自動分析（デフォルトのUI） | ✅ サポートされている | ✅ サポートされている |
| 優先順位付け | ❌ サポートされていない | ✅ サポートされている | 
| **コンテンツの更新** |
| Liquidテンプレート更新 | カードごとに一度だけ、送信時／起動時に | ✅ 更新のたびに更新される |
| 資格更新 | カードごとに一度だけ、送信時／起動時に | ✅ セッションごとに更新される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 製品の制限事項

- 1つの配置につき最大25件のアクティブなメッセージング。
- リフレッシュリクエストごとに最大10個の配置IDまで。これを超えるリクエストは切り捨てられる。

### SDKの制限事項

- バナーは現在、.NET MAUI (Xamarin)、Cordova、Unity、Vega、TV プラットフォームではサポートされていない。
- 前提条件に記載されている最小SDKバージョンを使用していることを確認せよ。

## 関連記事

- [バナーの配置]({{site.baseurl}}/developer_guide/banners/placements)
- [チュートリアル：配置IDによるバナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [バナー分析]({{site.baseurl}}/developer_guide/banners/analytics)
- [バナーに関するよくある質問]({{site.baseurl}}/developer_guide/banners/faq)

