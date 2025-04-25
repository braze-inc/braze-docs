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

> [Branch][1], a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints.

_This integration is maintained by Branch._

## About the integration

The Braze and Branch integration allows you to provide better experiences to your customers by allowing you to properly [attribute]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) the beginning of their user journey and connect them through deep links to their intended location.

## Integration

Follow [Branch's SDK integration guide](https://help.branch.io/developers-hub/docs/native-sdks-overview) to get up and running with your Branch integration. Refer to the following for additional use cases.

### Support iOS universal links

To support sending iOS universal links as deep links from within Braze:

1. Follow Branch's documentation for setting up [universal links][3].
2. Implement the [`BrazeDelegate`][4] method [braze(_:shouldOpenURL:)][5] in your Braze SDK integration to [route universal links][6] from within your app.

### Deep linking in email

Refer to our documentation on [Universal links and App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)
or see [Branch's documentation](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) to set up deep linking from emails sent through Braze.

Linking to phone numbers (appending `tel` to `href`) isn't supported in the Gmail app for iOS unless a user grants call permissions to the app.

Depending on your ESP, additional customization may be required to support click-tracked universal links. This information is outlined in our dedicated article. You can also refer to the following references to learn more:

- [SendGrid][7]
- [SparkPost][9]


[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://help.branch.io/developers-hub/docs/ios-universal-links
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
