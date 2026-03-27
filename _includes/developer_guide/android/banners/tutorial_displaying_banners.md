## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners for the Android SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Android" %}

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
  <p>This tutorial walks you through displaying Banners in an Android app using the Braze Android SDK and placement IDs. Each section introduces a concept, shows the code, and explains how the pieces connect. At the end, you can see the full working implementation with a preview of the expected result.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Configure the Braze SDK for banners in your Android app</li>
    <li>Subscribe to banner updates with <code>subscribeToBannersUpdates()</code></li>
    <li>Request fresh banner content for specific placements</li>
    <li>Add a <code>BannerView</code> to your XML layout</li>
    <li>Handle control group assignments</li>
    <li>Use the Jetpack Compose <code>Banner</code> composable as an alternative</li>
  </ul>
</div>

### Step 1: Configure the Braze SDK

In your `Application` class, create a `BrazeConfig` with your API key and SDK endpoint, then call `Braze.configure()` to initialize the SDK:

```kotlin
val config = BrazeConfig.Builder()
    .setApiKey("YOUR-API-KEY")
    .setCustomEndpoint("YOUR-ENDPOINT")
    .build()
Braze.configure(this, config)
```

This runs once when the app starts. The SDK uses your configuration to connect to the Braze servers and begin syncing data for the current user.

### Step 2: Enable debugging (optional)

To make troubleshooting easier during development, set the log level to verbose at the top of your `Application.onCreate()` method:

```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```

This prints detailed SDK activity to Logcat, including banner requests and responses. Remove this line before deploying to production.

### Step 3: Subscribe to banner updates

Register a callback that runs whenever banner data changes. Call `subscribeToBannersUpdates()` on the Braze instance to set up the listener:

```kotlin
Braze.getInstance(this)
    .subscribeToBannersUpdates { update ->
        for (banner in update.banners) {
            Log.d("Banners", "Received: ${banner.placementId}")
        }
    }
```

The SDK calls this function when banners are first loaded and whenever they change during a session. Register your subscription **before** requesting a refresh so you don't miss the initial response.

### Step 4: Request a banner refresh

Call `requestBannersRefresh()` with a list of placement IDs to fetch the latest banner content from the Braze servers:

```kotlin
Braze.getInstance(this)
    .requestBannersRefresh(listOf("top-1"))
```

Call this method in your `Activity.onCreate()` after the Braze SDK has been configured. You can also call it at any point during a session to fetch updated content, for example when the user navigates to a new screen.

### Step 5: Add a BannerView to your layout

In your XML layout file, add a `<com.braze.ui.banners.BannerView>` element with the `app:placementId` attribute set to your placement ID:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/banner_view_1"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="top-1" />
```

`BannerView` is a `WebView` subclass that automatically renders banner HTML content. When the SDK receives banner data for the specified placement, the view loads and displays the content. No additional rendering code is needed.

Have a look at the result when the `BannerView` is added to a layout:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0">banners.xml</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;ScrollView
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"&gt;

    &lt;LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal"&gt;

        &lt;com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:placementId="top-1" /&gt;

        &lt;!-- Your other content here --&gt;

    &lt;/LinearLayout&gt;
&lt;/ScrollView&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-layout" class="braze-tutorial-iframe" title="Android banner layout preview"></iframe>
    </div>
  </div>
</div>

The `BannerView` starts empty and fills with content after the SDK receives banner data. The `wrap_content` height adapts to the banner's intrinsic height, and the optional `heightCallback` property reports the content height in dp if you need to adjust surrounding layout programmatically.

### Step 6: Use Jetpack Compose (alternative)

If your app uses Jetpack Compose, use the `Banner` composable from the Braze Jetpack Compose module instead of the XML `BannerView`:

```kotlin
import androidx.compose.foundation.layout.Column
import androidx.compose.runtime.Composable
import com.braze.jetpackcompose.banners.Banner

@Composable
fun BannerScreen() {
    Column {
        Banner(
            placementId = "top-1",
            heightCallback = { heightInDp ->
                // Adjust layout based on banner height
            }
        )
    }
}
```

The `Banner` composable wraps `BannerView` in an `AndroidView` and handles placement ID updates automatically. The optional `heightCallback` reports the banner's content height in dp, which you can use to adjust surrounding layout.

### Step 7: Handle control groups

Some users may be assigned to a control group for A/B testing. When a user is in a control group, `BannerView` renders empty content automatically — no additional code is needed for basic control handling.

To detect control group assignment in your subscription callback, check the `isControl` property on a `Banner` object:

```kotlin
Braze.getInstance(this)
    .subscribeToBannersUpdates { update ->
        for (banner in update.banners) {
            if (banner.isControl) {
                Log.d("Banners", "Control group: ${banner.placementId}")
            }
        }
    }
```

If you need to completely hide the `BannerView` (removing any reserved space in the layout), set its visibility to `View.GONE` when a control banner is detected.

### Putting it all together

Here's the complete implementation with SDK configuration, subscription, refresh, and a `BannerView` layout. The preview shows what the rendered banner looks like on a device:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-android-full">MainApplication.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-android-full">MainActivity.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="2" data-sandbox="sandbox-android-full">banners.xml</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-android-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-kotlin">import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger

class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Enable verbose logging for development
        BrazeLogger.logLevel = Log.VERBOSE

        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        Braze.getInstance(this)
            .subscribeToBannersUpdates { update ->
                for (banner in update.banners) {
                    Log.d("Banners",
                        "Received: ${banner.placementId}")
                }
            }
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-kotlin">import android.os.Bundle
import androidx.activity.ComponentActivity
import com.braze.Braze

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.banners)

        Braze.getInstance(this)
            .requestBannersRefresh(
                listOf("top-1")
            )
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;ScrollView
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"&gt;

    &lt;LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal"&gt;

        &lt;com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:placementId="top-1" /&gt;

        &lt;!-- The rest of your activity layout --&gt;

    &lt;/LinearLayout&gt;
&lt;/ScrollView&gt;</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-full" class="braze-tutorial-iframe" title="Full Android banner implementation preview"></iframe>
    </div>
  </div>
</div>

The `BrazeLogger.logLevel` setting in `MainApplication.kt` is optional. It prints SDK activity to Logcat, which is helpful for debugging during development. Remove it before deploying to production.

### Next steps

Now that you can display banners by placement ID, explore these topics for more advanced usage:

- [Manage Banner placements]({{site.baseurl}}/developer_guide/banners/placements/) — create placements, log impressions and clicks, and work with custom properties.
- [About Banners]({{site.baseurl}}/developer_guide/banners/) — learn how Banners work in the Braze SDK.
- [Android SDK reference](https://braze-inc.github.io/braze-android-sdk/kdoc/) — full API documentation for all banner classes and methods.

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

    var phoneStyles = '* { box-sizing: border-box; margin: 0; padding: 0; }' +
      'body { font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f7f9; padding: 12px; }' +
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 28px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 4px 20px; font-size: 10px; display: flex; justify-content: space-between; }' +
      '.phone-appbar { background: #1B2536; color: #fff; padding: 12px 16px; font-weight: 600; font-size: 15px; }' +
      '.phone-body { background: #fafafa; padding: 16px; min-height: 280px; }';

    var bannerHtml =
      '<div style="background: linear-gradient(135deg, #1B2536 0%, #2d4a6f 50%, #1a7f8a 100%); color: #fff; padding: 20px 16px; border-radius: 10px; text-align: center; margin-bottom: 12px;">' +
      '<div style="font-size: 9px; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; margin-bottom: 6px;">Limited Time Offer</div>' +
      '<h3 style="margin: 0 0 4px; font-size: 17px; font-weight: 700;">Spring Sale: 25% Off</h3>' +
      '<p style="margin: 0 0 12px; opacity: 0.9; font-size: 12px; line-height: 1.4;">Use code SPRING25 at checkout.</p>' +
      '<a href="javascript:void(0)" style="display: inline-block; background: #00B3E6; color: #fff; border: none; padding: 8px 20px; border-radius: 6px; font-size: 12px; font-weight: 600; text-decoration: none; cursor: pointer;">Shop Now</a>' +
      '</div>';

    var layoutPreview = '<!DOCTYPE html><html><head><style>' + phoneStyles +
      '.placeholder { border: 2px dashed #cbd5e1; border-radius: 8px; height: 120px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 12px; background: #fff; margin-bottom: 12px; }' +
      '.content-block { background: #fff; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }' +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>LTE</span></div>' +
      '<div class="phone-appbar">MyApp</div>' +
      '<div class="phone-body">' +
      '<div class="placeholder">BannerView (empty)</div>' +
      '<div class="content-block">' +
      '<div style="font-weight:600;font-size:13px;color:#1B2536;">Your app content</div>' +
      '<div style="color:#64748b;font-size:11px;margin-top:4px;">The BannerView is waiting for banner data from the Braze SDK.</div>' +
      '</div></div></div></body></html>';

    var fullPreview = '<!DOCTYPE html><html><head><style>' + phoneStyles +
      '.content-block { background: #fff; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }' +
      '.product-row { display: flex; gap: 8px; margin-top: 12px; }' +
      '.product-card { flex: 1; background: #fff; border-radius: 8px; padding: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }' +
      '.product-img { background: linear-gradient(135deg, #e2e8f0, #f1f5f9); height: 60px; border-radius: 6px; margin-bottom: 6px; }' +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>LTE</span></div>' +
      '<div class="phone-appbar">MyApp</div>' +
      '<div class="phone-body">' +
      bannerHtml +
      '<div class="content-block">' +
      '<div style="font-weight:600;font-size:13px;color:#1B2536;">Featured products</div>' +
      '</div>' +
      '<div class="product-row">' +
      '<div class="product-card"><div class="product-img"></div><div style="font-size:11px;font-weight:600;color:#1B2536;">Sneakers</div><div style="font-size:10px;color:#64748b;">$89.99</div></div>' +
      '<div class="product-card"><div class="product-img"></div><div style="font-size:11px;font-weight:600;color:#1B2536;">Jacket</div><div style="font-size:10px;color:#64748b;">$129.99</div></div>' +
      '</div></div></div></body></html>';

    var previews = {
      'braze-preview-android-layout': layoutPreview,
      'braze-preview-android-full': fullPreview
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
