---
nav_title: 배너 카드 통합
article_title: 배너 카드 통합
hidden: true
description: "이 참조 문서에서는 배너 카드와 이 기능을 Braze SDK에 통합하는 방법에 대해 설명합니다."
platform:
  - iOS
  - Android
  - Web
  
---

# 배너 카드 통합

[콘텐츠 카드와]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) 마찬가지로 배너 카드는 앱이나 웹사이트에 직접 임베드되므로 자연스럽게 느껴지는 경험으로 사용자의 참여를 유도할 수 있습니다. 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장하면서 사용자를 위한 개인화된 메시지를 빠르고 원활하게 생성할 수 있는 솔루션입니다.

{% alert important %}
배너 카드는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

이 기능은 다음 [SDK 버전부터]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) 사용할 수 있습니다:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## 대시보드 필수 구성 요소

### 게재 위치 정의 {#define-placements}

앱에서 배너 카드 캠페인을 시작하기 전에 Braze 대시보드에서 게재 위치를 설정해야 합니다. 게재 위치는 앱에서 배너 카드를 표시할 수 있는 위치를 정의하는 것입니다.

#### 1단계: 새 게재 위치 만들기

**설정** > **배너 카드 배치**로 이동한 다음 **배치 만들기를** 선택합니다.

![배너 카드 게재 위치 섹션에서 게재 위치 ID를 생성합니다.]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### 2단계: 세부 정보 입력

배치에 이름을 지정하고 **배치 ID를** 부여합니다. 원하는 경우 배치에 대한 설명을 추가할 수 있습니다.

마케팅 팀과 협력하여 이 ID를 만드세요. 앱 코드에서 참조할 ID이며, 마케팅 팀은 이 ID를 사용하여 앱의 위치에 캠페인을 할당합니다. 

{% alert important %}
앱 또는 웹사이트와의 연동이 중단될 수 있으므로 실행 후 게재 위치 ID를 수정하지 마세요.
{% endalert %}

![봄 세일 프로모션 캠페인의 경우 배너 카드를 지정하는 배치 세부 정보가 왼쪽 사이드바에 표시됩니다.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

배너 카드 캠페인을 시작하는 방법에 대한 단계는 [배너 카드 만들기를]({{site.baseurl}}/create_banner_card/) 참조하세요.

## 앱의 게재 위치 새로 고침 {#requestBannersRefresh}

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

## 업데이트 듣기 {#subscribeToBannersUpdates}

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

## 배치 ID로 배너 카드 받기 및 삽입하기 {#insertBanner}

{% tabs %}
{% tab 자바스크립트 %}

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

## 모범 사례

### 배너 카드 크기 및 크기 조정

- Braze에서는 치수 정보를 전송하지 않습니다.

{% alert note %}
컴포저를 사용하면 배너를 다양한 크기로 미리 볼 수 있습니다. 해당 정보는 SDK에 저장되거나 전송되지 않습니다.
{% endalert %}

- HTML은 렌더링되는 컨테이너의 전체 너비를 차지합니다.
- 모범 사례로 고정된 차원 요소를 만들고 컴포저에서 해당 차원을 테스트하는 것이 좋습니다.
