---
nav_title: "Migrating from Content Cards"
article_title: "Migrating from Content Cards to Banners"
description: "Learn how to migrate from Content Cards to Banners, including code examples for all supported SDKs, limitations, and benefits."
page_order: 5
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Migrating from Content Cards to Banners

> This guide helps you migrate from Content Cards to Banners for banner-style messaging use cases. Banners are ideal for inline, persistent in-app and web messages that appear at specific placements in your application.

## Why migrate to Banners?

Banners offer several advantages over Content Cards for banner-style messaging:

### Accelerated production

- **No engineering support required**: Marketers can build custom messages using a drag-and-drop editor and custom HTML without requiring developer assistance for customization
- **Simplified customization**: No need for complex key-value pair (KVP) designs for customization

### Better UX

- **Dynamic content updates**: Banners refresh Liquid logic and eligibility on every refresh, ensuring users always see the most relevant content
- **Native placement support**: Messages appear in specific contexts rather than a feed, providing better contextual relevance
- **Native prioritization**: Control over display order without custom logic, making it easier to manage message hierarchy

### Persistence

- **No expiration limit**: Banners do not have a 30-day expiration limit like Content Cards, allowing for true persistence of messages

## When to migrate

Consider migrating to Banners if you're using Content Cards for:

- **Single banner messages at specific locations**: Messages that appear at fixed placements (e.g., top of page, navigation bar, sidebar)
- **Announcements or promotional messages**: One-time or ongoing promotional content that needs to persist beyond 30 days
- **Persistent inline messaging**: Messages that should remain visible without requiring a feed interface
- **Marketer-driven customization**: Use cases where marketers need to frequently update content without developer assistance
- **Context-specific messaging**: Messages that should appear in specific contexts rather than a general feed

## When to keep Content Cards

Continue using Content Cards if you need:

- Displaying multiple cards together in a scrollable feed or list interface
- Card-based message centers where users can view, interact with, and manage multiple messages
- Advanced interactions like swiping between cards, individual card dismissal, or card-specific actions
- Implementing custom logic to filter, sort, or organize cards based on complex criteria

## Migration guide

### Prerequisites

Before migrating, ensure your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

### 1. Subscribing to updates

#### Content Cards approach

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

#### Banners approach

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

### 2. Displaying content

#### Content Cards approach

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

#### Banners approach

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

### 3. Logging Analytics (Custom Implementations)

{% alert note %}
Both Content Cards and Banners automatically track analytics when using their default UI components. The examples below are for custom implementations where you're building your own UI.
{% endalert %}

#### Content Cards approach

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  if (!card.isControl) {
    braze.logContentCardImpressions([card]);
  } else {
    // Still log impressions for control cards
    braze.logContentCardImpressions([card]);
  }
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  if (!card.isControl) {
    card.logImpression()
  } else {
    // Still log impressions for control cards
    card.logImpression()
  }
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  if !card.isControl {
    card.context?.logImpression()
  } else {
    // Still log impressions for control cards
    card.context?.logImpression()
  }
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  if (!card.isControl) {
    Braze.logContentCardImpression(card.id);
  } else {
    // Still log impressions for control cards
    Braze.logContentCardImpression(card.id);
  }
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  if (!card.isControl) {
    braze.logContentCardImpression(card);
  } else {
    // Still log impressions for control cards
    braze.logContentCardImpression(card);
  }
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Banners approach

{% tabs %}
{% tab Web %}
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
```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}
```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### 4. Handling control groups

#### Content Cards approach

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Don't display, but still log impression
    braze.logContentCardImpressions([card]);
  } else {
    // Display and log impression
    braze.logContentCardImpressions([card]);
    // Render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Don't display, but still log impression
    card.logImpression()
  } else {
    // Display and log impression
    card.logImpression()
    // Render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Don't display, but still log impression
    card.context?.logImpression()
  } else {
    // Display and log impression
    card.context?.logImpression()
    // Render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Don't display, but still log impression
    Braze.logContentCardImpression(card.id);
  } else {
    // Display and log impression
    Braze.logContentCardImpression(card.id);
    // Render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Don't display, but still log impression
    braze.logContentCardImpression(card);
  } else {
    // Display and log impression
    braze.logContentCardImpression(card);
    // Render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Banners approach

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

## Limitations

When migrating from Content Cards to Banners, be aware of the following limitations:

### Feature differences

| Feature | Content Cards | Banners |
|---------|--------------|---------|
| Multiple cards in feed | ✅ Supported | ❌ Single banner per placement |
| Card types (Classic, Captioned, Image Only) | ✅ Multiple types | ✅ Single HTML-based banner |
| Manual dismissal | ✅ Supported | ❌ Not supported |
| Pinned cards | ✅ Supported | ❌ Not supported |
| Card expiration | ✅ Supported | ✅ Supported |
| Custom card filtering | ✅ Supported | ❌ Not supported |
| Feed UI | ✅ Default feed available | ❌ Placement-based only |

### SDK limitations

- **Unity and Cordova**: Banners are not currently supported on .NET MAUI (Xamarin), Cordova, Unity, Vega, or TV platforms
- **Minimum SDK versions**: Ensure you're using the minimum SDK versions listed in the prerequisites

## Next steps

- Learn more about [Banner placements]({{site.baseurl}}/developer_guide/banners/placements)
- Review the [Banner tutorial]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- Check [Banner analytics]({{site.baseurl}}/developer_guide/banners/analytics)
- Read the [Banner FAQ]({{site.baseurl}}/developer_guide/banners/faq)

