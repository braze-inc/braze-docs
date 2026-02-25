---
page_order: 1.1
nav_title: iOS deep linking guide
article_title: iOS deep linking guide
description: "Learn which type of deep link to use for your iOS app, when you need an AASA file, and which app delegate methods to implement."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOS deep linking guide

> This guide helps you choose the right deep linking strategy for your iOS app, depending on which messaging channel you're using and whether you use a third-party linking provider like Branch.

For implementation details, see [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). For troubleshooting, see [Deep linking troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Choosing a link type

There are three ways to handle links from Braze messages in your iOS app. Each one works differently and is suited for different channels and use cases.

| Link type | Example | Best for | Opens without app installed? |
|---|---|---|---|
| **Custom scheme** | `myapp://products/123` | Push, in-app messages, Content Cards | No — link fails |
| **Universal link** | `https://myapp.com/products/123` | Email, SMS, channels with click tracking | Yes — falls back to web |
| **Open Web URL Inside App** | Any `https://` URL | Displaying web content in a modal WebView | N/A — displays in WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Custom scheme deep links

Custom scheme deep links (for example, `myapp://products/123`) open your app directly to a specific screen. They are the simplest option for channels where links aren't modified by a third party.

**Use custom scheme deep links when:**
- Sending push notifications, in-app messages, or Content Cards
- You don't need the link to work if the app isn't installed
- You don't need click tracking (email ESP link wrapping)

**Don't use custom scheme deep links when:**
- Sending emails — ESPs wrap links for click tracking, which breaks custom schemes
- You need the link to fall back to a web page if the app isn't installed

### Universal links

Universal links (for example, `https://myapp.com/products/123`) are standard HTTPS URLs that iOS can route to your app instead of opening in a browser. They require server-side configuration (an AASA file) and app-side setup (Associated Domains entitlement).

**Use universal links when:**
- Sending emails. Your ESP wraps links for click tracking, so links must be HTTPS.
- Sending SMS or other channels where links are wrapped or shortened.
- You need the link to fall back to a web page when the app isn't installed.
- You're using a third-party linking provider like Branch or AppsFlyer.

**Don't use universal links when:**
- You only need deep links from push, in-app messages, or Content Cards — custom schemes are simpler

### "Open Web URL Inside App"

This option opens a web page inside a modal WebView within your app. It's handled entirely by the Braze SDK using `Braze.WebViewController` — you don't need to write any URL handling code.

**Use "Open Web URL Inside App" when:**
- You want to display a web page (such as a promotion or article) without leaving your app
- The URL is a standard HTTPS web page, not a deep link to a specific app screen

**Don't use "Open Web URL Inside App" when:**
- You need to navigate to a specific view in your app — use a custom scheme or universal link instead
- The web page requires authentication or has Content Security Policy headers that block embedding

## What you need for each link type

### Custom scheme deep links

| Requirement | Details |
|---|---|
| AASA file | Not required |
| `Info.plist` | Register your scheme under `CFBundleURLTypes` and add it to `LSApplicationQueriesSchemes` |
| App delegate method | Implement `application(_:open:options:)` to parse the URL and navigate |
| Braze SDK configuration | None — the SDK opens custom scheme URLs by default |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Universal links

| Requirement | Details |
|---|---|
| AASA file | Required — host at `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Add `applinks:yourdomain.com` in Xcode under **Signing & Capabilities** |
| App delegate method | Implement `application(_:continue:restorationHandler:)` to handle `NSUserActivity` |
| Braze SDK configuration | Set `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optional) | Implement `braze(_:shouldOpenURL:)` for custom routing (for example, Branch) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
If you send emails through Braze, your ESP (SendGrid, SparkPost, or Amazon SES) wraps links in a click-tracking domain. You must host the AASA file on your click-tracking domain as well, not only on your primary domain. For complete setup, see [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### "Open Web URL Inside App"

| Requirement | Details |
|---|---|
| AASA file | Not required |
| App delegate method | Not required — the SDK handles this automatically |
| Braze SDK configuration | None — select **Open Web URL Inside App** in the campaign composer |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## When you need an AASA file {#when-aasa}

An Apple App Site Association (AASA) file is only required when you use **universal links**. It tells iOS which URLs your app can handle.

You need an AASA file when:

- You send deep links in **email** campaigns (because ESPs wrap links in HTTPS click-tracking URLs)
- You send deep links in **SMS** campaigns (because links may be shortened to HTTPS URLs)
- You use **Branch**, **AppsFlyer**, or another linking provider (because they use their own HTTPS domains)
- You use universal links from **push**, **in-app messages**, or **Content Cards** (less common, but possible with `forwardUniversalLinks = true`)

You don't need an AASA file when:

- You only use **custom scheme** deep links (for example, `myapp://`) from push, in-app messages, or Content Cards
- You use the **"Open Web URL Inside App"** option

For AASA setup instructions, see [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links).

## When you need app code to handle links {#when-app-code}

Which delegate method you implement depends on the type of link you're using:

| Delegate method | Handles | When to implement |
|---|---|---|
| `application(_:open:options:)` | Custom scheme deep links (`myapp://`) | You use custom scheme deep links from any channel |
| `application(_:continue:restorationHandler:)` | Universal links (`https://`) | You use universal links from email, SMS, or with `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | All URLs opened by the SDK | You need custom routing logic (for example, Branch, conditional handling, analytics) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
If you use a third-party linking provider like Branch, implement `BrazeDelegate.braze(_:shouldOpenURL:)` to intercept URLs and forward them to the provider's SDK. See [Branch for deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) for a complete example.
{% endalert %}

## Using Branch with Braze {#branch}

If you use [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) as your linking provider, your setup requires a few additional steps beyond a standard universal link configuration:

1. **Branch SDK**: Integrate the Branch SDK following [Branch's documentation](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Associated Domains**: Add your Branch domain (for example, `applinks:yourapp.app.link`) in Xcode under **Signing & Capabilities**.
3. **BrazeDelegate**: Implement `braze(_:shouldOpenURL:)` to route Branch links to the Branch SDK instead of letting Braze handle them directly.
4. **Forward universal links**: Set `configuration.forwardUniversalLinks = true` in your Braze SDK configuration.

For implementation details and debugging guidance, see [Branch for deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).