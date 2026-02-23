---
page_order: 1.2
nav_title: Deep Linking Troubleshooting
article_title: Deep linking troubleshooting
description: "Common deep linking issues on iOS and how to diagnose them, including custom scheme links, universal links, email links, and third-party providers like Branch."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Deep linking troubleshooting

> This page covers common deep linking issues on iOS and how to diagnose them. For help choosing the right link type, see [iOS deep linking guide]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). For implementation details, see [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## Custom scheme deep link doesn't open the correct view

If a custom scheme deep link (for example, `myapp://products/123`) opens your app but doesn't navigate to the intended screen:

1. **Verify the scheme is registered.** In Xcode, check that your scheme is listed under `CFBundleURLTypes` in `Info.plist`.
2. **Check your handler.** Set a breakpoint in `application(_:open:options:)` to confirm it's being called and inspect the `url` parameter.
3. **Test the link independently.** Run the following command from Terminal to test the deep link outside of Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   If the link doesn't work here, the issue is in your app's URL handling—not in Braze.
4. **Check the URL format.** Verify the URL in your campaign matches what your handler expects. Common mistakes include missing path components or incorrect casing.

## Universal link opens in Safari instead of the app

If a universal link (for example, `https://myapp.com/products/123`) opens in Safari instead of your app:

### Verify the Associated Domains entitlement

In Xcode, go to your app target > **Signing & Capabilities** and check that `applinks:yourdomain.com` is listed under **Associated Domains**.

### Validate the AASA file

Your Apple App Site Association (AASA) file must be hosted at one of these locations:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Verify the following:

- The file is served over HTTPS with a valid certificate.
- The `Content-Type` is `application/json`.
- The file size is under 128 KB.
- The `appID` matches your Team ID and Bundle ID (for example, `ABCDE12345.com.example.myapp`).
- The `paths` or `components` array includes the URL patterns you expect.

You can validate your AASA using [Apple's search validation tool](https://search.developer.apple.com/appsearch-validation-tool/) or by running:

```bash
swcutil dl -d yourdomain.com
```

### Check the `AppDelegate`

Verify that `application(_:continue:restorationHandler:)` is implemented in your `AppDelegate` and handles the `NSUserActivity` correctly:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Verify Braze SDK configuration

If you're using universal links from Braze-delivered push notifications, in-app messages, or Content Cards, confirm that `forwardUniversalLinks` is enabled:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
Universal link forwarding requires access to the application entitlements. When running in a simulator, these entitlements aren't directly available. To test in a simulator, add the `.entitlements` file to the **Copy Bundle Resources** build phase.
{% endalert %}

### Check for the long-press issue

If you long-press a universal link and select **Open**, iOS may "break" the universal link association for that domain. This is a known iOS behavior. To reset it, long-press the link again and select **Open in [App Name]**.

## Deep link from email doesn't open the app

Email links go through your ESP's click-tracking system, which wraps links in a tracking domain (for example, `https://click.yourdomain.com/...`). For universal links to work from email, you must configure the AASA file on your click-tracking domain — not just your primary domain.

### Verify click-tracking domain AASA

1. Identify your click-tracking domain from your ESP settings (SendGrid, SparkPost, or Amazon SES).
2. Host the AASA file at `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Ensure the AASA file on the click-tracking domain includes the same `appID` and valid path patterns.

For ESP-specific setup instructions, see [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

### Check the redirect chain

Some ESPs perform a redirect from the click-tracking URL to your final URL. Universal links only work if iOS recognizes the *initial* domain (the click-tracking domain) as associated with your app. If the redirect bypasses the AASA check, the link opens in Safari.

To test:

1. Send yourself a test email.
2. Long-press the link and inspect the URL — this is the click-tracking URL.
3. Verify this domain has a valid AASA file.

## Deep link works from push but not from in-app messages (or vice versa)

### Check the BrazeDelegate

If you implement `BrazeDelegate.braze(_:shouldOpenURL:)`, verify it handles links consistently across channels. The `context` parameter includes the source channel. Look for conditional logic that may accidentally filter links from specific channels.

### Enable verbose logging

[Enable verbose logging]({{site.baseurl}}/developer_guide/verbose_logging) and reproduce the issue. Look for the `Opening` log entry:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compare the log output for the working channel vs. the non-working channel. Differences in `useWebView` or `isUniversalLink` indicate how the SDK is interpreting the link differently.

### Check for custom display delegates

If you use a custom in-app message display delegate or Content Card click handler, verify that it correctly passes link events to the Braze SDK for handling.

## "Open Web URL Inside App" shows a blank or broken page

If selecting **Open Web URL Inside App** results in a blank or broken WebView:

1. **Verify the URL uses HTTPS.** The SDK's WebView requires ATS-compliant URLs. HTTP links fail silently.
2. **Check for Content Security Policy headers.** If the target web page sets `X-Frame-Options: DENY` or a restrictive `Content-Security-Policy`, it blocks rendering in a WebView.
3. **Check for redirects to custom schemes.** If the web page redirects to a custom scheme (for example, `myapp://`), the WebView can't handle it.
4. **Test the URL in Safari.** If the page doesn't load in Safari on the device, it won't load in the WebView either.

## Troubleshooting Branch with Braze {#branch}

If you use [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) as your linking provider:

### Verify the BrazeDelegate routes to Branch

Your `BrazeDelegate` must intercept Branch links and pass them to the Branch SDK. Verify the following:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

If `shouldOpenURL` returns `true` for Branch links, Braze handles them directly instead of routing to Branch.

### Check Branch link domain

Verify the Branch domain in your `BrazeDelegate` matches your actual Branch link domain. Branch uses several domain formats:

- `yourapp.app.link` (default)
- `yourapp-alternate.app.link` (alternate)
- Custom domains (if configured in Branch dashboard)

### Enable both SDKs' logging

To diagnose where the link breaks in the chain:

1. Enable [Braze verbose logging]({{site.baseurl}}/developer_guide/verbose_logging) — look for `Opening '<URL>':` entries to verify the SDK received the link.
2. Enable [Branch test mode](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) — check the Branch dashboard for link click events.
3. Compare: If Braze logs the link but Branch doesn't see a click, the `BrazeDelegate` routing logic is the likely issue.

### Check Branch dashboard configuration

In the Branch dashboard, verify:

- Your app's **Bundle ID** and **Team ID** match your Xcode project.
- Your **Associated Domains** include the Branch link domain.
- Your Branch AASA file is valid (Branch hosts this automatically on `app.link` domains).

### Test Branch links independently

Test the Branch link outside of Braze to isolate the issue:

1. Open the Branch link in Safari on your device. If it doesn't open the app, the issue is in your Branch or AASA configuration — not Braze.
2. Paste the Branch link into the Notes app and tap it. Universal links work more reliably from Notes than from Safari's address bar.

## General debugging tips

### Use verbose logging

[Enable verbose logging]({{site.baseurl}}/developer_guide/verbose_logging) to see exactly how the SDK processes links. Key entries to look for:

| Log entry | What it means |
|---|---|
| `Opening '<URL>': - channel: notification` | SDK is processing a link from a push notification |
| `Opening '<URL>': - channel: inAppMessage` | SDK is processing a link from an in-app message |
| `Opening '<URL>': - channel: contentCard` | SDK is processing a link from a Content Card |
| `useWebView: true` | SDK opens the URL in the in-app WebView |
| `isUniversalLink: true` | SDK identified the URL as a universal link |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details on reading these logs, see [Reading verbose logs]({{site.baseurl}}/developer_guide/verbose_logging).

### Test links in isolation

Before testing through Braze, verify that your deep link or universal link works on its own:

- **Custom scheme**: Run `xcrun simctl openurl booted "myapp://path"` in Terminal.
- **Universal link**: Paste the URL into the Notes app on a physical device and tap it. Don't test from the Safari address bar, as iOS treats typed URLs differently from tapped links.
- **Branch link**: Open the Branch link from the Notes app on a device.

### Test on a physical device

Universal links have limited support in the iOS simulator. Always test on a physical device for accurate results. If you must test in a simulator, add the `.entitlements` file to the **Copy Bundle Resources** build phase.