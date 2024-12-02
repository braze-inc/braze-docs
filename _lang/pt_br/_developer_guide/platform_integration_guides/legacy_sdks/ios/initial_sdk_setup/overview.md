---
nav_title: Visão geral
article_title: Visão geral da integração para iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Visão Geral da Integração"
guide_top_text: ""
description: "Esta landing page cobre os guias de integração do SDK da Braze para CocoaPods, Swift Package Manager, Carthage e mais."

guide_featured_title: "Opções básicas de integração"
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
- name: "Concluindo a integração"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/flag-05.svg
- name: "Outras personalizações opcionais do SDK"
  link: /docs/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/ios_sdk_integration
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

Instalar o SDK iOS da Braze fornecerá a você funcionalidades básicas de análise de dados (manipulação de sessões) e mensagens básicas no app. Você deve personalizar ainda mais sua integração para canais e recursos adicionais. <br> <br> O SDK da Braze para iOS pode ser instalado ou atualizado usando CocoaPods, Carthage, Swift Package Manager ou uma integração manual. <br> <br> Além disso, o SDK da Braze para iOS oferece suporte integral para aplicativos RubyMotion.

{% alert important %}
O SDK do iOS adicionará 1 MB a 2 MB ao arquivo IPA do app, além de um arquivo app, e 30 MB para o framework.
{% endalert %}

Depois de fazer a integração usando uma das opções listadas, seguir os passos para [completar a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/) e habilitar outras personalizações do SDK (opcional), prossiga para integrar, habilitar e personalizar canais e recursos adicionais para atender às necessidades de suas futuras campanhas.  

<br>
