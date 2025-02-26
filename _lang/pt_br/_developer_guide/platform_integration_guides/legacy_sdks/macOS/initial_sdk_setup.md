---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "Este artigo de referência oferece recursos para a integração inicial do SDK da Braze no macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuração inicial do SDK

> Este artigo de referência ensina como instalar o SDK da Braze para macOS. 

A partir da versão [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), o SDK da Braze é compatível com macOS para apps que usam [Mac Catalyst](https://developer.apple.com/mac-catalyst/) com integração pelo Swift Package Manager. No momento, o SDK não é compatível com o Mac Catalyst ao usar CocoaPods ou Carthage.

{% alert note %}
Para criar seu app com o Mac Catalyst, consulte a <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">documentação da Apple</a>.
{% endalert %}

Depois que seu app for compatível com o Catalyst, siga [estas instruções para usar o Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) para importar o SDK da Braze para o seu app.

## Recursos compatíveis

A Braze oferece [notificações por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), [cartões de conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/#content-cards-data-model), [mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/) e [coleta automática de localização]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/) quando executada no Mac Catalyst.

Vale ressaltar que o macOS é incompatível com stories por push, rich push e geofences.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
