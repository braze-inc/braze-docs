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

> [Branch](https://branch.io/), a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints.

The Braze and Branch integration allows you to provide better experiences to your customers by allowing you to properly [attribute]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) the beginning of their user journey and connect them through deep links to their intended location.

If you include a call link (`href=tel:`),

## Integration

Follow [Branch's SDK integration guide](https://help.branch.io/developers-hub/docs/native-sdks-overview) to get up and running with your Branch integration. Refer to the following for additional use cases.

### Support iOS universal links

To support sending iOS universal links as deep links from within Braze:

1. Follow Branch's documentation for setting up [universal links](https://docs.branch.io/pages/deep-linking/universal-links/#search).
2. Implement the [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) method [braze(_:shouldOpenURL:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5) in your Braze SDK integration to [route universal links]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization) from within your app.

### Deep linking in email

Refer to our documentation on [Universal links and App Links]({{site.baseurl}}/help/help_articles/email/universal_links/)
or see [Branch's documentation](https://docs.branch.io/pages/integrations/braze/) to set up deep linking from emails sent through Braze.

Linking to phone numbers (appending `tel` to `href`) isn't supported in the Gmail app for iOS unless a user grants call permissions to the app.

Depending on your ESP, additional customization may be required to support click-tracked universal links. This information is outlined in our dedicated article. You can also refer to the following references to learn more:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

