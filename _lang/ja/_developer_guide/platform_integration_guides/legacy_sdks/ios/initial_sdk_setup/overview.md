---
nav_title: 概要
article_title: iOS の統合の概要
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "統合の概要"
guide_top_text: ""
description: "このランディングページでは、CocoaPods、Swift Package Manager、Carthage などの Braze SDK 統合ガイドについて説明します。"

guide_featured_title: "基本的な統合オプション"
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

noindex: true
---
<br>

{% multi_lang_include archive/objective-c-deprecation-notice.md %}

Braze iOS SDK をインストールすると、基本的な分析機能 (セッション処理) と基本的なアプリ内メッセージが提供されます。追加のチャネルと機能のために統合をさらにカスタマイズする必要があります。<br> <br> Braze iOS SDK は、CocoaPods、Carthage、Swift Package Manager、または手動統合を使用してインストールまたは更新できます。<br> <br> さらに、Braze iOS SDK はRubyMotion アプリを完全にサポートしています。

{% alert important %}
iOS SDK は、APP ファイルに加えて、アプリの IPA ファイルに 1 MB から 2 MB、フレームワークに 30 MB を追加します。
{% endalert %}

リストされているオプションのいずれかを使用して統合し、[統合を完了する]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/)ための手順に従って、他の SDK のカスタマイズ (オプション) を有効にしたら、今後のキャンペーンのニーズに合わせて追加のチャネルと機能の統合、有効化、カスタマイズに進みます。  

<br>
