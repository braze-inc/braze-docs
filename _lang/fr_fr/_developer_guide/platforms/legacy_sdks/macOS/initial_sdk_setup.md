---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour macOS
platform: MacOS
page_order: 0
page_type: reference
description: "Cet article de référence fournit des ressources pour l’intégration initiale du SDK Braze sur macOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuration initiale du SDK

> Cet article de référence explique comment installer le SDK Braze pour MacOS. 

À partir de la version [3.32.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0), le SDK Braze prend en charge macOS pour les applications utilisant [Mac Catalyst](https://developer.apple.com/mac-catalyst/) lors de l’intégration via le Gestionnaire de paquets Swift. Actuellement, le SDK ne prend pas en charge Mac Catalyst lors de l’utilisation de Cocoapods ou de Carthage.

{% alert note %}
Pour créer votre application avec Mac Catalyst, consultez la <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Documentation d’Apple</a>.
{% endalert %}

Une fois que votre application prend en charge Catalyst, suivez [ces instructions pour utiliser le gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/) pour importer le SDK Braze dans votre application.

## Fonctions prises en charge

Braze prend en charge les [notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), les [cartes de contenu]({{site.baseurl}}/developer_guide/platforms/swift/content_cards/#content-cards-data-model), les [messages in-app]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift) et la [collecte automatique d'emplacements]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift) lors de l'exécution sur Mac Catalyst.

Notez que Push Stories, Rich Push et Géorepérages ne sont pas pris en charge sur macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
