## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners for the Web SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=8-23

#### 2. Subscribe to Banner updates

Use `subscribeToBannersUpdates()` to register a handler that runs whenever a Banner is updated. Inside the handler, call `braze.getBanner("global_banner")` to get the latest placement.

!!step
lines-index.js=15-22

#### 3. Insert the Banner and handle control groups

Use `braze.insertBanner(banner, container)` to insert a Banner when it's returned. To ensure keep your layout clean, hide or collapse Banners that are apart of a control group (for example, when `isControl` is `true`).

!!step
lines-index.js=25

#### 4. Refresh your Banners

After initializing the SDK, call `requestBannersRefresh(["global_banner", ...])` to ensure that Banners are refreshed at the start of each session.

You can also call this function at any time to refresh Banner placements later.

!!step
lines-main.html=3

#### 5. Add a container for your Banner

In your HTML, add a new `<div>` element and give it a short, Banner-related `id`, such as `global-banner-container`. Braze will use this `<div>` to insert your Banner into the page.

{% endscrolly %}
