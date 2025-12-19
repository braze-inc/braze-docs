# Braze Banners Integration - High-Level Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          BRAZE BANNERS ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────┐              ┌──────────────────────────┐
│   BRAZE DASHBOARD        │              │   CUSTOMER APP/WEBSITE   │
│   (Marketing Team)       │              │   (End Users)            │
├──────────────────────────┤              ├──────────────────────────┤
│                          │              │                          │
│  1. Create Placements    │◀────────────▶│  Placement IDs           │
│  2. Design Banners       │              │  - homepage_banner       │
│  3. Set Priority         │              │  - cart_promo           │
│  4. Define Targeting     │              │  - checkout_banner      │
│  5. Configure Custom     │              │                          │
│     Properties           │              │  Container Elements      │
│  6. Launch Campaign      │              │  <div id="banner-       │
│                          │              │       container">        │
│                          │              │                          │
└───────────┬──────────────┘              └──────────┬───────────────┘
            │                                        │
            │                                        │
            │         ┌──────────────────────┐      │
            │         │   BRAZE BACKEND      │      │
            └────────▶│   (API & Services)   │◀─────┘
                      ├──────────────────────┤
                      │                      │
                      │ • Campaign Logic     │
                      │ • Priority Engine    │
                      │ • Targeting Engine   │
                      │ • Personalization    │
                      │ • HTML Generation    │
                      │ • Analytics Store    │
                      │ • Rate Limiting      │
                      │                      │
                      └──────────┬───────────┘
                                 │
                                 │
                      ┌──────────▼───────────┐
                      │   BRAZE SDK          │
                      │   (Client Library)   │
                      ├──────────────────────┤
                      │                      │
                      │ Platform Support:    │
                      │ • Web (v5.8.1+)     │
                      │ • iOS (v11.3.0+)    │
                      │ • Android (v33.1.0+)│
                      │ • React Native      │
                      │ • Flutter           │
                      │                      │
                      └──────────────────────┘
```

---

## Component Details

### 1. BRAZE DASHBOARD (Marketing Interface)
```
┌────────────────────────────────────────────────┐
│  Banner Campaign Creation                      │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────────────────────────┐         │
│  │  Content Editor                  │         │
│  │  - Drag-and-drop builder         │         │
│  │  - HTML blocks                   │         │
│  │  - Images, text, buttons         │         │
│  │  - Email capture forms           │         │
│  │  - Custom code support           │         │
│  └──────────────────────────────────┘         │
│                                                │
│  ┌──────────────────────────────────┐         │
│  │  Configuration                   │         │
│  │  - Placement assignment          │         │
│  │  - Priority (high/medium/low)    │         │
│  │  - Campaign duration             │         │
│  │  - Audience segments             │         │
│  │  - A/B testing variants          │         │
│  │  - Conversion tracking           │         │
│  └──────────────────────────────────┘         │
│                                                │
│  ┌──────────────────────────────────┐         │
│  │  Custom Properties (Optional)    │         │
│  │  - String                        │         │
│  │  - Boolean                       │         │
│  │  - Number                        │         │
│  │  - Timestamp                     │         │
│  │  - Image URL                     │         │
│  │  - JSON Object                   │         │
│  └──────────────────────────────────┘         │
│                                                │
└────────────────────────────────────────────────┘
```

### 2. CLIENT APP/WEBSITE (Developer Implementation)
```
┌────────────────────────────────────────────────┐
│  Developer Integration                         │
├────────────────────────────────────────────────┤
│                                                │
│  STEP 1: Initialize SDK                       │
│  ┌──────────────────────────────────┐         │
│  │  braze.initialize(apiKey, {      │         │
│  │    baseUrl: endpoint,             │         │
│  │    allowUserSuppliedJavascript    │         │
│  │  });                              │         │
│  └──────────────────────────────────┘         │
│                                                │
│  STEP 2: Define Placement Containers          │
│  ┌──────────────────────────────────┐         │
│  │  <div id="homepage-banner"       │         │
│  │       style="width:100%;          │         │
│  │              height:450px">       │         │
│  │  </div>                           │         │
│  └──────────────────────────────────┘         │
│                                                │
│  STEP 3: Subscribe to Updates                 │
│  ┌──────────────────────────────────┐         │
│  │  braze.subscribeToBannersUpdates │         │
│  │    ((banners) => {                │         │
│  │      // Handle updates            │         │
│  │    });                            │         │
│  └──────────────────────────────────┘         │
│                                                │
│  STEP 4: Request Banner Refresh                │
│  ┌──────────────────────────────────┐         │
│  │  braze.requestBannersRefresh(    │         │
│  │    ["homepage_banner",            │         │
│  │     "cart_promo"]                 │         │
│  │  );                               │         │
│  └──────────────────────────────────┘         │
│                                                │
│  STEP 5: Insert Banner                        │
│  ┌──────────────────────────────────┐         │
│  │  const banner = braze.getBanner( │         │
│  │    "homepage_banner"              │         │
│  │  );                               │         │
│  │  braze.insertBanner(banner,       │         │
│  │    containerElement);             │         │
│  └──────────────────────────────────┘         │
│                                                │
└────────────────────────────────────────────────┘
```

### 3. BRAZE BACKEND (Server-Side Processing)
```
┌─────────────────────────────────────────────────────────┐
│  Banner Request Processing Pipeline                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────────┐              │
│  │  1. REQUEST VALIDATION              │              │
│  │  - Verify API key                   │              │
│  │  - Check rate limits                │              │
│  │  - Validate placement IDs           │              │
│  │  - Max 10 placements per request    │              │
│  └─────────────┬───────────────────────┘              │
│                │                                        │
│  ┌─────────────▼───────────────────────┐              │
│  │  2. USER ELIGIBILITY CHECK          │              │
│  │  - Segment membership               │              │
│  │  - Campaign active status           │              │
│  │  - User attributes matching         │              │
│  │  - Control group assignment         │              │
│  └─────────────┬───────────────────────┘              │
│                │                                        │
│  ┌─────────────▼───────────────────────┐              │
│  │  3. PRIORITY RESOLUTION             │              │
│  │  - Filter by placement ID           │              │
│  │  - Sort by priority:                │              │
│  │    * High                           │              │
│  │    * Medium (default)               │              │
│  │    * Low                            │              │
│  │  - Newest eligible banner wins      │              │
│  │    if same priority                 │              │
│  └─────────────┬───────────────────────┘              │
│                │                                        │
│  ┌─────────────▼───────────────────────┐              │
│  │  4. CONTENT PERSONALIZATION         │              │
│  │  - Apply Liquid templating          │              │
│  │  - User attribute substitution      │              │
│  │  - Dynamic content generation       │              │
│  │  - Custom property attachment       │              │
│  └─────────────┬───────────────────────┘              │
│                │                                        │
│  ┌─────────────▼───────────────────────┐              │
│  │  5. HTML GENERATION                 │              │
│  │  - Generate iframe-ready HTML       │              │
│  │  - Inject tracking pixels           │              │
│  │  - Add click handlers               │              │
│  │  - Include custom properties        │              │
│  └─────────────┬───────────────────────┘              │
│                │                                        │
│  ┌─────────────▼───────────────────────┐              │
│  │  6. RESPONSE PAYLOAD                │              │
│  │  {                                  │              │
│  │    placementId: "homepage_banner",  │              │
│  │    html: "<div>...</div>",         │              │
│  │    isControl: false,                │              │
│  │    customProperties: {...}          │              │
│  │  }                                  │              │
│  └─────────────────────────────────────┘              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Data Flow Sequence

```
┌─────────┐         ┌─────────┐         ┌─────────┐         ┌─────────┐
│  USER   │         │   APP   │         │   SDK   │         │  BRAZE  │
│         │         │         │         │         │         │ BACKEND │
└────┬────┘         └────┬────┘         └────┬────┘         └────┬────┘
     │                   │                   │                   │
     │ 1. Opens App      │                   │                   │
     ├──────────────────▶│                   │                   │
     │                   │                   │                   │
     │                   │ 2. Initialize SDK │                   │
     │                   ├──────────────────▶│                   │
     │                   │                   │                   │
     │                   │ 3. Request Refresh│                   │
     │                   │   (placement_ids) │ 4. Fetch Banners  │
     │                   ├──────────────────▶├──────────────────▶│
     │                   │                   │                   │
     │                   │                   │                   │ 5. Validate
     │                   │                   │                   │    Request
     │                   │                   │                   │
     │                   │                   │                   │ 6. Check User
     │                   │                   │                   │    Eligibility
     │                   │                   │                   │
     │                   │                   │                   │ 7. Apply
     │                   │                   │                   │    Priority
     │                   │                   │                   │
     │                   │                   │                   │ 8. Personalize
     │                   │                   │                   │    Content
     │                   │                   │                   │
     │                   │                   │ 9. Return Banners │
     │                   │                   │◀──────────────────┤
     │                   │                   │                   │
     │                   │ 10. Trigger       │                   │
     │                   │     Update Event  │                   │
     │                   │◀──────────────────┤                   │
     │                   │                   │                   │
     │                   │ 11. Get Banner    │                   │
     │                   ├──────────────────▶│                   │
     │                   │                   │                   │
     │                   │ 12. Insert Banner │                   │
     │                   │    into Container │                   │
     │                   │◀──────────────────┤                   │
     │                   │                   │                   │
     │ 13. View Banner   │                   │                   │
     │◀──────────────────┤                   │                   │
     │                   │                   │                   │
     │                   │                   │ 14. Log           │
     │                   │                   │     Impression    │
     │                   │                   ├──────────────────▶│
     │                   │                   │                   │
     │ 15. Click Banner  │                   │                   │
     ├──────────────────▶│                   │                   │
     │                   │                   │                   │
     │                   │                   │ 16. Log Click     │
     │                   │                   ├──────────────────▶│
     │                   │                   │                   │
     │ 17. Navigate to   │                   │                   │
     │     Destination   │                   │                   │
     │◀──────────────────┤                   │                   │
     │                   │                   │                   │
```

---

## Key Features & Constraints

### Rate Limiting (Token Bucket Algorithm)
```
┌─────────────────────────────────────────────┐
│  Refresh Request Rate Limiting              │
│  (SDK v13.1.0+ / 38.0.0+ / 6.1.0+)         │
├─────────────────────────────────────────────┤
│                                             │
│  Initial Tokens: 5                          │
│  Refill Rate: 1 token / 180 seconds        │
│                                             │
│  Per Session:                               │
│  ┌─────────────────────────────┐           │
│  │ Token Count: [●●●●●]         │           │
│  │ (5 available)                │           │
│  └─────────────────────────────┘           │
│                                             │
│  After Request:                             │
│  ┌─────────────────────────────┐           │
│  │ Token Count: [●●●●○]         │           │
│  │ (4 available)                │           │
│  └─────────────────────────────┘           │
│                                             │
│  If No Tokens:                              │
│  ┌─────────────────────────────┐           │
│  │ Request BLOCKED              │           │
│  │ Error logged                 │           │
│  │ Wait for refill              │           │
│  └─────────────────────────────┘           │
│                                             │
└─────────────────────────────────────────────┘
```

### Priority Resolution Engine
```
┌───────────────────────────────────────────────────┐
│  Multiple Campaigns → Same Placement              │
├───────────────────────────────────────────────────┤
│                                                   │
│  Placement: "homepage_banner"                     │
│                                                   │
│  Campaign A: Priority HIGH    ◀── Displayed First│
│  Campaign B: Priority HIGH    ◀── If A ineligible│
│  Campaign C: Priority MEDIUM  ◀── If A & B       │
│  Campaign D: Priority LOW     ◀── Last resort    │
│                                                   │
│  Tiebreaker: Newest eligible campaign wins       │
│                                                   │
└───────────────────────────────────────────────────┘
```

### Placement Request Constraints
```
┌─────────────────────────────────────────────┐
│  Placement Request Rules                    │
├─────────────────────────────────────────────┤
│                                             │
│  Max per refresh: 10 placements             │
│  ┌─────────────────────────────┐           │
│  │ requestBannersRefresh([     │           │
│  │   "p1", "p2", ..., "p10"    │  ✓ OK    │
│  │ ])                          │           │
│  └─────────────────────────────┘           │
│                                             │
│  ┌─────────────────────────────┐           │
│  │ requestBannersRefresh([     │           │
│  │   "p1", "p2", ..., "p15"    │  ✗ ERROR │
│  │ ])                          │           │
│  │ // Only first 10 returned   │           │
│  └─────────────────────────────┘           │
│                                             │
│  Per placement: 1 highest-priority Banner   │
│  Max active campaigns per workspace: 200    │
│                                             │
└─────────────────────────────────────────────┘
```

### Rendering Architecture
```
┌──────────────────────────────────────────────────┐
│  Banner Rendering (iframe-based)                 │
├──────────────────────────────────────────────────┤
│                                                  │
│  App Container:                                  │
│  ┌────────────────────────────────────────────┐ │
│  │  <div id="banner-container">               │ │
│  │                                            │ │
│  │    ┌──────────────────────────────────┐   │ │
│  │    │  <iframe>                        │   │ │
│  │    │                                  │   │ │
│  │    │    Banner HTML Content           │   │ │
│  │    │    - Isolated styles             │   │ │
│  │    │    - Isolated scripts            │   │ │
│  │    │    - Click tracking              │   │ │
│  │    │    - Impression tracking         │   │ │
│  │    │                                  │   │ │
│  │    │    [Banner Visual Content]       │   │ │
│  │    │                                  │   │ │
│  │    └──────────────────────────────────┘   │ │
│  │                                            │ │
│  └────────────────────────────────────────────┘ │
│                                                  │
│  Benefits:                                       │
│  • Style isolation                               │
│  • Script sandboxing                             │
│  • Dynamic content updates                       │
│  • Consistent cross-device rendering             │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## Analytics & Tracking Flow

```
┌─────────────────────────────────────────────────────┐
│  Automatic Analytics Tracking                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  SDK Insertion Method Used:                         │
│  ✓ Impressions tracked automatically                │
│  ✓ Clicks tracked automatically                     │
│  ✓ Control group impressions tracked                │
│                                                     │
│  Events Logged:                                     │
│  ┌───────────────────────────────────────────────┐ │
│  │  IMPRESSION                                   │ │
│  │  - When banner enters viewport                │ │
│  │  - Includes control group variants            │ │
│  │  - Placement ID                               │ │
│  │  - Campaign ID                                │ │
│  │  - Variant ID                                 │ │
│  │  - Timestamp                                  │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
│  ┌───────────────────────────────────────────────┐ │
│  │  CLICK                                        │ │
│  │  - User interaction with banner               │ │
│  │  - Button/link/element clicked                │ │
│  │  - Destination URL                            │ │
│  │  - Custom event/attribute triggers            │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
│  ┌───────────────────────────────────────────────┐ │
│  │  CONVERSION                                   │ │
│  │  - Tracked conversion events                  │ │
│  │  - Up to 30-day attribution window            │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Platform Support Matrix

```
┌────────────────────────────────────────────────────────┐
│  Braze SDK Minimum Versions                            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Platform          Min Version      Status            │
│  ─────────────────────────────────────────────────    │
│  Web               5.8.1+           ✓ Supported       │
│  iOS (Swift)       11.3.0+          ✓ Supported       │
│  Android           33.1.0+          ✓ Supported       │
│  React Native      14.0.0+          ✓ Supported       │
│  Flutter           13.0.0+          ✓ Supported       │
│  Unity             N/A              ✗ Not Supported   │
│  Cordova           N/A              ✗ Not Supported   │
│  Roku              N/A              ✗ Not Supported   │
│                                                        │
│  Enhanced Features (Custom Properties, Advanced Rate   │
│  Limiting):                                            │
│  ─────────────────────────────────────────────────    │
│  Web               6.1.0+                              │
│  iOS (Swift)       13.1.0+                             │
│  Android           38.0.0+                             │
│  React Native      17.0.0+                             │
│  Flutter           15.0.0+                             │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Custom Properties Architecture

```
┌──────────────────────────────────────────────────────┐
│  Custom Properties System                            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Dashboard Configuration:                            │
│  ┌────────────────────────────────────────────────┐ │
│  │  Property Key  │  Type      │  Value           │ │
│  │  ───────────────────────────────────────────── │ │
│  │  color         │  String    │  "#FF0000"       │ │
│  │  expanded      │  Boolean   │  true            │ │
│  │  height        │  Number    │  450             │ │
│  │  start_date    │  Timestamp │  1702656000000   │ │
│  │  icon          │  Image URL │  "https://..."   │ │
│  │  settings      │  JSON      │  {"key": "val"}  │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  SDK Access Methods:                                 │
│  ┌────────────────────────────────────────────────┐ │
│  │  const banner = braze.getBanner(placementId); │ │
│  │                                                │ │
│  │  banner.getStringProperty("color")             │ │
│  │  banner.getBooleanProperty("expanded")         │ │
│  │  banner.getNumberProperty("height")            │ │
│  │  banner.getTimestampProperty("start_date")     │ │
│  │  banner.getImageProperty("icon")               │ │
│  │  banner.getJsonProperty("settings")            │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Use Cases:                                          │
│  • Third-party analytics metadata                    │
│  • Conditional UI logic                              │
│  • Dynamic behavior control                          │
│  • Integration with external systems                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## System Limitations & Constraints

```
┌──────────────────────────────────────────────────────┐
│  Banner System Constraints                           │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Workspace Limits:                                   │
│  • Max active campaigns: 200                         │
│  • Placements per workspace: No fixed limit          │
│  • Campaigns per placement: 10 active                │
│                                                      │
│  Request Limits:                                     │
│  • Placements per refresh: 10 max                    │
│  • Refresh requests per session: Rate limited        │
│    (Token bucket: 5 initial, 1/180s refill)          │
│                                                      │
│  Not Supported:                                      │
│  ✗ Canvas integration                                │
│  ✗ API-triggered campaigns                           │
│  ✗ Action-based campaigns                            │
│  ✗ Connected Content                                 │
│  ✗ Promotional codes                                 │
│  ✗ User-controlled dismissals                        │
│  ✗ catalog_items with :rerender tag                  │
│                                                      │
│  Supported:                                          │
│  ✓ Scheduled campaigns                               │
│  ✓ Segment targeting                                 │
│  ✓ A/B testing                                       │
│  ✓ Liquid personalization                            │
│  ✓ Custom properties                                 │
│  ✓ Control groups                                    │
│  ✓ Conversion tracking (30-day window)               │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## Integration Checklist

```
┌─────────────────────────────────────────────────────┐
│  Developer Implementation Checklist                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [ ] 1. Update Braze SDK to minimum version         │
│         (Web 5.8.1+, iOS 11.3.0+, Android 33.1.0+) │
│                                                     │
│  [ ] 2. Initialize SDK with required config         │
│         - API key                                   │
│         - Base URL                                  │
│         - allowUserSuppliedJavascript: true         │
│                                                     │
│  [ ] 3. Create placement IDs in code                │
│         - Define container elements                 │
│         - Set dimensions (width/height)             │
│                                                     │
│  [ ] 4. Implement Banner lifecycle:                 │
│         - Subscribe to updates                      │
│         - Request refresh on session start          │
│         - Handle banner retrieval                   │
│         - Insert banners into containers            │
│         - Handle control groups                     │
│                                                     │
│  [ ] 5. Test integration:                           │
│         - Send test Banners                         │
│         - Verify rendering                          │
│         - Check analytics tracking                  │
│                                                     │
│  [ ] 6. Coordinate with marketing team:             │
│         - Share placement ID list                   │
│         - Document placement locations              │
│         - Provide dimension recommendations         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Error Handling & Edge Cases

```
┌──────────────────────────────────────────────────────┐
│  Error Scenarios & Handling                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Scenario 1: No Banner Available                     │
│  ┌────────────────────────────────────────────────┐ │
│  │  braze.getBanner(placementId) returns null     │ │
│  │  → Hide container or show default content      │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Scenario 2: Control Group Assignment                │
│  ┌────────────────────────────────────────────────┐ │
│  │  banner.isControl === true                     │ │
│  │  → Still call insertBanner() for tracking      │ │
│  │  → Hide container with display:none            │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Scenario 3: Rate Limit Exceeded                     │
│  ┌────────────────────────────────────────────────┐ │
│  │  No tokens available                           │ │
│  │  → Request blocked                             │ │
│  │  → Error logged to console                     │ │
│  │  → Wait for token refill                       │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Scenario 4: Too Many Placements Requested           │
│  ┌────────────────────────────────────────────────┐ │
│  │  More than 10 placement IDs in request         │ │
│  │  → Only first 10 processed                     │ │
│  │  → Remaining dropped                           │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Scenario 5: Network Failure                         │
│  ┌────────────────────────────────────────────────┐ │
│  │  API request fails                             │ │
│  │  → Cache returns stale data if available       │ │
│  │  → Fallback to default content                 │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```
