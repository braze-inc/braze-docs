---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour macOS
platform: MacOS
page_order: 0
page_type: reference
description: "Cet article de référence fournit des ressources pour l’intégration initiale du SDK Braze sur macOS."
search_rank: 1
---

# Configuration initiale du SDK

> Cet article de référence explique comment installer le SDK Braze pour MacOS. 

À partir de la version [3,32,0][1], le SDK Braze prend en charge macOS pour les applications utilisant [Mac Catalyst][2] lors de l’intégration via le Gestionnaire de paquets Swift. Actuellement, le SDK ne prend pas en charge Mac Catalyst lors de l’utilisation de Cocoapods ou de Carthage.

{% alert note %}
Pour créer votre application avec Mac Catalyst, consultez la <a href="https://developer.apple.com/documentation/uikit/mac_catalyst">Documentation d’Apple</a>.
{% endalert %}

Une fois que votre application prend en charge Catalyst, suivez [ces instructions pour utiliser le gestionnaire de paquets Swift][3] pour importer le SDK Braze dans votre application.

## Fonctions prises en charge

Braze prend en charge les [notifications push][4], les [cartes de contenu][7], les [messages in-app][5], et le [recueil automatique de la localisation][5] lors de l’exécution sur Mac Catalyst.

Notez que Push Stories, Rich Push et Geofences ne sont pas pris en charge sur macOS.

[1]:https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.32.0
[2]:https://developer.apple.com/mac-catalyst/
[3]:{{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/
[4]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[5]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
