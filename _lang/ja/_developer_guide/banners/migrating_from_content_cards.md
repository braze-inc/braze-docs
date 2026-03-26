---
nav_title: "コンテンツカードから移行する"
article_title: "コンテンツカードからバナーへ移行する"
description: "コンテンツカードからバナーへの移行方法を学びます。サポートされている全SDKのコード例、制限事項、利点を含みます。"
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

> このガイドは、バナー形式のメッセージングユースケースにおいて、コンテンツカードからバナーへの移行を支援するものです。バナーは、アプリケーション内の特定の配置に表示される、インラインで持続的なアプリ内メッセージおよびWebメッセージに最適です。

## なぜバナーに移行するのか？

- エンジニアリングチームがカスタムコンテンツカードを構築または保守している場合、バナーへの移行によりその継続的な投資を削減できます。バナーはマーケターがUIを直接コントロールできるようにし、開発者を他の作業に解放します。
- 新しいホームページメッセージやオンボーディングフロー、常時表示の告知を立ち上げる場合は、コンテンツカードで構築するよりバナーから始めましょう。リアルタイムのパーソナライゼーション、30日間の有効期限なし、サイズ制限なし、そしてネイティブな優先順位付けを導入初日から活用できます。
- 30日間の有効期限制限を回避する必要がある場合、複雑な再適格性ロジックを管理している場合、あるいは陳腐化したパーソナライゼーションに悩まされている場合、バナーはこれらの問題をネイティブに解決します。

バナーは、バナー形式のメッセージングにおいてコンテンツカードよりもいくつかの利点があります：

### 制作の加速

- **継続的なエンジニアリングサポートの必要性が減少**：マーケターは、カスタマイズに開発者の支援を必要とせずに、ドラッグ＆ドロップエディターとカスタムHTMLを使用して独自のメッセージを作成できます。
- **柔軟なカスタマイズオプション**：エディター内で直接デザインするか、HTMLを使用するか、カスタムプロパティで既存のデータモデルを活用できます。

### より良いユーザー体験

- **ダイナミックなコンテンツの更新**：バナーはリフレッシュのたびにLiquidロジックと適格性を更新するため、ユーザーは常に最も関連性の高いコンテンツを閲覧できます。
- **ネイティブ配置サポート**：メッセージはフィードではなく特定のコンテキストで表示されるため、文脈に応じた関連性が高くなります。
- **ネイティブ優先順位付け**：カスタムロジックなしで表示順序をコントロールできるため、メッセージの階層構造を管理しやすくなります。

### 永続性

- **有効期限なし**：バナーキャンペーンにはコンテンツカードのような30日間の有効期限がないため、メッセージを真に永続的に表示できます。

## 移行するタイミング

以下の目的でコンテンツカードを使用している場合は、バナーへの移行を検討してください：

- ホームページのヒーロー広告、商品ページのプロモーション、チェックアウト時のオファー
- 常時表示のナビゲーション告知やサイドバーメッセージ
- 30日以上継続する常時表示メッセージ
- リアルタイムでのパーソナライゼーションと適格性を求めるメッセージ

## コンテンツカードを維持すべきケース

以下が必要な場合は、コンテンツカードを引き続き使用してください：

- **フィード体験：**複数のスクロール可能なメッセージやカード形式の「受信トレイ」を伴うあらゆるユースケース。
- **特定の機能：**コネクテッドコンテンツやプロモーションコードを必要とするメッセージ。バナーはこれらをネイティブでサポートしていません。
- **トリガー配信：**APIトリガーまたはアクションベースの配信を厳密に必要とするユースケース。バナーはAPIトリガー型やアクションベースの配信をサポートしていませんが、リアルタイム適格性評価により、ユーザーは各リフレッシュ時にSegment所属に基づいて即座に適格か不適格かが判定されます。

## 移行ガイド

### 前提条件

移行前に、Braze SDKが最低バージョン要件を満たしていることを確認してください：

{% multi_lang_include sdk_versions.md feature='banners' %}

### 更新をサブスクライブする

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

#### バナー方式

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
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
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### コンテンツを表示する

{% alert note %}
コンテンツカードはカスタムUIロジックで手動レンダリングできますが、バナーは標準のSDKメソッドでのみレンダリングできます。
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

#### バナー方式

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
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

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### 分析のログ記録（カスタム実装）

{% alert note %}
コンテンツカードとバナーは、デフォルトのUIコンポーネントを使用する場合、自動的に分析データをトラッキングします。以下の例は、独自のUIを構築するカスタム実装向けです。
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

#### バナー方式

{% tabs %}
{% tab Web %}

{% alert important %}
`insertBanner()` を使用すると、分析は自動的にトラッキングされます。`insertBanner()` を使用している場合は、手動でのログ記録は使用しないでください。
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
BannerViewを使用すると、分析データは自動的にトラッキングされます。BannerViewを使用する際は、手動でのログ記録は使用しないでください。
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
BannerUIViewを使用すると、分析は自動的にトラッキングされます。デフォルトのBannerUIViewでは手動でのログ記録は使用しないでください。
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
BrazeBannerViewを使用すると、分析は自動的にトラッキングされます。手動でのログ記録は不要です。
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
BrazeBannerViewを使用すると、分析は自動的にトラッキングされます。手動でのログ記録は不要です。
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### プロパティの取得

#### コンテンツカード方式

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### バナー方式

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### コントロールグループの処理

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

#### バナー方式

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
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
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## 制限事項

コンテンツカードからバナーへ移行する際は、以下の制限事項に注意してください：

### トリガーメッセージの移行

バナーはスケジュールされた配信キャンペーンのみをサポートしています。以前APIトリガーまたはアクションベースで送信されていたメッセージを移行するには、Segmentベースのターゲティングに変換してください：

- **例：**APIで「プロファイルを完了」カードをトリガーする代わりに、過去7日以内に登録したがプロファイルを完了していないユーザー向けのSegmentを作成します。
- **リアルタイム適格性：**ユーザーは、各リフレッシュ時にSegment所属に基づいて、バナーの表示対象となるか否かが即座に判定されます。

### 機能の違い

| 機能 | コンテンツカード | バナー |
|---------|--------------|---------|
| **コンテンツ構造** |
| フィード内の複数カード | ✅ サポートされています | ✅ 複数の配置を作成でき、カルーセルのような実装を実現できます。各配置につき、バナーは1つだけ返されます。 |
| 複数の配置 | N/A | ✅ 複数配置に対応しています |
| カードの種類（クラシック、キャプション付き、画像のみ） | ✅ 複数の事前定義済みタイプ | ✅ 単一のHTMLベースのバナー（より柔軟性があります） |
| **コンテンツ管理** |
| ドラッグ＆ドロップエディター | ❌ カスタマイズには開発者が必要です | ✅ マーケターはエンジニアリングなしで作成・更新できます |
| カスタムHTML/CSS | ❌ カード構造に限定されます | ✅ HTML/CSSの完全サポート |
| カスタマイズ用のキーと値のペア | ✅ 高度なカスタマイズに必要です | ✅ 高度なカスタマイズのための「プロパティ」と呼ばれる強い型付けのキーと値のペア |
| **永続性と有効期限** |
| カードの有効期限 | ✅ サポート対象（30日間制限あり） | ✅ サポート対象（有効期限なし） |
| 真の永続性 | ❌ 最大30日間 | ✅ 無制限の永続性 |
| **表示とターゲティング** |
| フィードUI | ✅ デフォルトのフィードが利用可能です | ❌ 配置ベースのみ |
| 状況に即した配置 | ❌ フィードベース | ✅ ネイティブ配置サポート |
| ネイティブ優先順位付け | ❌ カスタムロジックが必要です | ✅ 組み込みの優先順位付け |
| **ユーザーインタラクション** |
| 手動での解除 | ✅ サポートされています | ❌ サポートされていません |
| 固定されたカード | ✅ サポートされています | N/A |
| **分析** |
| 自動分析（デフォルトのUI） | ✅ サポートされています | ✅ サポートされています |
| 優先順位ソート | ❌ サポートされていません | ✅ サポートされています |
| **コンテンツの更新** |
| Liquidテンプレート更新 | ❌ カードごとに送信時/起動時に1回のみ | ✅ リフレッシュのたびに更新されます |
| 適格性の更新 | ❌ カードごとに送信時/起動時に1回のみ | ✅ セッションごとに更新されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 製品の制限事項

- 1つの配置につき最大25件のアクティブなメッセージです。
- リフレッシュリクエストごとに最大10個の配置IDまでです。これを超えるリクエストは切り捨てられます。

### SDKの制限事項

- バナーは現在、.NET MAUI（Xamarin）、Cordova、Unity、Vega、TVプラットフォームではサポートされていません。
- 前提条件に記載されている最小SDKバージョンを使用していることを確認してください。

## 関連記事

- [バナーの配置]({{site.baseurl}}/developer_guide/banners/placements)
- [チュートリアル：配置IDによるバナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [バナー分析]({{site.baseurl}}/developer_guide/banners/analytics)
- [バナーに関するよくある質問]({{site.baseurl}}/developer_guide/banners/faq)