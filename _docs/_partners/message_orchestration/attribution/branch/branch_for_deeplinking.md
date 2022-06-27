---
nav_title: Branch for Deep Linking
article_title: Branch for Deep Linking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "This article describes the partnership between Braze and Branch and how to use it to support your deep linking practices."
search_tag: Partner

---

# Branch for deep linking {#branch}

{% include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch][1], a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints.

The Braze and Branch integration allows you to provide better experiences to your customers by allowing you to properly [attribute]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) the beginning of their user journey and connect them through deep links to their intended location.

## Integration

Follow [Branch's SDK integration guide](https://help.branch.io/developers-hub/docs/native-sdks-overview) to get up and running with your Branch integration. Refer to the following for additional use cases.

### Support iOS universal links

To support sending iOS universal links as deep links from within Braze:

1. Follow Branch's documentation for setting up [universal links][3].
2. Add the `ABKURLDelegate` to your Braze SDK integration to [route universal links][4] from within your app.

### Deep linking in email

See [Branch's documentation](https://docs.branch.io/pages/integrations/braze/) to set up deep linking from emails sent through Braze.

Depending on your ESP, additional customization may be required to support click-tracked universal links:

- [SendGrid][5]
- [Mailjet][6]
- [Sparkpost][7]

[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://docs.branch.io/pages/deep-linking/universal-links/#search
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-customization
[5]: https://help.branch.io/using-branch/page/braze-sendgrid
[6]: https://help.branch.io/using-branch/page/braze-mailjet
[7]: https://help.branch.io/using-branch/page/braze-sparkpost