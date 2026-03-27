## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners for the Swift SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Swift" %}

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
/* Framework tab spacing (UIKit / SwiftUI tabs) */
.ab-nav.ab-nav-tabs {
  padding-left: 8px !important;
}
.ab-nav-tabs .coderow a.tab_toggle {
  padding: 10px 16px !important;
}
.ab-tab-pane {
  padding: 0 20px !important;
}
</style>

<div class="braze-tutorial-intro">
  <p>This tutorial walks you through displaying Banners in an iOS app using the Braze Swift SDK and placement IDs. Each section introduces a concept, shows the code, and explains how the pieces connect. Select the <strong>UIKit</strong> or <strong>SwiftUI</strong> tab to see the implementation for your preferred framework.</p>
</div>

<div class="braze-learn-box">
  <h4>You will learn how to</h4>
  <ul>
    <li>Configure the Braze SDK for banners in your iOS app</li>
    <li>Request fresh banner content for specific placements</li>
    <li>Create a <code>BannerUIView</code> (UIKit) or <code>BannerView</code> (SwiftUI) to display banners</li>
    <li>Handle the <code>processContentUpdates</code> callback for dynamic height</li>
    <li>Check for available banners before displaying them</li>
    <li>Constrain banner height with Auto Layout or SwiftUI modifiers</li>
  </ul>
</div>

### Step 1: Configure the Braze SDK

Create a `Braze.Configuration` with your API key and endpoint, then initialize the SDK in your `AppDelegate`:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-API-KEY",
    endpoint: "YOUR-ENDPOINT"
)
AppDelegate.braze = Braze(configuration: configuration)
```

Store the Braze instance as a static property on your `AppDelegate` so it's accessible from your view controllers and SwiftUI views throughout the app.

### Step 2: Enable debugging (optional)

To make troubleshooting easier during development, set the logger level before initializing the SDK:

```swift
configuration.logger.level = .debug
```

This prints detailed SDK activity to the Xcode console, including banner requests and responses. Remove this line before deploying to production.

### Step 3: Request a banner refresh

After initializing the SDK, call `requestBannersRefresh(placementIds:)` to fetch the latest banner content for your placements:

```swift
AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])
```

Call this in `application(_:didFinishLaunchingWithOptions:)` so banners are fetched at the start of each session. You can also call it later during a session to fetch updated content, for example when the user navigates to a new screen.

{% tabs %}
{% tab UIKit %}

### Step 4: Create a BannerUIView

Initialize a `BrazeBannerUI.BannerUIView` with your placement ID, the Braze instance, and a `processContentUpdates` callback. The callback receives a `Result` containing a `ContentUpdates` object with the banner's intrinsic height:

```swift
lazy var bannerView: BrazeBannerUI.BannerUIView = {
    var bannerView = BrazeBannerUI.BannerUIView(
        placementId: "top-1",
        braze: AppDelegate.braze!,
        processContentUpdates: { [weak self] result in
            DispatchQueue.main.async {
                guard let self else { return }
                switch result {
                case .success(let updates):
                    if let height = updates.height {
                        self.bannerView.isHidden = false
                        self.bannerHeightConstraint?.constant = min(height, 80)
                    }
                case .failure:
                    return
                }
            }
        }
    )
    bannerView.translatesAutoresizingMaskIntoConstraints = false
    bannerView.isHidden = true
    return bannerView
}()
```

The `processContentUpdates` closure fires when banner content finishes rendering. On success, unhide the view and update its height constraint. Use `min(height, 80)` to cap the banner at a maximum height. The view starts hidden and with `translatesAutoresizingMaskIntoConstraints` set to `false` so Auto Layout manages its frame.

### Step 5: Set up Auto Layout constraints

In `viewDidLoad()`, add the content view and banner view to the hierarchy, then activate Auto Layout constraints. Pin the banner below your main content and set an initial height constraint of `0` that updates when content loads:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    view.addSubview(contentView)
    view.addSubview(bannerView)
    bannerHeightConstraint = bannerView.heightAnchor.constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
        contentView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
        contentView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
        contentView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        bannerView.topAnchor.constraint(equalTo: contentView.bottomAnchor),
        bannerView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
        bannerView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
        bannerView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
        bannerHeightConstraint!,
    ])
}
```

The banner's leading, trailing, and bottom edges are pinned to the safe area. The height constraint starts at `0` and is updated by the `processContentUpdates` callback when content loads, creating a smooth appearance transition.

### Putting it all together

Here's the complete UIKit implementation with SDK configuration, banner refresh, view creation, and Auto Layout. The preview shows what the rendered banner looks like on a device:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-uikit-full">AppDelegate.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-uikit-full">BannerViewController.swift</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-uikit-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-swift">import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder,
    UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions:
      [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    configuration.logger.level = .debug

    AppDelegate.braze = Braze(
      configuration: configuration
    )

    AppDelegate.braze?.banners
      .requestBannersRefresh(
        placementIds: ["top-1"]
      )

    return true
  }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import UIKit
import BrazeKit
import BrazeUI

final class BannerViewController: UIViewController {
  static let bannerPlacementID = "top-1"
  var bannerHeightConstraint: NSLayoutConstraint?

  lazy var contentView: UILabel = {
    let label = UILabel()
    label.text = "Your Content Here"
    label.textAlignment = .center
    label.translatesAutoresizingMaskIntoConstraints
      = false
    return label
  }()

  lazy var bannerView:
    BrazeBannerUI.BannerUIView = {
    var view = BrazeBannerUI.BannerUIView(
      placementId:
        BannerViewController.bannerPlacementID,
      braze: AppDelegate.braze!,
      processContentUpdates: {
        [weak self] result in
        DispatchQueue.main.async {
          guard let self else { return }
          switch result {
          case .success(let updates):
            if let height = updates.height {
              self.bannerView.isHidden = false
              self.bannerHeightConstraint?
                .constant = min(height, 80)
            }
          case .failure:
            return
          }
        }
      }
    )
    view.translatesAutoresizingMaskIntoConstraints
      = false
    view.isHidden = true
    return view
  }()

  override func viewDidLoad() {
    super.viewDidLoad()
    view.addSubview(contentView)
    view.addSubview(bannerView)
    bannerHeightConstraint = bannerView
      .heightAnchor
      .constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
      contentView.topAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .topAnchor),
      contentView.leadingAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .leadingAnchor),
      contentView.trailingAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .trailingAnchor),
      bannerView.topAnchor.constraint(
        equalTo: contentView.bottomAnchor),
      bannerView.leadingAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .leadingAnchor),
      bannerView.trailingAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .trailingAnchor),
      bannerView.bottomAnchor.constraint(
        equalTo: view.safeAreaLayoutGuide
          .bottomAnchor),
      bannerHeightConstraint!,
    ])
  }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-uikit-full" class="braze-tutorial-iframe" title="UIKit banner implementation preview"></iframe>
    </div>
  </div>
</div>

The `configuration.logger.level = .debug` setting in `AppDelegate.swift` is optional. It prints SDK activity to the Xcode console, which is helpful for debugging during development. Remove it before deploying to production.

{% endtab %}
{% tab SwiftUI %}

### Step 4: Create a BannerView component

Build a SwiftUI view that displays a `BrazeBannerUI.BannerView`. Use `@State` properties to track whether a banner is available and its content height:

```swift
@available(iOS 13.0, *)
struct BannerSwiftUIView: View {
    static let bannerPlacementID = "top-1"

    @State var hasBannerForPlacement: Bool = false
    @State var contentHeight: CGFloat = 0

    var body: some View {
        VStack {
            Text("Your Content Here")
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            if let braze = AppDelegate.braze,
                hasBannerForPlacement
            {
                BrazeBannerUI.BannerView(
                    placementId: BannerSwiftUIView.bannerPlacementID,
                    braze: braze,
                    processContentUpdates: { result in
                        switch result {
                        case .success(let updates):
                            if let height = updates.height {
                                self.contentHeight = height
                            }
                        case .failure:
                            return
                        }
                    }
                )
                .frame(height: min(contentHeight, 80))
            }
        }
    }
}
```

The `BannerView` is only rendered when the SDK is initialized and a banner is available for the placement. The `processContentUpdates` callback updates `contentHeight` when content finishes rendering, and the `.frame(height: min(contentHeight, 80))` modifier caps the banner at a maximum height to keep your layout balanced.

### Step 5: Check for available banners

Use `getBanner(for:completion:)` in an `.onAppear` modifier to check whether a banner exists for your placement before displaying the `BannerView`. This prevents blank space in your layout when no banner is assigned:

```swift
.onAppear {
    AppDelegate.braze?.banners.getBanner(
        for: BannerSwiftUIView.bannerPlacementID,
        { banner in
            hasBannerForPlacement = banner != nil
        }
    )
}
```

The completion handler receives a `Banner?` object. If it's non-nil, a banner is available and you set `hasBannerForPlacement` to `true`, which triggers SwiftUI to render the `BannerView`. If it's `nil`, the banner area stays hidden.

### Step 6: Handle content height dynamically

The `processContentUpdates` callback receives a `Result` with a `ContentUpdates` object containing the banner's intrinsic height. Update your `@State` property and apply a `.frame` modifier to constrain the height:

```swift
processContentUpdates: { result in
    switch result {
    case .success(let updates):
        if let height = updates.height {
            self.contentHeight = height
        }
    case .failure:
        return
    }
}
```

Use `min(contentHeight, 80)` in the frame modifier to ensure the banner never exceeds a maximum height. Adjust the cap to match your layout requirements.

### Putting it all together

Here's the complete SwiftUI implementation with SDK configuration, banner refresh, availability checking, and dynamic height handling. The preview shows what the rendered banner looks like on a device:

<div class="braze-tutorial-sandbox">
  <div class="braze-tutorial-sandbox-top">
    <button class="braze-tutorial-tab active" role="tab" aria-selected="true" data-tab-index="0" data-sandbox="sandbox-swiftui-full">AppDelegate.swift</button>
    <button class="braze-tutorial-tab" role="tab" aria-selected="false" data-tab-index="1" data-sandbox="sandbox-swiftui-full">BannerSwiftUIView.swift</button>
  </div>
  <div class="braze-tutorial-sandbox-body">
    <div class="braze-tutorial-editor" id="sandbox-swiftui-full">
      <div class="braze-tutorial-panel active">
        <pre><code class="language-swift">import BrazeKit
import BrazeUI

class AppDelegate: UIResponder,
    UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions:
      [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    configuration.logger.level = .debug

    AppDelegate.braze = Braze(
      configuration: configuration
    )

    AppDelegate.braze?.banners
      .requestBannersRefresh(
        placementIds: ["top-1"]
      )

    return true
  }
}</code></pre>
      </div>
      <div class="braze-tutorial-panel">
        <pre><code class="language-swift">import BrazeKit
import BrazeUI
import SwiftUI

@available(iOS 13.0, *)
struct BannerSwiftUIView: View {
  static let bannerPlacementID = "top-1"
  @State var hasBannerForPlacement = false
  @State var contentHeight: CGFloat = 0

  var body: some View {
    VStack {
      Text("Your Content Here")
        .frame(maxWidth: .infinity,
               maxHeight: .infinity)
      if let braze = AppDelegate.braze,
        hasBannerForPlacement
      {
        BrazeBannerUI.BannerView(
          placementId:
            BannerSwiftUIView.bannerPlacementID,
          braze: braze,
          processContentUpdates: { result in
            switch result {
            case .success(let updates):
              if let height = updates.height {
                self.contentHeight = height
              }
            case .failure:
              return
            }
          }
        )
        .frame(height: min(contentHeight, 80))
      }
    }.onAppear {
      AppDelegate.braze?.banners.getBanner(
        for:
          BannerSwiftUIView.bannerPlacementID,
        { banner in
          hasBannerForPlacement =
            banner != nil
        }
      )
    }
  }
}</code></pre>
      </div>
    </div>
    <div class="braze-tutorial-preview">
      <div class="braze-tutorial-preview-bar">Result</div>
      <iframe id="braze-preview-swiftui-full" class="braze-tutorial-iframe" title="SwiftUI banner implementation preview"></iframe>
    </div>
  </div>
</div>

The `configuration.logger.level = .debug` setting in `AppDelegate.swift` is optional. It prints SDK activity to the Xcode console, which is helpful for debugging during development. Remove it before deploying to production.

{% endtab %}
{% endtabs %}

### Next steps

Now that you can display banners by placement ID, explore these topics for more advanced usage:

- [Manage Banner placements]({{site.baseurl}}/developer_guide/banners/placements/) — create placements, log impressions and clicks, and work with custom properties.
- [About Banners]({{site.baseurl}}/developer_guide/banners/) — learn how Banners work in the Braze SDK.
- [Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/) — full API documentation for all banner classes and methods.

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
      '.phone-body { background: #f8f9fa; padding: 16px; min-height: 280px; }';

    var bannerHtml =
      '<div style="background: linear-gradient(135deg, #1B2536 0%, #2d4a6f 50%, #1a7f8a 100%); color: #fff; padding: 20px 16px; border-radius: 10px; text-align: center; margin-bottom: 12px;">' +
      '<div style="font-size: 9px; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; margin-bottom: 6px;">Limited Time Offer</div>' +
      '<h3 style="margin: 0 0 4px; font-size: 17px; font-weight: 700;">Spring Sale: 25% Off</h3>' +
      '<p style="margin: 0 0 12px; opacity: 0.9; font-size: 12px; line-height: 1.4;">Use code SPRING25 at checkout.</p>' +
      '<a href="javascript:void(0)" style="display: inline-block; background: #00B3E6; color: #fff; border: none; padding: 8px 20px; border-radius: 6px; font-size: 12px; font-weight: 600; text-decoration: none; cursor: pointer;">Shop Now</a>' +
      '</div>';

    var iosPreview = '<!DOCTYPE html><html><head><style>' + phoneStyles +
      '.content-block { background: #fff; border-radius: 10px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }' +
      '.product-row { display: flex; gap: 8px; margin-top: 12px; }' +
      '.product-card { flex: 1; background: #fff; border-radius: 10px; padding: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }' +
      '.product-img { background: linear-gradient(135deg, #e2e8f0, #f1f5f9); height: 60px; border-radius: 8px; margin-bottom: 6px; }' +
      '</style></head><body>' +
      '<div class="phone">' +
      '<div class="phone-status"><span>9:41</span><span>5G</span></div>' +
      '<div class="phone-navbar">MyApp</div>' +
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
      'braze-preview-uikit-full': iosPreview,
      'braze-preview-swiftui-full': iosPreview
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
