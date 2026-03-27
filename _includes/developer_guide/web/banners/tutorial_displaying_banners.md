## Prerequisites

Before you start this tutorial, verify that your Braze Web SDK meets the minimum version requirement:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners for the Web SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

<style>
/* Standard code blocks: light mode, no line numbers */
.highlight {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
  overflow: hidden !important;
}
.highlight pre,
.highlight .rouge-code,
.highlight .rouge-code pre {
  background: #ffffff !important;
}
.highlight .rouge-table,
.highlight .rouge-table tbody,
.highlight .rouge-table tr {
  display: block !important;
  width: 100% !important;
}
.highlight .rouge-table td.rouge-code {
  display: block !important;
  width: 100% !important;
}
.highlight td.gl,
.highlight td.gutter,
.highlight .rouge-table td.gl,
.highlight .rouge-table td.gutter,
.highlight .gutter,
.highlight .lineno {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
  padding: 0 !important;
  font-size: 0 !important;
  visibility: hidden !important;
}
.highlight code.hljs,
.highlight pre code.hljs {
  background: #ffffff !important;
  color: #1B2536 !important;
  padding: 16px !important;
}
.highlight .hljs-keyword { color: #0969da !important; font-weight: 600; }
.highlight .hljs-string { color: #0a3069 !important; }
.highlight .hljs-comment { color: #6e7781 !important; font-style: italic; }
.highlight .hljs-function,
.highlight .hljs-title { color: #8250df !important; }
.highlight .hljs-number,
.highlight .hljs-literal { color: #0550ae !important; }
.highlight .hljs-built_in { color: #0550ae !important; }
.highlight .hljs-attr,
.highlight .hljs-attribute { color: #0550ae !important; }
.highlight .hljs-tag,
.highlight .hljs-name { color: #116329 !important; }
.highlight .hljs-params { color: #1B2536 !important; }
.highlight .hljs-meta { color: #0550ae !important; }
.braze-tutorial-intro {
  font-size: 17px;
  line-height: 1.7;
  color: #404756;
  margin-bottom: 28px;
}
.braze-learn-box {
  background: #f0f8ff;
  border: 1px solid #d4e8f7;
  border-left: 4px solid #00B3E6;
  border-radius: 8px;
  padding: 20px 24px;
  margin: 0 0 36px;
}
.braze-learn-box h4 {
  margin: 0 0 12px !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  color: #1B2536 !important;
}
.braze-learn-box ul {
  margin: 0 !important;
  padding-left: 20px !important;
  list-style-type: disc !important;
}
.braze-learn-box li {
  margin: 6px 0 !important;
  font-size: 14px !important;
  color: #3A506B !important;
  line-height: 1.55 !important;
}
.braze-tutorial-sandbox {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
  margin: 28px 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.07);
}
.braze-tutorial-sandbox-top {
  background: #f5f7f9;
  display: flex;
  align-items: center;
  padding: 0 4px;
  border-bottom: 1px solid #e2e8f0;
}
.braze-tutorial-tab {
  padding: 9px 14px;
  color: #6b7280;
  font-size: 13px;
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  cursor: pointer;
  border: none;
  background: transparent;
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s, background 0.15s;
  outline: none;
}
.braze-tutorial-tab:hover {
  color: #1B2536;
}
.braze-tutorial-tab:focus-visible {
  outline: 2px solid #00B3E6;
  outline-offset: -2px;
  border-radius: 4px;
}
.braze-tutorial-tab.active {
  color: #1B2536;
  font-weight: 500;
  border-bottom-color: #00B3E6;
  background: rgba(0, 179, 230, 0.06);
}
.braze-tutorial-sandbox-body {
  display: flex;
  min-height: 200px;
}
@media (max-width: 840px) {
  .braze-tutorial-sandbox-body {
    flex-direction: column;
  }
  .braze-tutorial-preview {
    border-left: none !important;
    border-top: 1px solid #e2e8f0;
  }
}
.braze-tutorial-editor {
  flex: 1.2;
  min-width: 0;
  background: #ffffff;
  overflow: auto;
  max-height: 440px;
  border-right: 1px solid #e2e8f0;
}
.braze-tutorial-panel {
  display: none;
}
.braze-tutorial-panel.active {
  display: block;
}
.braze-tutorial-editor pre {
  margin: 0 !important;
  padding: 16px !important;
  background: #ffffff !important;
  border: none !important;
  border-radius: 0 !important;
  white-space: pre !important;
  overflow-x: auto !important;
}
.braze-tutorial-editor code {
  font-size: 13px !important;
  line-height: 1.65 !important;
  background: transparent !important;
  padding: 0 !important;
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs {
  background: #ffffff !important;
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs-keyword {
  color: #0969da !important;
  font-weight: 600;
}
.braze-tutorial-editor .hljs-string {
  color: #0a3069 !important;
}
.braze-tutorial-editor .hljs-comment {
  color: #6e7781 !important;
  font-style: italic;
}
.braze-tutorial-editor .hljs-function,
.braze-tutorial-editor .hljs-title {
  color: #8250df !important;
}
.braze-tutorial-editor .hljs-number,
.braze-tutorial-editor .hljs-literal {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-built_in {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-attr,
.braze-tutorial-editor .hljs-attribute {
  color: #0550ae !important;
}
.braze-tutorial-editor .hljs-tag,
.braze-tutorial-editor .hljs-name {
  color: #116329 !important;
}
.braze-tutorial-editor .hljs-params {
  color: #1B2536 !important;
}
.braze-tutorial-editor .hljs-meta {
  color: #0550ae !important;
}
.braze-tutorial-preview {
  flex: 1;
  min-width: 0;
  border-left: 1px solid #e2e8f0;
  background: #fff;
  display: flex;
  flex-direction: column;
}
.braze-tutorial-preview-bar {
  padding: 8px 16px;
  background: #f5f7f9;
  border-bottom: 1px solid #e2e8f0;
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
  letter-spacing: 0.03em;
}
.braze-tutorial-iframe {
  flex: 1;
  width: 100%;
  min-height: 300px;
  border: none;
  display: block;
}
</style>

<div class="braze-tutorial-intro">
  <p>This tutorial walks you through displaying Banners in a web app using the Braze Web SDK and placement IDs. Each section introduces a concept, shows the code, and explains how the pieces connect. At the end, you can see the full working implementation with a live preview.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Initialize the Braze Web SDK for banners</li>
    <li>Add a banner container to your HTML</li>
    <li>Subscribe to banner updates</li>
    <li>Get and display a banner by placement ID</li>
    <li>Handle control groups</li>
    <li>Refresh banners on demand</li>
  </ul>
</div>

### Step 1: Initialize the SDK

The first step is to import and initialize the Braze Web SDK. Call `braze.initialize()` with your API key and SDK endpoint:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-SDK-ENDPOINT",
    allowUserSuppliedJavascript: true,
});
```

The `allowUserSuppliedJavascript` option is required for banners. It permits the SDK to render HTML and JavaScript content from your Braze dashboard inside banner placements.

After initializing, call `openSession()` to start a user session:

```javascript
braze.openSession();
```

The SDK needs an active session before it can fetch banner data from the Braze servers.

### Step 2: Create a banner container

In your HTML, add a `<div>` element where you want the banner to appear. Give it a unique `id` so the SDK can find it, and set a width and height:

```html
<div id="global-banner-container" style="width: 100%; height: 200px;"></div>
```

The banner HTML fills the full width and height of this container, so size it according to your layout. Create a fixed-dimension element and test those dimensions in the Braze Banner composer to verify alignment.

Have a look at the result:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0">index.html</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;My App&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;My App&lt;/h1&gt;

    &lt;div id="global-banner-container"
      style="width: 100%; height: 200px;"&gt;
    &lt;/div&gt;

    &lt;p&gt;Welcome to the app.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-web-container" class="braze-tutorial-iframe" title="Banner container preview"></iframe>
    </div>
  </div>
</div>

The `<div>` is an empty placeholder for now. The Braze SDK will inject banner content into it after you subscribe to updates and request a refresh.

### Step 3: Subscribe to banner updates

Register a callback function that runs whenever banner data changes. Call `subscribeToBannersUpdates()` to set up the listener:

```javascript
braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
});
```

The SDK calls this function when banners are first loaded and whenever they change during a session. Register your subscription **before** requesting banners so you don't miss the initial response.

### Step 4: Get a banner by placement ID

Inside your subscription callback, call `getBanner()` with a placement ID to retrieve a specific banner. If the user didn't qualify for any banner at that placement, it returns `null`:

```javascript
const globalBanner = braze.getBanner("global_banner");

if (!globalBanner) {
    return;
}
```

The placement ID (like `"global_banner"`) is the string identifier you set when creating the placement in the Braze dashboard.

### Step 5: Insert the banner

Pass the banner object and a DOM container element to `insertBanner()` to render the banner's HTML content:

```javascript
const container = document.getElementById("global-banner-container");
braze.insertBanner(globalBanner, container);
```

`insertBanner()` replaces the inner HTML of the container with the banner content. It also automatically tracks impressions and clicks for standard banner elements, so no additional analytics code is needed.

Here's the subscribe, get, and insert flow wired together. The preview shows what a rendered banner looks like:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-web-insert">index.js</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-web-insert">index.html</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-web-insert">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-javascript">import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-SDK-ENDPOINT",
    allowUserSuppliedJavascript: true,
});

braze.subscribeToBannersUpdates((banners) => {
    const globalBanner = braze.getBanner("global_banner");

    if (!globalBanner) {
        return;
    }

    const container =
        document.getElementById("global-banner-container");

    braze.insertBanner(globalBanner, container);
});

braze.openSession();
braze.requestBannersRefresh(["global_banner"]);</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;My App&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;My App&lt;/h1&gt;

    &lt;div id="global-banner-container"
      style="width: 100%; height: 200px;"&gt;
    &lt;/div&gt;

    &lt;p&gt;Welcome to the app.&lt;/p&gt;
    &lt;script type="module" src="index.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-web-insert" class="braze-tutorial-iframe" title="Banner insert preview"></iframe>
    </div>
  </div>
</div>

Notice that `subscribeToBannersUpdates()` is called before `requestBannersRefresh()`. This ordering matters because the refresh triggers an immediate network request, and the subscription callback needs to be registered before the response arrives.

### Step 6: Handle control groups

Some users may be assigned to a control group for A/B testing. When a user is in a control group, the banner's `isControl` property is `true`. Hide or collapse the container so no visual space is occupied:

```javascript
if (globalBanner.isControl) {
    container.style.display = "none";
}
```

Call `insertBanner()` even for control banners before hiding the container. This ensures impressions are tracked correctly for the control group, which is needed for accurate A/B test results.

### Step 7: Refresh banners

After registering your subscription, call `requestBannersRefresh()` with an array of placement IDs to fetch the latest banners:

```javascript
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

Call this method after you register your subscriber to ensure you receive the response. You can also call it at any point during a session to fetch updated banner content, for example after the user navigates to a new page.

Placements are cached automatically when a user's session expires or when you switch users with `changeUser()`.

### Putting it all together

Here's the complete implementation with initialization, subscription, banner rendering, control group handling, and refresh. The preview shows the final result:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-web-full">index.js</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-web-full">index.html</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-web-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-javascript">import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-SDK-ENDPOINT",
    allowUserSuppliedJavascript: true,
    enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
    const globalBanner =
        braze.getBanner("global_banner");

    if (!globalBanner) {
        return;
    }

    const container =
        document.getElementById("global-banner-container");

    // Insert the banner (also tracks impressions)
    braze.insertBanner(globalBanner, container);

    // Handle control group assignment
    if (globalBanner.isControl) {
        container.style.display = "none";
    }
});

braze.openSession();
braze.requestBannersRefresh([
    "global_banner",
    "navigation_square_banner"
]);</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;My App&lt;/title&gt;
    &lt;style&gt;
      body {
        font-family: -apple-system, BlinkMacSystemFont,
          "Segoe UI", Roboto, sans-serif;
        margin: 0;
        padding: 24px;
        background: #f8f9fa;
      }
      h1 {
        color: #1B2536;
        margin-bottom: 16px;
      }
      #global-banner-container {
        width: 100%;
        max-width: 600px;
        min-height: 200px;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;My App&lt;/h1&gt;
    &lt;div id="global-banner-container"&gt;&lt;/div&gt;
    &lt;p&gt;Welcome to the app.&lt;/p&gt;
    &lt;script type="module" src="index.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-web-full" class="braze-tutorial-iframe" title="Full banner implementation preview"></iframe>
    </div>
  </div>
</div>

The `enableLogging` option in the initializer is optional. It prints SDK activity to the browser console, which is helpful for debugging during development. Remove it before deploying to production.

### Next steps

Now that you can display banners by placement ID, explore these topics for more advanced usage:

- [Manage Banner placements]({{site.baseurl}}/developer_guide/banners/placements/) — create placements, log impressions and clicks, and work with custom properties.
- [About Banners]({{site.baseurl}}/developer_guide/banners/) — learn about how Banners work in the Braze SDK.
- [Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) — full API documentation for all banner methods.

{% raw %}
<script>
(function() {
  function initBrazeTutorial() {
    document.querySelectorAll('.braze-tutorial-tab').forEach(function(tab) {
      tab.addEventListener('click', function() {
        var sandboxId = this.getAttribute('data-sandbox');
        if (!sandboxId) return;
        var editor = document.getElementById(sandboxId);
        if (!editor) return;
        var tabIndex = parseInt(this.getAttribute('data-tab-index'), 10);
        var allTabs = this.parentElement.querySelectorAll('.braze-tutorial-tab');
        var allPanels = editor.querySelectorAll('.braze-tutorial-panel');
        allTabs.forEach(function(t, i) {
          var isActive = i === tabIndex;
          t.classList.toggle('active', isActive);
          t.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
        allPanels.forEach(function(p, i) {
          p.classList.toggle('active', i === tabIndex);
        });
      });
    });

    document.querySelectorAll('.highlight td.gl, .highlight td.gutter, .highlight .gutter, .highlight .lineno, td.gl, td.gutter').forEach(function(el) {
      el.remove();
    });

    if (typeof hljs !== 'undefined') {
      document.querySelectorAll('.braze-tutorial-editor code').forEach(function(block) {
        hljs.highlightElement(block);
      });
    }

    var sharedStyles = '* { box-sizing: border-box; margin: 0; padding: 0; }' +
      'body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8f9fa; color: #1B2536; }' +
      '.app-nav { background: #1B2536; color: #fff; padding: 10px 20px; display: flex; align-items: center; }' +
      '.app-nav-brand { font-weight: 700; font-size: 15px; }' +
      '.app-nav-links { margin-left: auto; display: flex; gap: 18px; }' +
      '.app-nav-links a { color: rgba(255,255,255,0.75); text-decoration: none; font-size: 13px; }' +
      '.app-content { padding: 20px; }' +
      'h2.page-title { font-size: 20px; font-weight: 700; margin-bottom: 14px; }' +
      '.text-muted { color: #64748b; font-size: 14px; line-height: 1.6; }';

    var navBar = '<div class="app-nav">' +
      '<span class="app-nav-brand">MyApp</span>' +
      '<nav class="app-nav-links">' +
      '<a href="javascript:void(0)">Home</a><a href="javascript:void(0)">Products</a><a href="javascript:void(0)">About</a>' +
      '</nav></div>';

    var bannerHtml =
      '<div style="background: linear-gradient(135deg, #1B2536 0%, #2d4a6f 50%, #1a7f8a 100%); color: #fff; padding: 24px 20px; border-radius: 10px; text-align: center;">' +
      '<div style="font-size: 10px; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; margin-bottom: 8px;">Limited Time Offer</div>' +
      '<h3 style="margin: 0 0 6px; font-size: 20px; font-weight: 700;">Spring Sale: 25% Off</h3>' +
      '<p style="margin: 0 0 14px; opacity: 0.9; font-size: 13px; line-height: 1.5;">Use code SPRING25 at checkout.</p>' +
      '<a href="javascript:void(0)" style="display: inline-block; background: #00B3E6; color: #fff; border: none; padding: 9px 22px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; cursor: pointer;">Shop Now</a>' +
      '</div>';

    var containerPreview = '<!DOCTYPE html><html><head><style>' + sharedStyles +
      '.container-placeholder { width: 100%; height: 180px; border: 2px dashed #cbd5e1; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 13px; background: #fff; margin-bottom: 14px; }' +
      '</style></head><body>' +
      navBar +
      '<div class="app-content">' +
      '<h2 class="page-title">Home</h2>' +
      '<div class="container-placeholder">Banner container (empty)</div>' +
      '<p class="text-muted">This is the rest of your page content. The banner will be inserted into the container above by the Braze SDK.</p>' +
      '</div></body></html>';

    var insertPreview = '<!DOCTYPE html><html><head><style>' + sharedStyles +
      '#global-banner-container { width: 100%; margin-bottom: 16px; }' +
      '</style></head><body>' +
      navBar +
      '<div class="app-content">' +
      '<h2 class="page-title">Home</h2>' +
      '<div id="global-banner-container">' + bannerHtml + '</div>' +
      '<p class="text-muted">This is the rest of your page content. The Braze SDK rendered the banner into the container using <code>insertBanner()</code>.</p>' +
      '</div></body></html>';

    var productCard = function(name, price) {
      return '<div style="background: #fff; border-radius: 8px; padding: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">' +
        '<div style="background: linear-gradient(135deg, #e2e8f0, #f1f5f9); height: 80px; border-radius: 6px; margin-bottom: 10px;"></div>' +
        '<div style="font-weight: 600; font-size: 13px; color: #1B2536;">' + name + '</div>' +
        '<div style="color: #64748b; font-size: 12px; margin-top: 3px;">' + price + '</div></div>';
    };

    var fullPreview = '<!DOCTYPE html><html><head><style>' + sharedStyles +
      '#global-banner-container { width: 100%; margin-bottom: 16px; }' +
      '.product-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 16px; }' +
      '</style></head><body>' +
      navBar +
      '<div class="app-content">' +
      '<h2 class="page-title">Home</h2>' +
      '<div id="global-banner-container">' + bannerHtml + '</div>' +
      '<p class="text-muted">Featured products</p>' +
      '<div class="product-grid">' +
      productCard('Classic Sneakers', '$89.99') +
      productCard('Denim Jacket', '$129.99') +
      '</div></div></body></html>';

    var previews = {
      'braze-preview-web-container': containerPreview,
      'braze-preview-web-insert': insertPreview,
      'braze-preview-web-full': fullPreview
    };

    Object.keys(previews).forEach(function(id) {
      var iframe = document.getElementById(id);
      if (iframe) {
        iframe.srcdoc = previews[id];
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrazeTutorial);
  } else {
    initBrazeTutorial();
  }
})();
</script>
{% endraw %}
