# Migration Guide: Content Cards → Banners

This guide provides comprehensive instructions for migrating from Braze Content Cards to Banners. It is divided into two sections:

1. **User Guide** - For marketers and non-technical users
2. **Developer Guide** - For engineering teams

---

# User Guide

## Introduction

### What is Changing and Why

Braze is introducing **Banners** as a new messaging channel designed to replace Content Cards for certain use cases. Banners provide a more streamlined, placement-based approach to displaying persistent in-app and web messages.

**Key Benefits of Banners:**
- **Simpler workflow**: No need to manage card feeds or inboxes
- **Dynamic updates**: Content refreshes automatically each session without campaign changes
- **Placement-based targeting**: Display banners at specific locations in your app or website
- **Priority system**: Control which banner shows when multiple campaigns target the same location
- **No expiration limits**: Banners can run indefinitely (Content Cards expire after 30 days)

### High-Level Summary of the New Workflow

**Content Cards (Old Way):**
1. Create a Content Card campaign
2. Cards are delivered to a user's feed/inbox
3. Users see multiple cards in a message center
4. Cards expire after 30 days
5. Cards can be dismissed by users

**Banners (New Way):**
1. Developers create placement IDs in your app/website
2. You create a Banner campaign and assign it to a placement
3. The banner appears at that specific location
4. Content updates dynamically each session
5. Banners run indefinitely until you stop the campaign

---

## Before You Begin

### Prerequisites

1. **Developer Setup Required**: Before you can create Banner campaigns, your development team must:
   - Create placement IDs in your application or website
   - Integrate the Banner SDK methods
   - See the [Developer Guide](#developer-guide) section for details

2. **Braze Package**: Banners availability depends on your Braze package. Contact your account director or customer success manager to get started.

3. **SDK Version Requirements**: Ensure your app uses the minimum SDK versions:
   - Swift: 11.3.0+
   - Android: 33.1.0+
   - Web: 5.8.1+
   - React Native: 14.0.0+
   - Flutter: 13.0.0+

### What You Need to Understand About Banners

**Placements**: Unlike Content Cards that go into a feed, Banners are displayed at specific locations (placements) in your app or website. Examples:
- Top of homepage
- Product detail pages
- Checkout flow
- Navigation sidebar

**Priority System**: When multiple Banner campaigns target the same placement, only the highest priority banner displays. You can set priority as High, Medium, or Low.

**Dynamic Updates**: Banner content updates automatically each session based on current user eligibility and personalization, without requiring campaign edits.

---

## Concept Mapping: Content Cards → Banners

| Content Cards Term | Banners Equivalent | Notes |
|-------------------|---------------------|-------|
| **Content Card Feed/Inbox** | **Placement** | Instead of a feed where multiple cards appear, banners are placed at specific locations |
| **Card Types** (Classic, Captioned Image, Image Only) | **HTML Composer** | Banners use a drag-and-drop HTML editor - no predefined card types |
| **Card Expiration** (up to 30 days) | **No Expiration** | Banners run indefinitely until you stop the campaign |
| **User Dismissal** | **Segment-Based Removal** | Users cannot dismiss banners; remove users from segments to hide banners |
| **Pin to Top** | **Priority System** | Use High/Medium/Low priority instead of pinning |
| **Multiple Cards per User** (up to 250) | **One Banner per Placement** | Each placement shows only the highest priority eligible banner |
| **Card Removal Events** | **Segment Eligibility** | Control visibility through segment targeting rather than event-based removal |
| **First Impression vs. Entry** | **Session-Based Updates** | Banners update dynamically each session based on current eligibility |

---

## Side-by-Side Workflow Comparison

### How You Did It in Content Cards

1. **Create Campaign**
   - Go to Campaigns → Create Campaign → Content Cards
   - Choose card type: Classic, Captioned Image, or Image Only
   - Compose card with title, message, image, link
   - Set expiration (up to 30 days)
   - Optionally pin card to top
   - Set removal events if needed

2. **Delivery**
   - Cards delivered to user's feed/inbox
   - Multiple cards accumulate in feed
   - Cards expire after set duration
   - Users can dismiss cards

3. **Updates**
   - Cards are static once delivered
   - To update content, must stop campaign and create new one
   - Or duplicate campaign with changes

### How You Will Do It in Banners

1. **Create Placement** (Developer Step)
   - Developer creates placement ID (e.g., "homepage_top")
   - Placement defines where banner appears in app/website

2. **Create Campaign**
   - Go to Campaigns → Create Campaign → Banner
   - Select the placement ID
   - Use drag-and-drop HTML composer (no card types)
   - Set priority (High/Medium/Low)
   - No expiration needed (runs indefinitely)
   - Add custom properties if needed

3. **Delivery**
   - Banner appears at the specified placement location
   - Only one banner per placement (highest priority)
   - Content updates automatically each session

4. **Updates**
   - Edit campaign content anytime
   - Changes reflect in next user session
   - No need to stop/restart campaign

### What Becomes Easier or More Powerful

✅ **Easier:**
- No expiration management (banners run indefinitely)
- Dynamic content updates without campaign edits
- Simpler targeting (placement-based vs. feed management)
- No need to manage card dismissal
- Priority system is clearer than pinning

✅ **More Powerful:**
- Full HTML customization (not limited to card types)
- Automatic session-based updates
- Placement-specific targeting
- Custom properties for advanced use cases

---

## Step-by-Step Migration Instructions

### Step 1: Identify Your Content Card Use Cases

Review your existing Content Card campaigns and categorize them:

- **Banner Candidates**: Messages that appear at specific locations (homepage, product pages, etc.)
- **Feed Candidates**: Messages that belong in an inbox/feed (notifications, updates, etc.)

**Note**: Banners are best for placement-specific messages. If you need a feed/inbox experience, you may need to keep using Content Cards or work with developers to create a custom feed.

### Step 2: Work with Developers to Create Placements

For each location where you want to display banners, developers need to:

1. Create a placement ID in Braze (Settings → Banner Placements → Create Placement)
2. Integrate the placement in your app/website code
3. Test the placement integration

**Example Placements:**
- `homepage_top` - Top of homepage
- `product_detail_promo` - Product detail page promotions
- `checkout_offer` - Checkout flow offers
- `navigation_sidebar` - Sidebar announcements

### Step 3: Recreate Campaigns as Banners

For each Content Card campaign you're migrating:

#### 3.1 Create the Banner Campaign

1. Go to **Messaging** → **Campaigns** → **Create Campaign**
2. Select **Banner**
3. Name your campaign (e.g., "Homepage Spring Sale Banner")
4. Add teams and tags as needed
5. **Select the placement** created by your developers

#### 3.2 Compose Your Banner

1. **Choose a template**:
   - Start with blank template
   - Use a Braze banner template
   - Select a saved banner template

2. **Build your message**:
   - Drag and drop blocks and rows
   - Add images, text, buttons, forms
   - Customize styles via the Styles panel
   - Add custom HTML blocks if needed

3. **Set click behavior**:
   - Define what happens when users click the banner
   - Can navigate within app or redirect to web
   - Can log custom attributes or events

4. **Add custom properties** (optional):
   - Add metadata for analytics or integrations
   - Use for conditional logic in your app

#### 3.3 Configure Campaign Settings

1. **Set duration**:
   - Choose start date/time
   - Banners run indefinitely by default
   - Optionally set end date/time

2. **Set priority**:
   - High, Medium, or Low
   - Use "Set Exact Priority" for drag-and-drop ordering
   - Important when multiple campaigns target same placement

3. **Target audience**:
   - Select segments or filters
   - Preview approximate population
   - Exact membership calculated at session start

4. **Set conversion events**:
   - Track user actions after seeing banner
   - 30-day conversion window

### Step 4: Test Your Banners

Before launching:

1. **Send test banner**:
   - Use Braze's test message feature
   - Send to test groups or individual users
   - Verify placement, content, and styling

2. **Check different scenarios**:
   - Users eligible for banner
   - Users not eligible (banner should not appear)
   - Multiple campaigns with same placement (verify priority)

3. **Test on different devices**:
   - Mobile apps (iOS/Android)
   - Web browsers
   - Different screen sizes

### Step 5: Launch and Monitor

1. **Launch your campaign**
2. **Monitor analytics**:
   - View impressions, clicks, conversions
   - Compare performance to original Content Cards
   - Adjust targeting or content as needed

3. **Iterate**:
   - Edit banner content without stopping campaign
   - Changes reflect in next user session
   - Adjust priority if needed

---

## Common Pitfalls & How to Avoid Them

### ❌ Pitfall 1: Expecting Multiple Banners in One Location

**Issue**: Trying to show multiple banners at the same placement.

**Solution**: Remember - only one banner per placement (the highest priority eligible banner). If you need multiple messages, either:
- Use different placements for different messages
- Combine messages into a single banner
- Use Content Cards for feed-based experiences

### ❌ Pitfall 2: Forgetting to Set Priority

**Issue**: Multiple campaigns targeting same placement, unsure which shows.

**Solution**: Always set priority when creating campaigns. Use "Set Exact Priority" for precise control.

### ❌ Pitfall 3: Expecting User Dismissal

**Issue**: Users cannot dismiss banners like they could Content Cards.

**Solution**: Control visibility through segment targeting. Remove users from segments when you want to hide banners.

### ❌ Pitfall 4: Not Testing Placement Integration

**Issue**: Campaign created but banner doesn't appear.

**Solution**: Ensure developers have:
- Created placement IDs in Braze
- Integrated SDK methods in code
- Tested placement rendering

### ❌ Pitfall 5: Using Expired Content

**Issue**: Content Cards had 30-day expiration; banners don't expire automatically.

**Solution**: Manually set end dates for time-sensitive campaigns, or use segment targeting to remove users when campaigns should end.

### ❌ Pitfall 6: Expecting Canvas Integration

**Issue**: Trying to use Banners in Canvas workflows.

**Solution**: Banners cannot be used in Canvas. Use Content Cards for Canvas or create separate Banner campaigns.

---

## FAQ

### Q: Can I use Banners in my existing Content Card feed?

**A**: No. Banners and Content Cards are separate systems. You cannot mix them in the same feed. To replace Content Card feeds with Banners, you'll need to create placements and migrate campaigns.

### Q: What happens to my existing Content Card campaigns?

**A**: Existing Content Card campaigns continue to work. You can run both Content Cards and Banners simultaneously during migration. Plan to migrate campaigns over time.

### Q: Can users dismiss Banners?

**A**: No. Users cannot manually dismiss banners. Control visibility by removing users from campaign segments.

### Q: How many Banners can be active at once?

**A**: Each workspace can have up to 200 active Banner campaigns. There's no limit on placements, but you can request up to 10 placements per user session.

### Q: Can I update Banner content after launching?

**A**: Yes! Edit your campaign content anytime. Changes will appear in the next user session without stopping the campaign.

### Q: What if I need a feed/inbox experience?

**A**: Banners are placement-based, not feed-based. If you need a message inbox, consider:
- Keeping Content Cards for feed experiences
- Working with developers to create a custom feed using Banner data
- Using a hybrid approach (Banners for placements, Content Cards for feeds)

### Q: Do Banners support all Liquid tags?

**A**: Most Liquid tags work, except `catalog_items` with the `:rerender` tag. Test your Liquid personalization before launching.

### Q: Can I use Banners in Canvas?

**A**: No. Banners are not integrated with Canvas. Use Content Cards for Canvas workflows or create separate Banner campaigns.

### Q: How do I handle A/B testing with Banners?

**A**: Banners support A/B and multivariate testing just like Content Cards. Create variants in your campaign and Braze will handle distribution.

### Q: What analytics are available for Banners?

**A**: Banner analytics include impressions, clicks, and conversions, similar to Content Cards. View analytics in the campaign dashboard or export via API.

---

# Developer Guide

## Overview

### Architecture Differences

**Content Cards Architecture:**
- Feed-based system
- Cards stored in user's feed cache
- Multiple cards per user (up to 250)
- Cards retrieved via `getContentCards()` or `subscribeToContentCardsUpdates()`
- Cards displayed in custom UI or default feed view
- Cards have types: Classic, CaptionedImage, ImageOnly

**Banners Architecture:**
- Placement-based system
- Banners stored per placement ID
- One banner per placement (highest priority)
- Banners retrieved via `getBanner(placementId)`
- Banners rendered as HTML in iframes
- No predefined types - fully customizable HTML

### SDK/API Differences

| Content Cards | Banners |
|--------------|---------|
| `getContentCards()` | `getBanner(placementId)` |
| `subscribeToContentCardsUpdates()` | `subscribeToBannersUpdates()` |
| `showContentCards(parentNode)` | `insertBanner(banner, container)` |
| `logContentCardImpressions(cards)` | Automatic (when using `insertBanner`) |
| `logContentCardClick(card)` | Automatic (when using `insertBanner`) |
| `dismissCard(card)` | Not available (segment-based removal) |
| No placement concept | `requestBannersRefresh(placementIds)` |

### Data Model Differences

**Content Cards Data Model:**
```javascript
{
  id: string,
  type: "Classic" | "CaptionedImage" | "ImageOnly",
  title: string,
  description: string,
  imageUrl: string,
  url: string,
  linkText: string,
  expiresAt: number,
  pinned: boolean,
  dismissed: boolean,
  dismissible: boolean,
  extras: { [key: string]: string },
  // ... other properties
}
```

**Banners Data Model:**
```javascript
{
  placementId: string,
  html: string,  // Rendered HTML content
  customProperties: { [key: string]: any },
  isControl: boolean,
  // No expiration, dismissal, or pinning
}
```

---

## Code Changes Required

### Required Changes for Initialization

#### Web SDK

**Content Cards (Old):**
```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
});
```

**Banners (New):**
```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  allowUserSuppliedJavascript: true, // Required for banners
});
```

**⚠️ WARNING**: Banners require `allowUserSuppliedJavascript: true` in initialization. This is a security consideration - ensure you trust the content being rendered.

#### Android SDK

**Content Cards (Old):**
```kotlin
val config = BrazeConfig.Builder()
    .setApiKey("YOUR-API-KEY")
    .setCustomEndpoint("YOUR-ENDPOINT")
    .build()
Braze.configure(this, config)
```

**Banners (New):**
```kotlin
// Same initialization, but requires SDK 33.1.0+
val config = BrazeConfig.Builder()
    .setApiKey("YOUR-API-KEY")
    .setCustomEndpoint("YOUR-ENDPOINT")
    .build()
Braze.configure(this, config)
```

#### Swift SDK

**Content Cards (Old):**
```swift
let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")
let braze = Braze(configuration: configuration)
```

**Banners (New):**
```swift
// Same initialization, but requires SDK 11.3.0+
let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")
let braze = Braze(configuration: configuration)
```

### Required Changes for Placement Configuration

#### Step 1: Create Placements in Braze Dashboard

Before writing code, create placement IDs in Braze:
1. Go to **Settings** → **Banner Placements**
2. Click **Create Placement**
3. Enter name and Placement ID (e.g., "homepage_top")
4. **⚠️ Important**: Placement IDs should not be changed after campaigns are launched

#### Step 2: Request Banner Refresh

**Web SDK:**
```javascript
// Old: Content Cards auto-refresh
// braze.requestContentCardsRefresh(); // Not needed for Content Cards

// New: Banners require explicit refresh
braze.requestBannersRefresh(["homepage_top", "product_detail_promo"]);
```

**Android SDK:**
```kotlin
// Old: Content Cards
// Braze.getInstance(context).requestContentCardsRefresh()

// New: Banners
Braze.getInstance(context).requestBannersRefresh(
    listOf("homepage_top", "product_detail_promo")
)
```

**Swift SDK:**
```swift
// Old: Content Cards
// braze.contentCards.requestRefresh()

// New: Banners
braze.banners.requestRefresh(placementIds: ["homepage_top", "product_detail_promo"])
```

**⚠️ WARNING**: You can request up to 10 placements per session. Additional requests will be ignored.

### Required Changes to Fetching and Rendering

#### Web SDK

**Content Cards (Old):**
```javascript
// Subscribe to updates
braze.subscribeToContentCardsUpdates((cards) => {
  // Display cards in feed
  braze.showContentCards(document.getElementById("feed"));
  
  // Or custom rendering
  cards.forEach(card => {
    if (card instanceof braze.ClassicCard) {
      // Render classic card
    } else if (card instanceof braze.CaptionedImage) {
      // Render captioned image
    } else if (card instanceof braze.ImageOnly) {
      // Render image only
    }
  });
  
  // Manual analytics
  braze.logContentCardImpressions(cards);
});

// Get cached cards
const cards = braze.getCachedContentCards();
```

**Banners (New):**
```javascript
// Subscribe to updates
braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const homepageBanner = braze.getBanner("homepage_top");
  
  if (!homepageBanner) {
    // User not eligible or no banner for this placement
    return;
  }
  
  // Insert banner HTML into container
  const container = document.getElementById("homepage-banner-container");
  braze.insertBanner(homepageBanner, container);
  
  // Handle control groups
  if (homepageBanner.isControl) {
    container.style.display = "none";
  }
  
  // Analytics are automatic when using insertBanner()
});

// Refresh placements
braze.requestBannersRefresh(["homepage_top"]);
```

**Key Differences:**
- Banners use placement IDs, not card arrays
- `insertBanner()` replaces `showContentCards()` for rendering
- Analytics are automatic (no manual logging needed)
- Must handle `null` case (user not eligible)

#### Android SDK

**Content Cards (Old):**
```kotlin
// Subscribe to updates
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
    // Display in RecyclerView or custom view
    cards.forEach { card ->
        when (card) {
            is ClassicCard -> { /* render */ }
            is CaptionedImage -> { /* render */ }
            is ImageOnly -> { /* render */ }
        }
    }
    
    // Manual analytics
    Braze.getInstance(context).logContentCardImpressions(cards)
}

// Get cached cards
val cards = Braze.getInstance(context).getCachedContentCards()
```

**Banners (New):**

**Option 1: Using XML Layout**
```xml
<!-- banners.xml -->
<com.braze.ui.banners.BannerView
    android:id="@+id/homepage_banner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="homepage_top" />
```

**Option 2: Programmatic Access**
```kotlin
// Subscribe to updates
Braze.getInstance(context).subscribeToBannersUpdates { update ->
    update.banners.forEach { banner ->
        Log.d(TAG, "Banner for placement: ${banner.placementId}")
        // Custom logic if needed
    }
}

// Get banner for placement
val banner = Braze.getInstance(context).getBanner("homepage_top")
if (banner != null && !banner.isControl) {
    // Use banner data or render BannerView
}

// Refresh
Braze.getInstance(context).requestBannersRefresh(
    listOf("homepage_top")
)
```

**Jetpack Compose:**
```kotlin
@Composable
fun HomePage() {
    Banner(placementId = "homepage_top")
}
```

#### Swift SDK

**Content Cards (Old):**
```swift
// Subscribe to updates
let cancellable = braze.contentCards.subscribeToUpdates { cards in
    // Display cards in table view or custom view
    cards.forEach { card in
        switch card {
        case let classic as ClassicCard:
            // Render classic card
        case let captioned as CaptionedImage:
            // Render captioned image
        case let imageOnly as ImageOnly:
            // Render image only
        default:
            break
        }
    }
    
    // Manual analytics
    braze.contentCards.logCardImpressions(cards)
}

// Get cached cards
let cards = braze.contentCards.cachedCards
```

**Banners (New):**

**Option 1: Using UIView**
```swift
// Create BannerView
if let braze = AppDelegate.braze {
    let bannerView = BrazeBannerUI.BannerUIView(
        placementId: "homepage_top",
        braze: braze,
        processContentUpdates: { result in
            switch result {
            case .success(let updates):
                if let height = updates.height {
                    // Adjust view height
                }
            case .failure(let error):
                // Handle error
            }
        }
    )
    view.addSubview(bannerView)
}
```

**Option 2: Using SwiftUI**
```swift
// Create BannerView
if let braze = AppDelegate.braze {
    let bannerView = BrazeBannerUI.BannerView(
        placementId: "homepage_top",
        braze: braze,
        processContentUpdates: { result in
            // Handle updates
        }
    )
}
```

**Option 3: Programmatic Access**
```swift
// Subscribe to updates
let cancellable = braze.banners.subscribeToUpdates { banners in
    banners.forEach { placementId, banner in
        print("Banner for placement: \(placementId)")
    }
}

// Get banner
braze.banners.getBanner(for: "homepage_top") { banner in
    if let banner = banner, !banner.isControl {
        // Use banner
    }
}

// Refresh
braze.banners.requestRefresh(placementIds: ["homepage_top"])
```

### Required HTML/JS/CSS Adjustments

#### Container Setup

**Content Cards (Old):**
```html
<!-- Feed container -->
<div id="content-cards-feed"></div>

<script>
  braze.showContentCards(document.getElementById("content-cards-feed"));
</script>
```

**Banners (New):**
```html
<!-- Placement containers - one per placement -->
<div id="homepage-banner-container" style="width: 100%; height: 450px;"></div>
<div id="product-banner-container" style="width: 100%; height: 300px;"></div>

<script>
  // Containers must have defined dimensions
  // Banner HTML will fill container width
  // Height should be set based on expected banner content
</script>
```

**⚠️ Important**: 
- Set explicit width and height on containers
- Banner HTML fills container width
- Test dimensions in Banner composer

#### Styling Differences

**Content Cards (Old):**
```css
/* Content Cards had default Braze styles */
.ab-feed {
  width: 400px;
  background: white;
}

.ab-card {
  margin: 10px;
  border: 1px solid #ccc;
}
```

**Banners (New):**
```css
/* Banners are rendered in iframes - styles are isolated */
/* Customize via Banner composer Styles panel */
/* Or use custom HTML blocks with inline styles */

/* Container styling */
#homepage-banner-container {
  width: 100%;
  height: 450px;
  margin: 20px 0;
}
```

**Key Difference**: Banners render in iframes, so external CSS doesn't affect banner content. Use the Banner composer's Styles panel or inline styles in custom HTML blocks.

### Breaking API Changes and How to Resolve Them

#### 1. No Card Types

**Breaking Change**: Content Cards had three types (Classic, CaptionedImage, ImageOnly). Banners have no types.

**Resolution**: 
- Migrate card content to Banner HTML composer
- Use drag-and-drop blocks to recreate card layouts
- Use custom HTML for advanced layouts

#### 2. No Feed/Inbox Concept

**Breaking Change**: Content Cards used feeds where multiple cards appeared. Banners are placement-based.

**Resolution**:
- Create separate placements for different locations
- If feed experience is needed, consider:
  - Keeping Content Cards for feeds
  - Building custom feed using Banner data
  - Hybrid approach

#### 3. No Expiration Property

**Breaking Change**: Content Cards had `expiresAt` property. Banners don't expire.

**Resolution**:
- Set campaign end dates in Braze dashboard
- Use segment targeting to remove users when campaign should end
- Monitor campaigns and stop manually when needed

#### 4. No Dismissal API

**Breaking Change**: Content Cards had `dismissCard()` method. Banners cannot be dismissed.

**Resolution**:
- Control visibility through segment targeting
- Remove users from segments to hide banners
- No programmatic dismissal needed

#### 5. No Pin to Top

**Breaking Change**: Content Cards had `pinned` property. Banners use priority system.

**Resolution**:
- Set campaign priority (High/Medium/Low)
- Use "Set Exact Priority" for precise ordering
- Priority determines which banner shows when multiple campaigns target same placement

#### 6. Different Analytics Model

**Breaking Change**: Content Cards required manual `logContentCardImpressions()` and `logContentCardClick()`. Banners log automatically.

**Resolution**:
- Remove manual analytics calls
- Analytics are automatic when using `insertBanner()` or SDK view components
- For control groups, still call `insertBanner()` then hide container

#### 7. Placement Limit

**Breaking Change**: Can only request 10 placements per session.

**Resolution**:
- Prioritize which placements to request
- Request only placements needed for current screen
- Cache placement IDs and request on-demand

---

## Migration Checklist

### Pre-Migration

- [ ] Review all Content Card campaigns and identify migration candidates
- [ ] Identify placement locations needed in app/website
- [ ] Create placement IDs in Braze dashboard
- [ ] Update SDK to minimum required versions
- [ ] Test SDK initialization with `allowUserSuppliedJavascript: true` (Web)

### Code Changes

- [ ] Update initialization code (add `allowUserSuppliedJavascript` for Web)
- [ ] Replace `subscribeToContentCardsUpdates()` with `subscribeToBannersUpdates()`
- [ ] Replace `getContentCards()` with `getBanner(placementId)`
- [ ] Replace `showContentCards()` with `insertBanner()` or SDK view components
- [ ] Remove manual analytics calls (`logContentCardImpressions`, `logContentCardClick`)
- [ ] Add `requestBannersRefresh()` calls
- [ ] Update HTML containers (add explicit dimensions)
- [ ] Handle `null` banners (user not eligible)
- [ ] Handle control groups (`isControl` property)
- [ ] Remove card type checking code (Classic, CaptionedImage, ImageOnly)
- [ ] Remove dismissal logic (`dismissCard()`)
- [ ] Remove expiration checking (`expiresAt`)
- [ ] Remove pinning logic (`pinned`)

### Testing

- [ ] Test placement creation and integration
- [ ] Test banner rendering in all placements
- [ ] Test priority system (multiple campaigns, same placement)
- [ ] Test control groups
- [ ] Test user eligibility (eligible vs. not eligible)
- [ ] Test banner updates across sessions
- [ ] Test on all platforms (Web, iOS, Android)
- [ ] Test different screen sizes
- [ ] Verify analytics are logging correctly
- [ ] Test custom properties access

### Post-Migration

- [ ] Monitor banner performance vs. Content Cards
- [ ] Update documentation
- [ ] Train team on new Banner workflow
- [ ] Archive old Content Card campaigns (if fully migrated)
- [ ] Update error handling and logging

---

## Testing & Validation Guide

### QA Steps

#### 1. Placement Integration Testing

**Test Case**: Verify placements are created and accessible
```javascript
// Web SDK
const banner = braze.getBanner("test_placement");
console.assert(banner !== null, "Banner should be available");
```

**Expected Result**: Banner object returned (or null if user not eligible)

#### 2. Banner Rendering Testing

**Test Case**: Verify banner renders in container
```javascript
// Web SDK
const container = document.getElementById("test-container");
const banner = braze.getBanner("test_placement");
if (banner) {
  braze.insertBanner(banner, container);
  // Verify container has content
  console.assert(container.innerHTML.length > 0, "Banner should render");
}
```

**Expected Result**: Container contains banner HTML

#### 3. Priority System Testing

**Test Case**: Verify highest priority banner shows
- Create Campaign A with High priority for placement "test"
- Create Campaign B with Low priority for placement "test"
- User eligible for both

**Expected Result**: Only Campaign A banner displays

#### 4. Control Group Testing

**Test Case**: Verify control groups are handled
```javascript
const banner = braze.getBanner("test_placement");
if (banner && banner.isControl) {
  // Container should be hidden
  container.style.display = "none";
}
```

**Expected Result**: Control banners don't display to users

#### 5. Session Update Testing

**Test Case**: Verify banners update each session
1. User sees Banner A
2. Update campaign content
3. User starts new session

**Expected Result**: User sees updated Banner A content

#### 6. Eligibility Testing

**Test Case**: Verify segment targeting works
- User in Segment A sees Banner
- Remove user from Segment A
- User starts new session

**Expected Result**: Banner no longer displays

### Expected Output in Logs

#### Web SDK

**Successful Banner Load:**
```
[Braze] Banner updated for placement: homepage_top
[Braze] Banner inserted into container: #homepage-banner-container
```

**User Not Eligible:**
```
[Braze] No banner available for placement: homepage_top
```

**Placement Refresh:**
```
[Braze] Requesting banner refresh for placements: ["homepage_top"]
[Braze] Banner refresh completed
```

#### Android SDK

**Successful Banner Load:**
```
D/Braze: Banner received for placement: homepage_top
D/Braze: BannerView rendered for placement: homepage_top
```

#### Swift SDK

**Successful Banner Load:**
```
[Braze] Banner updated for placement: homepage_top
[Braze] BannerView displayed
```

### Error Scenarios to Test

#### 1. Invalid Placement ID

**Scenario**: Request banner for non-existent placement
```javascript
const banner = braze.getBanner("invalid_placement");
// Returns null
```

**Expected**: Returns `null`, no error thrown

#### 2. Too Many Placements

**Scenario**: Request more than 10 placements
```javascript
braze.requestBannersRefresh([
  "placement_1", "placement_2", ..., "placement_11"
]);
```

**Expected**: Only first 10 placements are requested, rest ignored

#### 3. Missing Container

**Scenario**: Call `insertBanner()` with null container
```javascript
braze.insertBanner(banner, null);
```

**Expected**: Error thrown or gracefully handled

#### 4. Container Without Dimensions

**Scenario**: Insert banner into container without width/height
```html
<div id="container"></div> <!-- No dimensions -->
```

**Expected**: Banner may not render correctly or may have layout issues

#### 5. Network Failure

**Scenario**: Network error during banner refresh

**Expected**: Cached banner displayed (if available), or no banner shown

---

## Deprecation Notes

### What Must Be Removed from Code

#### Content Cards Methods (if fully migrating)

**Web SDK:**
- ❌ `braze.showContentCards()` - Replace with `braze.insertBanner()`
- ❌ `braze.getCachedContentCards()` - Replace with `braze.getBanner(placementId)`
- ❌ `braze.logContentCardImpressions()` - Automatic with banners
- ❌ `braze.logContentCardClick()` - Automatic with banners
- ❌ `card.dismissCard()` - Not available for banners

**Android SDK:**
- ❌ `Braze.getInstance(context).getCachedContentCards()` - Replace with `getBanner()`
- ❌ `Braze.getInstance(context).logContentCardImpressions()` - Automatic
- ❌ `card.dismiss()` - Not available

**Swift SDK:**
- ❌ `braze.contentCards.cachedCards` - Replace with `getBanner()`
- ❌ `braze.contentCards.logCardImpressions()` - Automatic
- ❌ `card.dismiss()` - Not available

#### Content Cards Data Model Properties

Remove code that accesses these properties (not available in Banners):
- ❌ `card.expiresAt` - No expiration
- ❌ `card.pinned` - Use priority instead
- ❌ `card.dismissed` - Not applicable
- ❌ `card.dismissible` - Not applicable
- ❌ `card.type` - No card types
- ❌ `card.title` (for ImageOnly) - Use HTML content
- ❌ `card.description` (for ImageOnly) - Use HTML content

### Timelines

**Note**: Content Cards are not being deprecated. Both Content Cards and Banners will coexist. However, if you're migrating specific use cases:

1. **Phase 1 (Weeks 1-2)**: Create placements, update SDK code
2. **Phase 2 (Weeks 3-4)**: Migrate campaigns, test thoroughly
3. **Phase 3 (Week 5+)**: Monitor performance, iterate, archive old Content Card campaigns if desired

---

## Examples Section

### Before/After Code Snippets

#### Example 1: Homepage Banner

**Content Cards (Before):**
```javascript
// Subscribe to Content Cards
braze.subscribeToContentCardsUpdates((cards) => {
  // Filter for homepage cards
  const homepageCards = cards.filter(card => 
    card.extras?.category === "homepage"
  );
  
  // Render in feed
  const feedContainer = document.getElementById("homepage-feed");
  braze.showContentCards(feedContainer, (allCards) => {
    return homepageCards;
  });
  
  // Manual analytics
  braze.logContentCardImpressions(homepageCards);
});

// Get cached cards
const cachedCards = braze.getCachedContentCards();
```

**Banners (After):**
```javascript
// Subscribe to Banner updates
braze.subscribeToBannersUpdates((banners) => {
  // Get banner for homepage placement
  const homepageBanner = braze.getBanner("homepage_top");
  
  if (!homepageBanner) {
    // User not eligible - hide container
    document.getElementById("homepage-banner-container").style.display = "none";
    return;
  }
  
  // Insert banner
  const container = document.getElementById("homepage-banner-container");
  braze.insertBanner(homepageBanner, container);
  
  // Handle control groups
  if (homepageBanner.isControl) {
    container.style.display = "none";
  }
});

// Refresh on page load
braze.requestBannersRefresh(["homepage_top"]);
```

#### Example 2: Product Detail Page Promotion

**Content Cards (Before):**
```kotlin
// Android - Content Cards
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
    val productCards = cards.filter { card ->
        card.extras?.get("category") == "product_promo"
    }
    
    // Display in RecyclerView
    adapter.submitList(productCards)
    
    // Manual analytics
    Braze.getInstance(context).logContentCardImpressions(productCards)
}
```

**Banners (After):**
```kotlin
// Android - Banners
// XML Layout
// <com.braze.ui.banners.BannerView
//     android:id="@+id/product_banner"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="product_detail_promo" />

// Or programmatic
Braze.getInstance(context).subscribeToBannersUpdates { update ->
    val banner = Braze.getInstance(context).getBanner("product_detail_promo")
    if (banner != null && !banner.isControl) {
        // Use banner or render BannerView
    }
}

// Refresh
Braze.getInstance(context).requestBannersRefresh(
    listOf("product_detail_promo")
)
```

#### Example 3: Checkout Flow Offer

**Content Cards (Before):**
```swift
// Swift - Content Cards
let cancellable = braze.contentCards.subscribeToUpdates { cards in
    let checkoutCards = cards.filter { card in
        card.extras?["category"] as? String == "checkout_offer"
    }
    
    // Display in table view
    self.checkoutCards = checkoutCards
    self.tableView.reloadData()
    
    // Manual analytics
    braze.contentCards.logCardImpressions(checkoutCards)
}
```

**Banners (After):**
```swift
// Swift - Banners
let cancellable = braze.banners.subscribeToUpdates { banners in
    braze.banners.getBanner(for: "checkout_offer") { banner in
        if let banner = banner, !banner.isControl {
            // Display banner
            let bannerView = BrazeBannerUI.BannerUIView(
                placementId: "checkout_offer",
                braze: braze
            )
            self.view.addSubview(bannerView)
        }
    }
}

// Refresh
braze.banners.requestRefresh(placementIds: ["checkout_offer"])
```

### Integration Examples for Each Platform

#### Web - React Integration

```tsx
import { useEffect, useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function HomePageBanner() {
    const bannerRef = useRef<HTMLDivElement>(null);
    const placementId = "homepage_top";

    useEffect(() => {
        // Subscribe to updates
        const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
            const banner = braze.getBanner(placementId);
            
            if (!banner || banner.isControl) {
                if (bannerRef.current) {
                    bannerRef.current.style.display = "none";
                }
                return;
            }
            
            if (bannerRef.current) {
                braze.insertBanner(banner, bannerRef.current);
            }
        });

        // Refresh placements
        braze.requestBannersRefresh([placementId]);

        // Cleanup
        return () => {
            braze.removeSubscription(subscriptionId);
        };
    }, []);

    return (
        <div 
            ref={bannerRef}
            style={{ width: "100%", height: "450px" }}
        />
    );
}
```

#### Android - Jetpack Compose

```kotlin
@Composable
fun ProductDetailScreen(productId: String) {
    val context = LocalContext.current
    
    LaunchedEffect(productId) {
        // Refresh banner when product changes
        Braze.getInstance(context).requestBannersRefresh(
            listOf("product_detail_promo")
        )
    }
    
    Column {
        // Banner at top
        Banner(placementId = "product_detail_promo")
        
        // Product details below
        ProductDetails(productId = productId)
    }
}
```

#### Swift - SwiftUI Integration

```swift
import SwiftUI
import BrazeUI

struct HomeView: View {
    var body: some View {
        VStack {
            // Banner at top
            if let braze = AppDelegate.braze {
                BrazeBannerUI.BannerView(
                    placementId: "homepage_top",
                    braze: braze
                )
            }
            
            // Rest of content
            ContentView()
        }
        .onAppear {
            // Refresh on appear
            AppDelegate.braze?.banners.requestRefresh(
                placementIds: ["homepage_top"]
            )
        }
    }
}
```

#### React Native Integration

```javascript
import { Braze } from '@braze/react-native-sdk';
import { useEffect } from 'react';

export default function HomeScreen() {
    useEffect(() => {
        // Subscribe to updates
        const subscription = Braze.addListener(
            Braze.Events.BANNER_CARDS_UPDATED,
            (data) => {
                console.log('Banners updated:', data.banners);
            }
        );

        // Refresh
        Braze.requestBannersRefresh(["homepage_top"]);

        return () => {
            subscription.remove();
        };
    }, []);

    return (
        <View>
            <Braze.BrazeBannerView
                placementID="homepage_top"
            />
        </View>
    );
}
```

#### Flutter Integration

```dart
import 'package:braze_plugin/braze_plugin.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    super.initState();
    
    // Subscribe to updates
    braze.subscribeToBanners((List<BrazeBanner> banners) {
      setState(() {
        // Update UI if needed
      });
    });
    
    // Refresh
    braze.requestBannersRefresh(["homepage_top"]);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Banner widget
        BrazeBannerView(
          placementId: "homepage_top",
        ),
        // Rest of content
        Expanded(child: ContentWidget()),
      ],
    );
  }
}
```

---

## Needs Clarification

If you encounter any of these scenarios during migration, you may need to clarify with your team or Braze support:

1. **Feed/Inbox Requirements**: If you need a message inbox experience, Banners may not be the right fit. Consider keeping Content Cards for feeds or building a custom solution.

2. **Canvas Integration**: Banners cannot be used in Canvas. If your Content Cards are part of Canvas workflows, you'll need to either:
   - Keep Content Cards for Canvas
   - Restructure workflows to use separate Banner campaigns

3. **Complex Card Interactions**: If your Content Cards have complex interactions (swipe actions, custom gestures, etc.), you may need to:
   - Recreate interactions using Banner custom HTML/JavaScript
   - Consider if Banner iframe limitations affect your use case

4. **Multi-Card Scenarios**: If you need to show multiple messages at the same location, Banners (one per placement) may not work. Consider:
   - Combining messages into one banner
   - Using different placements
   - Keeping Content Cards for multi-card scenarios

5. **Real-time Updates**: Content Cards update when new cards are delivered. Banners update each session. If you need real-time updates, verify that session-based updates meet your requirements.

---

## Additional Resources

- [Banners User Guide]({{site.baseurl}}/user_guide/message_building_by_channel/banners)
- [Banners Developer Guide]({{site.baseurl}}/developer_guide/banners)
- [Content Cards User Guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)
- [Content Cards Developer Guide]({{site.baseurl}}/developer_guide/content_cards)
- [Braze SDK Documentation]({{site.baseurl}}/developer_guide)

---

**Last Updated**: [Current Date]
**SDK Versions**: Swift 11.3.0+, Android 33.1.0+, Web 5.8.1+, React Native 14.0.0+, Flutter 13.0.0+
