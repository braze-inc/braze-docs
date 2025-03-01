---
nav_title: Übersicht
article_title: Integrationsübersicht für iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Überblick über die Integration"
guide_top_text: ""
description: "Auf dieser Startseite finden Sie Anleitungen zur Braze SDK-Integration für CocoaPods, Swift-Paketmanager, Carthage und mehr."

guide_featured_title: "Grundlegende Integrationsmöglichkeiten"
guide_featured_list:
- name: CocoaPods
  link: /developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Swift-Paketmanager (SPM)
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/braze_icons/swift.svg
- name: Karthago
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/
  image: /assets/img/carthage.png
- name: Manuell
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/
  image: /assets/img/braze_icons/tool-01.svg
- name: "Fertigstellung der Integration"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/flag-05.svg
- name: "Andere optionale SDK-Anpassungen"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/ios_sdk_integration
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

Durch die Installation des Braze iOS-SDK erhalten Sie grundlegende Analytics-Funktionen (Sitzungsverarbeitung) sowie grundlegende In-App-Nachrichten. Für zusätzliche Kanäle und Features müssen Sie die Integration weiter anpassen. <br> <br> Das Braze iOS-SDK kann mit CocoaPods, Carthage, Swift-Paketmanager oder einer manuellen Integration installiert oder aktualisiert werden. <br> <br> Außerdem bietet das Braze iOS-SDK vollständige Unterstützung für RubyMotion-Apps.

{% alert important %}
Zusätzlich zu einer APP-Datei fügt das iOS-SDK der IPA-Datei der App 1 bis 2 MB hinzu. Für das Framework kommen weitere 30 MB hinzu.
{% endalert %}

Nachdem Sie die Integration mit einer der aufgelisteten Optionen durchgeführt, die Schritte zur [Fertigstellung der Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/) befolgt und andere SDK-Anpassungen aktiviert haben (optional), fahren Sie mit der Integration, Aktivierung und Anpassung weiterer Kanäle und Funktionen fort, um sie an die Anforderungen Ihrer zukünftigen Kampagnen anzupassen.  

<br>
