---
nav_title: Resumen
article_title: Resumen de integración para iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Resumen de la integración"
guide_top_text: ""
description: "Esta página de inicio cubre las guías de integración de SDK de Braze para CocoaPods, Swift Package Manager, Carthage y más."

guide_featured_title: "Opciones básicas de integración"
guide_featured_list:
- name: CocoaPods
  link: /developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Swift Package Manager (SPM)
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/braze_icons/swift.svg
- name: Carthage
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/
  image: /assets/img/carthage.png
- name: Manual
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/
  image: /assets/img/braze_icons/tool-01.svg
- name: "Completar la integración"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/flag-05.svg
- name: "Otras personalizaciones opcionales del SDK"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/ios_sdk_integration
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

La instalación del SDK Braze para iOS te proporcionará una funcionalidad básica de análisis (gestión de sesiones) y mensajes dentro de la aplicación. Debes personalizar aún más tu integración para canales y características adicionales. <br> <br> El SDK Braze para iOS puede instalarse o actualizarse mediante CocoaPods, Carthage, Swift Package Manager o una integración manual. <br> <br> Además, el SDK de Braze para iOS es totalmente compatible con las aplicaciones RubyMotion.

{% alert important %}
El SDK de iOS añadirá de 1 MB a 2 MB al archivo IPA de la aplicación, además de un archivo APP, y 30 MB para el framework.
{% endalert %}

Una vez que te hayas integrado utilizando una de las opciones de la lista, hayas seguido los pasos para [completar la integración]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/) y hayas habilitado otras habilitaciones del SDK (opcional), pasa a integrar, habilitar y personalizar canales y características adicionales que se ajusten a las necesidades de tus futuras campañas.  

<br>
