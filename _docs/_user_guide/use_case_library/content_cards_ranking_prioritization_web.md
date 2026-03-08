---
nav_title: Content Card ranking and prioritization on Web
article_title: Content Card ranking and prioritization on Web
description: "Best practices for ranking and prioritizing Content Cards on websites using the Braze Web SDK and key-value pairs (KVPs)."
page_order: 1
page_type: reference
tags:
  - Content Cards
  - Web SDK
  - Key-Value Pairs
---

# Content Card ranking and prioritization on Web

This use case describes best practices and options for ranking and prioritizing Content Cards on websites that use the Braze Web SDK. Braze does not offer an out-of-the-box prioritization for Content Cards (unlike [In-App Message prioritization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/#step-7-build-the-remainder-of-your-campaign-or-canvas) with Low, Medium, and High). The approaches below use **key-value pairs (KVPs)** and custom logic to achieve a similar Low, Medium, and High priority system.

Braze uses a Crawl, Walk, and Run model for [Content Card customizations]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). The solutions here are "Walk" and "Run" approaches and cover ranking and prioritization via KVPs. The specific handling and display of the Content Cards is up to your team to implement; refer to the [Braze Web SDK documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) for display and customization.

---

## Solution 1: Prioritized feed (Walk)

This approach uses the **standard Content Card feed** with a small amount of custom development. You display cards from a single feed, filtered and sorted by a `priority_level` KVP. The same principle as [multiple feeds by feed type]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) is used, but all priority levels are shown in one feed.

**Priority mapping:**

- Low → 1  
- Medium → 2  
- High → 3  

**KVPs on each card:** `priority_level` → `1`, `2`, or `3`

### Step 1: Configure the feed and sorting

Configure the [standard Content Card feed]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) in your webpage with the Braze Web SDK. Implement code that filters and sorts cards by the `priority_level` KVP in the `extras` property. Example: a function that returns cards sorted by priority (ascending):

```javascript
function showCardsByFeedType(...priority_levels) {
  braze.showContentCards(null, function(cards) {
    const filteredCards = cards.filter(function(card) {
      return priority_levels.includes(card.extras["priority_level"]);
    });
    filteredCards.sort(function(a, b) {
      const priorityA = a.extras.priority_level;
      const priorityB = b.extras.priority_level;
      if (priorityA < priorityB) return -1;
      if (priorityA > priorityB) return 1;
      return 0;
    });
    return filteredCards;
  });
}
```

### Step 2: Display the feed

Add code to display the feed (for example, via a button). The following shows cards with priorities 1, 2, and 3:

```javascript
document.getElementById("priority_cards_toggle").onclick = function() {
  showCardsByFeedType("1", "2", "3");
};
```

### Step 3: Set KVPs on Content Cards

When creating your Content Cards, set the KVPs in the **Settings** tab during the **Compose** step. Use the key `priority_level` and values `1`, `2`, or `3`. These appear in the `extras` property of each card.

### Step 4: Launch the campaign

Complete **Schedule**, **Target**, **Assign**, and **Review**, then launch the campaign.

**Result:**

- Cards are pre-filtered and pre-sorted by `priority_level`.
- The Braze feed then sorts by pinned cards and date received.
- Within each priority group, new cards are ordered newest to oldest.

### Step 5 (optional): Custom styling

Add [custom styling]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/) for the feed if needed.

---

## Solution 2: Multiple feeds separated by priority

This approach is similar to Solution 1, but each priority level has its **own feed**. Use a KVP such as `priority_level` with values like `low_priority`, `medium_priority`, and `high_priority`.

### Step 1: Filter cards by priority

Implement a function that returns only cards matching the given priority value(s):

```javascript
function showCardsByFeedType(...priority_levels) {
  braze.showContentCards(null, function(cards) {
    return cards.filter(function(card) {
      return priority_levels.includes(card.extras["priority_level"]);
    });
  });
}
```

### Step 2: Display separate feeds

Use separate buttons (or triggers) to show each feed:

```javascript
document.getElementById("low_priority_cards_toggle").onclick = function() {
  showCardsByFeedType("low_priority");
};
document.getElementById("medium_priority_cards_toggle").onclick = function() {
  showCardsByFeedType("medium_priority");
};
document.getElementById("high_priority_cards_toggle").onclick = function() {
  showCardsByFeedType("high_priority");
};
```

### Step 3: Set KVPs and launch

Set the `priority_level` KVP on each Content Card to `low_priority`, `medium_priority`, or `high_priority` in the **Settings** tab. Complete campaign setup and launch.

### Step 4 (optional): Custom styling

Apply custom styling per feed if desired.

---

## Solution 3: Custom Content Card feed (Run)

This solution uses a [custom Content Card view]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) instead of the default feed. Your development team implements custom views/UI using Braze class properties and methods and the data models (e.g. `ab.ClassicCard`, `ab.Banner`, `ab.CaptionedImage`).

**Example:** Display cards by **priority level** and **expiry date** (e.g. limited-time offers, local offers, standing offers, with a second sort by expiry).

### Step 1: Add KVPs for priority and expiry

Create Content Cards with KVPs that support filtering and sorting, for example:

- `priority_level` → `1`, `2`, or `3` (low, medium, high)  
- `expiry_date` → `yyyy-mm-dd`

### Step 2: Custom logic

Using the `extras` field on each [card object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html):

1. Filter to cards that include an expiry (if applicable).  
2. Sort by expiry date.  
3. Sort by priority level.  
4. Display in a single feed or multiple feeds as needed.

Example `extras` object: `{ expiry_date: '2022-08-17', priority_level: '1' }`

**Result:** Content Cards are shown by priority and by expiry, with full control over order and display.

---

## Related documentation

- [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/)
- [Key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)
- [Content Card feed customization]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/)
- [Creating Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards/)
