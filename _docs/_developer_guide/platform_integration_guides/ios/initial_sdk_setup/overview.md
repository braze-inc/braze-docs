---
nav_title: Overview
article_title: Integration Overview for iOS
platform: iOS
page_order: 0
layout: featured

guide_top_header: "Integration Overview"
guide_top_text: "Installing the Braze iOS SDK will provide you with basic analytics functionality (session handling) and basic in-app messages. You must further customize your integration for additional channels and features. <br> <br> The Braze iOS SDK can be installed or updated using CocoaPods, Carthage, Swift Package Manager, or a Manual integration."
description: "This landing page covers Braze SDK integration guides for CocoaPods, Swift Package Manager, Carthage, and more."

guide_featured_title: "Basic Integration Options"
guide_featured_list:
- name: CocoaPods
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Swift Package Manager (SPM)
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/swift.png
- name: Carthage
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/
  image: /assets/img/carthage.jpeg
- name: Manual
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/
  fa_icon: fas fa-toolbox
- name: "Completing the Integration"
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/
  fa_icon: fas fa-flag-checkered
- name: "Other Optional SDK Customizations"
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/
  fa_icon: fas fa-id-card-alt

---

<br>

{% alert important %}
The iOS SDK will add 1MB to 2MB to the app IPA file, in addition to an APP File, and 30MB for the framework.
{% endalert %}

After you have integrated using one of the listed options, followed the steps for [completing the integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/), and enabled other SDK customizations (optional), move on to integrating, enabling, and customizing additional channels and features to fit the needs of your future campaigns.  

<br>
