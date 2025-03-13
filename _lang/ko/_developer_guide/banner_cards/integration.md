---
nav_title: 배너 카드
article_title: Braze SDK용 배너 카드
hidden: true
description: "이 참조 문서에서는 배너 카드와 이 기능을 Braze SDK에 통합하는 방법에 대해 설명합니다."
platform:
  - iOS
  - Android
  - Web
  
---

# 배너 카드 통합

> [콘텐츠 카드와]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) 마찬가지로 배너 카드는 앱이나 웹사이트에 직접 임베드되므로 자연스럽게 느껴지는 경험으로 사용자의 참여를 유도할 수 있습니다. 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장하면서 사용자를 위한 개인화된 메시지를 빠르고 원활하게 생성할 수 있는 솔루션입니다.

{% alert important %}
배너 카드는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 필수 조건

배너 카드를 통합하려면 먼저 앱에서 [배너 카드 게재 위치를 생성해야]({{site.baseurl}}/developer_guide/banner_cards/creating_placements) 합니다.

또한 배너 카드 사용을 시작하는 데 필요한 최소 SDK 버전입니다:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 reactnative:14.0.0 %}

## 배너 카드 통합

### 1단계: 앱의 게재 위치 새로 고침 {#requestBannersRefresh}

게재 위치는 세션마다 요청할 수 있으며, 사용자의 세션이 만료되거나 `changeUser` 방법을 사용하여 식별된 사용자를 변경하면 자동으로 캐시됩니다.

{% alert tip %}
배너 다운로드 또는 표시가 지연되지 않도록 가능한 한 빨리 게재 위치를 새로고침하세요.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}

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

{% tab 코르도바 %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not currently supported on Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### 2단계: 업데이트 듣기 {#subscribeToBannersUpdates}

{% alert tip %}
이 가이드의 SDK 방법을 사용하여 배너를 삽입하면 모든 애널리틱스 이벤트가 자동으로 처리됩니다. HTML을 수동으로 렌더링하려면 [알려주세요](mailto:banners-feedback@braze.com).
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}

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

{% tab 코르도바 %}
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

### 3단계: 배치 ID로 카드 삽입 {#insertBanner}

{% tabs %}
{% tab 자바스크립트 %}

배너의 컨테이너 요소를 만듭니다. 너비와 높이를 설정해야 합니다.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

그런 다음 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 메서드를 사용하여 컨테이너 요소의 내부 HTML을 교체합니다.

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
Java 코드로 배너를 가져오려면 다음을 사용합니다:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

이 XML을 포함하면 Android 보기 레이아웃에 배너 카드를 만들 수 있습니다:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
Kotlin에서 배너를 가져오려면 다음을 사용하세요:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

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

리액트 네이티브에서 배너를 사용하려면 다음을 사용하세요:

```javascript
const banner = await Braze.getBanner("global_banner");
```

리액트 네이티브 애플리케이션에서 뷰 계층 구조에 다음 자바스크립트 XML(JSX) 스니펫을 추가합니다.

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

{% tab 코르도바 %}
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

## 분석

배너 카드를 삽입하기 위해 SDK 방법을 사용할 때 Braze가 모든 노출 로깅을 자동으로 처리하므로 수동으로 노출을 추적하는 것에 대해 걱정할 필요가 없습니다.

사용자 지정 보기에서 HTML을 구문 분석하고 렌더링해야 하는 경우 [문의하세요](mailto:banners-feedback@braze.com).

{% details 수동으로 노출을 추적하는 방법에 대한 자세한 정보 %}

{% alert important %}
통합을 위한 사용자 지정은 불필요할 수 있으므로 다음 단계를 신중하게 고려하세요.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}

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

{% tab 코르도바 %}
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

{% enddetails %}

## 테스트 전송 처리하기

캠페인을 시작하기 전에 테스트 전송을 사용하여 배너 카드 통합을 확인합니다. 테스트 배너 카드는 별도의 인메모리 캐시에 저장되며 앱을 다시 시작할 때 지속되지 않습니다. 추가 설정은 필요하지 않지만, 테스트 배너 카드를 표시하려면 기기가 포그라운드 푸시 알림을 수신할 수 있어야 합니다.

{% alert important %}
테스트 배너는 다음 앱 세션에서 제거된다는 점을 제외하면 다른 배너와 동일하게 취급됩니다. 테스트 배너를 표시하려면 앱에서 해당 배너의 위치를 설정해야 합니다.
{% endalert %}

## 크기 및 크기 조정

배너 카드의 크기와 사이즈에 대해 알아야 할 몇 가지 사항은 다음과 같습니다:

- 컴포저를 사용하면 배너를 다양한 크기로 미리 볼 수 있지만, 해당 정보는 SDK에 저장되거나 전송되지 않습니다.
- HTML은 렌더링되는 컨테이너의 전체 너비를 차지합니다.
- 고정 치수 요소를 만들고 컴포저에서 해당 치수를 테스트하는 것이 좋습니다.
