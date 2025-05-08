---
nav_title: カードの埋め込み
article_title: ろう付けSDK用の埋め込みバナーカード
description: "Braze SDK 用のBanner Card を埋め込む方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# バナーカードの埋め込み

> Braze SDK を使用してバナーカードを埋め込む方法を学習することで、自然な感じの体験をユーザーにエンゲージできるようになります。一般的な情報については、[バナーカードについて]({{site.baseurl}}/developer_guide/banner_cards/)を参照してください。

{% alert important %}
バナーカードは現在、早期アクセス段階です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

## 前提条件

以下は、Banner Card の使用を開始するために必要な最低限のSDK バージョンです。

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## バナーカードの埋め込み

{% multi_lang_include banner_cards/creating_placements.md %}

### ステップ2:アプリの配置を更新する {#requestBannersRefresh}

配置はセッションごとにリクエストでき、ユーザーのセッションの有効期限が切れたとき、または `changeUser` メソッドを使用して識別されたユーザーを変更したときに自動的にキャッシュされます。

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
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### ステップ 3:更新をリッスンする {#subscribeToBannersUpdates}

{% alert tip %}
このガイドのSDK メソッドを使用してバナーを挿入すると、すべての分析イベントが自動的に処理されます。HTML を手動でレンダリングする場合は、[お知らせください](mailto:banners-feedback@braze.com)。
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
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  data => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map(banner => banner.placementId),
    );
  },
);
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
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### ステップ4:配置ID を使用した埋め込み {#insertBanner}

{% tabs %}
{% tab JavaScript %}

バナーのコンテナー要素を作成します。幅と高さは必ず設定してください。

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

次に、[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) メソッドを使用して、コンテナ要素の内部HTML を置き換えます。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
    baseUrl: "sdk-base-url",
    allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");
    if (!globalBanner) {
        return;
    }

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
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
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
Kotlin でバナーを取得するには、以下を使用します。
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

Android ビューを使用している場合は、次の XML を使用します。

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

[React Native の新しいアーキテクチャ](https://reactnative.dev/architecture/landing-page) を使用している場合は、`BrazeBannerView` をファブリックコンポーネントとして`AppDelegate.mm` に登録する必要があります。

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```

Banner Card のデータモデルをReact Native で取得するには、以下を使用します。

```javascript
const banner = await Braze.getBanner("global_banner");
```

`getBanner` メソッドを使用して、ユーザーのキャッシュにその配置が存在するかどうかを確認できます。ただし、最も単純な統合のために、以下のJavaScript XML (JSX) スニペットをビュー階層に追加し、配置ID のみを指定します。

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
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
バナーカードのデータモデルをFlutter で取得するには、以下を使用します。

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

`getBanner` メソッドを使用して、ユーザーのキャッシュにその配置が存在するかどうかを確認できます。ただし、最も単純な統合のために、以下のウィジェットをビュー階層に追加し、配置ID のみを指定します。

```dart
BrazeBannerView(
  placementId: "global_banner",
),
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### ステップ 5: テストカードを送信する(オプション) {#handling-test-cards}

[バナーカードキャンペーン]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)を起動する前に、テストバナーカードを送信して統合を検証できます。テストカードは別のメモリ内キャッシュに保存され、アプリの再起動後も保持されません。追加のセットアップは必要ありませんが、テスト・デバイスがテスト・カードを表示できるように、フォアグラウンド・プッシュ通知を受信できる必要があります。

{% alert note %}
テストバナーカードは、次のアプリセッションで削除される点を除き、他のバナーと同じです。
{% endalert %}

## 分析のログ記録

SDK メソッドを使用してバナーカードを挿入すると、Braze は自動的にインプレッションを記録します。そのため、インプレッションを手動で追跡する必要はありません。カスタムビューでHTML を解析してレンダリングする必要がある場合は、[banners-feedback@braze.com](mailto:banners-feedback@braze.com) までお問い合わせください。

## 寸法とサイズ

バナーカードの寸法とサイズについては、次のとおりです。

- 作曲者が異なる寸法のバナーをプレビューする間、その情報は保存されず、SDK に送信されません。
- HTML は、レンダリングされるコンテナの全幅を使用します。
- 固定寸法要素を作成し、それらの寸法をコンポーザーでテストすることをお勧めします。
