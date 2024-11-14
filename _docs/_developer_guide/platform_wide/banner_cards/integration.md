---
nav_title: Integrating Banner Cards
article_title: Integrating Banner Cards
hidden: true
description: "This reference article covers Banner Cards and how to integrate this feature in the Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Integrating Banner Cards

Similar to [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), Banner Cards are embedded directly in your app or website so that you can engage users with an experience that feels natural. They’re a quick and seamless solution to create personalized messaging for your users all while extending the reach of other channels (such as email or push notifications).

{% alert important %}
Banner Cards are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

This feature is available as of the following [SDK versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Dashboard prerequisites

### Define placements {#define-placements}

Before launching a Banner Card campaign in your app, you must set up a placement in the Braze dashboard. Placements are locations that you define in your app that can display Banner Cards.

#### Step 1: Create a new placement

Go to **Settings** > **Banner Cards Placements**, then select **Create Placement**.

![Banner Card Placements section to create placement IDs.]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### Step 2: Fill in the details

Name your placement and give it a **Placement ID**. Optionally, you can add a description for your placement.

Work with your marketing team to create this ID. This is the ID you'll reference in your app's code, and your marketing team will use the ID to assign a campaign to the location in your app. 

{% alert important %}
Avoid editing your placement ID after launch, as this can break the integration with your app or website.
{% endalert %}

![Placement details that designate a Banner Card will display in the left sidebar for spring sale promotion campaigns.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

For steps on how to launch a Banner Card campaign, refer to [Creating a Banner Card]({{site.baseurl}}/create_banner_card/).

## Refresh placements in your app {#requestBannersRefresh}

Placements can be requested each session and will be cached automatically when a user's session expires or when you change identified users using the `changeUser` method.

{% alert tip %}
Refresh placements as soon as possible to avoid delays in downloading or displaying banners.
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

## Listen for updates {#subscribeToBannersUpdates}

{% alert tip %}
If you insert banners using the SDK methods in this guide, all analytics events will be handled automatically. If you want to manually render the HTML, [let us know](mailto:banners-feedback@braze.com).
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

## Get and insert a Banner Card by placement ID {#insertBanner}

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
To get the Banner in Java code, use:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

You can create Banner Cards in your Android views layout by including this XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
To get the Banner in Kotlin, use:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

If you're using Android Views, use this XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

If you're using Jetpack Compose, you can use this:

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

## Analytics

Braze automatically handles all impression logging when using the SDK methods to insert Banner Cards, so you don't need to worry about tracking impressions manually.

If you need to parse and render the HTML in a custom view, [contact us](mailto:banners-feedback@braze.com).

{% details If you emailed us and confirmed you need to manually track impressions... %}

{% alert important %}
Customization for your integration is likely unnecessary, so consider the following step carefully.
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

{% enddetails %}

## Best practices

### Banner Card dimensions and sizing

- No dimension information is sent from Braze.

{% alert note %}
The composer allows a user to preview banners in different dimensions. That information is not saved or sent to the SDK.
{% endalert %}

- The HTML will take up the full width of the container it's rendered in.
- As a best practice, we recommend making a fixed dimension element and testing those dimensions in composer.
