---
nav_title: Overview
article_title: Integration Overview for iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Integration Overview"
guide_top_text: ""
description: "This landing page covers Braze SDK integration guides for CocoaPods, Swift Package Manager, Carthage, and more."

guide_featured_title: "Basic integration options"
guide_featured_list:
- name: CocoaPods
  link: /developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Swift Package Manager (SPM)
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/
  image: /assets/img/braze_icons/swift.svg
- name: Carthage
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/
  image: /assets/img/carthage.png
- name: Manual
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/
  image: /assets/img/braze_icons/tool-01.svg
- name: "Completing the Integration"
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/
  image: /assets/img/braze_icons/flag-05.svg
- name: "Other Optional SDK Customizations"
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

Installing the Braze iOS SDK will provide you with basic analytics functionality (session handling) and basic in-app messages. You must further customize your integration for additional channels and features. <br> <br> The Braze iOS SDK can be installed or updated using CocoaPods, Carthage, Swift Package Manager, or a Manual integration. <br> <br> Additionally, the Braze iOS SDK fully supports RubyMotion apps.

{% alert important %}
The iOS SDK will add 1&nbsp;MB to 2&nbsp;MB to the app IPA file, in addition to an APP File, and 30&nbsp;MB for the framework.
{% endalert %}

After you have integrated using one of the listed options, followed the steps for [completing the integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/), and enabled other SDK customizations (optional), move on to integrating, enabling, and customizing additional channels and features to fit the needs of your future campaigns.  

<br>
