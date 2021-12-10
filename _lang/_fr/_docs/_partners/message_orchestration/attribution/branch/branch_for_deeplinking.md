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

> [Branch][1], a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touchpoints. This article will walk you through how to use Branch with Braze to support your deep linking needs.

Branch, with Braze, allows you to provide better experiences to your customers by allowing you to properly attribute the beginning of their user journey & connect them through deep links to their intended location.

Branch and Braze help you understand exactly when and where users were acquired as well as how to personalize their journeys through robust [attribution]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) and deep linking.


## Install attribution {#branch-install-attribution}

Branch offers an install attribution feature to measure user acquisition. See our [Attribution documentation][2] for integration instructions.

## Deep linking

Follow Branch's SDK Integration Guide to get up and running with your Branch and Braze integration. For additional use cases, see below.

## Supporting iOS universal links

To support sending iOS Universal Links as deep links from within Braze:

1. Follow [Branch's documentation for setting up Universal Links][3].
2. Add `ABKURLDelegate` to your Braze SDK integration to route Universal Links from within your app. See our [Linking Customization documentation][4] for implementation details.

## Deep linking in email

To set up deep linking from emails sent through Braze, see [Branch's documentation](https://docs.branch.io/pages/integrations/braze/).

Depending on your ESP, additional customization is required to support click-tracked Universal Links:

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
