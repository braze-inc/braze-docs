---
nav_title: 統合の概要
article_title: スウィフトSDKのインテグレーション概況
platform: Swift
page_order: 0
layout: featured
search_rank: 3

guide_top_header: "スウィフトSDKのインテグレーション概況"
guide_top_text: "Braze Swift SDKをインストールすると、基本的な分析機能(セッション処理)と基本的なアプリ内メッセージが提供されます。追加のチャネルと機能のために統合をさらにカスタマイズする必要があります。<br> <br> Braze Swift SDKは、Swift Package Manager またはCocoaPod を使用してインストールまたは更新できます。"
description: "このランディングページでは、Swift Package Manager、CocoaPodsなどのBraze SDKインテグレーションガイドを紹介します。"

guide_featured_title: "基本的な統合オプション"
guide_featured_list:
- name: Swift Package Manager (サービスプロバイダーM)
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/braze_icons/swift.svg
- name: CocoaPods
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: 手動統合
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/
  image: /assets/img/braze_icons/tool-01.svg
- name: "統合の完了"
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/flag-05.svg

---

<br>

> 以前のObjective-C SDKからSwift iOS SDKにアップグレードすることをお考えですか?簡単です。詳細については、[マイグレーションガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)を参照してください。

リストされているオプションのいずれかを使用して統合した後、[のステップsに従って統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)を完了し、他のSDKのカスタマイズ(オプション)を有効にすると、将来のキャンペーンsのニーズに合わせて追加のチャネルsと機能を統合、有効化、およびカスタマイズできます。  

{% alert note %} Carthage は、Swift iOS SDKのパッケージマネージャーとしてサポートされていません。 {% endalert %}

<br>

