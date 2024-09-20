---
nav_title: Aperçu
article_title: Aperçu de l’intégration pour iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Aperçu de l’intégration"
guide_top_text: "L’installation du SDK Braze pour iOS vous offrira des fonctionnalités d’analyse de base (gestion de session) et des messages in-app de base. Vous devez davantage personnaliser votre intégration pour plus de canaux et de fonctionnalités. <br> <br> Le SDK Braze pour iOS peut être installé ou mis à jour à l’aide des champs Cocoapods, Carthage, Gestionnaire de paquets Swift ou d’une intégration manuelle. <br> <br> De plus, le SDK Braze pour iOS prend en charge les applications RubyMotion."
description: "Cette page d’accueil couvre les guides d’intégration SDK de Braze pour Cocoapods, le Gestionnaire de paquets Swift, Carthage, etc."

guide_featured_title: "Options d’intégration de base"
guide_featured_list:
- name: CocoaPods
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Gestionnaire de paquets Swift (SPM)
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
  image: /assets/img/braze_icons/swift.svg
- name: Carthage
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/
  image: /assets/img/carthage.png
- name: Manual (Manuel)
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/
  image: /assets/img/braze_icons/tool-02.svg
- name: "Terminer l’intégration"
  link: /docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/
  image: /assets/img/braze_icons/check-done-01.svg
- name: "Autres personnalisations SDK facultatives"
  link: /docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/
  image: /assets/img/braze_icons/user-square.svg

---

{% multi_lang_include deprecations/objective-c.md %}

<br>

{% alert important %}
Le SDK iOS ajoutera 1 Mo à 2 Mo au fichier IPA App, en plus d’un fichier APP et 30 Mo pour l’infrastructure.
{% endalert %}

Après avoir effectué l’intégration en utilisant l’une des options répertoriées, suivez les étapes pour [compléter l’intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/) et activez d’autres personnalisations SDK (en option), passez à l’intégration, en activant la personnalisation d’autres canaux et fonctionnalités pour répondre aux besoins de vos futures campagnes.  

<br>
