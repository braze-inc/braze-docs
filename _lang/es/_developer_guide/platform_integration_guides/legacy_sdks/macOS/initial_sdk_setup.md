---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para MacOS
platform: MacOS
page_order: 0
page_type: reference
description: "En este artículo de referencia se proporcionan recursos para la integración inicial del SDK de Braze en macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración inicial del SDK

> En este artículo de referencia se explica cómo instalar el SDK de Braze para MacOS. 

A partir de la versión [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), el SDK de Braze es compatible con macOS para aplicaciones que utilicen [Mac Catalyst](https://developer.apple.com/mac-catalyst/) al integrarse a través de Swift Package Manager. Actualmente, el SDK no es compatible con Mac Catalyst cuando se utilizan CocoaPods o Carthage.

{% alert note %}
Para crear tu aplicación con Mac Catalyst, consulta <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">la documentación de Apple.</a>
{% endalert %}

Una vez que tu aplicación sea compatible con Catalyst, sigue [estas instrucciones para utilizar Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) para importar el SDK de Braze a tu aplicación.

## Características compatibles

Braze es compatible con [notificaciones push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/), [tarjetas de contenido]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/#content-cards-data-model), [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/) y [recogida automática de ubicaciones]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/) cuando se ejecuta en Mac Catalyst.

Ten en cuenta que las historias push, las notificaciones push enriquecidas y las geovallas no son compatibles con macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
