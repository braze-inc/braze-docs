{% multi_lang_include developer_guide/prerequisites/web.md %}

However, no additional setup is required.

## Deferring and restoring triggered messages for Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Web" %}

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
  <p>This tutorial walks you through deferring triggered in-app messages so you can show them later—for example, after navigation or when the user taps a control. Each step covers one part of the flow: turning off automatic display, optional logging, subscribing for messages, deferring with <code>deferInAppMessage</code>, reading back with <code>getDeferredInAppMessage</code>, and calling <code>showInAppMessage</code> when you are ready. The last section shows the full example next to a preview of a page with a <strong>Show Deferred Message</strong> button and a slideup-style message below it.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Remove calls to <code>automaticallyShowInAppMessages</code> so custom logic can run</li>
    <li>Enable <code>enableLogging</code> during development (optional)</li>
    <li>Subscribe with <code>subscribeToInAppMessage</code> whenever a message is triggered</li>
    <li>Defer a message with <code>deferInAppMessage</code> so Braze persists it for a later page load</li>
    <li>Retrieve a stored message with <code>getDeferredInAppMessage</code></li>
    <li>Pass that object to <code>showInAppMessage</code> when you want the deferred UI</li>
    <li>Call <code>showInAppMessage</code> directly in the subscriber when you want immediate display instead</li>
  </ul>
</div>

### Step 1: Remove calls to `automaticallyShowInAppMessages`

If you call `braze.automaticallyShowInAppMessages()`, the SDK shows every eligible message with the built-in UI. That runs outside your subscriber, so remove any existing calls when you handle display yourself.

Start with an import. Do not call `automaticallyShowInAppMessages()` in your bundle:

```js
import * as braze from "@braze/web-sdk";
```

Leave the rest of your integration as-is aside from removing automatic display.

### Step 2: Enable debugging (optional)

While you integrate, pass `enableLogging: true` in the initializer so the SDK prints diagnostic information to the browser console. Omit this option in production builds.

```js
braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});
```

Verbose logging helps confirm that messages are received and that your callback runs when you expect.

### Step 3: Subscribe to the in-app message callback handler

Register a callback with `subscribeToInAppMessage()`. The SDK invokes it whenever an in-app message is triggered for the current user.

```js
braze.subscribeToInAppMessage(function (message) {
});
```

Register this callback after `initialize()` so you do not miss deliveries during the session.

### Step 4: Defer the message instance

When you are not ready to show the UI, call `deferInAppMessage(message)`. Braze serializes and stores the message so you can surface it on a future page load or after your own conditions are met.

```js
braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true;
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  }
});
```

Replace `shouldDefer` with your own rules (timing, route, feature flags, and so on).

### Step 5: Retrieve a previously deferred message

Elsewhere in your app—such as a button click or route change—call `getDeferredInAppMessage()` to read the stored message. The method returns the deferred instance when one exists, or a falsy value when nothing is queued.

```js
document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
};
```

Point `getElementById` at the DOM node that should trigger display (your markup may use a different id).

### Step 6: Display the deferred message

When `getDeferredInAppMessage()` returns a message, pass it to `showInAppMessage()` so Braze renders the default in-app UI.

```js
document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
  if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
  }
};
```

If you skip this call, the deferred message stays stored until you show or replace it.

### Step 7: Display a message immediately

To show a message as soon as it triggers—instead of deferring—call `showInAppMessage(message)` inside the same `subscribeToInAppMessage` callback, typically in the branch where you do not defer.

```js
braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true;
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  } else {
    braze.showInAppMessage(message);
  }
});
```

Keep `deferInAppMessage` and `showInAppMessage` mutually exclusive for a given delivery so you do not double-handle the same trigger.

### Putting it all together

This example wires initialization, logging, subscription, deferral, and a control that loads and shows the deferred message. Remove `enableLogging` before you ship to production.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0">index.js</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-web-defer-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-javascript">import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true;
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  } else {
    braze.showInAppMessage(message);
  }
});

document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
  if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
  }
};</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-web-defer-full" class="braze-tutorial-iframe" title="Deferred in-app message preview with Show Deferred Message button"></iframe>
    </div>
  </div>
</div>

### Next steps

- [About in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/) — concepts, triggers, and eligibility.
- [Customizing in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/customization/) — dashboard and SDK customization options.
- [Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) — full API documentation for the Web SDK.

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
      '.text-muted { color: #64748b; font-size: 14px; line-height: 1.6; }' +
      '.defer-btn { display: inline-block; margin-top: 8px; margin-bottom: 20px; background: #00B3E6; color: #fff; border: none; padding: 10px 20px; border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; text-decoration: none; }' +
      '.defer-btn:hover { filter: brightness(0.95); }';

    var navBar = '<div class="app-nav">' +
      '<span class="app-nav-brand">MyApp</span>' +
      '<nav class="app-nav-links">' +
      '<a href="javascript:void(0)">Home</a><a href="javascript:void(0)">Products</a><a href="javascript:void(0)">About</a>' +
      '</nav></div>';

    var slideupBg = '#0369a1';
    var deferFullPreview = '<!DOCTYPE html><html><head><style>' + sharedStyles +
      '.iam-slideup { margin-top: 0; padding: 16px 20px 20px; border-radius: 12px 12px 0 0; box-shadow: 0 4px 24px rgba(27,37,54,0.14); color: #fff; background: linear-gradient(135deg, ' + slideupBg + ' 0%, #0c4a6e 100%); max-width: 100%; }' +
      '.iam-slideup-head { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.88; margin-bottom: 6px; }' +
      '.iam-slideup-title { font-size: 17px; font-weight: 700; margin: 0 0 6px; }' +
      '.iam-slideup-meta { font-size: 12px; opacity: 0.92; margin: 0 0 14px; line-height: 1.45; }' +
      '.iam-slideup-cta { display: inline-block; background: rgba(255,255,255,0.22); color: #fff; padding: 9px 20px; border-radius: 6px; font-size: 13px; font-weight: 600; text-decoration: none; }' +
      '</style></head><body>' +
      navBar +
      '<div class="app-content">' +
      '<h2 class="page-title">Promotions</h2>' +
      '<p class="text-muted">After you defer a trigger, call <code>getDeferredInAppMessage</code> and <code>showInAppMessage</code> from your control—for example, when the user clicks <strong>Show Deferred Message</strong>.</p>' +
      '<a href="javascript:void(0)" class="defer-btn">Show Deferred Message</a>' +
      '<div class="iam-slideup">' +
      '<div class="iam-slideup-head">In-app message · slideup</div>' +
      '<div class="iam-slideup-title">Your saved offer is ready</div>' +
      '<p class="iam-slideup-meta">Preview: slideup shown below the button after you restore a deferred message with <code>showInAppMessage</code>.</p>' +
      '<a href="javascript:void(0)" class="iam-slideup-cta">Claim offer</a>' +
      '</div>' +
      '</div>' +
      '</body></html>';

    var previews = {
      'braze-preview-web-defer-full': deferFullPreview
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
