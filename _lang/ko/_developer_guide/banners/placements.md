---
nav_title: 배치 관리
article_title: Braze 소프트웨어 개발 키트 배너 배치 관리하기
description: "고유 속성에 액세스하고 노출 횟수를 기록하는 등 Braze SDK에서 배너 배치를 생성하고 관리하는 방법을 알아보세요."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# 배너 배치 관리하기

> 고유 속성에 액세스하고 노출 횟수를 기록하는 등 Braze SDK에서 배너 배치를 생성하고 관리하는 방법을 알아보세요. 자세한 내용은 [배너 정보를]({{site.baseurl}}/developer_guide/banners) 참조하세요.

## 배치 요청 정보 {#requests}

{% multi_lang_include banners/placement_requests.md %}

## 게재 위치 만들기

### 필수 조건

배너 배치를 만드는 데 필요한 최소 소프트웨어 개발 키트 버전입니다:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### 2단계: 앱의 게재 위치 새로 고침 {#requestBannersRefresh}

아래에 설명된 새로고침 메서드를 호출하여 게재 위치를 새로고침할 수 있습니다. 이러한 게재 위치는 사용자 세션이 만료되거나 `changeUser` 메서드를 사용하여 식별자를 변경할 때 자동으로 캐시됩니다.

{% alert tip %}
배너 다운로드 또는 표시가 지연되지 않도록 가능한 한 빨리 게재 위치를 새로고침하세요.
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

### 3단계: 업데이트 듣기 {#subscribeToBannersUpdates}

{% alert tip %}
이 가이드의 소프트웨어 개발 키트 방법을 사용하여 배너를 삽입하면 모든 분석 이벤트(노출 횟수 및 클릭 수 등)가 자동으로 처리되며, 배너가 표시될 때만 노출 횟수가 기록됩니다.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab Javascript %}
Web Braze 소프트웨어 개발 키트와 함께 바닐라 JavaScript를 사용하는 경우 [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) 를 사용하여 게재 위치 업데이트를 수신한 다음 [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) 를 호출하여 가져옵니다.

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
Web Braze 소프트웨어 개발 키트와 함께 React를 사용하는 경우, 설정하세요. [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) 를 `useEffect` 훅 안에 설정하고 [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) 를 호출하세요.

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

### 4단계: 배치 ID를 사용하여 삽입 {#insertBanner}

{% alert tip %}
전체 단계별 튜토리얼을 보려면 [배치 ID로 배너 표시하기를]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners) 확인하세요.
{% endalert %}

{% tabs %}
{% tab Web %}

배너의 컨테이너 요소를 만듭니다. 너비와 높이를 설정해야 합니다.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Web Braze 소프트웨어 개발 키트와 함께 바닐라 JavaScript를 사용하는 경우 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 메서드를 호출하여 컨테이너 요소의 내부 HTML을 교체하세요.

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
Web Braze 소프트웨어 개발 키트와 함께 React를 사용하는 경우, 컨테이너 엘리먼트의 내부 HTML을 바꾸려면 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 메서드를 `ref` 로 호출하여 컨테이너 엘리먼트의 내부 HTML을 대체하세요.

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
노출 수를 추적하려면 `insertBanner` 으로 전화하여 `isControl`. 그런 다음 나중에 컨테이너를 숨기거나 접을 수 있습니다.
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
Java 코드로 배너를 가져오려면 다음을 사용합니다:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

이 XML을 포함하여 Android 보기 레이아웃에 배너를 만들 수 있습니다:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Android 보기를 사용하는 경우 이 XML을 사용하세요:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

젯팩 컴포즈를 사용하는 경우 이 기능을 사용할 수 있습니다:

```kotlin
Banner(placementId = "global_banner")
```

Kotlin에서 배너를 가져오려면 다음을 사용하세요:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

[React Native의 새 아키텍처를](https://reactnative.dev/architecture/landing-page) 사용하는 경우, `AppDelegate.mm` 에 `BrazeBannerView` 을 패브릭 컴포넌트로 등록해야 합니다.

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
가장 간단한 통합을 위해 배치 ID만 제공하는 다음 JSX(JavaScript XML) 스니펫을 뷰 계층 구조에 추가합니다.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

리액트 네이티브에서 배너의 데이터 모델을 가져오거나 사용자 캐시에 해당 배치가 있는지 확인하려면 다음을 사용하세요:

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
가장 간단한 통합을 위해 다음 위젯을 뷰 계층 구조에 추가하고 배치 ID만 제공하면 됩니다.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

`getBanner` 메서드를 사용하여 사용자 캐시에 해당 배치가 있는지 확인할 수 있습니다.

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

### 5단계: 테스트 배너 보내기(선택 사항) {#handling-test-cards}

배너 캠페인을 시작하기 전에 [테스트 배너를 전송하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) 연동 여부를 확인할 수 있습니다. 테스트 배너는 별도의 인메모리 캐시에 저장되며 앱 재시작 시에도 유지되지 않습니다. 추가 설정은 필요하지 않지만, 테스트 기기가 테스트를 표시할 수 있도록 전경 푸시 알림을 수신할 수 있어야 합니다.

{% alert note %}
테스트 배너는 다음 앱 세션에서 제거된다는 점을 제외하면 다른 배너와 비슷합니다.
{% endalert %}

## 노출 수 기록

소프트웨어 개발 키트 방식을 사용하여 배너를 삽입할 때 노출되는 배너의 노출 횟수를 자동으로 기록하므로 수동으로 노출 횟수를 추적할 필요가 없습니다.

## 크기 및 크기 조정

배너 크기 및 크기 조정에 대해 알아야 할 사항은 다음과 같습니다:

- 컴포저를 사용하면 배너를 다양한 크기로 미리 볼 수 있지만, 해당 정보는 SDK에 저장되거나 전송되지 않습니다.
- HTML은 렌더링되는 컨테이너의 전체 너비를 차지합니다.
- 고정된 치수 요소를 만들고 컴포저에서 해당 치수를 테스트하는 것이 좋습니다.

## 커스텀 속성 {#custom-properties}

배너 캠페인의 커스텀 속성을 사용하여 소프트웨어 개발 키트를 통해 키값 데이터를 검색하고 앱의 행동이나 모양을 수정할 수 있습니다. 예를 들어, 다음과 같이 할 수 있습니다:

- 타사 분석 또는 통합을 위한 메타데이터를 전송하세요.
- `timestamp` 또는 JSON 객체와 같은 메타데이터를 사용하여 조건 로직을 트리거하세요.
- `ratio` 또는 `format` 과 같이 포함된 메타데이터를 기반으로 배너의 동작을 제어합니다.

### 필수 조건

배너 캠페인에 [커스텀 속성을 추가해야]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties) 합니다. 또한 커스텀 속성에 액세스하는 데 필요한 최소 소프트웨어 개발 키트 버전입니다:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### 커스텀 속성 액세스하기

배너의 커스텀 속성에 액세스하려면 대시보드에 정의된 속성 유형에 따라 다음 방법 중 하나를 사용합니다. 키가 해당 유형의 속성과 일치하지 않거나 존재하지 않는 경우 메서드는 `null` 을 반환합니다.

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
