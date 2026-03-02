---
nav_title: 配置の管理
article_title: Braze SDKのバナー配置の管理
description: "固有のプロパティへのアクセスやインプレッションの記録など、Braze SDKでバナープレイスメントを作成および管理する方法について説明します。"
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# バナー配置の管理

> 固有のプロパティへのアクセスやインプレッションの記録など、Braze SDKでバナープレイスメントを作成および管理する方法について説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/developer_guide/banners)を参照してください。

## 配置リクエストについて {#requests}

{% multi_lang_include banners/placement_requests.md %}

## 配置を作成する

### 前提条件

バナー配置を作成するために必要な最小SDKバージョンは次のとおりです。

{% multi_lang_include sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### ステップ2:アプリの配置をリフレッシュする {#requestBannersRefresh}

以下に説明するリフレッシュメソッドを呼び出すことで、配置をリフレッシュできます。これらの配置は、ユーザーのセッションが期限切れになったとき、または`changeUser`メソッドを使用して識別済みユーザーを変更したときに、自動的にキャッシュされます。

{% alert tip %}
バナーのダウンロードや表示の遅延を避けるため、できるだけ早く配置をリフレッシュしてください。
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
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

### ステップ3:更新をリッスンする {#subscribeToBannersUpdates}

{% alert tip %}
このガイドのSDKメソッドを使用してバナーを挿入すると、すべての分析イベント（インプレッションやクリックなど）が自動的に処理され、インプレッションはバナーが表示されているときにのみ記録されます。
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Web Braze SDKでバニラJavaScriptを使用している場合は、[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)を使用してプレイスメントの更新をリッスンし、[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)を呼び出してフェッチします。

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Web Braze SDKでReactを使用している場合は、`useEffect`フック内で[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)を設定し、リスナーの登録後に[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)を呼び出します。

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
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
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
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

### ステップ4:配置IDを使って挿入する {#insertBanner}

{% alert tip %}
完全なステップバイステップのチュートリアルについては、[配置IDでバナーを表示する]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)を確認してください。
{% endalert %}

{% tabs %}
{% tab Web %}

バナーのコンテナ要素を作成します。幅と高さを必ず設定してください。

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Web Braze SDKでバニラJavaScriptを使用している場合は、[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)メソッドを呼び出して、コンテナ要素の内部HTMLを置き換えます。

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

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Web Braze SDKでReactを使用している場合は、[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)メソッドを`ref`とともに呼び出して、コンテナ要素の内部HTMLを置き換えます。

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
インプレッションをトラッキングするには、`isControl`の場合でも必ず`insertBanner`を呼び出してください。その後、コンテナを非表示にしたり折りたたんだりできます。
{% endalert %}

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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Javaコードでバナーを取得するには、以下を使用します。

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

次のXMLを含めることで、Androidビューレイアウトでバナーを作成できます。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Android Viewsを使用している場合は、次のXMLを使用します。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Jetpack Composeを使用している場合は、次を使用できます。

```kotlin
Banner(placementId = "global_banner")
```

Kotlinでバナーを取得するには、以下を使用します。
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

[React Nativeの新しいアーキテクチャ](https://reactnative.dev/architecture/landing-page)を使用している場合は、`BrazeBannerView`をFabricコンポーネントとして`AppDelegate.mm`に登録する必要があります。

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
最もシンプルな統合方法として、以下のJavaScript XML（JSX）スニペットをビュー階層に追加し、配置IDのみを指定します。

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

React Nativeでバナーのデータモデルを取得したり、ユーザーのキャッシュにその配置が存在するかどうかを確認するには、以下を使用します。

```javascript
const banner = await Braze.getBanner("global_banner");
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
最もシンプルな統合方法として、以下のウィジェットをビュー階層に追加し、配置IDのみを指定します。

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

`getBanner`メソッドを使用して、ユーザーのキャッシュにその配置が存在するかどうかを確認できます。

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
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

### ステップ5:テストバナーを送信する（オプション） {#handling-test-cards}

バナーキャンペーンを開始する前に、[テストバナーを送信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)して統合を確認できます。テストバナーは別のインメモリキャッシュに保存され、アプリの再起動後は保持されません。追加のセットアップは不要ですが、テストを表示するためにテストデバイスがフォアグラウンドのプッシュ通知を受信できる必要があります。

{% alert note %}
テストバナーは通常のバナーと同じですが、次のアプリセッションで削除されます。
{% endalert %}

## インプレッションの記録

Brazeは、SDKメソッドを使用してバナーを挿入する際、表示中のバナーのインプレッションを自動的に記録します。そのため、インプレッションを手動でトラッキングする必要はありません。

## クリックの記録

バナークリックの記録方法は、バナーのレンダリング方法とクリックハンドラーの配置場所によって異なります。

### 標準バナーコンテンツ（自動）

デフォルトの標準SDKメソッドを使用してバナーを挿入し、バナーが標準のエディターコンポーネント（画像、ボタン、テキスト）を使用している場合、クリックは自動的にトラッキングされます。SDKがこれらの要素にクリックリスナーをアタッチするため、追加のコードは不要です。

### カスタムコードブロック

バナーがBrazeダッシュボードの**カスタムコード**エディターブロックを使用している場合は、`brazeBridge.logClick()`を使用して、そのカスタムHTML内からクリックを記録する必要があります。これは、SDKメソッドを使用してバナーをレンダリングする場合でも同様です。SDKはカスタムコード内の要素にリスナーを自動的にアタッチできないためです。

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

完全なリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge)を参照してください。`brazeBridge`は、バナーの内部HTMLと親Braze SDK間の通信レイヤーを提供します。

### カスタムUI実装（ヘッドレス）

バナーHTMLをレンダリングするのではなく、バナーの[カスタムプロパティ](#custom-properties)を使用して完全にカスタムのUIを構築する場合は、アプリケーションコードからクリック（およびインプレッション）を手動で記録する必要があります。SDKがバナーをレンダリングしていないため、カスタムUI要素とのインタラクションを自動的にトラッキングすることはできません。

Bannerオブジェクトの`logClick()`メソッドを使用してください。

## 寸法とサイズ

バナーの寸法とサイズについて知っておくべきことは以下のとおりです。

- コンポーザーではさまざまな寸法でバナーをプレビューできますが、その情報は保存されず、SDKにも送信されません。
- HTMLは、レンダリングされるコンテナの全幅を占めます。
- 固定寸法の要素を作成し、コンポーザーでその寸法をテストすることをお勧めします。

## カスタムプロパティ {#custom-properties}

バナーキャンペーンのカスタムプロパティを使用して、SDKからキーと値のデータを取得し、アプリの動作や外観を変更できます。たとえば、次のようなことが可能です。

- サードパーティの分析や統合のためにメタデータを送信する。
- `timestamp`やJSONオブジェクトなどのメタデータを使用して条件付きロジックをトリガーする。
- `ratio`や`format`などのメタデータに基づいてバナーの動作をコントロールする。

### 前提条件

バナーキャンペーンに[カスタムプロパティを追加]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties)する必要があります。また、カスタムプロパティにアクセスするために必要な最小SDKバージョンは以下のとおりです。

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### カスタムプロパティへのアクセス

バナーのカスタムプロパティにアクセスするには、ダッシュボードで定義されたプロパティの型に基づいて、以下のいずれかのメソッドを使用します。キーがその型のプロパティと一致しないか存在しない場合、メソッドは`null`を返します。

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object propertyßß
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}