{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners

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

Enable debugging while developing to make troubleshooting easier!

!!step
lines-index.js=8-23

#### 2. Subscribe to banner updates

Use `subscribeToBannersUpdates(callback)` to register a handler that will run any time banners are refreshed.

Within the callback, get the banner for your placement using `braze.getBanner("global_banner")`.

!!step
lines-index.js=15-22

#### 3. Insert the banner and handle control groups

If a banner is returned, insert it into your page with `braze.insertBanner(banner, container)`.

If the returned banner is a control group (i.e. `isControl` is true), hide or collapse the banner's container so your layout stays clean.

!!step
lines-index.js=25

#### 4. Request banners refresh

Call `requestBannersRefresh(["global_banner", ...])` after initializing to ensure your banners are fetched from Braze.
Call this whenever you want to refresh the banners for any placement(s).

!!step
lines-main.html=3

#### 5. Add a container for your banner

Add a div in your HTML (e.g. `<div id="global-banner-container"></div>`) where Braze will insert the banner content.

{% endscrolly %}
