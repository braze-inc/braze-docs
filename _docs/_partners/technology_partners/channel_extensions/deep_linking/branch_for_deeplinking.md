---
nav_title: Branch
alias: /partners/branch_for_deeplinking/
---
# Branch

[Branch][1], a mobile linking platform, helps you acquire, engage, and measure across all devices, channels, and platforms by providing a holistic view of all user touch points	Branch and Braze team to allow you to provide better experiences to your customers through allowing you to properly attribute the beginning of their user journey & connect them through deeplinks to the their intended location

## Install Attribution {#branch-install-attribution}

Branch offers an install attribution feature to measure user acquisition. See our [Attribution documentation][2] for integration instructions.

## Deep Linking

Follow Branch's SDK Integration Guide to get up and running with your Branch and Braze integration. For additional use cases, see below.

## Supporting iOS Universal Links

To support sending iOS Universal Links as deep links from within Braze:

1. Follow [Branch's documentation for setting up Universal Links][3].
2. Add `ABKURLDelegate` to your Braze SDK integration to route Universal Links from within your app. See our [Linking Customization documentation][4] for implementation details.

## Deep Linking in Email

To set up deep linking from emails sent through Braze, see [Branch's documentation](https://docs.branch.io/pages/integrations/braze/).

Depending on your ESP, additional customization is required in order to support click-tracked Universal Links:

- [SendGrid][5]
- [Mailjet][6]


[1]: https://branch.io/
[2]: {{ site.baseurl }}/partners/branch_for_attribution/
[3]: https://dev.branch.io/getting-started/universal-app-links/overview/
[4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-customization
[5]: https://dev.branch.io/marketing-channels/sendgrid/overview/
[6]: https://dev.branch.io/marketing-channels/mailjet/overview/
