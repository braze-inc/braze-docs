{% multi_lang_include developer_guide/prerequisites/swift.md %}

You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Customizing message styling using key-value pairs for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Swift" %}

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
  <p>This tutorial shows how to style slide-up in-app messages from key-value pairs you attach in the Braze dashboard. You implement <code>BrazeInAppMessageUIDelegate</code>, read <code>message.extras</code> in <code>inAppMessage(_:prepareWith:)</code>, and update <code>context.attributes?.slideup</code> before the message appears. Each step adds one piece of the flow; the final sandbox combines a SwiftUI app entry point with a complete <code>AppDelegate</code> example.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Implement <code>BrazeInAppMessageUIDelegate</code> on your <code>AppDelegate</code></li>
    <li>Enable debug logging during development (optional)</li>
    <li>Prepare messages before display in <code>inAppMessage(_:prepareWith:)</code></li>
    <li>Read customization values from <code>message.extras</code> key-value pairs</li>
    <li>Update slide-up styling through <code>context.attributes?.slideup</code></li>
  </ul>
</div>

### Step 1: Implement `BrazeInAppMessageUIDelegate`

Conform your `AppDelegate` to `BrazeInAppMessageUIDelegate`, keep a static `braze` reference, and in `application(_:didFinishLaunchingWithOptions:)` create `Braze.Configuration`, initialize `Braze`, set `BrazeInAppMessageUI`'s `delegate` to `self`, and assign `braze.inAppMessagePresenter` so the SDK calls your delegate before showing a message.

```swift
class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
  var window: UIWindow?
  static var braze: Braze?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )

    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    let inAppMessageUI = BrazeInAppMessageUI()
    inAppMessageUI.delegate = self
    braze.inAppMessagePresenter = inAppMessageUI

    return true
  }
}
```

### Step 2: Enable debugging (optional)

Set `configuration.logger.level` to `.debug` before you pass the configuration into `Braze(configuration:)`. That prints detailed SDK activity to the Xcode console while you test in-app messages and delegate behavior.

```swift
configuration.logger.level = .debug
```

Remove this line or lower the level before you ship to production.

### Step 3: Prepare messages before display

Implement `inAppMessage(_:prepareWith:)` on your `AppDelegate`. The SDK invokes this method with an in-out `PresentationContext` so you can adjust how each message appears.

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
}
```

Add your styling logic inside this method; the next steps read key-value data and mutate slide-up attributes.

### Step 4: Access key-value pairs from `message.extras`

Read values from `context.message.extras`. Keys and values you configure on the message in the Braze dashboard arrive here as dictionary entries. Cast them to the types your styling code expects.

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  let customization = context.message.extras["customization"] as? String
}
```

Use predictable keys (for example `customization`) so your app branches only when you intend to override defaults.

### Step 5: Update the message's styling attributes

When `customization` matches the value you set in the dashboard (here `slideup-attributes`), adjust `context.attributes?.slideup`: set `font`, `imageSize`, `cornerRadius`, `imageCornerRadius`, and on iOS 13 or later `cornerCurve` and `imageCornerCurve`, then write the struct back to `context.attributes?.slideup`.

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  let customization = context.message.extras["customization"] as? String

  if customization == "slideup-attributes" {
    var attributes = context.attributes?.slideup
    attributes?.font = UIFont(name: "Chalkduster", size: 17)!
    attributes?.imageSize = CGSize(width: 65, height: 65)
    attributes?.cornerRadius = 20
    attributes?.imageCornerRadius = 10
    if #available(iOS 13.0, *) {
      attributes?.cornerCurve = .continuous
      attributes?.imageCornerCurve = .continuous
    }
    context.attributes?.slideup = attributes
  }
}
```

If the named font is unavailable at runtime, supply a fallback `UIFont` so the message still renders.

### Putting it all together

The following example wires Braze at launch, sets the in-app message delegate, and styles slide-ups when `customization` equals `slideup-attributes` in message extras. Connect your SwiftUI app to this `AppDelegate` with `@UIApplicationDelegateAdaptor`. The preview shows a static iPhone mockup with a rounded slide-up at the bottom.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-swift-iam-full">AppDelegate.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-swift-iam-full">SampleApp.swift</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-swift-iam-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-swift">import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
  var window: UIWindow?
  static var braze: Braze?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    configuration.logger.level = .debug

    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    let inAppMessageUI = BrazeInAppMessageUI()
    inAppMessageUI.delegate = self
    braze.inAppMessagePresenter = inAppMessageUI

    return true
  }

  func inAppMessage(
    _ ui: BrazeInAppMessageUI,
    prepareWith context: inout BrazeInAppMessageUI.PresentationContext
  ) {
    let customization = context.message.extras["customization"] as? String

    if customization == "slideup-attributes" {
      var attributes = context.attributes?.slideup
      attributes?.font = UIFont(name: "Chalkduster", size: 17)!
      attributes?.imageSize = CGSize(width: 65, height: 65)
      attributes?.cornerRadius = 20
      attributes?.imageCornerRadius = 10
      if #available(iOS 13.0, *) {
        attributes?.cornerCurve = .continuous
        attributes?.imageCornerCurve = .continuous
      }
      context.attributes?.slideup = attributes
    }
  }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import SwiftUI

@main
struct SampleApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

  var body: some Scene {
    WindowGroup {
      YourView()
    }
  }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-swift-iam-full" class="braze-tutorial-iframe" title="Swift in-app message slide-up styling preview"></iframe>
    </div>
  </div>
</div>

The `configuration.logger.level = .debug` line in `AppDelegate.swift` is optional. Remove it before you deploy to production.

### Next steps

Dig deeper into in-app messages and the Swift SDK APIs:

- [About in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/)
- [Customizing in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/customization/)
- [Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/)

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
      'body { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", sans-serif; background: #f5f7f9; padding: 12px; }' +
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 32px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 6px 20px; font-size: 10px; display: flex; justify-content: space-between; }' +
      '.phone-navbar { background: #f8f9fa; padding: 12px 16px; font-weight: 600; font-size: 16px; color: #1B2536; text-align: center; border-bottom: 0.5px solid #e2e8f0; }' +
      '.phone-body { background: #f8f9fa; display: flex; flex-direction: column; min-height: 300px; }' +
      '.main-fill { flex: 1; padding: 16px 16px 8px; }' +
      '.slideup-wrap { padding: 0 12px 14px; }' +
      '.slideup { background: #fff; border-radius: 20px; box-shadow: 0 4px 24px rgba(0,0,0,0.14); display: flex; align-items: center; gap: 12px; padding: 14px 16px; border: 1px solid #e2e8f0; }' +
      '.slideup-img { width: 65px; height: 65px; border-radius: 10px; background: linear-gradient(135deg, #cbd5e1, #e2e8f0); flex-shrink: 0; }' +
      '.slideup-text { font-family: Chalkduster, "Marker Felt", "Comic Sans MS", cursive; font-size: 15px; color: #1B2536; line-height: 1.35; flex: 1; }' +
      '.slideup-dismiss { color: #94a3b8; font-size: 22px; line-height: 1; text-decoration: none; flex-shrink: 0; }';

    var slideupPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + phoneStyles +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>5G</span></div>' +
      '<div class="phone-navbar">MyApp</div>' +
      '<div class="phone-body">' +
      '<div class="main-fill">' +
      '<div style="color:#64748b;font-size:13px;">Your screen content</div>' +
      '<a href="javascript:void(0)" style="display:inline-block;margin-top:12px;color:#00B3E6;font-size:13px;font-weight:600;">View offer</a>' +
      '</div>' +
      '<div class="slideup-wrap">' +
      '<div class="slideup">' +
      '<div class="slideup-img"></div>' +
      '<div class="slideup-text">Your slide-up message uses custom font, image size, and corner radii.</div>' +
      '<a href="javascript:void(0)" class="slideup-dismiss" aria-label="Dismiss">&times;</a>' +
      '</div></div></div></div></body></html>';

    var previews = {
      'braze-preview-swift-iam-full': slideupPreview
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
