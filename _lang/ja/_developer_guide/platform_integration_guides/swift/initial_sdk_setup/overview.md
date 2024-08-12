---
nav_title: 統合の概要
article_title: Swift SDKの統合の概要
platform: Swift
page_order: 0
layout: featured
search_rank: 3

guide_top_header: "Swift SDKの統合の概要"
guide_top_text: "Braze iOS SDK をインストールすると、基本的な分析機能 (セッション処理) と基本的なアプリ内メッセージが提供されます。追加のチャネルと機能のために統合をさらにカスタマイズする必要があります。<br> <br> Braze Swift SDKは、Swift Package ManagerまたはCocoaPodsを使用してインストールまたは更新できます。"
description: "このランディングページでは、Swift Package ManagerやCocoaPodsなどのBraze SDK統合ガイドを紹介しています。"

guide_featured_title: "基本的な統合オプション"
guide_featured_list:
- name: Swift Package Manager (SPM)
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/swift.png
- name: CocoaPods
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Manual Integration
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/
  fa_icon: fas fa-toolbox
- name: "Completing the Integration"
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/
  fa_icon: fas fa-flag-checkered

---

<br>

> 古い Objective-C SDK から Swift iOS SDK へのアップグレードをお考えですか?簡単です。詳細については、 [移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/) をご覧ください。

リストされたオプションのいずれかを使用して統合し、 [統合を完了する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)ための手順に従い、他の SDK のカスタマイズ(オプション)を有効にしたら、将来のキャンペーンのニーズに合わせて追加のチャネルと機能を統合、有効化、カスタマイズできます。  

{% alert note %} Carthage は、Swift iOS SDK のパッケージ マネージャーとしてサポートされていません。 {% endalert %}

<br>

