{% multi_lang_include developer_guide/prerequisites/swift.md %}

You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Deferring and restoring triggered messages for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Swift" %}

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
  <p>This tutorial shows how to defer a triggered in-app message when it first arrives, then show it later from your own UI. You implement <code>BrazeInAppMessageUIDelegate</code>, return <code>.reenqueue</code> until you're ready, then call <code>presentNext()</code> on <code>BrazeInAppMessageUI</code> after you set a flag. Each step adds one part of the flow; the final sandbox wires a SwiftUI <code>App</code>, <code>AppDelegate</code>, and a button that restores the deferred message.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Implement <code>BrazeInAppMessageUIDelegate</code> on your <code>AppDelegate</code></li>
    <li>Enable debug logging during development (optional)</li>
    <li>Set up <code>BrazeInAppMessageUI</code>, assign the delegate, and set the in-app message presenter</li>
    <li>Override <code>DisplayChoice</code> to return <code>.reenqueue</code> or <code>.now</code> based on your own state</li>
    <li>Add a method that updates your flag and calls <code>presentNext()</code> to show a deferred message</li>
    <li>Trigger that method from SwiftUI (or another UI layer) when the user taps a control</li>
  </ul>
</div>

### Step 1: Implement `BrazeInAppMessageUIDelegate`

Conform your `AppDelegate` to `UIApplicationDelegate` and `BrazeInAppMessageUIDelegate`. Store a static `shared` reference, keep a `Braze` instance and a `showMessage` flag, and initialize Braze in `application(_:didFinishLaunchingWithOptions:)`.

```swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static private(set) var shared: AppDelegate!

    private var braze: Braze!
    public var showMessage: Bool = false

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        AppDelegate.shared = self
        let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")
        braze = Braze(configuration: configuration)
        return true
    }
}
```

The `showMessage` property is the signal your delegate uses later: when it's `false`, you defer; when it's `true`, you allow the message to display.

### Step 2: Enable debugging (optional)

Set `configuration.logger.level` to `.debug` on the configuration object before you pass it to `Braze(configuration:)`. This prints detailed SDK activity to the Xcode console while you test defer and restore behavior.

```swift
configuration.logger.level = .debug
```

Remove this line or lower the level before you ship to production.

### Step 3: Set up your Braze UI and delegate

Create a `BrazeInAppMessageUI` instance, assign `self` as its `delegate`, and set `braze.inAppMessagePresenter` to that UI object. The default implementation presents in-app messages; the delegate lets you control timing with `displayChoiceForMessage`.

```swift
let ui = BrazeInAppMessageUI()
ui.delegate = self
braze.inAppMessagePresenter = ui
```

Keep a strong reference to the UI object for as long as Braze needs it (here it is retained by the presenter property).

### Step 4: Override `DisplayChoice` with conditional logic

Implement [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb). Return `.reenqueue` to put the message back in the queue when `showMessage` is `false`, and `.now` to display it when you're ready.

```swift
func inAppMessage(
    _ ui: BrazeInAppMessageUI,
    displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice {
    if !showMessage {
        return .reenqueue
    }
    return .now
}
```

While messages are re-queued, nothing is shown until you call `presentNext()` on the same `BrazeInAppMessageUI` instance (see the next step).

### Step 5: Create a method to show deferred messages

Add a method that sets `showMessage` and asks the presenter to show the next eligible message. Cast `braze.inAppMessagePresenter` to `BrazeInAppMessageUI` so you can call `presentNext()`.

```swift
func showDeferredMessage(showMessage: Bool) {
    self.showMessage = showMessage
    (braze.inAppMessagePresenter as? BrazeInAppMessageUI)?.presentNext()
}
```

Call this after you've set `showMessage` to `true` so the delegate returns `.now` for the next presentation attempt.

### Step 6: Trigger the method from your UI

From SwiftUI, call `AppDelegate.shared.showDeferredMessage(showMessage: true)` when the user taps a button or another control. Ensure your `@main` `App` type uses `@UIApplicationDelegateAdaptor` so `AppDelegate.shared` is valid.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Button("Show Deferred IAM") {
                AppDelegate.shared.showDeferredMessage(showMessage: true)
            }
        }
        .padding()
    }
}
```

Connect this view from your `WindowGroup` in the app entry point file.

### Putting it all together

The following example ties together initialization, the delegate, deferral with `.reenqueue`, and a SwiftUI button that calls `showDeferredMessage(showMessage:)`. The preview shows an iPhone mockup with **Show Deferred IAM** and a slide-up in-app message after deferral is cleared.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-swift-defer-full">AppDelegate.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-swift-defer-full">IAMDeferApp.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="2" data-sandbox="sandbox-swift-defer-full">ContentView.swift</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-swift-defer-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-swift">import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static private(set) var shared: AppDelegate!

    private var braze: Braze!
    public var showMessage: Bool = false

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -&gt; Bool {
        AppDelegate.shared = self
        let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug
        braze = Braze(configuration: configuration)
        let ui = BrazeInAppMessageUI()
        ui.delegate = self
        braze.inAppMessagePresenter = ui
        return true
    }

    func inAppMessage(
        _ ui: BrazeInAppMessageUI,
        displayChoiceForMessage message: Braze.InAppMessage
    ) -&gt; BrazeInAppMessageUI.DisplayChoice {
        if !showMessage {
            return .reenqueue
        }
        return .now
    }

    func showDeferredMessage(showMessage: Bool) {
        self.showMessage = showMessage
        (braze.inAppMessagePresenter as? BrazeInAppMessageUI)?.presentNext()
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import SwiftUI

@main
struct IAMDeferApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Button("Show Deferred IAM") {
                AppDelegate.shared.showDeferredMessage(showMessage: true)
            }
        }
        .padding()
    }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-swift-defer-full" class="braze-tutorial-iframe" title="Swift defer and restore in-app message preview"></iframe>
    </div>
  </div>
</div>

The `configuration.logger.level = .debug` line in `AppDelegate.swift` is optional. Remove it before you deploy to production.

### Next steps

- [About in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/) — how in-app messages work across channels and use cases.
- [Customizing in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/customization/) — styling and behavior options beyond deferral.
- [Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/) — full API documentation for the Swift SDK.

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
      'body { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", sans-serif; background: #f5f7f9; padding: 12px; display: flex; justify-content: center; align-items: flex-start; }' +
      '.phone-wrap { text-align: center; }' +
      '.phone-caption { font-size: 11px; font-weight: 600; color: #64748b; margin-bottom: 8px; letter-spacing: 0.02em; }' +
      '.phone { width: 168px; border-radius: 24px; overflow: hidden; border: 2.5px solid #1B2536; box-shadow: 0 6px 20px rgba(0,0,0,0.10); }' +
      '.phone-status { background: #1B2536; color: rgba(255,255,255,0.7); padding: 4px 12px; font-size: 8px; display: flex; justify-content: space-between; }' +
      '.phone-navbar { background: #f8f9fa; padding: 8px 10px; font-weight: 600; font-size: 12px; color: #1B2536; text-align: center; border-bottom: 0.5px solid #e2e8f0; }' +
      '.phone-body { background: #f8f9fa; min-height: 200px; display: flex; flex-direction: column; position: relative; }' +
      '.main-fill { flex: 1; padding: 14px 12px 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; }' +
      '.iam-btn { display: inline-block; background: #00B3E6; color: #fff; border: none; padding: 10px 16px; border-radius: 10px; font-size: 11px; font-weight: 600; text-decoration: none; cursor: pointer; box-shadow: 0 2px 6px rgba(0,179,230,0.35); }' +
      '.content-line { height: 6px; background: #e2e8f0; border-radius: 3px; margin-bottom: 6px; width: 100%; max-width: 120px; }' +
      '.content-line.short { width: 70%; }' +
      '.slideup-wrap { padding: 0 8px 10px; }' +
      '.slideup { background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.12); padding: 10px 12px; border: 1px solid #e2e8f0; }' +
      '.slideup-title { font-size: 11px; font-weight: 700; color: #1B2536; margin-bottom: 3px; }' +
      '.slideup-body { font-size: 9px; color: #64748b; line-height: 1.4; }' +
      '.slideup-cta { display: inline-block; margin-top: 6px; font-size: 9px; font-weight: 600; color: #00B3E6; text-decoration: none; }';

    var deferPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + phoneStyles +
      '</style></head><body>' +
      '<div class="phone-wrap">' +
      '<div class="phone-caption">After tapping Show Deferred IAM</div>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>5G</span></div>' +
      '<div class="phone-navbar">MyApp</div>' +
      '<div class="phone-body">' +
      '<div class="main-fill">' +
      '<a href="javascript:void(0)" class="iam-btn">Show Deferred IAM</a>' +
      '<div style="margin-top:12px;width:100%;max-width:120px;">' +
      '<div class="content-line short"></div>' +
      '<div class="content-line"></div>' +
      '</div></div>' +
      '<div class="slideup-wrap">' +
      '<div class="slideup">' +
      '<div class="slideup-title">Welcome back</div>' +
      '<div class="slideup-body">Here is the in-app message that was deferred until you were ready.</div>' +
      '<a href="javascript:void(0)" class="slideup-cta">OK</a>' +
      '</div></div></div></div></div></body></html>';

    var previews = {
      'braze-preview-swift-defer-full': deferPreview
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
