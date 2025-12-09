# Content Cards to Banners Migration Guide

> This migration guide provides comprehensive instructions for transitioning from **Content Cards** to **Banners** in Braze. It is divided into two sections: a User Guide for marketers and non-technical users, and a Developer Guide for engineering teams.

---

# User Guide

> This section is designed for marketers, product managers, and non-technical team members migrating from Content Cards to Banners.

## Introduction

### What is changing and why

Braze has introduced **Banners**, a new messaging channel designed to deliver personalized, inline messaging within your app or website. While Content Cards have served as a powerful messaging tool for creating persistent, feed-based experiences, Banners offer a simpler, more streamlined approach for displaying contextual messages directly within your user interface.

**Key reasons for the transition:**

| Content Cards | Banners |
|---------------|---------|
| Requires custom development for each placement | Uses a visual drag-and-drop editor |
| Supports multiple card types (Classic, Captioned Image, Image Only) | Provides flexible HTML-based rendering |
| Cards exist in a "feed" that users browse | Banners are embedded inline at specific placements |
| Max 30-day expiration | No fixed expiration limit |
| User-dismissible | Not user-dismissible (controlled by targeting) |
| Supports Canvas and API-triggered campaigns | Campaigns only (scheduled delivery) |

### High-level summary of the new workflow

1. **Define Placements**: Work with your engineering team to create Banner placements in your app or website
2. **Create Campaigns**: Use the visual editor to design Banners
3. **Assign Placements**: Connect your Banner campaign to a placement
4. **Target & Launch**: Set audience, priority, and schedule your campaign

---

## Before You Begin

### Prerequisites

Before you can create and launch Banner campaigns:

1. ✅ **Development Integration**: Your engineering team must integrate Banner placements into your app or website (see Developer Guide)
2. ✅ **SDK Version Requirements**: Ensure your app uses minimum SDK versions:
   - Swift: 11.3.0+
   - Android: 33.1.0+
   - Web: 5.8.1+
   - React Native: 14.0.0+
   - Flutter: 13.0.0+
3. ✅ **Braze Package**: Banners availability depends on your Braze package—contact your account manager if you're unsure

### What you need to understand about Banners

**Banners are different from Content Cards:**

- **No Feed**: Banners don't appear in a scrollable feed—they appear at specific, developer-defined locations
- **No User Dismissal**: Users cannot swipe away or dismiss Banners; visibility is controlled by segment eligibility
- **Session-Based Updates**: Banner content refreshes at the start of each user session
- **Priority System**: When multiple Banners target the same placement, priority determines which one displays

---

## Concept Mapping (Content Cards → Banners)

### Terminology Changes

| Content Cards Term | Banners Term | Notes |
|--------------------|--------------|-------|
| Card Types (Classic, Captioned Image, Image Only) | Banner Templates | Banners use a flexible HTML editor with drag-and-drop blocks |
| Feed | Placement | A specific location in your app where Banners appear |
| Card Pinning | Banner Priority | High/Medium/Low priority system |
| Card Dismissal | Segment Eligibility | Control visibility through targeting criteria |
| Key-Value Pairs (extras) | Custom Properties | Metadata attached to Banners for app behavior |
| Card Expiration (max 30 days) | Campaign Duration | Set start/end times (no 30-day limit) |
| Content Card Inbox | N/A | Banners are inline—no inbox concept |
| Carousel | Multiple Placements | Use different placements for similar effects |

### Conceptual Changes

| Concept | Content Cards | Banners |
|---------|---------------|---------|
| **Message Persistence** | Cards remain in feed until expiration or dismissal | Banners display while user qualifies for campaign |
| **Multi-Message Display** | Users see all eligible cards in feed | One Banner per placement (highest priority) |
| **User Control** | Users can dismiss cards | App controls visibility via targeting |
| **Analytics Tracking** | Manual impression logging often required | Automatic impression logging when using SDK methods |
| **Message Creation** | Dashboard + custom code for appearance | Visual drag-and-drop editor |
| **Delivery Method** | API-triggered, action-based, or scheduled | Scheduled delivery only |

---

## Side-by-Side Workflow Comparison

### Creating a Campaign

<table>
<tr>
<th width="50%">Content Cards (Before)</th>
<th width="50%">Banners (Now)</th>
</tr>
<tr>
<td>

1. Go to **Campaigns** > **Create Campaign**
2. Select **Content Cards**
3. Name your campaign
4. Choose card type: Classic, Captioned Image, or Image Only
5. Fill in title, description, image URL, link text
6. Configure key-value pairs
7. Set delivery, targeting, expiration (max 30 days)
8. Launch

</td>
<td>

1. Go to **Campaigns** > **Create Campaign**
2. Select **Banner**
3. Name your campaign
4. **Select a Placement** (must be pre-created)
5. Use drag-and-drop editor to build your Banner
6. Configure custom properties (optional)
7. Set campaign duration, priority, targeting
8. Launch

</td>
</tr>
</table>

### Message Composition

<table>
<tr>
<th width="50%">Content Cards (Before)</th>
<th width="50%">Banners (Now)</th>
</tr>
<tr>
<td>

**Form-Based Editor:**
- Enter title text
- Enter description text
- Paste image URL
- Enter link text and URL
- Add key-value pairs manually

**Styling:** Controlled by developer code

</td>
<td>

**Visual Drag-and-Drop Editor:**
- Drag image blocks, text blocks, buttons
- Add email capture forms
- Insert custom HTML
- Style backgrounds, borders, spacing visually
- Preview in different dimensions

**Styling:** Built into the editor

</td>
</tr>
</table>

### What becomes easier with Banners

| Feature | Improvement |
|---------|-------------|
| **Visual Design** | No code changes needed—design directly in the dashboard |
| **Placement Control** | Define exactly where messages appear in your app |
| **Priority Management** | Drag-and-drop priority ordering for competing campaigns |
| **Content Updates** | Changes reflect on next session without app updates |
| **Custom Styling** | Full HTML/CSS support without developer involvement |
| **No Expiration Limit** | Banners can run indefinitely (Content Cards max out at 30 days) |

---

## Step-by-Step Migration Instructions

### Step 1: Audit Your Existing Content Card Campaigns

1. **List all active Content Card campaigns** in your Braze dashboard
2. For each campaign, document:
   - Campaign name and purpose
   - Card type used (Classic, Captioned Image, Image Only)
   - Where it appears in your app (e.g., homepage, inbox, specific screens)
   - Key-value pairs used
   - Targeting criteria
   - Delivery type (scheduled, API-triggered, action-based)

> **⚠️ WARNING:** Banners do NOT support API-triggered or action-based delivery. Campaigns using these delivery types will need to be redesigned for scheduled delivery with segment-based targeting.

### Step 2: Coordinate with Your Engineering Team

Before creating Banner campaigns, your engineering team must:

1. **Create Placement IDs** in **Settings** > **Banners Placements**
2. **Integrate placements** into your app using the Braze SDK
3. **Test placements** to ensure Banners render correctly

Provide your engineers with:
- The locations where Content Cards currently appear
- New locations you want Banners to appear
- Sizing requirements for each placement

### Step 3: Create Banner Placements in Braze

1. Go to **Settings** > **Banners Placements**
2. Select **Create Placement**
3. Give your placement a descriptive name (e.g., "Homepage Hero", "Checkout Promo")
4. Assign a **Placement ID** (e.g., `homepage_hero`, `checkout_promo`)

> **⚠️ WARNING:** Placement IDs should NOT be changed after launch. Coordinate with your engineering team to agree on IDs before creating them.

### Step 4: Recreate Your Campaigns as Banners

For each Content Card campaign you're migrating:

1. **Create a new Banner campaign:**
   - Go to **Messaging** > **Campaigns** > **Create Campaign**
   - Select **Banner**
   
2. **Select your placement:**
   - Choose the placement that corresponds to where your Content Card appeared
   
3. **Design your Banner:**
   - Use the drag-and-drop editor to recreate your Content Card content
   - For Classic cards: Add a text block for title and description
   - For Captioned Image: Add an image block above text blocks
   - For Image Only: Add a full-width image block
   
4. **Configure on-click behavior:**
   - Set up links, deep links, or custom events as needed
   - Note: You can set different actions for different elements within the Banner
   
5. **Add custom properties** (if you used key-value pairs):
   - Go to **Settings** > **Properties** > **Add property**
   - Recreate each key-value pair as a custom property
   
6. **Set campaign duration:**
   - Unlike Content Cards (max 30 days), you can set any duration
   - For indefinite campaigns, don't set an end time
   
7. **Configure targeting:**
   - Recreate your segment and filter criteria
   
8. **Set priority:**
   - If multiple Banners share the same placement, set priority levels

### Step 5: Test Your Banners

1. **Preview in the composer:**
   - Select **Preview** to see how your Banner will appear
   - Test different viewport sizes
   
2. **Send a test message:**
   - Add yourself as a test recipient
   - Select **Send Test**
   - View the test Banner on your device
   
3. **Verify checklist:**
   - [ ] Banner displays at the correct placement
   - [ ] Images and media render correctly
   - [ ] Links and buttons work as expected
   - [ ] Liquid personalization renders correctly
   - [ ] Copy is clear and correct

### Step 6: Launch and Monitor

1. **Launch your Banner campaign**
2. **Archive or stop your corresponding Content Card campaign**
3. **Monitor analytics:**
   - Compare impressions, clicks, and conversions between old and new campaigns
   - Verify data is tracking correctly

---

## Common Pitfalls & How to Avoid Them

### ❌ Pitfall 1: Expecting Banners to work like a feed

**Problem:** Assuming users can scroll through multiple Banners at one placement.

**Solution:** Banners display ONE message per placement. If you need a feed-like experience, create multiple placements or consider whether Banners are the right fit.

---

### ❌ Pitfall 2: Forgetting to coordinate with engineering

**Problem:** Creating Banner campaigns before placements are integrated into the app.

**Solution:** Your Banner campaign requires a valid placement ID that exists in your app. Work with your engineering team to create and test placements BEFORE designing campaigns.

---

### ❌ Pitfall 3: Using action-based triggers

**Problem:** Trying to trigger Banners based on user actions (like Content Cards can).

**Solution:** Banners use scheduled delivery with segment-based targeting. For action-based behavior, use segmentation to target users who have performed specific actions, combined with priority settings.

**Example:** Instead of triggering a Banner when a user adds to cart, target a segment of "users who added to cart" and set a higher priority than your general Banner.

---

### ❌ Pitfall 4: Expecting user dismissal

**Problem:** Users complain they can't dismiss a Banner.

**Solution:** Banners are not user-dismissible by design. Control visibility through:
- Campaign end dates
- Segment eligibility (remove users who complete an action)
- Frequency of session refreshes

---

### ❌ Pitfall 5: Not setting priorities for competing campaigns

**Problem:** Multiple Banners target the same placement, but the wrong one displays.

**Solution:** Always set explicit priorities when multiple campaigns share a placement. Use the drag-and-drop priority sorter in the campaign settings.

---

### ❌ Pitfall 6: Using Connected Content or promotional codes

**Problem:** Your Content Card uses Connected Content or promotional codes, which Banners don't support.

**Solution:** 
- For Connected Content: Use Liquid personalization with user attributes or catalog items (note: `:rerender` tag not supported)
- For promotional codes: Consider alternative approaches or continue using Content Cards for this use case

---

## FAQ

### Can I use Banners in Canvas?

**No.** Banners currently support campaigns only, not Canvas. If you have Content Cards in Canvas steps, you'll need to keep using Content Cards for those journeys or restructure them as standalone campaigns.

### What happens if a user qualifies for multiple Banners at the same placement?

The highest-priority Banner is displayed. If multiple Banners have the same priority, the newest eligible Banner is shown.

### Can users dismiss Banners?

No. Unlike Content Cards, Banners cannot be dismissed by users. Control visibility through segment eligibility and campaign scheduling.

### Do Banners support animated GIFs?

Yes. The Banner editor supports GIF uploads.

### What's the maximum number of active Banner campaigns?

Each workspace supports up to 200 active Banner campaigns.

### How do I migrate my Content Card carousel?

Carousels were custom implementations for Content Cards. For Banners, consider:
- Creating multiple placements for a multi-message experience
- Using a single placement with rotating priority campaigns
- Working with your engineering team on custom carousel logic

### Can I still use Content Cards?

Yes! Content Cards and Banners serve different use cases. You can use both. Content Cards are ideal for:
- Message inboxes and notification centers
- Feed-based experiences
- Canvas integrations
- API-triggered messaging
- Action-based campaigns

### When should I NOT migrate to Banners?

Keep using Content Cards when you need:
- Canvas integration
- API-triggered delivery
- Action-based triggers
- User-dismissible messages
- A scrollable feed of messages
- Connected Content
- Promotional codes

---

# Developer Guide

> This section is designed for engineering teams implementing the migration from Content Cards to Banners.

## Overview

### Architecture Differences

**Content Cards Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                     Braze Dashboard                          │
│  (Campaign with card type: Classic/Captioned/Image Only)     │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Braze SDK                               │
│         subscribeToContentCardsUpdates()                     │
│         requestContentCardsRefresh()                         │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Custom UI Code                            │
│      ContentCardsFragment / BrazeContentCardUI.ViewController│
│           (Manual impression/click logging)                  │
└─────────────────────────────────────────────────────────────┘
```

**Banners Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                     Braze Dashboard                          │
│        (Campaign assigned to Placement ID)                   │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Braze SDK                               │
│              subscribeToBannersUpdates()                     │
│              requestBannersRefresh()                         │
│                   getBanner()                                │
│                  insertBanner()                              │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                Container Element / View                      │
│   (BannerView / BrazeBannerUI.BannerUIView / <div>)         │
│          (Auto impression/click logging via SDK)             │
└─────────────────────────────────────────────────────────────┘
```

### SDK/API Differences

| Feature | Content Cards | Banners |
|---------|---------------|---------|
| **Subscribe Method** | `subscribeToContentCardsUpdates()` | `subscribeToBannersUpdates()` |
| **Refresh Method** | `requestContentCardsRefresh()` | `requestBannersRefresh(placementIds)` |
| **Get Data** | `getCachedContentCards()` / callback | `getBanner(placementId)` |
| **Display Method** | Custom UI required | `insertBanner()` / `BannerView` / `BrazeBannerUI` |
| **Impression Logging** | Manual: `logImpression()` | Automatic when using SDK insert methods |
| **Click Logging** | Manual: `logClick()` | Automatic for elements with on-click actions |
| **Dismissal** | `logDismissed()` / `isDismissed` | N/A - not user-dismissible |
| **Control Variants** | `isControl` flag | `isControl` flag |
| **Extra Data** | `extras` (key-value pairs) | Custom properties via getters |

### Data Model Differences

**Content Card Data Model:**

```javascript
// Content Card (Web)
{
  id: string,
  viewed: boolean,
  title: string,
  description: string,
  imageUrl: string,
  url: string,
  linkText: string,
  extras: { key: value, ... },  // Key-value pairs
  created: Date,
  updated: Date,
  expiresAt: Date,
  pinned: boolean,
  dismissible: boolean,
  isControl: boolean
}
```

**Banner Data Model:**

```javascript
// Banner (Web)
{
  placementId: string,
  html: string,                  // Rendered HTML content
  isControl: boolean,
  // Custom properties accessed via methods:
  getStringProperty(key): string,
  getBooleanProperty(key): boolean,
  getNumberProperty(key): number,
  getTimestampProperty(key): number,
  getImageProperty(key): string,
  getJsonProperty(key): object
}
```

---

## Code Changes Required

### Minimum SDK Versions

Before migrating, ensure your apps meet these minimum SDK requirements:

| Platform | Minimum Version for Banners |
|----------|----------------------------|
| Swift | 11.3.0 |
| Android | 33.1.0 |
| Web | 5.8.1 |
| React Native | 14.0.0 |
| Flutter | 13.0.0 |

> **Note:** For custom properties support, additional versions required:
> - Swift: 13.1.0+
> - Android: 38.0.0+
> - Web: 6.1.0+
> - React Native: 17.0.0+
> - Flutter: 15.1.0+

---

### Web SDK Migration

#### Before (Content Cards)

```javascript
import * as braze from "@braze/web-sdk";

// Initialize
braze.initialize("YOUR_API_KEY", {
  baseUrl: "YOUR_ENDPOINT",
});

// Subscribe to Content Card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  
  cards.forEach(card => {
    // Skip control cards in UI
    if (card.isControl) {
      braze.logContentCardImpressions([card]);
      return;
    }
    
    // Build custom UI
    const element = document.createElement('div');
    element.innerHTML = `
      <h3>${card.title}</h3>
      <p>${card.description}</p>
      ${card.imageUrl ? `<img src="${card.imageUrl}">` : ''}
    `;
    
    // Manual impression logging
    braze.logContentCardImpressions([card]);
    
    // Manual click handling
    element.addEventListener('click', () => {
      braze.logContentCardClick(card);
      if (card.url) window.open(card.url);
    });
    
    document.getElementById('feed-container').appendChild(element);
  });
});

braze.requestContentCardsRefresh();
```

#### After (Banners)

```javascript
import * as braze from "@braze/web-sdk";

// Initialize - IMPORTANT: Enable user-supplied JavaScript for Banners
braze.initialize("YOUR_API_KEY", {
  baseUrl: "YOUR_ENDPOINT",
  allowUserSuppliedJavascript: true,  // Required for Banners
});

// Subscribe to Banner updates
braze.subscribeToBannersUpdates((banners) => {
  // Get the specific placement's banner
  const homepageBanner = braze.getBanner("homepage_hero");
  
  if (!homepageBanner) {
    // User didn't qualify for any banner at this placement
    return;
  }
  
  // Get the container element
  const container = document.getElementById("homepage-banner-container");
  
  // Insert the banner - impressions logged automatically!
  braze.insertBanner(homepageBanner, container);
  
  // Handle control variants
  if (homepageBanner.isControl) {
    container.style.display = "none";
  }
  
  // Access custom properties (if needed)
  const backgroundColor = homepageBanner.getStringProperty("background_color");
  const showAnimation = homepageBanner.getBooleanProperty("animate");
});

// Request banners for specific placements
braze.requestBannersRefresh(["homepage_hero", "checkout_promo"]);
```

#### HTML Changes

```html
<!-- Before: Content Card Feed Container -->
<div id="feed-container"></div>

<!-- After: Banner Placement Container -->
<div id="homepage-banner-container" style="width: 100%; height: 450px;"></div>
```

---

### Android SDK Migration

#### Before (Content Cards - Kotlin)

```kotlin
class ContentCardsActivity : AppCompatActivity() {
    private var subscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Subscribe to Content Card updates
        subscriber = IEventSubscriber { event ->
            val cards = event.allCards
            
            cards.forEach { card ->
                if (card.isControl) {
                    card.logImpression()
                    return@forEach
                }
                
                // Manual impression logging
                card.logImpression()
                
                // Build custom UI with card data
                when (card) {
                    is CaptionedImageCard -> {
                        displayCaptionedImage(card.title, card.description, card.imageUrl)
                    }
                    is ShortNewsCard -> {
                        displayClassicCard(card.title, card.description)
                    }
                }
            }
        }
        
        Braze.getInstance(this).subscribeToContentCardsUpdates(subscriber)
        Braze.getInstance(this).requestContentCardsRefresh()
    }
}
```

#### After (Banners - Kotlin)

**Option 1: XML Layout (Recommended)**

```xml
<!-- res/layout/activity_main.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <!-- Banner will render here automatically -->
    <com.braze.ui.banners.BannerView
        android:id="@+id/homepage_banner"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:placementId="homepage_hero" />

</LinearLayout>
```

**Option 2: Programmatic (Kotlin)**

```kotlin
class BannersActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Subscribe to Banner updates
        Braze.getInstance(this).subscribeToBannersUpdates { update ->
            for (banner in update.banners) {
                Log.d("Banners", "Received banner: ${banner.placementId}")
                
                // Handle control variant
                if (banner.isControl) {
                    // Hide the container for this placement
                }
                
                // Access custom properties
                val bgColor = banner.getStringProperty("background_color")
                val showAnimation = banner.getBooleanProperty("animate")
            }
        }
        
        // Request banners for specific placements
        Braze.getInstance(this).requestBannersRefresh(
            listOf("homepage_hero", "checkout_promo")
        )
    }
}
```

**Option 3: Jetpack Compose**

```kotlin
@Composable
fun HomepageScreen() {
    Column {
        // Banner composable - handles everything automatically
        Banner(placementId = "homepage_hero")
        
        // Rest of your UI
        Text("Welcome to our app!")
    }
}
```

---

### Swift SDK Migration

#### Before (Content Cards)

```swift
class ContentCardsViewController: UIViewController {
    private var cancellable: Braze.Cancellable?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Subscribe to Content Card updates
        cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] cards in
            for card in cards {
                if card.isControl {
                    card.logImpression(using: AppDelegate.braze!)
                    continue
                }
                
                // Manual impression logging
                card.logImpression(using: AppDelegate.braze!)
                
                // Build custom UI
                self?.displayCard(
                    title: card.title,
                    description: card.description,
                    imageUrl: card.imageURL
                )
            }
        }
        
        // Request refresh
        AppDelegate.braze?.contentCards.requestRefresh()
    }
}
```

#### After (Banners - SwiftUI)

```swift
import SwiftUI
import BrazeKit
import BrazeBannerUI

struct HomepageView: View {
    var body: some View {
        VStack {
            // Banner view - handles display and analytics automatically
            if let braze = AppDelegate.braze {
                BrazeBannerUI.BannerView(
                    placementId: "homepage_hero",
                    braze: braze,
                    processContentUpdates: { result in
                        switch result {
                        case .success(let updates):
                            if let height = updates.height {
                                // Adjust view height if needed
                            }
                        case .failure(let error):
                            // Handle error
                            print("Banner error: \(error)")
                        }
                    }
                )
            }
            
            // Rest of your UI
            Text("Welcome to our app!")
        }
    }
}
```

#### After (Banners - UIKit)

```swift
class BannersViewController: UIViewController {
    private var bannerView: BrazeBannerUI.BannerUIView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let braze = AppDelegate.braze else { return }
        
        // Create and add banner view
        bannerView = BrazeBannerUI.BannerUIView(
            placementId: "homepage_hero",
            braze: braze,
            processContentUpdates: { [weak self] result in
                switch result {
                case .success(let updates):
                    if let height = updates.height {
                        self?.updateBannerHeight(height)
                    }
                case .failure(let error):
                    print("Banner error: \(error)")
                }
            }
        )
        
        if let bannerView = bannerView {
            view.addSubview(bannerView)
            // Set up constraints...
        }
        
        // Request banner refresh
        braze.banners.requestRefresh(placementIds: ["homepage_hero"])
    }
}
```

---

### React Native Migration

#### Before (Content Cards)

```javascript
import Braze from "@braze/react-native-sdk";

// Subscribe to Content Cards
const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (data) => {
    const cards = data.cards;
    cards.forEach(card => {
      // Manual logging required
      Braze.logContentCardImpression(card.id);
    });
  }
);

// Request refresh
Braze.requestContentCardsRefresh();
```

#### After (Banners)

```javascript
import Braze, { BrazeBannerView } from "@braze/react-native-sdk";

// In your component
function HomepageScreen() {
  return (
    <View>
      {/* Banner view - handles display and analytics automatically */}
      <BrazeBannerView
        placementID="homepage_hero"
        style={{ width: '100%', height: 200 }}
      />
      
      <Text>Welcome to our app!</Text>
    </View>
  );
}

// If you need to access banner data programmatically
async function getBannerData() {
  const banner = await Braze.getBanner("homepage_hero");
  if (banner) {
    const bgColor = banner.getStringProperty("background_color");
    const animate = banner.getBooleanProperty("animate");
  }
}

// Subscribe to banner updates
const bannerSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(`Received ${banners.length} banners`);
  }
);

// Request refresh for specific placements
Braze.requestBannersRefresh(["homepage_hero", "checkout_promo"]);
```

---

### Flutter Migration

#### Before (Content Cards)

```dart
import 'package:braze_plugin/braze_plugin.dart';

// Subscribe to Content Cards
StreamSubscription contentCardsSubscription = 
    braze.subscribeToContentCards((List<BrazeContentCard> cards) {
  for (final card in cards) {
    // Manual logging
    braze.logContentCardImpression(card);
  }
});

// Request refresh
braze.requestContentCardsRefresh();
```

#### After (Banners)

```dart
import 'package:braze_plugin/braze_plugin.dart';

// In your widget
class HomepageScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Banner widget - handles display and analytics automatically
        BrazeBannerView(
          placementId: "homepage_hero",
        ),
        
        Text("Welcome to our app!"),
      ],
    );
  }
}

// Subscribe to banner updates
StreamSubscription bannerSubscription = 
    braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: ${banner.placementId}");
  }
});

// Access banner data programmatically
braze.getBanner("homepage_hero").then((banner) {
  if (banner != null) {
    final bgColor = banner.getStringProperty("background_color");
    final animate = banner.getBooleanProperty("animate");
  }
});

// Request refresh for specific placements
braze.requestBannersRefresh(["homepage_hero", "checkout_promo"]);
```

---

## Migration Checklist

### Pre-Migration

- [ ] Verify SDK versions meet minimum requirements for Banners
- [ ] Audit all existing Content Card implementations
- [ ] Document current Content Card placements and use cases
- [ ] Identify any Content Cards using:
  - [ ] API-triggered delivery (NOT supported in Banners)
  - [ ] Action-based delivery (NOT supported in Banners)
  - [ ] Canvas integration (NOT supported in Banners)
  - [ ] Connected Content (NOT supported in Banners)
  - [ ] Promotional codes (NOT supported in Banners)

### Implementation

- [ ] Create placement IDs in Braze dashboard (**Settings** > **Banners Placements**)
- [ ] Update SDK initialization (Web: add `allowUserSuppliedJavascript: true`)
- [ ] Replace Content Card subscription code with Banner subscription
- [ ] Replace Content Card UI components with Banner components
- [ ] Update refresh calls from `requestContentCardsRefresh()` to `requestBannersRefresh()`
- [ ] Remove manual impression logging (Banners auto-log when using SDK methods)
- [ ] Replace key-value pair access (`extras`) with custom property getters
- [ ] Handle control variants appropriately

### Testing

- [ ] Test each placement renders correctly
- [ ] Verify impression tracking in Braze analytics
- [ ] Verify click tracking in Braze analytics
- [ ] Test control variant handling (banner hidden, impression still logged)
- [ ] Test priority ordering when multiple campaigns target same placement
- [ ] Test session refresh behavior
- [ ] Test on all supported platforms

### Post-Migration

- [ ] Archive or stop old Content Card campaigns
- [ ] Monitor analytics for parity with previous implementation
- [ ] Remove legacy Content Card code (if no longer needed)
- [ ] Update documentation

---

## Testing & Validation Guide

### QA Steps

#### 1. Verify Placement Creation

```javascript
// Web: Check placements are registered
braze.subscribeToBannersUpdates((banners) => {
  console.log("Banner placements received:", Object.keys(banners));
});
braze.requestBannersRefresh(["your_placement_id"]);
```

#### 2. Verify Banner Display

1. Create a test Banner campaign targeting yourself
2. Assign it to your placement
3. Launch the campaign
4. Open your app and verify the Banner displays

#### 3. Verify Analytics

1. **Impressions**: Check Braze dashboard shows impression count
2. **Clicks**: Click a Banner element with on-click action; verify in dashboard
3. **Control variants**: Test a campaign with control group; verify control impressions log

### Expected Console Output

**Web SDK (with logging enabled):**

```
[Braze] INFO: Requesting banners refresh for placements: ["homepage_hero"]
[Braze] INFO: Received banners update with 1 banners
[Braze] INFO: Banner impression logged for placement: homepage_hero
```

**Android (with verbose logging):**

```
D/Braze: Requesting banners refresh for placements: [homepage_hero]
D/Braze: Received 1 banners from server
D/Braze: Banner view displayed for placement: homepage_hero
```

### Error Scenarios to Test

| Scenario | Expected Behavior |
|----------|------------------|
| Invalid placement ID | No banner returned; no crash |
| User not eligible for any banner | `getBanner()` returns `null` |
| Network error during refresh | Cached banners displayed (if available) |
| Rate limit exceeded | Request not sent; error logged |
| Control variant | `isControl` = true; hide container but log impression |

### Rate Limit Testing

Banners have refresh rate limits:

- **5 tokens** at session start
- **1 token** refills every 180 seconds (3 minutes)
- Each `requestBannersRefresh()` call consumes 1 token

Test by calling refresh multiple times and verifying rate limit errors appear after 5 calls.

---

## Deprecation Notes

### What Must Be Removed

When fully migrating to Banners, remove the following Content Card-specific code:

| Remove | Replacement |
|--------|-------------|
| `subscribeToContentCardsUpdates()` | `subscribeToBannersUpdates()` |
| `requestContentCardsRefresh()` | `requestBannersRefresh([placementIds])` |
| `getCachedContentCards()` | `getBanner(placementId)` |
| `logContentCardImpressions()` | Auto-logged by SDK |
| `logContentCardClick()` | Auto-logged by SDK |
| `logCardDismissal()` | N/A - not supported |
| `ContentCardsFragment` | `BannerView` (Android) |
| `BrazeContentCardUI.ViewController` | `BrazeBannerUI.BannerView` (iOS) |
| `showContentCards()` | `insertBanner()` (Web) |
| Card type handlers (`ClassicCard`, etc.) | Single Banner type |

### Keep Content Cards If...

You should continue using Content Cards (alongside or instead of Banners) if you need:

- Canvas integration
- API-triggered delivery
- Action-based campaign triggers
- User-dismissible messages
- A scrollable feed/inbox experience
- Connected Content
- Promotional code distribution

### Timeline

As of the documentation date, there is no announced deprecation timeline for Content Cards. Both Content Cards and Banners are actively supported. Check with your Braze account team for the latest roadmap information.

---

## Examples Section

### Before/After: Homepage Promotional Banner

#### Before (Content Cards)

```javascript
// Content Card implementation
braze.subscribeToContentCardsUpdates((updates) => {
  const promoCard = updates.cards.find(
    card => card.extras?.placement === 'homepage_promo'
  );
  
  if (!promoCard) return;
  
  const container = document.getElementById('promo-container');
  container.innerHTML = `
    <div class="promo-card" style="background: ${promoCard.extras?.bg_color || '#fff'}">
      <img src="${promoCard.imageUrl}" alt="${promoCard.title}">
      <h2>${promoCard.title}</h2>
      <p>${promoCard.description}</p>
      <a href="${promoCard.url}">${promoCard.linkText}</a>
    </div>
  `;
  
  // Manual impression logging
  braze.logContentCardImpressions([promoCard]);
  
  // Manual click logging
  container.querySelector('a').addEventListener('click', () => {
    braze.logContentCardClick(promoCard);
  });
});

braze.requestContentCardsRefresh();
```

#### After (Banners)

```javascript
// Banner implementation - much simpler!
braze.subscribeToBannersUpdates(() => {
  const promoBanner = braze.getBanner("homepage_promo");
  
  if (!promoBanner) return;
  
  const container = document.getElementById('promo-container');
  
  // Insert banner - impressions and clicks logged automatically!
  braze.insertBanner(promoBanner, container);
  
  if (promoBanner.isControl) {
    container.style.display = 'none';
  }
});

braze.requestBannersRefresh(["homepage_promo"]);
```

### Before/After: Android Notification Center

#### Before (Content Cards)

```kotlin
class NotificationCenterFragment : Fragment() {
    private val cards = mutableListOf<Card>()
    private var subscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        subscriber = IEventSubscriber { event ->
            requireActivity().runOnUiThread {
                cards.clear()
                cards.addAll(event.allCards.filter { 
                    it.extras["feed_type"] == "notification_center" 
                })
                adapter.notifyDataSetChanged()
                
                // Manual impression logging for visible cards
                cards.forEach { card ->
                    if (!card.viewed) {
                        card.logImpression()
                    }
                }
            }
        }
        
        Braze.getInstance(requireContext()).subscribeToContentCardsUpdates(subscriber!!)
        Braze.getInstance(requireContext()).requestContentCardsRefresh()
    }
    
    // ... lots more code for RecyclerView adapter, click handling, etc.
}
```

#### After (Banners)

```kotlin
class NotificationCenterFragment : Fragment() {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        // That's it! The BannerView in the layout handles everything
        Braze.getInstance(requireContext()).requestBannersRefresh(
            listOf("notification_center_banner")
        )
    }
}
```

```xml
<!-- fragment_notification_center.xml -->
<com.braze.ui.banners.BannerView
    android:id="@+id/notification_banner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="notification_center_banner" />
```

### Before/After: iOS SwiftUI Integration

#### Before (Content Cards)

```swift
struct ContentCardsFeed: View {
    @State private var cards: [Braze.ContentCard] = []
    
    var body: some View {
        ScrollView {
            ForEach(cards, id: \.id) { card in
                ContentCardView(card: card)
                    .onAppear {
                        // Manual impression logging
                        card.logImpression(using: AppDelegate.braze!)
                    }
                    .onTapGesture {
                        // Manual click logging
                        card.logClick(using: AppDelegate.braze!)
                    }
            }
        }
        .onAppear {
            AppDelegate.braze?.contentCards.subscribeToUpdates { updatedCards in
                self.cards = updatedCards
            }
            AppDelegate.braze?.contentCards.requestRefresh()
        }
    }
}

struct ContentCardView: View {
    let card: Braze.ContentCard
    
    var body: some View {
        VStack {
            if let imageUrl = card.imageURL {
                AsyncImage(url: imageUrl)
            }
            Text(card.title ?? "")
            Text(card.description ?? "")
        }
    }
}
```

#### After (Banners)

```swift
struct HomepageView: View {
    var body: some View {
        VStack {
            // Single line replaces all the Content Card code!
            if let braze = AppDelegate.braze {
                BrazeBannerUI.BannerView(
                    placementId: "homepage_hero",
                    braze: braze
                )
            }
        }
    }
}
```

---

## Needs Clarification

The following items were not explicitly documented and may require clarification from your Braze account team:

1. **Migration Tools**: Are there any automated migration tools or scripts to convert Content Card campaigns to Banner campaigns?

2. **Analytics Continuity**: When migrating from Content Cards to Banners, how should historical analytics be handled for reporting purposes?

3. **Deprecation Timeline**: Is there a planned deprecation date for Content Cards, or will both channels continue to be supported indefinitely?

4. **A/B Testing**: Can Banners be used in multivariate tests the same way Content Cards can?

5. **Segmentation Filters**: Are there Banner-specific segmentation filters (similar to "Has Received Content Card from Campaign")?

6. **Unity/Cordova/Roku Support**: These platforms show "not currently supported" for Banners in the documentation. Is support planned?

7. **Rate Limit Customization**: Can the Banner refresh rate limits be customized for high-frequency use cases?

8. **Connected Content Workarounds**: For customers heavily using Connected Content in Content Cards, what are the recommended alternatives for Banners?

---

## Support Resources

- **Braze Documentation**: [https://www.braze.com/docs/](https://www.braze.com/docs/)
- **Banners User Guide**: [https://www.braze.com/docs/user_guide/message_building_by_channel/banners/](https://www.braze.com/docs/user_guide/message_building_by_channel/banners/)
- **Banners Developer Guide**: [https://www.braze.com/docs/developer_guide/banners/](https://www.braze.com/docs/developer_guide/banners/)
- **Banner Feedback**: [banners-feedback@braze.com](mailto:banners-feedback@braze.com)
- **Braze Support**: Contact your account manager or customer success manager

---

*This migration guide was generated based on the Braze documentation. For the most current information, always refer to the official Braze documentation.*
