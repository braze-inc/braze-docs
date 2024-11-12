---
nav_title: バナーカードの統合
article_title: バナーカードの統合
hidden: true
description: "このリファレンス記事では、バナーカードとこの機能をブレーズSDK に統合する方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# バナーカードの統合

[Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about)と同様に、バナーカードはあなたのアプリやウェブサイトに直接埋め込まれており、自然な感じの体験でユーザーを巻き込むことができます。これらは、他のチャネル(電子メールやプッシュ通知など)の到達範囲を拡張しながら、すべてのユーザにパーソナライズされたメッセージングを作成するための迅速かつシームレスなソリューションです。

{% alert important %}
Banner Cardは現在初期アクセス中です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

この機能は、次の[SDK バージョン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) で使用できます。

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## ダッシュボードの前提条件

### 配置の定義 {#define-placements}

アプリでバナーカードキャンペーンを起動する前に、Braze ダッシュボードに配置を設定する必要があります。配置は、バナーカードを表示できるアプリケーションで定義する場所です。

#### ステップ1:新規配置の作成

**Settings**> **Banner Cards Placements**に移動し、**Create Placement**を選択します。

![配置ID を作成するためのバナーカード配置セクション。]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### ステップ 2:詳細を記入する

配置に名前を付け、**配置ID**を付けます。オプションで、配置の説明を追加できます。

マーケティングチームと協力して、このID を作成します。これは、アプリのコードで参照するID です。マーケティングチームは、このID を使用して、アプリの場所にキャンペーンを割り当てます。 

{% alert important %}
起動後に配置ID を編集することは避けてください。これにより、アプリやウェブサイトとの統合が損なわれる可能性があります。
{% endalert %}

![バナーカードを指定する配置詳細は、春の販売促進キャンペーンの左サイドバーに表示されます。]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

バナーカードキャンペーンの起動方法については、[バナーカードの作成]({{site.baseurl}}/create_banner_card/)を参照してください。

## アプリの配置を更新する {#requestBannersRefresh}

配置は各セッションごとに要求でき、ユーザーのセッションが期限切れになったとき、または`changeUser` メソッドを使用して識別されたユーザーを変更したときに自動的にキャッシュされます。

{% alert tip %}
バナーのダウンロードや表示の遅延を避けるため、できるだけ早く配置を更新してください。
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```
{% endtab %}
{% tab Java %}
```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
 Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## アップデートを聴く {#subscribeToBannersUpdates}

{% alert tip %}
このガイドのSDK メソッドを使用してバナーを挿入すると、すべての分析イベントが自動的に処理されます。HTML を手動でレンダリングする場合は、[](mailto:banners-feedback@braze.com) を知らせてください。
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
})

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
    for (banner in update.banners) {
      Log.d(TAG, "Received banner: " + banner.placementId)
    }
}
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## 配置ID によるバナーカードの取得と挿入 {#insertBanner}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");

    // choose where in the DOM you want to insert the banner HTML
    const container = document.getElementById("global-banner-container");

    // Insert the banner which replacees the innerHTML of that container
    braze.insertBanner(globalBanner, container);

    // Special handling if the user is part of a Control Variant
    if (globalBanner.isControl) {
        // hide or collapse the container
        container.style.display = 'none';
    }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])

```

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(placementId: "global_banner", braze: braze)
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(placementId: "global_banner", braze: braze)
}
```
{% endtab %}
{% tab Java %}
Java コードでバナーを取得するには、以下を使用します。

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

次のXML を含めることで、Android ビューレイアウトでBanner Cards を作成できます。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
コットリンのバナーを取得するには、以下を使用します。
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

Android ビューを使用している場合は、次のXML を使用します。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Jetpack Compose を使用している場合は、次を使用できます。

```kotlin
Banner(placementId = "global_banner")
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## 分析

Braze は、SDK メソッドを使用してBanner カードを挿入するときに、すべてのインプレッションロギングを自動的に処理します。 

HTML を解析してレンダリングする必要がある場合は、[ us](mailto:banners-feedback@braze.com) にお問い合わせください。以下の方法を使用して、インプレッションを追跡できます。

{% alert important %}
統合のカスタマイズは不要な場合があるため、次の手順を慎重に検討してください。
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
  // do something with the html
  // then log an impression when the HTML is in view
  braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
// First, get the Banner object:
var globalBanner: Braze.Banner?
brazeClient.braze()?.banners.getBanner(for: "global_banner", { banner in
  globalBanner = banner
})

// Then log the impression on the Banner.
globalBanner?.context?.logImpression()
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).logBannerImpression(banner.getPlacementId());
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).logBannerImpression(banner.placementId)
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## ベストプラクティス

### バナーカードの寸法とサイズ

- Braze から寸法情報は送信されません。

{% alert note %}
コンポーザーを使用すると、ユーザは異なる寸法のバナーをプレビューできます。この情報は保存されず、SDK に送信されません。
{% endalert %}

- HTML は、レンダリングされるコンテナの全幅を使用します。
- ベストプラクティスとして、固定寸法要素を作成し、それらの寸法をコンポーザーでテストすることをお勧めします。
