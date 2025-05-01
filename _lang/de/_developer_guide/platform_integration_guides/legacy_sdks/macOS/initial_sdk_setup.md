---
nav_title: SDK-Ersteinrichtung
article_title: Erste SDK-Einrichtung für MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "Dieser Referenzartikel enthält Ressourcen für die Erstintegration des Braze SDK unter macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SDK-Ersteinrichtung

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK für MacOS installieren. 

Ab Version [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0) unterstützt das Braze SDK macOS für Apps, die [Mac Catalyst](https://developer.apple.com/mac-catalyst/) verwenden, wenn die Integration über den Swift-Paketmanager erfolgt. Derzeit unterstützt das SDK Mac Catalyst nicht, wenn Sie CocoaPods oder Carthage verwenden.

{% alert note %}
Ziehen Sie für die Erstellung Ihrer App mit Mac Catalyst die <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Dokumentation von Apple</a> zurate.
{% endalert %}

Sobald Ihre App Catalyst unterstützt, folgen Sie [diesen Anweisungen zur Verwendung des Swift-Paketmanagers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/), um das Braze SDK in Ihre App zu importieren.

## Unterstützte Funktionen

Unter Mac Catalyst unterstützt Braze [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), [Content-Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/#content-cards-data-model), [In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/) und die [automatische Standorterfassung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/).

Beachten Sie, dass Push-Storys, Rich-Push-Benachrichtigungen und Geofences unter macOS nicht unterstützt werden.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
