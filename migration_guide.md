# Migration Guide: Content Cards → Banners

**Last Updated:** December 9, 2025

---

# User Guide

## Introduction

### What is changing and why

Braze is introducing **Banners** as the next evolution for inline, persistent in-app and web messaging. If you've been using Content Cards for banner-style messages (such as homepage promotions, announcements, or persistent offers), Banners provides a more streamlined and purpose-built solution.

**Why Banners?**
- **Simpler implementation:** No need to manage a feed—Banners are tied to specific placements in your app or website
- **Better performance:** Banners are optimized for inline, persistent display
- **More control:** Priority-based display when multiple campaigns target the same placement
- **Modern editor:** Drag-and-drop composer with support for email capture forms, custom code, and more
- **Dynamic updates:** Content refreshes automatically at the start of each session without requiring campaign resends

### High-level summary of the new workflow

With Content Cards, you created cards that lived in a dismissible feed. Users could scroll through multiple cards, dismiss them, and interact with them in a centralized location.

With Banners, you create placements (specific locations in your app or website), then assign Banner campaigns to those placements. Each placement displays one high-priority Banner at a time, inline with your content. Banners are non-dismissible by users and update dynamically based on user eligibility.

---

## Before You Begin

### Prerequisites

- **Developer coordination required:** Your development team must create placements in your app or website before you can launch Banner campaigns
- **Banners package:** Confirm with your Braze account manager that Banners are included in your package
- **SDK requirements:** Verify your SDK meets minimum version requirements (see Developer Guide)
- **Understanding user segments:** Banners are evaluated at session start, so timing of user attribute changes matters

### What you need to understand about Banners

1. **Banners are placement-based, not feed-based**  
   Each Banner is assigned to a specific placement ID that your developers create (e.g., `homepage_banner`, `checkout_promo`)

2. **Banners display by priority**  
   When multiple campaigns target the same placement, the highest-priority Banner (High > Medium > Low) is shown

3. **Users cannot dismiss Banners**  
   Unlike Content Cards, Banners stay visible until the user no longer qualifies for them based on your targeting

4. **Banners refresh at session start**  
   New Banner content appears when users start a new session or when developers call the refresh method

5. **Workspace limits**  
   Each workspace supports up to 200 active Banner campaigns (vs. unlimited Content Card campaigns)

---

## Concept Mapping: Content Cards → Banners

| Content Cards | Banners | Notes |
|--------------|---------|-------|
| **Feed** | **Placements** | Content Cards live in a feed; Banners are tied to specific placement IDs |
| **Card Types** (Classic, Captioned Image, Image Only) | **Drag-and-drop editor** | Banners use a visual editor instead of predefined card types |
| **Key-Value Pairs** | **Custom Properties** | Banners use typed custom properties (string, boolean, number, timestamp, image URL, JSON) |
| **Multiple cards in feed** | **One Banner per placement** | Each placement shows only the highest-priority eligible Banner |
| **User-dismissible** | **Non-dismissible** | Users cannot manually dismiss Banners; removal is segment-based |
| **Feed refresh** | **Placement refresh** | Different SDK methods for refreshing content |
| **Pinned cards** | **Priority levels** | Banners use High/Medium/Low priority instead of pinning |
| **Up to 250 cards per user** | **Up to 10 placements per refresh** | Different content limits |
| **30-day expiration max** | **Indefinite duration** | Banners can run longer than 30 days |
| **Canvas support** | **No Canvas support** | Banners only support campaigns (not Canvas) |
| **Action-based delivery** | **Scheduled delivery only** | Banners don't support action-based or API-triggered campaigns |

---

## Side-by-Side Workflow Comparison

### Creating a message campaign

#### How you did it in Content Cards

1. Go to **Messaging** > **Campaigns** > **Create Campaign**
2. Select **Content Cards**
3. Choose a card type: Classic, Captioned Image, or Image Only
4. Compose your card:
   - Add title and message text
   - Upload an image
   - Set on-click behavior
   - Optionally pin the card to top of feed
5. Add key-value pairs for custom data (optional)
6. Choose delivery schedule (scheduled, action-based, or API-triggered)
7. Target your audience with segments and filters
8. Launch campaign

Cards appeared in users' feed at next refresh, could be dismissed, and expired after up to 30 days.

#### How you will do it in Banners

1. **First time only:** Ask your developer to create placement IDs (e.g., `homepage_banner`, `cart_promo`)
2. Go to **Messaging** > **Campaigns** > **Create Campaign**
3. Select **Banner**
4. Select the placement you want to use
5. Compose your Banner using the drag-and-drop editor:
   - Drag blocks (text, images, buttons, email capture forms) onto canvas
   - Style your Banner using the Styles panel
   - Set on-click behavior (optional)
   - Add custom properties with typed values (optional)
6. Set campaign duration (start date/time, optional end date/time)
7. Set Banner priority: High, Medium, or Low (default is Medium)
8. Target your audience with segments and filters
9. Launch campaign

Banners appear at the assigned placement location at the start of the next user session.

#### What becomes easier

✅ **No feed UI to manage** – Banners render inline exactly where you want them  
✅ **Better control** – Priority system ensures the right message displays when multiple campaigns compete  
✅ **More creative freedom** – Drag-and-drop editor with custom HTML support  
✅ **Longer campaigns** – No 30-day expiration limit  
✅ **Automatic updates** – Edit and relaunch campaigns; users see updates at next session  

#### What requires more planning

⚠️ **Developer dependency** – Must coordinate with developers to create placements first  
⚠️ **No Canvas integration** – Must use campaigns only  
⚠️ **No action-based triggers** – Can't trigger display based on user actions in real-time  
⚠️ **Campaign limit** – Maximum 200 active Banner campaigns per workspace  

---

## Step-by-Step Migration Instructions

### Step 1: Audit your existing Content Cards

Before migrating, answer these questions:

1. **Which Content Cards are banner-style messages?**  
   Look for cards used for homepage promotions, top-of-page announcements, or persistent inline messages

2. **How are you using key-value pairs?**  
   Document any `feed_type` or placement-specific key-value pairs you're using to control where cards appear

3. **Do you use action-based or API-triggered Content Cards?**  
   ⚠️ These cannot be directly migrated; you'll need to use scheduled campaigns with segment targeting instead

4. **Are you using Content Cards in Canvas?**  
   ⚠️ Banners don't support Canvas; you'll need to convert these to standalone campaigns

### Step 2: Plan your placements

Work with your development team to identify placement locations:

**Example placement mapping:**

| Current Content Card Use Case | Suggested Banner Placement ID | Location |
|------------------------------|-------------------------------|----------|
| Homepage hero card | `homepage_hero` | Top of homepage |
| Product page promo | `product_page_banner` | Below product title |
| Checkout abandonment message | `checkout_banner` | Top of checkout page |
| Account dashboard announcement | `account_dashboard` | Top of dashboard |

**Planning tips:**
- Use descriptive, lowercase placement IDs with underscores (e.g., `navigation_promo`)
- Create separate placements for desktop vs. mobile if content differs
- Plan for 1-3 campaigns per placement to leverage priority system
- Document placement dimensions for your designers

### Step 3: Coordinate with your development team

**What to communicate to developers:**

1. **Placement IDs needed:** Provide your list of placement IDs
2. **Timeline:** When you need placements ready for testing
3. **Dimensions:** Expected width/height for each placement
4. **Refresh strategy:** When placements should refresh (session start vs. specific events)

**What developers need to do:** See Developer Guide below for technical implementation details.

### Step 4: Recreate your campaigns

For each Content Card you're migrating:

1. **Create a new Banner campaign** (do not stop your Content Card yet)
2. **Compose your Banner:**
   - Use the drag-and-drop editor to recreate your card's visual design
   - If you had a Classic card with image/text, add Image and Text blocks
   - If you had a Captioned Image card, add a large Image block with Text below
   - If you had an Image Only card, add just an Image block
3. **Migrate key-value pairs to custom properties:**
   - Review your existing key-value pairs
   - Convert them to typed custom properties (string, boolean, number, etc.)
   - Document property keys for your developers
4. **Set priority:**
   - If your card was pinned, set priority to High
   - For general cards, use Medium
   - For low-priority evergreen content, use Low
5. **Migrate targeting:**
   - Use the same segments and filters
   - ⚠️ Note: Banners are evaluated at session start, not at display time
6. **Set duration:**
   - Keep the same start date
   - Banners can run indefinitely (no 30-day limit)

### Step 5: Test your Banners

**Before launching to all users:**

1. **Send test Banners** using the test device feature:
   - Add your test user ID
   - Send test to verify rendering
   - Confirm placement location and sizing
2. **Test on all platforms** (web, iOS, Android) where placements exist
3. **Verify analytics** are tracking:
   - Impressions logging correctly
   - Clicks logging correctly
   - Conversions tracking as expected
4. **Test priority** if multiple Banners target the same placement:
   - Launch a High priority Banner
   - Launch a Medium priority Banner to same placement
   - Confirm High priority displays first

### Step 6: Launch and monitor

**Soft launch approach:**

1. **Launch to a small segment first** (e.g., 5% of users or internal team)
2. **Monitor for 24-48 hours:**
   - Check impression rates
   - Verify no rendering issues
   - Review user feedback
3. **Gradually expand** to larger audiences
4. **Compare performance** to previous Content Card campaigns

**When to stop your Content Card:**

- ✅ After verifying Banner is rendering correctly
- ✅ After confirming analytics are tracking
- ✅ When majority of users have started new sessions (so they see the Banner)

**How to stop Content Card:**
1. Go to your Content Card campaign
2. Select **Stop Campaign**
3. Choose **Remove card from feed** to hide from users' feeds

---

## Common Pitfalls & How to Avoid Them

### ❌ Pitfall 1: Launching before developers create placements
**Symptom:** Campaign created but cannot launch; "placement not found" errors  
**Solution:** Always confirm placements exist and are tested before creating campaigns  
**Prevention:** Use a shared tracking sheet with developers to document placement readiness

### ❌ Pitfall 2: Setting unrealistic dimensions
**Symptom:** Banners render too large/small; content is cut off  
**Solution:** Test dimensions in the composer preview, coordinate with developers on container sizes  
**Prevention:** Document standard dimension guidelines for each placement type

### ❌ Pitfall 3: Forgetting about priority
**Symptom:** Wrong Banner displays when multiple campaigns are active  
**Solution:** Use priority sorter to manually order campaigns targeting the same placement  
**Prevention:** Create a priority strategy document (e.g., "Flash sales = High, General promos = Medium")

### ❌ Pitfall 4: Not accounting for session-based refresh
**Symptom:** Users don't see new Banners immediately after qualifying  
**Solution:** Understand that Banners refresh at session start, not in real-time  
**Prevention:** Communicate timing expectations to stakeholders; consider push notifications to drive re-engagement

### ❌ Pitfall 5: Exceeding workspace limits
**Symptom:** Cannot create new Banner campaign; "200 campaign limit reached" error  
**Solution:** Archive or stop old Banner campaigns  
**Prevention:** Regularly audit and clean up inactive campaigns

### ❌ Pitfall 6: Using action-based logic
**Symptom:** Expecting Banners to appear after user completes an action  
**Solution:** Use segments (e.g., "completed purchase at least once") and rely on priority to show different Banners  
**Prevention:** During planning, identify action-based Content Cards and redesign with segment-based logic

### ❌ Pitfall 7: Overly complex Liquid
**Symptom:** Slow Banner rendering; timeouts  
**Solution:** Simplify Liquid logic; avoid complex catalog lookups with `:rerender`  
**Prevention:** Test rendering performance during composition; keep Banner HTML simple

---

## FAQ

### How many placements should I create?

**Start small.** Most apps need 3-5 placements:
- Homepage/main screen
- Product/content detail pages
- Checkout/conversion pages
- Account/settings pages
- Navigation bars

You can always add more placements later.

---

### Can I reuse content from my Content Cards?

**Yes.** You can copy images, text, and messaging from Content Cards into the Banner drag-and-drop editor. However, you'll need to rebuild the layout since Banners don't use the same card types.

---

### What happens to my Content Card analytics?

**Content Card analytics remain separate.** When you create a Banner campaign, it starts fresh analytics. You cannot carry over historical data. Export Content Card reports before stopping campaigns if you need historical records.

---

### Can I test Banners alongside Content Cards?

**Yes.** Banners and Content Cards are separate systems. You can run both simultaneously during migration. However, they cannot share the same UI space—Banners are placement-based and Content Cards live in a feed.

---

### How do I remove a Banner from users' screens?

**Banners are removed by changing user eligibility:**
1. Stop the campaign (users won't see it at next session)
2. Or, adjust targeting so users no longer qualify
3. Or, use segment removal (e.g., after user completes a purchase, exclude them from the segment)

Unlike Content Cards, users cannot manually dismiss Banners.

---

### Can I schedule Banners to appear at specific times of day?

**No.** Banners refresh at session start, not at specific times. If you need time-based display, use campaign scheduling with start/end dates and rely on users starting new sessions during that window.

---

### What if I have more than 200 Banner campaigns?

**Archive inactive campaigns.** The 200-campaign limit applies only to active campaigns. You can have unlimited archived campaigns. Regularly review and archive campaigns that have ended or are no longer needed.

---

### Can I use Banners for transactional messages?

**Not recommended.** Banners refresh at session start and are not real-time. For transactional messages (order confirmations, password resets), continue using email, push, or in-app messages.

---

### Do Banners work on all platforms?

**Minimum SDK versions required:**
- Web SDK: 5.8.1+
- iOS SDK: 11.3.0+
- Android SDK: 33.1.0+
- React Native: 14.0.0+
- Flutter: 13.0.0+

Banners are not yet supported on Unity, Cordova, or Roku.

---

### Can I use Connected Content with Banners?

**No.** Banners do not currently support Connected Content. If you rely on Connected Content in your Content Cards, you'll need to find alternative approaches (e.g., catalog items or hardcoded values).

---

### How do I A/B test Banners?

**Use campaign variants.** Just like with Content Cards, you can create multiple variants of a Banner campaign and Braze will distribute users across variants for testing. Analytics will show performance by variant.

---

### Can I duplicate a Banner campaign?

**Yes.** You can duplicate Banner campaigns just like other campaign types. This is useful when creating similar Banners for different placements or testing variations.

---

---

# Developer Guide

## Overview

This guide provides technical implementation details for migrating from Content Cards to Banners. Banners represent a fundamental shift in architecture: instead of a feed-based model where users can dismiss multiple cards, Banners use a placement-based model where specific locations in your app display one prioritized Banner at a time.

---

## Architecture Differences

### Content Cards Architecture

Content Cards follow a **feed-based** model:
- Multiple cards delivered to a centralized feed
- Users can scroll, dismiss, and interact with multiple cards
- Default UI provided by Braze SDK
- Cards sorted by pinned status and timestamp
- Up to 250 cards per user at any time
- Feed refreshes automatically at session start or after 60 seconds

```
┌─────────────────────────────┐
│    Content Cards Feed UI    │
├─────────────────────────────┤
│  [Card 1: Pinned]           │
│  [Card 2: New]              │
│  [Card 3: Older]            │
│  [Card 4: Oldest]           │
└─────────────────────────────┘
        ↓
   User can dismiss
   User can click
   User can scroll
```

### Banners Architecture

Banners follow a **placement-based** model:
- Individual placements defined in your app/website
- Each placement displays one Banner (highest priority)
- No default UI—you control the container
- Priority-based selection (High > Medium > Low)
- Up to 10 placements per refresh request
- Banners refresh at session start or manual refresh calls

```
┌─────────────────────────────┐
│      Your App UI            │
├─────────────────────────────┤
│  <Header>                   │
│                              │
│  [Banner Placement #1]      │  ← homepage_hero
│                              │
│  <Main Content>             │
│                              │
│  [Banner Placement #2]      │  ← product_promo
│                              │
│  <Footer>                   │
└─────────────────────────────┘
        ↓
   Not dismissible
   Priority-based display
   Inline rendering
```

---

## SDK/API Differences

### Key Conceptual Changes

| Concept | Content Cards | Banners |
|---------|---------------|---------|
| **Location** | Feed UI | Placement ID |
| **SDK Object** | `Card` | `Banner` |
| **Refresh Method** | `requestContentCardsRefresh()` | `requestBannersRefresh(placementIds)` |
| **Subscribe Method** | `subscribeToContentCardsUpdates()` | `subscribeToBannersUpdates()` |
| **Display Method** | `showContentCards()` | `insertBanner()` or native components |
| **Data Access** | `getCachedContentCards()` | `getBanner(placementId)` |
| **Custom Data** | `card.extras` (key-value pairs) | Typed properties: `banner.getStringProperty(key)` |

---

## Data Model Differences

### Content Card Model

```javascript
// Content Card (Web SDK example)
{
  id: "card_123",
  viewed: false,
  title: "Special Offer",
  description: "Get 20% off",
  imageUrl: "https://...",
  linkText: "Shop Now",
  url: "https://...",
  extras: {
    "feed_type": "homepage",
    "promo_code": "SAVE20"
  },
  pinned: true,
  dismissible: true,
  expiresAt: 1234567890,
  categories: ["promotions"]
}
```

### Banner Model

```javascript
// Banner (Web SDK example)
{
  placementId: "homepage_hero",
  htmlContent: "<div>...</div>", // Rendered HTML
  isControl: false,
  clicked: false,
  // Custom properties accessed via methods:
  getStringProperty(key),
  getBooleanProperty(key),
  getNumberProperty(key),
  getTimestampProperty(key),
  getImageProperty(key),
  getJsonProperty(key)
}
```

---

## Code Changes Required

### 1. Initialization Changes

#### Content Cards: No special initialization

```javascript
// Web SDK - Content Cards worked out of the box
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-ENDPOINT" });
```

#### Banners: Must opt-in to user-supplied JavaScript

```javascript
// Web SDK - Banners require explicit opt-in
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  allowUserSuppliedJavascript: true  // ← REQUIRED FOR BANNERS
});
```

**⚠️ IMPORTANT:** Banners deliver HTML content that may include JavaScript. You must explicitly opt in to `allowUserSuppliedJavascript` for security reasons.

---

### 2. Placement Configuration (New Requirement)

Banners require you to define **placement IDs** in your codebase. These are string identifiers representing locations in your UI.

**Best practices for placement IDs:**
- Use lowercase with underscores: `homepage_hero`, `checkout_banner`
- Be descriptive and location-specific
- Keep them consistent across platforms (iOS, Android, Web)
- Document them in a shared team wiki or README

**Example placement definitions:**

```javascript
// Define placement constants in your app
const PLACEMENTS = {
  HOMEPAGE_HERO: "homepage_hero",
  PRODUCT_PROMO: "product_promo",
  CHECKOUT_BANNER: "checkout_banner",
  NAV_ANNOUNCEMENT: "nav_announcement"
};
```

---

### 3. Refresh Method Changes

#### Content Cards: Refresh the entire feed

```javascript
// Web SDK
braze.requestContentCardsRefresh();

// iOS SDK
AppDelegate.braze?.contentCards.requestRefresh()

// Android SDK
Braze.getInstance(context).requestContentCardsRefresh()
```

#### Banners: Refresh specific placements

```javascript
// Web SDK - Refresh multiple placements
braze.requestBannersRefresh(["homepage_hero", "product_promo"]);

// iOS SDK
AppDelegate.braze?.banners.requestRefresh(placementIds: ["homepage_hero", "product_promo"])

// Android SDK
Braze.getInstance(context).requestBannersRefresh(listOf("homepage_hero", "product_promo"))
```

**⚠️ Rate Limiting:**
- **Older SDKs:** Only 1 refresh per session
- **Newer SDKs:** Token bucket algorithm (5 tokens at session start, 1 token refills every 3 minutes)
- **Limit:** Max 10 placements per refresh request

---

### 4. Subscribe/Listen for Updates

#### Content Cards: Subscribe to feed updates

```javascript
// Web SDK
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  // Render cards in your custom UI
});

// iOS SDK
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { cards in
  // cards is an array of all Content Cards
}

// Android SDK
Braze.getInstance(context).subscribeToContentCardsUpdates { event ->
  val cards = event.allCards
  // Render cards
}
```

#### Banners: Subscribe to placement updates

```javascript
// Web SDK
braze.subscribeToBannersUpdates((banners) => {
  // Get specific placement
  const homeBanner = braze.getBanner("homepage_hero");
  if (homeBanner) {
    const container = document.getElementById("banner-container");
    braze.insertBanner(homeBanner, container);
    
    // Handle control group
    if (homeBanner.isControl) {
      container.style.display = "none";
    }
  }
});

// iOS SDK
let cancellable = AppDelegate.braze?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    // Handle each placement's banner
  }
}

// Android SDK
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    // Handle each banner
  }
}
```

---

### 5. Rendering/Display Changes

#### Content Cards: Use Braze's default UI or build custom feed

**Using default UI:**

```javascript
// Web SDK
braze.showContentCards();

// iOS SDK
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
navigationController?.pushViewController(viewController, animated: true)

// Android SDK
val contentCardsFragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.container, contentCardsFragment)
  .commit()
```

**Custom UI:**

```javascript
// Web SDK - Custom rendering
braze.getCachedContentCards().cards.forEach(card => {
  const cardElement = document.createElement('div');
  cardElement.innerHTML = `
    <h3>${card.title}</h3>
    <p>${card.description}</p>
    <img src="${card.imageUrl}" />
  `;
  cardElement.onclick = () => {
    braze.logContentCardClick(card);
    window.location.href = card.url;
  };
  feedContainer.appendChild(cardElement);
  
  // Log impression
  braze.logContentCardImpressions([card]);
});
```

#### Banners: Insert into specific containers

**Web SDK:**

```javascript
// Step 1: Create HTML container with fixed dimensions
<div id="banner-container" style="width: 100%; height: 450px;"></div>

// Step 2: Subscribe to updates
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("homepage_hero");
  if (!banner) return;
  
  const container = document.getElementById("banner-container");
  braze.insertBanner(banner, container); // Replaces innerHTML
  
  if (banner.isControl) {
    container.style.display = "none"; // Hide control group
  }
});

// Step 3: Request refresh
braze.requestBannersRefresh(["homepage_hero"]);
```

**iOS SDK (UIKit):**

```swift
// Step 1: Create BannerUIView with placement ID
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "homepage_hero",
  braze: AppDelegate.braze!,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
        self.bannerHeightConstraint?.constant = height
        self.bannerView.isHidden = false
      }
    case .failure(let error):
      // Handle error
    }
  }
)

// Step 2: Add to view hierarchy with Auto Layout
view.addSubview(bannerView)
bannerView.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
  bannerView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
  bannerView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
  bannerView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
  bannerView.heightAnchor.constraint(equalToConstant: 0) // Updated dynamically
])
```

**iOS SDK (SwiftUI):**

```swift
struct ContentView: View {
  @State var bannerHeight: CGFloat = 0
  @State var hasBanner: Bool = false
  
  var body: some View {
    VStack {
      // Your content
      Text("Welcome")
      
      // Banner placement
      if let braze = AppDelegate.braze, hasBanner {
        BrazeBannerUI.BannerView(
          placementId: "homepage_hero",
          braze: braze,
          processContentUpdates: { result in
            if case .success(let updates) = result,
               let height = updates.height {
              bannerHeight = height
            }
          }
        )
        .frame(height: min(bannerHeight, 200))
      }
    }
    .onAppear {
      AppDelegate.braze?.banners.getBanner(for: "homepage_hero") { banner in
        hasBanner = (banner != nil)
      }
    }
  }
}
```

**Android SDK (XML Views):**

```xml
<!-- Step 1: Add to layout XML -->
<com.braze.ui.banners.BannerView
    android:id="@+id/banner_view"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="homepage_hero" />
```

```kotlin
// Step 2: Request refresh in Activity
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
    
    Braze.getInstance(this).requestBannersRefresh(listOf("homepage_hero"))
}
```

**Android SDK (Jetpack Compose):**

```kotlin
@Composable
fun HomeScreen() {
  Column {
    Text("Welcome")
    
    // Banner placement
    Banner(placementId = "homepage_hero")
  }
}
```

---

### 6. Custom Data Access Changes

#### Content Cards: Access via `extras` object

```javascript
// Web SDK
const card = braze.getCachedContentCards().cards[0];
const feedType = card.extras["feed_type"]; // String
const promoCode = card.extras["promo_code"]; // String

// iOS SDK
let feedType = card.extras["feed_type"] as? String

// Android SDK
val feedType = card.extras["feed_type"]
```

#### Banners: Use typed property methods

```javascript
// Web SDK - Typed property access
const banner = braze.getBanner("homepage_hero");
if (banner) {
  const color = banner.getStringProperty("background_color");      // String
  const expanded = banner.getBooleanProperty("is_expanded");       // Boolean
  const height = banner.getNumberProperty("height_px");            // Number
  const launchDate = banner.getTimestampProperty("launch_date");   // Timestamp
  const iconUrl = banner.getImageProperty("icon_url");             // Image URL
  const settings = banner.getJsonProperty("advanced_settings");    // JSON Object
}

// iOS SDK
AppDelegate.braze?.banners.getBanner(for: "homepage_hero") { banner in
  let color: String? = banner.stringProperty(key: "background_color")
  let expanded: Bool? = banner.boolProperty(key: "is_expanded")
  let height: Double? = banner.numberProperty(key: "height_px")
  let launchDate: Int? = banner.timestampProperty(key: "launch_date")
  let iconUrl: String? = banner.imageProperty(key: "icon_url")
  let settings: [String: Any]? = banner.jsonObjectProperty(key: "advanced_settings")
}

// Android SDK
val banner = Braze.getInstance(context).getBanner("homepage_hero")
banner?.let {
  val color: String? = it.getStringProperty("background_color")
  val expanded: Boolean? = it.getBooleanProperty("is_expanded")
  val height: Number? = it.getNumberProperty("height_px")
  val launchDate: Long? = it.getTimestampProperty("launch_date")
  val iconUrl: String? = it.getImageProperty("icon_url")
  val settings: JSONObject? = it.getJSONProperty("advanced_settings")
}
```

**Migration Strategy:**
1. Map your existing key-value pairs to typed custom properties
2. Update property keys to match your new Banners implementation
3. Document property types and usage for marketing teams

---

### 7. Analytics Changes

#### Content Cards: Manual impression/click logging for custom UI

```javascript
// Web SDK
braze.logContentCardImpressions([card]);
braze.logContentCardClick(card);

// iOS SDK
card.logImpression(using: braze)
card.logClick(using: braze)

// Android SDK
card.logImpression()
card.logClick()
```

#### Banners: Automatic impression logging when using SDK methods

```javascript
// Web SDK - Impressions logged automatically
braze.insertBanner(banner, container); // ← Logs impression automatically

// iOS SDK - Impressions logged automatically
BrazeBannerUI.BannerUIView(placementId: "...", braze: braze)

// Android SDK - Impressions logged automatically
<com.braze.ui.banners.BannerView app:placementId="..." />
```

**⚠️ Important:** If you build fully custom Banner rendering (not using `insertBanner` or native Banner components), you must manually log impressions:

```javascript
// Manual impression logging (if needed)
banner.logImpression();
```

---

### 8. Rate Limiting Changes

#### Content Cards: Token bucket with 5 tokens, 3-minute refill

```javascript
// Up to 5 refresh calls per device
// Tokens refill every 180 seconds (3 minutes)
// subscribeToContentCardsUpdates() returns cached cards even when rate-limited
```

#### Banners: Token bucket varies by SDK version

**Older SDKs (before Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0, Flutter 15.0.0):**
- Only 1 refresh per user session

**Newer SDKs:**
- 5 refresh tokens at session start
- Tokens refill at 1 token every 180 seconds (3 minutes)
- Failed requests don't consume tokens
- Max 10 placements per request

---

## Migration Checklist

Use this checklist to track your migration progress:

### Planning Phase
- [ ] Audit existing Content Cards to identify banner-style use cases
- [ ] Document Content Cards using action-based or API-triggered delivery (cannot migrate)
- [ ] Document Content Cards used in Canvas (cannot migrate)
- [ ] Create placement ID naming conventions
- [ ] Map Content Cards to Banner placement locations
- [ ] Identify SDK version requirements and plan upgrades if needed
- [ ] Review workspace campaign limits (max 200 active Banners)

### Development Phase
- [ ] Update SDK to minimum required versions:
  - [ ] Web SDK: 5.8.1+
  - [ ] iOS SDK: 11.3.0+
  - [ ] Android SDK: 33.1.0+
  - [ ] React Native: 14.0.0+
  - [ ] Flutter: 13.0.0+
- [ ] Enable `allowUserSuppliedJavascript` in Web SDK initialization
- [ ] Create placement IDs in codebase (define constants)
- [ ] Replace `requestContentCardsRefresh()` with `requestBannersRefresh(placementIds)`
- [ ] Replace `subscribeToContentCardsUpdates()` with `subscribeToBannersUpdates()`
- [ ] Remove Content Card feed UI code (if applicable)
- [ ] Implement Banner insertion at each placement location
- [ ] Add container elements with fixed dimensions (Web)
- [ ] Handle `isControl` flag to hide control group Banners
- [ ] Migrate `card.extras` access to typed Banner property methods
- [ ] Test on all platforms (iOS, Android, Web)

### Testing Phase
- [ ] Create test Banner campaigns for each placement
- [ ] Verify placements render correctly on all screen sizes
- [ ] Test priority system (create multiple campaigns per placement)
- [ ] Verify impression tracking in dashboard
- [ ] Verify click tracking in dashboard
- [ ] Test control groups render correctly (hidden containers)
- [ ] Test custom property access in code
- [ ] Verify rate limiting behavior (refresh token exhaustion)
- [ ] Test with slow network conditions
- [ ] Test error scenarios (placement not found, no eligible Banner)

### Migration Phase
- [ ] Create parallel Banner campaigns (keep Content Cards running initially)
- [ ] Launch Banners to small test segment
- [ ] Monitor analytics for 24-48 hours
- [ ] Compare Banner performance to Content Card baseline
- [ ] Gradually expand Banner audience
- [ ] Stop and remove Content Card campaigns
- [ ] Archive Content Card feed code (for rollback if needed)
- [ ] Update documentation and runbooks

### Post-Migration Phase
- [ ] Monitor Banner analytics for first 7 days
- [ ] Collect feedback from marketing team
- [ ] Document any edge cases or gotchas
- [ ] Update team training materials
- [ ] Clean up archived Content Card code
- [ ] Celebrate successful migration! 🎉

---

## Testing & Validation Guide

### QA Steps

#### 1. Verify Placement Creation

**Test:** Placements exist and are accessible by SDK

```javascript
// Web SDK - Try to get Banner for placement
braze.subscribeToBannersUpdates(() => {
  const banner = braze.getBanner("homepage_hero");
  if (!banner) {
    console.log("✅ Placement exists but no eligible Banner (expected)");
  } else {
    console.log("✅ Placement exists and Banner received");
  }
});
braze.requestBannersRefresh(["homepage_hero"]);
```

**Expected:** No errors; placement should be recognized even if no Banner is eligible

---

#### 2. Verify Impression Tracking

**Test:** Impressions log correctly when Banner displays

```javascript
// Web SDK - Check impression logging
braze.subscribeToBannersUpdates(() => {
  const banner = braze.getBanner("homepage_hero");
  if (banner) {
    const container = document.getElementById("banner-container");
    braze.insertBanner(banner, container);
    
    // Check dashboard after a few seconds
    console.log("✅ Banner inserted - check dashboard for impression");
  }
});
braze.requestBannersRefresh(["homepage_hero"]);
```

**Expected:** Impression appears in Braze dashboard within 1-2 minutes

---

#### 3. Verify Click Tracking

**Test:** Clicks log correctly when user interacts with Banner

```javascript
// If using insertBanner, clicks are automatically tracked for links/buttons
// with onclick behavior set in the dashboard

// For manual click tracking:
banner.logClick();
```

**Expected:** Click appears in Braze dashboard within 1-2 minutes

---

#### 4. Test Priority System

**Setup:**
1. Create 3 Banner campaigns targeting same placement:
   - Campaign A: High priority, targets "All Users"
   - Campaign B: Medium priority, targets "All Users"
   - Campaign C: Low priority, targets "All Users"

**Test:** Start a new session

**Expected:** Campaign A (High) displays. To test others, stop Campaign A and refresh.

---

#### 5. Test Control Groups

**Setup:** Create a Banner campaign with A/B test including a control group

**Test:** Users in control group should not see Banner

```javascript
braze.subscribeToBannersUpdates(() => {
  const banner = braze.getBanner("homepage_hero");
  if (banner && banner.isControl) {
    console.log("✅ User is in control group");
    document.getElementById("banner-container").style.display = "none";
  }
});
```

**Expected:** Control group users have hidden container; impressions still log

---

#### 6. Test Custom Properties

**Setup:** Add custom properties to Banner campaign:
- String property: `theme` = `dark`
- Boolean property: `show_icon` = `true`
- Number property: `height` = `450`

**Test:** Access properties via SDK

```javascript
const banner = braze.getBanner("homepage_hero");
console.assert(banner.getStringProperty("theme") === "dark", "✅ String property");
console.assert(banner.getBooleanProperty("show_icon") === true, "✅ Boolean property");
console.assert(banner.getNumberProperty("height") === 450, "✅ Number property");
```

**Expected:** All assertions pass

---

#### 7. Test Rate Limiting

**Test:** Call `requestBannersRefresh()` 6+ times in quick succession

```javascript
for (let i = 0; i < 10; i++) {
  braze.requestBannersRefresh(["homepage_hero"]);
}
```

**Expected:** First 5 succeed, subsequent requests fail with rate limit error (newer SDKs)

---

#### 8. Test Session-based Refresh

**Test:** Change user segment eligibility mid-session

1. User starts session → sees Banner A
2. User completes action that changes segment
3. User remains on page (no session change)

**Expected:** Banner A remains visible until next session start or manual refresh

---

### Expected Output in Logs

#### Successful Banner Load (Web SDK)

```
[Braze] Requesting banners refresh for placements: ["homepage_hero"]
[Braze] Banners updated
[Braze] Banner received for placement: homepage_hero
[Braze] Banner inserted into container
[Braze] Impression logged for placement: homepage_hero
```

#### No Eligible Banner

```
[Braze] Requesting banners refresh for placements: ["homepage_hero"]
[Braze] Banners updated
[Braze] No banner available for placement: homepage_hero (user not eligible)
```

#### Rate Limit Exceeded

```
[Braze] Requesting banners refresh for placements: ["homepage_hero"]
[Braze] ERROR: Banner refresh rate limit exceeded. Tokens available: 0. Next token refills in 120 seconds.
```

---

### Error Scenarios to Test

#### Scenario 1: Placement doesn't exist

**Test:** Request refresh for non-existent placement

```javascript
braze.requestBannersRefresh(["nonexistent_placement"]);
```

**Expected:** No error, but no Banner returned for that placement

---

#### Scenario 2: Container element not found (Web)

**Test:** Try to insert Banner into non-existent container

```javascript
const banner = braze.getBanner("homepage_hero");
const container = document.getElementById("missing_container");
braze.insertBanner(banner, container); // container is null
```

**Expected:** Error logged; Banner not rendered

---

#### Scenario 3: SDK not initialized

**Test:** Call Banner methods before SDK initialization

```javascript
// Don't call braze.initialize()
braze.requestBannersRefresh(["homepage_hero"]);
```

**Expected:** Error: SDK not initialized

---

#### Scenario 4: More than 10 placements requested

**Test:** Request 11 placements in one refresh

```javascript
braze.requestBannersRefresh([
  "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11"
]);
```

**Expected:** Only first 10 placements returned; 11th dropped with warning

---

#### Scenario 5: Slow network/timeout

**Test:** Test with throttled network (Chrome DevTools: 3G network)

**Expected:** Banners should still load but may take longer; timeouts should be handled gracefully

---

## Deprecation Notes

### What must be removed from code

#### 1. Content Card feed UI

If you were using Braze's default Content Card UI, remove these imports and methods:

```javascript
// Web SDK - REMOVE THESE
braze.showContentCards();
braze.hideContentCards();
braze.toggleContentCards();

// iOS SDK - REMOVE THESE
import BrazeUI
let viewController = BrazeContentCardUI.ViewController(braze: braze)

// Android SDK - REMOVE THESE
import com.braze.ui.contentcards.ContentCardsFragment
val fragment = ContentCardsFragment()
```

#### 2. Content Card refresh calls

Replace all Content Card refresh logic:

```javascript
// BEFORE (Content Cards)
braze.requestContentCardsRefresh();

// AFTER (Banners)
braze.requestBannersRefresh(["homepage_hero", "product_promo"]);
```

#### 3. Content Card subscription callbacks

Replace subscription methods:

```javascript
// BEFORE (Content Cards)
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  // ...
});

// AFTER (Banners)
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("homepage_hero");
  // ...
});
```

#### 4. Custom feed rendering logic

Remove any custom UI code that rendered Content Cards in a scrollable feed.

#### 5. Dismissal handling

Remove code that handled user dismissals of Content Cards:

```javascript
// REMOVE - Banners cannot be dismissed by users
card.dismiss();
```

#### 6. Feed filtering by key-value pairs (if used)

Remove logic that filtered Content Cards by `feed_type` or similar:

```javascript
// REMOVE - Not needed for Banners (use placements instead)
const homeCards = cards.filter(card => card.extras["feed_type"] === "home");
```

---

### Timelines

**Deprecation Schedule:**

- **Now:** Banners available for migration
- **Q1 2026:** Content Cards continue to be fully supported
- **Q2 2026+:** No deprecation announced; both systems supported

**Recommendation:** Migrate banner-style Content Cards to Banners now to leverage new features, but no urgent deadline exists for migration.

---

## Examples Section

### Before/After Code Snippets

#### Example 1: Homepage Hero Banner

**BEFORE (Content Cards):**

```javascript
// Web SDK - Content Cards
import * as braze from "@braze/web-sdk";

braze.initialize("API_KEY", { baseUrl: "ENDPOINT" });

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  
  // Filter for homepage cards
  const homeCards = cards.filter(card => 
    card.extras["feed_type"] === "homepage"
  );
  
  if (homeCards.length > 0) {
    const card = homeCards[0];
    
    // Custom rendering
    const container = document.getElementById("hero-container");
    container.innerHTML = `
      <div class="hero-card">
        <img src="${card.imageUrl}" alt="${card.title}">
        <h2>${card.title}</h2>
        <p>${card.description}</p>
        <a href="${card.url}">${card.linkText}</a>
      </div>
    `;
    
    // Manual analytics
    braze.logContentCardImpressions([card]);
    container.querySelector('a').onclick = () => {
      braze.logContentCardClick(card);
    };
  }
});

braze.requestContentCardsRefresh();
```

**AFTER (Banners):**

```javascript
// Web SDK - Banners
import * as braze from "@braze/web-sdk";

braze.initialize("API_KEY", {
  baseUrl: "ENDPOINT",
  allowUserSuppliedJavascript: true  // Required for Banners
});

braze.subscribeToBannersUpdates(() => {
  const banner = braze.getBanner("homepage_hero");
  
  if (banner) {
    const container = document.getElementById("hero-container");
    
    // Automatic rendering and analytics
    braze.insertBanner(banner, container);
    
    // Handle control group
    if (banner.isControl) {
      container.style.display = "none";
    }
  }
});

braze.requestBannersRefresh(["homepage_hero"]);
```

**Key Differences:**
- ✅ No manual HTML construction
- ✅ No manual impression/click tracking
- ✅ No filtering by key-value pairs (use placement instead)
- ✅ Simpler code

---

#### Example 2: Product Page Promo (iOS)

**BEFORE (Content Cards - UIKit):**

```swift
// iOS SDK - Content Cards
import UIKit
import BrazeKit

class ProductViewController: UIViewController {
  
  var cancellable: Braze.Cancellable?
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // Subscribe to Content Cards
    cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { cards in
      // Filter for product page cards
      let productCards = cards.filter {
        $0.extras["feed_type"] as? String == "product_page"
      }
      
      guard let card = productCards.first else { return }
      
      // Custom rendering
      let cardView = UIView()
      let imageView = UIImageView()
      imageView.loadImage(from: card.imageUrl)
      let label = UILabel()
      label.text = card.title
      
      // Add to view hierarchy
      self.view.addSubview(cardView)
      cardView.addSubview(imageView)
      cardView.addSubview(label)
      
      // Manual analytics
      card.logImpression(using: AppDelegate.braze!)
    }
    
    // Refresh Content Cards
    AppDelegate.braze?.contentCards.requestRefresh()
  }
}
```

**AFTER (Banners - UIKit):**

```swift
// iOS SDK - Banners
import UIKit
import BrazeKit
import BrazeUI

class ProductViewController: UIViewController {
  
  var bannerHeightConstraint: NSLayoutConstraint?
  
  lazy var bannerView: BrazeBannerUI.BannerUIView = {
    let view = BrazeBannerUI.BannerUIView(
      placementId: "product_page_promo",
      braze: AppDelegate.braze!,
      processContentUpdates: { [weak self] result in
        guard let self = self else { return }
        switch result {
        case .success(let updates):
          if let height = updates.height {
            self.bannerHeightConstraint?.constant = height
            self.bannerView.isHidden = false
          }
        case .failure:
          self.bannerView.isHidden = true
        }
      }
    )
    view.translatesAutoresizingMaskIntoConstraints = false
    view.isHidden = true
    return view
  }()
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // Add banner to view
    view.addSubview(bannerView)
    
    // Setup constraints
    bannerHeightConstraint = bannerView.heightAnchor.constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
      bannerView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
      bannerView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
      bannerView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
      bannerHeightConstraint!
    ])
    
    // Refresh banners
    AppDelegate.braze?.banners.requestRefresh(placementIds: ["product_page_promo"])
  }
}
```

**Key Differences:**
- ✅ No manual view construction
- ✅ No filtering by key-value pairs
- ✅ Automatic analytics tracking
- ✅ Dynamic height handling via callback

---

#### Example 3: Checkout Banner (Android)

**BEFORE (Content Cards - Jetpack Compose):**

```kotlin
// Android SDK - Content Cards
@Composable
fun CheckoutScreen() {
  var contentCards by remember { mutableStateOf<List<Card>>(emptyList()) }
  
  LaunchedEffect(Unit) {
    Braze.getInstance(context).subscribeToContentCardsUpdates { event ->
      contentCards = event.allCards.filter { card ->
        card.extras["feed_type"] == "checkout"
      }
    }
    Braze.getInstance(context).requestContentCardsRefresh()
  }
  
  Column {
    Text("Checkout")
    
    contentCards.firstOrNull()?.let { card ->
      Card(
        modifier = Modifier.clickable {
          card.logClick()
          // Navigate
        }
      ) {
        AsyncImage(model = card.imageUrl, contentDescription = null)
        Text(card.title ?: "")
        Text(card.description ?: "")
      }
      
      LaunchedEffect(card) {
        card.logImpression()
      }
    }
  }
}
```

**AFTER (Banners - Jetpack Compose):**

```kotlin
// Android SDK - Banners
@Composable
fun CheckoutScreen() {
  Column {
    Text("Checkout")
    
    // Single line to add Banner
    Banner(placementId = "checkout_promo")
  }
  
  LaunchedEffect(Unit) {
    Braze.getInstance(context).requestBannersRefresh(listOf("checkout_promo"))
  }
}
```

**Key Differences:**
- ✅ One-line component
- ✅ No state management needed
- ✅ No filtering logic
- ✅ Automatic analytics

---

### Integration Examples for Each Platform

#### Web SDK (Complete Example)

```html
<!DOCTYPE html>
<html>
<head>
  <title>Banners Example</title>
  <style>
    #homepage-banner { width: 100%; height: 450px; margin: 20px 0; }
    #nav-banner { width: 100%; height: 60px; }
  </style>
</head>
<body>
  <header>
    <div id="nav-banner"></div>
  </header>
  
  <main>
    <h1>Welcome</h1>
    <div id="homepage-banner"></div>
    <p>Main content here...</p>
  </main>
  
  <script type="module">
    import * as braze from "@braze/web-sdk";
    
    // Initialize with allowUserSuppliedJavascript
    braze.initialize("YOUR-API-KEY", {
      baseUrl: "YOUR-ENDPOINT",
      allowUserSuppliedJavascript: true
    });
    
    // Open session
    braze.openSession();
    
    // Subscribe to Banner updates
    braze.subscribeToBannersUpdates(() => {
      // Homepage Banner
      const homeBanner = braze.getBanner("homepage_hero");
      if (homeBanner) {
        const homeContainer = document.getElementById("homepage-banner");
        braze.insertBanner(homeBanner, homeContainer);
        if (homeBanner.isControl) {
          homeContainer.style.display = "none";
        }
      }
      
      // Nav Banner
      const navBanner = braze.getBanner("nav_announcement");
      if (navBanner) {
        const navContainer = document.getElementById("nav-banner");
        braze.insertBanner(navBanner, navContainer);
        if (navBanner.isControl) {
          navContainer.style.display = "none";
        }
      }
    });
    
    // Request refresh for both placements
    braze.requestBannersRefresh(["homepage_hero", "nav_announcement"]);
  </script>
</body>
</html>
```

---

#### iOS SDK (Complete Example - SwiftUI)

```swift
// AppDelegate.swift
import UIKit
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    AppDelegate.braze = Braze(configuration: configuration)
    return true
  }
}

// ContentView.swift
import SwiftUI
import BrazeKit
import BrazeUI

struct ContentView: View {
  @State var homeBannerHeight: CGFloat = 0
  @State var hasHomeBanner: Bool = false
  
  var body: some View {
    ScrollView {
      VStack(spacing: 20) {
        // Navigation Banner
        if let braze = AppDelegate.braze {
          BrazeBannerUI.BannerView(
            placementId: "nav_announcement",
            braze: braze,
            processContentUpdates: { _ in }
          )
          .frame(height: 60)
        }
        
        // Main Content
        Text("Welcome to Our App")
          .font(.largeTitle)
        
        // Homepage Banner
        if let braze = AppDelegate.braze, hasHomeBanner {
          BrazeBannerUI.BannerView(
            placementId: "homepage_hero",
            braze: braze,
            processContentUpdates: { result in
              if case .success(let updates) = result,
                 let height = updates.height {
                homeBannerHeight = height
              }
            }
          )
          .frame(height: min(homeBannerHeight, 450))
        }
        
        Text("More content here...")
      }
      .padding()
    }
    .onAppear {
      // Check for Banner availability
      AppDelegate.braze?.banners.getBanner(for: "homepage_hero") { banner in
        hasHomeBanner = (banner != nil)
      }
      
      // Request refresh
      AppDelegate.braze?.banners.requestRefresh(
        placementIds: ["homepage_hero", "nav_announcement"]
      )
    }
  }
}
```

---

#### Android SDK (Complete Example - Jetpack Compose)

```kotlin
// Application.kt
import android.app.Application
import com.braze.Braze
import com.braze.configuration.BrazeConfig

class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    
    val config = BrazeConfig.Builder()
      .setApiKey("YOUR-API-KEY")
      .setCustomEndpoint("YOUR-ENDPOINT")
      .build()
    Braze.configure(this, config)
    
    // Subscribe to Banner updates
    Braze.getInstance(this).subscribeToBannersUpdates { update ->
      for (banner in update.banners) {
        Log.d("Banners", "Received banner: ${banner.placementId}")
      }
    }
  }
}

// MainActivity.kt
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.braze.Braze
import com.braze.jetpackcompose.banners.Banner

class MainActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    
    // Request Banner refresh
    Braze.getInstance(this).requestBannersRefresh(
      listOf("homepage_hero", "nav_announcement")
    )
    
    setContent {
      MyAppTheme {
        HomeScreen()
      }
    }
  }
}

@Composable
fun HomeScreen() {
  Scaffold(
    topBar = {
      Column {
        Text("My App", modifier = Modifier.padding(16.dp))
        // Navigation Banner
        Banner(placementId = "nav_announcement")
      }
    }
  ) { paddingValues ->
    Column(
      modifier = Modifier
        .padding(paddingValues)
        .padding(16.dp)
    ) {
      Text("Welcome", style = MaterialTheme.typography.headlineLarge)
      
      Spacer(modifier = Modifier.height(20.dp))
      
      // Homepage Banner
      Banner(placementId = "homepage_hero")
      
      Spacer(modifier = Modifier.height(20.dp))
      
      Text("More content here...")
    }
  }
}
```

---

## Needs Clarification

The following items require additional clarification from the Braze team or further discovery:

1. **Migration tool availability**  
   Is there a bulk migration tool to convert Content Card campaigns to Banner campaigns, or must each be manually recreated?

2. **Connected Content workarounds**  
   What are recommended alternatives for Content Cards that heavily use Connected Content? Can catalog items fully replace this functionality?

3. **Canvas integration timeline**  
   Is Canvas support for Banners planned? If so, what's the expected timeline?

4. **API-triggered alternatives**  
   What's the recommended approach for real-time, action-based banner displays currently using API-triggered Content Cards?

5. **User dismissal alternatives**  
   For use cases where users need to dismiss promotional content, what's the recommended alternative pattern?

6. **Multiple Banners per placement**  
   Is there a way to display multiple Banners in a carousel format within a single placement, or must we create multiple placements?

7. **Analytics migration**  
   Can historical Content Card analytics be associated with new Banner campaigns for trend analysis, or are they completely separate?

8. **Promotional codes**  
   Banners don't support promo codes. What's the workaround for distributing unique codes via Banners?

9. **Deep linking considerations**  
   Are there any differences in deep linking behavior between Content Cards and Banners that should be documented?

10. **Testing tools**  
    Are there specific testing tools or debug modes for Banner placement validation beyond manual testing?

---

## Summary

Migrating from Content Cards to Banners represents a shift from a feed-based to a placement-based architecture. While Banners offer improved performance, simpler integration, and better control for inline messaging use cases, they require careful planning and coordination with marketing teams.

**Key Takeaways:**
- ✅ Banners are ideal for inline, persistent messages (homepage heroes, announcements, promotions)
- ✅ Placement-based model provides better control and performance
- ✅ Simpler SDK integration with automatic analytics
- ⚠️ Requires developer coordination for placement creation
- ⚠️ No Canvas, action-based, or API-triggered support (yet)
- ⚠️ Users cannot manually dismiss Banners

**Next Steps:**
1. Review this guide with your development and marketing teams
2. Identify Content Cards suitable for migration
3. Create placement ID strategy
4. Coordinate development timeline
5. Begin migration with low-risk, high-value placements first

For questions or support, contact [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
