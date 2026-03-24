{% multi_lang_include developer_guide/prerequisites/swift.md %}

You'll also need to [enable in-app messages for Swift]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=swift#swift_enabling-in-app-messages).

## Making an inbox with Content Cards for Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Content Card Inbox Swift" %}

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
  <p>This tutorial walks you through building a message inbox with Content Cards using the Braze Swift SDK, SwiftUI for the app entry point, and a UIKit <code>UITableViewController</code>. Each step adds one concept, shows the code, and explains how it fits together.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Configure the Braze SDK with <code>Braze.Configuration</code>, your API key, and endpoint</li>
    <li>Turn on optional debug logging for development</li>
    <li>Create a <code>BrazeInboxViewController</code> subclass of <code>UITableViewController</code></li>
    <li>Subscribe to Content Card updates and call <code>requestRefresh()</code></li>
    <li>Bind card <code>title</code> and <code>description</code> to table cells</li>
    <li>Handle row selection with <code>logClick(using:)</code> and URL opening</li>
    <li>Log impressions with <code>willDisplay</code> and a <code>Set</code> to guard against duplicate logs</li>
  </ul>
</div>

### Step 1: Configure the Braze SDK

Create a `Braze.Configuration` with your SDK API key and endpoint, store a shared `Braze` instance on `AppDelegate`, and initialize the SDK when the app launches. Keeping `AppDelegate.braze` static lets your view controllers access the same instance.

```swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze!

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {

        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        return true
    }
}
```

Replace the placeholder strings with your SDK API key and Braze endpoint from the dashboard.

### Step 2: Enable debugging (optional)

Set the configuration logger to `.debug` before you create the `Braze` instance so Xcode prints detailed SDK activity while you build and test the inbox.

```swift
configuration.logger.level = .debug
```

Remove this line or lower the log level before you ship to production so you don't emit verbose logs to customers' devices.

### Step 3: Create a UITableViewController

Subclass `UITableViewController` for your inbox. Register a reuse identifier for plain cells, set a comfortable row height, and declare properties for the card list, the Content Cards subscription token, and impression deduplication.

```swift
import SwiftUI
import UIKit
import BrazeKit

class BrazeInboxViewController: UITableViewController {
    private var cards: [Braze.ContentCard] = []
    private var subscription: Any?
    private var loggedImpressions = Set<String>()

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "CardCell")
        tableView.rowHeight = 100
    }
}
```

This tutorial uses SwiftUI for the app shell. Embed your inbox controller in a `UINavigationController` with `UIViewControllerRepresentable`, and use `@main` with `@UIApplicationDelegateAdaptor` so `AppDelegate` still runs—see the **Putting it all together** section for the full `AppDelegate` and `SampleApp` wiring.

### Step 4: Subscribe to Content Card updates

Use `contentCards.subscribeToUpdates` to receive the latest cards on the main queue, assign them to `cards`, and reload the table. Call `requestRefresh()` so the SDK fetches Content Cards for the current user. Add this code inside `viewDidLoad()` after you register the cell and set `rowHeight`:

```swift
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "CardCell")
        tableView.rowHeight = 100

        subscription = AppDelegate.braze.contentCards.subscribeToUpdates { [weak self] updatedCards in
            self?.cards = updatedCards
            self?.tableView.reloadData()
        }

        AppDelegate.braze.contentCards.requestRefresh()
    }
```

The closure keeps a weak reference to the controller to avoid retain cycles.

### Step 5: Display card content in cells

Return a single section and one row per card. Dequeue a cell, allow multiple lines on the text label, and combine each card's `title` and `description` with a newline so the inbox reads like a standard message list.

```swift
    override func numberOfSections(in tableView: UITableView) -> Int { 1 }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        cards.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let card = cards[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "CardCell", for: indexPath)

        // Work with the content card's title and description
        cell.textLabel?.numberOfLines = 2
        cell.textLabel?.text = [card.title, card.description].compactMap { $0 }.joined(separator: "\n")

        return cell
    }
```

You can split title and subtitle into custom views or use Content Card [attributes](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) such as `imageUrl` when you need richer layouts.

### Step 6: Handle card taps

In `didSelectRowAt`, log the click with `logClick(using:)`, open the card's URL when `clickAction` provides one, and deselect the row for visual feedback.

```swift
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        card.logClick(using: AppDelegate.braze)
        if let url = card.clickAction?.url {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }
```

You can also call [`logDismissed(using:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logdismissed(using:)/) when the user dismisses a card in your UI.

### Step 7: Track impressions

You can log impressions using [`logImpression(using:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/logimpression(using:)/) on the content card. Impressions should only be logged once when the user views the card. Here, a naive mechanism uses a `Set` and `willDisplay` to guard against duplicate logs. You may need to consider the UI lifecycle of your app, as well as your use case, to ensure impressions are logged correctly—for example, insert each `card.id` into `loggedImpressions` after a successful log.

```swift
    override func tableView(_ tableView: UITableView,
                            willDisplay cell: UITableViewCell,
                            forRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        if !loggedImpressions.contains(card.id) {
            card.logImpression(using: AppDelegate.braze)
        }
    }
}
```

This pattern matches the sample in the **Putting it all together** section. Extend it if your table reuse or navigation requires stricter deduplication.

### Putting it all together

Here's the full sample: `AppDelegate` configures the SDK and hosts the inbox in SwiftUI, `BrazeInboxView.swift` implements the table and Content Cards logic, and `SampleApp` wires the delegate adaptor. The preview is a static HTML device mockup (SwiftUI doesn't run inside the iframe).

The `configuration.logger.level = .debug` line is optional. Remove it before you release.

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-swift-inbox-full">AppDelegate.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-swift-inbox-full">BrazeInboxView.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="2" data-sandbox="sandbox-swift-inbox-full">SampleApp.swift</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-swift-inbox-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-swift">import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze!

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -&gt; Bool {

        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        return true
    }
}

struct InboxViewControllerRepresentable: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -&gt; UINavigationController {
        let vc = BrazeInboxViewController(style: .plain)
        return UINavigationController(rootViewController: vc)
    }
    func updateUIViewController(_ uiViewController: UINavigationController, context: Context) {}
}

struct ContentView: View {
    var body: some View {
        NavigationView {
                InboxViewControllerRepresentable()
            .navigationTitle("Message Inbox")
        }
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import SwiftUI
import UIKit
import BrazeKit

class BrazeInboxViewController: UITableViewController {
    private var cards: [Braze.ContentCard] = []
    private var subscription: Any?
    private var loggedImpressions = Set&lt;String&gt;()

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "CardCell")
        tableView.rowHeight = 100

        subscription = AppDelegate.braze.contentCards.subscribeToUpdates { [weak self] updatedCards in
            self?.cards = updatedCards
            self?.tableView.reloadData()
        }

        AppDelegate.braze.contentCards.requestRefresh()
    }

    override func numberOfSections(in tableView: UITableView) -&gt; Int { 1 }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -&gt; Int {
        cards.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
        let card = cards[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: "CardCell", for: indexPath)

        // Work with the content card's title and description
        cell.textLabel?.numberOfLines = 2
        cell.textLabel?.text = [card.title, card.description].compactMap { $0 }.joined(separator: "\n")

        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        card.logClick(using: AppDelegate.braze)
        if let url = card.clickAction?.url {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
        tableView.deselectRow(at: indexPath, animated: true)
    }

    override func tableView(_ tableView: UITableView,
                            willDisplay cell: UITableViewCell,
                            forRowAt indexPath: IndexPath) {
        let card = cards[indexPath.row]
        if !loggedImpressions.contains(card.id) {
            card.logImpression(using: AppDelegate.braze)
        }
    }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import SwiftUI

@main
struct SampleApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-swift-inbox-full" class="braze-tutorial-iframe" title="Swift Content Card inbox preview"></iframe>
    </div>
  </div>
</div>

### Next steps

- [About Content Cards]({{site.baseurl}}/developer_guide/content_cards/) — how Content Cards work across channels and SDKs.
- [Customizing Content Card styles]({{site.baseurl}}/developer_guide/content_cards/customizing_styles/) — match Braze cards to your app's look and feel.
- [Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/) — full API documentation for Content Cards and related types.

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
      '.phone { max-width: 300px; margin: 0 auto; border-radius: 32px; overflow: hidden; border: 3px solid #1B2536; box-shadow: 0 8px 30px rgba(0,0,0,0.12); background: #000; }' +
      '.phone-notch { height: 28px; background: #000; display: flex; justify-content: center; align-items: flex-end; padding-bottom: 6px; }' +
      '.phone-notch-pill { width: 100px; height: 22px; background: #1a1a1a; border-radius: 12px; }' +
      '.phone-status { background: #f8f9fa; color: #1B2536; padding: 6px 18px 4px; font-size: 11px; font-weight: 600; display: flex; justify-content: space-between; align-items: center; border-bottom: 0.5px solid #e2e8f0; }' +
      '.phone-navbar { background: #f8f9fa; padding: 12px 16px; font-weight: 600; font-size: 16px; color: #1B2536; text-align: center; border-bottom: 0.5px solid #c8c8c8; }' +
      '.phone-body { background: #f2f2f7; min-height: 320px; }' +
      '.inbox-row { background: #fff; padding: 12px 16px; border-bottom: 0.5px solid #c6c6c8; }' +
      '.inbox-row:last-child { border-bottom: none; }' +
      '.inbox-title { font-size: 15px; font-weight: 600; color: #1B2536; margin-bottom: 4px; line-height: 1.25; }' +
      '.inbox-desc { font-size: 13px; color: #64748b; line-height: 1.4; }';

    function inboxRow(title, desc) {
      return '<a href="javascript:void(0)" class="inbox-row" style="display:block;text-decoration:none;cursor:default;">' +
        '<div class="inbox-title">' + title + '</div>' +
        '<div class="inbox-desc">' + desc + '</div></a>';
    }

    var inboxPreview = '<!DOCTYPE html><html><head><meta charset="utf-8"><style>' + phoneStyles +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-notch"><div class="phone-notch-pill"></div></div>' +
      '<div class="phone-status"><span>9:41</span><span><a href="javascript:void(0)" style="color:inherit;text-decoration:none;">5G</a></span></div>' +
      '<div class="phone-navbar">Message Inbox</div>' +
      '<div class="phone-body">' +
      inboxRow('Welcome to Braze!', 'Thanks for installing our app.') +
      inboxRow('Flash Sale This Weekend', 'Save up to 40% on select items.') +
      inboxRow('New Feature: Dark Mode', 'Try our new dark mode setting.') +
      inboxRow('Your weekly digest', 'Catch up on what you missed.') +
      '</div></div></body></html>';

    var previews = {
      'braze-preview-swift-inbox-full': inboxPreview
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
    setTimeout(forcePopulatePreviews, 300);
    setTimeout(forcePopulatePreviews, 1000);

    document.querySelectorAll('.tab_toggle, .sdk-tab_toggle').forEach(function(toggle) {
      toggle.addEventListener('click', function() {
        setTimeout(forcePopulatePreviews, 150);
      });
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
