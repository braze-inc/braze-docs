{% multi_lang_include developer_guide/prerequisites/android.md %}

You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Customizing message styling using key-value pairs for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Android" %}

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
  <p>This tutorial shows how to style in-app messages on Android using key-value pairs from the message payload. You build a custom view factory that wraps Braze's default UI, reads values from <code>extras</code>, and applies them to the rendered view. Each step adds one piece of the flow; the last section combines everything with a preview of a slide-up message whose background color comes from your key-value pairs.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Turn on verbose SDK logging during development (optional)</li>
    <li>Register <code>BrazeActivityLifecycleCallbackListener</code> with your <code>Application</code></li>
    <li>Implement <code>IInAppMessageViewFactory</code> for custom in-app message views</li>
    <li>Delegate to <code>getDefaultInAppMessageViewFactory()</code> and adjust the default view</li>
    <li>Read styling inputs from <code>inAppMessage.extras</code></li>
    <li>Register your factory with <code>BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()</code></li>
  </ul>
</div>

### Step 1: Enable debugging (optional)

During development, set the Braze log level to verbose so Logcat shows detailed SDK activity, including in-app message display and lifecycle events. Add this near the start of <code>Application.onCreate()</code>.

```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```

Remove this assignment before you ship to production so you don't log sensitive detail in release builds.

### Step 2: Register activity lifecycle callbacks

In-app messages need activity lifecycle events. Register Braze's listener on your <code>Application</code> so every activity's lifecycle is forwarded to the SDK.

```kotlin
registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
```

Call this after <code>super.onCreate()</code> in <code>onCreate()</code>, typically in the same place you configure the SDK.

### Step 3: Create a custom view factory class

Implement <code>IInAppMessageViewFactory</code> with a <code>createInAppMessageView()</code> method that receives the host <code>Activity</code> and the <code>IInAppMessage</code>. This class is where you return the view hierarchy Braze shows for each message.

```kotlin
import android.app.Activity
import android.view.View
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.IInAppMessageViewFactory

class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
    override fun createInAppMessageView(
        activity: Activity,
        inAppMessage: IInAppMessage
    ): View {
        TODO()
    }
}
```

Replace <code>TODO()</code> after you add the default factory delegation and extras handling in the next steps.

### Step 4: Delegate to Braze's default factory

Instead of building every in-app message from scratch, obtain Braze's default factory for the current message type, create the default view, then modify it. That keeps standard behavior for layout and click handling while you layer on styling.

```kotlin
val defaultFactory =
    BrazeInAppMessageManager.getInstance()
        .getDefaultInAppMessageViewFactory(inAppMessage)
        ?: throw IllegalStateException("Braze default IAM view factory is missing")
val iamView = defaultFactory
    .createInAppMessageView(activity, inAppMessage)
    ?: throw IllegalStateException("Braze default IAM view is null")
```

If either the default factory or the created view is missing, treat it as an SDK or integration error and fail fast so you notice it during testing.

### Step 5: Access key-value pairs from extras

Campaign and Canvas key-value pairs arrive on the message as string entries in <code>inAppMessage.extras</code>. Read the keys your team agrees on (for example, a flag that selects which customizations apply and a color string), then update the default view when those values are present.

```kotlin
import android.graphics.Color

val extras = inAppMessage.extras ?: emptyMap()
val customization = extras["customization"]
val overrideColor = extras["custom-color"]
if (customization == "slideup-attributes" && overrideColor != null) {
    try {
        iamView.setBackgroundColor(Color.parseColor(overrideColor))
    } catch (_: IllegalArgumentException) {
    }
}
return iamView
```

Invalid color strings throw <code>IllegalArgumentException</code> from <code>Color.parseColor()</code>; catch and skip so a bad payload doesn't crash the app.

### Step 6: Register the custom factory

After you configure Braze, set your factory on <code>BrazeInAppMessageManager</code> so all in-app messages use your implementation.

```kotlin
BrazeInAppMessageManager.getInstance()
    .setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
```

Register the factory once during application startup, after <code>Braze.configure()</code> and alongside your lifecycle callback registration.

### Putting it all together

The following setup matches the steps above: verbose logging (optional), SDK configuration, lifecycle registration, and a custom factory that reads <code>customization</code> and <code>custom-color</code> from extras. The preview shows a static phone mockup with a slide-up style message at the bottom using a custom background color.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-android-iam-full">MainApplication.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-android-iam-full">CustomInAppMessageViewFactory.kt</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-android-iam-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-kotlin">package com.example.brazedevlab

import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger
import com.braze.ui.inappmessage.BrazeInAppMessageManager

class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        BrazeLogger.logLevel = Log.VERBOSE
        val brazeConfig = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, brazeConfig)
        registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
        BrazeInAppMessageManager.getInstance()
            .setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-kotlin">package com.example.brazedevlab

import android.app.Activity
import android.graphics.Color
import android.view.View
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.IInAppMessageViewFactory

class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
    override fun createInAppMessageView(
        activity: Activity,
        inAppMessage: IInAppMessage
    ): View {
        val defaultFactory =
            BrazeInAppMessageManager.getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage)
                ?: throw IllegalStateException("Braze default IAM view factory is missing")
        val iamView = defaultFactory
            .createInAppMessageView(activity, inAppMessage)
            ?: throw IllegalStateException("Braze default IAM view is null")
        val extras = inAppMessage.extras ?: emptyMap()
        val customization = extras["customization"]
        val overrideColor = extras["custom-color"]
        if (customization == "slideup-attributes" && overrideColor != null) {
            try {
                iamView.setBackgroundColor(Color.parseColor(overrideColor))
            } catch (_: IllegalArgumentException) {
            }
        }
        return iamView
    }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-iam-full" class="braze-tutorial-iframe" title="Android in-app message styling preview with slide-up and custom color"></iframe>
    </div>
  </div>
</div>

The <code>BrazeLogger.logLevel</code> line is optional. Remove it, along with any other debug-only settings, before you release to production.

### Next steps

- [About in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/) — how in-app messages work across channels and use cases.
- [Customizing in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/customization/) — more customization options beyond key-value pairs.
- [Android SDK reference](https://braze-inc.github.io/braze-android-sdk/kdoc/) — full API documentation for the Android SDK.

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
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 28px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); display: flex; flex-direction: column; min-height: 380px; }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 4px 20px; font-size: 10px; display: flex; justify-content: space-between; }' +
      '.phone-appbar { background: #1B2536; color: #fff; padding: 12px 16px; font-weight: 600; font-size: 15px; }' +
      '.phone-body { background: #fafafa; flex: 1; display: flex; flex-direction: column; min-height: 280px; position: relative; padding: 16px; padding-bottom: 0; }' +
      '.phone-scroll { flex: 1; padding-bottom: 12px; }' +
      '.content-card { background: #fff; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 10px; }' +
      '.slideup-iam { margin-top: auto; background: #5b21b6; color: #fff; padding: 14px 16px 18px; border-radius: 12px 12px 0 0; box-shadow: 0 -4px 24px rgba(0,0,0,0.12); }' +
      '.slideup-iam h3 { font-size: 15px; font-weight: 700; margin: 0 0 6px; }' +
      '.slideup-iam p { font-size: 12px; line-height: 1.45; opacity: 0.92; margin: 0 0 12px; }' +
      '.slideup-row { display: flex; align-items: center; justify-content: space-between; gap: 10px; }' +
      '.slideup-cta { display: inline-block; background: rgba(255,255,255,0.2); color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 12px; font-weight: 600; text-decoration: none; }' +
      '.slideup-dismiss { color: rgba(255,255,255,0.75); font-size: 11px; text-decoration: none; }';

    var fullPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + phoneStyles +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>LTE</span></div>' +
      '<div class="phone-appbar">MyApp</div>' +
      '<div class="phone-body">' +
      '<div class="phone-scroll">' +
      '<div class="content-card">' +
      '<div style="font-weight:600;font-size:13px;color:#1B2536;">Home</div>' +
      '<div style="color:#64748b;font-size:11px;margin-top:4px;">Screen content continues behind the slide-up message.</div>' +
      '</div>' +
      '</div>' +
      '<div class="slideup-iam">' +
      '<div class="slideup-row">' +
      '<h3 style="flex:1;">Limited offer</h3>' +
      '<a class="slideup-dismiss" href="javascript:void(0)">Close</a>' +
      '</div>' +
      '<p>Thanks for subscribing. Here is 15% off your next order. Tap below to apply it at checkout.</p>' +
      '<a class="slideup-cta" href="javascript:void(0)">Shop now</a>' +
      '</div>' +
      '</div></div></body></html>';

    var previews = {
      'braze-preview-android-iam-full': fullPreview
    };

    function forcePopulatePreviews() {
      Object.keys(previews).forEach(function(id) {
        var iframe = document.getElementById(id);
        if (iframe) {
          iframe.srcdoc = previews[id];
        }
      });
    }

    forcePopulatePreviews();

    var populateAttempts = 0;
    var populateInterval = setInterval(function() {
      forcePopulatePreviews();
      populateAttempts++;
      if (populateAttempts >= 30) clearInterval(populateInterval);
    }, 500);

    document.addEventListener('click', function(e) {
      var target = e.target;
      if (!(target instanceof Element)) {
        target = target.parentElement;
      }
      if (!(target instanceof Element)) return;
      if (target.closest('.tab_toggle, .sdk-tab_toggle, .sdk-tab_toggle_only, .ab-nav-tabs, .sdk-ab-nav-tabs, .braze-tutorial-tab, [class*="tab"]')) {
        setTimeout(forcePopulatePreviews, 100);
        setTimeout(forcePopulatePreviews, 300);
        setTimeout(forcePopulatePreviews, 600);
      }
    }, true);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBrazeTutorial);
  } else {
    initBrazeTutorial();
  }
})();
</script>
{% endraw %}
