---
nav_title: Branch for Deep Linking
article_title: Branch for Deep Linking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "This reference article describes the partnership between Braze and Branch and how to use it to support your deep linking practices."
search_tag: Partner

---

# Branch for deep linking {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/) is a mobile linking platform used to acquire, engage, and measure across devices, channels, and platforms by providing a holistic view of user touchpoints.

_This integration is maintained by Branch._

## About the integration

The Braze and Branch integration allows you to provide better experiences to your customers by allowing you to properly [attribute]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) the beginning of their user journey and connect them through deep links to their intended location.

{% alert tip %}
For help choosing the right deep linking approach for your use case, see [iOS deep linking guide]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide).
{% endalert %}

## Integration

Follow [Branch's SDK integration guide](https://help.branch.io/developers-hub/docs/native-sdks-overview) to get up and running with your Branch integration. Refer to the following for additional use cases.

### Support iOS universal links

To support sending iOS universal links as deep links from within Braze:

#### Step 1: Set up Branch universal links

Follow Branch's documentation for setting up [universal links](https://help.branch.io/developers-hub/docs/ios-universal-links). As part of this setup, Branch hosts the AASA file on your Branch link domain (for example, `yourapp.app.link`) automatically.

#### Step 2: Configure Associated Domains

In Xcode, go to your app target > **Signing & Capabilities** and add your Branch link domain under **Associated Domains**:

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

If you use a custom Branch domain, add that as well.

#### Step 3: Forward universal links in Braze

Set `forwardUniversalLinks` to `true` in your Braze SDK configuration so the SDK forwards universal links to your app's `AppDelegate`:

{% tabs %}
{% tab swift %}
```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### Step 4: Route Branch links with BrazeDelegate

Implement [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) to intercept Branch links before Braze handles them. This ensures Branch can process the link and perform its own routing:

{% tabs %}
{% tab swift %}
```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

Replace `yourdomain.com` with your custom Branch domain, if applicable.

### Deep linking in email

Refer to the documentation on [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)
or see [Branch's documentation](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) to set up deep linking from emails sent through Braze.

Linking to phone numbers (appending `tel` to `href`) isn't supported in the Gmail app for iOS unless a user grants call permissions to the app.

Depending on your ESP, additional customization may be required to support click-tracked universal links. This information is outlined in our dedicated article. You can also refer to the following references to learn more:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## Troubleshooting

If Branch links aren't working as expected from Braze campaigns, follow these steps.

### Verify the link works outside of Braze

Open the Branch link from the Notes app on a physical iOS device. If it doesn't open your app:

- The issue is in your Branch or AASA configuration, not Braze.
- Validate your Branch AASA at `https://yourapp.app.link/.well-known/apple-app-site-association`.
- Check that your Bundle ID and Team ID match in the Branch dashboard.

### Enable dual logging

1. **Braze**: [Enable verbose logging]({{site.baseurl}}/developer_guide/verbose_logging) and look for `Opening '<URL>':` entries. This confirms the SDK received the link.
2. **Branch**: Enable [Branch test mode](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) and check the Branch dashboard for link click events.
3. **Compare**: If Braze logs the link but Branch doesn't see a click, the `BrazeDelegate` routing logic is likely not intercepting the link correctly. Check that the domain match in `shouldOpenURL` includes your Branch domain.

### Common issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Branch link opens in Safari | AASA invalid or missing on Branch domain | Verify Associated Domains and AASA file |
| Branch link opens but lands on wrong screen | Branch link data misconfigured | Check routing rules in Branch dashboard |
| Link works from push but not email | Click-tracking domain missing AASA | Host AASA on your ESP's click-tracking domain; see [Email setup](#deep-linking-in-email) |
| `shouldOpenURL` never fires for Branch links | `forwardUniversalLinks` not enabled | Set `configuration.forwardUniversalLinks = true` |
| Branch link works from Notes but not Braze | `BrazeDelegate` returning `true` for Branch URLs | Verify domain check in `shouldOpenURL` matches your Branch domain |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more deep linking troubleshooting scenarios, see [Deep linking troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).