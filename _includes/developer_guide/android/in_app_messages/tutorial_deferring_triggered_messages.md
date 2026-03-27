{% multi_lang_include developer_guide/prerequisites/android.md %}

You'll also need to [enable in-app messages for Android]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=android#android_enabling-in-app-messages).

## Deferring and restoring triggered messages for Android

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Android" %}

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
  <p>This tutorial shows how to defer triggered in-app messages on Android until your app is ready to show them, then restore display with a single call. You expose your <code>Application</code> as a singleton, register Braze lifecycle callbacks, and set a custom <code>IInAppMessageManagerListener</code> that returns <code>InAppMessageOperation.DISPLAY_LATER</code> or <code>InAppMessageOperation.DISPLAY_NOW</code> based on a flag. When you set the flag and call <code>requestDisplayInAppMessage()</code>, the deferred message can appear. Each step adds one piece of the flow; the last section shows <code>MainApplication.kt</code> and <code>MainActivity.kt</code> together with a preview that mimics tapping <strong>Show Deferred IAM</strong> and seeing a slide-up message.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Create a singleton <code>Application</code> using a <code>companion object</code></li>
    <li>Turn on verbose SDK logging during development (optional)</li>
    <li>Register <code>BrazeActivityLifecycleCallbackListener</code> with your <code>Application</code></li>
    <li>Set a custom <code>IInAppMessageManagerListener</code> on <code>BrazeInAppMessageManager</code></li>
    <li>Use a <code>showMessage</code> flag so <code>beforeInAppMessageDisplayed()</code> returns <code>DISPLAY_NOW</code> or <code>DISPLAY_LATER</code></li>
    <li>Implement <code>showDeferredMessage()</code> to update the flag and call <code>requestDisplayInAppMessage()</code></li>
    <li>Trigger deferred display from your UI (for example, a button or tap handler)</li>
  </ul>
</div>

### Step 1: Create a singleton Application instance

Braze needs a stable place to hold display state and call <code>requestDisplayInAppMessage()</code> from anywhere in your app. Subclass <code>Application</code>, keep a private reference to the instance, and expose it through a <code>companion object</code> so activities and composables can reach the same object.

```kotlin
import android.app.Application

class MainApplication : Application() {
    companion object {
        private var instance: MainApplication? = null
        fun getInstance(): MainApplication = instance!!
    }

    override fun onCreate() {
        super.onCreate()
        instance = this
    }
}
```

Register this class in your <code>AndroidManifest.xml</code> with <code>android:name</code> so the system instantiates it at process start.

### Step 2: Enable debugging (optional)

During development, set the Braze log level to verbose so Logcat shows detailed SDK activity, including in-app message handling. Add this near the start of <code>Application.onCreate()</code>.

```kotlin
import android.util.Log
import com.braze.support.BrazeLogger

BrazeLogger.logLevel = Log.VERBOSE
```

Remove this assignment before you ship to production so you don't log sensitive detail in release builds.

### Step 3: Register activity lifecycle callbacks

In-app messages rely on activity lifecycle events. Register Braze's listener on your <code>Application</code> so every activity's lifecycle is forwarded to the SDK.

```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
```

Call this after <code>Braze.configure()</code> in <code>onCreate()</code>, alongside your other startup setup.

### Step 4: Set up an in-app message listener

Use <code>BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()</code> with an object that implements <code>IInAppMessageManagerListener</code>. The SDK calls <code>beforeInAppMessageDisplayed()</code> for each message before it renders, so your code can defer or allow display.

```kotlin
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.InAppMessageOperation
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener

BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
    override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
        return InAppMessageOperation.DISPLAY_LATER
    }
})
```

Register the listener once during application startup, after <code>Braze.configure()</code>. Returning <code>DISPLAY_LATER</code> for now defers every message until you add the flag in the next step.

### Step 5: Create conditional logic

Add a boolean property on your <code>Application</code> (for example, <code>showMessage</code>) that your UI can toggle. In <code>beforeInAppMessageDisplayed()</code>, return <code>InAppMessageOperation.DISPLAY_NOW</code> when you want Braze to show the message immediately, and <code>InAppMessageOperation.DISPLAY_LATER</code> when you want to hold it until you call <code>requestDisplayInAppMessage()</code>.

```kotlin
private var showMessage = false

BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
    override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
        return if (showMessage) {
            InAppMessageOperation.DISPLAY_NOW
        } else {
            InAppMessageOperation.DISPLAY_LATER
        }
    }
})
```

While <code>showMessage</code> is false, eligible triggered messages stay queued for a later display opportunity instead of appearing on screen.

### Step 6: Create a method for displaying deferred messages

Add a method on your <code>Application</code> that sets <code>showMessage</code> and asks the in-app message manager to try showing a deferred message again.

```kotlin
fun showDeferredMessage(show: Boolean) {
    showMessage = show
    BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()
}
```

Call this when your screen is ready (for example, after navigation finishes or a modal closes). Setting <code>show</code> to true before <code>requestDisplayInAppMessage()</code> lets the listener return <code>DISPLAY_NOW</code> for the pending message.

### Step 7: Trigger the method from your UI

From an activity, fragment, or composable, obtain your <code>Application</code> singleton and call <code>showDeferredMessage(true)</code> when the user takes an action that should reveal the deferred message.

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ContentView()
        }
    }
}

@Composable
fun ContentView() {
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        Button(onClick = {
            MainApplication.getInstance().showDeferredMessage(true)
        }) {
            Text("Show Deferred IAM")
        }
    }
}
```

Wire the same call into any control that fits your product flow; the important part is setting the flag and invoking <code>requestDisplayInAppMessage()</code> together.

### Putting it all together

The following setup matches the steps above: a singleton <code>Application</code>, optional verbose logging, SDK configuration, lifecycle registration, a listener that defers or shows based on <code>showMessage</code>, and a Compose screen that calls <code>showDeferredMessage(true)</code>. The preview shows an Android-style phone mockup with a <strong>Show Deferred IAM</strong> button; tap it to reveal a slide-up in-app message below.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-android-defer-full">MainApplication.kt</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-android-defer-full">MainActivity.kt</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-android-defer-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-kotlin">package com.example.brazedevlab

import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.configuration.BrazeConfig
import com.braze.models.inappmessage.IInAppMessage
import com.braze.support.BrazeLogger
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.InAppMessageOperation
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener

class MainApplication : Application() {
    companion object {
        private var instance: MainApplication? = null
        fun getInstance(): MainApplication = instance!!
    }

    private var showMessage = false

    override fun onCreate() {
        super.onCreate()
        instance = this
        BrazeLogger.logLevel = Log.VERBOSE
        val brazeConfig = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, brazeConfig)
        registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
        BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
            override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
                return if (showMessage) {
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    InAppMessageOperation.DISPLAY_LATER
                }
            }
        })
    }

    fun showDeferredMessage(show: Boolean) {
        showMessage = show
        BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-kotlin">package com.example.brazedevlab

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ContentView()
        }
    }
}

@Composable
fun ContentView() {
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        Button(onClick = {
            MainApplication.getInstance().showDeferredMessage(true)
        }) {
            Text("Show Deferred IAM")
        }
    }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-android-defer-full" class="braze-tutorial-iframe" title="Android deferred in-app message: button and slide-up message"></iframe>
    </div>
  </div>
</div>

The <code>BrazeLogger.logLevel</code> line is optional. Remove it, along with any other debug-only settings, before you release to production.

### Next steps

- [About in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/) — how in-app messages work across channels and use cases.
- [Customizing in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/customization/) — styling, behavior, and integration options.
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
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 28px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); display: flex; flex-direction: column; }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 4px 20px; font-size: 10px; display: flex; justify-content: space-between; }' +
      '.phone-appbar { background: #1B2536; color: #fff; padding: 12px 16px; font-weight: 600; font-size: 15px; }' +
      '.phone-body { background: #fafafa; flex: 1; display: flex; flex-direction: column; min-height: 300px; padding: 16px; padding-bottom: 18px; }' +
      '.phone-scroll { flex: 1; min-height: 40px; }' +
      '.content-card { background: #fff; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 14px; }' +
      '.defer-btn { display: block; width: 100%; padding: 12px 16px; border: none; border-radius: 8px; background: #00B3E6; color: #fff; font-size: 14px; font-weight: 600; font-family: inherit; cursor: pointer; margin-bottom: 0; }' +
      '.defer-btn:active { opacity: 0.92; }' +
      '.slideup-iam { margin-top: 12px; background: linear-gradient(135deg, #1B2536 0%, #2d4a6f 50%, #1a7f8a 100%); color: #fff; padding: 14px 16px 18px; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.12); display: none; }' +
      '.slideup-iam.is-visible { display: block; }' +
      '.slideup-iam h3 { font-size: 15px; font-weight: 700; margin: 0 0 6px; }' +
      '.slideup-iam p { font-size: 12px; line-height: 1.45; opacity: 0.92; margin: 0 0 12px; }' +
      '.slideup-row { display: flex; align-items: center; justify-content: space-between; gap: 10px; }' +
      '.slideup-cta { display: inline-block; background: #00B3E6; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 12px; font-weight: 600; text-decoration: none; }' +
      '.slideup-dismiss { color: rgba(255,255,255,0.75); font-size: 11px; text-decoration: none; }';

    var phoneInner =
      '<div class="phone-scroll">' +
      '<div class="content-card">' +
      '<div style="font-weight:600;font-size:13px;color:#1B2536;">Home</div>' +
      '<div style="color:#64748b;font-size:11px;margin-top:4px;">Tap the button to reveal the deferred slide-up message.</div>' +
      '</div></div>' +
      '<button type="button" class="defer-btn" id="deferShowBtn">Show Deferred IAM</button>' +
      '<div class="slideup-iam" id="deferSlideup">' +
      '<div class="slideup-row">' +
      '<h3 style="flex:1;">You have a message</h3>' +
      '<a class="slideup-dismiss" href="javascript:void(0)">Close</a>' +
      '</div>' +
      '<p>Thanks for your patience. Here is the offer you deferred.</p>' +
      '<a class="slideup-cta" href="javascript:void(0)">Continue</a>' +
      '</div>';

    var deferIframeScript = '(function(){var b=document.getElementById("deferShowBtn");var s=document.getElementById("deferSlideup");if(b&&s){b.addEventListener("click",function(){s.classList.add("is-visible");});}})();';

    var fullPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + phoneStyles +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>LTE</span></div>' +
      '<div class="phone-appbar">MyApp</div>' +
      '<div class="phone-body">' + phoneInner + '</div></div>' +
      '<scr' + 'ipt>' + deferIframeScript + '</scr' + 'ipt>' +
      '</body></html>';

    var previews = {
      'braze-preview-android-defer-full': fullPreview
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
